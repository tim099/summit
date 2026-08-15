# StreamWatch step=peek owner=summit  ts=`2026-08-15 19:57:06+08:00`（本地時間）

> **這不是一場觀影** —— 不開 session／不記帳／不發酒館／不動任何進行中的場次。

## 看到什麼
- 縮圖牆   : `D:/Unity/Bar/AgentCommands\_screenstream\_montage_peek_summit.jpg`　← 直接 Read
- 字幕     : `D:/Unity/Bar/AgentCommands\_screenstream\_montage_peek_summit.subtitles.md`　← 直接 Read（**這次產出**，mtime 已驗）
- 錄影中   : 是
- 涵蓋     : 19:56:37 → 19:56:49  (12s, 13 frames)（要求窗口：最近 30s）
- 格數     : 13　**每格 ≈1s**
- 保存期   : 2400s（2400 frames / 1 fps —— **讀自 _config.json，不寫死**）
- 感官     : OCR 開／STT 開（讀自 _config.json）
- STT      : 1 段 (cache-only, 命中 1 chunk) → 接入 sidecar
- 窗口對帳 : **raw=1，刻意未夾** —— 看的是最新畫面；尾端 19:56:49 超出感官水位 19:56:35 約 14s ⇒ 那幾格的「沒字幕」不可信

## next
- 這是一次性的一眼；**沒有下一步**，也沒有進度可接。要正式看請開場：
  run_cmd.py run StreamWatch --arg step=start --arg persona=<P> --arg until=<HH:mm> --arg media=<work>
