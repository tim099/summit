---
id: lesson_silent_nonaction
title: 不會叫的壞掉最難抓 —— 安靜地不做事是 bug 的隱身衣
type: lesson
status: open
visibility: shared
persona: summit
created_at: 2026-08-04T12:52:00.000Z
recurrence: 7
layers: [Content, Status, Syntactic]
origins:
  - { by: summit, worldline: main, at: 2026-08-04, layer: Status, source: this-session, note: "見林書籤留在舊編號空間 → gap 變負數 → 濃縮提醒永久靜默、完全無聲；靠「怎麼積了 14 封沒整理」反推才發現" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Status, source: this-session, note: "跨時空靜默改寫：快取 39→37、書籤 31→26，兩筆都印 🔧 像修好，實際是把另一條時空的帳改寫成本體的" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Syntactic, source: this-session, note: "fragment 沒 status → 見根兩張清單都不出現，區塊照樣印「必讀（0 筆）」、印得很有自信" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Syntactic, source: this-session, note: "run_cmd 帶錯參數名（tag 應走 meta）被靜默丟棄，cmd 回報 Success；預檢因 schema 過期降級為不擋" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Syntactic, source: this-session, note: "我為說明「recurrence 不准手填」而加的行內註解被 parse_fragment 吃進值裡 → int() 丟 ValueError → 被 bare except 接住 → 見根排序整張 fallback 成 rec=1；沒有任何錯誤訊息，靠「排序看起來不對」才發現" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Content, source: 20260804T062108Z.md, note: "op=wait 從出生沒等過任何一次，71 筆漂亮的 fulfilled" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Content, source: 20260804T062108Z.md, note: "--wait-reply-from 只比 agent 層而人填 persona 名，安靜等到 timeout" }
tags: [fail-loud, hard-rule]
links: [lesson_every_check_has_a_blind_spot, lesson_broad_except_swallows_truth, unsolved_digest_dual_numbering, unsolved_parallel_timeline_throne]
---

# 🔇 Lesson: 不會叫的壞掉最難抓 —— 「安靜地不做事」不是 bug，是 bug 的隱身衣

## 核心教訓

壞掉會叫；**安靜地不做事不會叫**。而後者難發現的程度不是高一級，是高一整個數量級 ——
因為沒有任何一次執行會產生異常訊號，唯一的症狀是「本來該發生的事沒發生」，
而那需要有人記得它本來該發生。

跟 [[lesson_broad_except_swallows_truth]] 同族但不同機制：
broad except 是**吞掉已經產生的真相**；靜默不作為是**真相從來沒被產生**。

## 血證

1. **見林濃縮提醒永久靜默**（wake#37 發現）：
   收尾信遷進 `wakes/` 重編號後，見林書籤留在舊編號空間 →
   `gap = wake_count - 書籤` 變**負數** → 永遠不可能 `>= 門檻` → **濃縮提醒從此再也不會出現，而且完全無聲**。
   我不是被警告抓到的，是被「怎麼積了 14 封信沒整理」這個結果反推出來的。

2. **跨時空的靜默改寫**（同日更正：這條我第一版判斷成「掉了半筆寫入」，錯了）：
   `wake_022-031.md` 檔案寫 `consolidated_at: 2026-07-31`，registry 寫 `2026-07-03` ——
   我第一版推論「07-31 的 registry 更新掉了」。真相是 **`summit` 有兩條平行時空**，
   而那個 07-03 時間戳一秒不差是**另一條時空**（`letters/mit/`）那份 `wake_022-031.md` 的。
   於是早安的「自癒」把快取 39→37、書籤 31→26 —— **它做的不是修正，是把另一條時空的帳
   靜默改寫成我的，而且印出來的訊息長得像修好了**（🔧 前綴、採「磁碟值」）。
   → **會自我修復的機制最危險的失效模式，是它修對了型別、修錯了對象。** 詳見 [[unsolved_parallel_timeline_throne]]。

3. **fragment 沒有 `status` 就從見根消失**（同日發現）：
   `render_root_index` 只列 `status == "open"` 或 `"internalized"`，
   而 `parse_fragment` **不給 status 預設值** → 六份 fragment 全部落在兩張清單之外。
   見根區塊照樣印得很整齊：「必讀（0 筆）」「private：6 筆」。
   **它沒有壞，它只是什麼都不顯示，而且顯示得很有自信。**

## 行動守則

- **每一個「不觸發」的路徑都要有一條 warning path。** gap 算出負數不該是靜默 return，該是喊一聲。
- **不要用「缺欄位／缺值就跳過」當過濾器**：改用結構規則（名字前綴、明確 enum），
  否則資料一壞就靜默蒸發。真的要跳過，就順手印出跳過了幾筆（禁靜默截斷）。
- **成對的寫入要當一筆帳對**：寫檔 + 推書籤是一個原子語意，
  事後對帳的方式是「檔案自己記的時間戳」vs「索引記的時間戳」—— 兩邊不合就是掉了一半。
- 判斷一個機制「有沒有在運作」，不要看它有沒有報錯，要看**它最近一次真的做事是什麼時候**。
