# AIOS 技術架構建議

> 撰寫者：Claude Code（技術角色）
> 日期：2026-07-02
> 範圍：ST（my-bookstore-next-V2）／SS（surprise-corner-src）／SD（stock-dashboard）／AIOS
> 性質：純技術架構文件，不含公司理念、願景、商業規劃內容

---

## 1. 現有資料夾結構

### 1.1 四個資料夾的實際狀態（`MyProjects01/` 下）

```
MyProjects01/
├── my-bookstore-next-V2/   (ST)
├── surprise-corner-src/    (SS)
├── stock-dashboard/        (SD)
└── AIOS/                   (僅有 README.md)
```

### 1.2 ST（my-bookstore-next-V2）

- 有 `docs/`（含 `docs/data/`），是三個 repo 裡文件化程度最高的
- repo 根目錄有 30+ 個一次性技術檔案直接堆在最外層：`test_*.js`、`check_*.js`、`debug_*.js`、`fix-*.mjs`、`upload-*.mjs` 等，未歸檔
- repo 根目錄有多個**內容為空的檔案**被 git 追蹤：`Final`、`JS`、`MD`、`api`、`bug`、`data`、`frontend`、`guide`、`install`、`stock`、`t-forward`、`v2`、`verification`、`virtualstock`、`·`
- `.claude/` 只有 `launch.json` 與 `worktrees/`，無其他內容

### 1.3 SS（surprise-corner-src）

- **沒有 `docs/` 資料夾**
- repo 根目錄有 30+ 個一次性 `fix-*.cjs` / `fix_*.py` migration 腳本，全部堆在最外層
- 兩個大型內容檔案（`魯魯來了_final.md`、`魯魯來了_全集.md`，各約 80KB）直接放在 repo 根目錄，不在任何內容資料夾裡
- `CLAUDE.md` 同時存在於 repo 根目錄與 `src/CLAUDE.md` 兩處

### 1.4 SD（stock-dashboard）

- 有 `docs/`，但只有 1 個檔案（`c-brief-sd.md`）
- repo 根目錄有獨立的 `MEMORY.md`（與 Claude Code 自身的 memory 機制是兩套不同系統）
- 三者中根目錄最乾淨，無大量散落腳本

### 1.5 AIOS

- 位於 `MyProjects01/AIOS/`，與 ST/SS/SD 同層
- 目前只有 `README.md` 一個檔案，內容是架構定義文件本身，其餘結構（`01_公司章程.md` 等）均未建立
- **AIOS 本身不是 git repo**

### 1.6 Claude Code 記憶系統的實際位置

- 位於 `C:\Users\user\.claude\projects\C--Users-user-Desktop-MyProjects01-my-bookstore-next-V2\memory\`
- 這個路徑由**工作目錄雜湊值決定**，目前只在從 ST 目錄啟動的 session 才看得到
- 從 SS 或 SD 目錄啟動 Claude Code，會產生完全獨立、空白的 memory 儲存區，看不到這批記憶

### 1.7 意外發現：使用者帳號根目錄下有孤兒 git repo

- `C:\Users\user\.git` 存在，是一個以整個 Windows 使用者設定檔目錄為根的 git repo
- 內容：1 個 commit（`初始版本：Surprise Corner 首頁...`），無 remote
- 任何在 `C:\Users\user` 底下、但不屬於某個獨立 repo 的資料夾（例如 `AIOS/`）執行 `git` 指令，都會被這個外層 repo 接管
- 目前追蹤範圍涵蓋 SS 部分檔案（顯示為 modified/deleted），未追蹤範圍包含 `.ssh/`、`AppData/`、`.claude.json` 等整個使用者設定檔內容（目前為 untracked，尚未被 commit）

---

## 2. AIOS 最佳放置位置

- `MyProjects01/AIOS/`（現況位置）是正確位置：與 ST/SS/SD 同層、不隸屬任何一站，符合「AIOS 不屬於任何網站」的既有定義
- 前提：AIOS 必須成為**獨立的 git repo**（現況不是），否則任何在此資料夾內的 git 操作都會被 1.7 節的孤兒 repo 接管

---

## 3. AIOS 建議資料夾架構（技術角度）

技術上需要區分兩類文件，現況（ST `docs/` 資料夾）把這兩類混在一起：

- **活文件（living doc）**：規則/流程/現況，會被覆寫更新，同一檔名只有一份
- **快照文件（snapshot doc）**：某個時間點的稽核/盤點報告，檔名帶日期，寫完後不再修改，只會被更新的快照取代

```
AIOS/
├── README.md
├── 00_INDEX.md              ← 文件地圖，每份文件加一行指向索引
├── 01_公司章程.md            活文件
├── 02_組織架構.md            活文件
├── 03_AI員工手冊.md          活文件
├── 04_公司資產.md            活文件（各書院/系列現況總表，定期覆寫）
├── 05_產品策略.md            活文件
├── 06_工作流程.md            活文件
├── 07_任務儀表板.md          活文件
├── 08_停車場.md              活文件
├── sop/
│   ├── 電子書上架流程.md
│   ├── 社群發文流程.md
│   ├── 書院建立流程.md
│   ├── MongoDB修改流程.md
│   └── Git流程.md
├── decision/                 ← append-only，一決策一檔，檔名帶日期
│   └── 2026-07-02_內容資產schema定案.md
├── meeting/
├── snapshot/                 ← 稽核/盤點報告，帶日期，唯讀
│   └── 2026-07-02_內容資產v1.1稽核.md
└── archive/                  ← 被取代的舊版活文件搬進來，不刪除
```

---

## 4. Git 最佳管理方式

1. **AIOS 需初始化為獨立 git repo**，設定 remote（比照 ST/SS/SD 模式，push 到 GitHub）
2. **必須處理 `C:\Users\user\.git`**：這個孤兒 repo 目前會攔截 AIOS 及其他使用者根目錄下鬆散資料夾的 git 指令，且工作目錄裡包含 `.ssh/`、`AppData/` 等敏感內容。在為 AIOS 做 `git init` 前，需先確認這個外層 repo 不會造成路徑衝突
3. **ST/SS/SD 維持三個獨立 repo，不合併為 monorepo**：三者技術棧不同（Next.js App Router `.js` ／ Next.js App Router `.tsx` ／ Next.js + Supabase），合併不會減少維運複雜度
4. **根目錄散落的一次性腳本需歸檔**：ST 的 `test_*.js`／`check_*.js`／`debug_*.js`，SS 的 `fix-*.cjs`／`fix_*.py`，全部移入各自 repo 的 `scripts/archive/`，往後新增同類腳本也統一放 `scripts/` 而非 repo 根目錄
5. **ST repo 根目錄的空內容檔案**（`Final`、`JS`、`MD`、`api`、`bug`、`data`、`frontend`、`guide`、`install`、`stock`、`t-forward`、`v2`、`verification`、`virtualstock`、`·`）應從版控移除
6. **`.env.local`／`.env.vercel` 現況已正確排除於 git 追蹤外**，機密備份走獨立 private repo（`my-env-backup`），這個模式是對的，AIOS 若之後有機密等級的策略文件可比照辦理（獨立 private repo，不混進公開/半公開的 AIOS）
7. **ST 的 git remote URL 目前內嵌明碼 GitHub PAT token**（存在 `.git/config` 裡），屬於憑證管理風險，應改用 git credential manager 或 SSH key，不要讓 token 常駐在 remote URL 字串內

---

## 5. 哪些文件應放 AIOS

- 跨三站的策略/決策文件：書院架構總表、內容資產 Schema 定案、商業模式與定價政策
- 跨三站共用的 SOP：電子書上架全流程、Git 流程、MongoDB 修改流程
- AI 角色分工與職責邊界（誰負責什麼技術範圍）
- 任何「三站都要遵守」或「不特定屬於單一 repo」的規則

---

## 6. 哪些文件應留在各專案 docs

- 該 repo 專屬的技術實作細節：API 規格、資料庫欄位定義、部署設定
- 該 repo 專屬的一次性技術稽核報告（例如 ST 的內容資產逐筆清單 CSV/JSON、全資產地圖）—— 這些是針對單一資料庫的技術稽核，屬於該站的技術資產，不是跨站策略
- 各站的 `README.md`／`CLAUDE.md`：AI 啟動時依工作目錄讀取專案說明，不會主動去讀 AIOS，因此站台專屬操作指引仍須留在各自 repo 根目錄

---

## 7. 如何避免文件重複

1. **分工原則**：策略/決策/跨站規範只寫一份放 AIOS；技術實作細節只寫一份放各站 `docs/`；不兩邊各寫一份
2. **現況已發生的重複風險**：ST `docs/` 裡「內容資產重整」系列文件，同時包含 Schema 定案（策略層，最終應併入 AIOS `04_公司資產.md` 或 `05_產品策略.md`）與逐筆清單稽核（技術層，留在 ST `docs/`）——兩者目前混在同一批檔案裡，拆分時需要分流，不能整批搬移
3. **`CLAUDE.md` 與 AIOS `03_AI員工手冊.md` 的界線**：`CLAUDE.md` 放「這個 repo 怎麼操作」的技術細節；`03_AI員工手冊.md` 放「AI 在公司裡的角色分工」。主題不同不算重複，但不能把跨站規則寫進單一 repo 的 `CLAUDE.md`，否則其他 repo 的 AI 看不到
4. **Claude Code memory 是重複的潛在來源**：目前 memory 只在 ST session 可見（見 1.6 節），SS/SD 各自的 session 看不到。技術上的因應方式：只要是「跨站的、任何 AI 都要查得到」的內容，一律寫進 AIOS，不要依賴 Claude Code memory 做跨專案共享

---

## 8. 如何讓未來 Codex 可以直接接手

技術上讓 Codex 能直接接手的最低需求：

1. **AIOS 必須是可 clone 的 git repo**（現況不是，見第 4 節第 1 點）
2. **每個 repo 的 README.md／CLAUDE.md 需註明「本 repo 屬於 AIOS 管理」並附上 AIOS repo 連結**，讓 Codex 從任一專案都能找到總部文件的位置
3. **SOP 需寫到「不需要問人就能照做」的完成度**：現況 `sop/` 資料夾是空的，實際 SOP 散落在 ST 的 `docs/電子書上架全流程SOP.md`，屬於孤島狀態，尚未搬進 AIOS
4. **決策記錄需保留「為什麼」而非只有「做了什麼」**：目前 Claude Code 的 memory 檔案已經有記錄 Why 的習慣（例如本次 session 產出的內容資產 Schema memory），這個習慣需要延續到 AIOS 的 `decision/` 資料夾，而不是只存在單一專案的 memory 或聊天紀錄裡
