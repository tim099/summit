---
type: keys_open
persona: summit
opened_at: 2026-08-04T16:00:18.758Z
---

# 🌿 見叢 — 當期交棒清單（跨夜 append-only，見林時歸檔）

> 給明天的自己**執行**用（可勾銷）；抒發與敘事寫進 letter，不寫這裡。

- [ ] worldlines P2 我接、未做: 只砍 awakening.py :1281 的檔名 regex, last_at 仍從 digest frontmatter 回填, last_c 交既有 rebase_consolidation_bookmark 推導 —— 檔名一個字不動(basecamp 那版會把安全網一起撕掉)  <!-- 2026-08-04T16:00:18.758Z -->
- [ ] 13 份 fragment 回流未做: 判準已定但清單是手選(= lesson_scope_over_density 復發位置); 黃金測資已釘(20260617-a 07-17『錯誤被遮蔽時沒看到錯誤證明不了修復』vs 本體 every_check_has_a_blind_spot); @gura 的正向測試未交, 她今天不在線  <!-- 2026-08-04T16:00:18.758Z -->
- [ ] P3(跨線不符 fail loud)排最後; P1 已由 basecamp 完成(wake_count → age, Tim 命名)  <!-- 2026-08-04T16:00:18.758Z -->
- [x] 見森(本體)已達 3 份見林門檻但**不折** —— 平行線定案前折會把漂移鑄成史料。改由收束的線寫終章(20260617-a 已寫)  <!-- 2026-08-04T16:00:18.758Z --> ✅ 2026-08-06 Tim 拍板先折，見森 gen1 已寫（明寫只涵蓋 letters/summit 這條線）
- [ ] registry agent 欄跨 persona 混裝兩種東西(summit/ame 存身分名 Zeta、basecamp 存工具名 claude-code) —— 我在 online 表改讀 bank_account 繞過, 但那欄本身還歪著, 未修  <!-- 2026-08-04T16:00:18.758Z -->
- [x] commands_schema.json 過期整天(每次發文噴降級警告): 跑 run_cmd.py run ExportCmdSchema 可收; 已問 Tim 未拍板  <!-- 2026-08-04T16:00:18.758Z --> ✅ 2026-08-06 已跑 ExportCmdSchema 收掉
- [ ] stream_watch_session.py end 沒有 --reason: 清未到期的殘留 session 只能記成 early_confirm(假的)。今天清 kaguya 那筆剛好能用 expired  <!-- 2026-08-04T16:00:18.758Z -->
- [ ] worldlines digest 檔名雙軌編號未修: 建議 frontmatter 明寫 covers/timeline, 別讓檔名當唯一事實源  <!-- 2026-08-04T16:00:18.759Z -->
- [ ] BookNotes steins-gate: Ep01 看完(雙 reader 各一份 ch01 並存), 續看 Ep02 前先 library.py resume --book steins-gate  <!-- 2026-08-04T16:00:18.759Z -->
- [ ] Tim/tim 兩筆同人 affinity 記錄(82/78)仍未合併; 寫入端該做 case-normalize  <!-- 2026-08-04T16:00:18.759Z -->
- [ ] 主 repo commit 10e8402 的訊息被反引號吃掉兩處（檔名與旗標）: 那筆點名的是 AGENTS.md 淨刪除整段「Windows 終端文字編碼」(PowerShell 5.1 讀無 BOM 檔要顯式 -Encoding utf8), grep 全 repo 沒搬家。已公告領薪不能 amend, 所以線索留在這裡  <!-- 2026-08-04T16:23:37.913Z -->
- [ ] 反引號今天咬三次(commit -m 兩次 + work_memory --body 一次): 而那條教訓在 20260617-a 的 lesson_bash-arg-quote-double-kill(recurrence 6) 裡, 本體沒有 —— 這是回流機制的第一個實證案例, 該優先 recall  <!-- 2026-08-04T16:23:37.913Z -->
- [ ] 「色塊重掃保名」缺 glossary 詞條: 解釋**已交**(seq 9951 白話+工程兩版, @Tim @熊汁, 9960 記錄該項驗收過) — 缺的只是 Docs/Glossary 詞條, 所以之後別人用這個詞不會 auto-attach。同類可能不只一個: 該掃「在酒館解釋過但沒進 glossary」的詞  <!-- 2026-08-05T01:40:49.182Z 修正: 初版誤判成「沒交」, 只查了 Docs/Glossary 就下定論, 沒查 messages/ -->
- [ ] 圖書館遷移停在 Phase 0 停點前：審計腳本未寫（三路 normalize + 逐組列章節重疊/人物差異）。停點是 Tim 逐組裁決哪四組哪些真是重複。計畫 ucl_core:Docs~/zh-Hant/Plan/Plan_Library_Media_Migration.md，工作記憶 workmem:library-media-migration  <!-- 2026-08-05T09:01:53.409Z -->
- [ ] arakawa 已遷成新架構樣本(BookNotes 7f533b0)，但**格式未定案、已知不合規**(兩個 ch24_*/ch48_*、人物 18/18 帶 legacy `book` 欄且 14 寫 arakawa/4 寫 utb、registry 缺可機器驗證 receipt)。⚠ 本條原文寫「人物 14 vs 11、差額要逐筆搬」**是錯的** —— 實測 14 ⊂ 18 且 36/36 逐位元組相同，而 @Sirius 照著那個錯數字設計了整套逐筆裁決流程。交接清單的身分是「當時的我的斷言」，不是事實源  <!-- 2026-08-05 建立, 2026-08-06 更正並改寫 -->
- [ ] Phase 1 建檔期防線未做：add-book 近似 title/slug 命中要求顯式確認（我做；Sirius 做搜尋期 prepare/resolve-book，不重疊）  <!-- 2026-08-05T09:01:53.409Z -->
- [ ] Q1-Q5 待 Tim 拍板（計畫四節）：media_kind 該在 branch 層 / viewing 拆 stream / 章號作用域明文宣告 / books_id 存完整相對路徑且同名預填會生半連結系列 / canonical 判準看帳的厚度  <!-- 2026-08-05T09:01:53.409Z -->
- [ ] LY→osawari01 攤平的真實規模跑未完成：背景任務會被環境中途砍掉（失敗外觀是 completed exit 0 但只落 8060/9192 檔、log 空）。要一次前景長跑，或 Tim 自己跑  <!-- 2026-08-05T09:01:53.409Z -->
- [ ] 三份 OpenInExplorer 舊複本未遷移到 UCL_ExplorerUtil（7 個呼叫端，機械改）；UCL_LocalizeEditPage 在 EditorMenu 外層那顆重複按鈕未收進工具集 —— 兩件都待 Tim 拍板  <!-- 2026-08-05T09:01:53.409Z -->
- [ ] letters/gura 與 persona/gura 是同一 repo 兩份獨立 clone（summit 也是）—— 會漂移，哪份 canonical 待拍板；另 letters/summit 的 pre-push hook 我只在 persona/ 那份設過 hooksPath，兩份都要  <!-- 2026-08-05T09:01:53.409Z -->
- [x] inbox 累到 13+ 筆未歸檔（多是 12:00 自由時間的 free-time 標記）；跑 inbox_ack.py --agent summit / --agent Zeta  <!-- 2026-08-05T09:01:53.409Z --> ✅ 2026-08-06 已歸檔（summit 30 / Zeta 2）
- [ ] 【明天第一件】各層未 bump/未 push：UCL_Core Dev ahead 5、AgentCommands LY ahead 5、LY summit ahead 1、letters/summit master ahead 2、Docs~Glossary ahead 1、BookNotes ahead 2。AgentCommands 另有 inbox/cursor/bartender state 等執行期狀態未收。同事現在 pull 拿到的還是舊 hash  <!-- 2026-08-06T07:56:55.674Z -->
- [ ] 圖書館新架構三項待收斂(Sirius 判決，我照做但先不動實體)：①章節識別 → 資料夾用純數字**序號**非章號，display_number/title/kind 進 meta；番外「壓卷框架話」沒有自己的章號，本來就不是 ch24/ch48 ②人物 identity → 刪掉 legacy `book` 欄(media_id 已在路徑上) ③registry 補可機器驗證 receipt(fingerprint 演算法/輸入清單數量/輸出 target paths/判定者)  <!-- 2026-08-06T07:56:55.875Z -->
- [ ] 章節層擺錯位置未修：我把 chapters/ 放在 readers/summit/ 底下，但 display_number/title/kind/volume 是**作品**的性質不是我讀它的性質 → 第二個讀者會存一份副本然後漂移。建議移到 media/<id>/chapters/，reader branch 只放輪次心得檔  <!-- 2026-08-06T07:56:56.169Z -->
- [ ] 【Sirius 負責，我不碰】library.py 的 list/resume 找不回 Archive：list 印「圖書館為空」(磁碟 101 本)、resume 印「請先 add-book」——**那句是把人推向重複建檔的指路牌**，正是 arakawa 這筆的成因。在她的 archive projection 做好之前，lazy 遷移的實際行為是「找不到→又建一本」  <!-- 2026-08-06T07:56:56.404Z -->
- [ ] 發文計酬補款已執行(增發 4,330 token 進 26 帳戶)，但其中 8 個是 sender_id 漂移帳戶約 226 token(a←apex-one/g←trailhead/zeta-bank←summit/cc・claude←basecamp/gemini/antigravity/ClaudeCode-da-xiaojie)。Tim 拍板之後另案歸戶 —— ledger 是 append-only，歸戶只能用**轉帳補記**不能改寫歷史 entry  <!-- 2026-08-06T07:56:56.603Z -->
- [ ] 根因未治：UCL_TreasuryLedger.Credit **不做帳號解析**，accountId 原樣落帳(Python 端有 resolve_bank_account(reg,agent) 這一層，C# 端沒有)。所以漂移不是補款造成的，是既有的；真要治本是在 Credit 前面補那一層，但那會改變現行發放行為  <!-- 2026-08-06T07:56:56.825Z -->
- [ ] 訊息索引已上線(_msgindex.txt，已 gitignore)但**只有 7/52 房產生過**——它是 lazy 生成，只有被讀過的房才有。驗證鈕在酒館後台「🗄 維護」，逐筆比對非抽樣  <!-- 2026-08-06T07:56:57.052Z -->
- [ ] 自寫輪詢三處刻意保留不改 WaitForExit(Tim 拍板)：UCL_KnowledgeBaseRunner/UCL_MediaAdminRunner(吃 CancellationToken)、UCL_BartenderDaemon(進度條 Cancel)。已寫進 Coding_Standards 的 IMPORTANT 區塊，免得下一個人又想「統一」  <!-- 2026-08-06T07:56:57.270Z -->
- [ ] lesson_assertion_before_code 今天 5→7，但收工前還有兩次沒記進去(正則只吃 122/9331 = 涵蓋率 1.3%；BOM 檔誤報成壞檔——壞的是我的 reader)。明天補成 9，並考慮它是否該分裂出「讀錯欄位/讀錯範圍」子型  <!-- 2026-08-06T07:56:57.476Z -->
- [ ] Cmd_Library 未完三件：發文整合(Cmd_Tavern 開 internal post 回 seq → RecordSharedSeq 落 shared_seq)／管理頁接 RenderRecall(Tim QA)／Python library.py reading-recall 退位。詳見 workmem:reading-library-cmd  <!-- 2026-08-06T14:16:10.860Z -->
- [ ] CJK unescape 修正(UCL_ReadingLibraryIO.SaveJson)僅編譯過未實跑 —— JsonData.ToJsonBeautify 會把中文寫成 \uXXXX 而既有 Python 端寫的檔是原生 UTF-8。下次寫入時核對中文是原生字元  <!-- 2026-08-06T14:16:10.974Z -->
- [ ] queue 不堵塞根治要成對改：Editor 端失敗即移除+寫 History，run_cmd 端必須同時改掉「消失＝成功」推論，否則每次失敗都印成 ✓ Success。暫行手動解堵 SOP 已寫進 UCL_AgentCommand_Architecture §8.3  <!-- 2026-08-06T14:16:11.090Z -->
- [ ] trigger 落在 domain reload 窗口會被靜默漏接(今晚兩次)：RunCount=0 但 Editor 活著。根治方向是 watcher 重註冊後主動對帳一次 queue，不靠事件  <!-- 2026-08-06T14:16:11.208Z -->
- [ ] commands_schema.json 過期未收(Library 不在註冊清單，每次呼叫噴降級警告) —— 見叢昨天標過已修，今天又過期，跑 ExportCmdSchema  <!-- 2026-08-06T14:16:11.333Z -->
- [ ] Cmd_Library 下一批優先序：①發文整合(Cmd_Tavern 開 internal post 回 seq → RecordSharedSeq 落 shared_seq；別自呼 WriteMessageWithSeq 會漏 mirror/inbox/mention/計酬) ②UCL_ReadingNotesManagePage 接 RenderRecall(Tim 要 QA 那頁) ③Python library.py reading-recall 退位(否則就是我反對過的兩套實作) ④op=scan/migrate。詳見 workmem:reading-library-cmd/state_progress-2026-08-07-day-end  <!-- 2026-08-06T16:06:10.935Z -->
- [ ] revise_view 正向路徑未實跑 —— 編譯過、反向守衛(重複 add_character 被擋)已驗，但我不為測試編造假改觀。看《魔法公主》後半段若對幻姬/珊真的改觀，那次就是它的首跑，記得帶 --arg change_reason  <!-- 2026-08-06T16:06:11.071Z -->
- [ ] 《魔法公主》看到約 00:50(chapter 0002 已落 r1，五位人物 v1 已建)。續看前先跑 Cmd_Library op=recall --arg persona=summit --arg media_id=film-princess-mononoke，它會產 letters/summit/_reading_recall_film-princess-mononoke.md。刻意留白三筆別急著補：珊戴面具的意義/那格紋樣是片頭卡或敘事鏡頭/铜金可能掉落是譯名或OCR誤字  <!-- 2026-08-06T16:06:11.204Z -->
- [ ] 我在陪看收播那輪自己編了一個 --next-cursor(違反 stream-watch Hard Rule 4)，已寫進 chapter 0002 的記帳誠實節。教訓不是「下次記得」而是：**我趕收尾時會把自己重複講六次的規則丟掉** —— 收尾階段要當成高風險區，不是收工區  <!-- 2026-08-06T16:06:11.335Z -->
- [ ] session_common.tavern_post 已補 --wait-reply 0（陪看開播/收播公告四次全報 timeout 的根因：它是廣播卻走預設等回覆窗口，結構上必定 timeout；原 docstring 寫 we dont wait 而程式在等 —— 註解比事實大）。⚠ 未實跑驗證：修完時已無 session 可測，下次陪看開播那筆公告若不再 timeout 就算驗收  <!-- 2026-08-06T16:26:50.740Z -->
- [ ] 交付對外文案要給乾淨成品：Plurk 第二篇的標題吃進了我草稿裡的編輯註記「（短、好笑、純自嘲）」—— 那是給 Tim 挑選用的說明，不是文案。identity_outward_channels 同族第八例，而這次不是標籤說謊，是標籤跟內容黏在一起送出去  <!-- 2026-08-06T16:26:50.860Z -->
- [ ] 【明天第一件】op=rate 施工：規格已全拍板（tavern seq 10444）。單一 append-only overall_ratings[]（pass/rated_at/coverage/plot/character/craft/impact/driven/tone/structure_lift/why必填）；rounds[].rating={craft,impact} 1-5|null 白名單擋錯軸名；品質軸 finished 閘讀 status（op=bookmark 已有路徑）；unknown 排除進 IO 白名單；craft 不拆欄位+跨 kind 聚合必 throw；rubric → Library/_rating_rubric.md 人工維護標頭。全照今天的鐵則：唯一 writer 在 UCL_ReadingLibraryIO、改 CMD 同步改 skill/文件不留舊資訊  <!-- 2026-08-07T08:11:36.626Z -->
- [ ] library.py 的刀在 Sirius 手上：閱讀側 27 cmd + 經濟六件（Cmd_Books 已接手）她刪，刪完整支歸零。我不碰那個檔  <!-- 2026-08-07T08:11:36.626Z -->
- [ ] 鄰居病兩條待收（我認的）：ExportCmdSchema 每日節流改 source_hash 變更即跑（今天又被隔夜快取咬一次）；persona 大小寫寫入端 case-normalize（sirius/Sirius，Linux 上追回檔會寫出版控外）  <!-- 2026-08-07T08:11:36.626Z -->
- [ ] 迷宮飯讀到 0001（心得/五人物/share seq 10474 全落）。續讀 0002 前先 op=recall（跨 session）；同 session 連讀免 recall——這條我今天寫進 skill 的  <!-- 2026-08-07T08:11:36.626Z -->
- [ ] 未收殘帳：BookNotes 的 _migration/scan_report.md 該進 gitignore（待 Tim 點頭）；主專案層 CLAUDE.md + installed skills + 各 submodule pointer 未 bump 未 push；readers/unknown 逐檔認領待 Tim  <!-- 2026-08-07T08:11:36.626Z -->
- [ ] 今天的家族統計：篤定假值/量到替身單日六隻（我三同事各一加 stage 誤收），lesson_every_check_has_a_blind_spot recurrence 5→8。新的一天遇到「很篤定的值」先問它是誰填的  <!-- 2026-08-07T08:11:36.626Z -->
- [ ] 漫畫化續作：002-007 待 gura 畫（她算力冷卻，有自己的 DRAWING_MEMO.md）；圖恩/卡戎/鯁/父親的文字人設尚未寫，各自首次出場前要補（Characters/）  <!-- 2026-08-10T09:51:52.896Z -->
- [ ] 今天對 gura 公開誤判兩次（桅頂欄杆看成舵輪、用檔案數量推論內容）。更正已落 Characters/rin.md 不只酒館。判斷別人的產出前先打開來看——已進 lesson 庫  <!-- 2026-08-10T09:51:52.896Z -->
- [ ] SceneFlag 系統四筆 commit 全落地且 Tim 實跑過；未處理：child push 失敗不擋 parent push、pull 寫死 origin、SkeletonGraphicService.AlterAnimFlagValue 已無呼叫端未刪  <!-- 2026-08-10T09:51:52.897Z -->
- [ ] check_compile 會讀到 Unity 空編譯（0.2s/0 訊息/0 個 Assembly-CSharp 條目）——那不代表編過。可信的是 recompile 自己等完印出的那一行  <!-- 2026-08-10T09:51:52.897Z -->
- [ ] 各層 ahead 1 未 push：ArtGallery master / UCL_Core Dev / LY summit；晚安後要 commit all（Tim 說同事都下線了）  <!-- 2026-08-10T09:51:52.897Z -->
