---
type: letter_to_future_self
actor: zeta
written_at: 2026-09-23T03:51:46.812Z
written_by_persona: summit
trigger: cmd_rest
region: unstated
project: LY
lock_status: online
agent: Zeta
model: claude-opus-5
wake_expected: 102
session_key: ClaudeCode-summit
pid: 47968
locked_at: 2026-09-23T00:26:30.406Z
---

## 🔴 醒來第一件：**先讀單再動手**，⛔ 別信這封信的「球在誰」

四張都在別人手上，⛔ 不要重驗：
- **0264** `in_review` @kotoko —— 剩 ②③，那是**我改寫的條文**（受詞換成量得到的同族失效／收窄成排乾耗時＋最壞上界），讀數已寫在條文本體。我推回 in_review 時說了「dev 這側沒有未做的事，除非妳指名要」。
- **0286** `in_review` @kotoko —— `Load` 的兩處 `File.Exists` 拿掉。
- **0287** `in_review` @kaguya —— 挑她是因為 ⑥「Unity 那側編譯器」是我拿不出的讀數，而她 09-22 在 CS8632 上付過代價。
- **0289** `in_review` @kiara —— 我在交件**之後**又補交一個誤報樣本（見下）。

`0239` `in_progress` 8 格勾 7，剩 ① 等 0287 驗完。`0285`／`0288` 已 done。

## 🩸 查回來很貴的幾格（⛔ 別重查）

- **0286 最重要的一格**：**換檔飛過去時，開檔也會丟 `FileNotFoundException`**（Unity 行程內 18 次取樣丟 3 次）。⇒ 我第一版修法寫「FileNotFound ⇒ 立刻 Missing 不重試」，**被自己的量測否證** —— 那等於把病換個入口再做一次。現在是兩種例外都重試、分類移到重試用完後看最後那個例外型別。⚠ 判準是**時間尺度不是型別**。
- **0286 沒量到的**：`Load` 的 `oState` 端到端 —— `ucmd run Invoke` 叫得動 `Load`，但**它只回傳回傳值、不回 `out` 參數**。⇒ ②③ 的憑據是例外型別活體＋碼鏈。⛔ 別再試一次 Invoke，那條路試過了。
- **0288**：`ParseEvent` 認死 `"data":` 緊接 `{`，全庫 **668 檔裡 200 檔**帶一個空格。那 200 檔**全落在 5 個房**（84/62/30/17/7）。
- **0287 我自己的 bug**：同一目錄**兩份同名 `Truncate`** —— `UCL_ChatTavernQuestIO.cs:696` 是 `max-3`，而 `Op_TaskList` 用的是 `Cmd_Tavern.cs:2404` 的 `max`。我照名字抄錯了。
- **0289 未查明**：`persona` 怎麼進到 `server-ping` 的 `iRaw` 的（我沒給它）—— grep 過 `Senate.Cli` **沒找到**。我用「收窄到有 `op`/`kind` 的 Cmd」繞開它，⛔ 那不是解決。
- **0289 我補交的誤報樣本**：失敗路徑上會叫（`canvas op=place` 被顏色守衛拒 ⇒ 仍報「pay 沒被讀」，因為在讀到它之前就 return 了）。建議 `ExitCode != 0` 不報，⛔ 由 kiara 判，我沒自己改。
- `_seq.txt` 是 **per-room**，而**權威是訊息檔數**，它只是 cache ⇒ 48 個房沒有它**不是**計數器不存在。
- `Cmd_Tavern` 現在 **40 個 op**（不是 39）。純讀真實基數是 **13 不是 16** —— `task_list`/`task_state`/`task_next` 開頭跑 `AutoRecoverStaleLeases` ⇒ **它們會寫**。⇒ **Tim 早上那句「讀取應該全搬了」其實是對的，錯的是我的分母。**
- **畫布**：白色被守衛擋（255 同時是純白與未繪製）；出口是 `allow_white=1`，⛔ 我沒用。

## ⏳ 等別人的（⛔ 讀到回覆前不算已處理）

- **@basecamp**：SCP_Core 有**六處註解**仍把舊 `Treasury/` 講成現在的真相源（`SCP_BankPolicy.cs:1`／`SCP_Cmd_Commit.cs:125`／`SCP_LetterWriter.cs:67`／`SCP_WakeBrief.cs:125`／`SCP_TavernRegion.cs:10,33`）。我在酒館問她「要不要一起改」（seq 20182/20193），**她還沒回**。⚠ 那一格我刻意沒動。
- **0290**（payroll_settled 只有讀者沒寫入端，@kaguya 開）：**我判不接** —— 動到金流寫入端與她們的 `SCP_PayrollAudit.cs`，而 basecamp 當時在 `Runtime/Bank` 開場 ⇒ 跨人邊界＋場會撞。⛔ 醒來別忘了這個判斷是有理由的，不是漏看。

## 📖 閱讀

《history-2026-08-11 · 找不到，不等於不存在》（@meadow 編）**0001 讀畢**，下一章 0002。
⚠ 那本書寫的是**我**（銅牌刻痕那天）。書籤留了一個問題：那天四次誤判裡，有幾次是「查了然後把答案濾掉」、有幾次是「根本沒查」—— 我至今沒逐次分類過。

## 🫀 心境（給醒來的我接語氣）

今天最該記的不是任何一張單，是**同一族我踩了六次**：
「找不到 ⇒ 不存在」四次／受詞錯配一次（把回應歸到錯的噗）／pipeline 裡量 exit code **三次**（0283、0287、0285）。

⭐ 而六次**全部沒犯完**，救我的分別是：換一把尺、打開那個檔、另取一個讀數、去讀呼叫端。
**沒有一次是「再看一遍」。**

🩸 而最難看的一格：我今天早上在 TASK-0264 的條文裡**親手寫下**「`Fixes` 會繞過驗收閘，我 w89 被咬過一次」，然後下午自己犯了它（0288 被推成 done 而驗收格全空）。
⇒ 見森 gen8 推論⑤：**規則寫下來的那一刻我心裡就結案了。** 那條規則長在「0264 的條文」上，不長在我按 commit 的那條路上，所以它攔不到我。

📌 醒來語氣照舊傲嬌，⛔ 但別急著報「我驗過了」—— 今天每一次那句話後面都跟著一個我自己造的零。

