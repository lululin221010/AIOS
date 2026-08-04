# 06_Operations

## Purpose
存放跨產品線共用的營運流程與 SOP：內容上架、發文、資料庫修改等標準作業程序。

## 使用方式
任何 AI（CC／Co／C／SG）開始一項工作前，先在下面依類別找對應 SOP，不要憑記憶或試錯重新摸索。**跨專案通用**的 SOP 放這裡；**只限單一資料夾範圍**的 SOP（例如某一篇故事的插圖指令），留在各專案自己的本地索引（見文末「各專案本地索引」）。

> 這是總索引，內容連結指向各文件實際所在位置（大多不在 AIOS repo 裡，而是分散在 ST/SS repo 或 Desktop 內容資料夾）。**每份 SOP 只留一個檔案、不帶版本號**——不同情境的做法寫在文件內的「使用時機」分支段落，不是切成多個版本檔案並存（2026-08-04 定案）。

---

## 電子書出版
| SOP | 位置 | 用途 |
|---|---|---|
| PUBLISH.md | ST repo `docs/PUBLISH.md` | MD→EPUB、檢查、Blob/Mongo 發布與 release 分階段權限，**唯一權威流程** |
| 電子書上架全流程SOP | ST repo `docs/電子書上架全流程SOP.md` | 從構想確認、寫書、封面、metadata、EPUB 到平台上架的全流程 |
| 電子書封面模板規範 | ST repo `docs/電子書封面模板規範.md` | 封面版面、尺寸、文字位置與輸出規格 |
| 內容母版MD規範 | ST repo `docs/內容母版MD規範.md` | 同一份 MD 同時供 EPUB／互動課程／有聲書／短影音使用的草案規範 |

## 繪本製作
| SOP | 位置 | 用途 |
|---|---|---|
| 可翻閱電子繪本除錯SOP | `有的沒的小舖\推廣\心理學\暗黑心理學\操控與控制\_可翻閱電子繪本除錯SOP_lulu_20260803.md` | 互動翻頁繪本 index.html 的測試環境、JS bug、CSS、CTA 頁除錯方法 |

## 影片製作
| SOP | 位置 | 用途 |
|---|---|---|
| Ken Burns運鏡推廣影片SOP | `有的沒的小舖\推廣\心理學\暗黑心理學\操控與控制\_KenBurns運鏡推廣影片SOP_lulu_20260803.md` | SG/Grok Imagine 生成運鏡片段→下載→TTS→字幕配樂組裝全流程 |

## 社群經營
| SOP | 位置 | 用途 |
|---|---|---|
| 社群經營SOP v1 | `有的沒的小舖\推廣\平台\00_SOP\社群經營SOP_v1.md` | 內容主檔、7週排程、Buffer、成效追蹤的長期經營流程 |
| 各平台Playbook | `有的沒的小舖\推廣\平台\06_Playbook\`（Facebook／Instagram／Threads／TikTok） | 各平台玩法與操作心法 |

## 課程
| SOP | 位置 | 用途 |
|---|---|---|
| **課程製作SOP.md** | [06_Operations/課程製作SOP.md](課程製作SOP.md) | **完整流程權威版**（2026-08-04整合建立）：企劃質量關卡→C自我檢查(單堂4項/整本5項)→測驗品質雙項檢查→Codex批次交派方法論→技術上架注意事項→機械檢查→上架後維護，適用股市/心理學/AI書院/理財調查局/自律神經等所有系列 |
| 內容母版MD規範.md | [06_Operations/內容母版MD規範.md](內容母版MD規範.md) | 一份MD內容源同時供EPUB(ST)／互動課程(SS)／有聲書／短影音／知識卡使用的格式規則，只管內容源格式，是課程製作SOP的補充 |
| Content_Quality_Checklist.md | [05_Knowledge/Content_Quality_Checklist.md](../05_Knowledge/Content_Quality_Checklist.md) | 內容品質檢查完整版（含合格/不合格對照範例），課程製作SOP第二節引用的唯一權威版 |
| mission-writing-rules.md | SS repo `docs/mission-writing-rules.md` | Mission 互動內容動筆前的場景/玩家問題設計規則 |
| mission-engine-schema.md | SS repo `docs/mission-engine-schema.md` | Mission Engine 資料格式規範 |

`有的沒的小舖\驚喜樂世界\驚喜學院\AI書院\課程\`底下的「給Codex」交辦指令是個別任務指令，不是通用SOP，不重複收錄。

## 驚喜學院制度
| SOP | 位置 | 用途 |
|---|---|---|
| 驚喜學院制度.md | [06_Operations/驚喜學院制度.md](驚喜學院制度.md) | 整體階層架構(驚喜學院→書院→系列→產品)、好康書院/繪本推廣兩個例外說明、理財書院內部結構(台股系列vs理財調查局系列)、各書院現況總表、書院UX規則。2026-08-04建立 |

> ⚠️ 各書院解鎖技術機制（SHA-256/GrantService等）盤點尚未逐一查證，見文件內「待補」節，需要專門investigation才能補上。

## 收費制度
| SOP | 位置 | 用途 |
|---|---|---|
| 收費制度.md | [06_Operations/收費制度.md](收費制度.md) | 定價原則/付款方式/**退款政策(含法源依據+技術落地要求)**/交付方式，2026-08-04建立，唯一權威版 |
| Pricing_Reference.md | [02_Assets/Pricing_Reference.md](../02_Assets/Pricing_Reference.md) | 現行價位快照（非制度說明，查即時價格用） |

補充參考：`有的沒的小舖\推廣\心理學\討論\暗夜觀察日記_定價架構討論稿_lulu_20260715.md`（精緻禮物版定價討論稿，尚未定案部分）

## 內容品質
| SOP | 位置 | 用途 |
|---|---|---|
| Content_Quality_Checklist.md | [05_Knowledge/Content_Quality_Checklist.md](../05_Knowledge/Content_Quality_Checklist.md) | 跨系列內容品質檢查表，任何新系列開工前必讀 |

## AI Agent 安全制度
| SOP | 位置 | 用途 |
|---|---|---|
| AI_AGENT_SAFETY.md | ST repo `docs/AI_AGENT_SAFETY.md` | AI Agent 權限、Stage 1~3 信任階段、正式資產修改前必須妹當次同意的規則 |

---

## 各專案本地索引（僅限該資料夾範圍的SOP，往這裡查）
- ST repo：`docs/`資料夾（見上表大部分條目）+ `CLAUDE.md`
- SS repo：`CLAUDE.md`、`docs/mission-writing-rules.md`、`docs/mission-engine-schema.md`
- 有的沒的小舖：`PROJECT_CONTEXT.md`
- 操控與控制（精緻禮物版繪本/影片專案）：`PROJECT_CONTEXT.md`「技術SOP索引」區塊

## 已知重複/待整理（2026-08-04盤點）
完整清單見`有的沒的小舖\SOP索引_盤點報告_draft_lulu_20260804.md`；整合結果見`有的沒的小舖\電子書\SOP整合報告_lulu_20260804.md`

- ✅ **已完成**：`ebook-sop_lulu_20260710.md`／`_v1.1.md`／`_v1.3.md` 三版本已整合成`有的沒的小舖\電子書\ebook-sop_lulu.md`（無版本號），原3份封存到`有的沒的小舖\電子書\_封存\`
- 🔲 **待人工確認**：`有的沒的小舖\電子書\舊書\指令\`底下5份SOP（電子書上架全流程SOP／電子書MD寫作SOP_給C／心理學MD寫作SOP_給C／舊版參考\電子書MD格式修正指令／舊版參考\Canva封面生成指令）——Co逐份比對後確認**都不能直接判定已被ST正式版完全取代**（各自有ST版本沒收錄的細節，例如心理學系列專用章節結構、封面Canva prompt清單），需要人工看過才能決定封存或補回ST正式版
- 🔲 **待人工確認**：`靈異誌世界版-流程SOP.md`／`-系列內容SOP.md`與各自「-最終版」——Co比對後確認**「-最終版」不是完整超集**（非最終版仍有查證指令模板、角色分工細節等未被保留的內容），未封存，維持4個檔案並存，需要人工判斷

## Maintainer
本索引由 Claude Code 維護，新增/搬移跨專案SOP時同步更新。單一資料夾範圍的SOP不用回報這裡，維護在該專案自己的本地索引即可。
