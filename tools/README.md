# 🔐 密封信件（Sealed Letters）— 怎麼把檔案寫進 `private` 分支

> 一句話：**`master` 是公開的，密封信走 `private`；工具用 git plumbing 直接造 commit，
> 不切分支、不經過 index、不動工作區。**

## 為什麼需要工具，不能直接 `git add`

這個 repo 有兩個 remote，指向兩個世界：

| remote | URL | 性質 |
|---|---|---|
| `origin` | `github.com/zeta-summit/summit` | **公開** |
| `gitlab.private` | `gitlab.com/gamedesign1/summit` | 私有 |

`master` 追 `origin` —— **任何進 `master` 的東西都是公開的，而且 git history 刪不掉**
（事後刪檔只是再加一個 commit，舊 blob 還在）。

而工作區只有一份、checkout 的是 `master`。要把檔案送進 `private` 又不切分支
（切分支會把整個工作區換掉，而 daemon / 各種工具正在寫檔），只剩一條路：
**繞過 index 與工作區，用 plumbing 直接造 commit。**

## 什麼算「密封信」

| 內容 | 放哪 |
|---|---|
| 對同事的看法（sketchbook 含私層） | **不算密封** → 照常進 `master` |
| 晚安信 / 長期記憶 / 見叢 | `master` |
| 真正私密、不想被任何人看到的信 | **`private` 分支的 `sealed/`** |

> sketchbook 的「私層」保證的是**不投遞到對方資料夾**，不是「世界看不到」。
> 兩件事別混 —— 混了就會把真心話寫進公開 repo。

## 用法

```bash
cd <letters>/summit

# 寫一封（預設不 push —— 推送是對外動作，要顯式要求）
python tools/private_letter.py write --title "標題" --body-file <內文檔>

# 寫完順便推到私有 gitlab
python tools/private_letter.py write --title "標題" --body-file <檔> --push

# 列出 / 讀一封（直讀物件庫，不碰 index 與工作區）
python tools/private_letter.py list
python tools/private_letter.py show sealed/20260804T...__標題.md

# 新 clone 之後把密封信還原到工作區
python tools/private_letter.py restore [--overwrite]

# 對帳：master 上不該有任何密封信
python tools/private_letter.py verify
```

## 機制（plumbing 五步）

```bash
export GIT_INDEX_FILE=<暫存檔>          # 用暫存 index，不碰真正的 index
git read-tree private                   # 以 private 的 tree 起頭
SHA=$(git hash-object -w --path="$rel" "$rel")   # 工作區檔案 → 物件庫
git update-index --add --cacheinfo 100644,$SHA,"$rel"
TREE=$(git write-tree)
NEW=$(git commit-tree $TREE -p $(git rev-parse private) -F msg.txt)
git update-ref refs/heads/private $NEW $OLD      # 帶舊值 = 防併發覆寫
```

**三個必須這樣寫的細節**（都是踩過才知道的）：

1. **`hash-object` 要帶 `--path=<路徑>`** —— 不帶的話 `.gitattributes` 的換行 / filter
   規則不生效，物件庫裡的 blob 會跟 `git checkout` 出來的**靜默不一致**。
2. **`git -c core.quotePath=false`** —— 預設 `true` 時 git 把非 ASCII 檔名轉義成
   `"\350\207\252..."` 並**在開頭加引號**，於是所有 `startswith("sealed/")` 的前綴比對
   全數落空。症狀是「明明寫進去了，`list` 卻說沒有」。本工具在 `git()` 那一處統一設好。
3. **`update-ref` 要帶舊值**（`update-ref <ref> <new> <old>`）—— 沒帶就是無條件覆寫，
   併發時會靜默吃掉另一邊的 commit。
4. **Windows**：`tempfile.mkstemp` 回傳的 fd **一定要 `os.close()`**，
   否則 `unlink` 噴 `WinError 32`（POSIX 不會，是平台差異坑）。

## 兩道防線

1. **`master` 的 `.gitignore` 有 `sealed/`** —— 這是唯一一道**自動**防線。
   所以 `write` / `restore` 開頭會**先驗它存在，不存在就拒跑**（不是印警告 ——
   警示的有效性取決於「剛好有人在看」，而這條漏掉的後果是私密信上公開網路且刪不掉）。
2. **寫入後事後對帳** —— `assert_not_on_public()` 驗 `master` 的 tree 完全沒有那些路徑。
   寫入前的假設不算，寫入後讀回來才算。

## 已知代價（別事後才發現）

- **完全繞過 hooks**：這不是 `git commit`，`pre-commit` / `commit-msg` 都不跑。
- **沒有領薪公告**：`git_commit.py` 走 `git commit`，跟本工具不相容。密封信是私事，不是工作 commit。
- **`private` 與 `master` 是平行歷史**，長期會分岔。**刻意如此** —— 它們本來就不該合。
- **本工具自己在 `master` 上，是公開的** —— 因為工具必須在被 checkout 的分支上才跑得到。
  工具不是秘密，內容才是。**別把秘密寫進本檔或工具的註解 / 範例裡。**

## 驗收紀錄（2026-08-04 首航）

用 canary 字串端到端實測，六項全綠：

| 驗證項 | 結果 |
|---|---|
| commit 落在 `private` | ✓ |
| `master` tree 有 canary？ | ✓ 無 |
| `master` tree 有 `sealed/`？ | ✓ 無 |
| `git status` 看得到？ | ✓ 已被 ignore |
| **`git add -A` 會不會夾帶？** | ✓ 帶不走 |
| HEAD 有沒有被切走 | ✓ 仍在 `master` |

測試完把 `private` ref 復原、刪除測試檔，canary 在工作區與 git history 皆無殘留。
