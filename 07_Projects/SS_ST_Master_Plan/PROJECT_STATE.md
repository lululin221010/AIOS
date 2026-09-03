# SS × ST 完工總藍圖（Master Plan）

建立：2026-08-29（CC，ST session）
用途：取代「做到哪算到哪、回頭不知道完成什麼」的狀態。這份文件是**唯一權威現況來源**，任何AI（CC/CC2/GPT/C/SG）看之前先讀這份，不要各自猜現況。
更新規則：任何一方完成一個節點，直接來改這份文件打勾，不用等「整理時間」。狀態不明的節點誠實標「待查」，不要用猜的填掉。

---

## 總覽

| 站 | 最終角色（已拍板，不重談） | 目前最大缺口 |
|---|---|---|
| SS 驚喜角落 | 純免費流量／體驗樂園，不推銷、不負責轉換（2026-08-27定案，取代「社群→SS→ST」單一漏斗） | 首頁第一層入口數／IA從未正式定案（3/5/7都討論過，未拍板）|
| ST 有的沒的小舖 | 作品／商品／課程站，負責購買與交付 | Phase 5（第一個可購買版本）已用checkout-v2蓋出雛形，但**從沒被妹真實走過一次完整購買流程驗證** |

---

## SS 驚喜角落

### 定位（已拍板）
純免費樂園。不解鎖、不導購、不假裝免費再推ST。內容：免費測驗、免費完整內容、Lulu撿到、冷知識、AI快訊等。詳見AIOS `07_Projects/Platform_Transformation/Decision_Log.md` 2026-08-27條目。

### 現有路由盤點（2026-08-29 CC直接ls出來的事實，不是猜的）
```
admin/ ai-news/ bazi/ books/ classroom/ cold-knowledge/ creator/
experience/ experience-v2/ feeling/ games/ horoscope/ login/
moon-sign/ name-numerology/ novels/ play/ quiz/ reader/ share/
tarot/ tarot-year/ tools/ wall/ wonderland/
```
**这些路由對應到「幾個園區」還沒有IA歸位**——這正是下面第①項blocker要解決的事。

### 分支與現況

| 分支 | 現況 | 下一步 | DoD |
|---|---|---|---|
| ① IA／首頁入口數定案 | ❌ 未定案。GPT提案「四方（GPT/C/Grok/CC）各自獨立提案→交叉review→妹拍板」，尚未執行 | 四方各自出方案（不能先看彼此的，避免錨定）→列優缺點/風險/樂園感→妹拍板 | 入口數＋每個入口的定位一句話＋現有29個路由全部歸位到某個入口，鎖版 |
| ② 那個感覈(feeling) 36本閱讀路徑 | ✅ 2026-08-28修復完成並push（commit 91561c0+fc43c0a） | 無 | 已達成 |
| ③ 小教室(classroom) | 🟢 2026-08-29精準路由地圖(CC2)+付費入口已下架：12個付費解鎖路由（stock/psychology/ai-academy+9系列/brain-universe/autonomic）全數用middleware擋下導回/classroom，不分是否已解鎖過。免費試讀（bonus/、stock/trial、stock/trial-investigation）不受影響。`classroom/page.tsx`入口卡片同步移除這4個書院的可點連結，改列「搬家整理中」。**改動已完成但還沒commit/push**，等妹審查。無法瀏覽器實測——SS dev server因既有`globals.css`編碼bug整站500，與本次改動無關 | 妹review後決定push；日後classroom路由本體最終去留（保留當彩蛋/合併/退役）待①IA定案後再議 | 已達成（付費入口下架部分）；路由去留仍待① |
| ④ Lulu撿到 | 🔴 構想階段，尚未有正式路由／內容格式；三級制(原礦/實測寶/金礦)已定義但還沒發過第一篇 | 出第一篇「魯魯撿寶」測市場反應 | 有一篇正式發表＋收錄機制 |
| ⑤ 全站24路由「有無導購殘留」audit | ✅ 2026-08-29 CC2完成唯讀稽核，7個違規路由中：**classroom/**已下架付費入口(見③)；**ai-news/、books/、login/、quiz/**四個較輕路由已由Co清理、CC驗diff後push(commit 8a8996e)——4檔案+4/-70行，純刪除，範圍精準。**novels/**（鎖章CTA套用在5本非連載小說，跟classroom同等級「嚴重」）與**reader/**（`BuyButton.tsx`整段即購買按鈕）先不動，妹提出這類試閱內容可能挑段落重寫成「小文章/魯魯觀點」而非直接刪，但這個內容格式本身還沒規劃（見候選池） | reader/、novels/待GPT/C定案：①直接退役 ②開放全免費 ③重寫進「小文章/魯魯觀點」（格式待設計） | classroom/+4個較輕路由已達成；reader/novels/待內容方向定案 |
| ⑥ 全站手機驗收 | 🔴 未做（只驗收過首頁手機版視覺） | 待①②③④收斂後才有意義做 | 手機/桌機都走過一次全部入口 |

**SS Done 判準（暫定，待①定案後補完整）**：①~⑥全部打勾 = SS 1.0完工。

---

## ST 有的沒的小舖

### 定位（已拍板）
作品/商品/課程站，負責購買→付款→交付→使用。永久買斷制，不做訂閱字眼。

### 分支與現況

| 分支 | 現況 | 下一步 | DoD |
|---|---|---|---|
| ① Commerce Phase 1-4（Model/Pricing/Checkout Pipeline/Payment） | ✅ 2026-07-06完成並正式封存，64單元測試全過 | 無 | 已達成 |
| ② Commerce Phase 5（第一個可購買版本） | 🟡 2026-08-29 CC2完成程式碼層走查（唯讀）：1-7項看起來都有支援（付款=人工轉帳確認按鈕，是既定商業模式非缺陷）。**真缺口在第8、9項**：「我的商品」統一入口完全沒處理`course`型商品——UI分類漏掉(`my-purchases/page.js`只分ebooks/audiobooks/serials/picturebooks/videos五類)、API的downloadLinks/unlockCodes也漏掉，course買家直接被賣單一SKU會永久看不到內容。**目前course都走「電子書+courseBump加購解鎖碼+email通知」模式，缺口暫不會被觸發，但這不代表已驗證過**——妹本人仍從沒真的走過一次真實購買流程 | 妹確認「course是否已/將直接販售」；不論答案為何，都建議找時間妹或CC實際走一次checkout-v2全流程（含order bump/促銷開關），把「全流程人工測試通過」這項真正打勾 | 9項全打勾，尤其「全流程人工測試通過」；若course要直接販售，需先補my-purchases的course分區+downloadLinks/unlockCodes |
| ③ Content→多格式Product模型 | ✅ 2026-07-06建立，2026-08-27確認非新設計、已可直接沿用未來有聲書/繪本/影片/課程 | 無（等真的有新格式商品要上架時才用） | 已達成 |
| ④ magic-link登入 | 🟡 環境變數讀取bug已修復（2026-08-28，CC2第一個工程試點PR#2），但完整登入流程本身**還沒重新測過** | 走一次完整magic-link登入流程驗證 | 登入成功且能看到「我的商品」 |
| ⑤ Reader串接 | 🟡 `/read/[token]`存在，但和②一樣沒被完整驗收過「付款成功→Grant→我的商品→Reader」整條線 | 隨②一起驗收 | 併入②的DoD |
| ⑥ order bump 商品覆蓋率 | 🟡 28筆中已恢復11個（股市3+AI書院8本），剩17個暫停（6系列AI書院約632題+理財調查局+舊版自律神經7冊），需走雙重驗證SOP | 依[[feedback_quiz_quality_sop_20260727]]逐批驗證恢復 | 17個全部驗證完並決定去留 |
| ⑦ 關於我們/隱私權政策更新 | 🔴 未做 | — | 頁面更新完成 |

**ST Done 判準（暫定）**：①~⑦全部打勾，且②的「全流程人工測試通過」是目前最卡的一項——**技術上可能已經接近完工，但沒人實際驗證過，這正是妹說「做了多少不知道」的具體案例**。

---

## SS×ST 合流驗收（尚未開始規劃）
陌生人從社群看到魯魯→進SS免費玩不被推銷→某篇作品內容連去ST→ST看得出是同一家→買了能真的登入拿到商品。這條完整路徑目前沒有人走過一次。等SS①、ST②都收斂後才排這個。

---

## AI Resource Board
不在這裡重複維護，權威版在 `AIOS/01_Company/AI_Team_Roles.md`（2026-08-29已更新Co/CC2/SG的實際能力與限制）。

---

## 本週工作台

### 本週唯一目標（2026-08-29起）
先把 **ST②（Phase5全流程驗收）** 跟 **SS①（IA四方提案）** 兩件事其中一件真的收斂，不要兩件同時做到一半。

### 候選池（想到就丟這裡，不直接變新工程）
- 影音實驗室：Image2→分鏡→Seedance、龐德AI-drama Skill實測、熱門影片反推重製
- 魯魯撿寶第一篇
- SS classroom路由最終去留
- **「小文章/魯魯觀點」內容格式規格待設計**（2026-08-29妹提出，尚無規劃）：兩條線都指向同一個缺口——①reader/novels裡寫得好的試閱段落，與其刪除或整段開放免費，不如挑選重寫；②社群平台(FB/IG/Threads/Buffer)下架/退役的舊推廣貼文，也可能值得回收改寫。但目前完全沒有：這個內容格式的產出流程、SS上要放在哪個位置/路由、什麼樣的內容算夠格被收錄。屬內容策略設計，需GPT/C討論定案，不是CC能拍板或動手的範圍。

### 可派工任務
1. ~~SS全站路由audit~~ ✅ 2026-08-29 CC2完成，見上方SS⑤
2. ~~ST checkout-v2全流程走查~~ ✅ 2026-08-29 CC2完成，見上方ST②
3. ~~SS classroom/免費付費路由地圖+付費入口下架~~ ✅ 2026-08-29 CC2畫地圖+CC執行middleware擋下，見上方SS③（待妹review push）
4. **下一批候選（待妹拍板優先順序）**：
   - SS reader/、quiz/、books/、ai-news/、login/、novels/ 六個較輕路由的導購文案清除（機械性文字/連結移除，適合Co）
   - ST my-purchases course分區+downloadLinks/unlockCodes補強（需先確認course是否要直接販售）
   - SS dev server `globals.css`編碼bug（既有問題，目前擋著沒法用瀏覽器驗證任何SS改動）——要不要順手修，還是繼續擱置
