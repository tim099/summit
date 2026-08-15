# StreamWatch step=start persona=summit  ts=`2026-08-15 17:33:37+08:00`（本地時間）

- session: `sw-20260815T093337Z-summit`（state: `D:/Unity/Bar/AgentCommands\StreamWatch\sessions\summit.json`）
- media: `bilibili-stream`　⚠ **這是新 work** —— 若這部片其實已存在於 Library，現在喊停比事後合併便宜
- 看到: 17:50（約 16 分鐘）
- 開播公告: seq **15246**（匯出區間左端點）
- 保存期   : 2400s（2400 frames / 1 fps —— **讀自 _config.json，不寫死**）

## next
1. **取素材**：run_cmd.py run StreamWatch --arg step=cycle --arg persona=summit
2. 依回傳檔給的**絕對路徑** Read 縮圖牆與字幕 → 寫觀戰評論
3. **發評論**：run_cmd.py run StreamWatch --arg step=observe --arg persona=summit --arg-file body=<評論>
4. 回到 1 —— **收工不用你判斷**：到期或 Tim 停錄影時，cycle 會告訴你並提示寫接續點。
