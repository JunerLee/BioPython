# Chapter 04: 函数 - 实验室的标准操作流程(SOP)

## 📖 写在最前面 - 给生物学研究者的信

亲爱的同行：

还记得你第一次独立完成DNA提取的经历吗？一开始，你小心翼翼地对照着protocol，一步一步操作。但现在，这整个流程已经成为你的肌肉记忆。

**编程中的函数，就是你的数字化SOP。**

想象一下：你的实验室每天都要处理上百个样品的GC含量计算。如果每次都重新写计算步骤，不仅效率低下，还容易出错。但如果你创建了一个`calculate_gc_content`函数，就像制定了一个标准的GC含量测定SOP，需要时只需"调用"即可。

## 🎯 本章导航

### 📊 学习目标

完成本章后你将能够：

✅ **理解函数的本质** - 为什么需要函数，如何工作
✅ **掌握函数的创建** - 定义、参数、返回值、文档
✅ **理解作用域概念** - 局部vs全局变量，避免副作用
✅ **实践函数设计** - 单一职责，最佳实践，错误处理
✅ **构建函数库** - 组合函数，创建工具集，代码重构

### 🗺️ 知识结构图

```
函数编程
├── 为什么需要函数？
│   ├── 消除代码重复
│   ├── 提高可维护性
│   └── 促进代码复用
│
├── 函数基础
│   ├── 定义语法（def关键字）
│   ├── 参数系统（位置/默认/关键字）
│   ├── 返回值处理
│   └── 文档字符串
│
├── 作用域
│   ├── 局部作用域（函数内部）
│   ├── 全局作用域（模块级别）
│   └── LEGB规则（查找顺序）
│
└── 最佳实践
    ├── 函数设计原则
    ├── 错误处理
    └── 代码重构
```

### 🎓 学习路径

```
第一步：理解必要性（20分钟）
    ↓
第二步：创建第一个函数（30分钟）
    ↓
第三步：掌握参数设计（40分钟）
    ↓
第四步：处理返回值（30分钟）
    ↓
第五步：理解作用域（20分钟）
    ↓
第六步：实践重构（40分钟）
    ↓
第七步：构建工具库（60分钟）
```

## 🔬 第一部分：为什么需要函数？

### 真实案例：疯狂的复制粘贴

李博士要分析100个基因的表达数据，每个基因需要相同处理：
1. 计算平均表达量
2. 标准化处理
3. 判断是否差异表达

**没有函数的噩梦：**

```python
# 处理基因1
gene1_expression = [23.5, 24.1, 22.8, 23.9, 24.5]
gene1_mean = sum(gene1_expression) / len(gene1_expression)
gene1_std = ((sum((x - gene1_mean)**2 for x in gene1_expression) / len(gene1_expression))**0.5)
if abs(gene1_mean - 20) > 2:
    print("Gene1 is differentially expressed")

# 处理基因2（复制粘贴，修改变量名）
gene2_expression = [18.2, 17.9, 18.5, 19.1, 18.8]
gene2_mean = sum(gene2_expression) / len(gene2_expression)
# ... 重复相同的计算
# ... 还有98个基因要处理 😱
```

**问题分析：**
- 代码重复100次，文件超长
- 修改算法需要改100个地方
- 极易出错（忘记改变量名）
- 代码难以理解和维护

**使用函数的优雅解决方案：**

```python
def analyze_gene_expression(expression_data, gene_name, control_level=20, threshold=2):
    """
    分析基因表达数据的标准流程
    
    就像实验室的标准操作流程(SOP)：
    1. 计算平均值
    2. 数据标准化
    3. 判断差异表达
    
    参数：
        expression_data: 表达量数据列表
        gene_name: 基因名称
        control_level: 对照组表达水平
        threshold: 差异表达阈值
    
    返回：
        分析结果字典
    """
    # 计算平均表达量
    mean_expression = sum(expression_data) / len(expression_data)
    
    # 计算标准差
    variance = sum((x - mean_expression)**2 for x in expression_data) / len(expression_data)
    std_dev = variance ** 0.5
    
    # 判断是否差异表达
    is_differential = abs(mean_expression - control_level) > threshold
    
    return {
        'gene': gene_name,
        'mean': mean_expression,
        'std': std_dev,
        'is_differential': is_differential
    }

# 现在处理100个基因变得轻松
genes_data = {
    'BRCA1': [23.5, 24.1, 22.8, 23.9, 24.5],
    'TP53': [18.2, 17.9, 18.5, 19.1, 18.8],
    'MYC': [30.1, 29.8, 31.2, 30.5, 30.9]
}

for gene_name, expression in genes_data.items():
    result = analyze_gene_expression(expression, gene_name)
    if result['is_differential']:
        print(f"{gene_name} is differentially expressed (mean: {result['mean']:.2f})")
```

### 🧬 生物学类比理解

函数就像实验室的标准操作流程：

```
实验室SOP                 →    程序函数
─────────────────────────────────────────
• 标题（实验名称）         →    函数名
• 所需材料清单            →    参数
• 详细操作步骤            →    函数体
• 预期结果               →    返回值
• 注意事项               →    文档字符串
• 质量控制               →    错误处理
```

## 🎭 第二部分：创建你的第一个函数

### 2.1 函数定义语法

```python
def function_name(parameters):
    """文档字符串 - 这个函数做什么"""
    # 函数体
    result = do_something()
    return result  # 返回结果
```

### 2.2 基础示例：GC含量计算器

```python
def calculate_gc_content(dna_sequence):
    """
    计算DNA序列的GC含量
    
    就像用分光光度计测定GC含量一样，
    这个函数统计G和C碱基的比例。
    
    参数：
        dna_sequence (str): DNA序列
    
    返回：
        float: GC含量百分比
    """
    # 转换为大写，确保统一格式
    sequence = dna_sequence.upper()
    
    # 统计G和C的数量
    gc_count = sequence.count('G') + sequence.count('C')
    
    # 计算百分比
    if len(sequence) == 0:
        return 0.0
    
    gc_percentage = (gc_count / len(sequence)) * 100
    
    return gc_percentage

# 使用函数
sequences = [
    "ATGCGATCGATC",
    "GCGCGCGCGCGC", 
    "ATATATATATATAT"
]

for seq in sequences:
    gc = calculate_gc_content(seq)
    print(f"序列 {seq}: GC含量 {gc:.1f}%")
```

### 2.3 参数设计：必需vs可选

```python
def reverse_complement(dna_sequence, rna_mode=False):
    """
    生成DNA的反向互补序列
    
    就像设计PCR引物时需要考虑反向互补一样
    
    参数：
        dna_sequence (str): 输入的DNA序列
        rna_mode (bool): 是否生成RNA格式（U代替T）
    
    返回：
        str: 反向互补序列
    """
    # 定义配对规则
    if rna_mode:
        complement = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    else:
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # 生成互补序列
    sequence = dna_sequence.upper()
    complement_seq = ''.join(complement.get(base, base) for base in sequence)
    
    # 返回反向互补
    return complement_seq[::-1]

# 使用示例
dna = "ATGCGATCG"
print(f"原始序列: {dna}")
print(f"DNA反向互补: {reverse_complement(dna)}")
print(f"RNA反向互补: {reverse_complement(dna, rna_mode=True)}")
```

### 2.4 多值返回：序列统计

```python
def analyze_sequence_composition(sequence):
    """
    全面分析序列组成
    
    就像全套的序列质量检测
    
    参数：
        sequence (str): DNA序列
    
    返回：
        tuple: (总长度, GC含量, 碱基计数字典)
    """
    sequence = sequence.upper()
    length = len(sequence)
    
    # 统计各碱基数量
    base_counts = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C'),
        'N': sequence.count('N')
    }
    
    # 计算GC含量
    gc_content = ((base_counts['G'] + base_counts['C']) / length * 100) if length > 0 else 0
    
    return length, gc_content, base_counts

# 使用示例
seq = "ATGCGATCGNATCG"
length, gc, counts = analyze_sequence_composition(seq)

print(f"序列长度: {length} bp")
print(f"GC含量: {gc:.1f}%")
print(f"碱基组成: {counts}")
```

## 🔍 第三部分：作用域 - 避免"实验室污染"

### 3.1 局部vs全局变量

```python
# 全局变量（实验室的公共试剂）
CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'ATG': 'M', 'TAA': '*', 'TAG': '*', 'TGA': '*'
}

def translate_codon(codon):
    """
    翻译密码子为氨基酸
    
    参数：
        codon (str): 三联体密码子
    
    返回：
        str: 氨基酸字母
    """
    # 局部变量（函数内部的实验用品）
    clean_codon = codon.upper().strip()
    
    # 访问全局变量
    return CODON_TABLE.get(clean_codon, 'X')  # X表示未知氨基酸

def translate_dna(dna_sequence):
    """
    将DNA序列翻译为蛋白质序列
    
    参数：
        dna_sequence (str): DNA序列
    
    返回：
        str: 氨基酸序列
    """
    sequence = dna_sequence.upper()
    protein = ""
    
    # 每三个碱基翻译一次
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            amino_acid = translate_codon(codon)  # 调用其他函数
            if amino_acid == '*':  # 遇到终止密码子就停止
                break
            protein += amino_acid
    
    return protein

# 使用示例
dna = "ATGTTCTTATTGTAG"  # ATG TTC TTA TTG TAG
protein = translate_dna(dna)
print(f"DNA: {dna}")
print(f"蛋白质: {protein}")
```

### 3.2 参数传递：引用vs值

```python
def analyze_samples_safe(sample_list):
    """
    安全的样品分析（不修改原始数据）
    
    参数：
        sample_list: 样品列表
    
    返回：
        分析结果
    """
    # 创建副本，避免修改原始数据
    samples = sample_list.copy()
    
    results = []
    for sample in samples:
        # 进行分析但不修改原始数据
        gc_content = calculate_gc_content(sample)
        results.append({
            'sequence': sample,
            'gc_content': gc_content,
            'length': len(sample)
        })
    
    return results

def analyze_samples_unsafe(sample_list):
    """
    不安全的样品分析（可能修改原始数据）
    """
    # 直接修改传入的列表
    for i in range(len(sample_list)):
        sample_list[i] = sample_list[i].upper()  # 危险！修改了原始数据
    
    return sample_list

# 演示差异
original_samples = ["atgc", "cgta", "ggcc"]
print(f"原始数据: {original_samples}")

# 安全方法
safe_results = analyze_samples_safe(original_samples)
print(f"安全分析后，原始数据: {original_samples}")  # 未被修改

# 不安全方法
unsafe_results = analyze_samples_unsafe(original_samples)
print(f"不安全分析后，原始数据: {original_samples}")  # 被修改了！
```

## 🔧 第四部分：函数设计最佳实践

### 4.1 单一职责原则

```python
# ❌ 错误：一个函数做太多事
def bad_sequence_processor(sequence):
    # 计算GC含量
    gc = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    # 查找ORF
    orfs = []
    for i in range(len(sequence)-2):
        if sequence[i:i+3] == 'ATG':
            orfs.append(i)
    # 翻译蛋白质
    protein = translate_dna(sequence)
    # 保存到文件
    with open('results.txt', 'w') as f:
        f.write(f"GC: {gc}, ORFs: {orfs}, Protein: {protein}")
    
    return gc, orfs, protein

# ✅ 正确：每个函数只负责一件事
def calculate_gc_content(sequence):
    """只负责计算GC含量"""
    return (sequence.count('G') + sequence.count('C')) / len(sequence) * 100

def find_start_codons(sequence):
    """只负责查找起始密码子"""
    positions = []
    for i in range(len(sequence)-2):
        if sequence[i:i+3] == 'ATG':
            positions.append(i)
    return positions

def save_results(filename, **data):
    """只负责保存结果"""
    with open(filename, 'w') as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

# 使用组合来完成复杂任务
def process_sequence(sequence):
    """组合多个函数完成序列处理"""
    results = {}
    results['gc_content'] = calculate_gc_content(sequence)
    results['start_codons'] = find_start_codons(sequence)
    results['protein'] = translate_dna(sequence)
    return results
```

### 4.2 错误处理

```python
def robust_gc_calculator(sequence):
    """
    健壮的GC含量计算器
    
    参数：
        sequence (str): DNA序列
    
    返回：
        float: GC含量百分比
    
    异常：
        ValueError: 输入不是字符串或为空
        TypeError: 输入类型错误
    """
    # 参数验证
    if not isinstance(sequence, str):
        raise TypeError(f"序列必须是字符串，得到的是 {type(sequence)}")
    
    if not sequence:
        raise ValueError("序列不能为空")
    
    # 清理和验证序列
    clean_sequence = sequence.upper().strip()
    valid_bases = set('ATGCN')
    invalid_bases = set(clean_sequence) - valid_bases
    
    if invalid_bases:
        print(f"警告：发现无效碱基 {invalid_bases}，将忽略")
        clean_sequence = ''.join(base for base in clean_sequence if base in valid_bases)
    
    if not clean_sequence:
        return 0.0
    
    # 计算GC含量
    gc_count = clean_sequence.count('G') + clean_sequence.count('C')
    return (gc_count / len(clean_sequence)) * 100

# 使用示例
try:
    print(robust_gc_calculator("ATGCXYZ"))  # 包含无效字符
    print(robust_gc_calculator(""))        # 空序列
except (ValueError, TypeError) as e:
    print(f"错误：{e}")
```

### 4.3 函数文档规范

```python
def find_orfs(dna_sequence, min_length=30, start_codons=None):
    """
    在DNA序列中查找开放阅读框(ORF)
    
    开放阅读框是从起始密码子开始到终止密码子结束的序列段，
    可能编码蛋白质。这个函数在三个阅读框中搜索ORF。
    
    参数：
        dna_sequence (str): 待分析的DNA序列
        min_length (int, 可选): ORF最小长度，默认30bp
        start_codons (list, 可选): 起始密码子列表，默认['ATG']
    
    返回：
        list: ORF信息字典列表，包含：
            - 'frame': 阅读框 (0, 1, 2)
            - 'start': 起始位置
            - 'end': 结束位置
            - 'length': ORF长度
            - 'sequence': ORF序列
    
    示例：
        >>> find_orfs("ATGAAATAG", min_length=9)
        [{'frame': 0, 'start': 0, 'end': 9, 'length': 9, 'sequence': 'ATGAAATAG'}]
    
    注意：
        - 序列会自动转换为大写
        - ORF必须以指定的起始密码子开始
        - 必须以终止密码子(TAA/TAG/TGA)结束
    """
    if start_codons is None:
        start_codons = ['ATG']
    
    stop_codons = ['TAA', 'TAG', 'TGA']
    sequence = dna_sequence.upper()
    orfs = []
    
    # 在三个阅读框中搜索
    for frame in range(3):
        i = frame
        while i <= len(sequence) - 3:
            codon = sequence[i:i+3]
            
            if codon in start_codons:
                # 寻找终止密码子
                for j in range(i + 3, len(sequence), 3):
                    if j + 2 < len(sequence):
                        stop_codon = sequence[j:j+3]
                        if stop_codon in stop_codons:
                            orf_length = j + 3 - i
                            if orf_length >= min_length:
                                orfs.append({
                                    'frame': frame,
                                    'start': i,
                                    'end': j + 3,
                                    'length': orf_length,
                                    'sequence': sequence[i:j+3]
                                })
                            i = j + 3  # 跳到ORF结束
                            break
                else:
                    i += 3  # 没找到终止密码子，继续搜索
            else:
                i += 3
    
    return orfs
```

## 🔨 第五部分：构建生物信息学工具库

### 5.1 序列工具集

```python
class SequenceToolkit:
    """生物序列分析工具集"""
    
    @staticmethod
    def gc_content(sequence):
        """计算GC含量"""
        seq = sequence.upper()
        if len(seq) == 0:
            return 0.0
        gc_count = seq.count('G') + seq.count('C')
        return (gc_count / len(seq)) * 100
    
    @staticmethod
    def reverse_complement(sequence):
        """反向互补"""
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
        return ''.join(complement.get(base.upper(), base) for base in sequence[::-1])
    
    @staticmethod
    def translate(dna_sequence, genetic_code=None):
        """翻译DNA为蛋白质"""
        if genetic_code is None:
            genetic_code = {
                'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
                'ATG': 'M', 'TAA': '*', 'TAG': '*', 'TGA': '*'
                # 简化的遗传密码表
            }
        
        protein = ""
        for i in range(0, len(dna_sequence), 3):
            codon = dna_sequence[i:i+3].upper()
            if len(codon) == 3:
                aa = genetic_code.get(codon, 'X')
                if aa == '*':
                    break
                protein += aa
        return protein
    
    @staticmethod
    def find_pattern(sequence, pattern):
        """查找序列模式"""
        positions = []
        seq = sequence.upper()
        pattern = pattern.upper()
        
        for i in range(len(seq) - len(pattern) + 1):
            if seq[i:i+len(pattern)] == pattern:
                positions.append(i)
        
        return positions

# 使用工具集
toolkit = SequenceToolkit()
dna = "ATGAAATTCTAG"

print(f"序列: {dna}")
print(f"GC含量: {toolkit.gc_content(dna):.1f}%")
print(f"反向互补: {toolkit.reverse_complement(dna)}")
print(f"翻译蛋白质: {toolkit.translate(dna)}")
print(f"ATG位置: {toolkit.find_pattern(dna, 'ATG')}")
```

### 5.2 质量控制流程

```python
def sequence_quality_pipeline(sequences, min_length=10, max_n_percent=10, min_gc=20, max_gc=80):
    """
    序列质量控制流水线
    
    参数：
        sequences (list): 序列列表
        min_length (int): 最小长度
        max_n_percent (float): 最大N含量百分比
        min_gc (float): 最小GC含量
        max_gc (float): 最大GC含量
    
    返回：
        dict: 质控结果
    """
    results = {
        'passed': [],
        'failed': [],
        'stats': {
            'total': len(sequences),
            'passed_count': 0,
            'failed_reasons': {}
        }
    }
    
    for i, seq in enumerate(sequences):
        seq_info = {
            'index': i,
            'sequence': seq,
            'length': len(seq),
            'gc_content': SequenceToolkit.gc_content(seq),
            'n_percent': (seq.count('N') / len(seq) * 100) if seq else 0,
            'passed': True,
            'fail_reasons': []
        }
        
        # 质量检查
        if seq_info['length'] < min_length:
            seq_info['passed'] = False
            seq_info['fail_reasons'].append('too_short')
        
        if seq_info['n_percent'] > max_n_percent:
            seq_info['passed'] = False
            seq_info['fail_reasons'].append('too_many_ns')
        
        if not (min_gc <= seq_info['gc_content'] <= max_gc):
            seq_info['passed'] = False
            seq_info['fail_reasons'].append('gc_out_of_range')
        
        # 分类存储
        if seq_info['passed']:
            results['passed'].append(seq_info)
            results['stats']['passed_count'] += 1
        else:
            results['failed'].append(seq_info)
            for reason in seq_info['fail_reasons']:
                results['stats']['failed_reasons'][reason] = results['stats']['failed_reasons'].get(reason, 0) + 1
    
    return results

# 使用示例
test_sequences = [
    "ATGCGATCGATCGATCG",     # 正常序列
    "ATGC",                  # 太短
    "NNNNATGCNNNNGCTANNN",   # N太多
    "AAAAAAAAAAAAAAA",       # GC含量过低
    "GCGCGCGCGCGCGCGC"       # 正常序列
]

qc_results = sequence_quality_pipeline(test_sequences)

print(f"质控结果：")
print(f"总序列数: {qc_results['stats']['total']}")
print(f"通过: {qc_results['stats']['passed_count']}")
print(f"失败: {len(qc_results['failed'])}")
print(f"失败原因: {qc_results['stats']['failed_reasons']}")
```

## 📝 本章总结

### 🎯 核心概念回顾

| 概念 | 作用 | 生物学类比 | 使用场景 |
|------|------|------------|----------|
| **函数定义** | `def function():` | 制定SOP | 封装重复操作 |
| **参数** | 输入数据 | 实验材料 | 灵活处理不同数据 |
| **返回值** | 输出结果 | 实验产物 | 获取处理结果 |
| **文档字符串** | 函数说明 | SOP说明书 | 代码文档化 |
| **局部变量** | 函数内变量 | 实验台用品 | 避免变量冲突 |
| **全局变量** | 程序级变量 | 公共试剂 | 共享常量数据 |

### 💡 最佳实践建议

1. **函数设计原则**
   - 单一职责：一个函数只做一件事
   - 命名清晰：动词+名词的组合
   - 参数合理：必需参数在前，可选参数在后
   - 返回一致：同一函数的返回类型应一致

2. **文档规范**
   - 写清楚函数的作用
   - 详细描述参数和返回值
   - 提供使用示例
   - 说明异常情况

3. **错误处理**
   - 验证输入参数
   - 处理边界情况
   - 提供清晰的错误信息
   - 使用适当的异常类型

### 🚀 实际应用场景

函数在生物信息学中的核心应用：

- **序列分析**：GC含量、反向互补、翻译
- **质量控制**：数据过滤、异常检测
- **格式转换**：FASTA、GenBank、JSON互转
- **统计分析**：描述性统计、假设检验
- **可视化**：绘图函数、报告生成
- **管道构建**：分析流程自动化

## 🎓 练习任务预览

本章配套了精心设计的练习题：

### ⭐ 练习1：基础函数创建
创建DNA序列基本分析函数，掌握函数定义和参数设计。

### ⭐⭐ 练习2：序列格式转换
实现FASTA格式解析和生成，学习字符串处理和文件操作。

### ⭐⭐⭐ 练习3：ORF预测工具
构建完整的开放阅读框预测器，综合运用函数组合。

### ⭐⭐ 练习4：质量控制管道
设计序列质量控制流水线，实践工程化思维。

### ⭐⭐⭐ 练习5：序列分析工具包
创建综合的序列分析工具库，体验模块化编程。

## 🌟 下一步学习

恭喜你掌握了函数编程的精髓！

下一章（Chapter 05：文件操作）将学习如何：
- 📁 读写各种生物信息学文件格式
- 🔄 批量处理大型数据集
- 💾 数据持久化和缓存策略
- 🛡️ 文件操作的安全性和健壮性

就像学会了标准实验操作，现在要学习如何管理实验数据和记录！

---

*"好的函数就像好的实验协议——清晰、可重复、可靠。掌握了函数，你就掌握了编程的重要思维方式。"*

**—— 你的生物信息学导师**