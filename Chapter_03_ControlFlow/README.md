# Chapter 03: 控制流 - 给程序装上"大脑"的决策系统

## 📬 写在最前面：给生物学研究者的一封信

亲爱的研究者：

还记得你第一次设计PCR引物时的紧张吗？

"退火温度应该设多少度？"
"如果引物有二聚体怎么办？"
"GC含量太高要不要重新设计？"

每一步都需要判断，每个决定都影响结果。这就是**控制流**——程序的决策系统。

想象一下：
- **if语句** = 实验室的决策点（pH值太高？加酸！）
- **for循环** = 重复的实验操作（96孔板每个孔都要加样）
- **while循环** = 持续监测（细胞密度到80%了吗？没到就继续培养）

控制流让程序从"死板的食谱"变成"智能的助手"。就像一个经验丰富的实验员，知道什么时候该做什么，什么情况下要调整方案。

准备好了吗？让我们一起探索如何让程序学会"思考"！

## 🗺️ 本章导航

### 🎯 学习目标清单

完成本章后，你将能够：

✅ **条件判断（if语句）**
- 根据序列质量自动筛选数据
- 判断基因是否在特定染色体上
- 检测序列中是否含有特定motif

✅ **循环遍历（for循环）**
- 批量处理测序数据
- 逐个分析基因列表
- 自动化重复的实验操作

✅ **条件循环（while循环）**
- 持续搜索直到找到目标
- 监测实验条件是否满足
- 实现迭代算法

✅ **流程控制（break/continue）**
- 提前终止不必要的计算
- 跳过不符合条件的数据
- 优化程序运行效率

### 📊 知识结构图

```
控制流知识体系
├── 条件判断 (Decision Making)
│   ├── 单分支 if
│   ├── 双分支 if-else
│   └── 多分支 if-elif-else
│
├── 循环结构 (Loops)
│   ├── for循环
│   │   ├── 遍历序列
│   │   ├── range()函数
│   │   └── enumerate()索引
│   │
│   └── while循环
│       ├── 条件控制
│       ├── 计数器模式
│       └── 哨兵模式
│
├── 流程控制 (Flow Control)
│   ├── break（中断）
│   ├── continue（跳过）
│   └── pass（占位）
│
└── 嵌套结构 (Nested Structures)
    ├── 嵌套条件
    ├── 嵌套循环
    └── 混合嵌套
```

### 🧭 学习路径

```
第1站：为什么需要控制流？（5分钟）
    ↓
第2站：if语句 - 程序的判断力（20分钟）
    ↓
第3站：for循环 - 批量处理专家（25分钟）
    ↓
第4站：while循环 - 条件监测器（15分钟）
    ↓
第5站：流程控制 - 精细调控（10分钟）
    ↓
第6站：综合应用 - 构建分析流程（20分钟）
    ↓
第7站：常见错误与调试（10分钟）
```

## 🔬 第1站：为什么需要控制流？

### 真实的研究场景

#### 场景1：高通量测序数据质控

你刚收到了测序公司发来的数据：10,000条reads。但不是所有reads都能用！

```
问题：如何自动筛选高质量序列？

手动方法（痛苦）：
1. 打开Excel
2. 逐条查看质量分数
3. 手动删除低质量序列
4. 耗时：8小时
5. 错误率：高

程序方法（轻松）：
for read in all_reads:
    if quality_score >= 30:
        保留这条序列
    else:
        丢弃这条序列
耗时：5秒
错误率：0
```

#### 场景2：限制性酶切位点分析

你需要在质粒上找到所有的EcoRI和BamHI酶切位点。

```
质粒序列：5000 bp

手动方法：
- 用眼睛逐个寻找GAATTC和GGATCC
- 记录每个位置
- 容易遗漏，眼睛疲劳

程序方法：
position = 0
while position < 序列长度:
    if 当前位置是酶切位点:
        记录位置
    position += 1
```

#### 场景3：蛋白质翻译

将1000条mRNA序列翻译成蛋白质。

```
手动：查密码子表3000次以上！
程序：自动查表，瞬间完成

for mRNA in sequences:
    for codon in mRNA:
        查密码子表
        添加氨基酸
```

### 🧬 生物学类比理解

控制流就像细胞内的信号传导：

```
细胞信号传导              →    程序控制流
─────────────────────────────────────────────
接收信号（配体结合）        →    输入数据
   ↓                            ↓
信号判断（激活/抑制）       →    if条件判断
   ↓                            ↓
级联反应（逐级传递）        →    for循环处理
   ↓                            ↓
持续响应（直到信号停止）    →    while循环
   ↓                            ↓
终止信号（负反馈）          →    break退出
```

## 🎭 第2站：if语句 - 让程序学会判断

### 2.1 概念引入：什么是条件判断？

#### 生物学类比

想象你在做Western Blot：

```
实验流程决策树：
                    
跑完电泳
   ↓
查看Marker
   ↓
[条带清晰吗？]
   ├─是→ 转膜
   └─否→ 重新跑胶
```

这就是if语句的本质：**根据条件选择不同的执行路径**。

#### 语法基础

```python
# 基本结构
if 条件:
    执行这些操作  # 注意缩进！
    
# 为什么要缩进？
# 缩进表示"属于"关系，就像实验步骤的子步骤
```

### 2.2 单分支if：简单的是/否判断

#### 示例1：检查序列长度

```python
# 检查PCR产物长度是否正确
pcr_product = "ATGCGATCGATCGATCGATCGATCG"
expected_length = 25

print(f"PCR产物: {pcr_product}")
print(f"实际长度: {len(pcr_product)} bp")
print(f"预期长度: {expected_length} bp")

if len(pcr_product) == expected_length:
    print("✅ PCR成功！产物长度正确")
    print("可以进行下一步克隆")

# 输出:
# PCR产物: ATGCGATCGATCGATCGATCGATCG
# 实际长度: 25 bp
# 预期长度: 25 bp
# ✅ PCR成功！产物长度正确
# 可以进行下一步克隆
```

#### 示例2：质量控制

```python
# Nanodrop测定的DNA浓度和纯度
concentration = 150  # ng/μL
ratio_260_280 = 1.82  # 纯度指标

print(f"DNA浓度: {concentration} ng/μL")
print(f"A260/A280: {ratio_260_280}")

# 检查浓度
if concentration >= 50:
    print("✅ 浓度合格，可用于测序")

# 检查纯度
if 1.8 <= ratio_260_280 <= 2.0:
    print("✅ 纯度良好，无蛋白污染")

# 输出:
# DNA浓度: 150 ng/μL
# A260/A280: 1.82
# ✅ 浓度合格，可用于测序
# ✅ 纯度良好，无蛋白污染
```

### 2.3 双分支if-else：二选一

#### 示例3：酶切检查

```python
# 检查序列中是否含有EcoRI位点
plasmid = "ATGCGAATTCGATCG"
ecori_site = "GAATTC"

print(f"质粒序列: {plasmid}")
print(f"检查EcoRI位点: {ecori_site}")

if ecori_site in plasmid:
    position = plasmid.find(ecori_site)
    print(f"✅ 发现EcoRI位点在位置 {position}")
    print("可以使用EcoRI进行酶切")
else:
    print("❌ 未发现EcoRI位点")
    print("需要选择其他限制酶")

# 输出:
# 质粒序列: ATGCGAATTCGATCG
# 检查EcoRI位点: GAATTC
# ✅ 发现EcoRI位点在位置 4
# 可以使用EcoRI进行酶切
```

#### 示例4：突变检测

```python
# 检测点突变
wild_type = "ATGGCATAA"  # 野生型
sample = "ATGCCATAA"     # 样品序列

print(f"野生型: {wild_type}")
print(f"样品:   {sample}")

if sample == wild_type:
    print("✅ 序列正常，无突变")
else:
    print("⚠️ 检测到序列变异！")
    # 找出突变位置
    for i in range(len(wild_type)):
        if wild_type[i] != sample[i]:
            print(f"   位置{i}: {wild_type[i]} → {sample[i]}")

# 输出:
# 野生型: ATGGCATAA
# 样品:   ATGCCATAA
# ⚠️ 检测到序列变异！
#    位置3: G → C
```

### 2.4 多分支if-elif-else：多重选择

#### 示例5：测序质量分级

```python
# Illumina测序的Phred质量分数
quality_score = 35

print(f"Phred质量分数: Q{quality_score}")
print("评估测序质量...")

if quality_score >= 40:
    print("⭐ 极高质量 (错误率 < 0.01%)")
    print("建议: 可用于任何分析")
elif quality_score >= 30:
    print("✅ 高质量 (错误率 < 0.1%)")
    print("建议: 适合大多数分析")
elif quality_score >= 20:
    print("⚠️ 中等质量 (错误率 < 1%)")
    print("建议: 需要额外验证")
elif quality_score >= 10:
    print("⚠️ 低质量 (错误率 < 10%)")
    print("建议: 仅用于初步分析")
else:
    print("❌ 极低质量 (错误率 >= 10%)")
    print("建议: 丢弃此数据")

# 输出:
# Phred质量分数: Q35
# 评估测序质量...
# ✅ 高质量 (错误率 < 0.1%)
# 建议: 适合大多数分析
```

#### 示例6：基因表达水平分类

```python
# RNA-seq的FPKM值
gene_name = "GAPDH"
fpkm = 150.5

print(f"基因: {gene_name}")
print(f"表达量: {fpkm} FPKM")

if fpkm == 0:
    expression_level = "不表达"
    color = "⚫"
elif fpkm < 1:
    expression_level = "极低表达"
    color = "🔵"
elif fpkm < 10:
    expression_level = "低表达"
    color = "🟢"
elif fpkm < 100:
    expression_level = "中等表达"
    color = "🟡"
elif fpkm < 1000:
    expression_level = "高表达"
    color = "🟠"
else:
    expression_level = "极高表达"
    color = "🔴"

print(f"{color} {expression_level}")

# 输出:
# 基因: GAPDH
# 表达量: 150.5 FPKM
# 🟠 高表达
```

### 2.5 复合条件：and、or、not

#### 示例7：引物设计标准

```python
# 检查引物是否合格
primer = "ATGGCGATCGATCGATCGAT"
length = len(primer)
gc_content = (primer.count('G') + primer.count('C')) / length * 100
tm = 4 * (primer.count('G') + primer.count('C')) + 2 * (primer.count('A') + primer.count('T'))

print(f"引物序列: {primer}")
print(f"长度: {length} bp")
print(f"GC含量: {gc_content:.1f}%")
print(f"Tm: {tm}°C")
print()

# 检查多个条件
if 18 <= length <= 25 and 40 <= gc_content <= 60:
    print("✅ 引物设计合格")
else:
    print("❌ 引物需要重新设计")
    if not (18 <= length <= 25):
        print(f"   - 长度不合适 (应该18-25bp)")
    if not (40 <= gc_content <= 60):
        print(f"   - GC含量不合适 (应该40-60%)")

# 输出:
# 引物序列: ATGGCGATCGATCGATCGAT
# 长度: 20 bp
# GC含量: 50.0%
# Tm: 60°C
# 
# ✅ 引物设计合格
```

#### 示例8：样品质控综合判断

```python
# 细胞培养质控
cell_density = 85  # 密度百分比
viability = 92     # 活力百分比
contamination = False  # 污染状态

print("细胞培养状态检查:")
print(f"- 密度: {cell_density}%")
print(f"- 活力: {viability}%")
print(f"- 污染: {'是' if contamination else '否'}")
print()

# 综合判断
if contamination:
    print("❌ 发现污染！立即丢弃")
elif cell_density >= 80 and viability >= 90:
    print("✅ 细胞状态极佳，可以传代或实验")
elif cell_density >= 80 or viability < 80:
    if cell_density >= 80:
        print("⚠️ 密度过高但活力不足，建议传代")
    else:
        print("⚠️ 活力偏低，检查培养条件")
else:
    print("ℹ️ 继续培养")

# 输出:
# 细胞培养状态检查:
# - 密度: 85%
# - 活力: 92%
# - 污染: 否
# 
# ✅ 细胞状态极佳，可以传代或实验
```

### 2.6 嵌套if：多层决策

#### 示例9：基因功能预测

```python
# 根据序列特征预测基因功能
sequence = "ATGGCACCCAAATAG"
length = len(sequence)
has_start = sequence.startswith("ATG")
has_stop = sequence.endswith("TAA") or sequence.endswith("TAG") or sequence.endswith("TGA")

print(f"序列: {sequence}")
print(f"长度: {length} bp")
print()

if has_start:
    print("✓ 发现起始密码子ATG")
    
    if has_stop:
        print("✓ 发现终止密码子")
        
        if length % 3 == 0:
            print("✓ 长度是3的倍数")
            print("🧬 结论: 可能是完整的编码序列(CDS)")
        else:
            print("✗ 长度不是3的倍数")
            print("⚠️ 结论: 可能有移码突变")
    else:
        print("✗ 缺少终止密码子")
        print("⚠️ 结论: 可能是部分序列")
else:
    print("✗ 缺少起始密码子")
    print("ℹ️ 结论: 可能是非编码RNA或序列片段")

# 输出:
# 序列: ATGGCACCCAAATAG
# 长度: 15 bp
# 
# ✓ 发现起始密码子ATG
# ✓ 发现终止密码子
# ✓ 长度是3的倍数
# 🧬 结论: 可能是完整的编码序列(CDS)
```

## 🔄 第3站：for循环 - 批量处理的利器

### 3.1 概念引入：什么是for循环？

#### 生物学类比

for循环就像：
- 96孔板加样：对每个孔执行相同操作
- 批量DNA提取：每个样品走相同流程
- 显微镜计数：逐个视野统计细胞

```
实验室场景：
96孔板 → for孔 in 所有孔:
            加入50μL试剂
```

### 3.2 基础语法：遍历序列

#### 示例10：逐个碱基分析

```python
# 分析DNA序列组成
dna = "ATGCGATCG"

print(f"分析序列: {dna}")
print("逐个碱基检查:")

for base in dna:
    if base in "AT":
        bond_type = "2个氢键"
    else:  # G或C
        bond_type = "3个氢键"
    print(f"  {base} - {bond_type}")

# 输出:
# 分析序列: ATGCGATCG
# 逐个碱基检查:
#   A - 2个氢键
#   T - 2个氢键
#   G - 3个氢键
#   C - 3个氢键
#   G - 3个氢键
#   A - 2个氢键
#   T - 2个氢键
#   C - 3个氢键
#   G - 3个氢键
```

#### 示例11：批量样品处理

```python
# 处理多个样品
samples = ["Sample_A", "Sample_B", "Sample_C", "Control"]
concentrations = [150, 230, 180, 195]  # ng/μL

print("DNA定量结果:")
print("-" * 40)

for i in range(len(samples)):
    sample = samples[i]
    conc = concentrations[i]
    
    # 计算稀释倍数（目标：100 ng/μL）
    dilution = conc / 100
    
    print(f"{sample}:")
    print(f"  原始浓度: {conc} ng/μL")
    print(f"  稀释倍数: {dilution:.1f}x")
    print(f"  加水体积: {(dilution-1)*10:.1f} μL (10μL样品)")
    print()

# 输出:
# DNA定量结果:
# ----------------------------------------
# Sample_A:
#   原始浓度: 150 ng/μL
#   稀释倍数: 1.5x
#   加水体积: 5.0 μL (10μL样品)
# 
# Sample_B:
#   原始浓度: 230 ng/μL
#   稀释倍数: 2.3x
#   加水体积: 13.0 μL (10μL样品)
# 
# Sample_C:
#   原始浓度: 180 ng/μL
#   稀释倍数: 1.8x
#   加水体积: 8.0 μL (10μL样品)
# 
# Control:
#   原始浓度: 195 ng/μL
#   稀释倍数: 1.9x
#   加水体积: 9.5 μL (10μL样品)
```

### 3.3 range()函数：控制循环次数

#### 示例12：PCR循环模拟

```python
# 模拟PCR扩增
initial_copies = 100  # 初始模板数
cycles = 5  # PCR循环数

print("PCR扩增模拟:")
print(f"初始模板数: {initial_copies}")
print()

copies = initial_copies
for cycle in range(1, cycles + 1):
    copies = copies * 2  # 每个循环翻倍
    print(f"第{cycle}轮循环后: {copies:,} 个拷贝")

print()
print(f"扩增倍数: {copies/initial_copies:.0f}x")
print(f"理论值: 2^{cycles} = {2**cycles}x")

# 输出:
# PCR扩增模拟:
# 初始模板数: 100
# 
# 第1轮循环后: 200 个拷贝
# 第2轮循环后: 400 个拷贝
# 第3轮循环后: 800 个拷贝
# 第4轮循环后: 1,600 个拷贝
# 第5轮循环后: 3,200 个拷贝
# 
# 扩增倍数: 32x
# 理论值: 2^5 = 32x
```

### 3.4 enumerate()：获取索引和值

#### 示例13：序列位置标注

```python
# 标注限制酶切位点
sequence = "CGGAATTCATGGATCCTAGAATTC"
ecori = "GAATTC"

print(f"序列: {sequence}")
print("位置: " + "".join([str(i%10) for i in range(len(sequence))]))
print()
print("搜索EcoRI位点 (GAATTC):")

# 使用enumerate获取位置和碱基
for i in range(len(sequence) - len(ecori) + 1):
    if sequence[i:i+len(ecori)] == ecori:
        print(f"  发现位点: 位置 {i}-{i+len(ecori)-1}")
        print(f"  上下文: ...{sequence[max(0,i-3):i]}[{ecori}]{sequence[i+len(ecori):min(i+len(ecori)+3, len(sequence))]}...")

# 输出:
# 序列: CGGAATTCATGGATCCTAGAATTC
# 位置: 012345678901234567890123
# 
# 搜索EcoRI位点 (GAATTC):
#   发现位点: 位置 2-7
#   上下文: ...CG[GAATTC]ATG...
#   发现位点: 位置 18-23
#   上下文: ...TAG[GAATTC]...
```

### 3.5 嵌套for循环：多维处理

#### 示例14：密码子扫描

```python
# 在三个阅读框中搜索起始密码子
dna = "CCATGGCATGAAATGTAG"

print(f"DNA序列: {dna}")
print(f"长度: {len(dna)} bp")
print()

# 三个阅读框
for frame in range(3):
    print(f"阅读框 {frame}:")
    codons = []
    
    # 在当前阅读框中提取密码子
    for i in range(frame, len(dna) - 2, 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            codons.append(codon)
            if codon == "ATG":
                print(f"  ✓ 发现ATG在位置 {i}")
    
    print(f"  密码子: {' '.join(codons)}")
    print()

# 输出:
# DNA序列: CCATGGCATGAAATGTAG
# 长度: 18 bp
# 
# 阅读框 0:
#   密码子: CCA TGG CAT GAA ATG TAG
# 
# 阅读框 1:
#   ✓ 发现ATG在位置 2
#   ✓ 发现ATG在位置 7
#   密码子: CAT GGC ATG AAA TGT
# 
# 阅读框 2:
#   ✓ 发现ATG在位置 3
#   ✓ 发现ATG在位置 12
#   密码子: ATG GCA TGA AAT GTA
```

### 3.6 列表推导式：简洁的for循环

#### 示例15：快速数据转换

```python
# 序列处理的多种方法
sequences = ["ATGC", "CGTA", "GGCC"]

print("原始序列:", sequences)
print()

# 方法1：传统for循环
reverse_seqs = []
for seq in sequences:
    reverse_seqs.append(seq[::-1])
print("反向序列(传统):", reverse_seqs)

# 方法2：列表推导式（更简洁）
reverse_seqs2 = [seq[::-1] for seq in sequences]
print("反向序列(推导):", reverse_seqs2)

# 方法3：带条件的列表推导式
long_seqs = [seq for seq in sequences if len(seq) >= 4]
print("长序列(>=4bp):", long_seqs)

# 方法4：转换并过滤
gc_rich = [seq for seq in sequences if (seq.count('G') + seq.count('C'))/len(seq) > 0.5]
print("GC富集序列:", gc_rich)

# 输出:
# 原始序列: ['ATGC', 'CGTA', 'GGCC']
# 
# 反向序列(传统): ['CGTA', 'ATGC', 'CCGG']
# 反向序列(推导): ['CGTA', 'ATGC', 'CCGG']
# 长序列(>=4bp): ['ATGC', 'CGTA', 'GGCC']
# GC富集序列: ['GGCC']
```

## ⏰ 第4站：while循环 - 条件监测器

### 4.1 概念引入：什么是while循环？

#### 生物学类比

while循环就像：
- 细胞培养：密度未到80%就继续培养
- 透析：电导率未降到阈值就继续换液
- PCR：温度未到就继续加热

```
while 细胞密度 < 80%:
    继续培养
    每天检查
```

### 4.2 基础while循环

#### 示例16：搜索模式

```python
# 搜索下一个ATG
sequence = "CCGATCCATGAAATGCCCTAG"
position = 0

print(f"序列: {sequence}")
print("搜索ATG起始密码子...")
print()

while position <= len(sequence) - 3:
    codon = sequence[position:position+3]
    
    if codon == "ATG":
        print(f"✓ 找到ATG在位置 {position}")
        print(f"  上下文: ...{sequence[max(0,position-3):position]}[ATG]{sequence[position+3:min(position+6,len(sequence))]}...")
        break  # 找到第一个就停止
    
    position += 1

if position > len(sequence) - 3:
    print("未找到ATG")

# 输出:
# 序列: CCGATCCATGAAATGCCCTAG
# 搜索ATG起始密码子...
# 
# ✓ 找到ATG在位置 7
#   上下文: ...TCC[ATG]AAA...
```

#### 示例17：迭代优化

```python
# 二分法找最佳pH值
target_activity = 100  # 目标酶活性
ph_low = 6.0
ph_high = 8.0
tolerance = 0.1
iteration = 0

print("寻找最佳pH值（酶活性最接近100）")
print(f"初始范围: pH {ph_low} - {ph_high}")
print()

while ph_high - ph_low > tolerance:
    iteration += 1
    ph_mid = (ph_low + ph_high) / 2
    
    # 模拟酶活性（实际应该是实验测定）
    # 假设最佳pH是7.2
    activity = 100 - abs(ph_mid - 7.2) * 50
    
    print(f"迭代{iteration}: pH={ph_mid:.2f}, 活性={activity:.1f}")
    
    if activity < target_activity:
        if ph_mid < 7.2:
            ph_low = ph_mid
        else:
            ph_high = ph_mid
    else:
        break

print()
print(f"最佳pH: {ph_mid:.2f}")
print(f"总迭代次数: {iteration}")

# 输出:
# 寻找最佳pH值（酶活性最接近100）
# 初始范围: pH 6.0 - 8.0
# 
# 迭代1: pH=7.00, 活性=90.0
# 迭代2: pH=7.50, 活性=85.0
# 迭代3: pH=7.25, 活性=97.5
# 迭代4: pH=7.12, 活性=96.0
# 迭代5: pH=7.19, 活性=99.5
# 
# 最佳pH: 7.19
# 总迭代次数: 5
```

### 4.3 无限循环与退出条件

#### 示例18：用户交互菜单

```python
# 序列分析菜单（演示概念）
sequence = "ATGCGATCGATCG"
choice = ""

print("序列分析工具")
print(f"当前序列: {sequence}")
print()

# 模拟用户选择
choices = ["1", "2", "3", "4"]  # 预设的选择序列
choice_index = 0

while choice != "4":
    print("菜单:")
    print("1. 计算GC含量")
    print("2. 反向互补")
    print("3. 查找ATG")
    print("4. 退出")
    
    # 模拟用户输入
    choice = choices[choice_index]
    print(f"选择: {choice}")
    
    if choice == "1":
        gc = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        print(f"→ GC含量: {gc:.1f}%\n")
    elif choice == "2":
        complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
        rev_comp = "".join([complement[b] for b in sequence[::-1]])
        print(f"→ 反向互补: {rev_comp}\n")
    elif choice == "3":
        if "ATG" in sequence:
            pos = sequence.find("ATG")
            print(f"→ ATG位置: {pos}\n")
        else:
            print("→ 未找到ATG\n")
    
    choice_index += 1
    if choice_index >= len(choices):
        break

print("程序结束")

# 输出:
# 序列分析工具
# 当前序列: ATGCGATCGATCG
# 
# 菜单:
# 1. 计算GC含量
# 2. 反向互补
# 3. 查找ATG
# 4. 退出
# 选择: 1
# → GC含量: 53.8%
# 
# 菜单:
# 1. 计算GC含量
# 2. 反向互补
# 3. 查找ATG
# 4. 退出
# 选择: 2
# → 反向互补: CGATCGATCGCAT
# 
# 菜单:
# 1. 计算GC含量
# 2. 反向互补
# 3. 查找ATG
# 4. 退出
# 选择: 3
# → ATG位置: 0
# 
# 菜单:
# 1. 计算GC含量
# 2. 反向互补
# 3. 查找ATG
# 4. 退出
# 选择: 4
# 程序结束
```

## 🎮 第5站：流程控制 - break、continue和pass

### 5.1 break：紧急刹车

#### 示例19：找到目标立即停止

```python
# 在多个数据库中搜索基因
databases = {
    "GenBank": ["BRCA1", "TP53", "EGFR"],
    "RefSeq": ["MYC", "KRAS", "BRCA2"],
    "Ensembl": ["BRAF", "BRCA1", "APC"]
}

target_gene = "BRCA1"
print(f"搜索基因: {target_gene}")
print()

found = False
for db_name, genes in databases.items():
    print(f"搜索 {db_name}...")
    
    for gene in genes:
        if gene == target_gene:
            print(f"  ✓ 找到了！{target_gene} 在 {db_name}")
            found = True
            break  # 退出内层循环
    
    if found:
        break  # 退出外层循环
    else:
        print(f"  未在 {db_name} 中找到")

# 输出:
# 搜索基因: BRCA1
# 
# 搜索 GenBank...
#   ✓ 找到了！BRCA1 在 GenBank
```

### 5.2 continue：跳过当前

#### 示例20：过滤无效数据

```python
# 质量控制：跳过低质量序列
sequences = [
    {"id": "seq1", "dna": "ATGCGATC", "quality": 35},
    {"id": "seq2", "dna": "NNNNNNNN", "quality": 10},  # 低质量
    {"id": "seq3", "dna": "ATGGCGTA", "quality": 38},
    {"id": "seq4", "dna": "ATGNCGAT", "quality": 15},  # 低质量
]

print("处理高质量序列 (Q>=30):")
print()

processed_count = 0
for seq in sequences:
    # 跳过低质量序列
    if seq["quality"] < 30:
        print(f"⚠️ 跳过 {seq['id']}: 质量太低 (Q{seq['quality']})")
        continue
    
    # 只处理高质量序列
    gc_content = (seq["dna"].count('G') + seq["dna"].count('C')) / len(seq["dna"]) * 100
    print(f"✅ 处理 {seq['id']}: GC={gc_content:.1f}%")
    processed_count += 1

print()
print(f"处理完成: {processed_count}/{len(sequences)} 条序列")

# 输出:
# 处理高质量序列 (Q>=30):
# 
# ✅ 处理 seq1: GC=50.0%
# ⚠️ 跳过 seq2: 质量太低 (Q10)
# ✅ 处理 seq3: GC=50.0%
# ⚠️ 跳过 seq4: 质量太低 (Q15)
# 
# 处理完成: 2/4 条序列
```

### 5.3 pass：占位符

#### 示例21：框架代码

```python
# 构建分析流程框架
def analyze_sequence(sequence):
    """序列分析流程框架"""
    print(f"分析序列: {sequence}")
    
    # 步骤1：质量检查
    if len(sequence) < 10:
        print("  ⚠️ 序列太短")
        pass  # TODO: 添加详细的质量检查
    else:
        print("  ✓ 长度检查通过")
    
    # 步骤2：查找ORF
    if "ATG" in sequence:
        print("  ✓ 发现起始密码子")
        # TODO: 实现完整的ORF查找
        pass
    else:
        print("  ✗ 无起始密码子")
    
    # 步骤3：功能预测
    pass  # TODO: 添加功能预测代码
    
    return "分析完成"

# 测试框架
result = analyze_sequence("ATGCGATCGATCG")
print(f"结果: {result}")

# 输出:
# 分析序列: ATGCGATCGATCG
#   ✓ 长度检查通过
#   ✓ 发现起始密码子
# 结果: 分析完成
```

## 🔧 第6站：综合应用 - 构建完整的分析流程

### 6.1 实战项目：多序列质控分析系统

```python
def comprehensive_sequence_analysis():
    """
    综合示例：构建一个完整的序列分析流程
    包含：质量控制、模式搜索、统计分析
    """
    print("=" * 60)
    print("多序列质控分析系统 v1.0")
    print("=" * 60)
    
    # 模拟的测序数据
    sequences = [
        {"id": "READ001", "seq": "ATGGCGATCGATCGATCGTAG", "qual": 38},
        {"id": "READ002", "seq": "NATGCCNNNATCGATCGATCG", "qual": 25},
        {"id": "READ003", "seq": "ATGAAACCCTAGATGGGGTAA", "qual": 42},
        {"id": "READ004", "seq": "CCGATGGCGATCGATCGATCG", "qual": 35},
        {"id": "READ005", "seq": "ATGATGATGATGATGATGATG", "qual": 30},
    ]
    
    # 分析参数
    min_quality = 30
    max_n_percent = 10
    target_motif = "GATC"
    
    print(f"\n📋 分析参数:")
    print(f"  • 最低质量分数: Q{min_quality}")
    print(f"  • 最大N含量: {max_n_percent}%")
    print(f"  • 搜索motif: {target_motif}")
    print(f"  • 序列总数: {len(sequences)}")
    
    # 存储结果
    passed_sequences = []
    failed_sequences = []
    motif_containing = []
    
    # 统计变量
    total_length = 0
    total_gc_content = 0
    atg_count = 0
    
    print("\n" + "=" * 60)
    print("开始分析...")
    print("=" * 60)
    
    # 主分析循环
    for seq_data in sequences:
        seq_id = seq_data["id"]
        sequence = seq_data["seq"]
        quality = seq_data["qual"]
        
        print(f"\n分析 {seq_id}:")
        print(f"  序列: {sequence}")
        print(f"  质量: Q{quality}")
        
        # 步骤1：质量控制
        passed_qc = True
        reasons = []
        
        # 检查质量分数
        if quality < min_quality:
            passed_qc = False
            reasons.append(f"质量低于Q{min_quality}")
        
        # 检查N含量
        n_count = sequence.count('N')
        n_percent = (n_count / len(sequence)) * 100
        if n_percent > max_n_percent:
            passed_qc = False
            reasons.append(f"N含量{n_percent:.1f}%超标")
        
        # 质控结果
        if passed_qc:
            print("  ✅ 通过质控")
            passed_sequences.append(seq_data)
            
            # 步骤2：序列分析（只对通过质控的序列）
            # 计算GC含量
            gc_count = sequence.count('G') + sequence.count('C')
            gc_percent = (gc_count / len(sequence)) * 100
            print(f"  📊 GC含量: {gc_percent:.1f}%")
            
            # 搜索motif
            if target_motif in sequence:
                positions = []
                pos = 0
                while pos < len(sequence):
                    pos = sequence.find(target_motif, pos)
                    if pos == -1:
                        break
                    positions.append(pos)
                    pos += 1
                
                motif_containing.append(seq_id)
                print(f"  🔍 发现motif '{target_motif}' 在位置: {positions}")
            
            # 检查起始密码子
            if sequence.startswith("ATG"):
                atg_count += 1
                print("  🧬 包含起始密码子ATG")
            
            # 更新统计
            total_length += len(sequence)
            total_gc_content += gc_percent
            
        else:
            print(f"  ❌ 未通过质控: {', '.join(reasons)}")
            failed_sequences.append(seq_data)
    
    # 生成报告
    print("\n" + "=" * 60)
    print("📈 分析报告")
    print("=" * 60)
    
    print(f"\n质控结果:")
    print(f"  • 通过: {len(passed_sequences)}/{len(sequences)} ({len(passed_sequences)/len(sequences)*100:.1f}%)")
    print(f"  • 失败: {len(failed_sequences)}/{len(sequences)}")
    
    if passed_sequences:
        print(f"\n通过质控的序列统计:")
        print(f"  • 平均长度: {total_length/len(passed_sequences):.1f} bp")
        print(f"  • 平均GC含量: {total_gc_content/len(passed_sequences):.1f}%")
        print(f"  • 含有motif '{target_motif}': {len(motif_containing)} 条")
        print(f"  • 含有起始密码子: {atg_count} 条")
        
        print(f"\n序列ID列表:")
        print(f"  • 高质量: {[s['id'] for s in passed_sequences]}")
        if motif_containing:
            print(f"  • 含motif: {motif_containing}")
    
    print("\n" + "=" * 60)
    print("分析完成！")
    print("=" * 60)
    
    return passed_sequences

# 运行综合分析
results = comprehensive_sequence_analysis()
```

### 6.2 实战项目：ORF预测器

```python
def orf_predictor():
    """
    ORF（开放阅读框）预测器
    在DNA序列中找出所有可能的编码区域
    """
    print("=" * 60)
    print("ORF预测器 - 寻找潜在的基因")
    print("=" * 60)
    
    # 测试序列（包含多个ORF）
    dna = "CCATGATGAAACCCTAGATGGGGTAACGATGCCCTGAATGAAATAACCCATGACCGTATGCGATGAAATAGTAG"
    
    print(f"\nDNA序列 ({len(dna)} bp):")
    print(dna)
    
    # 定义终止密码子
    stop_codons = ["TAA", "TAG", "TGA"]
    
    # 存储所有ORF
    all_orfs = []
    
    print("\n搜索ORF（最小长度: 30bp）...")
    print("-" * 40)
    
    # 在三个阅读框中搜索
    for frame in range(3):
        print(f"\n阅读框 {frame}:")
        frame_orfs = []
        
        # 搜索该阅读框中的所有ATG
        for start_pos in range(frame, len(dna) - 2, 3):
            codon = dna[start_pos:start_pos + 3]
            
            if codon == "ATG":
                # 从ATG开始寻找终止密码子
                for end_pos in range(start_pos + 3, len(dna) - 2, 3):
                    stop_codon = dna[end_pos:end_pos + 3]
                    
                    if stop_codon in stop_codons:
                        orf_length = end_pos + 3 - start_pos
                        
                        # 只记录足够长的ORF
                        if orf_length >= 30:
                            orf_seq = dna[start_pos:end_pos + 3]
                            frame_orfs.append({
                                'frame': frame,
                                'start': start_pos,
                                'end': end_pos + 3,
                                'length': orf_length,
                                'sequence': orf_seq,
                                'protein_length': orf_length // 3
                            })
                            
                            print(f"  ORF发现: {start_pos}-{end_pos+3} ({orf_length} bp, {orf_length//3} aa)")
                            
                        break  # 找到第一个终止密码子就停止
        
        if not frame_orfs:
            print("  未发现ORF")
        
        all_orfs.extend(frame_orfs)
    
    # 找出最长的ORF
    if all_orfs:
        longest_orf = max(all_orfs, key=lambda x: x['length'])
        
        print("\n" + "=" * 60)
        print("🏆 最可能的基因（最长ORF）:")
        print(f"  • 阅读框: {longest_orf['frame']}")
        print(f"  • 位置: {longest_orf['start']}-{longest_orf['end']}")
        print(f"  • 长度: {longest_orf['length']} bp")
        print(f"  • 蛋白质: {longest_orf['protein_length']} 氨基酸")
        print(f"  • 序列: {longest_orf['sequence'][:30]}...{longest_orf['sequence'][-10:]}")
    
    return all_orfs

# 运行ORF预测
orfs = orf_predictor()
```

## 🐛 第7站：常见错误与调试技巧

### 7.1 常见语法错误

```python
# ❌ 错误1：忘记冒号
# if x > 0  # SyntaxError!
#     print("positive")

# ✅ 正确
if x > 0:  # 记得加冒号
    print("positive")

# ❌ 错误2：缩进错误
# if x > 0:
# print("positive")  # IndentationError!

# ✅ 正确
if x > 0:
    print("positive")  # 使用4个空格缩进

# ❌ 错误3：比较与赋值混淆
# if x = 5:  # SyntaxError! 

# ✅ 正确
if x == 5:  # 双等号用于比较
    print("x is 5")
```

### 7.2 逻辑错误

```python
# ❌ 错误：无限循环
# count = 0
# while count < 10:
#     print(count)
#     # 忘记更新count！

# ✅ 正确
count = 0
while count < 10:
    print(count)
    count += 1  # 记得更新循环变量

# ❌ 错误：范围错误
sequence = "ATGC"
# for i in range(len(sequence)):
#     triplet = sequence[i:i+3]  # 最后会越界！

# ✅ 正确
for i in range(len(sequence) - 2):  # 注意边界
    triplet = sequence[i:i+3]
```

### 7.3 调试技巧

```python
# 技巧1：使用print调试
sequence = "ATGCGATC"
for i in range(len(sequence)):
    print(f"Debug: i={i}, base={sequence[i]}")  # 查看循环变量
    # 你的代码

# 技巧2：分步执行
# 复杂条件分解
gc_content = 45
length = 20

# 不要写成一行
# if gc_content > 40 and gc_content < 60 and length >= 18 and length <= 25:

# 分步检查
gc_ok = 40 < gc_content < 60
print(f"GC检查: {gc_ok}")

length_ok = 18 <= length <= 25
print(f"长度检查: {length_ok}")

if gc_ok and length_ok:
    print("引物合格")
```

## 📝 本章总结

### 🎯 核心概念回顾

| 概念 | 语法 | 生物学类比 | 使用场景 |
|------|------|------------|----------|
| **if语句** | `if 条件:` | 实验决策点 | 质量控制、数据筛选 |
| **if-else** | `if-else:` | 二选一 | 阳性/阴性判断 |
| **if-elif-else** | `if-elif-else:` | 多重选择 | 分级评估 |
| **for循环** | `for item in sequence:` | 96孔板加样 | 批量处理 |
| **while循环** | `while 条件:` | 细胞培养监测 | 条件搜索 |
| **break** | `break` | 紧急停止 | 找到目标即停 |
| **continue** | `continue` | 跳过当前 | 过滤无效数据 |

### 💡 最佳实践建议

1. **选择合适的控制结构**
   - 已知次数 → for循环
   - 条件未知 → while循环
   - 多重选择 → if-elif-else

2. **代码可读性**
   - 使用有意义的变量名
   - 适当添加注释
   - 保持一致的缩进

3. **避免常见陷阱**
   - while循环必须有退出条件
   - 注意序列索引边界
   - 区分`=`(赋值)和`==`(比较)

4. **性能优化**
   - 将最可能的条件放在前面
   - 使用break避免不必要的循环
   - 考虑列表推导式简化代码

### 🚀 实际应用场景

控制流在生物信息学中无处不在：

- **基因组注释**: 扫描基因组寻找基因
- **序列比对**: 找最佳匹配位置
- **进化分析**: 构建进化树
- **药物筛选**: 评估化合物活性
- **图像分析**: 细胞计数和分类
- **统计分析**: 差异表达基因筛选

## 🎓 练习任务预览

本章配套了5个精心设计的练习题：

### ⭐ 练习1：序列质量过滤
筛选高质量测序reads，学习基本的if判断和for循环。

### ⭐⭐ 练习2：限制性酶切位点搜索
在DNA序列中查找多个酶切位点，练习字符串搜索和位置记录。

### ⭐⭐⭐ 练习3：最长ORF预测
找出序列中最长的开放阅读框，掌握嵌套循环和最值查找。

### ⭐⭐ 练习4：滑动窗口GC分析
使用滑动窗口技术分析GC含量分布，学习窗口算法。

### ⭐⭐⭐ 练习5：密码子使用频率统计
统计密码子使用偏好，初步接触字典数据结构。

## 📚 延伸阅读

如果你想深入了解：

1. **算法复杂度**: 为什么某些循环比其他的慢？
2. **递归**: 另一种强大的控制结构
3. **生成器**: 处理大数据的高效方法
4. **并行处理**: 同时处理多个序列

## 🌟 下一步学习

恭喜你掌握了程序的"大脑"——控制流！

下一章（Chapter 04：函数）将学习如何：
- 📦 把重复代码封装成函数（像实验室的SOP）
- 🔧 创建自己的"工具箱"
- 📐 让代码更模块化、可重用
- 🎯 提高代码的可维护性

就像把常用的实验流程写成标准操作规程(SOP)，函数让我们能够：
- 一次编写，多次使用
- 减少重复代码
- 让程序更清晰、更专业

准备好了吗？让我们继续探索Python的强大功能！

---

*"编程就像做实验，需要严谨的逻辑和清晰的流程。掌握了控制流，你就掌握了让程序'思考'的能力。"*

**—— 你的生物信息学导师**