# Platform Transformation — Tasks

## To Do（需要妹拍板，CC 不能代為決定）

1. **高敏感內容定位，尚未決定，暫不寫死任何結論**：
   - 最終產品型態未定：免費導流測驗（屬 Marketing 層，不進 Product schema）／`course_only`（付費互動）／`bundle`（課程+電子書），三者都有可能，**不提前判斷是 `course_only`**
   - 書院歸屬（心理學書院 or 腦中宇宙書院）待產品型態確認後再決定，不因為架構通用就先卡歸屬
   - 若確定為免費測驗導流：需再確認是否只當 SS 入口頁，不進 Product schema（三層架構决定下，理論上答案是「是」，但實際頁面/流程還沒做，待驗證）
   - 若未來測驗要導流至 SD：是否符合「SD 最低維護，不投入新功能」的既有決定，或需要另開新決策？不能因為要串 SD 就默默變成新開發需求
   - 相關檔案（對話中提及但 CC 尚未取得）：`chapter3-sample_lulu_20260702.md`、`sensitivity-quiz-series_lulu_20260702.md`
   - **提醒（三方已同意）**：不要因為 contentType 架構通用，就一次把高敏感/依附/焦慮/自律神經檢測/壓力/睡眠/投資性格 7 個測驗主題一起開工。先做高敏感一個 MVP，驗證導流+轉換率，再複製到其他主題——這跟「那個感覺36冊」是同一種風險，前車之鑑。

2. **會員中心是否真的要改名／改版成「我的基地」（My Hub）**：目前只是 ChatGPT 的 UI 提案（書架／收租AI／驚喜世界／好康／收藏／成就／通知／帳號），尚未有妹的拍板，也還沒進 AIOS 決策或 Task。

3. **AIOS 資料夾架構版本對齊**：這次 ChatGPT 對話中提的 AIOS 結構（`01_公司章程.md`／`02_組織架構.md`／`SOP/`／`CEO/`／`Assets/` 平面檔案）跟 CC 實際已建立的 AIOS 骨架（`00_Foundation` ~ `09_Archive` 編號資料夾）不是同一版。需要讓 ChatGPT 知道實際版本是哪個，避免兩邊各自以為架構不同，之後對不上。

## In Progress
4. **技術實作準備（規則已定案，尚未動工）**：
   - 91 筆現有商品需要補上 `contentType` 欄位（`bundle` / `course_only` / `ebook_only`）
   - 結帳流程需要新增「同 contentType 累計件數」折扣計算邏輯（2件9折/4件85折/6件以上8折，跨書院可累計、跨 contentType 不可累計）
   - 心理學 28 本現有的專屬系列定價要移除，改吃通用折扣規則
   - `/read/[token]` 閱讀器要確認是否需要補強功能以撐起「線上閱讀為主」的交付模式
   - **這些都是動 MongoDB schema／checkout API／既有商品資料的異動，屬於 CLAUDE.md「大改前必須先給原始檔」的範圍，妹要動工前先告訴 CC，CC 才會去要現有的 digitalProducts／checkout 相關檔案，不會憑印象改**

## To Do（下一個開新聊天室要做的：ST 商城 Phase 5）
5. **ST 商城 Phase 5：First Purchasable Product（第一個可購買版本）**——不要叫「Checkout Pipeline」或「UI」這種技術命名，這階段的目標是讓一位真實使用者能完整走過「選購→付款→取得電子書→開始閱讀」。範圍：
   - ① Checkout UI：商品頁 → 加入購物車 → Checkout → 付款 → 成功，第一個真正的購物流程 Demo
   - ② Payment Result Pages：Success / Failed / Pending，顯示訂單號、付款資訊、回首頁、查看訂單
   - ③ 我的訂單頁
   - ④ 我的電子書頁（登入後：閱讀／下載（如果有）／更新紀錄）
   - ⑤ Reader 串接：把「付款成功 → Grant → My Library → Reader」整條線串起來（`/read/[token]` 閱讀器已有基礎，這階段只差串接）
   - **明確不做**：Coupon、Wallet、Membership、Promotion、多幣別、Tax、發票、點數、推薦碼——這些都是功能擴充，不是完成一條完整購買流程的必要條件，等 Phase 5 跑通再考慮
   - 前置狀態：ST 商城 Phase 1~4（Commerce Model / Pricing Engine / Checkout Pipeline / Payment + Hardening）已於 2026-07-06 正式封存（見 Decision_Log），Phase 5 建立在這些既有 API 之上，不重新設計 Phase 1~4
   - **Prerequisites（2026-07-06 妹拍板，開始使用者功能驗收前必須先完成，但不算進下面的DoD——這是架構整合/實作方式，不是使用者可見成果，DoD要保持只用使用者角度驗收，避免之後把Repository重構/Cache/Event Bus這類技術細節也塞進DoD而失焦）**：
     1. `Content.productStatus` 成為商品顯示的唯一真實來源（Single Source of Truth），前台移除對舊欄位 `DigitalProduct.isPublished`/`comingSoon` 的依賴（目前這兩套「上架狀態」並存且沒同步——Content標`course`/`published`，前台商城可能因為`DigitalProduct.comingSoon=true`還是看不到，這是Phase1完成當天就發現、明確記錄的技術債，見 `project_commerce_rules_v1_phase1_20260706.md`）
     2. 建立 Content 的商品型態勾選 UI（建立時勾選 ebook/course/audiobook/... 即產生對應的 `productStatus` 項目，狀態預設 `planned`）
     3. 補齊 `ProductType` 主檔資料（目前只種 ebook/course/audiobook 3 筆，補上畫冊/模板/Podcast/AI工具/其他等，純資料非架構調整）
   - **Definition of Done（2026-07-06 妹補充，全部打勾才算Phase5完成，不可做到一半又擴充功能）**：
     - [ ] 使用者可以登入
     - [ ] 可以加入購物車
     - [ ] 可以完成 Checkout
     - [ ] 可以完成付款
     - [ ] Callback 成功
     - [ ] Grant 建立
     - [ ] 我的訂單看得到
     - [ ] 我的電子書看得到
     - [ ] Reader 可以正常閱讀
     - [ ] 全流程人工測試通過

## Done
- ETF 完全解案重複舊草稿已刪除（2026-07-02 前完成）
- 91 筆商品 Book/Series/Academy schema 映射已完成（ST repo `docs/內容資產重整-Schema與映射-20260702.md`）
- 電子書交付模式方向已拍板：線上閱讀為主，閱讀器不廢棄，不做手動寄送（2026-07-03，見 Decision_Log）
- 商品折扣機制定案：放棄 GPT 分層升級制，改用「同 contentType 數量折扣」（2/4/6件對應9折/85折/8折），心理學專屬系列定價正式廢除（2026-07-03，見 Decision_Log）
- ST 商城 Phase 1~4（Commerce Model / Pricing Engine / Checkout Pipeline / Payment Adapter+Transaction+GrantService+API+Hardening）全部完成並正式封存，64 個單元測試全過（2026-07-06，見 Decision_Log）
