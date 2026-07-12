# Platform Transformation — Decision Log

## Format
每筆決策新增一個區塊，格式如下：

```
## YYYY-MM-DD｜決策標題
Decision：
Why：
Owner：
```

## Log

## 2026-07-02｜AI 角色分工定案
Decision：ChatGPT＝CEO（策略／商業模式／品牌／內容出版品質驗收）；Claude Code＝CTO（工程／MongoDB／Git／自動化／技術盤點／文件整理）。內容值不值得出版、會不會傷品牌，屬於編輯／出版判斷，歸 CEO，不歸 CC。
Why：CC 擅長字數統計、找重複、格式檢查，不擅長「這本書值不值得出版」這種編輯判斷；妹已明確糾正過一次分工錯誤（CC 不該用字數/格式評內容品質）。
Owner：妹 / ChatGPT

## 2026-07-02｜內容資產模型收斂為 Book / Series / Academy 三層
Decision：移除「書系」這個層級。內容只分：Book（單本 EPUB）→ Series（產品包，真正的販售單位）→ Academy（品牌入口）。未發布 / 測試內容需隔離成 Draft Pool，不可混入正式商城；重複商品需唯一 ID 規則。
Why：原本書院／書系／系列／訂閱混用，用戶分不清層級，也導致定價與版本追蹤混亂。
Owner：妹（技術面已由 CC 於 2026-07-02 完成 91 筆商品的 Book/Series/Academy 映射，見 ST repo `docs/內容資產重整-Schema與映射-20260702.md`，方向與此決策一致，可視為已落地）

## 2026-07-02｜ST / SS / SD 三站定位維持現有分工
Decision：ST＝母站／商店（電子書/數位商品交付）；SS＝流量中心（免費內容／測驗／書院／導流，不以直接營收為目的）；SD＝維持最低維護，未確認獨特商業模式前不投入大量新功能。
Why：避免資源分散，先讓內容引擎（書院）跑順再擴充新戰場。
Owner：妹

## 2026-07-02｜SD 收租 AI 現況澄清（非放棄）
Decision：SD 不是「放棄」，而是「維持最低維護，不投入新功能開發」；既有的 cron 抓資料、LINE 推播四條仍正常運作，不下架。
Why：對話中 ChatGPT 曾被問「SD 你徹底放棄？」，容易被誤讀成停止服務；實際是投資優先順序調整，不是關站。
Owner：妹

## 2026-07-02｜尋寶樂園（二手市集）整修擱置
Decision：尋寶樂園（規劃新品／二手物品／未來廣告商）現階段不投入整修規劃，維持現狀。
Why：妹明確表態「沒心力管到這裡，不是現在想做的」，非技術限制，是主動選擇優先順序。
Owner：妹

## 2026-07-03｜平台三層架構：Marketing / Product / Membership
Decision：整個平台拆成三層，只有 Product 層適用下面的三分類（bundle/course_only/ebook_only）：
- **Marketing**：免費測驗、文章、SEO、活動——不是 Product，不進三分類 schema，純粹是 SS 的導流入口
- **Product**：ebook、course、bundle——適用三分類
- **Membership**：訂閱、書院、SD——另一套邏輯，不套用三分類
Why：避免把「免費導流頁」跟「付費商品」混在同一個 schema 裡，兩者的技術需求（是否要解鎖權限、是否要進訂單系統）完全不同。
Owner：妹 / ChatGPT / CC 三方一致同意

## 2026-07-03｜Series ContentType 三分類定案
Decision：Product 層的商品內容型態固定為三種，不再新增第四種：
- `bundle`：課程 + 電子書（現有：AI書院、股市書院、心理學書院、自律神經）
- `course_only`：僅課程／測驗／互動內容（付費、需要解鎖權限的才算）
- `ebook_only`：僅電子書（現有：舊書5本等敘事/工具書）
Why：三種型態對應目前實際存在的三種內容特徵，命名反映內容型態而非網站前台分類。
Owner：妹 / ChatGPT / CC 三方一致同意

## 2026-07-03｜商品折扣機制定案：contentType 數量折扣，取代心理學專屬系列定價
Decision：
- 放棄 GPT 建議的「試讀→入門→進階→高階→完整系列」分層升級制，不做老買家比例折抵、不做自動解鎖下一級這類複雜機制
- 每本書／每個課程維持獨立單本定價
- 折扣改用「購物車內同一個 contentType 累計件數」計算，**不分主題／不分書院**：2 件 9 折、4 件 85 折、6 件以上 8 折
- 跨 contentType 不能湊數量（例如 1 本 ebook_only + 1 個 course_only 不算 2 件）
- 心理學 28 本原本的專屬系列定價（單本 249／4 本 699／6 本 999／全系列 2499）正式廢除，改套用這個通用規則
- 舉例：買 1 本 AI 書院（bundle）+ 2 本心理學（bundle）＝ 3 件 bundle 一起累計算折扣，不管主題是否相關
Why：妹認為 GPT 的分層升級制太繁瑣、要處理的邏輯太複雜；改用單本定價 + 同 contentType 數量折扣更單純，還能跨書院累計，反而更鼓勵多買不同主題的內容。
Owner：妹

## 2026-07-03｜電子書交付模式：改回線上閱讀為主，閱讀器不廢棄
Decision：電子書購買後開放帳號權限（線上閱讀＋解鎖），採用 Book/Series/Academy 重組後的系列包裝＋升級制度（試讀→入門→進階→高階），不做手動寄送 EPUB 檔案。`/read/[token]` 閱讀器繼續維護，不廢棄。
Why：妹確認要走 ChatGPT 建議的「線上閱讀為主」方向，取代 2026-06-18「放棄線上閱讀器、改回手動 Email 寄送」的舊決定。
**⚠️ 取代關係**：本決策正式取代 2026-06-18 決定；2026-06-28「EPUB 下載＋SS 書院課程解鎖，不拆賣」的商品綁定原則不變，但「下載」不再等於「手動 Email 寄送檔案」，而是「線上閱讀帳號權限」。EPUB 下載可留作備援選項，非主要交付方式。
Owner：妹

## 2026-07-06｜ST 商城 Phase 4：Completed & Frozen（Order Persistence + Payment + Hardening）
Decision：ST repo（`my-bookstore-next-V2`）商業規則規格書 v1.0 的 Phase 4（Order Persistence & Payment）正式完成並封存，不再回頭修改。範圍：`PurchaseOrder`/`PaymentTransaction` model、`OrderRepository`、`PaymentAdapter` 抽象介面（`manual_transfer` + `mock` 兩個實作）、`PaymentService`（Transaction Flow + Idempotency）、`GrantService`（實際寫入 `UserPurchase`）、`POST /api/checkout`、`POST /api/payment/callback`。完成後先做一輪多角度 code review 才驗收，抓到 Critical 安全漏洞（callback 零認證 + client 可自選測試用 `mock` provider，兩者疊加可免費觸發真實商品授權），已在 Phase 4.1 Hardening 修復（admin session 認證、paymentMethod 白名單、idempotency retry 修復、transactionId-based CAS）。64 個單元測試全過，經第二輪 adversarial verification 確認修復無誤、無新增 regression。下一步進入 Phase 5（Checkout UI / 我的訂單 / 我的電子書 / 付款成功頁 / 付款失敗頁等使用者可見功能），Phase 1～4 程式碼不再回頭重新設計。
Why：確立「每個 Phase 有明確邊界，完成並通過 review 後就封存，不做無止盡的 Hardening/Refactor」的開發節奏，避免陷入 Low → 更 Low → Style → Refactor → Architecture 的無限迴圈。詳細技術記錄見 ST repo Claude Code 記憶檔 `project_commerce_rules_v1_phase4_20260706.md`。
Owner：妹 / CC

## 2026-07-07｜stilltimecorner.com 網域正式啟用
Decision：ST 站自訂網域 stilltimecorner.com（Cloudflare 購買+代管 DNS）已完成串接 Vercel，DNS/SSL 皆已生效。apex 網域為主，www 導向 apex。
Why：ST 站正式對外身分升級，脫離 still-time-corner.vercel.app 子網域，為後續社群推廣做準備。
Owner：妹 / CC

## 2026-07-07｜ST 商城 Phase5：第一個真實商品（理財調查局）走完新結帳系統
Decision：Phase1-4 建好的新結帳 pipeline（CheckoutService/PaymentService/GrantService）首次真正接上前端，讓「理財調查局：ETF完全解案」成為第一個用新系統銷售的商品。同時修復 `/api/my-purchases` 與 `/api/read-epub` 對舊系統(DigitalOrder)/新系統(PurchaseOrder)的 cross-check 落差——這是讓新系統購買後能真正被讀到的關鍵修復。
Why：驗證整條新 pipeline（結帳→付款確認→發放權限→線上閱讀）能否在真實商品上跑通，作為後續全站商品遷移的第一個切片。
Owner：妹 / CC

## 2026-07-07｜取消電子書全系列訂閱制（SD 收租AI訂閱不受影響）
Decision：下架「電子書全系列3個月/半年/1年訂閱」3個商品，只保留單本買斷制。SD（收租AI）月訂/年訂維持不動，是完全獨立的商品線。
Why：只有家人在測試，沒有真實訂閱戶，訂閱制的工程複雜度（時效追蹤、續約提醒）換不到實際商業效益，拿掉後也讓全站商品遷移新結帳系統的範圍變乾淨。
Owner：妹

## 2026-07-07｜多品項購物車 + 電子書/課程組合購買 + 數量折扣，正式接上新結帳系統前端
Decision：新結帳系統（`/checkout-v2`）從單品購買升級為購物車模式；商品頁若有同內容（`contentId`相同）的課程存在，可選擇「只要電子書」或「電子書+課程組合」一起加入購物車，折扣由既有 Pricing Engine（`UpgradeRule` 同內容升級價 + `DiscountRule` 數量折扣）在結帳時自動計算，不需要另外開發定價邏輯。

⚠️ **發現跟本文件 2026-07-03「商品折扣機制定案」的數字不一致**：當時決策寫「2件9折、4件85折、6件以上8折」，但實際已上線的 `DiscountRule` 種子資料（`scripts/phase2-seed-discount-rules.mjs`）是「2-3件95折、4-5件9折、6件以上85折」。這個落差需要妹確認：是2026-07-03之後另外調整過折扣力度沒有回來更新這份記錄，還是實作本身跟決策沒對齊，需要挑一邊修正。
Why：全站商品分批遷移新結帳系統前，購物車/組合購買/折扣提示這三個前端功能要先到位。
Owner：妹 / CC

## 2026-07-07｜新結帳系統補上 SS 課程解鎖碼發放，AI書院系列1/2 解除遷移限制
Decision：`GrantService` 新增邏輯：購買商品若設定 `ssUnlockTarget`/`unlockTarget`，確認付款時自動產生 `SS-XXXX-XXXX` 解鎖碼；`/api/verify-unlock` 同時認得舊系統(DigitalOrder)與新系統(PurchaseOrder)產生的解鎖碼。AI書院系列1、2（共6本）確認可以安全遷移到新結帳系統。
Why：先前新結帳系統缺少 SS 解鎖碼發放能力，是 AI書院商品無法遷移的唯一技術阻礙，補上後解除限制。
Owner：妹 / CC

## 2026-07-07｜AI書院系列3遷移卡在SS repo缺付費書院頁；系列4~9內容其實已就緒（修正先前認知）
Decision：AI書院系列3（Prompt/AI Agent/AI記憶）的SS課程內容已寫好，但目前只有完全不鎖的「試讀頁」（跟系列2~9共用`AiTrialPage.tsx`元件），沒有像系列1/2一樣的付費解鎖書院頁，需要在SS repo新建獨立頁面才能遷移，這次未執行。另外妹確認AI書院系列4~9的電子書MD/部分epub、課程MD其實都已經寫好在Google Drive（`驚喜樂世界\驚喜學院\AI書院\`），並非先前記錄的「s4~s9共17冊還沒轉epub」——是內容已產出但還沒建置上架，不是內容還沒寫。這塊建置工作妹傾向另開新對話處理。
Why：釐清AI書院系列3~9的真實現況，避免下次接手時基於過時假設重工。
Owner：妹 / CC

## 2026-07-08｜AI角色分工重新定案：取代CEO/CTO框架，改為互相review的責任邊界制
Decision：正式取代2026-07-02「AI角色分工定案」中的權力歸屬部分。不再用CEO/CTO等頭銜定義權力階層，改用責任邊界表定義每個角色（妹/GPT/CC/龍蝦/未來Codex）該做什麼、不做什麼。核心精神：GPT與CC互相review、互相補強，不是誰有絕對專權；有分歧時由妹（Jane）拍板。原決定中「內容品質判斷不歸CC（CC不擅長editorial判斷）」這條理由保留，只移除「GPT持有CEO最終拍板權」的框架。龍蝦維持六隻專職分工，「每日例行工作」是六隻共同的工作模式，不新增第七隻。完整內容見新建文件 `01_Company/AI_Team_Roles.md`。
Why：舊決定讓GPT持有「CEO」頭銜與內容最終拍板權，與既有「GPT建議先討論再執行」的實務規則已產生潛在矛盾；妹在2026-07-08確認不執著頭銜，在意責任邊界清楚（方便未來加入Codex或其他AI時容易擴充），且明確要求AIOS維持「互相review、互相補強」而非階層專權。
Owner：妹 / GPT / CC 三方討論後定案

## 2026-07-12｜產品內容策略：多面貌呈現＋免費入門品質下限
Decision：同一份內容可用多種面貌呈現（遊戲片段／電子書／有聲書／短片／進階課程），吸引不同類型的人；不論哪種面貌，免費/入門層級都必須具備真實學習價值，不得空洞化，想學更多才導向站內付費多型態內容。
Why：直接呼應AI書院系列4~9品質問題（內容偏薄、跳過審稿關卡），妹主動把這次教訓套用成新方向（繪本播放器/短語音/推理解謎遊戲）的共同紅線。
Owner：妹
