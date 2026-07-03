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

## Done
- ETF 完全解案重複舊草稿已刪除（2026-07-02 前完成）
- 91 筆商品 Book/Series/Academy schema 映射已完成（ST repo `docs/內容資產重整-Schema與映射-20260702.md`）
- 電子書交付模式方向已拍板：線上閱讀為主，閱讀器不廢棄，不做手動寄送（2026-07-03，見 Decision_Log）
- 商品折扣機制定案：放棄 GPT 分層升級制，改用「同 contentType 數量折扣」（2/4/6件對應9折/85折/8折），心理學專屬系列定價正式廢除（2026-07-03，見 Decision_Log）
