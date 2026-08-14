#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stamp facing 朝向驗收 —— **刻意不用往返測試**。

為什麼不用往返：slice 與 stamp 共用同一張 AXIS_MAP。那張表建立在錯前提上時，
往返仍會 100% 通過（summit 2026-08-14 實測 112 顆座標與顏色全對，而圖其實是躺的）。
**往返證明的是一致性，不是正確性 —— 它測到的是那份共用轉換自己。**

改用獨立 oracle：渲染器的等角投影 `iso_y = (x+y)*H_half - z*Z_step`（z 越大畫面越高）
＋ OBJ 匯出的 `(wx,wy,wz)->(wx,wz,wy) # OBJ y-up`。兩者都說**世界的上方向是 Z**，
而且都不經過 AXIS_MAP —— 它們不用問 stamp 就能反駁 stamp。

判準刻意分兩類，避免誤告：
  - 圖**立在 Z 上**（各列 z 不同）→ 要求「圖最上」落在最大的 z，否則 FAIL（上下顛倒）
  - 圖**平躺**（各列 z 相同）→ 只回報朝向，**不判失敗**（地板貼紙的朝向是慣例題，不是缺陷）
"""
import importlib.util as ilu
import sys
from pathlib import Path

ENGINE = Path(sys.argv[1] if len(sys.argv) > 1
              else "Assets/Plugins/UCL_Core/Tools~/AgentCommands/sculpt.py")

spec = ilu.spec_from_file_location("sc", str(ENGINE))
sc = ilu.module_from_spec(spec)
spec.loader.exec_module(sc)

TOP, MID, BOT = 224, 255, 3          # 紅 / 白 / 藍
LABEL = {TOP: "圖最上", MID: "圖中間", BOT: "圖最下"}
painted = [(0, 0, TOP), (0, 1, MID), (0, 2, BOT)]   # 1 寬 x 3 高的直條

print("# stamp facing 朝向驗收（oracle = 渲染器投影式，非往返）")
print()

fails = []
for facing in ("z+", "z-", "y+", "y-", "x+", "x-"):
    space = sc.SparseVoxelSpace()
    placed, *_ = sc.stamp_pixels(space, painted, 3, [50, 50, 50], facing, 1, False)
    byz = {LABEL[v[3]]: v[2] for v in placed}
    byy = {LABEL[v[3]]: v[1] for v in placed}

    if len(set(byz.values())) > 1:                 # 立在上方向軸(Z)上
        if byz["圖最上"] == max(byz.values()):
            verdict = "OK   立著，且圖最上在最高處"
        else:
            verdict = "FAIL 立著但**上下顛倒**（圖最上落在最低的 z）"
            fails.append(facing)
    else:                                          # 平躺於地面
        away = byy["圖最上"] == min(byy.values())  # 等角投影中 y 小 = 遠 = 畫面上方
        verdict = ("INFO 平躺於地面，圖最上朝遠離觀察者（地板貼紙常見慣例）" if away
                   else "INFO 平躺於地面，圖最上朝觀察者（等於在地上轉 180 度 —— 慣例題，非缺陷）")

    print("  %-3s -> %s" % (facing, verdict))
    print("        z: " + "  ".join("%s=%s" % (k, v) for k, v in byz.items()))

print()
if fails:
    print("FAIL 上下顛倒的 facing: %s" % fails)
    print("     期望：v 映到上方向軸(Z) 的 facing 必須翻轉（影像 y 往下、Z 往上）。")
    sys.exit(1)
print("OK 沒有任何 facing 上下顛倒（平躺者為慣例題，見上）")
