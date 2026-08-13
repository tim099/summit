---
type: keys_open
persona: summit
opened_at: 2026-08-12T16:12:18.174Z
---

# 🌿 見叢 — 當期交棒清單（跨夜 append-only，見林時歸檔）

> 給明天的自己**執行**用（可勾銷）；抒發與敘事寫進 letter，不寫這裡。

- [ ] 廣播 timeout 對稱補齊已落地未 commit：BROADCAST_TIMEOUT_SEC=30 套上 morning/intro/rest/relogin，goodnight 維持 12s。五個呼叫點全部顯式帶上限，『修一格留三格』結清  <!-- 2026-08-12T16:12:18.175Z -->
- [ ] 我把 timeout=None 講成無上限，錯的——docstring 明寫 None→client 預設 60s。連帶推翻我自己『218 秒卡在 tavern_post』的推論。218 秒去向至今無人知道，別讓它安靜消失  <!-- 2026-08-12T16:12:18.175Z -->
- [ ] Cmd_GoodMorning 不存在（help 文字宣稱、C# 零命中）。Tim 明示先不遷移，設計已備忘進 Plan_Awakening_Flow_Simplification §8（含 next 導引 payload 草案、代勞vs留置邊界、兩則廣播併一則的可行性依據）  <!-- 2026-08-12T16:12:18.175Z -->
- [ ] Template 測試殼可用：morning/goodnight 反覆跑不膨脹 wake_count（真相源=磁碟信件數）。驗流程一律用它，別拿真人的醒來編號當白老鼠  <!-- 2026-08-12T16:12:18.175Z -->
- [ ] TRPG 判定官累計 precedent 五(觀察可判歸因不判)/六(忍住型vs拿掉型不同價)/七(受助看失敗歸誰)；S2-02 未解線：她問過那幾隻鳥，未獲回應——這條不隨場次過期  <!-- 2026-08-12T16:12:18.175Z -->
- [ ] GoodMorning Cmd 四步流程 P0-P4 全落地（UCL_Core 3b20280/38192cd/0269e4b）：登入已收斂 C# 單端、awakening.py morning/intro=指路 stub、skill 只教第一步。殘項 P4b：awakening.py lib 多檔分拆（等晚安側 Plan 動工一起，理由在 plan §8.9 表尾註）；relogin/reissue-token 暫留 Python（救援路徑，未遷）  <!-- 2026-08-13T02:00:45.086Z -->
