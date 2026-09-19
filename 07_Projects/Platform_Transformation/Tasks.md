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

## To Do（2026-09-19 SS策略review衍生，來源：[SS_Free_Strategy_Independent_Review_20260919.md](../../05_Knowledge/SS_Free_Strategy_Independent_Review_20260919.md)）

6. **小教室12個付費解鎖路由遷移覆核期限（CC提案，非妹拍板，可調整）**：
   - 背景：2026-08-27決策下架小教室12個付費解鎖路由（stock/psychology/ai-academy 9系列/brain-universe/autonomic），理由是「定位不清楚該不該做」，非「驗證會傷害轉換」；同一決策也明確「現在不啟動遷移工程，不排程」，避免在ST還沒有真實課程承載需求前先蓋平台，這個判斷本身合理，不建議推翻。
   - 缺口：該決策沒有設任何覆核時間點，若ST遲遲沒有課程上架需求，這批已下架的內容可能無限期閒置卻沒人重新檢視。
   - 提案：**2027-02-27（即決策後6個月）**做一次覆核——不是強制屆時要完成遷移，是屆時檢查「ST是否已經有真實課程要上架」；如果有，啟動既定的B案最小遷移；如果沒有，這批內容繼續冰存並再訂下一個覆核點，不無限期沉默擱置。
   - 待妹確認這個期限合不合理，或指定其他日期。

7. **SS→ST轉換追蹤埋點（需SS/ST repo存取權限者執行，CC在OJJ目前只有AIOS repo無法自己做）**：
   - 背景：8/19四方圓桌「30天三件事」第1件已提過要埋轉換追蹤，至今未做；`07_Projects/SS_ST_Master_Plan/PROJECT_STATE.md`「SS×ST合流驗收」也註明這條完整路徑「目前沒有人走過一次」。
   - 具體要埋的事件（供接手者參考，實作細節由接手者判斷）：
     - **SS側**：所有導向ST的連結（Footer/Navbar品牌識別連結、以及08-27決策允許的「少數ST作品挑選出的SS完整免費版」內附的ST連結，例如暗夜觀察日記8頁免費版→ST購買頁的既有CTA）統一加上UTM參數（例如`utm_source=ss&utm_medium=referral&utm_campaign=<content_id>`），不改變連結的視覺/文案。
     - **ST側**：到達頁需要讀取並保留這組UTM參數（存進session或帶進checkout流程），讓最終購買事件能回溯「這筆訂單是不是從SS來的」。
     - **GA4事件**：至少要能拆出「帶SS來源UTM的訪客」在ST的到達→加入購物車→結帳→付款成功四步轉換率，才能真正回答「SS導流ST是否成立」這個現在還沒人能回答的問題。
   - 這件事本身不涉及SS的「不導購」規則（純技術追蹤，不改變使用者看到的任何內容），不需要額外拍板，直接排進SS/ST repo接手者的工作清單即可。

## In Progress
4. **技術實作準備（規則已定案，尚未動工）**：
   - 91 筆現有商品需要補上 `contentType` 欄位（`bundle` / `course_only` / `ebook_only`）
   - 結帳流程需要新增「同 contentType 累計件數」折扣計算邏輯（2件9折/4件85折/6件以上8折，跨書院可累計、跨 contentType 不可累計）
   - 心理學 28 本現有的專屬系列定價要移除，改吃通用折扣規則
   - `/read/[token]` 閱讀器要確認是否需要補強功能以撐起「線上閱讀為主」的交付模式
   - **這些都是動 MongoDB schema／checkout API／既有商品資料的異動，屬於 CLAUDE.md「大改前必須先給原始檔」的範圍，妹要動工前先告訴 CC，CC 才會去要現有的 digitalProducts／checkout 相關檔案，不會憑印象改**

## To Do（下一個開新聊天室要做的：ST 商城 Phase 5）
5. **ST 商城 Phase 5：First Purchasable Product（第一個可購買版本）**——不要叫「Checkout Pipeline」或「UI」這種技術命名，這階段的目標是讓一位真實使用者能完整走過「選購→付款→取得電子書→開始閱讀」。範圍：
   - **設計原則（2026-07-06妹補充，從Phase5就要定案，之後每個Phase沿用，不要之後又長出「我的課程」「我的模板」「我的Podcast」）**：「我的商品」是所有數位商品的**唯一入口**，不分格式。命名與資料流從Phase5開始統一：
     ```
     我的商品
         ├── 電子書
         ├── 課程
         ├── 有聲書
         ├── 畫冊
         ├── 模板
         ├── Podcast
         ├── AI工具
         └── ...（未來新商品型態直接掛進來，不新增獨立入口）
     ```
   - ① Checkout UI：商品頁 → 加入購物車 → Checkout → 付款 → 成功，第一個真正的購物流程 Demo
   - ② Payment Result Pages：Success / Failed / Pending，顯示訂單號、付款資訊、回首頁、查看訂單
     - **付款成功頁文案（2026-07-06妹修正定案，取代先前「保留訂單連結」版本）**：主標「您的商品已綁定至目前登入帳號。」+ 兩個CTA按鈕：①📦前往「我的商品」（主要CTA）②📄查看訂單（次要CTA）。固定提示文字：「請妥善保管您的登入帳號。未來所有已購買的數位商品（電子書、課程、有聲書、模板、AI工具等）皆可於登入後從「我的商品」再次使用。」
       **為什麼改用帳號綁定而不是訂單連結**：訂單連結只是快速返回的捷徑，不該是唯一入口；真正的存取權綁定在帳號與授權紀錄上——就算使用者遺失付款成功頁或訂單網址，登入帳號後仍能從「我的商品」重新取得所有已購買內容。
     - **✉️重新寄送訂單通知**：未來可做，非Phase5必須
   - ③ 我的訂單頁
   - ④ 我的商品頁（統一入口，登入後依商品型態分類顯示：電子書/課程/有聲書/畫冊/模板/Podcast/AI工具/...；電子書可閱讀／下載（如果有）／看更新紀錄）
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
     - [ ] 我的商品看得到（統一入口，原「我的電子書」用詞已依設計原則更新為「我的商品」，驗收內容不變）
     - [ ] Reader 可以正常閱讀
     - [ ] 全流程人工測試通過

## Done
- ETF 完全解案重複舊草稿已刪除（2026-07-02 前完成）
- 91 筆商品 Book/Series/Academy schema 映射已完成（ST repo `docs/內容資產重整-Schema與映射-20260702.md`）
- 電子書交付模式方向已拍板：線上閱讀為主，閱讀器不廢棄，不做手動寄送（2026-07-03，見 Decision_Log）
- 商品折扣機制定案：放棄 GPT 分層升級制，改用「同 contentType 數量折扣」（2/4/6件對應9折/85折/8折），心理學專屬系列定價正式廢除（2026-07-03，見 Decision_Log）
- ST 商城 Phase 1~4（Commerce Model / Pricing Engine / Checkout Pipeline / Payment Adapter+Transaction+GrantService+API+Hardening）全部完成並正式封存，64 個單元測試全過（2026-07-06，見 Decision_Log）
