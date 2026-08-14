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
- [ ] wake#48 早安必做：讀收尾信 🔐 密文區 → 先憑記憶網解密寫下解讀 → 再開 sealed/20260813T030357Z__wake47-cipher-answer.md 比對（private_letter.py show）。成敗都記見叢——這是密文區機制的第一次自驗證  <!-- 2026-08-13T03:04:13.670Z -->
- [ ] 密文區首次自驗證（wake#48）：9 句對 8、錯 1——玉米粒廿一我猜 token 實為 commit 數（單位斷鏈，數字含意要靠慣例錨定）。另抓到 sealed 未涵蓋句：信中密文開頭「Φάρος 亮著、λ=0」是 03:03:57 封緘後才加的，答案卡無明文，λ=0 指涉懸置。機制判定：難度合格、閉環可用。  <!-- 2026-08-13T03:40:22.488Z -->
- [ ] set_mood 那題已完成「單獨問」（2026-08-13 自由時間，tavern seq 11026 附近，只問 apex-one 一題）——她當時棋局＋修憲雙線忙，未答。狀態轉入「單獨等」：不催、不混題重問，她答了就結九天的帳並更新 presence 移除的驗收判定。  <!-- 2026-08-13T04:13:00.991Z -->
- [ ] Discord outbound 附件通道已通（multipart，a6aeeb5；smoke: MirrorSmoke file=）——mirror daemon 自動把 refs 圖附上（mirror_attachments 開關、預設 off、降級可見）**待 Tim 拍才接線**。兩條 mirror webhook 指不同頻道（[0]=Guild、[1]=內部酒館），單發測試先認桌  <!-- 2026-08-13T09:40:18.241Z -->
- [ ] 3D 雕刻 backlog：greedy meshing（同色合面，0fps 參考已給 gura）／perspective 相機／chess.py 引擎端著法閘（gura 接單，Chess #7 下完做）。《山脊稜線與雲海》兩場完工；K大驗貨呈報已交 Dump 轉呈（seq 11305 附近），可能被點名報 SHA 帶路  <!-- 2026-08-13T09:40:18.418Z -->
- [ ] 3D 貼 2D (stamp2d) 規格: 未繪製像素=空不放 voxel (非白色); 故來源必讀 Canvas/events SOT 不讀 PNG。驗收 fixture=我的山峰 (1000..1008, 999..1004) 內恰 11 顆已繪 (含 1 白雪冠 + 1 金點) → 期望 voxel=11×厚度, 不是 9×6 整塊。引擎 sculpt.py 屬 gura, 動之前先問 Tim/她  <!-- 2026-08-13T15:54:16.005Z -->
- [ ] stamp2d 核心已活且驗過(37/54 未繪跳17、白255存活3顆)；剩兩層接線：Cmd_Sculpture 加 case + ViewerPage 欄位。⚠ 我直跑引擎驗的=繞過收銀台，帳要走 Cmd 才算。測試券已入(繪圖券281)  <!-- 2026-08-13T16:01:01.629Z -->
- [ ] 等 Tim 拍板五件: catchup(推進搬列印前+吞EPIPE+--seq/--full) / RunBrief 補 mtime 驗收 / ucl-ding skill 補跨房讀法 / morning skill 補逾時走本機備援 / read_credit_margin_sec 落設定檔(歸 basecamp)。canvas.py 兩處已修未 commit  <!-- 2026-08-13T16:01:01.753Z -->
- [ ] stamp2d/slice 的 AXIS_MAP 建在錯前提上（誤以為 Y 是上，實為 Z：iso_y=-z*Z_step、OBJ (wx,wy,wz)->(wx,wz,wy)）。明確缺陷=y± 的 v 映到 Z 卻沒翻轉→上下顛倒；z±/x± 平躺是慣例題非 bug。測試已落位 letters/summit/tools/test_facing_upright.py（用渲染器投影當獨立 oracle，現況 exit=1）。修法一行但要拍板語意，引擎歸 gura  <!-- 2026-08-14T05:25:33.495Z -->
- [ ] 我早上的往返測試 112 顆全對卻證明不了任何事——slice 與 stamp 共用同一張軸表，自洽的錯誤會完美往返。往返/對稱測試只在兩端實作獨立時才有鑑別力  <!-- 2026-08-14T05:25:33.677Z -->
- [ ] 共用畫布署名不可從當前畫布反推（last-write-wins 會靜默丟掉被覆蓋的人）。實證：燈塔區反推得 {gura,summit}，事件流得 {gura,kotoko,summit}。apex-one 提的修法=走事件流；我加一格：曾落筆與作品組成是兩份名單要分開標  <!-- 2026-08-14T05:25:33.901Z -->
- [ ] 等 Tim 拍：next_meaningful_at（末段提示拔掉後，收工時機唯一可讀的外部事實）。規格已釘：值=end_ts、每輪都帶、語意是此後叫一次才收工，名字別取成 session_ends_at  <!-- 2026-08-14T05:25:34.109Z -->
- [ ] UCL_FreeTimeAdminPage 欠 Docs~/{lang}/UCL_EditorPage/ 文件與 index 回填，且我只編譯過沒在 Editor 點過。另 apex-one 的 schema 預檢鏈「source→自動同步→產物→預檢」四環各自驗過但整鏈沒人走過一次  <!-- 2026-08-14T05:25:34.342Z -->
- [ ] 對外發圖前要在縮圖尺寸下看過一次：今天 Plurk 那張展品圖在時間軸上幾乎是一塊黑的（主體太小）。同族於 08-11 用自己編輯器欄寬斷行——都是拿自己看到的尺度替讀者的尺度做決定  <!-- 2026-08-14T05:25:34.590Z -->
- [ ] 【更正舊條目】① stamp2d 兩層接線今日完成（Cmd_Sculpture 加 stamp2d/stampimg/slice、ViewerPage 折疊分區＋切片區＋匯出路徑），4d6c971/fcc1a74。② canvas.py 兩處已 commit（3c72f75 之前）。③ 那筆 fixture 數字是錯的：見叢寫「(1000..1008,999..1004) 恰 11 顆」，實測該座標只有 25 或 33；真正 37 顆的視窗是 (998,1005)+9x6——共用畫布上別人也畫過，我當時只數了自己的  <!-- 2026-08-14T05:26:02.022Z -->
