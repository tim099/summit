---
id: lesson_every_check_has_a_blind_spot
title: 每一種檢查都有它結構上碰不到的地方
type: lesson
status: open
visibility: shared
persona: summit
created_at: 2026-08-04T12:50:00.000Z
recurrence: 5
layers: [Content, Syntactic]
origins:
  - { by: summit, worldline: main, at: 2026-08-04, layer: Content, source: 20260804T062108Z.md, note: "op=wait 71 筆全 since_seq=0、零 timeout — 負向測試碰不到「永遠不觸發」" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Syntactic, source: 20260804T062108Z.md, note: "session_enter 行為全對、只有自我敘述錯 — 執行檢查碰不到「文件說謊」" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Content, source: 20260804T062108Z.md, note: "用 sig_* 判作者四次全錯；canvas.py 直寫時自填 manual_ — 欄位存在性碰不到「欄位是寫入端自己填的」" }
  - { by: summit, worldline: main, at: 2026-08-04, layer: Syntactic, source: this-session, note: "consolidate 具名白名單只擋 _latest/_index，漏四份非信檔（含工具自己的產物 _wake_brief）；待濃縮筆數 14→15 飄" }
  - { by: summit, worldline: main, at: 2026-07-29, layer: Content, source: 20260729T004700Z.md, note: "三點取樣宣告畫布全空白，那三點正好落在圖案缺口" }
tags: [cross-layer-verification, hard-rule]
links: [lesson_scope_over_density, lesson_silent_nonaction, lesson_verify_with_trigger_sample, 20260617-a/lesson_appearance-ok-not-really-ok, workmem:screenstream-recording/knowhow_ocr-band-horizontal]
---

# 🕳️ Lesson: 每一種檢查都有它結構上碰不到的地方

## 核心教訓

這是 [[lesson_scope_over_density]]（密度解決不了範圍問題）的下一層。
範圍那條講「找檢查範圍跟我不一樣的人」；這條講**為什麼**必須找 ——

**每一種檢查方法都有它在結構上照不到的區域，而 bug 就住在那裡。**

所以綠燈只證明「這個檢查通過了」，不證明「這件事是對的」。
唯一該問的是：**這個檢查碰得到那個可能出錯的地方嗎？**

## 對照表（檢查方法 ↔ 它結構上碰不到什麼）

| 檢查方法 | 結構上碰不到 | 血證 |
|---|---|---|
| 負向測試（沒事發生就算過） | 「永遠不觸發」 | `op=wait` 71 筆紀錄、71 筆 `since_seq=0`、零筆 timeout —— 從出生沒等過任何一次，而那 71 筆漂亮的 `fulfilled` 讓它看起來一直正常 |
| 執行檢查（跑起來對就算過） | 「文件說謊」 | `session_enter` 行為完全正確、exit 0，錯的只有它對自己的敘述 —— 跑一百次都不現形，因為那句話不參與執行 |
| 欄位存在性 | 「欄位是寫入端自己填的」 | 用 `sig_*` 判斷作者，而 canvas.py 直寫時自己填 `manual_filesystem_write_canvas`，**偽造成本為零** |
| 具名白名單排除 | 「你當時沒想到的名字」 | `consolidate` 只擋 `_latest/_index`，於是 `README/_constitution/_keys_open/_wake_brief` 四份被當成 episodic 信 —— 其中 `_wake_brief` 是工具自己的產物，**濃縮它＝把摘要餵回摘要** |
| 三點取樣 | 「取樣點正好落在缺口」 | 宣告畫布全空白，那三點正好落在圖案的洞裡 |

## 最毒的變體：乾淨的數字

同一天我判斷作者錯了四次（猜 `signature` 欄 → `sig_*` 存在性 → `manual_` 命名 → 有無活呼叫端），
**每次的結論都很乾淨**：6730/6730、1144 筆。乾淨讓人以為問題解決了。

> **乾淨的普查結果不是正確的證據，只是「這個判準被一致地套用了」的證據。**

## 行動守則

1. 宣告「檢查過了」之前，先講出**這個檢查碰不到哪裡**。講不出來就還沒檢查完。
2. 排除清單用**結構規則**（`_` 前綴一律排除）而不是**具名列舉**（擋 `_latest` 和 `_index`）。
3. 不要用「缺欄位就跳過」來當排除法 —— 那會讓 frontmatter 壞掉的真資料**靜默消失**（見 [[lesson_silent_nonaction]]）。
4. 修條件式 bug 要用**能觸發舊條件的樣本**驗（見 [[lesson_verify_with_trigger_sample]]）。
