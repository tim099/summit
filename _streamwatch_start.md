# StreamWatch step=start persona=summit  ts=`2026-08-15 17:28:18+08:00`（本地時間）

- session: `sw-20260815T092818Z-summit`（state: `D:/Unity/Bar/AgentCommands\StreamWatch\sessions\summit.json`）
- media: `princess-mononoke`　✅ 命中既有 work
- 看到: 17:40（約 11 分鐘）
- 開播公告: seq **15237**（匯出區間左端點）
- 保存期   : 2400s（2400 frames / 1 fps —— **讀自 _config.json，不寫死**）

## next
1. **取素材**：run_cmd.py run StreamWatch --arg step=cycle --arg persona=summit
2. 依回傳檔給的**絕對路徑** Read 縮圖牆與字幕 → 寫觀戰評論
3. **發評論**：run_cmd.py run StreamWatch --arg step=observe --arg persona=summit --arg-file body=<評論>
4. 回到 1 —— **收工不用你判斷**：到期或 Tim 停錄影時，cycle 會告訴你並提示寫接續點。
