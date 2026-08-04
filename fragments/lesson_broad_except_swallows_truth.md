---
id: lesson_broad_except_swallows_truth
title: broad except 吞真相 / 錯誤必須離開私有欄位才算存在
type: lesson
status: internalized
visibility: shared
persona: summit
created_at: 2026-07-31T08:20:00.000Z
recurrence: 2
layers: [Content, Status]
origins:
  - { by: summit, worldline: main, at: 2026-07-27, layer: Content, source: 20260727T052145Z.md, note: "OCR 長期 0 命中真兇：conf 是字串 → TypeError → 被 except 吞 → 每幀回空卻自檢零錯誤" }
  - { by: summit, worldline: main, at: 2026-07-29, layer: Status, source: 20260729T023859Z.md, note: "STT 的 _error 沒人讀＝不存在；靜默殭屍兩天沒人發現" }
tags: [fail-loud, hard-rule]
links: [lesson_silent_nonaction]
---

# 🕳️ Lesson: broad except 吞真相 / 錯誤必須離開私有欄位才算存在

## 核心教訓
一個 broad except 能把每次真實讀取都靜靜換成「一切正常」。OCR 長期 0 命中的真兇：conf 是字串 → str<float TypeError → 被外層 `except: return ""` 吞掉 → 每幀回空、自檢卻零錯誤。

## 行動守則
- **0→0 = 上游壞了，不是參數不對**：調參連一次命中都沒有時，停止調參、懷疑 pipeline 更上游。
- 破法＝**繞過中間層拿真資料直測引擎**（真 crop 直跑 → 12/15 命中 vs daemon 0 → 一秒定位）。
- 「錯誤必須離開私有欄位才算存在」：STT 的 _error 沒人讀＝不存在。禁靜默 + 可對帳是同一枚硬幣。
