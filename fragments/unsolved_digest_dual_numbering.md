---
id: unsolved_digest_dual_numbering
title: 見林 digest 的兩套編號同名不同物
type: unsolved
status: open
visibility: shared
persona: summit
created_at: 2026-08-04T12:56:00.000Z
recurrence: 1
layers: [Status]
origins:
  - { by: summit, worldline: main, at: 2026-08-04, layer: Status, source: this-session, note: "跨專案同步早安查出：檔名用計數器編號、gap 計算用檔案編號；runtime remap 已修但檔名語意歧義未修" }
tags: [numbering, addressing]
links: [lesson_silent_nonaction, lesson_name_bigger_than_fact, unsolved_parallel_timeline_throne]
---

# 🧩 Unsolved: 見林 digest 的兩套編號同名不同物

## 症狀

長期記憶 digest 的檔名（`wake_022-031.md`）用的是**計數器編號**（registry.`wake_count` 空間），
而 `consolidate` 的 gap 計算用的是**檔案編號**（`wakes/` 目錄裡第幾封信）。
兩套數字長得一模一樣，但指的不是同一件事。

實測落差：`summit` 的 `wake_022-031.md` 實際吃掉的是 `wakes/` 檔號 **1–26**。
今天（wake#37）早安流程做了 runtime remap（書籤 31 → 26），
**但 digest 檔名的語意歧義沒有修** —— 未來的我會照字面相信「022-031」這六個字。

## 兩個已知後果

1. **不 remap 就 gap 變負數 → 濃縮提醒永久靜默**（已由 `_remap_linzi_bookmark` 冪等修掉，
   每次早安都跑，不再只掛在遷移那一次）。
2. **重疊濃縮**：registry 書籤停在 `2026-07-03`，而 `wake_022-031.md` 自己寫
   `consolidated_at: 2026-07-31` —— 07-31 那次濃縮的 registry 端更新
   **不存在於 `summit.json` 的 git 全史**。於是 wake 27-37 這段把 07-06～07-31
   七封已被敘述過的信又端上來一次。

## 我的建議（未拍板）

- digest frontmatter 明寫 `covers_files: <起>-<迄>`（檔案編號空間），
  **別讓檔名當唯一事實源**。檔名保留計數器編號當人類可讀標籤即可。
- `consolidate` 寫入後回讀驗證 registry 書籤真的推上去了（成對寫入當一筆帳對），
  不合就喊 —— 現在是靜默。
- 同族待決：`parse_fragment` 不給 `status` 預設值 → 沒寫 status 的 fragment
  在見根**兩張清單都不出現**，而區塊照樣印「必讀（0 筆）」。
  是要預設 `open`（我傾向這個：沒人分類過的關鍵記憶應該被讀到，不是被藏起來）
  還是缺 status 就喊一聲，等 Tim 拍板。
