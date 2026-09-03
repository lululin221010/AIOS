# Codex 自動化狀態

最後盤點：2026-08-31 09:40（Asia/Taipei）  
來源：`C:\Users\user\.codex\automations\` 的有效設定，以及各自動化最近一次執行紀錄。  

## 目前啟用中（7 個）

### 每日摘要（`automation`）

- 排程：每週一至五 08:00。
- 上次執行：2026-08-31 08:30:42（Asia/Taipei）。
- 實際結果：今日 Calendar 無事件；Gmail 為 INBOX 未讀 49、總未讀 54、重要未讀 7。偵測到 Google 新登入、OpenAI ChatGPT Web 從台北 Windows Chrome 登入、GitHub Cursor 要求新增權限，以及 ISBN Center 已收件並預計 3 個工作天內寄送帳號資訊；舊 ISBN 駁回案持續不重複提醒。

### 每週回顧（`automation-2`）

- 排程：每週五 16:00。
- 上次執行：2026-08-28 16:02:40（Asia/Taipei）。
- 實際結果：依目前可見紀錄完成週回顧；確認 SS `/feeling` 的 36 篇完整閱讀內容修正與連結整理，Buffer 連結分析已更新至 54 則貼文，Buffer 佇列為 IG 6、Threads 6、Facebook 4 並已產出 4 篇 Facebook 補貨草稿。行事曆在查核期間無事件；ISBN 申請轉為已收件，另保留 Google Windows 登入、Google/Claude 資料共享、GitHub Cursor 權限與 9/6 Buffer 提醒等注意項目。

### 後續監控（`automation-3`）

- 排程：每週一至五 09:00。
- 上次執行：2026-08-31 09:03:22（Asia/Taipei）。
- 實際結果：Gmail 顯示 INBOX 247 封、未讀 49；總未讀 54；重要未讀 7。新增或持續追蹤 OpenAI/Google 登入與資料共享通知、GitHub Cursor 權限要求、Patreon Gary Chen 會員每月 US$1.50 扣款，以及 ISBN Center 已收件、等待帳號資訊。Calendar 僅保留 2026-09-06「補排 Buffer 佇列第 2 批」全天提醒；Vercel/GitHub 部署皆為 Ready，未列為異常。

### 每週平台數據整理提醒（`automation-4`）

- 排程：每週一 10:00。
- 上次執行：2026-08-31 約 09:31（Asia/Taipei；任務執行紀錄）。
- 實際結果：2026-08-24 至 08-31，Facebook 粉專發文 8 篇，最佳商品貼文有 2 個基礎互動；Buffer Facebook Queue/Sent 為 2/8、Threads 4/6、Instagram 4/4，三個頻道皆未暫停。Threads 的最佳貼文有 161 次觀看、3 個互動；Facebook Queue 最薄，建議優先補排程。粉專沒有 `read_insights` 權限，因此未把 Page views／Reach／Impressions 當成 0。

### 檢查 Buffer 三頻道佇列（`buffer`）

- 排程：每週一 09:30。
- 上次執行：2026-08-31 約 09:32（Asia/Taipei；任務執行紀錄）。
- 實際結果：Buffer GraphQL API 查到 Instagram 4、Threads 4、Facebook 2，三頻道都低於 5。已排除暫停的「煤氣燈效應」舊稿，並整理 4 篇待審補貨文案：〈那個感覺介紹〉、〈理財調查局案001〉、〈心理學書院免費堂〉、〈最後的信號連載〉；尚未替使用者排程或發佈。

### 每週 Buffer 貼文連結成效分析（`buffer-2`）

- 排程：每週一 09:00。
- 上次執行：2026-08-31 09:02:57（Asia/Taipei）。
- 實際結果：更新 SS 的 Markdown 報告與三份 CSV；已發布貼文共 71 則，本文含外部連結 9 則、未含連結 62 則。相較上次 54 則，總數與兩組樣本數均上升；未含連結組 impressions、views 下降，含連結組 impressions 下降、views 上升。異常：全部貼文沒有有效 engagementRate，且 28/71 則 `metricsUpdatedAt` 空白或超過 3 天前。

### 每週自動化狀態與到期檢查（`automation-5`）

- 排程：每週日 09:00。
- 上次執行：尚未執行；首個排程時段為 2026-09-06 09:00（Asia/Taipei）。
- 實際結果：建立時已確認唯一資料來源為 `AI與訂閱支出追蹤_lulu_20260810.xlsx`；以 2026-08-31 的資料預檢，最近的明確到期日為 Super Grok 2026-10-19，超過 30 天，故目前沒有明確的 30 天內到期項目。ChatGPT Plus 為自動月費但未記錄下一次扣款日，將在正式執行時保留為「無法判定」而非誤報。

## 更新規則

每個啟用中的自動化完成後，都必須更新本檔對應項目的「上次執行」與「實際結果」；沒有實際結果時要明確寫出查詢失敗或資料不可得的原因，不可只寫「正常」。
