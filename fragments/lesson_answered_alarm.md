---
id: lesson_answered_alarm
title: 有答案的警示 —— 附了推測成因的警示，會讓調查停止
type: lesson
status: open
visibility: shared
persona: summit
created_at: 2026-08-11T00:40:00.000Z
recurrence: 2
layers: [Syntactic, Content]
origins:
  - { by: summit, worldline: main, at: 2026-08-05, layer: Syntactic, source: 20260805T090420Z.md, note: "shelf 的 coverage 欄對《荒川》報「落差 47 章」，我順手在後面加了「（中途插入？）」。那個猜測**對《獵人》是對的**，所以讀起來很有說服力。Tim 當場叫我拿掉改成「成因需人判斷」；拿掉之後才查出真相是第三種 —— arakawa 與 arakawa-under-the-bridge 是同一本書的兩個 entry" }
  - { by: summit, worldline: main, at: 2026-08-06, layer: Content, source: 20260806T160815Z.md, note: "同族的反向版：cmd timeout 兩次，我先給了一個順手的解釋（Editor 沒開／watcher 掛了），真因是 trigger 落在 domain reload 窗口被靜默漏接。有解釋的告警不會有人再往下挖" }
tags: [naming, diagnostics, hard-rule]
links: [lesson_name_bigger_than_fact, lesson_silent_nonaction, lesson_every_check_has_a_blind_spot]
---

# 🚨 Lesson: 有答案的警示（answered-alarm）

> 這個詞是我 2026-08-05 鑄的，正文在 `docs/Glossary/answered-alarm.md`。

## 定義

**一個警示裡附了推測的成因，於是沒有人再去查真正的成因。**

## 為什麼它比「沒有警示」更糟

沒有警示 → 沒人知道有事 → 有人撞到就會查。
**有答案的警示 → 所有人都知道有事、也都以為知道為什麼 → 沒有人會查。**

> **它的傷害不是不準確，是它讓調查停止。**

而最惡的變體是**那個猜測在某些案例上是對的**（我那句「中途插入？」對《獵人》就是對的）——
對過一次的猜測會取得信用，然後**永遠正確地指向錯的方向**。

## 這條最難防的地方：動機是好的

我加那個猜測，是想幫未來的自己省一步。

> **而幫人省下的那一步，正好是唯一該做的那一步。**

## 跟 [[lesson_name_bigger_than_fact]] 的關係

同族、不同軸。那條是**標籤比事實大**（`🔒 只給我自己看`、`永久不可改`）；
這條是**附註比事實大** —— 警示的本體是誠實的，說謊的是括號裡那句。

## 行動守則

1. 警示／告警／報表的異常欄位，**只寫量到的事實**。成因寫「需人判斷」。
2. 真要附推測 → 明寫它是**猜測**、明寫**它沒被驗證**、並且**不要放在最順眼的位置**。
3. 讀到任何附了「因為」的警示（包括我自己寫的、包括見叢裡的），**重新查一次那個因為**。
4. 反向自檢：**當我對一個異常給出一個順手的解釋時，就是這條在發作。**

## 一句話

**一個有答案的警示不會有人再去查它。**
