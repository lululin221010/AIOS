# AIOS Git Root 稽核報告

> **✅ 已解決（2026-07-06）**：CEO核准方案A，已確認19個追蹤檔案全數存在於SS自己的正式repo後，執行 `rm -rf C:\Users\user\.git`。已驗證ST/SS repo在刪除後皆能正確偵測自己的repo toplevel，功能無異常。本檔案原提交分析時未執行任何操作，以下為原始報告內容，保留作歷史記錄。

**調查對象**：`C:\Users\user\.git`
**調查方式**：唯讀指令（`git status` / `git log` / `git ls-files` / `git config` 檢視 / 檔案系統時間戳記查詢）
**未執行**：`git init`、`git add`、`git commit`、`git clean`、`git reset`、`git gc`、任何檔案刪除、任何設定修改
**日期**：2026-07-02

---

## 1. 建立時間與是否為正常 Repository

### 建立時間（依檔案系統 metadata，非猜測）

| 項目 | 時間 |
|------|------|
| `.git` 資料夾 Birth（建立） | **2025-12-17 08:57:03** |
| `HEAD` / `config` / `description` 建立 | 2025-12-17 08:57:03（與 `.git` 建立同時，符合 `git init` 當下行為） |
| `index` / `COMMIT_EDITMSG` 最後修改 | **2026-02-04 15:52:26**（對應唯一一次 commit 的時間點） |
| `fsmonitor--daemon` 最後活動 | 2026-05-30 18:11:36 |
| `.git` 資料夾最後 Modify | 2026-07-02 22:49:56（本次與前次調查的唯讀指令所觸發，非新增內容） |

### 是否為正常 Repository

**是一個技術上有效、但位置錯誤的 Repository**，不是損毀或惡意產物。判斷依據：

- `.git/config` 內容為 `git init` 產生的預設值（`repositoryformatversion=0`, `bare=false` 等），無異常設定
- `.git/hooks/` 內沒有任何非 `.sample` 的自訂 hook（排除被植入腳本的可能）
- `.git/description` 仍是預設文字，從未被編輯
- 只有 1 個 commit，commit 內容（19 個檔案）是 SS（surprise-corner-src）專案剛用 `create-next-app` 建立時的初始骨架檔案（`public/next.svg`、`public/vercel.svg`、`src/app/layout.tsx` 等預設檔案 + 少量早期自訂檔案）

**結論**：這是有人在 `C:\Users\user`（使用者主目錄）執行 `git init` 後，對當時剛建立的 SS 專案做了一次 `git add` + `git commit`，而不是在 `surprise-corner-src` 資料夾內部執行。之後 SS 專案另外在自己的資料夾內建立了正確的 `.git`（現況 SS 有自己完整、持續更新的 git 歷史），這個主目錄下的舊 repo 從此被遺忘，未再手動操作，僅因為 git 的 repository 探測機制（往上層資料夾尋找 `.git`）而在其後被其他指令意外觸碰。

---

## 2. 現況資訊

| 項目 | 值 |
|------|------|
| **git root** | `C:/Users/user` |
| **目前 branch** | `master` |
| **目前 HEAD** | `fbdcfe135f83cff5f0597b30e91bbc2a4bbba544`（`2026-02-04 15:52:26 +0800`，訊息：「初始版本：Surprise Corner 首頁 + 日期驚喜 + 前一天信件」） |
| **commit 數** | 1（`git rev-list --all --count` 亦為 1，無其他分支或隱藏 ref） |
| **remote** | 無（`git remote -v` 空白輸出，從未 push） |
| **status** | 9 個 modified、1 個 deleted（皆為 SS 專案檔案，因 SS 自己的 repo 已持續修改這些檔案，而這個舊 repo 的 index 停留在 2026-02-04 的舊快照）、**300 個 untracked 項目**（涵蓋使用者主目錄下幾乎所有內容） |

---

## 3. Tracked Files 與最大風險

### 目前 tracked 的 19 個檔案（全部屬於 SS 專案）

```
Desktop/MyProjects01/surprise-corner-src/.gitignore
Desktop/MyProjects01/surprise-corner-src/README.md
Desktop/MyProjects01/surprise-corner-src/data/episodes.json
Desktop/MyProjects01/surprise-corner-src/eslint.config.mjs
Desktop/MyProjects01/surprise-corner-src/next.config.ts
Desktop/MyProjects01/surprise-corner-src/package-lock.json
Desktop/MyProjects01/surprise-corner-src/package.json
Desktop/MyProjects01/surprise-corner-src/postcss.config.mjs
Desktop/MyProjects01/surprise-corner-src/public/file.svg
Desktop/MyProjects01/surprise-corner-src/public/globe.svg
Desktop/MyProjects01/surprise-corner-src/public/next.svg
Desktop/MyProjects01/surprise-corner-src/public/vercel.svg
Desktop/MyProjects01/surprise-corner-src/public/window.svg
Desktop/MyProjects01/surprise-corner-src/src/app/SurpriseButton.tsx
Desktop/MyProjects01/surprise-corner-src/src/app/favicon.ico
Desktop/MyProjects01/surprise-corner-src/src/app/globals.css
Desktop/MyProjects01/surprise-corner-src/src/app/layout.tsx
Desktop/MyProjects01/surprise-corner-src/src/app/page.tsx
Desktop/MyProjects01/surprise-corner-src/tsconfig.json
```

這 19 個檔案目前**全部**仍存在於 SS 自己獨立的 git repo（`surprise-corner-src/.git`）並持續被追蹤更新，沒有任何檔案是「只存在於這個舊 repo、SS 自己的 repo 裡沒有」的獨有內容。

### 最大風險

**不是「已經洩漏」，而是「結構性地隨時可能誤觸發洩漏」：**

1. **Repository 邊界覆蓋整個使用者主目錄**，意味著任何在 `C:\Users\user` 之下、且自己還沒有獨立 `.git` 的資料夾（例如新建但尚未 `git init` 的專案、暫存資料夾），git 指令都會被這個外層 repo 接管
2. **300 個 untracked 項目中包含高敏感內容**：`.ssh/`（SSH 私鑰）、`AppData/`、`.claude.json` / `.claude.json.backup`、`.gitconfig`、以及各種 AI 工具的設定目錄（`.codex/`、`.cursor/`、`.gemini/` 等）。目前這些**都還只是 untracked，尚未被加入版控**，但只要有人（或任何自動化腳本）在 `C:\Users\user` 或其任一無自己 repo 的子資料夾下執行 `git add -A` 或 `git add .`，這些內容就會被實際 stage 並可能被 commit
3. **沒有 remote，目前暴露範圍僅限本機**——這是唯一降低風險等級的因素。只要不新增 remote 並 push，敏感內容不會外流，但風險本質（誤 add）並未被排除

---

## 4. AIOS 是否一定會受這個 Repository 影響？

**現況（2026-07-02）：不會。**

原因：git 尋找 repository 的機制是「從目前工作目錄開始，往上層逐層尋找 `.git`，一旦找到就停止搜尋」。`C:\Users\user\Desktop\MyProjects01\AIOS` 在上一輪操作中已經被執行過 `git init`，本身擁有自己的 `.git`。因此從 AIOS 內部（或其未來子資料夾）執行 git 指令，會在到達 AIOS 自己的 `.git` 時就停止，**不會繼續往上探測到 `C:\Users\user\.git`**。

**但這個「不受影響」是有前提、非永久保證的**：

- 前提是 AIOS 的 `.git` 必須持續存在。若未來 AIOS 的 `.git` 被誤刪（例如清理作業、`.gitignore` 設定錯誤、手動整理資料夾時誤刪隱藏檔案），AIOS 會立刻回退成「沒有自己邊界」的狀態，此時執行 git 指令就會再度被 `C:\Users\user\.git` 接管
- 這個保護只涵蓋 AIOS 本身，**不涵蓋 `MyProjects01` 或 `Desktop` 底下未來新建、尚未 `git init` 的其他資料夾**——只要是還沒建立自己 `.git` 的新資料夾，都仍在這個外層 repo 的影響範圍內

---

## 5. 三種安全解法

### 方案 A（最佳）：確認無獨有內容後，刪除 `C:\Users\user\.git`

| | 內容 |
|---|---|
| **做法** | 人工確認 19 個 tracked 檔案與 SS 自己 repo 的對應版本無重大差異（已於第3節初步確認皆存在於 SS repo 中）後，直接移除 `C:\Users\user\.git` 資料夾 |
| **優點** | 徹底消除風險源頭，一勞永逸；不留任何「隨時可能被誤用」的邊界漏洞 |
| **缺點** | 需要人工執行刪除操作（本報告不執行，需 CEO 或後續操作者手動進行）；如果確認不夠仔細，理論上有極低機率遺漏某個獨有內容 |
| **風險** | 若刪除前未妥善備份，一旦誤判「無獨有內容」，該 commit 的歷史紀錄將無法復原（但因未曾 push，且內容已知全部存在於 SS 現行 repo，此風險趨近於零） |

### 方案 B：確保所有現有與未來子資料夾都各自 `git init`

| | 內容 |
|---|---|
| **做法** | 不動 `C:\Users\user\.git` 本身，改為要求每一個會被使用的專案資料夾（ST/SS/SD/AIOS 皆已符合）都必須有自己的 `.git`，形成邊界阻擋 |
| **優點** | 不需要刪除任何既有資料，風險最低、最保守；ST/SS/SD/AIOS 目前**已經自然符合**此條件 |
| **缺點** | 治標不治本——外層 repo 本體與其 300 個 untracked 敏感項目依然存在；任何「尚未建立自己 repo 的新資料夾」仍然暴露 |
| **風險** | 依賴人為紀律（每次建新資料夾都要記得先 `git init`），不是系統性保證；未來只要有一次疏忽，風險就會重新出現 |

### 方案 C：設定 `GIT_CEILING_DIRECTORIES` 環境變數

| | 內容 |
|---|---|
| **做法** | 設定環境變數 `GIT_CEILING_DIRECTORIES=C:\Users\user`，讓 git 在向上搜尋 `.git` 時遇到此路徑就停止搜尋，不再往上穿越到主目錄層級 |
| **優點** | 不需刪除任何資料、不需替每個資料夾手動 `git init`，一次設定、全域生效、且可逆（移除環境變數即可還原） |
| **缺點** | 僅在有設定此環境變數的終端機／使用者環境中生效；換一台機器、換一個未設定此變數的 shell（例如未來 Codex 在不同執行環境啟動）就會失效，不是跨環境的保證 |
| **風險** | 環境變數容易在不知情的情況下被覆寫或遺忘設定原因；且此變數本身需要額外文件記錄「為什麼要設這個」，否則會變成又一個沒人知道用途的隱性設定 |

---

## 6. 給 CEO 的唯一建議方案

**建議方案 A：確認後刪除 `C:\Users\user\.git`。**

理由：

- 此 repo 從未設定 remote、從未 push，風險完全侷限在本機，沒有「已外洩」的既成事實
- 其追蹤的 19 個檔案已確認全數存在於 SS 專案自己的正式 repo 中且持續維護，刪除這個舊 repo **不會遺失任何獨有內容**
- 方案 B（現況已自然達成）只是消極防禦，無法處理外層 repo 本體與其 300 個 untracked 敏感項目持續存在的問題
- 方案 C 是環境層級的權宜手段，跨機器/跨環境（尤其是未來 Codex 可能在不同執行環境啟動）不可靠，且會製造新的「需要被記住的隱性設定」

方案 A 是唯一能讓風險歸零、且不依賴任何後續人為紀律或環境設定的方案。

**本報告僅提交分析，未執行任何操作。（2026-07-06更新：已執行，見檔案頂端解決狀態）**
