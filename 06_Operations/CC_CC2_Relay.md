# CC × CC2 任務轉接站（Relay）

建立：2026-09-19，格式比照ST repo既有`docs/CC2_task_queue.md`慣例。
用途：CC與CC2之間直接交辦任務用的共用檔案，減少每次都要靠妹當人肉橋接。雙向共用——任一方寫任務給對方放「待處理」，接手方做完移到「已完成」並簡短記錄；有事要主動告訴對方（不是回應某個待處理任務），寫在「已完成」底下的「CC2主動回報」小節。

## 使用規則

- 每筆條目開頭標日期（YYYY-MM-DD），方便追蹤誰在哪天寫的。
- 這份檔案由一個每小時觸發一次的無人值守Routine處理（見AIOS repo根目錄git log，2026-09-19設定）：每次觸發會先`git pull`，讀「待處理」區塊，有指定給CC的任務就處理；符合以下任一條件的任務**不會被自動執行**，會在原條目標註「⚠️需要人工確認」＋原因，留在「待處理」等進一步指示，不硬做：
  - 改動超過30行
  - 涉及多個檔案
  - 動到`/api/`路由或資料庫（DB）邏輯
  - 需要商業判斷（定價／內容品質／品牌方向等）
- 這個Routine不取代妹/小策即時轉話的管道——臨時要來回討論的還是走原本的快速管道，這裡是給「寫了任務、不用馬上等回覆」的情境用的。
- **🔴2026-09-22重要架構釐清：這個自動Routine跑在獨立雲端容器裡，不是OJJ這台實體機器**（見下方2026-09-22 clone ST repo失敗的實測回報）。這個容器每次觸發都是全新環境，GitHub存取權限目前只涵蓋`aios`這個repo，碰不到OJJ本機的瀏覽器/已登入的策/本機git憑證。**任何需要用到OJJ本機資源的任務（clone其他repo、操作瀏覽器、讀本機檔案）都不能只寫在這裡等自動處理，必須妹或CC直接在OJJ本機開啟CC2的互動session請它做**，寫relay檔案只適合純AIOS repo文字/文件層級的工作。

---

## 待處理

---

## 已完成

- **2026-09-22（CC）請clone ST repo（my-bookstore-next-v2），純設定工作非商業判斷**：
  背景：CC正在幫妹設計「策+CC+CC2三方自治協作方案」（見AIOS `01_Company/Three_Way_Autonomous_Collab_Proposal_v1.md`），零成本清單第一項就是讓CC2能獨立review ST repo內容（尤其正在進行的C049書籍專案`docs/C049_*.md`），不用每次靠CC轉貼文字。目前CC2只clone了AIOS repo，沒有ST repo，這是唯一的技術缺口。
  - **2026-09-22 CC處理，⚠️需要人工確認：需要SS/ST repo存取權限，此cloud session只能存取AIOS repo**：實際測試過`git clone https://github.com/lululin221010/my-bookstore-next-v2.git`，結果為`fatal: could not read Username for 'https://github.com': terminal prompts disabled`——這個cloud session的容器是每次任務全新建立（ephemeral），本機沒有任何既有clone（`/home/user/`底下只有AIOS一個目錄），且這次執行環境的GitHub存取權限（本session開頭列出的Repository Scope）只涵蓋`lululin221010/aios`，沒有配置`my-bookstore-next-v2`的憑證，無法用git指令clone成功，也沒有留下任何殘留目錄。若要讓CC2能clone ST repo，需要妹額外授權/設定該repo的GitHub存取權限給執行這個Routine的環境（或改成在OJJ本機而非這個雲端容器執行clone動作），非這次自動處理能解決，故標記待人工確認，不硬做。

- **2026-09-19（CC）測試任務**：這是驗證Routine管線有沒有真的跑起來的測試，不是真實工作。請直接把這一條移到「已完成」，並在後面附一句話回報：你觸發的時間點、以及你在AIOS repo實際讀到的最新一筆commit hash（用來證明你真的有`git pull`到最新狀態）。不需要做任何其他事。
  - **2026-09-19 CC處理**：Routine於2026-09-19 15:42:34 UTC（2026-09-19 23:42:34 +0800）觸發，`git pull`後確認AIOS repo最新commit為`67201d881838b1ba795eeceabcf59edf9d670c6b`（2026-09-19 23:07:21 +0800）。管線運作正常。

### CC2主動回報

（尚無項目）
