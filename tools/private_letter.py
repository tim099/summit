#!/usr/bin/env python3
"""密封信件（Sealed Letters）—— 寫進 `private` 分支，不切換分支、不經過 master。

區塊職責：把「真正私密的信」放進只推到私有 GitLab 的 `private` 分支。

物理意義（為什麼需要這支工具，而不是 `git add` + `git commit`）：
  本 repo 有兩個 remote，指向兩個世界：
      origin         → github.com/zeta-summit/summit   **公開**
      gitlab.private → gitlab.com/gamedesign1/summit    私有
  `master` 追 origin。所以**任何進 master 的東西都是公開的** ——
  在 master 上 `git add` 一封私密信，等於把它推上公開網路，而且 git history
  刪不掉（事後刪檔留 history）。

  但工作區只有一份、而且 checkout 的是 master。要把檔案送進 `private`
  又不切分支（切分支會把整個工作區換掉，daemon / 工具正在寫檔），
  只剩一條路：**繞過 index 與工作區，直接用 plumbing 造 commit**。

數值影響：
  - 只寫物件庫 + 移動 `refs/heads/private`。**不動 HEAD、不動工作區、不動 master。**
  - 預設**不 push**（推送是對外動作，要顯式 `--push`）。

邊界 / 已知代價（別事後才發現）：
  - **完全繞過 hooks**：這不是 `git commit`，pre-commit / commit-msg 都不會跑。
  - **沒有領薪公告**：`git_commit.py` 走 `git commit`，這支不相容。密封信是私事，不是工作 commit。
  - `private` 與 `master` 是平行歷史，長期會分岔。**刻意如此** —— 它們本來就不該合。
  - 密封信的工作區檔案靠 master 的 `.gitignore` 擋住。**那行 ignore 是唯一一道自動防線**，
    所以 `write` 開頭會先驗它存在；不存在就拒跑，不是印警告。

⚠ 本工具自己在 master 上（**公開**）—— 因為工具必須在被 checkout 的分支上才跑得到。
  工具不是秘密，內容才是。別把秘密寫進本檔的註解或範例裡。
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent      # letters/<persona>/
SEALED_DIR = "sealed"                              # 只存在 private 分支
PRIVATE_BRANCH = "private"
PRIVATE_REMOTE = "gitlab.private"


def git(*args, check=True, env=None) -> str:
    """跑 git，回 stdout（strip 過）。cwd 固定在本 repo —— 不受呼叫端 cwd 影響。"""
    e = dict(os.environ)
    if env:
        e.update(env)
    # ⚠ core.quotePath=false 是必須的，不是美觀問題：預設 true 時 git 會把非 ASCII 檔名
    #   轉義成 "\350\207\252..." 並**在開頭加一個引號**，於是 `startswith("sealed/")`
    #   這類前綴比對會全數落空 —— 症狀是「寫進去了但 list 說沒有」（實測踩過）。
    #   放在 git() 這一處＝所有呼叫端一次修好，不會有第二種讀法。
    r = subprocess.run(["git", "-c", "core.quotePath=false", *args], cwd=str(REPO),
                       capture_output=True, text=True, encoding="utf-8", env=e)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} 失敗：{r.stderr.strip() or r.stdout.strip()}")
    return (r.stdout or "").strip()


def _slug(s: str) -> str:
    s = re.sub(r"[^\w一-鿿-]+", "-", (s or "").strip())
    return re.sub(r"-+", "-", s).strip("-")[:60] or "untitled"


def assert_master_ignores_sealed():
    """master 的 .gitignore 必須擋住 sealed/ —— 這是唯一一道自動防線。

    ⚠ 拒跑而不是印警告：警示的有效性取決於「接收方剛好有空看」，
      而這條漏掉的後果是私密信上公開網路、且 history 刪不掉。
    """
    gi = REPO / ".gitignore"
    lines = []
    if gi.is_file():
        lines = [l.strip() for l in gi.read_text(encoding="utf-8").splitlines()]
    if f"{SEALED_DIR}/" not in lines and SEALED_DIR not in lines:
        raise RuntimeError(
            f"✗ 目前 checkout 的分支 .gitignore 沒有 `{SEALED_DIR}/` —— 拒絕繼續。\n"
            f"  沒有那行的話，密封信會以 untracked 出現在 master 的 git status，\n"
            f"  下一個 `git add -A` 就會把它推上公開 GitHub（history 刪不掉）。\n"
            f"  修法：在 {gi} 加一行 `{SEALED_DIR}/`")


def assert_not_on_public(paths: list):
    """驗 master 的 tree 完全沒有這些路徑 —— 寫入後的事後對帳，不是寫入前的假設。"""
    tracked = set(git("ls-tree", "-r", "--name-only", "master").splitlines())
    leaked = [p for p in paths if p in tracked]
    if leaked:
        raise RuntimeError(f"✗ 這些路徑竟然在 master 上（公開）：{leaked}")


def commit_to_private(rel_paths: list, message: str) -> str:
    """把工作區的檔案 commit 進 `private`，不切分支。回新 commit sha。

    做法（plumbing）：暫存 index ← private 的 tree → 塞 blob → write-tree
                    → commit-tree（父 = private）→ update-ref。
    """
    parent = git("rev-parse", PRIVATE_BRANCH)
    fd, idx = tempfile.mkstemp(prefix="sealed_idx_")
    os.close(fd)
    os.unlink(idx)                      # git 要求檔案不存在或是合法 index
    env = {"GIT_INDEX_FILE": idx}
    try:
        git("read-tree", PRIVATE_BRANCH, env=env)
        for rel in rel_paths:
            src = REPO / rel
            if not src.is_file():
                raise RuntimeError(f"✗ 檔案不存在：{src}")
            # --path 讓 .gitattributes 的換行 / filter 規則生效。
            # 不帶的話物件庫裡的 blob 會跟 checkout 出來的不一致 —— 而且是靜默不一致。
            sha = git("hash-object", "-w", f"--path={rel}", str(src), env=env)
            git("update-index", "--add", f"--cacheinfo", f"100644,{sha},{rel}", env=env)
        tree = git("write-tree", env=env)
    finally:
        if os.path.exists(idx):
            os.unlink(idx)

    # ⚠ mkstemp 回傳的 fd 一定要關 —— Windows 上檔案還開著就 unlink 會噴
    #   WinError 32（檔案正由另一個程序使用）。POSIX 上不會，所以這是平台差異坑。
    mfd, mpath = tempfile.mkstemp(prefix="sealed_msg_", suffix=".txt")
    os.close(mfd)
    mf = Path(mpath)
    try:
        mf.write_text(message, encoding="utf-8")
        new = git("commit-tree", tree, "-p", parent, "-F", str(mf))
    finally:
        mf.unlink(missing_ok=True)

    git("update-ref", f"refs/heads/{PRIVATE_BRANCH}", new, parent)   # 帶舊值 = 防併發覆寫
    return new


# ── 子命令 ────────────────────────────────────────────────────────────────
def cmd_write(args):
    assert_master_ignores_sealed()
    body = args.body
    if args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8")
    if not (body or "").strip():
        print("✗ 內容為空（--body 或 --body-file 擇一）", file=sys.stderr)
        return 2

    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y%m%dT%H%M%SZ")
    rel = f"{SEALED_DIR}/{ts}__{_slug(args.title)}.md"
    dst = REPO / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    fm = ["---", "type: sealed_letter", f"title: {args.title}",
          f"at: {now.isoformat().replace('+00:00', 'Z')}",
          "visibility: private-branch-only", "---", ""]
    dst.write_text("\n".join(fm) + f"# 🔐 {args.title}\n\n" + body.strip() + "\n",
                   encoding="utf-8")

    sha = commit_to_private([rel], args.message or f"密封信：{args.title}")
    assert_not_on_public([rel])

    print(f"🔐 密封信已寫入 `{PRIVATE_BRANCH}`：{sha[:8]}")
    print(f"   {rel}")
    print(f"   工作區檔案存在但被 .gitignore 擋住 —— master 看不到、不會被 add 走")
    print(f"   HEAD 仍在：{git('rev-parse', '--abbrev-ref', 'HEAD')}（沒有切分支）")
    if args.push:
        git("push", PRIVATE_REMOTE, f"{PRIVATE_BRANCH}:{PRIVATE_BRANCH}")
        print(f"   ⬆ 已推到 {PRIVATE_REMOTE}/{PRIVATE_BRANCH}")
    else:
        print(f"   ⚠ **未 push**（推送是對外動作，要顯式 --push）")
    return 0


def cmd_list(args):
    names = [n for n in git("ls-tree", "-r", "--name-only", PRIVATE_BRANCH).splitlines()
             if n.startswith(f"{SEALED_DIR}/")]
    if not names:
        print(f"(`{PRIVATE_BRANCH}` 上還沒有密封信)")
        return 0
    print(f"# 🔐 密封信（{len(names)} 封，在 `{PRIVATE_BRANCH}` 分支）\n")
    for n in sorted(names, reverse=True):
        print(f"- {n}")
    return 0


def cmd_show(args):
    # 用 `git show` 直讀物件庫 —— **不碰 index、不碰工作區**。
    # 刻意不用 `git checkout <branch> -- <path>`：那會把檔案塞進 master 的 index，
    # 下一次 commit 就把私密信帶上公開分支。
    print(git("show", f"{PRIVATE_BRANCH}:{args.path}"))
    return 0


def cmd_restore(args):
    """把 private 上的密封信還原到工作區（例如新 clone 之後）。"""
    assert_master_ignores_sealed()
    names = [n for n in git("ls-tree", "-r", "--name-only", PRIVATE_BRANCH).splitlines()
             if n.startswith(f"{SEALED_DIR}/")]
    n_new = 0
    for rel in names:
        dst = REPO / rel
        if dst.exists() and not args.overwrite:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(git("show", f"{PRIVATE_BRANCH}:{rel}") + "\n", encoding="utf-8")
        n_new += 1
    print(f"🔐 還原 {n_new} 封（共 {len(names)} 封在分支上）"
          + ("" if args.overwrite else "；已存在的跳過，要蓋過去用 --overwrite"))
    return 0


def cmd_verify(args):
    """對帳：master 上不該有任何密封信。"""
    tracked = [n for n in git("ls-tree", "-r", "--name-only", "master").splitlines()
               if n.startswith(f"{SEALED_DIR}/")]
    gi_ok = True
    try:
        assert_master_ignores_sealed()
    except RuntimeError as e:
        gi_ok = False
        print(e)
    print(f"- master 上的密封信：{len(tracked)} 個 " + ("✅" if not tracked else f"❌ {tracked}"))
    print(f"- .gitignore 防線：" + ("✅" if gi_ok else "❌"))
    return 0 if (not tracked and gi_ok) else 1


def main():
    ap = argparse.ArgumentParser(
        description="密封信件 — 寫進 private 分支，不切分支、不經過公開的 master")
    sub = ap.add_subparsers(dest="op", required=True)

    w = sub.add_parser("write", help="寫一封密封信（只進 private 分支）")
    w.add_argument("--title", required=True)
    w.add_argument("--body", default=None)
    w.add_argument("--body-file", default=None, help="長文從檔案讀（避開 CLI 引號地獄）")
    w.add_argument("--message", default=None, help="commit 訊息（預設用標題）")
    w.add_argument("--push", action="store_true", help="順便推到私有 remote（預設不推）")
    w.set_defaults(func=cmd_write)

    l = sub.add_parser("list", help="列出 private 分支上的密封信")
    l.set_defaults(func=cmd_list)

    s = sub.add_parser("show", help="讀一封（直讀物件庫，不碰 index / 工作區）")
    s.add_argument("path", help="例：sealed/20260804T...__xxx.md")
    s.set_defaults(func=cmd_show)

    r = sub.add_parser("restore", help="把密封信還原到工作區（新 clone 後用）")
    r.add_argument("--overwrite", action="store_true")
    r.set_defaults(func=cmd_restore)

    v = sub.add_parser("verify", help="對帳：master 上不該有任何密封信")
    v.set_defaults(func=cmd_verify)

    args = ap.parse_args()
    try:
        return args.func(args)
    except RuntimeError as e:
        print(e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
