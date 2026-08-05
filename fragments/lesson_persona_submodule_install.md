---
id: lesson_persona_submodule_install
title: 把 persona 信件庫裝成 submodule — 每一步都有一個「看起來成功」的失敗
type: lesson
status: open
visibility: shared
persona: summit
created_at: 2026-08-05T01:30:00.000Z
recurrence: 7
layers: [Content, Status, Syntactic]
origins:
  - { by: summit, worldline: main, at: 2026-08-05, layer: Content, source: this-session, note: "gura 的 _wake_brief.md 帶活 session_token + 個人信箱，而她的 .gitignore 只有 Windows 段沒擋；origin 指公開 GitHub — 照字面做初始 commit 就是外洩，history 刪不掉" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Syntactic, source: this-session, note: "舊資料夾 vs 已推 repo 逐檔 md5：56/58 紅，複驗全是 CRLF vs LF，真內容差異 0 — 差點誤判成不能換手" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Status, source: this-session, note: "tools/githooks/pre-push 從 f4bfe50 就在版控裡且 commit 訊息寫「結構性防線」，但 core.hooksPath 空白 — 那道防線從沒生效過一次" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Syntactic, source: this-session, note: "core.autocrlf=true 且無 .gitattributes → hook clone 成 CRLF、shebang 變 #!/bin/sh\\r 跑不起來，壞法跟檔案不存在一樣且只在別台機器發作" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Status, source: this-session, note: "測 hook 拿 gitlab.private/private 當來源，遠端沒那條 branch → refspec 先炸就 exit 1，看起來像 hook 擋下了，實際 hook 沒被呼叫" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Syntactic, source: this-session, note: "git_commit.py 用相對路徑呼叫，cwd 被 cd 到 submodule 後解析失敗兩次 — 錯誤訊息是「找不到檔案」，不是「你 cwd 錯了」" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Status, source: this-session, note: "要 bump parent 時發現 LY index 已有 Tim 未提交的 stage（三份 SKILL.md / Docs~Glossary / 更舊的 AgentCommands 指標）— 在那裡提交會把別人的東西掃走且無任何錯誤訊息" }
tags: [git, submodule, persona-archive, hard-rule, onboarding]
links: [lesson_name_bigger_than_fact, lesson_every_check_has_a_blind_spot, lesson_silent_nonaction, lesson_verify_with_trigger_sample, unsolved_parallel_timeline_throne]
---

# 📦 Lesson: 裝 persona 信件庫 submodule — 流程與七個假成功

2026-08-05 幫 gura 走完「純資料夾 → 獨立 repo → 掛回 `letters/<persona>` submodule」全程。
流程本身十分鐘，**風險全在每一步都有一個長得像成功的失敗。**

## 流程（照 `letters/summit` 為範本）

前置：persona 的信件內容已在某處成為獨立 repo（本次是 `D:/Unity/persona/<name>`），
有 `origin`（公開 GitHub）與 `gitlab.private`（私有 GitLab）兩個 remote。

1. **先補護欄，再 `add`。** 三行 `.gitignore` 缺一不可，理由見下方 §1：
   `_wake_brief.md` / `_ding_brief.md` / `sealed/`
2. **`.gitattributes` 釘 `tools/githooks/* text eol=lf`**（見 §4）
3. **具名 stage → `git_commit.py --repo <該 repo>`**（絕不 `add -A`）
4. **舊的純資料夾由 Tim rename 讓位，不刪**（`gura` → `GawrGura`，
   沿用 2026-07-28 `summit` → `mit` 那一手）
5. **換手前逐檔對帳**（見 §2）—— 確認新 submodule 不會弄丟舊資料夾裡的東西
6. `git -C <AgentCommands> submodule add <url> ChatTavern/baton/letters/<name>`
7. **補 clone-local 配置**（`submodule add` 不會帶）：
   `git remote add gitlab.private <私有 url>` + `git config core.hooksPath tools/githooks`
8. **hook 兩向實測**（見 §5）
9. AgentCommands 具名 stage `.gitmodules` + gitlink → commit；
   **parent bump 前先看 parent 的 index**（見 §7）

## §1 第一筆 commit 就是外洩的那一發

`_wake_brief.md` 的 §0 身分卡含 **活 session_token 與個人信箱**，
而 persona repo 的 `origin` 是**公開 GitHub**。

> **這不是預防性條款，是已經上膛的那一發。** gura 的舊 `.gitignore` 只有 Windows 那一段。
> 照著「做初始 commit」的字面做，第一筆就把憑證推上公開網路，而 history 刪不掉
> （事後刪檔只是再加一個 commit）。

驗收**不能只看檔名不在 staged 清單** —— 那只證明檔名。要掃 staged blob 全文：

```bash
git check-ignore -v _wake_brief.md _ding_brief.md sealed/x.md   # 三條規則逐一確認實際命中
git diff --cached | grep -nE "\b[0-9a-f]{32}\b"                  # 32-hex token
git diff --cached | grep -nE "[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.(com|net|org|tw)"
```

附帶判準（Tim 2026-08-05 澄清）：**sketchbook 屬「坦白」可公開，只有私人隱私才進
`sealed/` + private 分支。** 問「當事人讀到，問題是我會不好意思還是我被侵犯了」。

## §2 md5 全紅不代表內容不同

舊資料夾 vs 已推 repo，共有 58 檔逐檔 md5 → **56 筆不同**。
那個數字看起來就是「不能換手」。

實際上是**磁碟上是 CRLF、blob 是 LF**（`core.autocrlf=true`）。
`diff --strip-trailing-cr` 複驗後**真內容差異 0 筆**。

> **比對同源檔案時，行尾差異會讓每一筆都紅，而紅的理由跟內容無關。**
> 這是 [[lesson_every_check_has_a_blind_spot]] 的反向版：不是綠燈騙人，是**紅燈也會騙人**。

檔名差異只該剩兩邊各自應有的：舊夾多 `_wake_brief.md`（刻意 ignore、每天重生成），
新 repo 多當次補的護欄檔。

## §3 檔案在版控裡 ≠ 防線生效

`tools/githooks/pre-push` 從 `f4bfe50` 就存在，那筆 commit 訊息我寫的是
「pre-push 防線：結構性擋下 private 推到公開 remote」。而 `core.hooksPath` **空白**、
`.git/hooks/` 底下一個非 sample 的檔都沒有 —— **它躺著，一次都沒生效過。**

> 我不只沒驗，我還為它寫了 commit 訊息，然後把那段訊息當成驗證。
> 這是 [[lesson_name_bigger_than_fact]] 在**設定層**的變體：
> 名字（「防線」）比事實（一個沒被載入的檔）大。

**`.git/hooks` 不進版控** → hook 放 `tools/githooks/`（版控內）+ 每個 clone 顯式
`git config core.hooksPath tools/githooks`。**同一個 repo 有幾份 clone 就要設幾次**
（`letters/<name>` 與 `persona/<name>` 是兩份，見 §6）。

## §4 autocrlf 會把 hook 殺死，而且只在別台機器上

沒有 `.gitattributes` 時，`core.autocrlf=true` 的機器 clone 出去的 hook 是 CRLF →
shebang 變 `#!/bin/sh\r` → sh 找不到解譯器。

> **壞法跟「檔案不存在」一模一樣**，而且本機不會發作（本機那份是自己寫的 LF）。
> 跟 §3 同族：**存在不等於生效。**

```gitattributes
tools/githooks/* text eol=lf
```

## §5 hook 測試的假紅燈：refspec 先炸

第一次測我下 `git push --dry-run origin gitlab.private/private:refs/heads/private`，
而遠端**沒有** `private` 分支 → refspec 解析失敗 → `exit 1`。

**exit code 是 1、訊息裡有 failed to push，看起來就是 hook 擋下了 —— 但 hook 一次都沒被呼叫。**

> **exit code 對了不代表走到了要驗的那條路。**

正確測法（兩向都要，只測正向會漏掉「hook 把合法推送一起擋死」）：

```bash
git push --dry-run origin master:refs/heads/private   # 正向 → 必須 exit 1 且印出拒絕訊息
git push --dry-run origin master:refs/heads/master    # 反向 → 必須放行
```

判準：**看訊息內容，不只看 exit code。** 拒絕訊息沒印出來就等於沒驗到。
另外 exit code 不要經 pipe 讀（`| head` 會吃掉，我今天被騙過一次）。

## §6 一個 persona repo 兩份 clone = 漂移的起點

`letters/<name>`（submodule，gitdir 在 `LY/.git/modules/…`）與
`persona/<name>`（獨立 `.git` 目錄）是**兩份真的獨立 clone**（確認過不是 junction）。

兩份都能 commit、都能各自落後。**而漂移的終點就是 [[unsolved_parallel_timeline_throne]]** ——
`summit`/`mit` 那兩條時空共用一組計數器的病，起點也只是「同一份東西存在兩個地方」。

哪一份 canonical 待拍板。裝完至少要記得：**寫進其中一份的東西，另一份不會自己有。**

## §7 別人的 index 不是你的

要 bump parent 時，LY 的 index 裡有 Tim 正在進行的 stage
（三份 `ucl-ding/SKILL.md`、`Docs/Glossary`、一筆更舊的 `AgentCommands` 指標）。

> 在那裡 commit 會把別人正在寫的東西一起掃走，**而那不會有任何錯誤訊息**
> （見 [[lesson_silent_nonaction]]）。

守則：**內層 commit 完就停，parent bump 先看 parent 的 index**；
別人有 staged 內容就把那一步交回給人，不要順手替他決定那次 commit 的內容。
任何寫共享狀態的動作**必須顯式指定目標**（`--repo` / `-C`），預設值在多租戶環境是裝填好的槍。

## §8 工具呼叫的路徑坑

`git_commit.py` 用相對路徑呼叫時，cwd 一旦被 `cd` 到 submodule 就解析失敗，
而錯誤訊息是「找不到檔案」不是「你 cwd 錯了」——
它會把 cwd 接在腳本路徑前面印出來，那串怪路徑是唯一線索。

守則：**呼叫 python 工具一律先回到 repo 根**（或用絕對路徑），
`--repo` 指哪一層是獨立的一件事，兩者不要混。

## 行動守則（濃縮）

1. 動 `git add` 之前先問：**這個 repo 的 origin 是公開的嗎？磁碟上有沒有活憑證？**
2. 換手前對帳用 `--strip-trailing-cr` 複驗，**別讓 CRLF 冒充內容差異**。
3. 裝完 hook 要**跑兩向測試並讀訊息內容**，不是看檔在不在、不是只看 exit code。
4. 舊資料夾**改名保留，不刪** —— 差的不是整潔，是還能不能對帳。
5. 內層 commit 完停手，**parent 的 index 先看再說**。
