# Platform Transformation — Tasks

## To Do（需要妹拍板，CC 不能代為決定）

1. **高敏感系列歸屬**：放在心理學書院、還是腦中宇宙書院？
   相關檔案（對話中提及但 CC 尚未取得）：`chapter3-sample_lulu_20260702.md`、`sensitivity-quiz-series_lulu_20260702.md`
   目前腦中宇宙書院官方只有「自律神經學系」一個學系，若高敏感也放腦中宇宙，需要新增學系；若放心理學書院，則是第 7 個學系。

2. **ST 電子書交付模式，兩份定案互相矛盾，需擇一**：
   - ChatGPT 這次建議：「線上閱讀為主，PDF 只當備援」，理由是要做平台不是做商品販售。
   - 但 ST 既有紀錄：2026-06-18 已定案「放棄線上閱讀器／訂閱制，改回手動 Email 寄送 epub」；2026-06-28 最新商業模式定案是「EPUB 下載＋SS 書院課程解鎖＝同一商品，不拆賣」。
   - 需要妹確認：`src/app/read/[token]/page.js` 這個閱讀器之後到底要繼續用、還是正式視為棄用的舊功能？兩個方向會讓 CC 之後的技術動作完全不同。

3. **會員中心是否真的要改名／改版成「我的基地」（My Hub）**：目前只是 ChatGPT 的 UI 提案（書架／收租AI／驚喜世界／好康／收藏／成就／通知／帳號），尚未有妹的拍板，也還沒進 AIOS 決策或 Task。

4. **AIOS 資料夾架構版本對齊**：這次 ChatGPT 對話中提的 AIOS 結構（`01_公司章程.md`／`02_組織架構.md`／`SOP/`／`CEO/`／`Assets/` 平面檔案）跟 CC 實際已建立的 AIOS 骨架（`00_Foundation` ~ `09_Archive` 編號資料夾）不是同一版。需要讓 ChatGPT 知道實際版本是哪個，避免兩邊各自以為架構不同，之後對不上。

## In Progress

## Done
- ETF 完全解案重複舊草稿已刪除（2026-07-02 前完成）
- 91 筆商品 Book/Series/Academy schema 映射已完成（ST repo `docs/內容資產重整-Schema與映射-20260702.md`）
