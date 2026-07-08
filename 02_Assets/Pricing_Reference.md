# 定價參考表（Pricing Reference）

版本：v1.0
建立日期：2026-07-08
資料來源：ST repo（`my-bookstore-next-V2`）MongoDB `digitalProducts` collection 即時查詢（`scripts/export-pricing-snapshot.mjs`）
用途：GPT／CC 討論定價策略前，先查這份表確認「現況實際是什麼」，不要憑印象或憑舊文件猜

> ⚠️ 這是某個時間點的查詢快照，不是即時同步的資料。之後若有新品上架或調價，這份表要重新查詢更新，不能只靠記憶維護。

---

## 現行定價邏輯（已確立，2026-07-08 查詢確認）

目前是**定位定價，不是市場比價**：同一類產品（同系列、同定位）統一單價，不因單本內容差異各自喊價，新品定價原則上比照同類已有的價位帶，不用每次重新市場調查。

| 價位 | 適用範圍 | 已上架/可購買數量 |
|---|---|---|
| NT$199 | 標準單書價：心理學6學系28本、自律神經7冊、「那個感覺」靈異系列、舊書5本（斜槓致富方程式／台股紅綠燈2026／影音AI工具指南／愛的最後一哩路／靈魂的轉運站）等 | 約57筆真正上架中（另有21筆已發布但comingSoon尚未開放購買、3筆draft未發布） |
| NT$249 | AI書院全系列（系列1、2、3，共9本，統一價；系列4~9比照同價） | 9筆已上架 |
| NT$299 | 股市書院（入門/進階/高階）、理財調查局：ETF完全解案（2026-07-08從NT$199調漲） | 4筆已上架 |

## 免費贈書機制（不是定價候選，是分層策略的一環）

`freeForMembers:true` 的商品（目前35本，主要是「那個感覺」靈異系列＋部分心理學書）：登入即可免費永久閱讀，不提供下載。這是既有的「免費書分層」策略的一部分（見 CLAUDE.md：註冊→那個感覺），**不是**要重新定價的候選，GPT 看到這些NT$199的免費書不用建議調價。

## 已知例外／討論定價時要特別小心的地方

1. **SD（收租AI）訂閱的真實價格不在這份資料裡**：`digitalProducts` collection 裡有「收租AI 月訂／年訂」兩筆記錄，`priceTWD` 都顯示 199，但這只是佔位／解鎖碼發放用途的記錄，**不是**SD的真實售價。SD 真實定價是月訂 NT$499／年訂 NT$4788，存在 SD 自己的系統（Supabase），不在這個 MongoDB 裡。討論 SD 定價時，不要拿這筆199當依據。
2. **電子書全系列訂閱制已下架**：3個月/半年/1年訂閱（`packageType: sub3m/sub6m/sub1y`）已於 2026-07-07 決定下架（`isPublished:false`），只保留單本買斷制，不算現行商品，不用納入定價比較。

## 查詢方式（CC 或未來龍蝦重新查詢用）

```
node scripts/export-pricing-snapshot.mjs
```
在 ST repo 根目錄執行，會列出 `digitalProducts` collection 目前所有商品的 title／productType／packageType／priceTWD／isPublished／comingSoon／freeForMembers／contentId。
