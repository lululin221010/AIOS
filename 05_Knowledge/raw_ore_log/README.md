# Raw Ore Log — 自動捕捉的原始Prompt

> 建立日期：2026-09-13，起因：Notion EVT-14／候選池[[Content_Candidate_Pool.md]] C024——妹提出「以前發現的東西常常沒留下就消失，尤其Prompt要留原文才能事後抽公式」，妹拍板值得投資做自動抓取。

## 這是什麼

`prompts.jsonl` 是一份append-only的原始Prompt捕捉紀錄，由CC本機`~/.claude/hooks/log-raw-ore.cjs`（PostToolUse hook，掛在`Bash`／`mcp__Claude_Browser__computer`／`mcp__Claude_Browser__form_input`）自動寫入，**不需要CC記得手動記錄**：

- CC用Bash呼叫Replicate／Fal／Stability／OpenAI圖片影片API時，自動抓command裡的`"prompt":"..."`欄位
- CC在Browser pane操作Grok／Vibe等網頁，透過`computer`(type動作)或`form_input`打字進20字以上的文字時，整段文字都會被記下來

## 設計原則：只存不判斷

- **不篩選好壞、不判斷值不值得**——只要符合上面兩種情況就整段存下來，好壞留給之後的人判斷
- 可能包含大量雜訊（例如打字打到一半的內容、非Prompt用途的長文字），這是刻意的：寧可多存不小心漏掉，事後清理比事後找不回來容易
- 每筆記錄：`ts`(時間)、`source`(bash-curl／browser-computer-type／browser-form-input)、`session_id`、`cwd`(當時在哪個專案資料夾)、`raw_prompt`(抓到的文字)，bash-curl另外存`raw_command`(完整指令，供比對command其餘參數如尺寸/模型版本)

## 使用方式（之後CC或妹要怎麼處理這份資料）

1. 定期（建議跟隨file-freshness-audit的週一巡查一起做，或累積到一定筆數再處理）掃過新增的行
2. 依妹原始想法：**同主題/同類型的多筆Prompt放一起比對**，抽出「核心機制、可替換槽位、風格、公式」——這是C024的真正目的，不是單純存檔案
3. 找到有價值的公式/模式，寫進Treasure Vault或Content_Candidate_Pool，並在該筆記錄旁標記已處理（例如加`processed: true`欄位，或另存一份「已萃取」清單），避免重複分析同一批
4. 純雜訊（打字打一半、不相關內容）可以直接略過不用特別刪除，量大之後再一次性清理

## 已知限制

- Grok Imagine等由妹在Browser pane手動操作最後一步的流程（見[[project_content_repurpose_pilot_dark_psych_20260909]]的技術踩坑記錄），CC沒有代打Prompt的那一步就不會被這個hook捕捉到，只能捕捉CC自己打字/呼叫API的部分
- 這個hook只裝在這台機器的`~/.claude/settings.json`（使用者層級），換一台機器或用CC2需要重新設定
- 20字的長度門檻是粗略經驗值，之後發現漏抓或雜訊太多可以回來調整`~/.claude/hooks/log-raw-ore.cjs`裡的`MIN_TEXT_LEN`
