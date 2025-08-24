# Chapter 04: 函数 - 实验室的标准操作流程(SOP)

## 📖 写在最前面 - 给生物学研究者的信

亲爱的同行：

还记得你第一次独立完成DNA提取的经历吗？一开始，你小心翼翼地对照着protocol，一步一步操作：加入裂解液、孵育、离心、转移上清、加入乙醇沉淀... 每一步都要查看说明书。但现在呢？这整个流程已经成为你的肌肉记忆，你甚至可以同时处理多个样品，因为你已经将这个复杂的过程内化为一个标准操作流程（SOP）。

**编程中的函数，就是你的数字化SOP。**

想象一下这个场景：你的实验室每天都要处理上百个样品的GC含量计算。如果每次都重新写计算步骤，不仅效率低下，还容易出错。但如果你创建了一个"calculate_gc_content"函数，就像制定了一个标准的GC含量测定SOP，任何时候需要计算GC含量，只需要"调用"这个SOP即可。

在这一章，我们将学习如何将重复的代码封装成函数，就像将重复的实验步骤标准化为SOP。你会发现，函数不仅让你的代码更简洁，更重要的是让你的分析流程可重复、可分享、可信赖。

让我们开始这段从"复制粘贴"到"模块化编程"的进化之旅！

## 🎯 本章导航 - 你的学习地图

### 📊 学习目标（完成本章后你将能够）

1. **理解函数的本质**
   - 为什么需要函数？（避免重复，提高效率）
   - 函数如何工作？（输入→处理→输出）
   - 什么时候创建函数？（识别重复模式）

2. **掌握函数的创建**
   - 定义简单函数（你的第一个SOP）
   - 设计函数参数（实验材料清单）
   - 处理返回值（实验产物）
   - 编写文档字符串（SOP说明书）

3. **理解作用域概念**
   - 局部变量 vs 全局变量（实验室内 vs 公共区域）
   - 参数传递机制（样品的传递方式）
   - 避免副作用（防止交叉污染）

4. **实践函数设计**
   - 单一职责原则（一个SOP只做一件事）
   - 参数设计最佳实践（必需品 vs 可选品）
   - 错误处理策略（异常情况应对）

5. **构建函数库**
   - 组合简单函数（流程整合）
   - 创建工具集（实验室工具箱）
   - 代码重构技巧（优化existing protocol）

### 🗺️ 知识结构图

```
函数编程
├── 为什么需要函数？
│   ├── 消除代码重复
│   ├── 提高可维护性
│   ├── 增强可读性
│   └── 促进代码复用
│
├── 函数基础
│   ├── 定义语法（def关键字）
│   ├── 函数命名（动词+名词）
│   ├── 函数体（缩进的代码块）
│   └── 函数调用（使用函数名）
│
├── 参数系统
│   ├── 位置参数（必需的输入）
│   ├── 默认参数（可选的输入）
│   ├── 关键字参数（明确指定）
│   └── 可变参数（*args, **kwargs）
│
├── 返回值
│   ├── 单一返回值
│   ├── 多值返回（元组）
│   ├── 结构化返回（字典）
│   └── None返回（无返回值）
│
├── 作用域
│   ├── 局部作用域（函数内部）
│   ├── 全局作用域（模块级别）
│   ├── 嵌套作用域（函数嵌套）
│   └── LEGB规则（查找顺序）
│
└── 最佳实践
    ├── 函数设计原则
    ├── 文档编写规范
    ├── 测试驱动开发
    └── 重构技巧
```

### 🎓 学习路径（建议的学习顺序）

```
第一步：理解必要性（30分钟）
  ↓ 通过实例理解为什么需要函数
第二步：创建第一个函数（45分钟）
  ↓ 动手写一个简单的GC含量计算器
第三步：掌握参数设计（60分钟）
  ↓ 学习如何设计灵活的函数接口
第四步：处理返回值（45分钟）
  ↓ 理解不同的返回值模式
第五步：理解作用域（30分钟）
  ↓ 避免变量冲突和副作用
第六步：实践重构（60分钟）
  ↓ 将现有代码重构为函数
第七步：构建工具库（90分钟）
  ↓ 创建自己的生物信息学函数库
第八步：综合项目（120分钟）
  ↓ 完成一个完整的序列分析项目
```

## 🔬 第一部分：为什么需要函数？

### 真实案例1：疯狂的复制粘贴

李博士正在分析100个基因的表达数据，她需要对每个基因进行相同的处理：
1. 计算平均表达量
2. 标准化处理
3. 判断是否差异表达

**没有函数的噩梦：**

```python
# 处理基因1
gene1_expression = [23.5, 24.1, 22.8, 23.9, 24.5]
gene1_mean = sum(gene1_expression) / len(gene1_expression)
gene1_std = ((sum((x - gene1_mean)**2 for x in gene1_expression) / len(gene1_expression))**0.5)
gene1_normalized = [(x - gene1_mean) / gene1_std for x in gene1_expression]
if abs(gene1_mean - 20) > 2:
    print("Gene1 is differentially expressed")

# 处理基因2（复制粘贴，修改变量名）
gene2_expression = [18.2, 17.9, 18.5, 19.1, 18.8]
gene2_mean = sum(gene2_expression) / len(gene2_expression)
gene2_std = ((sum((x - gene2_mean)**2 for x in gene2_expression) / len(gene2_expression))**0.5)
gene2_normalized = [(x - gene2_mean) / gene2_std for x in gene2_expression]
if abs(gene2_mean - 20) > 2:
    print("Gene2 is differentially expressed")

# 处理基因3（又复制粘贴...）
gene3_expression = [30.1, 29.8, 31.2, 30.5, 30.9]
gene3_mean = sum(gene3_expression) / len(gene3_expression)
gene3_std = ((sum((x - gene3_mean)**2 for x in gene3_expression) / len(gene3_expression))**0.5)
gene3_normalized = [(x - gene3_mean) / gene3_std for x in gene3_expression]
if abs(gene3_mean - 20) > 2:
    print("Gene3 is differentially expressed")

# ... 还有97个基因要处理 😱
```

**问题分析：**
- 代码重复100次，文件超过500行
- 修改分析方法需要改100个地方
- 极易出错（复制时忘记改变量名）
- 代码难以理解和维护
- 浪费大量时间

**使用函数的优雅解决方案：**

```python
def analyze_gene_expression(expression_data, gene_name, control_level=20, threshold=2):
    """
    分析基因表达数据的标准流程
    
    就像实验室的标准操作流程(SOP)：
    1. 计算平均值（相当于测定浓度）
    2. 计算标准差（评估数据质量）
    3. 数据标准化（像Western Blot的内参校正）
    4. 判断差异表达（统计学分析）
    
    参数：
        expression_data: 表达量数据列表
        gene_name: 基因名称
        control_level: 对照组表达水平
        threshold: 差异表达阈值
    
    返回：
        分析结果字典
    """
    # 步骤1：计算平均表达量
    mean_expression = sum(expression_data) / len(expression_data)
    
    # 步骤2：计算标准差
    variance = sum((x - mean_expression)**2 for x in expression_data) / len(expression_data)
    std_dev = variance ** 0.5
    
    # 步骤3：数据标准化
    if std_dev > 0:
        normalized = [(x - mean_expression) / std_dev for x in expression_data]
    else:
        normalized = [0] * len(expression_data)
    
    # 步骤4：判断是否差异表达
    is_differential = abs(mean_expression - control_level) > threshold
    
    # 返回完整的分析结果
    return {
        'gene': gene_name,
        'mean': mean_expression,
        'std': std_dev,
        'normalized': normalized,
        'is_differential': is_differential,
        'fold_change': mean_expression / control_level if control_level != 0 else None
    }

# 现在处理100个基因变得如此简单！
genes_data = {
    'Gene1': [23.5, 24.1, 22.8, 23.9, 24.5],
    'Gene2': [18.2, 17.9, 18.5, 19.1, 18.8],
    'Gene3': [30.1, 29.8, 31.2, 30.5, 30.9],
    # ... 更多基因数据
}

# 批量分析所有基因
results = []
for gene_name, expression in genes_data.items():
    result = analyze_gene_expression(expression, gene_name)
    results.append(result)
    
    # 打印分析结果
    if result['is_differential']:
        print(f"{gene_name}: 差异表达 (FC={result['fold_change']:.2f})")
    else:
        print(f"{gene_name}: 正常表达")

# 输出：
# Gene1: 差异表达 (FC=1.19)
# Gene2: 正常表达
# Gene3: 差异表达 (FC=1.52)
```

### 真实案例2：PCR引物设计

王同学需要为50个基因设计PCR引物，每个基因都需要：
1. 检查序列长度
2. 计算GC含量
3. 计算Tm值
4. 检查二级结构

**传统方法的问题：**

```python
# 不使用函数，每个引物都要重复这些计算
primer1 = "ATCGATCGATCGATCG"
# 检查长度
if len(primer1) < 18 or len(primer1) > 25:
    print("Primer1长度不合适")
# 计算GC含量
gc_count1 = primer1.count('G') + primer1.count('C')
gc_content1 = (gc_count1 / len(primer1)) * 100
# 计算Tm值（简化公式）
tm1 = 4 * (primer1.count('G') + primer1.count('C')) + 2 * (primer1.count('A') + primer1.count('T'))
# 检查是否有连续重复
has_repeat1 = 'AAAA' in primer1 or 'TTTT' in primer1 or 'GGGG' in primer1 or 'CCCC' in primer1

primer2 = "GCGCGCGCGCGCGC"
# 又要重复所有步骤...
```

**函数化的解决方案：**

```python
def evaluate_primer(sequence, gene_name=""):
    """
    评估PCR引物的质量
    
    这个函数就像一个引物质量检测的SOP：
    1. 长度检查（18-25 bp最佳）
    2. GC含量（40-60%最佳）
    3. Tm值计算（55-65°C最佳）
    4. 二级结构检查（避免发夹和二聚体）
    
    参数：
        sequence: 引物序列
        gene_name: 基因名称（可选）
    
    返回：
        评估报告字典
    """
    # 标准化序列
    sequence = sequence.upper()
    
    # 基础参数计算
    length = len(sequence)
    gc_count = sequence.count('G') + sequence.count('C')
    at_count = sequence.count('A') + sequence.count('T')
    gc_content = (gc_count / length) * 100 if length > 0 else 0
    
    # Tm值计算（Wallace规则，适用于短引物）
    if length < 14:
        tm = 2 * at_count + 4 * gc_count
    else:
        # 更精确的公式（Nearest Neighbor法简化版）
        tm = 64.9 + 41 * (gc_count - 16.4) / length
    
    # 质量评分系统
    score = 100  # 满分100
    warnings = []
    
    # 1. 长度评估
    if length < 18:
        score -= 20
        warnings.append(f"引物太短({length}bp)，建议18-25bp")
    elif length > 25:
        score -= 15
        warnings.append(f"引物太长({length}bp)，建议18-25bp")
    
    # 2. GC含量评估
    if gc_content < 40:
        score -= 15
        warnings.append(f"GC含量太低({gc_content:.1f}%)，建议40-60%")
    elif gc_content > 60:
        score -= 15
        warnings.append(f"GC含量太高({gc_content:.1f}%)，建议40-60%")
    
    # 3. Tm值评估
    if tm < 55:
        score -= 15
        warnings.append(f"Tm值太低({tm:.1f}°C)，建议55-65°C")
    elif tm > 65:
        score -= 10
        warnings.append(f"Tm值太高({tm:.1f}°C)，建议55-65°C")
    
    # 4. 检查连续重复碱基
    repeats = ['AAAA', 'TTTT', 'GGGG', 'CCCC']
    for repeat in repeats:
        if repeat in sequence:
            score -= 10
            warnings.append(f"包含连续重复{repeat}，可能形成二级结构")
    
    # 5. 检查3'端稳定性
    if sequence[-1] in ['G', 'C']:
        score += 5  # 3'端是G或C，有利于引物稳定
    
    # 生成评估报告
    report = {
        'gene': gene_name,
        'sequence': sequence,
        'length': length,
        'gc_content': gc_content,
        'tm': tm,
        'score': max(0, score),  # 确保分数不为负
        'quality': '优秀' if score >= 85 else '良好' if score >= 70 else '需要优化',
        'warnings': warnings if warnings else ['引物设计合理']
    }
    
    return report

def design_primer_pair(forward_seq, reverse_seq, gene_name=""):
    """
    评估引物对的兼容性
    
    不仅要单独评估每个引物，还要检查：
    1. Tm值差异（不超过5°C）
    2. 避免引物二聚体
    3. 产物长度预估
    """
    # 评估单个引物
    forward_report = evaluate_primer(forward_seq, f"{gene_name}_F")
    reverse_report = evaluate_primer(reverse_seq, f"{gene_name}_R")
    
    # 评估引物对兼容性
    tm_difference = abs(forward_report['tm'] - reverse_report['tm'])
    compatibility_score = 100
    compatibility_warnings = []
    
    if tm_difference > 5:
        compatibility_score -= 20
        compatibility_warnings.append(f"Tm值差异过大({tm_difference:.1f}°C)")
    
    # 检查3'端互补（可能形成引物二聚体）
    if forward_seq[-3:] == reverse_seq[-3:][::-1].replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper():
        compatibility_score -= 30
        compatibility_warnings.append("3'端可能形成引物二聚体")
    
    return {
        'forward': forward_report,
        'reverse': reverse_report,
        'compatibility_score': compatibility_score,
        'compatibility_warnings': compatibility_warnings,
        'overall_quality': '可用' if compatibility_score >= 70 else '需要重新设计'
    }

# 实际使用示例
print("="*60)
print("PCR引物设计评估系统")
print("="*60)

# 测试不同质量的引物
test_primers = [
    ("ATCGATCGATCGATCGATCG", "Good_primer"),
    ("GCGCGCGCGCGCGC", "High_GC"),
    ("ATATATATATAT", "Low_GC"),
    ("AAAATTTTGGGGCCCC", "Has_repeats"),
    ("ATCGATCGATCG", "Too_short")
]

for primer_seq, primer_name in test_primers:
    report = evaluate_primer(primer_seq, primer_name)
    print(f"\n引物: {primer_name}")
    print(f"序列: {primer_seq}")
    print(f"质量评分: {report['score']}/100 ({report['quality']})")
    print(f"Tm值: {report['tm']:.1f}°C")
    print(f"GC含量: {report['gc_content']:.1f}%")
    print("警告信息:")
    for warning in report['warnings']:
        print(f"  - {warning}")

# 评估引物对
print("\n" + "="*60)
print("引物对兼容性评估")
print("="*60)

forward = "ATCGATCGATCGATCG"
reverse = "GCTAGCTAGCTAGCTA"
pair_report = design_primer_pair(forward, reverse, "Test_gene")

print(f"正向引物: {forward} (Tm={pair_report['forward']['tm']:.1f}°C)")
print(f"反向引物: {reverse} (Tm={pair_report['reverse']['tm']:.1f}°C)")
print(f"兼容性评分: {pair_report['compatibility_score']}/100")
print(f"总体评价: {pair_report['overall_quality']}")
```

### 真实案例3：蛋白质序列分析流水线

张教授的实验室每天要分析大量的蛋白质序列，包括：
- 计算分子量
- 计算等电点
- 预测二级结构
- 查找功能域

**函数化的分析流水线：**

```python
def calculate_protein_mw(sequence):
    """
    计算蛋白质分子量
    
    使用平均分子量法计算
    """
    # 氨基酸平均分子量表（道尔顿）
    aa_weights = {
        'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1,
        'C': 121.2, 'E': 147.1, 'Q': 146.2, 'G': 75.1,
        'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2,
        'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1,
        'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1
    }
    
    # 计算总分子量
    mw = sum(aa_weights.get(aa, 0) for aa in sequence.upper())
    # 减去水分子（肽键形成）
    mw -= 18.015 * (len(sequence) - 1)
    
    return mw / 1000  # 转换为kDa

def calculate_protein_pi(sequence):
    """
    估算蛋白质等电点（pI）
    
    简化算法：基于酸性和碱性氨基酸的比例
    """
    sequence = sequence.upper()
    
    # 统计带电氨基酸
    acidic = sequence.count('D') + sequence.count('E')  # 天冬氨酸、谷氨酸
    basic = sequence.count('K') + sequence.count('R') + sequence.count('H')  # 赖氨酸、精氨酸、组氨酸
    
    # 简化的pI估算
    if acidic > basic:
        pi = 4.5 - (acidic - basic) * 0.1  # 偏酸性
    elif basic > acidic:
        pi = 9.5 + (basic - acidic) * 0.1  # 偏碱性
    else:
        pi = 7.0  # 中性
    
    # 限制在合理范围内
    return max(3.0, min(12.0, pi))

def predict_secondary_structure(sequence):
    """
    预测蛋白质二级结构倾向
    
    基于Chou-Fasman规则的简化版本
    """
    # 氨基酸的二级结构倾向性
    helix_formers = set('AELMQKRH')  # α螺旋倾向
    sheet_formers = set('YVWFTI')    # β折叠倾向
    turn_formers = set('GPSND')      # 转角倾向
    
    sequence = sequence.upper()
    length = len(sequence)
    
    if length == 0:
        return {'helix': 0, 'sheet': 0, 'turn': 0, 'coil': 0}
    
    # 统计各种结构倾向
    helix_count = sum(1 for aa in sequence if aa in helix_formers)
    sheet_count = sum(1 for aa in sequence if aa in sheet_formers)
    turn_count = sum(1 for aa in sequence if aa in turn_formers)
    
    # 计算百分比
    helix_percent = (helix_count / length) * 100
    sheet_percent = (sheet_count / length) * 100
    turn_percent = (turn_count / length) * 100
    coil_percent = 100 - (helix_percent + sheet_percent + turn_percent)
    
    return {
        'helix': helix_percent,
        'sheet': sheet_percent,
        'turn': turn_percent,
        'coil': max(0, coil_percent)
    }

def find_protein_motifs(sequence):
    """
    查找常见的蛋白质功能基序
    
    返回找到的基序及其位置
    """
    motifs = {
        'NLS': 'PKKKRKV',           # 核定位信号
        'NES': 'LXXXLXXLXL',        # 核输出信号
        'RGD': 'RGD',               # 整合素结合位点
        'KDEL': 'KDEL',             # 内质网滞留信号
        'Myristoylation': 'MGXXXS', # N-肉豆蔻酰化位点
        'PKC_site': '[ST]X[RK]',    # PKC磷酸化位点
    }
    
    found_motifs = []
    sequence = sequence.upper()
    
    # 简化的基序搜索
    for motif_name, pattern in motifs.items():
        if pattern.replace('X', '') in sequence:  # 简化匹配
            # 找到所有出现位置
            start = 0
            while True:
                pos = sequence.find(pattern.replace('X', ''), start)
                if pos == -1:
                    break
                found_motifs.append({
                    'motif': motif_name,
                    'pattern': pattern,
                    'position': pos + 1,  # 生物学中从1开始计数
                    'sequence': sequence[pos:pos+len(pattern)]
                })
                start = pos + 1
    
    return found_motifs

def analyze_protein_comprehensive(sequence, protein_name="Unknown"):
    """
    综合蛋白质分析流水线
    
    整合所有分析功能，生成完整报告
    """
    print(f"\n{'='*60}")
    print(f"蛋白质综合分析报告: {protein_name}")
    print(f"{'='*60}")
    
    # 基础信息
    length = len(sequence)
    print(f"\n基础信息:")
    print(f"  序列长度: {length} aa")
    
    # 分子量计算
    mw = calculate_protein_mw(sequence)
    print(f"  分子量: {mw:.2f} kDa")
    
    # 等电点预测
    pi = calculate_protein_pi(sequence)
    print(f"  等电点(pI): {pi:.1f}")
    
    # 氨基酸组成
    print(f"\n氨基酸组成:")
    aa_types = {
        '疏水性': 'AILMFVPW',
        '亲水性': 'STYNQC',
        '带正电': 'RKH',
        '带负电': 'DE',
        '芳香族': 'FWY'
    }
    
    for aa_type, aas in aa_types.items():
        count = sum(sequence.upper().count(aa) for aa in aas)
        percent = (count / length * 100) if length > 0 else 0
        print(f"  {aa_type}: {count} ({percent:.1f}%)")
    
    # 二级结构预测
    structure = predict_secondary_structure(sequence)
    print(f"\n二级结构预测:")
    print(f"  α-螺旋: {structure['helix']:.1f}%")
    print(f"  β-折叠: {structure['sheet']:.1f}%")
    print(f"  转角: {structure['turn']:.1f}%")
    print(f"  无规卷曲: {structure['coil']:.1f}%")
    
    # 功能基序
    motifs = find_protein_motifs(sequence)
    if motifs:
        print(f"\n发现的功能基序:")
        for motif in motifs:
            print(f"  - {motif['motif']} at position {motif['position']}")
    else:
        print(f"\n未发现已知功能基序")
    
    # 生成总结
    print(f"\n分析总结:")
    if mw < 20:
        print(f"  - 小分子蛋白质（{mw:.1f} kDa）")
    elif mw < 50:
        print(f"  - 中等大小蛋白质（{mw:.1f} kDa）")
    else:
        print(f"  - 大分子蛋白质（{mw:.1f} kDa）")
    
    if pi < 5.5:
        print(f"  - 酸性蛋白（pI={pi:.1f}）")
    elif pi > 8.5:
        print(f"  - 碱性蛋白（pI={pi:.1f}）")
    else:
        print(f"  - 中性蛋白（pI={pi:.1f}）")
    
    if structure['helix'] > 40:
        print(f"  - 富含α-螺旋结构")
    if structure['sheet'] > 40:
        print(f"  - 富含β-折叠结构")
    
    return {
        'name': protein_name,
        'length': length,
        'mw': mw,
        'pi': pi,
        'structure': structure,
        'motifs': motifs
    }

# 测试蛋白质分析流水线
test_proteins = {
    'Histone_H3': 'ARTKQTARKSTGGKAPRKQLATKAARKSAPATGGVKKPHRYRPGTVALRE',
    'Insulin_A': 'GIVEQCCTSICSLYQLENYCN',
    'Collagen': 'GPPGPPGPPGPPGPPGPPGPPGPPGPP'
}

for name, sequence in test_proteins.items():
    analyze_protein_comprehensive(sequence, name)
```

## 🧬 第二部分：函数的解剖学 - 深入理解函数结构

### 函数的完整结构解析

就像实验室的SOP有固定格式一样，Python函数也有标准结构：

```python
def function_name(required_param, optional_param=default_value):
    """
    函数文档字符串（Docstring）
    
    这部分就像SOP的说明部分：
    - 目的：这个函数做什么
    - 原理：如何实现功能
    - 参数：需要什么输入
    - 返回：产生什么输出
    - 注意事项：使用时的注意点
    
    Args:
        required_param: 必需参数的说明
        optional_param: 可选参数的说明（默认值）
    
    Returns:
        返回值的说明
    
    Examples:
        >>> function_name("input", optional_param=10)
        "expected output"
    """
    # 函数体：实际的操作步骤
    # 步骤1：输入验证（质控）
    if not required_param:
        raise ValueError("必需参数不能为空")
    
    # 步骤2：数据处理（实验操作）
    result = process_data(required_param, optional_param)
    
    # 步骤3：返回结果（实验产物）
    return result
```

### 深入理解：函数的每个组成部分

#### 1. def关键字 - 定义的开始

```python
# def = define（定义）
# 就像实验室说"现在我要制定一个新的SOP"

def extract_dna():  # 定义一个DNA提取的SOP
    pass
    
def pcr_amplification():  # 定义一个PCR扩增的SOP
    pass
    
def protein_purification():  # 定义一个蛋白纯化的SOP
    pass
```

#### 2. 函数名 - 清晰的标识

```python
# 好的函数名：动词 + 名词，清晰表达功能
# 就像SOP的标题要清晰明确

# ✅ 好的命名
def calculate_gc_content(sequence):
    """计算GC含量"""
    pass

def validate_sequence(sequence):
    """验证序列有效性"""
    pass

def translate_to_protein(dna_sequence):
    """将DNA翻译为蛋白质"""
    pass

# ❌ 不好的命名
def func1(s):  # 不知道做什么
    pass

def process(data):  # 太模糊
    pass

def gccccccc(seq):  # 无意义
    pass
```

#### 3. 参数列表 - 输入规范

```python
def advanced_pcr_setup(
    template_dna,                    # 必需：模板DNA
    forward_primer,                  # 必需：正向引物
    reverse_primer,                  # 必需：反向引物
    enzyme="Taq",                    # 可选：酶的类型（默认Taq）
    mg_concentration=1.5,            # 可选：Mg2+浓度（默认1.5mM）
    annealing_temp=55,              # 可选：退火温度（默认55°C）
    cycles=30,                      # 可选：循环数（默认30）
    extension_time=60               # 可选：延伸时间（默认60秒）
):
    """
    高级PCR反应设置
    
    参数设计原则：
    1. 必需参数在前（没有默认值的）
    2. 可选参数在后（有默认值的）
    3. 参数名要描述性强
    4. 默认值要合理
    """
    print(f"PCR反应配置:")
    print(f"  模板: {template_dna[:20]}...")
    print(f"  引物: F-{forward_primer}, R-{reverse_primer}")
    print(f"  酶: {enzyme}")
    print(f"  Mg2+: {mg_concentration}mM")
    print(f"  退火: {annealing_temp}°C")
    print(f"  循环: {cycles}次")
    print(f"  延伸: {extension_time}秒")
    
    # 实际的PCR程序
    program = {
        'initial_denaturation': (95, 300),  # 95°C, 5分钟
        'cycles': {
            'denaturation': (95, 30),       # 95°C, 30秒
            'annealing': (annealing_temp, 30),  # 退火
            'extension': (72, extension_time)   # 72°C延伸
        },
        'final_extension': (72, 420),       # 72°C, 7分钟
        'hold': (4, None)                   # 4°C保存
    }
    
    return program

# 使用示例：展示不同的调用方式
# 方式1：只提供必需参数（使用所有默认值）
program1 = advanced_pcr_setup(
    "ATCGATCGATCG",
    "ATCG",
    "CGAT"
)

# 方式2：修改部分默认值
program2 = advanced_pcr_setup(
    "ATCGATCGATCG",
    "ATCG",
    "CGAT",
    enzyme="Pfu",        # 使用高保真酶
    annealing_temp=58    # 提高退火温度
)

# 方式3：使用关键字参数（可以改变顺序）
program3 = advanced_pcr_setup(
    template_dna="ATCGATCGATCG",
    reverse_primer="CGAT",    # 顺序改变了
    forward_primer="ATCG",
    cycles=35                 # 增加循环数
)
```

#### 4. 文档字符串 - 使用说明书

```python
def comprehensive_sequence_analysis(sequence, analysis_type="all"):
    """
    综合序列分析函数
    
    详细说明：
        这个函数提供了全面的DNA/RNA序列分析功能，
        包括基础统计、结构预测、功能注释等。
        
    参数：
        sequence (str): 核酸序列，支持DNA和RNA
            - DNA序列：只包含ATCG
            - RNA序列：只包含AUCG
            - 支持大小写
            - 自动去除空白字符
            
        analysis_type (str): 分析类型，默认"all"
            - "basic": 基础统计（长度、GC含量）
            - "structure": 结构分析（发夹、二级结构）
            - "function": 功能预测（ORF、基序）
            - "all": 所有分析
    
    返回：
        dict: 分析结果字典，包含以下键：
            - sequence_type: "DNA"或"RNA"
            - length: 序列长度
            - gc_content: GC含量百分比
            - structures: 预测的结构列表（如果请求）
            - orfs: 开放阅读框列表（如果请求）
            - motifs: 功能基序列表（如果请求）
    
    异常：
        ValueError: 当序列包含无效字符时
        TypeError: 当输入不是字符串时
    
    示例：
        >>> result = comprehensive_sequence_analysis("ATCGATCG")
        >>> print(result['gc_content'])
        50.0
        
        >>> result = comprehensive_sequence_analysis(
        ...     "ATCGATCGATCG",
        ...     analysis_type="basic"
        ... )
        >>> print(result.keys())
        dict_keys(['sequence_type', 'length', 'gc_content'])
    
    注意事项：
        1. 长序列（>10000bp）可能需要较长计算时间
        2. 结构预测仅供参考，建议结合实验验证
        3. RNA序列会自动识别，无需特别指定
    
    参考文献：
        - Zuker, M. (2003) Mfold web server for nucleic acid folding
        - Lorenz, R. et al. (2011) ViennaRNA Package 2.0
    
    版本历史：
        v1.0 (2024-01-01): 初始版本
        v1.1 (2024-01-15): 添加RNA支持
        v1.2 (2024-02-01): 优化性能，添加并行处理
    
    作者：BioPython教学团队
    """
    # 函数实现...
    pass
```

#### 5. 函数体 - 具体实现

```python
def optimize_codon_usage(protein_sequence, organism="E.coli"):
    """
    密码子优化函数
    
    根据不同生物的密码子偏好性优化基因序列
    """
    # 步骤1：输入验证（质控检查）
    if not protein_sequence:
        raise ValueError("蛋白质序列不能为空")
    
    if not all(aa in "ACDEFGHIKLMNPQRSTVWY*" for aa in protein_sequence.upper()):
        raise ValueError("蛋白质序列包含无效氨基酸")
    
    # 步骤2：载入密码子表（准备试剂）
    codon_tables = {
        "E.coli": {
            'A': ['GCT', 'GCC'],  # 丙氨酸的优化密码子
            'R': ['CGT', 'CGC'],  # 精氨酸的优化密码子
            # ... 更多
        },
        "yeast": {
            'A': ['GCT', 'GCA'],
            'R': ['AGA', 'AGG'],
            # ... 更多
        }
    }
    
    if organism not in codon_tables:
        print(f"警告：未知生物{organism}，使用默认E.coli密码子表")
        organism = "E.coli"
    
    # 步骤3：密码子优化（核心反应）
    optimized_dna = ""
    codon_table = codon_tables[organism]
    
    for aa in protein_sequence.upper():
        if aa == '*':
            optimized_dna += 'TAA'  # 终止密码子
        elif aa in codon_table:
            # 随机选择一个优化的密码子
            import random
            optimized_dna += random.choice(codon_table[aa])
        else:
            # 使用通用密码子
            optimized_dna += 'NNN'
    
    # 步骤4：结果验证（产物检测）
    if len(optimized_dna) != len(protein_sequence) * 3:
        raise RuntimeError("密码子优化失败：长度不匹配")
    
    # 步骤5：返回结果（实验产物）
    return {
        'protein': protein_sequence,
        'optimized_dna': optimized_dna,
        'organism': organism,
        'gc_content': calculate_gc_content(optimized_dna),
        'length': len(optimized_dna)
    }
```

## 🔄 第三部分：参数传递机制 - 样品的传递方式

### 理解参数传递

在实验室中，我们传递样品有不同的方式：
- 直接传递试管（传值）
- 传递样品编号（传引用）
- 传递整个样品盒（传容器）

Python中的参数传递也有类似的概念：

```python
def demonstrate_parameter_passing():
    """
    演示Python的参数传递机制
    """
    print("="*60)
    print("参数传递机制演示")
    print("="*60)
    
    # 1. 不可变对象的传递（类似传递样品的复制品）
    def modify_number(x):
        """尝试修改数字（不可变对象）"""
        print(f"  函数内：收到x = {x}")
        x = x + 10
        print(f"  函数内：修改后x = {x}")
        return x
    
    original_number = 100
    print("\n1. 传递不可变对象（数字）:")
    print(f"原始值：{original_number}")
    result = modify_number(original_number)
    print(f"函数外：original_number = {original_number}")  # 不变
    print(f"函数返回值：{result}")
    
    # 2. 可变对象的传递（类似传递样品盒）
    def modify_list(sample_list):
        """修改列表（可变对象）"""
        print(f"  函数内：收到列表 = {sample_list}")
        sample_list.append("新样品")
        print(f"  函数内：修改后 = {sample_list}")
    
    original_list = ["样品1", "样品2", "样品3"]
    print("\n2. 传递可变对象（列表）:")
    print(f"原始列表：{original_list}")
    modify_list(original_list)
    print(f"函数外：original_list = {original_list}")  # 被修改了！
    
    # 3. 如何避免意外修改
    def safe_modify_list(sample_list):
        """安全地修改列表（创建副本）"""
        # 创建列表的副本，就像复制实验样品
        local_list = sample_list.copy()
        local_list.append("新样品")
        return local_list
    
    original_list2 = ["样品A", "样品B"]
    print("\n3. 安全的列表修改（使用副本）:")
    print(f"原始列表：{original_list2}")
    new_list = safe_modify_list(original_list2)
    print(f"函数外原始列表：{original_list2}")  # 未被修改
    print(f"函数返回的新列表：{new_list}")

demonstrate_parameter_passing()
```

### 不同类型的参数

```python
def demonstrate_parameter_types():
    """
    演示不同类型的参数
    """
    # 1. 位置参数（必需参数）
    def pcr_reaction(template, primer_f, primer_r):
        """
        PCR反应需要的必需参数
        必须按顺序提供，不能省略
        """
        print(f"模板: {template}")
        print(f"正向引物: {primer_f}")
        print(f"反向引物: {primer_r}")
    
    # 必须提供所有参数
    pcr_reaction("DNA_template", "ATCG", "CGAT")
    
    # 2. 默认参数（可选参数）
    def enzyme_reaction(substrate, enzyme, temperature=37, pH=7.0, time=60):
        """
        酶反应的参数设置
        temperature, pH, time有默认值，可以不提供
        """
        print(f"底物: {substrate}")
        print(f"酶: {enzyme}")
        print(f"温度: {temperature}°C")
        print(f"pH: {pH}")
        print(f"时间: {time}分钟")
    
    # 使用默认值
    enzyme_reaction("葡萄糖", "葡萄糖氧化酶")
    
    # 覆盖部分默认值
    enzyme_reaction("葡萄糖", "葡萄糖氧化酶", temperature=25)
    
    # 3. 关键字参数
    def cell_culture(
        cell_line,
        medium="DMEM",
        serum_concentration=10,
        antibiotics=True,
        co2_level=5
    ):
        """
        细胞培养条件设置
        可以通过关键字指定参数，不必按顺序
        """
        config = {
            'cell_line': cell_line,
            'medium': medium,
            'serum': f"{serum_concentration}% FBS",
            'antibiotics': "Yes" if antibiotics else "No",
            'CO2': f"{co2_level}%"
        }
        return config
    
    # 使用关键字参数（顺序可以改变）
    culture1 = cell_culture(
        cell_line="HEK293",
        co2_level=7,  # 顺序改变了
        medium="RPMI",
        serum_concentration=15
    )
    
    # 4. 可变参数 *args
    def mix_solutions(*solutions):
        """
        混合多个溶液
        可以接受任意数量的参数
        """
        print(f"混合{len(solutions)}种溶液:")
        for i, solution in enumerate(solutions, 1):
            print(f"  溶液{i}: {solution}")
        return f"混合液（{len(solutions)}种成分）"
    
    # 可以传入任意数量的参数
    mix_solutions("Buffer A")
    mix_solutions("Buffer A", "Enzyme")
    mix_solutions("Buffer A", "Enzyme", "Substrate", "Cofactor")
    
    # 5. 关键字可变参数 **kwargs
    def experiment_setup(**conditions):
        """
        实验条件设置
        可以接受任意的关键字参数
        """
        print("实验条件设置:")
        for param, value in conditions.items():
            print(f"  {param}: {value}")
    
    # 可以传入任意的关键字参数
    experiment_setup(
        temperature=37,
        pressure="1 atm",
        humidity=60,
        light="dark",
        shaking=True
    )

demonstrate_parameter_types()
```

### 参数设计最佳实践

```python
def design_good_parameters():
    """
    展示参数设计的最佳实践
    """
    
    # ❌ 不好的设计：参数过多，没有默认值
    def bad_analysis(a, b, c, d, e, f, g, h, i, j):
        # 太多参数，难以记忆和使用
        pass
    
    # ✅ 好的设计：使用配置字典
    def good_analysis(sequence, config=None):
        """
        使用配置字典简化参数
        """
        # 默认配置
        default_config = {
            'min_length': 100,
            'max_length': 1000,
            'gc_min': 40,
            'gc_max': 60,
            'quality_threshold': 30
        }
        
        # 更新配置
        if config:
            default_config.update(config)
        
        # 使用配置
        if len(sequence) < default_config['min_length']:
            return "序列太短"
        # ... 更多分析
    
    # ❌ 不好的设计：布尔参数过多
    def bad_process(data, flag1=True, flag2=False, flag3=True, flag4=False):
        # 布尔参数太多，调用时容易混淆
        pass
    
    # ✅ 好的设计：使用有意义的参数名
    def good_process(
        data,
        remove_duplicates=True,
        normalize=False,
        validate_input=True,
        generate_report=False
    ):
        """
        参数名清晰表达意图
        """
        if validate_input:
            # 验证输入
            pass
        if remove_duplicates:
            # 去重
            pass
        if normalize:
            # 标准化
            pass
        if generate_report:
            # 生成报告
            pass
    
    # ❌ 不好的设计：参数顺序混乱
    def bad_order(output_file, input_file, verbose, config, data):
        # 参数顺序不合理
        pass
    
    # ✅ 好的设计：逻辑顺序
    def good_order(
        input_file,      # 输入在前
        data=None,       # 数据次之
        config=None,     # 配置参数
        output_file=None,  # 输出在后
        verbose=False    # 控制参数最后
    ):
        """
        参数按逻辑顺序排列：
        输入 → 处理 → 输出 → 控制
        """
        pass

design_good_parameters()
```

## 🎁 第四部分：返回值设计 - 实验产物的输出

### 不同的返回值模式

```python
def demonstrate_return_patterns():
    """
    演示不同的返回值模式
    """
    
    # 模式1：单一返回值
    def get_sequence_length(sequence):
        """返回序列长度（单一值）"""
        return len(sequence)
    
    # 模式2：返回None（无返回值）
    def print_sequence_info(sequence):
        """打印信息，不返回值"""
        print(f"序列: {sequence}")
        print(f"长度: {len(sequence)}")
        # 没有return语句，默认返回None
    
    # 模式3：返回布尔值（判断结果）
    def is_valid_dna(sequence):
        """判断是否为有效DNA序列"""
        valid_bases = set('ATCG')
        return all(base in valid_bases for base in sequence.upper())
    
    # 模式4：返回元组（多个值）
    def analyze_sequence_basic(sequence):
        """返回多个分析结果"""
        length = len(sequence)
        gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
        at_content = (sequence.count('A') + sequence.count('T')) / length * 100
        return length, gc_content, at_content  # 返回元组
    
    # 使用元组解包
    seq = "ATCGATCGATCG"
    length, gc, at = analyze_sequence_basic(seq)
    print(f"长度: {length}, GC: {gc:.1f}%, AT: {at:.1f}%")
    
    # 模式5：返回字典（结构化数据）
    def analyze_sequence_detailed(sequence):
        """返回详细的分析结果字典"""
        return {
            'sequence': sequence,
            'length': len(sequence),
            'composition': {
                'A': sequence.count('A'),
                'T': sequence.count('T'),
                'C': sequence.count('C'),
                'G': sequence.count('G')
            },
            'gc_content': calculate_gc_content(sequence),
            'features': {
                'has_start_codon': 'ATG' in sequence,
                'has_stop_codon': any(stop in sequence for stop in ['TAA', 'TAG', 'TGA'])
            }
        }
    
    # 模式6：返回列表（多个同类型结果）
    def find_all_codons(sequence):
        """返回所有密码子列表"""
        codons = []
        for i in range(0, len(sequence) - 2, 3):
            codons.append(sequence[i:i+3])
        return codons
    
    # 模式7：返回自定义对象
    class SequenceAnalysis:
        """序列分析结果类"""
        def __init__(self, sequence):
            self.sequence = sequence
            self.length = len(sequence)
            self.gc_content = self._calculate_gc()
        
        def _calculate_gc(self):
            gc = self.sequence.count('G') + self.sequence.count('C')
            return (gc / self.length * 100) if self.length > 0 else 0
        
        def __str__(self):
            return f"SequenceAnalysis(length={self.length}, GC={self.gc_content:.1f}%)"
    
    def analyze_with_class(sequence):
        """返回自定义对象"""
        return SequenceAnalysis(sequence)
    
    # 模式8：条件返回（不同情况返回不同类型）
    def flexible_analysis(sequence, mode="simple"):
        """根据模式返回不同类型的结果"""
        if mode == "simple":
            return len(sequence)  # 返回数字
        elif mode == "detailed":
            return {  # 返回字典
                'length': len(sequence),
                'gc_content': calculate_gc_content(sequence)
            }
        elif mode == "boolean":
            return len(sequence) > 100  # 返回布尔值
        else:
            return None  # 无效模式返回None
    
    # 模式9：生成器返回（延迟计算）
    def generate_kmers(sequence, k=3):
        """生成所有k-mer（生成器模式）"""
        for i in range(len(sequence) - k + 1):
            yield sequence[i:i+k]
    
    # 使用生成器
    seq = "ATCGATCG"
    print("3-mers:")
    for kmer in generate_kmers(seq, k=3):
        print(f"  {kmer}")
    
    # 模式10：错误处理返回
    def safe_division(numerator, denominator):
        """安全的除法运算"""
        try:
            result = numerator / denominator
            return {'success': True, 'value': result}
        except ZeroDivisionError:
            return {'success': False, 'error': '除数不能为零'}
        except TypeError:
            return {'success': False, 'error': '输入类型错误'}

demonstrate_return_patterns()
```

### 返回值设计原则

```python
def return_value_best_practices():
    """
    返回值设计的最佳实践
    """
    
    # 原则1：返回值类型要一致
    # ❌ 不好：有时返回字符串，有时返回数字
    def bad_return(sequence):
        if len(sequence) == 0:
            return "empty"  # 字符串
        else:
            return len(sequence)  # 数字
    
    # ✅ 好：始终返回同一类型
    def good_return(sequence):
        if len(sequence) == 0:
            return 0  # 始终返回数字
        else:
            return len(sequence)
    
    # 原则2：使用None表示"无结果"
    def find_motif(sequence, motif):
        """查找基序，找不到返回None"""
        position = sequence.find(motif)
        if position >= 0:
            return position
        else:
            return None  # 明确返回None
    
    # 原则3：复杂结果使用字典
    def complex_analysis(sequence):
        """复杂分析返回结构化字典"""
        result = {
            'status': 'success',
            'data': {
                'sequence': sequence,
                'length': len(sequence),
                'metrics': {}
            },
            'warnings': [],
            'errors': []
        }
        
        # 添加警告
        if len(sequence) < 10:
            result['warnings'].append('序列过短')
        
        # 添加度量
        result['data']['metrics']['gc_content'] = calculate_gc_content(sequence)
        
        return result
    
    # 原则4：使用元组返回多个相关值
    def get_sequence_bounds(sequences):
        """返回最短和最长序列长度"""
        if not sequences:
            return None, None
        
        lengths = [len(seq) for seq in sequences]
        return min(lengths), max(lengths)  # 返回元组
    
    # 使用示例
    min_len, max_len = get_sequence_bounds(["ATG", "ATCGATCG", "GC"])
    print(f"长度范围: {min_len}-{max_len}")
    
    # 原则5：大量数据使用生成器
    def read_fasta_sequences(filename):
        """读取FASTA文件（生成器模式）"""
        with open(filename, 'r') as file:
            sequence = ""
            header = ""
            for line in file:
                if line.startswith('>'):
                    if sequence:
                        yield header, sequence  # 逐个返回
                    header = line[1:].strip()
                    sequence = ""
                else:
                    sequence += line.strip()
            if sequence:
                yield header, sequence

return_value_best_practices()
```

## 🌐 第五部分：作用域和变量生命周期

### 理解作用域

作用域就像实验室的不同区域：
- **局部作用域**：实验台（只在当前实验可见）
- **全局作用域**：公共区域（整个实验室可见）
- **嵌套作用域**：实验室内的小房间

```python
def demonstrate_scope():
    """
    演示Python的作用域规则
    """
    
    # 全局变量（实验室公共区域的设备）
    lab_temperature = 25  # 实验室温度
    
    def experiment_1():
        """实验1：局部作用域"""
        # 局部变量（实验台上的试剂）
        local_buffer = "PBS"
        sample_count = 10
        
        print(f"实验1使用: {local_buffer}")
        print(f"实验1样品数: {sample_count}")
        print(f"实验室温度: {lab_temperature}")  # 可以访问全局变量
    
    def experiment_2():
        """实验2：不同的局部作用域"""
        # 这里的变量与实验1的变量完全独立
        local_buffer = "Tris"  # 不同的buffer
        sample_count = 20      # 不同的样品数
        
        print(f"实验2使用: {local_buffer}")
        print(f"实验2样品数: {sample_count}")
    
    def experiment_3():
        """实验3：修改全局变量"""
        global lab_temperature  # 声明要修改全局变量
        lab_temperature = 37    # 修改实验室温度
        print(f"实验3将温度调整为: {lab_temperature}°C")
    
    def experiment_4():
        """实验4：嵌套作用域"""
        enzyme = "Taq聚合酶"
        
        def pcr_cycle():
            """PCR循环（嵌套函数）"""
            # 可以访问外层函数的变量
            temperature = 95
            print(f"使用{enzyme}在{temperature}°C变性")
        
        def extension():
            """延伸步骤"""
            temperature = 72  # 这个temperature是局部的
            print(f"使用{enzyme}在{temperature}°C延伸")
        
        pcr_cycle()
        extension()
    
    # 执行演示
    print("="*50)
    print("作用域演示")
    print("="*50)
    
    print(f"\n初始实验室温度: {lab_temperature}°C")
    
    print("\n执行实验1:")
    experiment_1()
    
    print("\n执行实验2:")
    experiment_2()
    
    print("\n执行实验3:")
    experiment_3()
    print(f"实验3后的实验室温度: {lab_temperature}°C")
    
    print("\n执行实验4:")
    experiment_4()

# LEGB规则演示
def demonstrate_legb_rule():
    """
    演示LEGB查找规则
    L - Local（局部）
    E - Enclosing（嵌套）
    G - Global（全局）
    B - Built-in（内置）
    """
    
    # Global作用域
    x = "全局变量"
    
    def outer():
        # Enclosing作用域
        x = "嵌套变量"
        
        def inner():
            # Local作用域
            x = "局部变量"
            print(f"inner函数中: x = {x}")  # 使用局部变量
        
        inner()
        print(f"outer函数中: x = {x}")  # 使用嵌套变量
    
    outer()
    print(f"全局作用域中: x = {x}")  # 使用全局变量
    
    # 使用nonlocal修改嵌套作用域变量
    def experiment():
        count = 0
        
        def increment():
            nonlocal count  # 声明使用外层的count
            count += 1
            return count
        
        print(f"第1次调用: {increment()}")
        print(f"第2次调用: {increment()}")
        print(f"第3次调用: {increment()}")
    
    print("\n使用nonlocal:")
    experiment()

demonstrate_scope()
print("\n" + "="*50)
demonstrate_legb_rule()
```

### 避免作用域陷阱

```python
def scope_pitfalls():
    """
    展示常见的作用域陷阱和如何避免
    """
    
    print("="*50)
    print("作用域陷阱演示")
    print("="*50)
    
    # 陷阱1：意外修改全局变量
    samples = ["DNA1", "DNA2", "DNA3"]
    
    def process_samples_bad():
        """❌ 不好：直接修改全局列表"""
        samples.append("DNA4")  # 修改了全局变量！
        return samples
    
    def process_samples_good():
        """✅ 好：创建副本"""
        local_samples = samples.copy()
        local_samples.append("DNA4")
        return local_samples
    
    print("\n陷阱1：意外修改全局变量")
    print(f"原始samples: {samples}")
    result = process_samples_bad()
    print(f"调用bad函数后: {samples}")  # 被修改了！
    
    samples = ["DNA1", "DNA2", "DNA3"]  # 重置
    result = process_samples_good()
    print(f"调用good函数后: {samples}")  # 未被修改
    
    # 陷阱2：默认参数的可变对象
    def add_sample_bad(sample, sample_list=[]):
        """❌ 不好：默认参数使用可变对象"""
        sample_list.append(sample)
        return sample_list
    
    def add_sample_good(sample, sample_list=None):
        """✅ 好：使用None作为默认值"""
        if sample_list is None:
            sample_list = []
        sample_list.append(sample)
        return sample_list
    
    print("\n陷阱2：默认参数的可变对象")
    print("使用bad函数:")
    print(f"第1次调用: {add_sample_bad('DNA1')}")
    print(f"第2次调用: {add_sample_bad('DNA2')}")  # 包含了前一次的结果！
    
    print("使用good函数:")
    print(f"第1次调用: {add_sample_good('DNA1')}")
    print(f"第2次调用: {add_sample_good('DNA2')}")  # 正确
    
    # 陷阱3：循环中的闭包
    def create_multipliers_bad():
        """❌ 不好：循环变量的延迟绑定"""
        multipliers = []
        for i in range(3):
            multipliers.append(lambda x: x * i)
        return multipliers
    
    def create_multipliers_good():
        """✅ 好：使用默认参数捕获值"""
        multipliers = []
        for i in range(3):
            multipliers.append(lambda x, i=i: x * i)
        return multipliers
    
    print("\n陷阱3：循环中的闭包")
    bad_funcs = create_multipliers_bad()
    print("bad函数结果:")
    for j, func in enumerate(bad_funcs):
        print(f"  函数{j}: 10 * {j} = {func(10)}")  # 全是20！
    
    good_funcs = create_multipliers_good()
    print("good函数结果:")
    for j, func in enumerate(good_funcs):
        print(f"  函数{j}: 10 * {j} = {func(10)}")  # 正确

scope_pitfalls()
```

## 🏗️ 第六部分：函数设计最佳实践

### 单一职责原则

```python
def demonstrate_single_responsibility():
    """
    演示单一职责原则
    每个函数只做一件事，做好一件事
    """
    
    # ❌ 违反单一职责的函数
    def analyze_and_save_and_email(sequence, filename, email):
        """
        这个函数做了太多事情：
        1. 分析序列
        2. 保存到文件
        3. 发送邮件
        """
        # 分析
        gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        
        # 保存
        with open(filename, 'w') as f:
            f.write(f"Sequence: {sequence}\n")
            f.write(f"GC Content: {gc_content}%\n")
        
        # 发邮件
        print(f"Sending email to {email}...")
        # email代码...
        
        return gc_content
    
    # ✅ 遵循单一职责的设计
    def analyze_gc_content(sequence):
        """只负责分析GC含量"""
        if not sequence:
            return 0.0
        return (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    
    def save_analysis_result(result, filename):
        """只负责保存结果"""
        with open(filename, 'w') as f:
            for key, value in result.items():
                f.write(f"{key}: {value}\n")
        return True
    
    def send_notification(recipient, message):
        """只负责发送通知"""
        print(f"Sending to {recipient}: {message}")
        return True
    
    def coordinate_analysis(sequence, filename=None, email=None):
        """协调函数：组合其他函数完成复杂任务"""
        # 步骤1：分析
        gc_content = analyze_gc_content(sequence)
        result = {
            'sequence': sequence,
            'gc_content': f"{gc_content:.2f}%",
            'length': len(sequence)
        }
        
        # 步骤2：保存（如果需要）
        if filename:
            save_analysis_result(result, filename)
        
        # 步骤3：通知（如果需要）
        if email:
            message = f"Analysis complete. GC content: {gc_content:.2f}%"
            send_notification(email, message)
        
        return result
    
    # 使用示例
    print("单一职责原则演示")
    print("-" * 40)
    
    seq = "ATCGATCGATCG"
    
    # 可以单独使用每个函数
    gc = analyze_gc_content(seq)
    print(f"GC含量: {gc:.2f}%")
    
    # 也可以组合使用
    result = coordinate_analysis(
        seq,
        filename="result.txt",
        email="researcher@lab.com"
    )
    print(f"完整结果: {result}")

demonstrate_single_responsibility()
```

### 函数命名规范

```python
def demonstrate_naming_conventions():
    """
    展示函数命名的最佳实践
    """
    
    # ✅ 好的命名示例
    
    # 1. 动作函数使用动词开头
    def calculate_melting_temperature(sequence):
        """计算熔解温度"""
        pass
    
    def validate_primer_pair(forward, reverse):
        """验证引物对"""
        pass
    
    def extract_coding_sequence(genomic_dna, start, end):
        """提取编码序列"""
        pass
    
    # 2. 判断函数使用is_或has_开头
    def is_valid_dna(sequence):
        """判断是否为有效DNA"""
        return all(base in 'ATCG' for base in sequence.upper())
    
    def has_start_codon(sequence):
        """判断是否包含起始密码子"""
        return 'ATG' in sequence.upper()
    
    def is_palindromic(sequence):
        """判断是否为回文序列"""
        return sequence == sequence[::-1]
    
    # 3. 获取函数使用get_开头
    def get_sequence_length(sequence):
        """获取序列长度"""
        return len(sequence)
    
    def get_orf_positions(sequence):
        """获取ORF位置"""
        positions = []
        # 查找逻辑
        return positions
    
    # 4. 设置函数使用set_开头
    def set_experiment_temperature(temp):
        """设置实验温度"""
        global EXPERIMENT_TEMP
        EXPERIMENT_TEMP = temp
    
    # 5. 转换函数描述转换过程
    def dna_to_rna(dna_sequence):
        """DNA转RNA"""
        return dna_sequence.replace('T', 'U')
    
    def celsius_to_fahrenheit(celsius):
        """摄氏度转华氏度"""
        return celsius * 9/5 + 32
    
    # ❌ 不好的命名示例
    
    def process(data):  # 太模糊
        pass
    
    def doit(x):  # 无意义
        pass
    
    def func1(seq):  # 编号命名
        pass
    
    def ANALYSISFUNCTION(SEQUENCE):  # 全大写（应该用于常量）
        pass

demonstrate_naming_conventions()
```

### 文档字符串规范

```python
def demonstrate_docstring_standards():
    """
    展示文档字符串的编写规范
    """
    
    def analyze_protein_sequence(
        sequence,
        calculate_pi=True,
        predict_structure=False,
        database="UniProt"
    ):
        """
        分析蛋白质序列的综合函数。
        
        这个函数提供了蛋白质序列的全面分析功能，包括基础
        统计、理化性质计算、结构预测等。适用于初步的蛋白
        质功能研究。
        
        参数
        ----------
        sequence : str
            蛋白质序列，使用单字母氨基酸代码。
            支持20种标准氨基酸，大小写不敏感。
            
        calculate_pi : bool, optional
            是否计算等电点(pI)，默认为True。
            计算使用Henderson-Hasselbalch方程。
            
        predict_structure : bool, optional
            是否预测二级结构，默认为False。
            预测使用Chou-Fasman方法。
            
        database : str, optional
            用于注释的数据库，默认"UniProt"。
            可选值：{"UniProt", "PDB", "Pfam"}
        
        返回
        -------
        dict
            包含分析结果的字典，键值对如下：
            - 'length' (int): 序列长度
            - 'molecular_weight' (float): 分子量(Da)
            - 'pi' (float): 等电点，如果calculate_pi=True
            - 'structure' (dict): 二级结构预测，如果predict_structure=True
            - 'composition' (dict): 氨基酸组成统计
        
        异常
        ------
        ValueError
            当序列包含非法氨基酸字符时抛出。
            
        TypeError
            当sequence不是字符串类型时抛出。
        
        示例
        --------
        >>> seq = "MKTVRQERLKSIVRILERSKEPVSGAQ"
        >>> result = analyze_protein_sequence(seq)
        >>> print(f"分子量: {result['molecular_weight']:.2f} Da")
        分子量: 3201.65 Da
        
        >>> result = analyze_protein_sequence(
        ...     seq,
        ...     calculate_pi=True,
        ...     predict_structure=True
        ... )
        >>> print(f"等电点: {result['pi']:.2f}")
        等电点: 11.04
        
        注意事项
        --------
        1. 对于长序列(>1000 aa)，结构预测可能需要较长时间。
        2. pI计算假设蛋白质处于水溶液中。
        3. 二级结构预测准确率约为60-70%。
        
        参见
        --------
        calculate_molecular_weight : 计算分子量的专用函数
        predict_secondary_structure : 二级结构预测的专用函数
        
        参考文献
        ---------
        .. [1] Chou, P.Y. and Fasman, G.D. (1974) "Prediction of 
               protein conformation" Biochemistry 13(2), 222-245.
        .. [2] Bjellqvist, B. et al. (1993) "The focusing positions of 
               polypeptides in immobilized pH gradients can be predicted 
               from their amino acid sequences" Electrophoresis 14, 1023-1031.
        
        版本历史
        ---------
        .. versionadded:: 1.0.0
           初始版本
        .. versionchanged:: 1.1.0
           添加了结构预测功能
        .. versionchanged:: 1.2.0
           优化了pI计算算法
        """
        # 函数实现
        pass

demonstrate_docstring_standards()
```

## 🔄 第七部分：重构 - 从重复代码到优雅函数

### 重构实战案例

```python
def refactoring_case_study():
    """
    重构案例：真实的生物信息学代码优化
    """
    
    print("="*60)
    print("重构案例：批量序列质量控制")
    print("="*60)
    
    # 原始代码：充满重复的质控流程
    print("\n❌ 重构前：重复且混乱的代码")
    print("-" * 40)
    
    # 样品1质控
    sample1_seq = "ATCGATCGATCGATCG"
    sample1_name = "Sample_001"
    # 检查长度
    if len(sample1_seq) < 10:
        print(f"{sample1_name}: 序列太短")
    elif len(sample1_seq) > 1000:
        print(f"{sample1_name}: 序列太长")
    # 检查N含量
    n_count1 = sample1_seq.count('N')
    n_percent1 = (n_count1 / len(sample1_seq)) * 100
    if n_percent1 > 5:
        print(f"{sample1_name}: N含量过高({n_percent1:.1f}%)")
    # 检查GC含量
    gc_count1 = sample1_seq.count('G') + sample1_seq.count('C')
    gc_percent1 = (gc_count1 / len(sample1_seq)) * 100
    if gc_percent1 < 20 or gc_percent1 > 80:
        print(f"{sample1_name}: GC含量异常({gc_percent1:.1f}%)")
    
    # 样品2质控（完全重复的代码）
    sample2_seq = "NNNNNATCGATCG"
    sample2_name = "Sample_002"
    # 又是相同的检查...
    
    print("\n✅ 重构后：模块化的函数设计")
    print("-" * 40)
    
    # 步骤1：识别重复的模式
    def check_sequence_length(sequence, min_len=10, max_len=1000):
        """检查序列长度是否合理"""
        length = len(sequence)
        if length < min_len:
            return False, f"序列太短({length}bp < {min_len}bp)"
        elif length > max_len:
            return False, f"序列太长({length}bp > {max_len}bp)"
        return True, "长度合格"
    
    def check_n_content(sequence, max_n_percent=5):
        """检查N含量"""
        n_count = sequence.upper().count('N')
        n_percent = (n_count / len(sequence)) * 100 if sequence else 0
        if n_percent > max_n_percent:
            return False, f"N含量过高({n_percent:.1f}% > {max_n_percent}%)"
        return True, "N含量合格"
    
    def check_gc_content(sequence, min_gc=20, max_gc=80):
        """检查GC含量"""
        sequence = sequence.upper()
        gc_count = sequence.count('G') + sequence.count('C')
        gc_percent = (gc_count / len(sequence)) * 100 if sequence else 0
        if gc_percent < min_gc:
            return False, f"GC含量过低({gc_percent:.1f}% < {min_gc}%)"
        elif gc_percent > max_gc:
            return False, f"GC含量过高({gc_percent:.1f}% > {max_gc}%)"
        return True, f"GC含量正常({gc_percent:.1f}%)"
    
    # 步骤2：创建综合质控函数
    def quality_control(sequence, sample_name, config=None):
        """
        综合序列质量控制
        
        将所有质控步骤整合到一个函数中
        """
        # 默认配置
        default_config = {
            'min_length': 10,
            'max_length': 1000,
            'max_n_percent': 5,
            'min_gc': 20,
            'max_gc': 80
        }
        
        # 更新配置
        if config:
            default_config.update(config)
        
        # 质控结果
        qc_results = {
            'sample': sample_name,
            'passed': True,
            'warnings': [],
            'metrics': {}
        }
        
        # 执行质控检查
        checks = [
            ('length', check_sequence_length(
                sequence,
                default_config['min_length'],
                default_config['max_length']
            )),
            ('n_content', check_n_content(
                sequence,
                default_config['max_n_percent']
            )),
            ('gc_content', check_gc_content(
                sequence,
                default_config['min_gc'],
                default_config['max_gc']
            ))
        ]
        
        # 收集结果
        for check_name, (passed, message) in checks:
            qc_results['metrics'][check_name] = message
            if not passed:
                qc_results['passed'] = False
                qc_results['warnings'].append(message)
        
        return qc_results
    
    # 步骤3：批量处理
    def batch_quality_control(samples, config=None):
        """批量质控"""
        results = []
        passed_count = 0
        
        for sample_name, sequence in samples.items():
            result = quality_control(sequence, sample_name, config)
            results.append(result)
            if result['passed']:
                passed_count += 1
        
        # 生成报告
        total = len(samples)
        print(f"\n质控报告摘要")
        print(f"{'='*40}")
        print(f"总样品数: {total}")
        print(f"通过质控: {passed_count} ({passed_count/total*100:.1f}%)")
        print(f"未通过: {total - passed_count}")
        
        print(f"\n详细结果:")
        for result in results:
            status = "✅ PASS" if result['passed'] else "❌ FAIL"
            print(f"\n{result['sample']}: {status}")
            if not result['passed']:
                for warning in result['warnings']:
                    print(f"  ⚠️  {warning}")
        
        return results
    
    # 使用重构后的代码
    test_samples = {
        'Sample_001': 'ATCGATCGATCGATCG',
        'Sample_002': 'NNNNNATCGATCG',
        'Sample_003': 'ATCG',  # 太短
        'Sample_004': 'GCGCGCGCGCGCGCGCGCGC',  # 高GC
        'Sample_005': 'ATATATATATATATATAT'  # 低GC
    }
    
    # 执行批量质控
    results = batch_quality_control(test_samples)
    
    # 自定义质控标准
    print(f"\n{'='*40}")
    print("使用自定义质控标准")
    strict_config = {
        'min_length': 15,
        'max_n_percent': 1,
        'min_gc': 40,
        'max_gc': 60
    }
    results = batch_quality_control(test_samples, strict_config)

refactoring_case_study()
```

## 🎯 第八部分：综合项目 - 构建完整的序列分析工具

### 项目：基因组注释流水线

```python
def genome_annotation_pipeline():
    """
    综合项目：构建基因组注释流水线
    整合本章所学的所有函数概念
    """
    
    print("="*60)
    print("基因组注释流水线 v1.0")
    print("="*60)
    
    # ==================== 基础工具函数 ====================
    
    def validate_sequence(sequence):
        """验证序列有效性"""
        valid_bases = set('ATCGN')
        sequence = sequence.upper()
        invalid = set(sequence) - valid_bases
        if invalid:
            raise ValueError(f"序列包含无效碱基: {invalid}")
        return True
    
    def clean_sequence(sequence):
        """清理序列"""
        # 去除空白字符和数字
        import re
        cleaned = re.sub(r'[^ATCGNatcgn]', '', sequence)
        return cleaned.upper()
    
    # ==================== 序列分析函数 ====================
    
    def find_orfs(sequence, min_length=300):
        """
        查找开放阅读框（ORF）
        
        参数：
            sequence: DNA序列
            min_length: 最小ORF长度（碱基）
        
        返回：
            ORF列表
        """
        orfs = []
        sequence = sequence.upper()
        
        # 在三个阅读框中查找
        for frame in range(3):
            # 获取当前阅读框
            frame_seq = sequence[frame:]
            
            # 查找所有ATG位置
            start_positions = []
            for i in range(0, len(frame_seq) - 2, 3):
                if frame_seq[i:i+3] == 'ATG':
                    start_positions.append(i)
            
            # 对每个起始密码子，查找终止密码子
            for start in start_positions:
                for i in range(start + 3, len(frame_seq) - 2, 3):
                    codon = frame_seq[i:i+3]
                    if codon in ['TAA', 'TAG', 'TGA']:
                        # 找到终止密码子
                        orf_length = i + 3 - start
                        if orf_length >= min_length:
                            orfs.append({
                                'frame': frame + 1,
                                'start': start + frame,
                                'end': i + 3 + frame,
                                'length': orf_length,
                                'sequence': frame_seq[start:i+3]
                            })
                        break
        
        return orfs
    
    def translate_dna(dna_sequence):
        """
        将DNA翻译为蛋白质
        """
        # 完整的密码子表
        codon_table = {
            'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
            'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
            'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
            'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
            'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
            'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
            'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
            'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }
        
        protein = ""
        sequence = dna_sequence.upper()
        
        for i in range(0, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if len(codon) == 3:
                protein += codon_table.get(codon, 'X')
        
        return protein
    
    def find_promoters(sequence):
        """
        查找启动子区域（简化版）
        """
        promoters = []
        sequence = sequence.upper()
        
        # TATA box (TATAAA)
        tata_pattern = 'TATAAA'
        pos = 0
        while True:
            pos = sequence.find(tata_pattern, pos)
            if pos == -1:
                break
            promoters.append({
                'type': 'TATA box',
                'position': pos,
                'sequence': sequence[max(0, pos-10):pos+20]
            })
            pos += 1
        
        # CAAT box (GGCCAATCT)
        caat_pattern = 'CCAAT'
        pos = 0
        while True:
            pos = sequence.find(caat_pattern, pos)
            if pos == -1:
                break
            promoters.append({
                'type': 'CAAT box',
                'position': pos,
                'sequence': sequence[max(0, pos-10):pos+20]
            })
            pos += 1
        
        return promoters
    
    def predict_gene_function(protein_sequence):
        """
        预测基因功能（基于简单的模体搜索）
        """
        functions = []
        
        # 定义功能模体
        motifs = {
            'DNA结合': ['CXXC', 'HXXXH'],  # 锌指结构
            '激酶': ['GXGXXG', 'DFG'],      # ATP结合位点
            '磷酸酶': ['HCXXGXXR'],         # 磷酸酶活性位点
            '转录因子': ['WRKY', 'MYB'],    # 转录因子结构域
        }
        
        sequence = protein_sequence.upper()
        
        for function, patterns in motifs.items():
            for pattern in patterns:
                # 简化的模式匹配（X表示任意氨基酸）
                if pattern.replace('X', '') in sequence:
                    functions.append(function)
                    break
        
        return functions if functions else ['未知功能']
    
    # ==================== 注释流水线主函数 ====================
    
    def annotate_genome(sequence, gene_name="Unknown"):
        """
        基因组注释主流水线
        """
        print(f"\n正在分析基因: {gene_name}")
        print("-" * 40)
        
        # 步骤1：序列预处理
        print("步骤1: 序列预处理")
        cleaned_seq = clean_sequence(sequence)
        validate_sequence(cleaned_seq)
        print(f"  ✓ 序列长度: {len(cleaned_seq)} bp")
        
        # 步骤2：查找启动子
        print("\n步骤2: 查找调控元件")
        promoters = find_promoters(cleaned_seq)
        print(f"  ✓ 发现 {len(promoters)} 个潜在启动子元件")
        for p in promoters:
            print(f"    - {p['type']} at position {p['position']}")
        
        # 步骤3：查找ORF
        print("\n步骤3: 查找开放阅读框(ORF)")
        orfs = find_orfs(cleaned_seq, min_length=90)
        print(f"  ✓ 发现 {len(orfs)} 个ORF (>90bp)")
        
        # 步骤4：翻译和功能预测
        print("\n步骤4: 蛋白质翻译和功能预测")
        annotations = []
        
        for i, orf in enumerate(orfs, 1):
            protein = translate_dna(orf['sequence'])
            functions = predict_gene_function(protein)
            
            annotation = {
                'id': f"{gene_name}_ORF{i}",
                'position': f"{orf['start']}-{orf['end']}",
                'frame': orf['frame'],
                'length': orf['length'],
                'protein_length': len(protein.replace('*', '')),
                'predicted_functions': functions
            }
            annotations.append(annotation)
            
            print(f"\n  ORF{i}:")
            print(f"    位置: {annotation['position']} (Frame {orf['frame']})")
            print(f"    长度: {orf['length']} bp ({annotation['protein_length']} aa)")
            print(f"    功能预测: {', '.join(functions)}")
            print(f"    蛋白序列前20aa: {protein[:20]}...")
        
        # 步骤5：生成注释报告
        print("\n" + "="*40)
        print("注释报告摘要")
        print("="*40)
        
        report = {
            'gene_name': gene_name,
            'sequence_length': len(cleaned_seq),
            'gc_content': calculate_gc_content(cleaned_seq),
            'promoter_count': len(promoters),
            'orf_count': len(orfs),
            'annotations': annotations
        }
        
        print(f"基因名称: {report['gene_name']}")
        print(f"序列长度: {report['sequence_length']} bp")
        print(f"GC含量: {report['gc_content']:.1f}%")
        print(f"启动子元件: {report['promoter_count']} 个")
        print(f"预测基因: {report['orf_count']} 个")
        
        # 功能统计
        all_functions = []
        for ann in annotations:
            all_functions.extend(ann['predicted_functions'])
        
        if all_functions:
            print(f"\n预测的功能类别:")
            function_counts = {}
            for func in all_functions:
                function_counts[func] = function_counts.get(func, 0) + 1
            for func, count in function_counts.items():
                print(f"  - {func}: {count} 个基因")
        
        return report
    
    # ==================== 测试流水线 ====================
    
    # 测试序列（包含多个ORF的模拟基因组片段）
    test_genome = """
    TATAAAAGGCCAATCTGATCGATCGATCG
    ATGGCGATCGATCGATCGATCGATCGTAGATCGATCG
    ATGAAACCCGGGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
    GGGCCCCGGGAAATTTCCCGGGATCGATCGATCGATCGATCGATCGATCGATCGATCGA
    TCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
    ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
    GATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAT
    CGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGTAGGATCGATCGA
    ATGCCCGGGAAATTTGGGCCCGGGATCGATCGATCGATCGATCGATCGATCGATCGATC
    GATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAT
    CGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGA
    TCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
    TAATAGATCGATCGATCGATCGATCGATCGATCG
    """
    
    # 运行注释流水线
    result = annotate_genome(test_genome, "TEST_GENOME_001")
    
    return result

# 运行综合项目
genome_annotation_pipeline()
```

## 📝 常见错误和调试技巧

### 常见错误模式

```python
def common_mistakes_and_solutions():
    """
    展示常见的函数编程错误和解决方案
    """
    
    print("="*60)
    print("常见错误和解决方案")
    print("="*60)
    
    # 错误1：忘记return
    print("\n错误1: 忘记return语句")
    print("-" * 40)
    
    def calculate_mean_wrong(values):
        """❌ 错误：计算了但没有返回"""
        mean = sum(values) / len(values)
        # 忘记return！
    
    def calculate_mean_correct(values):
        """✅ 正确：返回计算结果"""
        mean = sum(values) / len(values)
        return mean
    
    data = [1, 2, 3, 4, 5]
    result_wrong = calculate_mean_wrong(data)
    result_correct = calculate_mean_correct(data)
    
    print(f"错误版本返回: {result_wrong}")  # None
    print(f"正确版本返回: {result_correct}")  # 3.0
    
    # 错误2：修改默认参数
    print("\n错误2: 可变默认参数")
    print("-" * 40)
    
    def append_to_list_wrong(item, target=[]):
        """❌ 错误：默认参数使用可变对象"""
        target.append(item)
        return target
    
    def append_to_list_correct(item, target=None):
        """✅ 正确：使用None作为默认值"""
        if target is None:
            target = []
        target.append(item)
        return target
    
    # 演示问题
    print("错误版本:")
    list1 = append_to_list_wrong('A')
    print(f"  第1次调用: {list1}")
    list2 = append_to_list_wrong('B')  # 期望['B']，实际['A', 'B']
    print(f"  第2次调用: {list2}")
    
    print("正确版本:")
    list3 = append_to_list_correct('A')
    print(f"  第1次调用: {list3}")
    list4 = append_to_list_correct('B')
    print(f"  第2次调用: {list4}")
    
    # 错误3：作用域混淆
    print("\n错误3: 作用域混淆")
    print("-" * 40)
    
    count = 0  # 全局变量
    
    def increment_wrong():
        """❌ 错误：试图修改全局变量但没有声明"""
        try:
            count += 1  # UnboundLocalError
        except UnboundLocalError as e:
            print(f"  错误: {e}")
    
    def increment_correct():
        """✅ 正确：使用global声明"""
        global count
        count += 1
        return count
    
    print("错误版本:")
    increment_wrong()
    
    print("正确版本:")
    result = increment_correct()
    print(f"  count = {result}")
    
    # 错误4：参数顺序错误
    print("\n错误4: 参数顺序混淆")
    print("-" * 40)
    
    def create_primer(sequence, name, temperature=60):
        """设计引物"""
        return {
            'name': name,
            'sequence': sequence,
            'tm': temperature
        }
    
    # 错误调用
    # primer = create_primer("Primer1", "ATCGATCG")  # 顺序错了！
    
    # 正确调用
    primer = create_primer("ATCGATCG", "Primer1")
    # 或使用关键字参数
    primer = create_primer(name="Primer1", sequence="ATCGATCG")
    
    print(f"正确调用: {primer}")
    
    # 错误5：无限递归
    print("\n错误5: 无限递归")
    print("-" * 40)
    
    def factorial_wrong(n):
        """❌ 错误：没有递归终止条件"""
        # return n * factorial_wrong(n - 1)  # 会无限递归！
        pass
    
    def factorial_correct(n):
        """✅ 正确：有递归终止条件"""
        if n <= 1:  # 终止条件
            return 1
        return n * factorial_correct(n - 1)
    
    print(f"5! = {factorial_correct(5)}")

common_mistakes_and_solutions()
```

### 调试技巧

```python
def debugging_techniques():
    """
    函数调试技巧
    """
    
    print("="*60)
    print("函数调试技巧")
    print("="*60)
    
    # 技巧1：使用print调试
    def analyze_sequence_debug(sequence):
        """使用print语句调试"""
        print(f"[DEBUG] 输入序列: {sequence}")
        print(f"[DEBUG] 序列类型: {type(sequence)}")
        print(f"[DEBUG] 序列长度: {len(sequence)}")
        
        # 处理逻辑
        gc_count = sequence.count('G') + sequence.count('C')
        print(f"[DEBUG] GC碱基数: {gc_count}")
        
        gc_content = (gc_count / len(sequence)) * 100
        print(f"[DEBUG] GC含量: {gc_content:.2f}%")
        
        return gc_content
    
    # 技巧2：使用assert进行断言
    def safe_divide(a, b):
        """使用断言确保输入有效"""
        assert b != 0, "除数不能为零"
        assert isinstance(a, (int, float)), "被除数必须是数字"
        assert isinstance(b, (int, float)), "除数必须是数字"
        
        return a / b
    
    # 技巧3：添加日志
    def process_with_logging(data):
        """使用日志记录"""
        import logging
        
        # 配置日志
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        
        logger.debug(f"开始处理，数据大小: {len(data)}")
        
        try:
            # 处理逻辑
            result = []
            for item in data:
                logger.debug(f"处理项目: {item}")
                result.append(item.upper())
            
            logger.info(f"处理完成，结果数量: {len(result)}")
            return result
            
        except Exception as e:
            logger.error(f"处理失败: {e}")
            raise
    
    # 技巧4：使用装饰器追踪函数调用
    def trace_calls(func):
        """装饰器：追踪函数调用"""
        def wrapper(*args, **kwargs):
            print(f"\n[TRACE] 调用函数: {func.__name__}")
            print(f"[TRACE] 参数: args={args}, kwargs={kwargs}")
            
            result = func(*args, **kwargs)
            
            print(f"[TRACE] 返回值: {result}")
            return result
        return wrapper
    
    @trace_calls
    def calculate_tm(sequence):
        """计算Tm值"""
        gc = sequence.count('G') + sequence.count('C')
        at = sequence.count('A') + sequence.count('T')
        tm = 4 * gc + 2 * at
        return tm
    
    # 演示调试技巧
    print("\n1. Print调试:")
    analyze_sequence_debug("ATCGATCG")
    
    print("\n2. 断言测试:")
    try:
        result = safe_divide(10, 2)
        print(f"10 / 2 = {result}")
        # result = safe_divide(10, 0)  # 会触发断言错误
    except AssertionError as e:
        print(f"断言失败: {e}")
    
    print("\n3. 装饰器追踪:")
    tm = calculate_tm("ATCGATCG")

debugging_techniques()
```

## 🎮 练习预览

在 `practice.py` 文件中，你将找到7个渐进式练习：

### 练习概览

1. **你的第一个函数** ⭐
   - 创建计算AT含量的函数
   - 学习基本的函数定义和调用

2. **添加输入验证** ⭐⭐
   - 为函数添加质控步骤
   - 处理边界情况和异常输入

3. **灵活的参数设计** ⭐⭐
   - 使用默认参数
   - 设计用户友好的接口

4. **重构重复代码** ⭐⭐⭐
   - 识别代码中的重复模式
   - 提取共同逻辑为函数

5. **函数组合** ⭐⭐⭐
   - 组合简单函数构建复杂功能
   - 创建分析流水线

6. **ORF查找器** ⭐⭐⭐⭐
   - 实现专业的生物信息学工具
   - 处理复杂的序列分析

7. **错误处理** ⭐⭐⭐⭐
   - 创建健壮的函数
   - 优雅地处理各种异常

## 📚 知识总结

### 核心要点

✅ **函数是什么**
- 函数是可重用的代码块
- 相当于实验室的标准操作流程(SOP)
- 将复杂任务分解为简单步骤

✅ **为什么需要函数**
- 消除代码重复
- 提高代码可维护性
- 促进代码复用和分享
- 使代码更易理解和测试

✅ **函数的组成**
- `def`：定义关键字
- 函数名：描述功能的标识符
- 参数：输入数据
- 函数体：处理逻辑
- 返回值：输出结果

✅ **参数设计**
- 必需参数：没有默认值，必须提供
- 可选参数：有默认值，可以省略
- 位置参数：按顺序传递
- 关键字参数：按名称传递

✅ **返回值模式**
- 单一值：返回一个结果
- 多值：使用元组返回多个值
- 字典：返回结构化数据
- None：不返回值（副作用函数）

✅ **作用域规则**
- 局部作用域：函数内部
- 全局作用域：模块级别
- LEGB规则：Local → Enclosing → Global → Built-in

✅ **设计原则**
- 单一职责：一个函数只做一件事
- 清晰命名：函数名表达其功能
- 合理参数：不要太多参数
- 完善文档：编写清晰的文档字符串

✅ **最佳实践**
- 先写文档字符串，再写代码
- 保持函数简短（通常不超过20行）
- 避免副作用（不修改全局状态）
- 进行输入验证和错误处理
- 编写单元测试

### 生物学类比总结

| 编程概念 | 生物学类比 | 实际应用 |
|---------|-----------|---------|
| 函数定义 | 编写SOP | 标准化实验流程 |
| 函数调用 | 执行SOP | 按流程操作 |
| 参数 | 实验材料 | 输入样品和试剂 |
| 返回值 | 实验产物 | 获得实验结果 |
| 局部变量 | 实验台试剂 | 仅在当前实验使用 |
| 全局变量 | 公共试剂 | 整个实验室共享 |
| 函数组合 | 实验流程整合 | 构建完整方案 |
| 错误处理 | 故障排除 | 处理异常情况 |

## 🚀 下一步学习

完成本章学习后，你已经掌握了函数编程的核心概念。在下一章（Chapter 05: 文件IO），你将学习：

1. **读取生物数据文件**
   - FASTA格式
   - GenBank格式
   - CSV/TSV数据

2. **处理大文件**
   - 流式读取
   - 批处理策略
   - 内存优化

3. **数据输出**
   - 生成报告
   - 导出结果
   - 格式转换

你会发现，文件IO操作将大量使用本章学到的函数来解析、处理和分析数据。函数将成为你构建复杂生物信息学程序的基础积木。

## 🎯 行动计划

1. **立即练习**：完成 `practice.py` 中的7个练习
2. **实践应用**：用函数重构你现有的分析代码
3. **构建工具库**：创建自己的常用函数集合
4. **分享代码**：将函数打包分享给同事

记住：**好的函数就像精心编写的实验室SOP，让复杂的分析变得简单、可靠、可重复。** 每当你发现自己在复制粘贴代码时，就是创建函数的最佳时机！

---

*"程序员的三大美德：懒惰、急躁和傲慢。懒惰使你努力减少总的精力消耗，它使你编写省力的程序，并记录它们以免别人问你问题。"* - Larry Wall（Perl语言创始人）

在生物信息学中，这种"懒惰"正是我们追求的效率。通过创建函数，我们一次编写，无限复用，将更多时间投入到科学发现而非重复劳动中。

**现在，开始将你的代码转化为优雅的函数吧！** 🧬💪