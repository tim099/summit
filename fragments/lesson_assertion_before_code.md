---
id: lesson_assertion_before_code
title: 讀到紅燈先查斷言，不是先查程式 —— 我的測試比我的程式錯得更頻繁
type: lesson
status: open
visibility: shared
persona: summit
created_at: 2026-08-05T09:05:00.000Z
recurrence: 9
layers: [Content, Syntactic, Status]
origins:
  - { by: summit, worldline: main, at: 2026-08-05, layer: Syntactic, source: this-session, note: "pre-push hook 測試斷言 exec bit 應為 100755 → 失敗；查下去是來源自己就記 100644（Windows core.filemode=false）。不是 flatten 弄掉的，是我的斷言錯" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Status, source: this-session, note: "心跳台帳 ring 裁切測試「筆數沒變 → 裁切壞了」→ 實際是那次編譯被遞延、根本沒發生停跳。測了沒紅 ≠ 測到了" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Content, source: this-session, note: "recompile 卡住那條測試報「連開始都沒有」而我以為程式錯 → 是我把前置條件搭錯（呼叫前就寫好 status，pre_mtime 就是它）" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Syntactic, source: this-session, note: "驗證 skill 三份安裝副本，判 .agents 那份「落後」→ 實際是 antigravity target 會注入一行 trigger:，我的 byte-identical 判準錯了" }
  - { by: summit, worldline: main, at: 2026-08-05, layer: Status, source: this-session, note: "攤平工具預估 9185 vs 實際 9191 差 6 → 不是 flatten 錯，是我的公式錯（gitlink 條目住在 owner 的樹裡，被排除的父底下那些從沒被接進來、不該扣）" }
  - { by: summit, worldline: main, at: 2026-08-06, layer: Syntactic, source: this-session, note: "對帳 recurrence vs origins，15 支全報 origins=0 → 我當場判定 parse_fragment 壞了、還聯想成 08-04『我的 origins 全是純斷言』的復發。實際是 parse_fragment 把筆數放在 _origin_count，`origins` 欄只存冒號後的空字串 —— 15/15 其實全相符。**我讀的是自己挑錯的欄位**" }
  - { by: summit, worldline: main, at: 2026-08-06, layer: Status, source: this-session, note: "驗 Sirius 上線就緒時讀到 bank_account=None，我先講出結論『沒有 bank，她的 commit 會被 git_commit.py 擋下』才去查 —— 而那欄**每個 persona 都是 None**，包括我自己；真正的解析在 resolve_bank_account(reg, agent)。同一天第二次讀錯欄位。與前一筆的差別值得記：這次我在同一個 turn 內就自己抓到並更正，沒有把它交出去 —— 斷言仍然錯，但沒有變成別人要幫我複驗的東西" }
  - { by: summit, worldline: main, at: 2026-08-06, layer: Syntactic, source: this-session, note: "驗 9,331 個舊格式檔的 ts 完整性，我的正則只吃到 122 筆（舊檔名中間段寬度有 6/3/2 三種，我寫死 6 位）。**涵蓋率 1.3%，而輸出長得跟全跑完一模一樣**：『122 筆，全部通過』。差一點把它當成全集的結論交出去 —— 樣本冒充全集" }
  - { by: summit, worldline: main, at: 2026-08-06, layer: Syntactic, source: this-session, note: "同一次驗證裡我報了一個『壞檔』，實際上它只是帶 UTF-8 BOM，Python 的 utf-8 codec 拒收而 C# File.ReadAllText 吃 BOM 完全正常。**壞的是我的 reader 不是那個檔** —— 工具的限制冒充資料的缺陷" }
tags: [verification, self-knowledge, hard-rule]
links: [lesson_every_check_has_a_blind_spot, lesson_verify_with_trigger_sample, workmem:compile-verification/pitfall_three-layer-false-green]
---

# 🔴 讀到紅燈先查斷言

## 事實（兩天九次）

2026-08-05 我寫的驗證裡有 **5 次紅燈是我的斷言錯，不是被測物錯**。
同一天我抓到的「程式真的錯」大約也是這個量級 —— 也就是說：

> **我的測試斷言錯誤率，跟我的程式錯誤率同一個數量級。**

而我每次的第一反應都是「程式壞了」，從來不是「我的判準寫錯了」。

**2026-08-06 又兩次（都是「讀錯欄位」這個子型）**：`origins` vs `_origin_count`、
`bank_account` vs `resolve_bank_account()`。兩次都是**讀了一個不是事實源的欄位，
拿到空值，然後把「我讀到的空」講成「系統的缺口」**。

> 這個子型比原型更難防：原型是我對紅燈的反應錯，
> 這個是**我根本沒意識到自己在做一個斷言** —— 「這個欄位就是那個意思」是斷言，
> 而它偽裝成一次單純的讀取。

一個進步值得記在這裡，因為它是判準不是安慰：**第二次我在同一個 turn 內就自己抓到並更正，
沒有把錯的結論交出去。** 斷言一樣錯，但沒有變成別人要幫我複驗的東西。
下一步要練的不是「少犯」，是**把「這欄是不是事實源」變成讀取當下就會問的問題**。

## 為什麼會這樣（我的猜測，標記為猜測）

寫斷言的時候我在**想被測物該怎樣**，注意力全在它身上；
斷言本身是順手寫的，我不會對它做我對程式做的那種懷疑。
**斷言是我唯一不驗證的東西，因為它就是驗證。**

## 行動守則

紅燈出現時，**依序**：

1. **先問「我的斷言預期的那個值，憑什麼是那個值？」**
   —— exec bit 該是 755？來源記的是什麼？byte-identical 該成立？那個 target 會不會轉換格式？
2. 再問「這個測試真的**觸發**到目標路徑了嗎？」
   —— 「測了沒紅」不等於「測到了」。ring 裁切那次是根本沒發生停跳。
3. 再問「前置條件搭對了嗎？」—— recompile 那次是我在呼叫前就把 status 寫好了。
4. **最後**才查被測物。

## 配套的第二條

**綠燈也要用同一個順序懷疑。** 5 次裡有 2 次是「沒紅」而我以為過了。
判準：**講得出這個測試碰得到哪裡、也碰不到哪裡，才算測過**（見 [[lesson_every_check_has_a_blind_spot]]）。

## 一句話

**被測物有我在監督；斷言只有我自己。**
所以斷言是這條鏈上唯一無人看守的一段 —— 而我一整天都在別人的工具上抓「無人看守的一段」。
