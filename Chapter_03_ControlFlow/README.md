# Chapter 03: 控制流 - 给程序装上"大脑"的决策系统

## 📬 写在最前面：给生物学研究者的一封信

亲爱的研究者：

还记得你第一次设计PCR引物时的紧张吗？
"退火温度应该设多少度？" "如果引物有二聚体怎么办？" "GC含量太高要不要重新设计？"

每一步都需要判断，每个决定都影响结果。这就是**控制流**——程序的决策系统。

控制流让程序从"死板的食谱"变成"智能的助手"。就像一个经验丰富的实验员，知道什么时候该做什么，什么情况下要调整方案。

## 🗺️ 本章导航

### 🎯 学习目标清单

完成本章后，你将能够：

✅ **条件判断（if语句）** - 根据序列质量自动筛选数据，判断基因是否含有特定motif
✅ **循环遍历（for循环）** - 批量处理测序数据，逐个分析基因列表
✅ **条件循环（while循环）** - 持续搜索直到找到目标，监测实验条件
✅ **流程控制（break/continue）** - 提前终止计算，跳过不符合条件的数据

### 📊 知识结构图

```
控制流知识体系
├── 条件判断 (if/elif/else)
├── 循环结构 (for/while)
├── 流程控制 (break/continue/pass)
└── 嵌套结构与综合应用
```

### 🧭 学习路径

```
第1站：条件判断 if语句（20分钟）
    ↓
第2站：for循环 - 批量处理（25分钟）
    ↓
第3站：while循环 - 条件监测（15分钟）
    ↓
第4站：流程控制 - 精细调控（10分钟）
    ↓
第5站：综合应用 - 构建分析流程（15分钟）
```

## 🔬 为什么需要控制流？

### 真实的研究场景

想象你有10,000条测序reads需要质控：

```
手动方法（痛苦）：
- 打开Excel，逐条查看质量分数
- 手动删除低质量序列
- 耗时：8小时，错误率：高

程序方法（轻松）：
for read in all_reads:
    if quality_score >= 30:
        保留这条序列
    else:
        丢弃这条序列
# 耗时：5秒，错误率：0
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

## 🎭 第1站：if语句 - 让程序学会判断

### 1.1 概念引入：什么是条件判断？

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

### 1.2 基础语法

```python
# 基本结构
if 条件:
    执行这些操作  # 注意缩进！
    
# 为什么要缩进？
# 缩进表示"属于"关系，就像实验步骤的子步骤
```

### 1.3 单分支if：简单的是/否判断

#### 示例1：检查PCR产物长度

```python
# 检查PCR产物长度是否正确
pcr_product = "ATGCGATCGATCGATCGATCGATCG"
expected_length = 25

print(f"实际长度: {len(pcr_product)} bp")
print(f"预期长度: {expected_length} bp")

if len(pcr_product) == expected_length:
    print("✅ PCR成功！产物长度正确")
```

#### 示例2：DNA纯度检查

```python
# Nanodrop测定结果
concentration = 150  # ng/μL
ratio_260_280 = 1.82  # 纯度指标

if concentration >= 50:
    print("✅ 浓度合格，可用于测序")

if 1.8 <= ratio_260_280 <= 2.0:
    print("✅ 纯度良好，无蛋白污染")
```

### 1.4 双分支if-else：二选一决策

#### 示例3：酶切位点检查

```python
# 检查序列中是否含有EcoRI位点
plasmid = "ATGCGAATTCGATCG"
ecori_site = "GAATTC"

if ecori_site in plasmid:
    position = plasmid.find(ecori_site)
    print(f"✅ 发现EcoRI位点在位置 {position}")
else:
    print("❌ 未发现EcoRI位点，需要选择其他限制酶")
```

### 1.5 多分支if-elif-else：多重选择

#### 示例4：测序质量分级

```python
# Illumina测序的Phred质量分数评估
quality_score = 35

if quality_score >= 40:
    print("⭐ 极高质量 (错误率 < 0.01%)")
elif quality_score >= 30:
    print("✅ 高质量 (错误率 < 0.1%)")
elif quality_score >= 20:
    print("⚠️ 中等质量 (错误率 < 1%)")
else:
    print("❌ 极低质量，建议丢弃")
```

### 1.6 复合条件：and、or、not

#### 示例5：引物设计标准

```python
# 检查引物是否合格
primer = "ATGGCGATCGATCGATCGAT"
length = len(primer)
gc_content = (primer.count('G') + primer.count('C')) / length * 100

print(f"引物: {primer}")
print(f"长度: {length} bp, GC含量: {gc_content:.1f}%")

# 检查多个条件
if 18 <= length <= 25 and 40 <= gc_content <= 60:
    print("✅ 引物设计合格")
else:
    print("❌ 引物需要重新设计")
    if not (18 <= length <= 25):
        print("   - 长度不合适 (应该18-25bp)")
    if not (40 <= gc_content <= 60):
        print("   - GC含量不合适 (应该40-60%)")
```

## 🔄 第2站：for循环 - 批量处理的利器

### 2.1 概念引入：什么是for循环？

for循环就像：
- 96孔板加样：对每个孔执行相同操作
- 批量DNA提取：每个样品走相同流程
- 显微镜计数：逐个视野统计细胞

```
96孔板 → for孔 in 所有孔:
            加入50μL试剂
```

### 2.2 基础语法：遍历序列

#### 示例6：逐个碱基分析

```python
# 分析DNA序列组成
dna = "ATGCGATCG"

print(f"分析序列: {dna}")
for base in dna:
    bond_type = "2个氢键" if base in "AT" else "3个氢键"
    print(f"  {base} - {bond_type}")
```

#### 示例7：批量样品处理

```python
# 处理多个样品的浓度标准化
samples = ["Sample_A", "Sample_B", "Sample_C"]
concentrations = [150, 230, 180]  # ng/μL

print("DNA标准化结果:")
for i in range(len(samples)):
    sample = samples[i]
    conc = concentrations[i]
    dilution = conc / 100  # 目标：100 ng/μL
    
    print(f"{sample}: {conc} ng/μL → 稀释{dilution:.1f}x")
```

### 2.3 range()函数：控制循环次数

#### 示例8：PCR扩增模拟

```python
# 模拟PCR扩增
initial_copies = 100
cycles = 5

copies = initial_copies
for cycle in range(1, cycles + 1):
    copies *= 2  # 每个循环翻倍
    print(f"第{cycle}轮循环后: {copies:,} 个拷贝")

print(f"扩增倍数: {copies/initial_copies:.0f}x")
```

### 2.4 嵌套for循环：多维处理

#### 示例9：三个阅读框扫描

```python
# 在三个阅读框中搜索起始密码子ATG
dna = "CCATGGCATGAAATGTAG"

for frame in range(3):
    print(f"阅读框 {frame}:")
    for i in range(frame, len(dna) - 2, 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            if codon == "ATG":
                print(f"  ✓ 发现ATG在位置 {i}")
    print()
```

### 2.5 列表推导式：简洁的for循环

```python
# 序列处理的不同方法对比
sequences = ["ATGC", "CGTA", "GGCC"]

# 传统for循环
reverse_seqs = []
for seq in sequences:
    reverse_seqs.append(seq[::-1])

# 列表推导式（更简洁）
reverse_seqs2 = [seq[::-1] for seq in sequences]

# 带条件的过滤
gc_rich = [seq for seq in sequences 
           if (seq.count('G') + seq.count('C'))/len(seq) > 0.5]

print("原始序列:", sequences)
print("反向序列:", reverse_seqs2)  
print("GC富集序列:", gc_rich)
```

## ⏰ 第3站：while循环 - 条件监测器

### 3.1 概念引入：什么是while循环？

while循环就像：
- 细胞培养：密度未到80%就继续培养
- 透析：电导率未降到阈值就继续换液
- PCR：温度未到就继续加热

```python
while 细胞密度 < 80%:
    继续培养
    每天检查
```

### 3.2 基础while循环

#### 示例10：搜索第一个ATG

```python
# 搜索下一个ATG起始密码子
sequence = "CCGATCCATGAAATGCCCTAG"
position = 0

while position <= len(sequence) - 3:
    codon = sequence[position:position+3]
    if codon == "ATG":
        print(f"✓ 找到ATG在位置 {position}")
        break  # 找到第一个就停止
    position += 1

if position > len(sequence) - 3:
    print("未找到ATG")
```

#### 示例11：迭代优化算法

```python
# 二分法找最佳pH值
target_activity = 100
ph_low, ph_high = 6.0, 8.0
tolerance = 0.1
iteration = 0

while ph_high - ph_low > tolerance:
    iteration += 1
    ph_mid = (ph_low + ph_high) / 2
    
    # 模拟酶活性（假设最佳pH是7.2）
    activity = 100 - abs(ph_mid - 7.2) * 50
    
    print(f"迭代{iteration}: pH={ph_mid:.2f}, 活性={activity:.1f}")
    
    if activity < target_activity:
        if ph_mid < 7.2:
            ph_low = ph_mid
        else:
            ph_high = ph_mid
    else:
        break

print(f"最佳pH: {ph_mid:.2f}, 总迭代: {iteration}次")
```

## 🎮 第4站：流程控制 - break、continue和pass

### 4.1 break：紧急刹车

#### 示例12：数据库搜索

```python
# 在多个数据库中搜索基因，找到就停止
databases = {
    "GenBank": ["BRCA1", "TP53", "EGFR"],
    "RefSeq": ["MYC", "KRAS", "BRCA2"],
    "Ensembl": ["BRAF", "BRCA1", "APC"]
}

target_gene = "BRCA1"
found = False

for db_name, genes in databases.items():
    print(f"搜索 {db_name}...")
    if target_gene in genes:
        print(f"  ✓ 找到了！{target_gene} 在 {db_name}")
        found = True
        break  # 找到就立即停止
    else:
        print(f"  未找到")

print("搜索完成" if found else "未找到目标基因")
```

### 4.2 continue：跳过当前

#### 示例13：质量控制过滤

```python
# 跳过低质量序列
sequences = [
    {"id": "seq1", "quality": 35, "dna": "ATGCGATC"},
    {"id": "seq2", "quality": 10, "dna": "NNNNNNNN"},  # 低质量
    {"id": "seq3", "quality": 38, "dna": "ATGGCGTA"},
]

processed_count = 0
for seq in sequences:
    if seq["quality"] < 30:
        print(f"⚠️ 跳过 {seq['id']}: 质量太低")
        continue  # 跳过后面的处理步骤
    
    # 只处理高质量序列
    gc_content = (seq["dna"].count('G') + seq["dna"].count('C')) / len(seq["dna"]) * 100
    print(f"✅ 处理 {seq['id']}: GC={gc_content:.1f}%")
    processed_count += 1

print(f"处理完成: {processed_count} 条序列")
```

### 4.3 pass：占位符

```python
# 构建程序框架
def analyze_sequence(sequence):
    print(f"分析序列: {sequence}")
    
    if len(sequence) < 10:
        print("  ⚠️ 序列太短")
        pass  # TODO: 添加详细的质量检查
    else:
        print("  ✓ 长度检查通过")
    
    # TODO: 添加更多分析功能
    pass
    
    return "分析完成"
```

## 🔧 第5站：综合应用 - 构建完整的分析流程

### 实战项目：多序列质控分析系统

```python
def sequence_quality_control():
    """综合示例：构建序列质控系统"""
    print("=" * 50)
    print("多序列质控分析系统 v1.0")
    print("=" * 50)
    
    # 模拟测序数据
    sequences = [
        {"id": "READ001", "seq": "ATGGCGATCGATCGATCGTAG", "qual": 38},
        {"id": "READ002", "seq": "NATGCCNNNATCGATCGATCG", "qual": 25},
        {"id": "READ003", "seq": "ATGAAACCCTAGATGGGGTAA", "qual": 42},
        {"id": "READ004", "seq": "CCGATGGCGATCGATCGATCG", "qual": 35},
    ]
    
    # 分析参数
    min_quality = 30
    max_n_percent = 10
    target_motif = "GATC"
    
    print(f"\n📋 分析参数:")
    print(f"  • 最低质量分数: Q{min_quality}")
    print(f"  • 最大N含量: {max_n_percent}%")
    print(f"  • 搜索motif: {target_motif}")
    
    # 存储结果
    passed_sequences = []
    failed_sequences = []
    motif_containing = []
    
    # 主分析循环
    for seq_data in sequences:
        seq_id = seq_data["id"]
        sequence = seq_data["seq"]
        quality = seq_data["qual"]
        
        print(f"\n分析 {seq_id} (Q{quality}):")
        
        # 质量控制
        passed_qc = True
        reasons = []
        
        if quality < min_quality:
            passed_qc = False
            reasons.append(f"质量低于Q{min_quality}")
        
        # 检查N含量
        n_percent = (sequence.count('N') / len(sequence)) * 100
        if n_percent > max_n_percent:
            passed_qc = False
            reasons.append(f"N含量{n_percent:.1f}%超标")
        
        if passed_qc:
            print("  ✅ 通过质控")
            passed_sequences.append(seq_data)
            
            # 计算GC含量
            gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
            print(f"  📊 GC含量: {gc_content:.1f}%")
            
            # 搜索motif
            if target_motif in sequence:
                motif_containing.append(seq_id)
                positions = [i for i in range(len(sequence)) 
                           if sequence[i:i+len(target_motif)] == target_motif]
                print(f"  🔍 发现motif在位置: {positions}")
        else:
            print(f"  ❌ 未通过质控: {', '.join(reasons)}")
            failed_sequences.append(seq_data)
    
    # 生成报告
    print(f"\n📈 分析报告:")
    print(f"  • 通过质控: {len(passed_sequences)}/{len(sequences)}")
    print(f"  • 含有motif: {len(motif_containing)} 条")
    print(f"  • 高质量序列ID: {[s['id'] for s in passed_sequences]}")
    
    return passed_sequences

# 运行分析
results = sequence_quality_control()
```

## 🐛 常见错误与调试技巧

### 语法错误

```python
# ❌ 错误：忘记冒号
# if x > 0  # SyntaxError!

# ✅ 正确
if x > 0:  # 记得加冒号
    print("positive")

# ❌ 错误：缩进错误  
# if x > 0:
# print("positive")  # IndentationError!

# ✅ 正确
if x > 0:
    print("positive")  # 使用4个空格缩进
```

### 逻辑错误

```python
# ❌ 无限循环
# count = 0
# while count < 10:
#     print(count)  # 忘记更新count！

# ✅ 正确
count = 0
while count < 10:
    print(count)
    count += 1  # 记得更新循环变量
```

### 调试技巧

```python
# 技巧1：使用print调试
sequence = "ATGCGATC"
for i in range(len(sequence)):
    print(f"Debug: i={i}, base={sequence[i]}")  # 查看循环状态

# 技巧2：分步执行复杂条件
gc_content = 45
length = 20

gc_ok = 40 < gc_content < 60
length_ok = 18 <= length <= 25

print(f"GC检查: {gc_ok}, 长度检查: {length_ok}")

if gc_ok and length_ok:
    print("引物合格")
```

## 📝 本章总结

### 🎯 核心概念回顾

| 概念 | 语法 | 生物学类比 | 使用场景 |
|------|------|------------|----------|
| **if语句** | `if 条件:` | 实验决策点 | 质量控制、数据筛选 |
| **if-else** | `if-else:` | 二选一判断 | 阳性/阴性检测 |
| **for循环** | `for item in sequence:` | 96孔板操作 | 批量处理数据 |
| **while循环** | `while 条件:` | 培养监测 | 条件搜索 |
| **break** | `break` | 紧急停止 | 找到目标即停 |
| **continue** | `continue` | 跳过当前 | 过滤无效数据 |

### 💡 最佳实践建议

1. **选择合适的控制结构**
   - 已知次数 → for循环
   - 条件未知 → while循环
   - 多重选择 → if-elif-else

2. **代码可读性**
   - 使用有意义的变量名
   - 保持一致的缩进（4个空格）
   - 适当添加注释说明逻辑

3. **避免常见陷阱**
   - while循环必须有退出条件
   - 注意序列索引边界
   - 区分`=`(赋值)和`==`(比较)

4. **性能优化技巧**
   - 将最可能的条件放在前面
   - 使用break避免不必要的循环
   - 考虑列表推导式简化代码

### 🚀 实际应用场景

控制流在生物信息学中的核心应用：

- **基因组注释**: 扫描基因组寻找编码区域
- **序列比对**: 找最佳匹配位置  
- **质量控制**: 过滤低质量测序数据
- **模式搜索**: 查找酶切位点、motif
- **数据预处理**: 批量格式转换和清洗
- **统计分析**: 差异表达基因筛选

## 🎓 练习任务预览

本章配套了精心设计的练习题：

### ⭐ 练习1：序列质量过滤
筛选高质量测序reads，掌握if判断和for循环基础。

### ⭐⭐ 练习2：限制酶切位点搜索  
在DNA序列中查找多个酶切位点，练习字符串搜索。

### ⭐⭐⭐ 练习3：ORF预测器
找出最长的开放阅读框，掌握嵌套循环应用。

### ⭐⭐ 练习4：滑动窗口GC分析
分析GC含量分布，学习窗口算法思想。

### ⭐⭐⭐ 练习5：密码子频率统计
统计密码子使用偏好，为后续数据结构学习铺垫。

## 🌟 下一步学习

恭喜你掌握了程序的"大脑"——控制流！

下一章（Chapter 04：函数）将学习如何：
- 📦 把重复代码封装成函数（像实验室SOP）
- 🔧 创建自己的生信工具箱
- 📐 让代码更模块化、可重用
- 🎯 提高程序的专业性和可维护性

就像把常用实验流程写成标准操作规程，函数让我们能一次编写、多次使用，让程序更清晰、更专业！

---

*"编程就像做实验，需要严谨的逻辑和清晰的流程。掌握了控制流，你就掌握了让程序'思考'的能力。"*

**—— 你的生物信息学导师**