# StreamWatch step=start persona=summit  ts=`2026-08-15 20:46:00+08:00`（本地時間）

- session: `sw-20260815T124600Z-summit`（state: `D:/Unity/Bar/AgentCommands\StreamWatch\sessions\summit.json`）
- media: `bilibili-zhengqu-zuihou-de-ziyou`　⚠ **這是新 work** —— 若這部片其實已存在於 Library，現在喊停比事後合併便宜
- work 建檔: 已建立 `D:/Unity/Bar/AgentCommands\BookNotes\Library\works\bilibili-zhengqu-zuihou-de-ziyou\work.json`（title=`争取最后的自由`）—— 下一場起這個鍵會出現在既有清單裡
- UP 主  : **争取最后的自由**（work 認這個；影片標題/介紹記在場次上）
- 本場影片: 刚出狱就抢劫军用卡车！！！
- 出處    : https://www.bilibili.com/video/BV1dtX7BrEuM/
- 看到: 21:15（約 28 分鐘）
- 開播公告: seq **15289**（匯出區間左端點）
- 保存期   : 2400s（2400 frames / 1 fps —— **讀自 _config.json，不寫死**）

## next
1. **取素材**：run_cmd.py run StreamWatch --arg step=cycle --arg persona=summit
2. 依回傳檔給的**絕對路徑** Read 縮圖牆與字幕 → 寫觀戰評論
3. **發評論**：run_cmd.py run StreamWatch --arg step=observe --arg persona=summit --arg-file body=<評論>
4. 回到 1 —— **收工不用你判斷**：到期或 Tim 停錄影時，cycle 會告訴你並提示寫接續點。
