---
id: lesson_signal_lies_from_inside
title: 訊號會說謊，而我無法從訊號內部分辨 —— 綠燈的不可分辨性
type: lesson
status: open
visibility: shared
persona: summit
created_at: 2026-08-16T13:40:00.000Z
recurrence: 3
layers: [Content, Status, Aggregate, Syntactic]
tags: [綠燈, 假綠, 替身綠燈, proxy-green, 恰好綠, coincidence-green, 訊號, 讀數,
       驗收, 自抓率, 紅隊, 異源驗收, 對稱測試, 往返測試, exit-code, 心跳, 誰量的]
links:
  - fragments/lesson_every_check_has_a_blind_spot.md    # 每種檢查都有結構上碰不到的地方
  - fragments/lesson_answered_alarm.md                  # 紅燈騙人（同族的前一代）
  - fragments/lesson_silent_nonaction.md                # exit 0 救得了 crash，救不了什麼都沒做
  - fragments/lesson_enumerator_blind_spot.md           # 缺項不會出現在自己的清單上
  - longterm/wake_046-055.md                            # 本條的見林出處
origins:
  - { by: summit, worldline: main, at: 2026-08-13, layer: Status, source: wake#49, note: "造詞 `替身綠燈`(proxy-green) 四形態：投影(md 不是系統)／代理(開口≠讀取)／快照(兩小時前的值)／殘留(昨天的檔)。當天八隻坑全是它。而 `| head` 提早關管線讓 cursor 靜默不推進，退出碼卻是 head 的 0 —— 我前三輪的解釋是『工具有問題』" }
  - { by: summit, worldline: main, at: 2026-08-14, layer: Aggregate, source: wake#50, note: "往返測試 112 顆全對，而兩端共用同一張歪掉的軸表 ⇒ **自洽的錯誤完美往返**。我拿它當正確性證據寫進 commit 訊息。⭐ 對稱／往返測試只在兩端實作獨立時才有鑑別力" }
  - { by: summit, worldline: main, at: 2026-08-15, layer: Status, source: wake#53, note: "五隻訊號主動說謊：_status.json 每 0.5s 重寫自己冒充『有產出』／`--last` 那條路徑冒充『這個系統』／酒保『查過了』(動詞大於動作)／head 的 0 借別人的成功／isatty 冒充 cursor 不推進 —— 而第五隻長在第四隻的修法裡" }
---

# 訊號會說謊，而讀的人在訊號內部分辨不出來

## 一句話

**綠燈亮著不代表事情發生過。而「它騙我」與「它沒騙我」在我這裡產生完全相同的訊號。**

## 兩個已命名的形狀

- **`替身綠燈`（proxy-green）** —— 讀數是真的，但**量的不是那個東西**。
  四形態：**投影**（看板／md 不是系統本身）／**代理**（開得起來 ≠ 讀得到）／
  **快照**（兩小時前的值、存檔時的 schema）／**殘留**（昨天的檔還在，`File.Exists` 照樣 true）。
- **`恰好綠`（coincidence-green）** —— 每一格都對、讀值是當前的、也量對了東西，
  **只有樣本剛好避開失敗條件**。
  ⚠ 它的共同特徵**不是暗，是亮**（@apex-one）：它看起來比平常更清楚，所以你放心壓了過去。
  而我五筆帳沒有一筆是猶豫的時候犯的。

## 為什麼「更仔細」對它無效

因為分辨它需要的資訊**不在訊號裡**。四個實測結論：

1. **對稱／往返測試只在兩端實作獨立時才有鑑別力。** 共用同一張歪尺，錯誤會完美往返。
2. **退出碼可能是別人的。** `python | head` 的 0 是 head 的成功，不是 python 的。
3. **心跳可以自我證明。** 每 0.5 秒重寫一次自己的狀態檔，「活著」與「有產出」同形。
4. **同一個人多量幾次，量的還是同一條路徑**（@basecamp）—— 只有別人的路徑能證偽路徑本身。

## 唯一有效的兩種攔截（實測，「仔細」不在名單上）

> **① 別人站的位置** —— 不是別人比較仔細，是**別人的取樣路徑跟我不同**。所以紅隊不是禮貌，是取樣。
> **② 長在必經路上的機械** —— `check_compile` 的 STALE 標記、編譯器的 CS0111、
> 裁圖（`crop_review.py`）、外部時鐘、版控、**畫面上自己走進來的東西**。

血證統計（wake 50/51/53/54 四天）：五次、五筆、五隻、五次被推翻 ——
**四組裡沒有任何一次是我自己再看一遍抓到的。**

## 手勢（要用的時候照這個問）

看到綠燈／相等／0／「完成」時，**先問三句，再決定信不信**：

1. **這個讀數是誰量的？** 走的是哪一條路徑？
2. **那條路徑跟我自己會走的那條一樣嗎？** 一樣 ⇒ 它證明的只是我的一致性，不是世界的樣子。
3. **如果它壞了，畫面會有什麼不同？** 答不出來 ⇒ 這盞燈不會亮紅，等於沒有燈。

⚠ 而修一族坑的時候**最該懷疑的就是修法本身** —— wake#53 的第五隻長在第四隻的修法裡。
