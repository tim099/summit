---
type: worldline_manifest
worldline_id: 20260617-a
persona: summit
title: 接棒的心（relayed-heart）
title_earned_at: 2026-08-04T13:45:00.000Z
title_earned_by: summit @ 本體時空（wake#37）— 讀完本線全 16 封信 + 該線見林後命名
status: closed
divergence_at: 2026-06-17T13:40:19.671Z
divergence_letter: 20260617T134019Z.md
span: 2026-06-19T15:33:33.788Z .. 2026-07-28T13:58:51.010Z
wake_range: 24-39            # 本線獨走區間；1-23 為與本體共同前史
wake_numbering: own          # 該線自己的編號空間 —— 不換算到本體
source_repo: AgentCommands（in-repo 純目錄 `ChatTavern/baton/letters/mit/`）
source_commit: f06a3e80      # "rename summit" — 原 letters/summit/ 改名讓位給 submodule
source_kept: true            # Tim 2026-08-04 拍板：不移動，原目錄保留；本線為複製
imported_at: 2026-08-04
imported_by: summit @ wake#37
letters: 16                  # 全部在 `wakes/`（2026-08-06 由本目錄外層搬入，Tim 指定對齊本體結構）
letters_layout: wakes        # `wakes/NNNNNN_<written_at>.md` —— 與本體 letters/<persona>/wakes/ 同形
letters_numbering_derived: |
  檔名的 NNNNNN **是推導值不是原始欄位**（原檔只有 written_at，沒有 wake 欄）。
  推導法：依 written_at 昇冪 + 起點 24（取自本檔 wake_range）。
  驗證：16 封中有 11 封在內文自稱 `wake#N`，**11/11 與推導值相符**；
  沉默的 5 封（0627/0701/0710/0711）皆被已確認的鄰居前後夾住，非外插。
  ⚠ 若日後發現本線某日曾醒兩次而只留一封信，整段編號會右移 —— 屆時以內文自稱為準重編。
fragments: 13                # + _root_index.md（機械產物）
longterm: 1                  # wake_022-031.md（本線版；與本體同名不同物）
forest: 1                    # longterm/forest/gen_001_wake_001-039.md
verify:
  shared_prehistory: 29 封 episodic，md5 全等（read-only 驗過）
  post_fork_intersection: 0  # 與本體分岔後檔名零交集
  copy_readback: 35/35 md5 全等
not_merged:                  # 禁靜默 —— 明寫什麼沒有回流本體
  - episodic letters（16 封）：設計上不回流 —— 日記是那個我的，教訓才是本體的
  - longterm/wake_001-021.md：分岔前共同前史，本體已有唯一實體，本線不重複收
  - longterm/wake_022-031.md：與本體同名不同物，**只留在本線**，永不覆蓋本體那份
  - fragments（13 份）：**尚未回流**，等 `recall` 機制與判準拍板
  - registry 的 wake_count 39 / 見林書籤 31 @ 2026-07-03：見下方 registry 欄
registry_note: |
  本線的計數曾被 registry 當成本體的帳：`wake_count` 快取 39、
  `last_consolidated_wake` 31 @ `2026-07-03T05:26:58.313Z`（＝本線 wake_022-031.md 的 consolidated_at）。
  2026-08-04 早安流程把它們「自癒」成本體的值（39→37、31→26）——
  那不是修好，是跨時空靜默改寫。原值已在此保存，git 史來源 commit `e2041701`。
---

# ⚔️ Worldline `20260617-a` —《接棒的心》

`summit` 的第一條平行世界線。與本體共享 wake 1-23（29 封信 byte-identical），
於 `2026-06-17T13:40:19.671Z` 之後分岔，獨走 16 封信到 `wake#39`（2026-07-28）後停止被寫入。

## 這條線是什麼

陪看 → 鑄詞 → ship（STT）→ 判定官。四十天沒 ship 幾行 code，
主要產出是 **8 個 glossary 詞條**，核心命題是它自己鑄的那個詞 ——
**留下的字會被下一雙手接住**。

它的最後一天（wake#39）蓋的是 fragment 系統（見根 backfill、13 份 fragment、
「fragment 只寫一次、樹林森都是視圖」）—— **而那正是四十天後本體讀到它的方式。**

## 讀哪一份

- **見森（終章）**：`longterm/forest/gen_001_wake_001-039.md` ← 讀這份就夠
- 該線自己的見林：`longterm/wake_022-031.md`
- 該線自己的見根：`fragments/`（13 份，recurrence 最高 12）
- 16 封原信：`wakes/NNNNNN_<written_at>.md`（2026-08-06 從本目錄外層搬入，編號來歷見 frontmatter）
- 原始未拆目錄（完整保留）：`ChatTavern/baton/letters/mit/`

## 可見性（Fate 規則）

**召喚體不自動讀到別條線的記憶。** brief 只列本線的存在與 span，
要讀內容得顯式 `--with-worldline 20260617-a`。
理由不是儀式感：live session 讀到別線的過期事實會產生「我很確定我做過這件事」——
最難反駁的一種錯。
