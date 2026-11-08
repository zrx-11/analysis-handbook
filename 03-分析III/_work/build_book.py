#!/usr/bin/env python3
"""生成《分析 III》的支撑文件。"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BOOK = os.path.join(ROOT, "03-分析III")
os.makedirs(os.path.join(BOOK, "paths"), exist_ok=True)

CHAPTERS = [
    ("ch09", "第 9 章：测度论基础", "chapters/ch09-measure.md", 3),
    ("ch10", "第 10 章：积分理论", "chapters/ch10-integration-theory.md", 3),
    ("ch11", "第 11 章：流形与微分形式", "chapters/ch11-manifolds-forms.md", 3),
    ("ch12", "第 12 章：流形上的积分", "chapters/ch12-manifold-integration.md", 3),
]
CONCEPTS = [
    ("c11", "σ-代数与测度", "concepts/sigma-algebra-measure.md", ["ch09", "ch10"]),
    ("c12", "外测度与可测集", "concepts/outer-measure.md", ["ch09"]),
    ("c13", "收敛定理", "concepts/convergence-theorems.md", ["ch10"]),
    ("c14", "Lp 空间", "concepts/lp-spaces.md", ["ch10"]),
    ("c15", "微分形式与斯托克斯定理", "concepts/differential-forms-stokes.md", ["ch11", "ch12"]),
]

QUIZZES = [
    dict(id="q01", chapterId="ch09", type="single",
         question="σ-代数不需要满足下列哪条？",
         options=["包含全集", "对补集封闭", "对可数并封闭", "对任意并封闭"],
         answer=3,
         explain="σ-代数只要求可数并封闭；任意并超出可数可加性的框架，也不需要。"),
    dict(id="q02", chapterId="ch09", type="single",
         question="卡拉泰奥多里条件的作用是？",
         options=["定义外测度", "筛选出可测集", "证明选择公理", "计算体积"],
         answer=1,
         explain="条件 μ*(T) = μ*(T∩A) + μ*(T∩Aᶜ) 对所有 T 成立时称 A 可测，这是从外测度得到测度的筛子。"),
    dict(id="q03", chapterId="ch09", type="single",
         question="康托集的性质是？",
         options=["可数且测度为 0", "不可数且测度为 0", "不可数且测度为正", "可数且测度为正"],
         answer=1,
         explain="康托集与 [0,1] 等势（不可数），但总长度（测度）为 0。元素多少与测度大小是两回事。"),
    dict(id="q04", chapterId="ch10", type="single",
         question="勒贝格积分相对黎曼积分的核心优势是？",
         options=["能算更多初等函数", "不需要测度", "在更弱条件下交换极限与积分", "只适用于连续函数"],
         answer=2,
         explain="控制收敛定理只需逐点收敛 + 可积控制函数，黎曼积分通常要一致收敛。计算能力不是主要差别。"),
    dict(id="q05", chapterId="ch10", type="single",
         question="控制收敛定理中“存在可积的 g 使 |fₙ| ≤ g”能否去掉？",
         options=["能，只要 fₙ 逐点收敛", "不能，nχ_{(0,1/n)} 是反例", "能，只要 fₙ 非负", "能，只要测度有限"],
         answer=1,
         explain="该例逐点收敛到 0，但积分恒为 1；没有可积控制函数，结论失效。"),
    dict(id="q06", chapterId="ch10", type="single",
         question="换元公式中出现的因子是？",
         options=["det Dφ 的绝对值", "det Dφ 的平方", "‖Dφ‖", "φ 的导数之和"],
         answer=0,
         explain="雅可比行列式的绝对值是局部体积放大率；一维时就是 |φ′|。"),
    dict(id="q07", chapterId="ch11", type="single",
         question="关于外微分，正确的说法是？",
         options=["d(dω) = ω", "d(dω) = 0", "d 只在 0-形式上定义", "d 与拉回不可交换"],
         answer=1,
         explain="d² = 0 是外微分的代数性质；恰当形式必闭，但闭不一定恰当。"),
    dict(id="q08", chapterId="ch11", type="single",
         question="极坐标下 dx ∧ dy 等于？",
         options=["dr ∧ dθ", "r dr ∧ dθ", "r² dr ∧ dθ", "dr ∧ dθ / r"],
         answer=1,
         explain="直接计算得 dx ∧ dy = r dr ∧ dθ，因子 r 就是极坐标换元的雅可比行列式。"),
    dict(id="q09", chapterId="ch11", type="single",
         question="黎曼度量给出的体积元是？",
         options=["det(g) dx", "√|det(g)| dx¹∧…∧dxᵐ", "trace(g) dx", "‖g‖ dx"],
         answer=1,
         explain="体积元是 √|det g| 乘以坐标楔积；正定度量可以去掉绝对值。"),
    dict(id="q10", chapterId="ch12", type="single",
         question="流形上体积元的表达式是？",
         options=["dx¹∧…∧dxᵐ", "√|det G| dx¹∧…∧dxᵐ", "det(G) dx", "√(trace G) dx"],
         answer=1,
         explain="体积元 = √|det G| 乘坐标楔积；欧氏度量为 1，球坐标为 R² sin θ。"),
    dict(id="q11", chapterId="ch12", type="single",
         question="斯托克斯定理 ∫_∂M ω = ∫_M dω 中，ω 必须是？",
         options=["任意函数", "0-形式", "m-形式", "(m−1)-形式"],
         answer=3,
         explain="d 把 (m−1)-形式变成 m-形式，才能在 m 维 M 上积分；边界是 (m−1) 维。"),
    dict(id="q12", chapterId="ch12", type="single",
         question="球面 S² 的面积是？",
         options=["2πR²", "4πR²", "4πR³/3", "πR²"],
         answer=1,
         explain="∫₀^{2π}∫₀^{π} R² sin θ dθ dφ = 4πR²。4πR³/3 是球的体积。"),
    dict(id="aiii-x1", chapterId="__all__", type="single",
         question="把测度、积分、流形积分串起来，正确的逻辑顺序是？",
         options=["先定义积分再定义测度", "σ-代数 → 测度 → 可测函数 → 积分 → 流形上的体积元",
                  "流形积分是独立理论，与测度无关", "黎曼积分可以直接推广到流形"],
         answer=1,
         explain="先有可测结构才有测度，才有可测函数与积分；流形上的体积测度是用坐标卡把局部勒贝格测度抬上去的。"),
    dict(id="aiii-x2", chapterId="__all__", type="single",
         question="关于斯托克斯定理与拓扑，正确的说法是？",
         options=["闭形式在任何流形上的积分都为 0", "闭形式的积分可以非零，反映流形的洞",
                  "恰当形式不能积分", "斯托克斯定理只对 1-形式成立"],
         answer=1,
         explain="闭形式在带洞流形上的积分可以非零（如 ∮dz/z = 2πi），这正是德拉姆上同调捕捉的拓扑信息。"),
]

FLASHCARDS = [
    ("ch09", "σ-代数的三条公理？", "含全集；对补集封闭；对可数并封闭。", ["测度", "σ-代数"]),
    ("ch09", "外测度与测度的差别？", "外测度对所有子集有定义但只次可加；限制在可测集上才成为测度。", ["测度"]),
    ("ch09", "卡拉泰奥多里条件？", "对所有 T，μ*(T)=μ*(T∩A)+μ*(T∩Aᶜ) 时称 A 可测。", ["测度", "可测"]),
    ("ch09", "康托集的测度与势？", "测度 0，但不可数。", ["反例"]),
    ("ch09", "为什么不能给所有子集赋平移不变测度？", "与选择公理冲突：维塔利构造出不可测集。", ["测度", "选择公理"]),
    ("ch10", "简单函数与可测函数的关系？", "可测函数是简单函数列的几乎处处极限。", ["积分"]),
    ("ch10", "积分定义的三步？", "简单函数积分 → 非负函数取单调极限 → 一般函数拆正负部。", ["积分"]),
    ("ch10", "L1 完备化是什么意思？", "先定义简单函数上的积分，再按 L1 范数取完备化，得到博赫纳–勒贝格积分。", ["积分", "完备"]),
    ("ch10", "控制收敛的条件？", "fₙ→f a.e.，且存在可积 g 使 |fₙ|≤g a.e.。", ["收敛定理"]),
    ("ch10", "Lp 的元素是什么？", "几乎处处相等的函数等价类，不是单个函数。", ["Lp"]),
    ("ch11", "k-形式的定义？", "交替 k-线性映射，交换两个自变量变号。", ["形式"]),
    ("ch11", "楔积的性质？", "α∧β=−β∧α，α∧α=0；dx∧dy 在向量组上取值等于行列式。", ["形式"]),
    ("ch11", "d²=0 的含义？", "外微分的两次作用为零；恰当形式必闭。", ["形式"]),
    ("ch11", "浸入与嵌入的差别？", "浸入要求切映射单射；嵌入还要求到像的同胚（不自交）。", ["流形"]),
    ("ch11", "体积元与度量的关系？", "dV=√|det g| dx¹∧…∧dxᵐ，det g 是格拉姆行列式。", ["度量"]),
    ("ch12", "流形上如何定义可测集？", "逐坐标卡：φ(A∩U) 是 ℝᵐ 的勒贝格可测集；与坐标卡无关。", ["流形", "测度"]),
    ("ch12", "斯托克斯定理的内容？", "∫_∂M ω = ∫_M dω，ω 是 (m−1)-形式，M 可定向有边。", ["斯托克斯"]),
    ("ch12", "斯托克斯的四个特例？", "微积分基本定理、格林公式、高斯散度定理、经典斯托克斯公式。", ["斯托克斯"]),
    ("ch12", "球面面积怎么算？", "∫₀^{2π}∫₀^{π} R² sin θ dθ dφ = 4πR²。", ["计算"]),
    ("ch12", "闭形式积分非零说明什么？", "流形有洞；积分值反映同调/拓扑信息。", ["拓扑"]),
]

GLOSSARY = [
    ("σ-代数", "对补集与可数并封闭、含全集的集合族。", "ch09"),
    ("测度", "σ-代数上的可数可加非负函数。", "ch09"),
    ("博雷尔 σ-代数", "包含所有开集的最小 σ-代数。", "ch09"),
    ("外测度", "用可数覆盖的体积下确界定义、对所有子集有定义的函数。", "ch09"),
    ("可测集", "满足卡拉泰奥多里切割条件的集合。", "ch09"),
    ("零测集", "测度为 0 的集合。", "ch09"),
    ("几乎处处", "除一个零测集之外处处成立。", "ch09"),
    ("勒贝格测度", "ℝⁿ 上由外测度限制得到的平移不变测度。", "ch09"),
    ("豪斯多夫维数", "使豪斯多夫测度从无穷跳到零的临界维数。", "ch09"),
    ("简单函数", "有限个特征函数的线性组合，只取有限多个值。", "ch10"),
    ("可测函数", "简单函数列的几乎处处极限。", "ch10"),
    ("博赫纳–勒贝格积分", "向量值函数通过 L1 完备化定义的积分。", "ch10"),
    ("单调收敛定理", "非负递增函数列可无条件交换极限与积分。", "ch10"),
    ("法图引理", "非负函数列给出 ∫liminf ≤ liminf∫ 的不等式。", "ch10"),
    ("控制收敛定理", "存在可积控制函数时，逐点收敛可交换极限与积分。", "ch10"),
    ("Lp 空间", "p 次方可积函数的等价类空间，配 Lp 范数。", "ch10"),
    ("赫尔德不等式", "‖fg‖₁ ≤ ‖f‖ₚ‖g‖_q，1/p+1/q=1。", "ch10"),
    ("闵可夫斯基不等式", "Lp 范数满足三角不等式。", "ch10"),
    ("富比尼定理", "乘积空间上的积分可化为累次积分。", "ch10"),
    ("卷积", "(f∗g)(x)=∫f(x−y)g(y)dy，傅里叶变换下变乘积。", "ch10"),
    ("磨光核", "光滑紧支、积分为 1 的非负函数，用于逼近光滑化。", "ch10"),
    ("傅里叶变换", "f̂(ξ)=∫f(x)e^(−2πix·ξ)dx，L² 上是酉算子。", "ch10"),
    ("子流形", "局部在坐标卡中表现为平面切片的子集。", "ch11"),
    ("浸入", "切映射处处单射的光滑映射。", "ch11"),
    ("嵌入", "到像为同胚的浸入。", "ch11"),
    ("带边流形", "坐标卡取值于半空间，边界为 xₘ=0 的像。", "ch11"),
    ("k-形式", "交替 k-线性映射，可楔积、拉回、外微分。", "ch11"),
    ("外微分", "d(Σa_I dx^I)=Σda_I∧dx^I，满足 d²=0。", "ch11"),
    ("闭形式", "dω=0 的形式。", "ch11"),
    ("恰当形式", "等于 dη 的形式。", "ch11"),
    ("黎曼度量", "每点切空间上的正定内积场。", "ch11"),
    ("霍奇星", "依赖度量与定向、把 k-形式映为 (m−k)-形式的算子。", "ch11"),
    ("体积元", "√|det g| dx¹∧…∧dxᵐ，流形上的积分缩放因子。", "ch12"),
    ("斯托克斯定理", "∫_∂M ω = ∫_M dω，统一所有积分公式。", "ch12"),
]

PATH_MD = """# 学习路径：《分析 III》

覆盖原书第 9–12 章：测度、积分理论、微分形式、流形积分。这是三卷中最抽象的一段，建议每章都先读"一句话核心"，再逐概念推进。

## 路径总览

```mermaid
flowchart LR
  S1[09 测度] --> S2[10 积分理论]
  S2 --> S3[11 形式与流形]
  S3 --> S4[12 流形积分 斯托克斯]
```

## 步骤 9：测度

**目标**：能写出 σ-代数与测度公理，能解释外测度为什么要用卡拉泰奥多里条件筛可测集。
**阅读**：ch09-measure.md，配合「σ-代数与测度」「外测度与可测集」。
**检查点**：ch09 自测三题；能说明康托集为什么测度为 0。
**复习**：卡片标签「测度」。

## 步骤 10：积分理论

**目标**：能用简单函数逼近定义积分，能陈述并应用三大收敛定理，能说明 Lp 的等价类问题。
**阅读**：ch10-integration-theory.md，配合「收敛定理」「Lp 空间」。
**检查点**：ch10 自测三题；能构造控制收敛失效的反例。
**复习**：卡片标签「积分」「收敛定理」。

## 步骤 11：流形与微分形式

**目标**：能判断形式是否闭/恰当，能算极坐标下的 dx∧dy，能说明浸入与嵌入的差别。
**阅读**：ch11-manifolds-forms.md，配合「微分形式与斯托克斯定理」。
**检查点**：ch11 自测三题；能独立算出极坐标体积元。
**复习**：卡片标签「形式」「流形」。

## 步骤 12：流形上的积分

**目标**：能用体积元算球面面积，能写出斯托克斯定理并指出它是四个经典公式的统一。
**阅读**：ch12-manifold-integration.md。
**检查点**：ch12 自测三题；能复述单位分解在证明中的作用。
**复习**：卡片标签「斯托克斯」「计算」。

## 学完全程后

- 你能：独立读懂测度论的基本构造；用收敛定理论证极限交换；在具体流形上算体积与通量。
- 综合检验：选一个带洞区域（如 ℝ² 去掉原点），验证 ω=(xdy−ydx)/(x²+y²) 闭而不恰当，说明斯托克斯定理在该区域如何"失败"，并解释这个失败为什么是拓扑的而不是分析的。
"""

PATTERNS_MD = """# 模式与框架库：《分析 III》

## 框架：覆盖 → 外测度 → 筛可测 → 得测度

这是卡拉泰奥多里路线的四步。遇到"给某类集合赋大小"的问题，先想清楚覆盖用什么基本块（区间、长方体、球），再验证次可加，再用切割条件筛，最后证明限制后满足可数可加。

## 框架：简单函数 → 可测函数 → 积分 → 完备化

积分的标准脚手架。每一步都问"逼近用什么收敛"：简单函数到可测函数是几乎处处，积分定义是单调极限，L1 完备化是范数收敛。

## 框架：局部坐标 + 单位分解

流形上的全局命题几乎都这样证：用单位分解把整体切成有限块，每块落在坐标卡内，化成 ℝᵐ 的命题，证完再拼回去。斯托克斯定理是标准范例。

## 决策规则

- 要交换极限与积分：先说清是单调、非负还是有控制函数；三者都不满足就找反例。
- 要判断形式是否恰当：先算 dω；闭了再看区域有没有洞；星形区域可直接用庞加莱引理。
- 要算流形上的积分：先定坐标卡，再算度量矩阵，再取 √det G，最后套普通多重积分。

## 反模式

- **把外测度当测度用**。外测度只次可加，直接相加会出错。
- **忽略等价类**。Lp 里"几乎处处相等"的函数是同一元素，范数为 0 不代表函数为零。
- **忘掉定向**。流形积分换定向变号；不可定向时只能取绝对值。
- **在带洞区域硬用"闭 ⇒ 恰当"**。洞是拓扑障碍，局部条件消不掉。
"""

CHEATSHEET_MD = """# 速查表：《分析 III》

## 定义与公式

| 场景 | 内容 |
|---|---|
| σ-代数 | 含 X；对补集封闭；对可数并封闭 |
| 测度 | μ(∅)=0；不交列 μ(∪Aⱼ)=Σμ(Aⱼ) |
| 外测度 | λ*(A)=inf Σvol(Qⱼ)，A⊆∪Qⱼ |
| 可测（卡拉泰奥多里） | 对所有 T：μ*(T)=μ*(T∩A)+μ*(T∩Aᶜ) |
| 可测函数 | 简单函数列的 a.e. 极限 |
| 简单函数积分 | Σ eⱼ μ(Aⱼ) |
| 单调收敛 | 0≤fₙ↑f ⇒ ∫fₙ↑∫f |
| 法图引理 | ∫liminf fₙ ≤ liminf ∫fₙ |
| 控制收敛 | fₙ→f a.e.，|fₙ|≤g∈L¹ ⇒ ∫fₙ→∫f |
| Lp 范数 | ‖f‖ₚ=(∫|f|ᵖ)^(1/p) |
| 赫尔德 | ‖fg‖₁≤‖f‖ₚ‖g‖_q，1/p+1/q=1 |
| 闵可夫斯基 | ‖f+g‖ₚ≤‖f‖ₚ+‖g‖ₚ |
| 富比尼 | ∫∫f = ∫(∫f dν)dμ = ∫(∫f dμ)dν（绝对可积） |
| 换元 | ∫_V f dy = ∫_U f(φ(x))|det Dφ| dx |
| 卷积 | (f∗g)(x)=∫f(x−y)g(y)dy |
| 傅里叶变换 | f̂(ξ)=∫f(x)e^(−2πix·ξ)dx，‖f̂‖₂=‖f‖₂ |
| 楔积 | α∧β(v,w)=α(v)β(w)−α(w)β(v) |
| 外微分 | d(Σa_I dx^I)=Σda_I∧dx^I；d²=0 |
| 体积元 | dV=√|det g| dx¹∧…∧dxᵐ |
| 斯托克斯 | ∫_∂M ω = ∫_M dω |
| 球面面积 | 4πR² |
| 球体积 | 4πR³/3 |

## 常用推理链

1. 覆盖 → 外测度 → 卡拉泰奥多里 → 测度 → 可测函数 → 积分。
2. 简单函数 → 单调收敛 → 一般积分 → L1 完备化 → Lp。
3. 度量 → 格拉姆矩阵 → 体积元 → m-形式积分 → 斯托克斯。
4. dω=0 → 闭；星形区域 → 恰当；有洞 → 积分非零（拓扑）。

## 反例清单

| 命题 | 反例 |
|---|---|
| 所有集合可测 | 维塔利集（需选择公理） |
| 外测度可加 | 一般覆盖重叠 |
| 测度 0 即有限 | 康托集 |
| 逐点收敛可交换积分 | nχ_{(0,1/n)} |
| 闭形式必恰当 | (xdy−ydx)/(x²+y²) |
| 连续曲线可求长 | t cos²(π/2t) |
"""

SKILL_MD = """---
name: 分析 III（点化学习总纲）
---

# 《分析 III》点化学习系统

## 这本书在讲什么

第三卷把分析从"平坦空间"搬到"弯曲空间"。先用卡拉泰奥多里的外测度路线建立测度与积分，得到勒贝格理论与三大收敛定理；再用多重线性代数造出微分形式，用外微分把"闭/恰当"变成代数条件；最后在流形上用体积元积分 m-形式，以斯托克斯定理收束全书。

## 全书心智模型

```mermaid
flowchart TB
  S[σ-代数] --> M[测度]
  M --> O[外测度 可测集]
  O --> L[勒贝格测度]
  L --> F[可测函数]
  F --> I[积分 L1 完备化]
  I --> C[收敛定理 Lp]
  I --> FB[富比尼 换元 卷积 傅里叶]
  V[多重线性代数] --> DF[微分形式 d]
  DF --> G[流形 度量 体积元]
  G --> MI[流形积分]
  MI --> ST[斯托克斯定理]
  FB --> ST
```

## 学习路径（推荐顺序）

| 步骤 | 章节 | 主题 | 前置 | 检查点 |
|---|---|---|---|---|
| 09 | ch09 | σ-代数、测度、外测度 | 分析 I 第 2–3 章 | ch09 自测三题 |
| 10 | ch10 | 可测函数、积分、收敛定理 | ch09 | ch10 自测三题 |
| 11 | ch11 | 流形、形式、度量 | 分析 II 第 7–8 章 | ch11 自测三题 |
| 12 | ch12 | 体积元、形式积分、斯托克斯 | ch09–ch11 | ch12 自测三题 |

## 章节索引

- 第 9 章 测度论基础（难度 ★★★）→ chapters/ch09-measure.md
- 第 10 章 积分理论（难度 ★★★）→ chapters/ch10-integration-theory.md
- 第 11 章 流形与微分形式（难度 ★★★）→ chapters/ch11-manifolds-forms.md
- 第 12 章 流形上的积分（难度 ★★★）→ chapters/ch12-manifold-integration.md

## 前置知识（零基础缺口补讲）

| 缺口 | 对应补讲位置 | 学完标志 |
|---|---|---|
| 没接触过测度 | ch09 概念 1、概念 2 | 能写出 σ-代数三条公理 |
| 不理解"几乎处处" | ch10 概念 1 | 能解释零测集为何不影响积分 |
| 不熟悉多重线性代数 | ch11 概念 2 | 能算 dx∧dy 在两组向量上的值 |
| 不会算曲面面积 | ch12 概念 2 | 能独立算出球面面积 |

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
    out = ["# 《分析 III》测验\n"]
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
    out.append("在 ℝ² 去掉原点的区域上，验证 ω=(xdy−ydx)/(x²+y²) 闭而不恰当；说明斯托克斯定理在该区域为何不能给出「积分为 0」的结论；并解释这个非零积分与复分析留数的关系。评分要点：闭性计算、单连通性讨论、绕圈积分值、拓扑解释。\n")
    return "".join(out)


def render_cards_md():
    out = ["# 《分析 III》抽认卡\n"]
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
        "slug": "analysis-iii",
        "title": "分析 III",
        "subtitle": "测度、勒贝格积分与流形上的斯托克斯定理",
        "book": {
            "title": "分析 III（Analysis III）",
            "author": "Herbert Amann / Joachim Escher",
            "source": ["分析 III (Herbert Amann  Joachim Escher) (z-library.sk, 1lib.sk, z-lib.sk).pdf"],
        },
        "audience": "已读完《分析 I》《分析 II》或具备同等基础",
        "goal": "掌握测度论、勒贝格积分、微分形式与流形积分",
        "learningPath": [
            {"step": "09", "title": "测度论基础", "chapterIds": ["ch09"], "checkpoint": "ch09 自测三题"},
            {"step": "10", "title": "积分理论", "chapterIds": ["ch10"], "checkpoint": "ch10 自测三题"},
            {"step": "11", "title": "流形与微分形式", "chapterIds": ["ch11"], "checkpoint": "ch11 自测三题"},
            {"step": "12", "title": "流形上的积分", "chapterIds": ["ch12"], "checkpoint": "ch12 自测三题"},
        ],
        "chapters": [{"id": c[0], "title": c[1], "file": c[2], "difficulty": c[3]} for c in CHAPTERS],
        "concepts": [{"id": c[0], "title": c[1], "file": c[2], "chapterIds": c[3]} for c in CONCEPTS],
        "glossary": [{"term": g[0], "def": g[1], "chapterId": g[2]} for g in GLOSSARY],
        "patterns": {"file": "patterns.md"},
        "cheatsheet": {"file": "cheatsheet.md"},
        "quizzes": QUIZZES,
        "flashcards": cards,
        "companion": "analysis-iii学习伴侣.html",
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
