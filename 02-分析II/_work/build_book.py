#!/usr/bin/env python3
"""生成《分析 II》的支撑文件。"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BOOK = os.path.join(ROOT, "02-分析II")
os.makedirs(os.path.join(BOOK, "paths"), exist_ok=True)

CHAPTERS = [
    ("ch06", "第 6 章：一元函数的积分", "chapters/ch06-integration.md", 3),
    ("ch07", "第 7 章：多变量微分学", "chapters/ch07-multivariable.md", 3),
    ("ch08", "第 8 章：线积分", "chapters/ch08-line-integrals.md", 3),
]
CONCEPTS = [
    ("c06", "黎曼积分", "concepts/riemann-integral.md", ["ch06"]),
    ("c07", "弗雷歇微分与雅可比矩阵", "concepts/frechet-derivative.md", ["ch07"]),
    ("c08", "逆映射定理与隐函数定理", "concepts/inverse-implicit.md", ["ch07"]),
    ("c09", "线积分与势函数", "concepts/line-integral.md", ["ch08"]),
    ("c10", "全纯函数", "concepts/holomorphic.md", ["ch08"]),
]

QUIZZES = [
    dict(id="q01", chapterId="ch06", type="single",
         question="下列关于跳跃连续函数的说法，正确的是？",
         options=["必须连续", "每点左右极限存在，可以不等于函数值", "只能有有限个间断点", "必须有界变差"],
         answer=1,
         explain="跳跃连续只要求单侧极限存在；分段连续才是“有限个跳跃点”的更强要求。跳跃连续函数在紧区间上自动有界。"),
    dict(id="q02", chapterId="ch06", type="single",
         question="∫_1^∞ 1/x^p 收敛的条件是？",
         options=["p > 0", "p > 1", "p < 1", "对所有 p 都收敛"],
         answer=1,
         explain="p > 1 时原函数 x^(1−p)/(1−p) 在无穷远处趋于 0；p ≤ 1 时发散。对照 ∫_0^1 1/x^p 的条件是 p < 1。"),
    dict(id="q03", chapterId="ch06", type="single",
         question="Γ(5) 等于？",
         options=["5!", "4!", "5", "24/5"],
         answer=1,
         explain="Γ(n+1) = n!，所以 Γ(5) = 4! = 24。注意指标偏移一格。"),
    dict(id="q04", chapterId="ch07", type="single",
         question="设 f(x, y) = xy/(x² + y²)（原点补 0），则 f 在原点？",
         options=["可微", "两个偏导存在但不连续", "不可微且偏导不存在", "连续但偏导不存在"],
         answer=1,
         explain="沿坐标轴 f 恒为 0，两个偏导都是 0；沿 y = x 极限为 1/2，不连续，故不可微。"),
    dict(id="q05", chapterId="ch07", type="single",
         question="隐函数定理中，保证能解出 y = φ(x) 的关键条件是？",
         options=["F(a,b) = 0", "F 连续", "∂F/∂y(a,b) 可逆", "∂F/∂x(a,b) 可逆"],
         answer=2,
         explain="要对 y 求解，必须让 y 方向的导数可逆，才能用压缩映射把 y 反解出来。"),
    dict(id="q06", chapterId="ch07", type="single",
         question="约束极值中，若 ∇g(a) ≠ 0，极值点满足？",
         options=["∇f(a) = 0", "∇f(a) = λ∇g(a)", "∇g(a) = λ∇f(a)", "f(a) = g(a)"],
         answer=1,
         explain="等值面与约束面在极值点相切，法向量平行，故梯度成比例，比例因子就是乘子 λ。"),
    dict(id="q07", chapterId="ch08", type="single",
         question="关于全变差，正确的说法是？",
         options=["连续曲线的全变差总有限", "全变差是折线长度的上确界", "全变差等于端点距离", "全变差只对直线有限"],
         answer=1,
         explain="定义就是 sup 折线长度。连续曲线可以不可求长，端点距离只是下界。"),
    dict(id="q08", chapterId="ch08", type="single",
         question="ω = (x dy − y dx)/(x² + y²) 在 ℝ² 去掉原点后？",
         options=["恰当", "闭但不恰当", "既不闭也不恰当", "恒为 0"],
         answer=1,
         explain="混合偏导相等故闭；但绕单位圆积分 2π ≠ 0，所以不存在单值势函数。"),
    dict(id="q09", chapterId="ch08", type="single",
         question="∮_{|z|=1} dz/z 的值是？",
         options=["0", "2πi", "πi", "1"],
         answer=1,
         explain="1/z 在 0 处留数为 1，由留数定理积分等于 2πi·1。"),
    dict(id="aii-x1", chapterId="__all__", type="single",
         question="微积分基本定理 ∫_α^β f = F(β) − F(α) 成立，需要的核心条件是？",
         options=["f 有界", "f 连续（或可积）且 F′ = f", "f 单调", "F 有界"],
         answer=1,
         explain="需要 f 可积，且 F 是可微函数、F′ = f。仅有界不够（Dirichlet 函数不可积）；单调也不是必要条件。"),
    dict(id="aii-x2", chapterId="__all__", type="single",
         question="把「线积分只依赖端点」与「微分学」联系起来，正确的说法是？",
         options=["任何 1-形式都路径无关", "恰当形式的线积分等于势函数在端点的差", "闭形式一定恰当", "路径无关只对直线成立"],
         answer=1,
         explain="ω = df 时 ∫_γ ω = f(终点) − f(起点)，这是牛顿–莱布尼茨公式的曲线版。闭形式只在单连通区域上恰当。"),
]

FLASHCARDS = [
    ("ch06", "积分为什么先用阶梯函数定义？", "阶梯函数的积分是有限和，无极限；再用一致逼近延拓到跳跃连续函数，保证唯一性。", ["积分", "构造"]),
    ("ch06", "可积的实用判据？", "对每个 ε > 0 存在阶梯函数 φ 使 sup|f − φ| < ε。", ["积分"]),
    ("ch06", "微积分基本定理的两半各说什么？", "变上限积分求导得 f；反过来 ∫f = F(β) − F(α)。", ["基本定理"]),
    ("ch06", "∫ sin x / x 收敛吗？绝对收敛吗？", "收敛（条件收敛），绝对值积分发散。", ["反常积分"]),
    ("ch06", "Γ 函数与阶乘的关系？", "Γ(n+1) = n!，由 Γ(z+1) = zΓ(z) 与 Γ(1)=1 推出。", ["伽马函数"]),
    ("ch07", "多变量导数的定义？", "存在线性映射 A 使 f(a+h)=f(a)+Ah+r(h)，‖r(h)‖/‖h‖→0。", ["微分"]),
    ("ch07", "偏导存在为什么不足以保证可微？", "偏导只管坐标轴方向；可微要求所有方向的误差统一为 o(‖h‖)。xy/(x²+y²) 是反例。", ["微分", "反例"]),
    ("ch07", "算子范数是什么？", "‖A‖ = sup{‖Ax‖ : ‖x‖ ≤ 1}，是线性映射的最大放大倍数。", ["算子"]),
    ("ch07", "逆映射定理的条件？", "f 是 C¹ 且 f′(a) 是拓扑同构（可逆且逆连续）。", ["逆映射"]),
    ("ch07", "拉格朗日乘子的几何解释？", "目标函数等值面与约束面在极值点相切，梯度平行。", ["极值"]),
    ("ch08", "弧长怎么定义？", "分割折线长度的上确界，即全变差；C¹ 时等于 ∫‖γ′‖。", ["弧长"]),
    ("ch08", "连续曲线一定可求长吗？", "不一定。t cos²(π/2t) 是连续但全变差无穷的例子。", ["弧长"]),
    ("ch08", "恰当形式的积分性质？", "∫_γ ω = f(终点) − f(起点)，与路径无关。", ["线积分"]),
    ("ch08", "闭形式何时恰当？", "单连通区域上闭 ⇒ 恰当；有洞时不成立，(xdy−ydx)/(x²+y²) 是反例。", ["线积分"]),
    ("ch08", "柯西–黎曼方程？", "u_x = v_y，u_y = −v_x；等价于复可微。", ["全纯"]),
]

GLOSSARY = [
    ("阶梯函数", "在分割的每个开区间上取常数值的函数。", "ch06"),
    ("跳跃连续", "每点处左右单侧极限都存在（可不等于函数值）。", "ch06"),
    ("分段连续", "只有有限个跳跃点的跳跃连续函数。", "ch06"),
    ("柯西–黎曼积分", "本书对一元函数积分的称呼，由阶梯函数积分延拓得到。", "ch06"),
    ("微积分基本定理", "变上限积分求导得被积函数；反之积分等于原函数端点差。", "ch06"),
    ("反常积分", "区间无界或被积函数无界时，用极限定义的积分。", "ch06"),
    ("绝对收敛", "被积函数绝对值可积；绝对收敛必收敛。", "ch06"),
    ("傅里叶系数", "用三角函数内积投影得到的系数 aₖ、bₖ。", "ch06"),
    ("伽马函数", "Γ(z)=∫t^(z−1)e^(−t)dt，满足 Γ(n+1)=n!。", "ch06"),
    ("算子范数", "线性映射的最大放大倍数，‖A‖=sup‖Ax‖/‖x‖。", "ch07"),
    ("弗雷歇导数", "使 f(a+h)=f(a)+Ah+o(‖h‖) 的唯一线性映射 A。", "ch07"),
    ("雅可比矩阵", "导数在标准基下的矩阵，元素为偏导数。", "ch07"),
    ("链式法则", "复合函数导数等于两个线性映射的复合（矩阵相乘）。", "ch07"),
    ("黑塞矩阵", "二阶偏导组成的对称矩阵，表示二阶导数。", "ch07"),
    ("逆映射定理", "导数可逆时函数局部可逆，逆映射 C¹ 且导数为原导数的逆。", "ch07"),
    ("隐函数定理", "F(a,b)=0 且对 y 的偏导可逆时，可局部解出 y=φ(x)。", "ch07"),
    ("拉格朗日乘子", "约束极值中使 ∇f=λ∇g 的比例因子。", "ch07"),
    ("全变差", "所有分割折线长度的上确界。", "ch08"),
    ("可求长", "全变差有限的曲线。", "ch08"),
    ("普法夫形式", "形如 Σaⱼdxⱼ 的 1-形式。", "ch08"),
    ("恰当形式", "等于某个函数微分的 1-形式。", "ch08"),
    ("势函数", "满足 df=ω 的函数 f。", "ch08"),
    ("全纯函数", "复可微的函数，等价于满足柯西–黎曼方程。", "ch08"),
    ("亚纯函数", "除孤立极点外全纯的函数。", "ch08"),
    ("留数", "洛朗展开中 (z−a)⁻¹ 的系数。", "ch08"),
]

PATH_MD = """# 学习路径：《分析 II》

覆盖原书第 6–8 章，从一元积分到多变量微分，再到线积分与复分析入门。终点能力：能算常见积分、能判断反常积分收敛、能写多变量泰勒公式、能判断线积分是否路径无关。

## 路径总览

```mermaid
flowchart LR
  S1[06 积分与基本定理] --> S2[07 多变量微分]
  S2 --> S3[08 线积分与全纯]
```

## 步骤 6：积分

**目标**：能用阶梯逼近理解积分定义，熟练使用基本定理、换元、分部；能判断反常积分收敛。
**阅读**：ch06-integration.md，配合「黎曼积分」。
**检查点**：ch06 自测三题；能独立算出 ∫₀^{π/2} sin²x dx。
**复习**：卡片标签「积分」「反常积分」。

## 步骤 7：多变量微分

**目标**：把导数理解为线性映射，能写雅可比矩阵，能陈述逆映射与隐函数定理。
**阅读**：ch07-multivariable.md，配合「弗雷歇微分」「逆映射与隐函数」。
**检查点**：ch07 自测三题；能用隐函数定理求圆上一点的导数。
**复习**：卡片标签「微分」「逆映射」。

## 步骤 8：线积分与全纯

**目标**：能判断形式是否恰当、求势函数、算线积分；理解全纯与柯西–黎曼。
**阅读**：ch08-line-integrals.md，配合「线积分与势函数」「全纯函数」。
**检查点**：ch08 自测三题；能算出 ∮(xdy−ydx) 在单位圆上的值。
**复习**：卡片标签「线积分」「全纯」。

## 学完全程后

- 你能：用积分技巧处理面积、弧长、功；用隐函数定理解方程；用势函数判断保守场。
- 综合检验：给定 F(x,y,z) = (y, x, 0)，判断它是否为保守场，求势函数，并计算从 (0,0,0) 到 (1,2,3) 的线积分；再说明若去掉 z 轴，结论是否改变。
"""

PATTERNS_MD = """# 模式与框架库：《分析 II》

## 框架：逼近 → 延拓 → 性质

积分、线积分、微分形式都走同一条路：先在简单对象（阶梯函数、折线、常系数形式）上定义量，证明它在 sup 范数或一致收敛下连续，再延拓到闭包，最后证明延拓后的对象保持线性与基本估计。遇到新定义，先问"简单对象是什么、逼近用什么范数、延拓凭什么唯一"。

## 框架：把非线性问题局部线性化

多变量的所有存在性定理都是这个套路：取 A = f′(a)，把方程改写成 x = x − A⁻¹(F(x))，验证压缩，得到不动点。逆映射、隐函数、流形、微分方程解的存在性都是同一模板的不同外衣。

## 决策规则

- 判断偏导能否替代导数：先看偏导是否连续（C¹）；连续则可用，不连续要找反例。
- 判断反常积分：先找比较对象 x^{-p}，再看区间方向决定 p 的不等式方向。
- 判断路径无关：先算 ∂aⱼ/∂xₖ 是否相等；相等再看区域是否有洞。
- 判断全纯：先写 u、v 验柯西–黎曼；满足再谈积分。

## 反模式

- **把雅可比矩阵当成"导数本身"**。换基就换矩阵，导数是映射。
- **用偏导存在冒充可微**。xy/(x²+y²) 是常备反例。
- **在临界点硬用隐函数定理**。∂F/∂y = 0 时解可能分裂，必须换坐标或改用其他方法。
- **把条件收敛的积分随意重排**。收敛不等于绝对收敛，重排会改变结果。
"""

CHEATSHEET_MD = """# 速查表：《分析 II》

## 定义与公式

| 场景 | 内容 |
|---|---|
| 阶梯函数积分 | Σ cⱼ(αⱼ − αⱼ₋₁) |
| 积分估计 | ｜∫f｜ ≤ ‖f‖∞(β − α) |
| 基本定理 | (∫_α^x f)′ = f；∫_α^β f = F(β) − F(α) |
| 换元 | ∫f(φ(t))φ′(t)dt = ∫f(u)du |
| 分部 | ∫u′v = uv − ∫uv′ |
| p-积分 | ∫_1^∞ x^{−p} 收敛 ⇔ p>1；∫_0^1 x^{−p} 收敛 ⇔ p<1 |
| 算子范数 | ‖A‖ = sup_{‖x‖≤1}‖Ax‖ |
| 可微 | f(a+h)=f(a)+Ah+r(h)，‖r(h)‖/‖h‖→0 |
| 雅可比 | Jᵢⱼ = ∂fᵢ/∂xⱼ |
| 链式 | (f∘g)′ = f′(g(a))g′(a) |
| 泰勒二阶 | f(a+h)=f(a)+Df(a)h+½D²f(a)(h,h)+o(‖h‖²) |
| 逆映射 | (f⁻¹)′(f(a)) = f′(a)⁻¹ |
| 隐函数 | φ′ = −(∂F/∂y)⁻¹∂F/∂x |
| 乘子法 | ∇f = λ∇g，g=0 |
| 全变差 | Var(γ) = sup_Z Σ‖γ(tⱼ)−γ(tⱼ₋₁)‖ |
| 弧长 | C¹ 时 L(γ)=∫‖γ′(t)‖dt |
| 线积分 | ∫_γ ω = ∫_a^b Σaⱼ(γ(t))γⱼ′(t)dt |
| 恰当 | ω=df ⇒ ∫_γ ω = f(终点)−f(起点) |
| 柯西–黎曼 | u_x=v_y，u_y=−v_x |
| 留数 | ∮f dz = 2πiΣRes(f,aₖ) |

## 常用推理链

1. 阶梯函数 → 一致逼近 → 积分 → 基本定理 → 计算。
2. 偏导连续 → 可微 → 雅可比 → 链式 → 逆映射/隐函数。
3. 1-形式 → 闭性检验 → 单连通 → 势函数 → 路径无关。
4. 复可微 → 柯西–黎曼 → 解析 → 柯西定理 → 留数。

## 反例清单

| 命题 | 反例 |
|---|---|
| 连续曲线可求长 | t cos²(π/2t) |
| 偏导存在则可微 | xy/(x²+y²) |
| 闭形式必恰当 | (xdy−ydx)/(x²+y²) |
| 条件收敛可重排 | ∫sin x/x |
| 实可微即全纯 | f(z)=\u007abar(z) |
"""

SKILL_MD = """---
name: 分析 II（点化学习总纲）
---

# 《分析 II》点化学习系统

## 这本书在讲什么

第二卷把第一卷的极限与连续工具用到三个新战场：一元积分、多变量微分、曲线上的积分。它的主线是"逼近"与"线性化"：积分用阶梯函数逼近，多变量导数用仿射映射逼近，线积分用 1-形式沿曲线累加。最后以全纯函数收尾，展示一维复分析如何把线积分理论变成留数计算。

## 全书心智模型

```mermaid
flowchart TB
  I[阶梯逼近] --> G[一元积分]
  G --> B[基本定理]
  B --> T[换元 分部]
  G --> A[反常积分]
  L[仿射逼近] --> M[多变量微分]
  M --> J[雅可比 链式]
  M --> R[逆映射 隐函数]
  M --> F[流形 切空间]
  G --> C[线积分]
  M --> C
  C --> H[全纯 留数]
```

## 学习路径（推荐顺序）

| 步骤 | 章节 | 主题 | 前置 | 检查点 |
|---|---|---|---|---|
| 06 | ch06 | 积分、基本定理、反常积分 | 分析 I 第 3–5 章 | ch06 自测三题 |
| 07 | ch07 | 多变量微分、隐函数 | ch06 | ch07 自测三题 |
| 08 | ch08 | 曲线、线积分、全纯 | ch06、ch07 | ch08 自测三题 |

## 章节索引

- 第 6 章 一元函数的积分（难度 ★★★）→ chapters/ch06-integration.md
- 第 7 章 多变量微分学（难度 ★★★）→ chapters/ch07-multivariable.md
- 第 8 章 线积分（难度 ★★★）→ chapters/ch08-line-integrals.md

## 前置知识（零基础缺口补讲）

| 缺口 | 对应补讲位置 | 学完标志 |
|---|---|---|
| 不熟悉一致收敛 | 分析 I 第 5 章 | 能解释为什么积分要用一致逼近 |
| 不会算定积分 | ch06 概念 3、概念 4 | 能独立算 5 个常见积分 |
| 没接触过线性映射 | ch07 概念 1 | 能算 2×2 矩阵的算子范数 |
| 没学过复变 | ch08 概念 4 | 能验柯西–黎曼方程 |

## 术语表 / 模式库 / 速查表 入口

- 术语：glossary.md
- 模式：patterns.md
- 速查：cheatsheet.md
"""


def write(path, text):
    with open(os.path.join(BOOK, path), "w", encoding="utf-8") as f:
        f.write(text)
    print("写入", path)


def render_q(q, idx):
    lines = [f"### Q{idx}.（{'填空' if q['type']=='blank' else '单选'}）{q['question']}\n"]
    if q["options"]:
        letters = "ABCD"
        lines.append("　".join(f"{letters[i]}. {o}" for i, o in enumerate(q["options"])) + "\n")
    lines.append(f"**答案**：{q['answer'] if q['type']=='blank' else 'ABCD'[q['answer']]}\n")
    lines.append(f"**解析**：{q['explain']}\n")
    return "\n".join(lines)


def render_quiz_md():
    out = ["# 《分析 II》测验\n"]
    for ch in CHAPTERS:
        out.append(f"\n## {ch[1]}测验（检查点）\n")
        idx = 0
        for q in QUIZZES:
            if q["chapterId"] == ch[0]:
                idx += 1
                out.append(render_q(q, idx))
    out.append("\n## 综合测验（多章联考）\n")
    idx = 0
    for q in QUIZZES:
        if q["chapterId"] == "__all__":
            idx += 1
            out.append(render_q(q, idx))
    out.append("\n## 最终检验\n")
    out.append("给定 F(x,y,z) = (y, x, 0)：判断是否为保守场；求势函数；计算从 (0,0,0) 到 (1,2,3) 的线积分；再讨论去掉 z 轴后 ω 的恰当性是否改变。评分要点：闭性检验、单连通性讨论、势函数差、结论一致性。\n")
    return "".join(out)


def render_cards_md():
    out = ["# 《分析 II》抽认卡\n"]
    for ch in CHAPTERS:
        out.append(f"\n## {ch[1]}\n")
        for cid, front, back, tags in FLASHCARDS:
            if cid == ch[0]:
                out.append(f"### 卡片：{front}\n- **背面**：{back}\n- **标签**：{', '.join(tags)}\n- **章节**：{cid}\n")
    return "".join(out)


def render_glossary_md():
    out = ["# 术语表\n\n| 术语 | 白话定义 | 首次出现 | 章节 |\n|---|---|---|---|\n"]
    for term, d, cid in GLOSSARY:
        title = next(c[1] for c in CHAPTERS if c[0] == cid)
        out.append(f"| {term} | {d} | {cid} | {title} |\n")
    return "".join(out)


def build_manifest():
    cards = [{"id": f"f{i:02d}", "chapterId": cid, "front": front, "back": back, "tags": tags}
             for i, (cid, front, back, tags) in enumerate(FLASHCARDS, 1)]
    return {
        "slug": "analysis-ii",
        "title": "分析 II",
        "subtitle": "从积分到流形：逼近与线性化的进阶",
        "book": {
            "title": "分析 II（Analysis II）",
            "author": "Herbert Amann / Joachim Escher",
            "source": ["分析 II (Herbert Amann  Joachim Escher) (z-library.sk, 1lib.sk, z-lib.sk).pdf"],
        },
        "audience": "已读完《分析 I》或具备同等基础",
        "goal": "掌握一元积分、多变量微分、线积分与复分析入门",
        "learningPath": [
            {"step": "06", "title": "积分与基本定理", "chapterIds": ["ch06"], "checkpoint": "ch06 自测三题"},
            {"step": "07", "title": "多变量微分", "chapterIds": ["ch07"], "checkpoint": "ch07 自测三题"},
            {"step": "08", "title": "线积分与全纯", "chapterIds": ["ch08"], "checkpoint": "ch08 自测三题"},
        ],
        "chapters": [{"id": c[0], "title": c[1], "file": c[2], "difficulty": c[3]} for c in CHAPTERS],
        "concepts": [{"id": c[0], "title": c[1], "file": c[2], "chapterIds": c[3]} for c in CONCEPTS],
        "glossary": [{"term": g[0], "def": g[1], "chapterId": g[2]} for g in GLOSSARY],
        "patterns": {"file": "patterns.md"},
        "cheatsheet": {"file": "cheatsheet.md"},
        "quizzes": QUIZZES,
        "flashcards": cards,
        "companion": "analysis-ii学习伴侣.html",
    }


if __name__ == "__main__":
    write("paths/learn.md", PATH_MD)
    write("patterns.md", PATTERNS_MD)
    write("cheatsheet.md", CHEATSHEET_MD)
    write("SKILL.md", SKILL_MD)
    write("quiz.md", render_quiz_md())
    write("flashcards.md", render_cards_md())
    write("glossary.md", render_glossary_md())
    with open(os.path.join(BOOK, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(build_manifest(), f, ensure_ascii=False, indent=2)
    print("写入 manifest.json")
