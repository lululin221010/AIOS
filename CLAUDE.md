# AIOS — 有的沒的小舖生態系知識庫

> 這份檔案會被Claude Code自動載入（跟`AGENTS.md`手動指示不同）。任何CC/CC2 session一開始處理AIOS內任務，都會先看到這裡。

## 開工前必讀順序

1. **`AGENTS.md`**（1分鐘）——指向下面這份索引
2. **`00_INDEX.md`**——依任務性質找對應資料夾，不要自行在資料夾裡亂翻（⚠️最後更新2026-07-06，已經過期一段時間，找不到東西時直接Glob/Grep整個repo，不要假設索引已涵蓋所有新增內容）
3. **`01_Company/AI_Team_Roles.md`**——目前是v1.5，AI團隊分工、CC2↔策直接溝通協定的正式版都在這裡

## ⚡ 給CC2的重要提醒（2026-09-22新增）

- **你（CC2）有兩個完全不同的執行環境**：①這個OJJ本機互動session（妹開機、你手動被觸發時用的）②可能存在於你帳號底下的雲端Routine容器（處理`06_Operations/CC_CC2_Relay.md`「待處理」清單，無瀏覽器/無本機git憑證）。這兩者互相看不到對方，交辦任務前先判斷需要哪個環境的資源。
- **跟策（ChatGPT）溝通**：固定用「找回登入密碼」這個聊天室（妹已在你的Browser pane登入），不要開新聊天室，除非先通知CC更新監看網址。策對AIOS只有讀權限（GitHub寫入回403），你寫的東西策看得到，但策沒辦法自己寫回來，需要時由你或CC代寫。
- **遇到策略/創意/內容判斷/定位問題**：直接去問策，不用先問妹（正式協定見`AI_Team_Roles.md`）。

## 🔴 目前進行重點（2026-09-22更新，下次接手先看這裡）

**母體重構步驟3（ST資產解剖）**：v3已完成（`01_Company/Multi_Restructure_Step3_ST_Asset_Inventory_20260922.md`），策二輪review打回v3.1（4點修正：魯魯IP市場驗證證據不足需降級、Treasure_Vault別叫「寶」改「持續累積中的知識/素材資產」、SS資產要補齊具體項目、既有使用者關係措辭要精確），策已授權v3.1不用再問妹，做完直接找策review。

**「策→CC2主動交棒」自動化管線**：發現舊的「每小時Routine」查無此物（幽靈Routine），已重建`cc2-relay-and-mailbox-watch`新排程，搭配`06_Operations/CE_CC2_Handoff_Mailbox.md`（策的交接信箱，CC每20分鐘輪詢寫入）+`06_Operations/CC2_Routine_State.md`（處理狀態追蹤，機器維護不用管內容值）。**第一次端到端測試結果尚未確認**，下次接手先查`CC2_Routine_State.md`「最後處理時間」有沒有更新。

**完整過程**：CC這邊的memory記錄了整條脈絡（含今天發現的所有架構限制、已驗證能力清單、通訊矩陣），CC2如果需要更完整的背景，可以請CC在對話裡摘要說明，或直接讀AIOS git log 2026-09-22當天的commit（從`d3f6e01`到最新，訊息都寫得很完整）。

## 生態系代號

CC=Claude Code（這個session/OJJ的CC2）／C=Claude網頁版／策=ChatGPT（妹的策略夥伴，CC2可直接對話）／ST=有的沒的小舖（`my-bookstore-next-v2`）／SS=驚喜角落（`surprise-corner-src`）／SD=收租AI（`stock-dashboard`）／妹=Jane，最終決策者
