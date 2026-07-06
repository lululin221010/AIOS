# Platform Transformation Roadmap

## Vision
ST（`my-bookstore-next-V2`）從純架構/程式碼，跨入「真正可讓使用者購買並閱讀電子書」的產品。

## Current Phase
🚀 **ST 商城 Phase 5：First Purchasable Product**（Ready to Start，2026-07-06 起）
Scope/Exclusion List/Definition of Done 已固定，見 `Tasks.md` To Do 第 5 項；不用開新聊天室討論要做什麼，直接開發。

## Milestones
- **M1：First Purchasable Product**（尚未開始，Phase 5 DoD 10 項全部打勾才算達成）——代表第一位使用者可以完整走過商品 → 結帳 → 付款 → 我的電子書 → 線上閱讀，ST 商城從工程專案跨入真正可使用的產品。達成後才開新 Phase，不直接跳過里程碑往下做。
- M1 之後：Phase 6（營運功能：優惠券／會員／發票等）、Phase 7（成長功能：推薦／行銷／自動化等）——目前只是命名占位，範圍未定案，等 M1 達成後再展開規劃。

## Priority
Phase 1~4（Commerce Model / Pricing Engine / Checkout Pipeline / Payment + Hardening）已全部 Completed & Frozen（見 Decision_Log 2026-07-06），不回頭重新設計，除非是 production bug / 安全性 / 資料完整性問題。

## Decisions
詳見 `Decision_Log.md`。

## Risks

## Next Actions
- 開新聊天室，直接進入 Phase 5 開發（Checkout UI → Payment Result Pages → 我的訂單 → 我的電子書 → Reader 串接）
- Phase 5 完成後：更新本檔 Milestones 區塊，標記 M1 達成，再規劃 Phase 6 範圍
