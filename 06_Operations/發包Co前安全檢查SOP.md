# 發包Co（`codex exec`）前的安全檢查SOP

> 2026-08-03由「操控與控制」資料夾內的聊天室建立、2026-08-04轉正搬到AIOS（跨專案通用技巧，任何session只要會呼叫`codex exec`都適用，不限單一資料夾任務）。原位置`操控與控制\_發包Co前安全檢查SOP_lulu_20260803.md`已改成指標檔。
>
> **這份SOP的誕生本身就是一次真實的「孤兒SOP」事故**：同一天稍早這個技巧只寫在memory筆記裡（`feedback_double_check_codex_idle_before_dispatch_20260802.md`），另一個聊天室要用時沒能正確叫出這條記憶，自己土法煉鋼判斷「process check不可靠只能問妹」，跟已經驗證有效的CPU delta方法完全不同——證實「有索引的SOP檔案」比「純memory筆記」更容易被穩定找到。這份文件第一版寫在`操控與控制`資料夾時，還犯了第二次同類錯誤（放在只有做該資料夾任務的session才會去讀的地方），這次轉正到AIOS才是真正解決「任何session都要找得到」這個問題。

## 為什麼需要這個檢查
`codex exec`平行執行（同一時間有2個以上`codex exec`同時在跑）會觸發已知的並行亂碼bug——輸出大量`?????`取代整段中文，這是實測驗證過的真實故障模式，不是理論風險。

妹常常同時開多個聊天室（Claude Code或其他AI工具）處理同一組資產，如果兩邊「剛好都在同一時間各自呼叫`codex exec`」，就會撞上這個bug。

## 正確做法：CPU delta雙重確認法

**不要只檢查一次process有沒有在跑**——單一次的process list檢查不可靠，因為單一個`codex exec`呼叫內部本身可能因為supervisor/sandbox worker架構就有多個行程存在，光看「有沒有process」分不出是不是別的聊天室在跑一個真正的任務。

**正確方法是量測CPU使用量的變化（delta），而且要做兩次**：

```powershell
# 第一次讀數
try { $p1 = Get-Process -Name codex -ErrorAction Stop | Measure-Object CPU -Sum; "CPU1: $($p1.Sum)" } catch { "no codex process running" }
```

等待幾秒（例如用`sleep 8`或`Start-Sleep 8`）

```powershell
# 第二次讀數
try { $p2 = Get-Process -Name codex -ErrorAction Stop | Measure-Object CPU -Sum; "CPU2: $($p2.Sum)" } catch { "no codex process running" }
```

**判斷標準**：
- 如果兩次都顯示「no codex process running」→ 閒置，可以發包
- 如果兩次CPU數字幾乎沒變（delta < 8秒等級的差異）→ 閒置（背景常駐行程本身也會有一點點CPU使用，不代表在跑任務），可以發包
- 如果CPU數字持續明顯增加 → 真的在跑任務，不要發包，等一下再檢查

**⚠️ 常見誤區**：不要只看「有沒有`codex.exe`這個process存在」就判斷有沒有在工作。Codex App本身可能常駐在背景（開著視窗但沒在執行任何任務），process存在是正常的，不代表正在跑一個真正的任務。只有「CPU持續消耗」才代表真的在執行工作。**2026-08-04再次驗證**：實測確認沒有任何比CPU delta更可靠的技術判斷方式——即使查到某個codex.exe行程已經常駐一整天，也看不出「現在是不是正在跑一個任務」，這不是查詢方法不夠好，是這個資訊本身在作業系統層級就無法從外部單純判斷。

## 如果不確定，直接問妹

CPU delta方法不是100%萬能——如果檢查完還是不確定（例如剛好卡在一個很輕量、CPU使用量很低的任務中間），**不要賭運氣硬發**，直接問妹：「另一個聊天室現在有在跑codex exec嗎？」，等她確認後才送出。**問了就要等答案，不要在等待期間又接著做別的動作**（2026-08-04的真實教訓：曾經問完沒等回覆就自己接著問了SG的事，這是疏失）。

如果妹說不確定或她自己也搞不清楚哪個視窗在跑什麼，一樣先暫停，不要硬發。

## 兩次確認的實際操作習慣（重要）

每次要`codex exec`發包之前：
1. 讀CPU第一次
2. 等待數秒（`sleep 8`或`Start-Sleep -Seconds 8`）
3. 讀CPU第二次
4. 確認delta在安全範圍才送出`codex exec`指令

這個「兩次讀數夾一個等待」的模式要**每次發包前都做**，不是只在session一開始做一次就好，因為聊天室之間互相不知道彼此的狀態，隨時都可能有新的任務被其他視窗發起。
