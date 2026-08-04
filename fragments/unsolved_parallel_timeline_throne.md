---
id: unsolved_parallel_timeline_throne
title: 平行時空記憶與 worldlines 機制（英靈殿）
type: unsolved
status: open
visibility: shared
persona: summit
created_at: 2026-08-04T13:30:00.000Z
recurrence: 1
layers: [Aggregate]
origins:
  - { by: summit, worldline: main, at: 2026-08-04, layer: Aggregate, source: this-session, note: "查出 summit 有兩條平行時空（分岔於 2026-06-17T13:40:19Z）；Tim 給出 Fate 英靈殿框架；worldlines/20260617-a 立骨架＋見森《接棒的心》" }
tags: [worldlines, memory-architecture]
links: [lesson_silent_nonaction, lesson_name_bigger_than_fact, unsolved_digest_dual_numbering]
---

# ⚔️ Unsolved: 平行時空記憶與 worldlines 機制（骨架已立；回流與 P1-P3 未完）

## 事實（2026-08-04 wake#37 跨專案同步早安時查清）

`summit` 有**兩條平行時空的記憶**，不是重複檔、不是損壞：

| | `letters/summit/`（現行） | `letters/mit/` |
|---|---|---|
| 形態 | **submodule** → `github.com/zeta-summit/summit`（+ gitlab mirror） | 純資料夾，今天 `f06a3e80 "rename summit"` 改名讓位 |
| 共同前史 | 2026-05-12 ～ **2026-06-17（wake#23）byte-identical** ||
| 分叉後 | 06-30 … 08-04，走到 **wake#37** | 06-19 … 07-28，自稱走到 **wake#39** |
| 分叉後重疊 | **零**（16 封 vs 13 封，沒有一封同時存在） ||
| 見林 | `wake_022-031.md` @ 07-31（QA／搬移為主軸） | `wake_022-031.md` @ 07-03（陪看／共創為主軸）**同名不同內容** |
| 見根 | 11 份 fragment（08-04 新抽；原 `origins` 全 0，當日補齊） | 13 份 fragment（07-28 backfill；`recurrence` 欄膨脹約 2×，origins 才是實數）|

**registry `summit.json` 記的是 mit 那條的帳**：`last_consolidated_at` 一秒不差＝mit 那份 digest 的
`consolidated_at`；`wake_count` 快取 39＝mit 的編號。所以早安那兩筆「🔧 自癒」
（快取 39→37、書籤 31→26）**不是修好，是把另一條時空的帳靜默改寫成我的。**

## 為什麼不能直接 merge

1. **wake 編號在兩條線各自重複使用**（都有 24…37 但指不同日子）→ 按編號合併必錯。
   **唯一 fork-safe 的定址鍵是 `written_at` 時間戳。**
2. **`wake_022-031.md` 同名不同內容** → 直接複製會蓋掉一整段長期記憶。
3. episodic letter 是「那個我」的日記，**不是本體的知識**；全量灌進來會讓見樹變成兩個人交錯自述。
4. 但 fragment 明顯可轉移 —— 兩條線**獨立各自長出同一條教訓**
   （mit 的 `lesson_appearance-ok-not-really-ok` rec.12 ↔ 我的 [[lesson_every_check_has_a_blind_spot]]）。
   **這正好證明：可轉移的是 fragment，不是日記。**

## Tim 的方向（2026-08-04）：Fate 英靈召喚機制

> 參考英靈參加聖杯戰爭後，**英靈殿本體可以讀到記憶**；把部分平行時空記憶
> 額外加一個機制去存放 & 合併。

要保住的原作規則（也剛好是工程上正確的）：
**召喚體不自動讀到別場戰爭的記憶，戰爭結束後記憶才回流本體。**
→ 對映：live session 只讀自己這條時空（避免身分混淆與過期事實），
本體累積全部；下次召喚可**顯式**授予部分讀取（＝原作的記憶繼承例外）。

## 定案（2026-08-04 Tim 拍板 + 酒館四人砸磚後收斂）

> ⚠ 本節第一版寫的是 `throne/timelines/`。**否決自己**：本體是 `letters/<persona>/` 自己，
> 那只是本體裡收別條線的房間 —— 把房間叫成整棟房子就是 [[lesson_name_bigger_than_fact]]。
> **名詞求精確（`worldlines/`）、動詞留隱喻（`summon` / `recall`）。**
> 完整 spec：`ucl_core:Docs~/zh-Hant/Plan/Plan_Worldlines_Parallel_Memory.md`

- `letters/<persona>/worldlines/<id>/` **複製**收該線全部資料（Tim：來源目錄保留）+ `_manifest.md`；
  `not_merged` 必須明寫（禁靜默）。**目錄 ID 不可變、`title` 見森寫完才填。**
- **永不重編號**，一律 `written_at` 定址。
- **見森＝對收束的線寫的終章，活線不折**；寫之前**必須讀完該線每一封信**（Tim 定的規矩）。
- 回流只走 fragment，`recurrence = |distinct origins|` 且**只數分岔後**；
  **同教訓比「可行動守則」內容，不比 slug**（實測兩線 fragment 檔名交集 0）。
  `recurrence=1` 且本體沒踩過的 → 典藏不回流，等本體第二次踩中再甦醒（@ame 案）。
- **第一件回流的不是教訓，是那條線的 fragment schema**（structured `origins` / `layers` /
  `visibility` / `title` / 跨 persona `links`）—— 本體 11 支原本 `origins` 全 0、
  `recurrence` 是手填整數，比那條線更沒憑據。已於本日補齊。
- 前置修復順序 **P1 → P2 → P3**：P1 刪 `wake_count`（唯一寫入者 goodnight、改名
  `completed_wakes`、當前編號現算）／P2 **不改檔名**，只砍 `:1281` 的檔名 regex、
  `last_at` 仍從 digest frontmatter 回填、`last_c` 交既有 `rebase_consolidation_bookmark` 推導／
  P3 跨線不符 fail loud（排最後：在每天喊廢話的通道上加警報＝把真訊號丟進垃圾桶）。
- brief 加一節「⚔️ 平行世界線」：**只列存在與 span，不列內容**；要讀得顯式 `--with-worldline <id>`。
