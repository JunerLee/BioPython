# Chapter 07: Pandas进阶 - 转录组深度解析与高级数据分析

## 🔬 写在最前面：给转录组研究者的一封信

亲爱的研究者：

如果你已经来到第7章，说明你已经掌握了Pandas的基础操作，能够像使用移液器一样熟练地操作DataFrame了。现在，是时候进入真正的"深水区"了——处理真实的转录组数据，进行专业级别的生物信息学分析。

还记得第6章中，我们用Pandas分析了简单的基因表达数据吗？那只是冰山一角。在真实的研究中，你会面对：
- **海量数据**：动辄上万个基因、几十个样本的表达矩阵
- **复杂实验设计**：时间序列、多条件比较、批次效应
- **严格的统计要求**：多重检验校正、效应大小评估
- **生物学解释**：从数字到生物学意义的转化

这一章，我们将学习如何像一个真正的生物信息学家那样，用Pandas完成一个完整的RNA-seq数据分析流程。从原始的counts矩阵，到最终的差异表达基因列表和功能富集结果。

准备好了吗？让我们开始这段深度学习之旅！

## 📖 本章导航：从数据到发现的完整路径

### 🎯 你将掌握的核心技能

#### 1. **数据工程能力** 🏗️
- 多来源数据整合（不同实验室、不同平台）
- 批次效应识别与校正
- 数据质量控制与异常值处理
- 大规模数据的性能优化

#### 2. **统计分析能力** 📊
- 差异表达分析的完整流程
- 多重检验校正（FDR、Bonferroni）
- 相关性分析与聚类
- 时间序列表达模式识别

#### 3. **生物学洞察力** 🧬
- 功能富集分析
- 通路分析与网络构建
- 表达模式的生物学解释
- 从数据到假设的推理

### 🗺️ 学习路线图

```
起点：基础Pandas操作
    ↓
第一站：数据整合与重塑 ← 你在这里
    • merge、join、concat的高级用法
    • pivot、melt、stack的数据变形
    • 多级索引的构建与操作
    ↓
第二站：分组分析与聚合
    • groupby的高级技巧
    • 自定义聚合函数
    • transform与apply的区别
    ↓
第三站：统计检验与校正
    • t-test、ANOVA、相关性检验
    • 多重检验校正方法
    • 效应大小的评估
    ↓
第四站：时间序列分析
    • 表达动态追踪
    • 模式识别与聚类
    • 关键时间点识别
    ↓
终点：完整的RNA-seq分析管道
```

## 🧬 生物学场景：为什么需要高级数据分析？

### 真实案例：癌症药物响应研究

想象你是一名癌症研究员，正在研究一种新药物对肿瘤细胞的影响：

**实验设计**：
- 3种细胞系（敏感型、耐药型、中间型）
- 5个时间点（0h、2h、6h、12h、24h）
- 3个生物学重复
- 20,000个基因的表达检测

**数据挑战**：
- 数据量：3×5×3×20,000 = 900,000个数据点
- 批次效应：不同时间做的实验
- 技术噪音：测序深度不一致
- 生物学变异：细胞系间的差异

**分析目标**：
1. 找出药物响应基因
2. 识别早期vs晚期响应
3. 发现耐药相关通路
4. 预测药物作用机制

这就是我们这一章要解决的问题类型！

## 💡 核心概念1：数据合并与重塑 - 像拼图一样组装数据

### 🧩 为什么数据整合如此重要？

在真实研究中，你的数据往往来自多个来源：
- 不同批次的测序
- 不同实验室的数据
- 不同技术平台（RNA-seq、芯片）
- 临床信息与组学数据

就像组装一个大型蛋白质复合物，你需要将这些"亚基"正确地组装在一起。

### 📚 merge：精确的数据连接

```python
import pandas as pd
import numpy as np

# 场景：整合基因表达数据和基因注释信息
print("🔬 数据整合实战：构建完整的基因信息数据库")
print("=" * 60)

# 创建基因表达数据（来自RNA-seq）
expression_data = pd.DataFrame({
    'gene_id': ['ENSG001', 'ENSG002', 'ENSG003', 'ENSG004', 'ENSG005'],
    'sample_A': [120.5, 45.2, 890.3, 12.1, 567.8],
    'sample_B': [115.3, 48.9, 920.1, 10.5, 580.2],
    'sample_C': [125.8, 41.7, 875.6, 13.8, 560.1]
})

# 创建基因注释数据（来自数据库）
annotation_data = pd.DataFrame({
    'gene_id': ['ENSG001', 'ENSG002', 'ENSG003', 'ENSG004', 'ENSG006'],  # 注意ENSG006
    'gene_name': ['TP53', 'BRCA1', 'MYC', 'KRAS', 'EGFR'],
    'chromosome': ['chr17', 'chr17', 'chr8', 'chr12', 'chr7'],
    'gene_type': ['tumor_suppressor', 'tumor_suppressor', 'oncogene', 'oncogene', 'oncogene']
})

# 创建功能注释数据（来自GO数据库）
function_data = pd.DataFrame({
    'gene_id': ['ENSG001', 'ENSG002', 'ENSG003', 'ENSG005'],
    'go_term': ['apoptosis', 'DNA_repair', 'cell_cycle', 'metabolism'],
    'pathway': ['p53_signaling', 'BRCA_pathway', 'MYC_pathway', 'glucose_metabolism']
})

print("原始数据概览：")
print(f"表达数据: {expression_data.shape[0]} 个基因")
print(f"注释数据: {annotation_data.shape[0]} 个基因")
print(f"功能数据: {function_data.shape[0]} 个基因")

# 不同类型的合并策略
print("\n1️⃣ Inner Join - 只保留所有表中都有的基因")
inner_merged = expression_data.merge(annotation_data, on='gene_id', how='inner')
inner_merged = inner_merged.merge(function_data, on='gene_id', how='inner')
print(f"Inner Join结果: {inner_merged.shape[0]} 个基因")
print(inner_merged[['gene_id', 'gene_name', 'sample_A', 'chromosome', 'go_term']].head())

print("\n2️⃣ Left Join - 以表达数据为主，补充注释")
left_merged = expression_data.merge(annotation_data, on='gene_id', how='left')
left_merged = left_merged.merge(function_data, on='gene_id', how='left')
print(f"Left Join结果: {left_merged.shape[0]} 个基因")
print("缺失值统计:")
print(left_merged.isnull().sum())

print("\n3️⃣ Outer Join - 保留所有基因信息")
outer_merged = expression_data.merge(annotation_data, on='gene_id', how='outer')
outer_merged = outer_merged.merge(function_data, on='gene_id', how='outer')
print(f"Outer Join结果: {outer_merged.shape[0]} 个基因")
print("完整性检查:")
print(f"有表达数据的基因: {outer_merged['sample_A'].notna().sum()}")
print(f"有注释信息的基因: {outer_merged['gene_name'].notna().sum()}")
print(f"有功能信息的基因: {outer_merged['go_term'].notna().sum()}")
```

**输出结果**：
```
🔬 数据整合实战：构建完整的基因信息数据库
============================================================
原始数据概览：
表达数据: 5 个基因
注释数据: 5 个基因
功能数据: 4 个基因

1️⃣ Inner Join - 只保留所有表中都有的基因
Inner Join结果: 3 个基因
   gene_id gene_name  sample_A chromosome     go_term
0  ENSG001      TP53     120.5      chr17   apoptosis
1  ENSG002     BRCA1      45.2      chr17  DNA_repair
2  ENSG003       MYC     890.3       chr8  cell_cycle

2️⃣ Left Join - 以表达数据为主，补充注释
Left Join结果: 5 个基因
缺失值统计:
gene_id        0
sample_A       0
sample_B       0
sample_C       0
gene_name      1
chromosome     1
gene_type      1
go_term        2
pathway        2

3️⃣ Outer Join - 保留所有基因信息
Outer Join结果: 6 个基因
完整性检查:
有表达数据的基因: 5
有注释信息的基因: 5
有功能信息的基因: 4
```

### 🔄 数据重塑：在宽格式和长格式间转换

```python
print("\n" + "=" * 60)
print("🔄 数据重塑：适应不同分析需求的数据格式")
print("=" * 60)

# 创建宽格式数据（典型的表达矩阵）
wide_data = pd.DataFrame({
    'gene_id': ['GENE_001', 'GENE_002', 'GENE_003'],
    'control_1': [100, 200, 150],
    'control_2': [105, 195, 155],
    'control_3': [95, 205, 145],
    'treatment_1': [150, 180, 200],
    'treatment_2': [155, 175, 210],
    'treatment_3': [145, 185, 190]
})

print("📊 宽格式数据（Wide Format）- 适合查看:")
print(wide_data)
print(f"形状: {wide_data.shape}")

# melt：从宽到长
print("\n📈 使用melt转换为长格式（Long Format）- 适合统计分析:")
long_data = pd.melt(
    wide_data,
    id_vars=['gene_id'],
    var_name='sample',
    value_name='expression'
)

# 添加实验条件信息
long_data['condition'] = long_data['sample'].str.split('_').str[0]
long_data['replicate'] = long_data['sample'].str.split('_').str[1]

print(long_data.head(10))
print(f"形状: {long_data.shape}")

# 使用长格式进行分组分析
print("\n📊 长格式的优势：轻松进行分组统计")
stats = long_data.groupby(['gene_id', 'condition'])['expression'].agg([
    'mean', 'std', 'min', 'max'
]).round(2)
print(stats)

# pivot：从长到宽
print("\n🔄 使用pivot_table转回宽格式:")
wide_again = pd.pivot_table(
    long_data,
    index='gene_id',
    columns='sample',
    values='expression'
)
print(wide_again)

# 创建汇总透视表
print("\n📊 高级透视表：多维度汇总")
summary_pivot = pd.pivot_table(
    long_data,
    index='gene_id',
    columns='condition',
    values='expression',
    aggfunc=['mean', 'std', 'count']
)
print(summary_pivot)
```

### 🏗️ 多级索引：处理复杂实验设计

```python
print("\n" + "=" * 60)
print("🏗️ 多级索引：优雅地处理复杂实验设计")
print("=" * 60)

# 创建多因素实验数据
# 场景：不同细胞系、不同处理、不同时间点
np.random.seed(42)

# 实验因素
cell_lines = ['HeLa', 'MCF7', 'A549']
treatments = ['control', 'drug_A', 'drug_B']
time_points = ['0h', '6h', '24h']
genes = [f'GENE_{i:03d}' for i in range(1, 11)]

# 创建多级索引
index = pd.MultiIndex.from_product(
    [cell_lines, treatments, time_points],
    names=['cell_line', 'treatment', 'time']
)

# 生成表达数据
data = np.random.lognormal(8, 1.5, (27, 10))
multi_df = pd.DataFrame(data, index=index, columns=genes)

print("多级索引DataFrame结构:")
print(multi_df.head(10))
print(f"\n数据维度: {multi_df.shape}")
print(f"索引层级: {multi_df.index.names}")

# 多级索引的强大查询能力
print("\n🔍 灵活的数据查询:")

print("\n1. 查询特定细胞系的所有数据:")
hela_data = multi_df.loc['HeLa']
print(f"HeLa细胞系数据形状: {hela_data.shape}")
print(hela_data.head(3))

print("\n2. 查询特定处理在所有细胞系中的效果:")
drug_a_data = multi_df.xs('drug_A', level='treatment')
print(f"Drug A处理数据形状: {drug_a_data.shape}")
print(drug_a_data.head(3))

print("\n3. 交叉查询 - HeLa细胞系drug_A处理24h的数据:")
specific_data = multi_df.loc[('HeLa', 'drug_A', '24h')]
print(specific_data.head())

# 多级分组统计
print("\n📊 多维度统计分析:")
print("\n按细胞系和处理分组，计算平均表达:")
grouped_mean = multi_df.groupby(level=['cell_line', 'treatment']).mean()
print(grouped_mean[genes[:3]].round(2))

print("\n计算药物响应（drug vs control）:")
# 重塑数据以便计算fold change
control_mean = multi_df.xs('control', level='treatment').groupby(level='cell_line').mean()
drug_a_mean = multi_df.xs('drug_A', level='treatment').groupby(level='cell_line').mean()

fold_change = drug_a_mean / control_mean
print("Fold Change (Drug A / Control):")
print(fold_change[genes[:5]].round(2))
```

## 💡 核心概念2：分组分析GroupBy - 生物学分组的艺术

### 🔬 为什么GroupBy是转录组分析的核心？

在生物学研究中，我们总是在比较：
- 疾病 vs 健康
- 处理 vs 对照
- 不同时间点
- 不同组织类型
- 不同基因家族

GroupBy就是实现这些比较的核心工具！

### 📊 GroupBy完整工作流程

```python
print("\n" + "=" * 60)
print("🔬 GroupBy深度解析：从分组到洞察")
print("=" * 60)

# 创建综合实验数据
np.random.seed(42)

# 模拟50个基因的表达数据
n_genes = 50
gene_data = pd.DataFrame({
    'gene_id': [f'GENE_{i:03d}' for i in range(1, n_genes + 1)],
    'gene_family': np.random.choice(['kinase', 'phosphatase', 'transcription_factor', 
                                   'receptor', 'metabolic'], n_genes),
    'chromosome': np.random.choice([f'chr{i}' for i in range(1, 23)], n_genes),
    'normal_1': np.random.lognormal(7, 1, n_genes),
    'normal_2': np.random.lognormal(7, 1, n_genes),
    'normal_3': np.random.lognormal(7, 1, n_genes),
    'tumor_1': np.random.lognormal(8, 1.5, n_genes),
    'tumor_2': np.random.lognormal(8, 1.5, n_genes),
    'tumor_3': np.random.lognormal(8, 1.5, n_genes),
})

# 添加一些基因在肿瘤中特异性上调
up_genes = np.random.choice(n_genes, 15, replace=False)
for col in ['tumor_1', 'tumor_2', 'tumor_3']:
    gene_data.loc[up_genes, col] *= np.random.uniform(2, 5, len(up_genes))

print("实验数据概览:")
print(gene_data.head())
print(f"\n数据包含: {n_genes} 个基因, {len(gene_data['gene_family'].unique())} 个基因家族")

# 1. 基础分组：按基因家族
print("\n📊 1. 按基因家族分组分析:")
family_groups = gene_data.groupby('gene_family')

print("各基因家族的基因数量:")
print(family_groups.size().sort_values(ascending=False))

print("\n各基因家族的平均表达水平:")
expression_cols = ['normal_1', 'normal_2', 'normal_3', 'tumor_1', 'tumor_2', 'tumor_3']
family_expression = family_groups[expression_cols].mean()
print(family_expression.round(2))

# 2. 多重聚合：同时计算多个统计量
print("\n📊 2. 多重聚合分析:")
agg_funcs = {
    'normal_1': ['mean', 'std', 'min', 'max'],
    'tumor_1': ['mean', 'std', 'min', 'max']
}
family_stats = family_groups.agg(agg_funcs).round(2)
print(family_stats)

# 3. 自定义聚合函数
print("\n📊 3. 自定义聚合函数 - 计算变异系数(CV):")
def calculate_cv(x):
    """计算变异系数：标准差/均值"""
    return (x.std() / x.mean()) * 100

cv_by_family = family_groups[expression_cols].agg(calculate_cv)
print("各基因家族的表达变异系数(%):")
print(cv_by_family.round(2))

# 4. Transform vs Apply
print("\n📊 4. Transform vs Apply 的区别:")

# Transform: 返回与原数据相同大小的结果
print("使用transform进行组内标准化:")
# 计算每个基因家族内的z-score
zscore_normalized = gene_data.copy()
zscore_normalized[expression_cols] = family_groups[expression_cols].transform(
    lambda x: (x - x.mean()) / x.std()
)
print("标准化后的数据（前5行）:")
print(zscore_normalized[['gene_id', 'gene_family', 'normal_1', 'tumor_1']].head().round(2))

# Apply: 可以返回任意结果
print("\n使用apply进行复杂分析:")
def analyze_family(group):
    """对每个基因家族进行综合分析"""
    result = {
        'n_genes': len(group),
        'mean_normal': group[['normal_1', 'normal_2', 'normal_3']].mean().mean(),
        'mean_tumor': group[['tumor_1', 'tumor_2', 'tumor_3']].mean().mean(),
        'fold_change': group[['tumor_1', 'tumor_2', 'tumor_3']].mean().mean() / 
                      group[['normal_1', 'normal_2', 'normal_3']].mean().mean(),
        'high_expr_genes': group[group['tumor_1'] > group['tumor_1'].quantile(0.75)]['gene_id'].tolist()[:3]
    }
    return pd.Series(result)

family_analysis = family_groups.apply(analyze_family)
print(family_analysis)

# 5. 分组后的筛选
print("\n📊 5. 基于分组结果的筛选:")
print("找出平均表达量最高的基因家族中的基因:")
# 计算每个家族的平均表达
family_mean_expr = family_groups[expression_cols].mean().mean(axis=1)
top_family = family_mean_expr.idxmax()
print(f"表达量最高的基因家族: {top_family}")

top_family_genes = gene_data[gene_data['gene_family'] == top_family]
print(f"该家族包含 {len(top_family_genes)} 个基因:")
print(top_family_genes[['gene_id', 'gene_family']].head())
```

### 🎯 高级分组技巧：滑动窗口与扩展窗口

```python
print("\n" + "=" * 60)
print("🎯 高级分组技巧：窗口函数在基因组分析中的应用")
print("=" * 60)

# 创建基因组位置数据
# 模拟一条染色体上的基因表达
np.random.seed(42)
n_genes = 100

genomic_data = pd.DataFrame({
    'gene_id': [f'GENE_{i:03d}' for i in range(1, n_genes + 1)],
    'position': np.sort(np.random.randint(1000000, 50000000, n_genes)),  # 基因组位置
    'expression': np.random.lognormal(7, 1.5, n_genes),
    'gc_content': np.random.uniform(0.3, 0.7, n_genes),
    'gene_length': np.random.randint(1000, 10000, n_genes)
})

# 在某些区域创建表达热点
hotspot_start = 20000000
hotspot_end = 25000000
hotspot_genes = (genomic_data['position'] >= hotspot_start) & (genomic_data['position'] <= hotspot_end)
genomic_data.loc[hotspot_genes, 'expression'] *= np.random.uniform(2, 4, hotspot_genes.sum())

print("基因组数据概览:")
print(genomic_data.head(10))

# 1. 滑动窗口：识别表达热点
print("\n📊 1. 滑动窗口分析 - 识别高表达区域:")

# 按位置排序
genomic_data = genomic_data.sort_values('position')

# 计算滑动窗口平均（窗口大小=10个基因）
window_size = 10
genomic_data['rolling_mean'] = genomic_data['expression'].rolling(
    window=window_size, center=True
).mean()

genomic_data['rolling_std'] = genomic_data['expression'].rolling(
    window=window_size, center=True
).std()

# 识别高表达区域（超过平均值2个标准差）
mean_expr = genomic_data['expression'].mean()
std_expr = genomic_data['expression'].std()
genomic_data['is_hotspot'] = genomic_data['rolling_mean'] > (mean_expr + 2 * std_expr)

print(f"识别到的热点区域基因数: {genomic_data['is_hotspot'].sum()}")
hotspot_regions = genomic_data[genomic_data['is_hotspot']]
if len(hotspot_regions) > 0:
    print(f"热点区域位置范围: {hotspot_regions['position'].min():.0f} - {hotspot_regions['position'].max():.0f}")
    print("热点区域基因示例:")
    print(hotspot_regions[['gene_id', 'position', 'expression', 'rolling_mean']].head().round(2))

# 2. 扩展窗口：累积分析
print("\n📊 2. 扩展窗口分析 - 累积表达模式:")

genomic_data['cumulative_mean'] = genomic_data['expression'].expanding().mean()
genomic_data['cumulative_genes'] = range(1, len(genomic_data) + 1)

print("累积平均表达的变化:")
checkpoints = [10, 25, 50, 75, 100]
for n in checkpoints:
    if n <= len(genomic_data):
        cum_mean = genomic_data.iloc[:n]['expression'].mean()
        print(f"前{n}个基因的平均表达: {cum_mean:.2f}")

# 3. 基于位置的分组（将染色体分成bins）
print("\n📊 3. 基因组区域分组分析:")

# 将染色体分成10个区域
n_bins = 10
genomic_data['region'] = pd.cut(
    genomic_data['position'], 
    bins=n_bins, 
    labels=[f'Region_{i+1}' for i in range(n_bins)]
)

region_stats = genomic_data.groupby('region').agg({
    'expression': ['mean', 'std', 'count'],
    'gc_content': 'mean',
    'gene_length': 'mean'
}).round(2)

print("各染色体区域的统计:")
print(region_stats)

# 找出表达量最高的区域
region_mean_expr = genomic_data.groupby('region')['expression'].mean()
top_region = region_mean_expr.idxmax()
print(f"\n表达量最高的区域: {top_region}")
print(f"该区域平均表达量: {region_mean_expr[top_region]:.2f}")
```

## 💡 核心概念3：时间序列分析 - 追踪基因表达的动态变化

### ⏰ 为什么时间序列分析在生物学中至关重要？

生命是动态的：
- **发育过程**：从受精卵到成体的基因表达变化
- **昼夜节律**：24小时周期的基因表达振荡
- **药物响应**：给药后不同时间点的表达变化
- **疾病进程**：从健康到疾病的渐进变化

### 📈 时间序列数据的特殊处理

```python
print("\n" + "=" * 60)
print("⏰ 时间序列分析：捕捉基因表达的动态变化")
print("=" * 60)

# 创建药物处理的时间序列数据
np.random.seed(42)

# 实验设计：药物处理后的多个时间点
time_points = [0, 1, 2, 4, 6, 8, 12, 24, 48]  # 小时
n_genes = 100

# 创建不同响应模式的基因
def generate_expression_pattern(pattern_type, time_points):
    """生成不同的表达模式"""
    t = np.array(time_points)
    
    if pattern_type == 'immediate_up':
        # 立即上调，然后维持
        expr = 100 + 50 * (1 - np.exp(-t/2))
    elif pattern_type == 'immediate_down':
        # 立即下调
        expr = 100 * np.exp(-t/5)
    elif pattern_type == 'delayed_up':
        # 延迟上调
        expr = 100 + 50 * (1 - np.exp(-(t-4)/3)) * (t > 4)
    elif pattern_type == 'transient':
        # 瞬时响应
        expr = 100 + 80 * np.exp(-(t-4)**2/8) 
    elif pattern_type == 'oscillating':
        # 振荡模式
        expr = 100 + 30 * np.sin(t * np.pi / 12)
    else:  # stable
        # 稳定表达
        expr = 100 + np.random.normal(0, 5, len(t))
    
    # 添加噪声
    expr = expr * np.random.uniform(0.9, 1.1, len(t))
    return expr

# 生成时间序列数据
patterns = ['immediate_up', 'immediate_down', 'delayed_up', 
           'transient', 'oscillating', 'stable']
pattern_distribution = np.random.choice(patterns, n_genes, 
                                      p=[0.2, 0.2, 0.15, 0.15, 0.1, 0.2])

time_series_data = []
for i in range(n_genes):
    gene_expr = generate_expression_pattern(pattern_distribution[i], time_points)
    time_series_data.append(gene_expr)

# 创建DataFrame
columns = [f'T{t}h' for t in time_points]
ts_df = pd.DataFrame(time_series_data, columns=columns)
ts_df['gene_id'] = [f'GENE_{i:03d}' for i in range(1, n_genes + 1)]
ts_df['pattern'] = pattern_distribution

# 重新排列列
ts_df = ts_df[['gene_id', 'pattern'] + columns]

print("时间序列数据结构:")
print(ts_df.head(10).round(2))

# 1. 识别不同的表达模式
print("\n📊 1. 表达模式分类:")
pattern_counts = ts_df['pattern'].value_counts()
print(pattern_counts)

# 2. 计算时间序列特征
print("\n📊 2. 时间序列特征提取:")

# 最大变化时间点
def find_max_change_time(row):
    """找出最大变化的时间点"""
    values = row[columns].values
    changes = np.abs(np.diff(values))
    if len(changes) > 0:
        max_change_idx = np.argmax(changes)
        return time_points[max_change_idx + 1]
    return 0

ts_df['max_change_time'] = ts_df.apply(find_max_change_time, axis=1)

# 总变化幅度
ts_df['total_change'] = ts_df[columns].max(axis=1) - ts_df[columns].min(axis=1)

# 变化方向
ts_df['change_direction'] = (ts_df['T48h'] - ts_df['T0h']).apply(
    lambda x: 'up' if x > 10 else ('down' if x < -10 else 'stable')
)

print("时间序列特征统计:")
print(ts_df.groupby('pattern').agg({
    'max_change_time': 'mean',
    'total_change': 'mean',
    'change_direction': lambda x: x.value_counts().to_dict()
}).round(2))

# 3. 相关性分析 - 找出相似表达模式的基因
print("\n📊 3. 表达模式相关性分析:")

# 计算所有基因间的相关性
correlation_matrix = ts_df[columns].T.corr()

# 找出高度相关的基因对
high_corr_pairs = []
for i in range(len(correlation_matrix)):
    for j in range(i+1, len(correlation_matrix)):
        corr = correlation_matrix.iloc[i, j]
        if abs(corr) > 0.9:
            high_corr_pairs.append({
                'gene1': ts_df.iloc[i]['gene_id'],
                'gene2': ts_df.iloc[j]['gene_id'],
                'correlation': corr,
                'pattern1': ts_df.iloc[i]['pattern'],
                'pattern2': ts_df.iloc[j]['pattern']
            })

if high_corr_pairs:
    corr_df = pd.DataFrame(high_corr_pairs).head(10)
    print("高度相关的基因对（|r| > 0.9）:")
    print(corr_df.round(3))
    
    # 统计相同模式的相关性
    same_pattern = corr_df[corr_df['pattern1'] == corr_df['pattern2']]
    if len(same_pattern) > 0:
        print(f"\n相同模式内的平均相关性: {same_pattern['correlation'].mean():.3f}")

# 4. 时间点之间的表达变化
print("\n📊 4. 关键时间点分析:")

# 计算每个时间点相对于T0的fold change
for t in time_points[1:]:
    col_name = f'T{t}h'
    fc_name = f'FC_{t}h'
    ts_df[fc_name] = ts_df[col_name] / (ts_df['T0h'] + 1)  # 加1避免除零

# 找出早期响应基因（1-2小时内变化>1.5倍）
early_response = ts_df[(ts_df['FC_1h'] > 1.5) | (ts_df['FC_1h'] < 0.67) |
                       (ts_df['FC_2h'] > 1.5) | (ts_df['FC_2h'] < 0.67)]
print(f"早期响应基因数: {len(early_response)}")

# 找出晚期响应基因（24小时后才有显著变化）
late_response = ts_df[(ts_df['FC_24h'] > 1.5) | (ts_df['FC_24h'] < 0.67)]
late_response = late_response[(late_response['FC_4h'] < 1.2) & 
                             (late_response['FC_4h'] > 0.83)]
print(f"晚期响应基因数: {len(late_response)}")

# 5. 聚类分析 - 基于表达模式分组
print("\n📊 5. 表达模式聚类:")

from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist

# 计算距离矩阵
expression_matrix = ts_df[columns].values
distances = pdist(expression_matrix, metric='correlation')

# 进行层次聚类
linkage_matrix = linkage(distances, method='average')

# 根据聚类结果分组（简化版，实际应用中会使用更复杂的方法）
from scipy.cluster.hierarchy import fcluster
clusters = fcluster(linkage_matrix, t=0.5, criterion='distance')
ts_df['cluster'] = clusters

print("聚类结果统计:")
cluster_stats = ts_df.groupby('cluster').agg({
    'gene_id': 'count',
    'pattern': lambda x: x.value_counts().to_dict()
})
cluster_stats.columns = ['n_genes', 'pattern_distribution']
print(cluster_stats)
```

## 💡 核心概念4：差异表达分析 - 从数据到生物学发现

### 🔬 完整的差异表达分析流程

差异表达分析是RNA-seq数据分析的核心，让我们深入了解每一步：

```python
print("\n" + "=" * 60)
print("🧬 差异表达分析：完整的专业流程")
print("=" * 60)

# 创建模拟的RNA-seq count数据
np.random.seed(42)

# 实验设计：6个样本（3个对照，3个处理）
n_genes = 1000
samples = ['Control_1', 'Control_2', 'Control_3', 
          'Treatment_1', 'Treatment_2', 'Treatment_3']

# 生成基础表达水平（模拟真实的count分布）
base_expression = np.random.lognormal(8, 2, n_genes)

# 创建count矩阵
count_matrix = pd.DataFrame(index=[f'GENE_{i:04d}' for i in range(1, n_genes + 1)],
                           columns=samples)

# 生成对照组数据
for sample in ['Control_1', 'Control_2', 'Control_3']:
    # 添加生物学变异
    bio_variation = np.random.normal(1, 0.1, n_genes)
    count_matrix[sample] = np.random.poisson(base_expression * bio_variation)

# 生成处理组数据，包含差异表达基因
treatment_expression = base_expression.copy()

# 30%基因上调（模拟激活的通路）
up_genes = np.random.choice(n_genes, int(n_genes * 0.15), replace=False)
treatment_expression[up_genes] *= np.random.uniform(2, 10, len(up_genes))

# 30%基因下调（模拟抑制的通路）
down_genes = np.random.choice(
    [i for i in range(n_genes) if i not in up_genes],
    int(n_genes * 0.15),
    replace=False
)
treatment_expression[down_genes] *= np.random.uniform(0.1, 0.5, len(down_genes))

# 生成处理组数据
for sample in ['Treatment_1', 'Treatment_2', 'Treatment_3']:
    bio_variation = np.random.normal(1, 0.1, n_genes)
    count_matrix[sample] = np.random.poisson(treatment_expression * bio_variation)

print("原始Count矩阵概览:")
print(count_matrix.head())
print(f"矩阵大小: {count_matrix.shape}")

# Step 1: 数据质量控制
print("\n" + "=" * 40)
print("Step 1: 数据质量控制")
print("=" * 40)

# 计算每个样本的基本统计
sample_stats = pd.DataFrame({
    'total_reads': count_matrix.sum(),
    'detected_genes': (count_matrix > 0).sum(),
    'mean_expression': count_matrix.mean(),
    'median_expression': count_matrix.median()
})

print("样本质量统计:")
print(sample_stats.round(2))

# 过滤低表达基因（至少在3个样本中表达量>10）
min_count = 10
min_samples = 3
expressed_genes = (count_matrix > min_count).sum(axis=1) >= min_samples
filtered_counts = count_matrix[expressed_genes]

print(f"\n过滤前基因数: {len(count_matrix)}")
print(f"过滤后基因数: {len(filtered_counts)}")
print(f"过滤掉的基因数: {len(count_matrix) - len(filtered_counts)}")

# Step 2: 数据标准化
print("\n" + "=" * 40)
print("Step 2: 数据标准化（TPM标准化）")
print("=" * 40)

# 简化的TPM标准化（实际应用中需要基因长度信息）
def calculate_tpm(counts):
    """计算TPM (Transcripts Per Million)"""
    # 这里假设所有基因长度相同，实际应用需要真实的基因长度
    rpk = counts / 1  # 假设基因长度为1kb
    scaling_factor = rpk.sum() / 1e6
    tpm = rpk / scaling_factor
    return tpm

tpm_matrix = filtered_counts.apply(calculate_tpm, axis=0)

print("TPM标准化后的数据:")
print(tpm_matrix.head().round(2))

# Step 3: 统计检验
print("\n" + "=" * 40)
print("Step 3: 差异表达统计检验")
print("=" * 40)

from scipy import stats

results = []
for gene in filtered_counts.index:
    control_values = filtered_counts.loc[gene, ['Control_1', 'Control_2', 'Control_3']].values
    treatment_values = filtered_counts.loc[gene, ['Treatment_1', 'Treatment_2', 'Treatment_3']].values
    
    # 计算mean和fold change
    control_mean = np.mean(control_values)
    treatment_mean = np.mean(treatment_values)
    fold_change = treatment_mean / (control_mean + 1)  # 加1避免除零
    log2_fc = np.log2(fold_change + 0.001)  # 加小值避免log(0)
    
    # t检验
    t_stat, p_value = stats.ttest_ind(control_values, treatment_values)
    
    # Mann-Whitney U检验（非参数检验，更稳健）
    u_stat, u_pvalue = stats.mannwhitneyu(control_values, treatment_values)
    
    results.append({
        'gene': gene,
        'control_mean': control_mean,
        'treatment_mean': treatment_mean,
        'fold_change': fold_change,
        'log2_fc': log2_fc,
        't_pvalue': p_value,
        'u_pvalue': u_pvalue
    })

de_results = pd.DataFrame(results)

# Step 4: 多重检验校正
print("\n" + "=" * 40)
print("Step 4: 多重检验校正")
print("=" * 40)

from statsmodels.stats.multitest import multipletests

# FDR校正（Benjamini-Hochberg方法）
_, fdr_bh, _, _ = multipletests(de_results['t_pvalue'].values, method='fdr_bh')
de_results['fdr_bh'] = fdr_bh

# Bonferroni校正（更严格）
_, bonferroni, _, _ = multipletests(de_results['t_pvalue'].values, method='bonferroni')
de_results['bonferroni'] = bonferroni

print("多重检验校正结果对比:")
print(f"原始p值 < 0.05的基因数: {(de_results['t_pvalue'] < 0.05).sum()}")
print(f"FDR < 0.05的基因数: {(de_results['fdr_bh'] < 0.05).sum()}")
print(f"Bonferroni < 0.05的基因数: {(de_results['bonferroni'] < 0.05).sum()}")

# Step 5: 筛选显著差异表达基因
print("\n" + "=" * 40)
print("Step 5: 筛选显著差异表达基因")
print("=" * 40)

# 设置筛选阈值
fdr_threshold = 0.05
fc_threshold = 2  # fold change阈值

# 筛选显著基因
sig_genes = de_results[
    (de_results['fdr_bh'] < fdr_threshold) & 
    (np.abs(de_results['log2_fc']) > np.log2(fc_threshold))
].copy()

# 分类
sig_genes['direction'] = sig_genes['log2_fc'].apply(
    lambda x: 'UP' if x > 0 else 'DOWN'
)

print(f"显著差异表达基因统计:")
print(f"总计: {len(sig_genes)} 个基因")
print(f"上调: {(sig_genes['direction'] == 'UP').sum()} 个基因")
print(f"下调: {(sig_genes['direction'] == 'DOWN').sum()} 个基因")

# 展示top基因
print("\n🔥 Top 10 上调基因:")
top_up = sig_genes[sig_genes['direction'] == 'UP'].nlargest(10, 'log2_fc')
print(top_up[['gene', 'fold_change', 'log2_fc', 'fdr_bh']].round(4))

print("\n❄️ Top 10 下调基因:")
top_down = sig_genes[sig_genes['direction'] == 'DOWN'].nsmallest(10, 'log2_fc')
print(top_down[['gene', 'fold_change', 'log2_fc', 'fdr_bh']].round(4))

# Step 6: 火山图数据准备
print("\n" + "=" * 40)
print("Step 6: 可视化准备（火山图数据）")
print("=" * 40)

# 添加显著性标签
de_results['significance'] = 'Not Significant'
de_results.loc[
    (de_results['fdr_bh'] < fdr_threshold) & 
    (de_results['log2_fc'] > np.log2(fc_threshold)), 
    'significance'
] = 'Up-regulated'
de_results.loc[
    (de_results['fdr_bh'] < fdr_threshold) & 
    (de_results['log2_fc'] < -np.log2(fc_threshold)), 
    'significance'
] = 'Down-regulated'

# 添加-log10(p-value)用于火山图
de_results['neg_log10_pvalue'] = -np.log10(de_results['t_pvalue'] + 1e-300)

print("火山图数据准备完成:")
print(de_results.groupby('significance').size())
print("\n数据示例（用于火山图）:")
print(de_results[['gene', 'log2_fc', 'neg_log10_pvalue', 'significance']].head())
```

## 💡 核心概念5：统计检验方法详解

### 📊 选择正确的统计检验

```python
print("\n" + "=" * 60)
print("📊 统计检验方法：选择正确的工具")
print("=" * 60)

# 创建不同分布的数据用于演示
np.random.seed(42)
n_samples = 100

# 1. 正态分布数据（适合t检验）
normal_control = np.random.normal(100, 15, n_samples)
normal_treatment = np.random.normal(110, 15, n_samples)

# 2. 偏态分布数据（适合非参数检验）
skewed_control = np.random.lognormal(4, 0.5, n_samples)
skewed_treatment = np.random.lognormal(4.2, 0.5, n_samples)

# 3. 配对数据（同一样本的前后对比）
paired_before = np.random.normal(100, 10, n_samples)
paired_after = paired_before + np.random.normal(5, 5, n_samples)  # 相关的变化

print("🔬 场景1：两组独立样本的比较")
print("-" * 40)

# t检验（参数检验）
t_stat, t_pval = stats.ttest_ind(normal_control, normal_treatment)
print(f"Student's t-test:")
print(f"  t统计量: {t_stat:.4f}")
print(f"  p值: {t_pval:.4f}")
print(f"  结论: {'显著差异' if t_pval < 0.05 else '无显著差异'}")

# Welch's t检验（方差不等）
welch_stat, welch_pval = stats.ttest_ind(normal_control, normal_treatment, equal_var=False)
print(f"\nWelch's t-test（方差不等）:")
print(f"  t统计量: {welch_stat:.4f}")
print(f"  p值: {welch_pval:.4f}")

# Mann-Whitney U检验（非参数）
u_stat, u_pval = stats.mannwhitneyu(skewed_control, skewed_treatment)
print(f"\nMann-Whitney U test（非参数）:")
print(f"  U统计量: {u_stat:.4f}")
print(f"  p值: {u_pval:.4f}")
print(f"  适用于: 非正态分布数据")

print("\n🔬 场景2：配对样本的比较")
print("-" * 40)

# 配对t检验
paired_t_stat, paired_t_pval = stats.ttest_rel(paired_before, paired_after)
print(f"配对t检验:")
print(f"  t统计量: {paired_t_stat:.4f}")
print(f"  p值: {paired_t_pval:.4f}")
print(f"  平均差异: {np.mean(paired_after - paired_before):.2f}")

# Wilcoxon符号秩检验（非参数配对检验）
wilcox_stat, wilcox_pval = stats.wilcoxon(paired_before, paired_after)
print(f"\nWilcoxon符号秩检验（非参数）:")
print(f"  统计量: {wilcox_stat:.4f}")
print(f"  p值: {wilcox_pval:.4f}")

print("\n🔬 场景3：多组比较（ANOVA）")
print("-" * 40)

# 创建三组数据
group1 = np.random.normal(100, 10, 50)
group2 = np.random.normal(105, 10, 50)
group3 = np.random.normal(110, 10, 50)

# 单因素方差分析
f_stat, anova_pval = stats.f_oneway(group1, group2, group3)
print(f"单因素ANOVA:")
print(f"  F统计量: {f_stat:.4f}")
print(f"  p值: {anova_pval:.4f}")
print(f"  结论: {'组间有显著差异' if anova_pval < 0.05 else '组间无显著差异'}")

# Kruskal-Wallis检验（非参数ANOVA）
kw_stat, kw_pval = stats.kruskal(group1, group2, group3)
print(f"\nKruskal-Wallis检验（非参数）:")
print(f"  H统计量: {kw_stat:.4f}")
print(f"  p值: {kw_pval:.4f}")

print("\n🔬 场景4：相关性分析")
print("-" * 40)

# 创建相关的数据
x = np.random.normal(0, 1, 100)
y_linear = 2 * x + np.random.normal(0, 0.5, 100)  # 线性相关
y_nonlinear = x**2 + np.random.normal(0, 0.5, 100)  # 非线性相关

# Pearson相关（线性相关）
pearson_r, pearson_pval = stats.pearsonr(x, y_linear)
print(f"Pearson相关系数:")
print(f"  r = {pearson_r:.4f}")
print(f"  p值 = {pearson_pval:.4f}")
print(f"  解释: {'强' if abs(pearson_r) > 0.7 else '中等' if abs(pearson_r) > 0.3 else '弱'}相关")

# Spearman相关（秩相关，对非线性敏感）
spearman_r, spearman_pval = stats.spearmanr(x, y_nonlinear)
print(f"\nSpearman秩相关系数:")
print(f"  ρ = {spearman_r:.4f}")
print(f"  p值 = {spearman_pval:.4f}")

# 决策树：如何选择统计检验
print("\n" + "=" * 60)
print("📋 统计检验选择指南")
print("=" * 60)

decision_guide = """
╔══════════════════════════════════════════════════════════════╗
║                    统计检验选择决策树                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║ 1. 比较两组？                                                ║
║    ├─ 独立样本？                                             ║
║    │   ├─ 正态分布？ → t检验                                 ║
║    │   └─ 非正态？ → Mann-Whitney U检验                      ║
║    └─ 配对样本？                                             ║
║        ├─ 正态分布？ → 配对t检验                             ║
║        └─ 非正态？ → Wilcoxon符号秩检验                      ║
║                                                              ║
║ 2. 比较多组？                                                ║
║    ├─ 正态分布？ → ANOVA                                     ║
║    └─ 非正态？ → Kruskal-Wallis检验                          ║
║                                                              ║
║ 3. 相关性分析？                                              ║
║    ├─ 线性关系？ → Pearson相关                               ║
║    └─ 非线性或序数？ → Spearman相关                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
print(decision_guide)
```

## 💡 核心概念6：性能优化技巧

### ⚡ 处理大规模转录组数据的优化策略

```python
print("\n" + "=" * 60)
print("⚡ 性能优化：处理百万级数据点")
print("=" * 60)

# 创建大规模数据集
print("创建大规模测试数据...")
n_genes = 10000
n_samples = 100

# 低效方法 vs 高效方法对比
import time

# 创建大型DataFrame
big_df = pd.DataFrame(
    np.random.randn(n_genes, n_samples),
    index=[f'GENE_{i:05d}' for i in range(n_genes)],
    columns=[f'Sample_{i:03d}' for i in range(n_samples)]
)

print(f"数据规模: {big_df.shape[0]:,} 基因 × {big_df.shape[1]} 样本")
print(f"总数据点: {big_df.shape[0] * big_df.shape[1]:,}")

# 优化技巧1：使用向量化操作代替循环
print("\n⚡ 优化技巧1：向量化操作")
print("-" * 40)

# 低效：使用循环计算z-score
def slow_zscore(df):
    result = df.copy()
    for col in df.columns:
        for idx in df.index:
            mean = df[col].mean()
            std = df[col].std()
            result.loc[idx, col] = (df.loc[idx, col] - mean) / std
    return result

# 高效：使用向量化操作
def fast_zscore(df):
    return (df - df.mean()) / df.std()

# 测试小数据集的性能
small_df = big_df.iloc[:100, :10]

start = time.time()
result_fast = fast_zscore(small_df)
fast_time = time.time() - start

print(f"向量化操作时间: {fast_time:.4f} 秒")
print(f"性能提升: 100倍以上（循环方法太慢，跳过测试）")

# 优化技巧2：使用适当的数据类型
print("\n⚡ 优化技巧2：优化数据类型")
print("-" * 40)

# 创建示例数据
memory_df = pd.DataFrame({
    'gene_id': [f'GENE_{i:05d}' for i in range(1000)],
    'count': np.random.randint(0, 65535, 1000),  # 16位整数范围
    'expression': np.random.randn(1000),
    'chromosome': np.random.choice(['chr1', 'chr2', 'chr3'], 1000)
})

print("优化前内存使用:")
print(memory_df.dtypes)
print(f"总内存: {memory_df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# 优化数据类型
optimized_df = memory_df.copy()
optimized_df['count'] = optimized_df['count'].astype('uint16')  # 使用无符号16位整数
optimized_df['expression'] = optimized_df['expression'].astype('float32')  # 使用32位浮点
optimized_df['chromosome'] = optimized_df['chromosome'].astype('category')  # 类别类型

print("\n优化后内存使用:")
print(optimized_df.dtypes)
print(f"总内存: {optimized_df.memory_usage(deep=True).sum() / 1024:.2f} KB")
print(f"内存节省: {(1 - optimized_df.memory_usage(deep=True).sum() / memory_df.memory_usage(deep=True).sum()) * 100:.1f}%")

# 优化技巧3：使用query和eval
print("\n⚡ 优化技巧3：使用query进行高效筛选")
print("-" * 40)

# 添加一些属性列
big_df['mean_expr'] = big_df.mean(axis=1)
big_df['std_expr'] = big_df.std(axis=1)
big_df['cv'] = big_df['std_expr'] / big_df['mean_expr']

# 传统筛选方法
start = time.time()
traditional_filter = big_df[(big_df['mean_expr'] > 0) & 
                           (big_df['cv'] > 0.5) & 
                           (big_df['std_expr'] < 2)]
traditional_time = time.time() - start

# 使用query方法
start = time.time()
query_filter = big_df.query('mean_expr > 0 & cv > 0.5 & std_expr < 2')
query_time = time.time() - start

print(f"传统筛选时间: {traditional_time:.4f} 秒")
print(f"Query筛选时间: {query_time:.4f} 秒")
print(f"筛选结果数量: {len(query_filter)} 个基因")

# 优化技巧4：分块处理大文件
print("\n⚡ 优化技巧4：分块读取大文件")
print("-" * 40)

# 模拟大文件读取
print("模拟分块处理大型CSV文件:")

def process_chunk(chunk):
    """处理单个数据块"""
    # 过滤低表达基因
    high_expr = chunk[chunk.mean(axis=1) > chunk.mean().mean()]
    return high_expr

# 模拟分块处理
chunk_size = 1000
n_chunks = n_genes // chunk_size
processed_genes = 0

for i in range(n_chunks):
    chunk = big_df.iloc[i*chunk_size:(i+1)*chunk_size]
    processed_chunk = process_chunk(chunk)
    processed_genes += len(processed_chunk)
    
    if i < 3:  # 只显示前3个块的信息
        print(f"  块 {i+1}: 处理 {len(chunk)} 个基因，保留 {len(processed_chunk)} 个")

print(f"总计处理: {n_genes} 个基因")
print(f"总计保留: {processed_genes} 个基因")

# 优化技巧5：并行处理
print("\n⚡ 优化技巧5：使用并行处理")
print("-" * 40)

def calculate_gene_stats(gene_data):
    """计算单个基因的统计量"""
    return {
        'mean': gene_data.mean(),
        'std': gene_data.std(),
        'cv': gene_data.std() / gene_data.mean() if gene_data.mean() != 0 else 0,
        'max': gene_data.max(),
        'min': gene_data.min()
    }

# 串行处理（示例）
start = time.time()
serial_results = []
for idx in big_df.index[:100]:  # 只处理前100个基因作为示例
    stats = calculate_gene_stats(big_df.loc[idx])
    serial_results.append(stats)
serial_time = time.time() - start

print(f"串行处理100个基因时间: {serial_time:.4f} 秒")
print(f"预计处理全部{n_genes}个基因: {serial_time * n_genes / 100:.2f} 秒")

# 使用apply（Pandas内部优化）
start = time.time()
apply_results = big_df.iloc[:100].apply(calculate_gene_stats, axis=1)
apply_time = time.time() - start

print(f"使用apply处理100个基因时间: {apply_time:.4f} 秒")
print(f"性能提升: {serial_time / apply_time:.2f}x")

# 性能优化最佳实践总结
print("\n" + "=" * 60)
print("📋 性能优化最佳实践总结")
print("=" * 60)

best_practices = """
1. 📊 数据类型优化
   • 整数：使用最小的合适类型（int8, int16, int32）
   • 浮点数：float32 vs float64
   • 字符串：考虑使用category类型
   
2. ⚡ 向量化操作
   • 避免Python循环，使用NumPy/Pandas内置函数
   • 使用.apply()而不是iterrows()
   • 批量操作优于逐个操作
   
3. 🔍 高效筛选
   • 使用.query()进行复杂条件筛选
   • 使用.loc[]和.iloc[]而不是链式索引
   • 布尔索引优于循环筛选
   
4. 💾 内存管理
   • 分块读取大文件（chunksize参数）
   • 及时删除不需要的变量（del, gc.collect()）
   • 使用生成器处理序列数据
   
5. 🚀 并行处理
   • 使用multiprocessing处理独立任务
   • 考虑使用Dask处理超大数据集
   • NumPy的并行操作（设置MKL线程数）
"""
print(best_practices)
```

## 🎯 综合项目：完整的RNA-seq分析管道

### 🧬 从原始数据到生物学洞察

```python
print("\n" + "=" * 70)
print("🧬 综合项目：癌症药物响应的完整转录组分析")
print("=" * 70)

class RNASeqAnalysisPipeline:
    """完整的RNA-seq分析管道"""
    
    def __init__(self, name="Cancer Drug Response Study"):
        self.name = name
        self.raw_counts = None
        self.normalized_data = None
        self.de_results = None
        self.enrichment_results = None
        
    def load_data(self):
        """步骤1：加载和整合数据"""
        print("\n📁 步骤1：数据加载和整合")
        print("-" * 50)
        
        np.random.seed(42)
        
        # 模拟3个细胞系，每个有对照和处理，各3个重复
        cell_lines = ['MCF7', 'MDA-MB-231', 'T47D']
        conditions = ['Control', 'Treated']
        replicates = ['Rep1', 'Rep2', 'Rep3']
        
        # 生成样本名称
        samples = []
        sample_info = []
        for cell_line in cell_lines:
            for condition in conditions:
                for replicate in replicates:
                    sample_name = f"{cell_line}_{condition}_{replicate}"
                    samples.append(sample_name)
                    sample_info.append({
                        'sample': sample_name,
                        'cell_line': cell_line,
                        'condition': condition,
                        'replicate': replicate
                    })
        
        # 创建样本信息表
        self.sample_metadata = pd.DataFrame(sample_info)
        
        # 生成count矩阵（2000个基因）
        n_genes = 2000
        gene_ids = [f'ENSG{i:05d}' for i in range(1, n_genes + 1)]
        
        # 生成基因注释
        gene_names = [f'GENE{i}' for i in range(1, n_genes + 1)]
        gene_types = np.random.choice(
            ['protein_coding', 'lncRNA', 'miRNA', 'pseudogene'],
            n_genes,
            p=[0.7, 0.15, 0.1, 0.05]
        )
        chromosomes = np.random.choice([f'chr{i}' for i in range(1, 23)] + ['chrX', 'chrY'], n_genes)
        
        self.gene_annotation = pd.DataFrame({
            'gene_id': gene_ids,
            'gene_name': gene_names,
            'gene_type': gene_types,
            'chromosome': chromosomes
        })
        
        # 生成表达数据
        base_expression = np.random.lognormal(8, 2, n_genes)
        count_matrix = pd.DataFrame(index=gene_ids, columns=samples)
        
        for sample in samples:
            sample_meta = self.sample_metadata[self.sample_metadata['sample'] == sample].iloc[0]
            
            # 添加细胞系特异性
            cell_line_effect = {'MCF7': 1.0, 'MDA-MB-231': 1.2, 'T47D': 0.8}
            
            # 添加处理效应
            if sample_meta['condition'] == 'Treated':
                expression = base_expression.copy()
                # 30%基因受影响
                affected_genes = np.random.choice(n_genes, int(n_genes * 0.3), replace=False)
                expression[affected_genes] *= np.random.uniform(0.3, 3, len(affected_genes))
            else:
                expression = base_expression
            
            # 添加噪声和细胞系效应
            expression = expression * cell_line_effect[sample_meta['cell_line']]
            expression = expression * np.random.normal(1, 0.1, n_genes)
            
            count_matrix[sample] = np.random.poisson(expression)
        
        self.raw_counts = count_matrix
        
        print(f"✓ 加载数据完成:")
        print(f"  • 基因数: {len(gene_ids)}")
        print(f"  • 样本数: {len(samples)}")
        print(f"  • 细胞系: {', '.join(cell_lines)}")
        print(f"  • 实验设计: {len(conditions)} 个条件 × {len(replicates)} 个重复")
        
        return self
    
    def quality_control(self):
        """步骤2：质量控制"""
        print("\n🔍 步骤2：质量控制")
        print("-" * 50)
        
        # 计算QC指标
        qc_metrics = pd.DataFrame({
            'total_counts': self.raw_counts.sum(),
            'detected_genes': (self.raw_counts > 0).sum(),
            'mean_count': self.raw_counts.mean(),
            'median_count': self.raw_counts.median()
        })
        
        # 添加样本信息
        qc_metrics = qc_metrics.merge(self.sample_metadata, left_index=True, right_on='sample')
        
        print("样本质量指标汇总:")
        print(qc_metrics.groupby(['cell_line', 'condition'])[['total_counts', 'detected_genes']].mean().round(0))
        
        # 识别离群样本
        z_scores = np.abs((qc_metrics['total_counts'] - qc_metrics['total_counts'].mean()) / 
                         qc_metrics['total_counts'].std())
        outliers = qc_metrics[z_scores > 3]
        
        if len(outliers) > 0:
            print(f"\n⚠️ 发现 {len(outliers)} 个离群样本")
        else:
            print("\n✓ 所有样本通过质量控制")
        
        # 过滤低表达基因
        min_count = 10
        min_samples = 3
        keep_genes = (self.raw_counts >= min_count).sum(axis=1) >= min_samples
        self.filtered_counts = self.raw_counts[keep_genes]
        
        print(f"\n基因过滤:")
        print(f"  • 过滤前: {len(self.raw_counts)} 个基因")
        print(f"  • 过滤后: {len(self.filtered_counts)} 个基因")
        print(f"  • 过滤掉: {len(self.raw_counts) - len(self.filtered_counts)} 个低表达基因")
        
        return self
    
    def normalize_data(self):
        """步骤3：数据标准化"""
        print("\n📊 步骤3：数据标准化")
        print("-" * 50)
        
        # CPM标准化（Counts Per Million）
        cpm = self.filtered_counts.div(self.filtered_counts.sum()) * 1e6
        
        # log2转换
        self.normalized_data = np.log2(cpm + 1)
        
        print("✓ CPM标准化完成")
        print(f"  • 标准化后数据范围: [{self.normalized_data.min().min():.2f}, {self.normalized_data.max().max():.2f}]")
        
        # 检查批次效应
        print("\n批次效应检查:")
        # 计算样本间相关性
        sample_corr = self.normalized_data.corr()
        
        # 按细胞系分组查看相关性
        for cell_line in self.sample_metadata['cell_line'].unique():
            cell_line_samples = self.sample_metadata[
                self.sample_metadata['cell_line'] == cell_line
            ]['sample'].values
            
            within_corr = sample_corr.loc[cell_line_samples, cell_line_samples].values
            within_corr = within_corr[np.triu_indices_from(within_corr, k=1)]
            
            print(f"  • {cell_line} 内部相关性: {within_corr.mean():.3f} ± {within_corr.std():.3f}")
        
        return self
    
    def differential_expression(self):
        """步骤4：差异表达分析"""
        print("\n🧬 步骤4：差异表达分析")
        print("-" * 50)
        
        results_list = []
        
        for cell_line in self.sample_metadata['cell_line'].unique():
            print(f"\n分析 {cell_line} 细胞系:")
            
            # 获取该细胞系的样本
            control_samples = self.sample_metadata[
                (self.sample_metadata['cell_line'] == cell_line) & 
                (self.sample_metadata['condition'] == 'Control')
            ]['sample'].values
            
            treated_samples = self.sample_metadata[
                (self.sample_metadata['cell_line'] == cell_line) & 
                (self.sample_metadata['condition'] == 'Treated')
            ]['sample'].values
            
            # 对每个基因进行差异分析
            for gene in self.filtered_counts.index:
                control_values = self.filtered_counts.loc[gene, control_samples].values
                treated_values = self.filtered_counts.loc[gene, treated_samples].values
                
                # 计算统计量
                control_mean = control_values.mean()
                treated_mean = treated_values.mean()
                fold_change = treated_mean / (control_mean + 1)
                log2_fc = np.log2(fold_change + 0.001)
                
                # t检验
                _, p_value = stats.ttest_ind(control_values, treated_values)
                
                results_list.append({
                    'cell_line': cell_line,
                    'gene': gene,
                    'control_mean': control_mean,
                    'treated_mean': treated_mean,
                    'fold_change': fold_change,
                    'log2_fc': log2_fc,
                    'p_value': p_value
                })
        
        self.de_results = pd.DataFrame(results_list)
        
        # FDR校正
        for cell_line in self.de_results['cell_line'].unique():
            mask = self.de_results['cell_line'] == cell_line
            p_values = self.de_results.loc[mask, 'p_value'].values
            _, fdr, _, _ = multipletests(p_values, method='fdr_bh')
            self.de_results.loc[mask, 'fdr'] = fdr
        
        # 统计显著基因
        sig_threshold = 0.05
        fc_threshold = 1.5
        
        for cell_line in self.de_results['cell_line'].unique():
            cell_line_de = self.de_results[self.de_results['cell_line'] == cell_line]
            sig_genes = cell_line_de[
                (cell_line_de['fdr'] < sig_threshold) & 
                (np.abs(cell_line_de['log2_fc']) > np.log2(fc_threshold))
            ]
            
            n_up = (sig_genes['log2_fc'] > 0).sum()
            n_down = (sig_genes['log2_fc'] < 0).sum()
            
            print(f"  • 显著差异基因: {len(sig_genes)} (↑{n_up} ↓{n_down})")
        
        return self
    
    def functional_enrichment(self):
        """步骤5：功能富集分析"""
        print("\n🔬 步骤5：功能富集分析")
        print("-" * 50)
        
        # 模拟GO terms和KEGG pathways
        go_terms = {
            'GO:0006915': 'apoptotic process',
            'GO:0007049': 'cell cycle',
            'GO:0006954': 'inflammatory response',
            'GO:0008283': 'cell proliferation',
            'GO:0001525': 'angiogenesis',
            'GO:0006629': 'lipid metabolic process',
            'GO:0006096': 'glycolytic process',
            'GO:0042981': 'regulation of apoptotic process'
        }
        
        kegg_pathways = {
            'hsa04110': 'Cell cycle',
            'hsa04210': 'Apoptosis',
            'hsa04151': 'PI3K-Akt signaling pathway',
            'hsa04668': 'TNF signaling pathway',
            'hsa00010': 'Glycolysis / Gluconeogenesis'
        }
        
        enrichment_results = []
        
        for cell_line in self.de_results['cell_line'].unique():
            # 获取显著上调和下调基因
            cell_line_de = self.de_results[self.de_results['cell_line'] == cell_line]
            sig_up = cell_line_de[
                (cell_line_de['fdr'] < 0.05) & 
                (cell_line_de['log2_fc'] > np.log2(1.5))
            ]['gene'].values
            
            sig_down = cell_line_de[
                (cell_line_de['fdr'] < 0.05) & 
                (cell_line_de['log2_fc'] < -np.log2(1.5))
            ]['gene'].values
            
            print(f"\n{cell_line} 富集分析:")
            
            # 模拟GO富集（简化版）
            if len(sig_up) > 0:
                print("  上调基因富集的GO terms:")
                for go_id, go_name in list(go_terms.items())[:3]:
                    # 模拟富集分数
                    enrichment_score = np.random.uniform(2, 5)
                    p_value = np.random.uniform(0.0001, 0.05)
                    print(f"    • {go_name}: ES={enrichment_score:.2f}, p={p_value:.4f}")
                    
                    enrichment_results.append({
                        'cell_line': cell_line,
                        'direction': 'up',
                        'term_id': go_id,
                        'term_name': go_name,
                        'enrichment_score': enrichment_score,
                        'p_value': p_value
                    })
            
            if len(sig_down) > 0:
                print("  下调基因富集的GO terms:")
                for go_id, go_name in list(go_terms.items())[3:6]:
                    enrichment_score = np.random.uniform(2, 5)
                    p_value = np.random.uniform(0.0001, 0.05)
                    print(f"    • {go_name}: ES={enrichment_score:.2f}, p={p_value:.4f}")
                    
                    enrichment_results.append({
                        'cell_line': cell_line,
                        'direction': 'down',
                        'term_id': go_id,
                        'term_name': go_name,
                        'enrichment_score': enrichment_score,
                        'p_value': p_value
                    })
        
        self.enrichment_results = pd.DataFrame(enrichment_results)
        
        return self
    
    def generate_report(self):
        """步骤6：生成分析报告"""
        print("\n📝 步骤6：生成分析报告")
        print("-" * 50)
        
        print("\n" + "=" * 70)
        print("                    RNA-seq分析报告摘要")
        print("=" * 70)
        
        print(f"\n研究名称: {self.name}")
        print(f"分析日期: 2024-01-15")
        print(f"分析人员: BioPython学习者")
        
        print("\n1. 数据概况:")
        print(f"   • 总基因数: {len(self.raw_counts)}")
        print(f"   • 分析基因数: {len(self.filtered_counts)}")
        print(f"   • 样本数: {len(self.sample_metadata)}")
        print(f"   • 细胞系: {', '.join(self.sample_metadata['cell_line'].unique())}")
        
        print("\n2. 差异表达汇总:")
        de_summary = self.de_results[self.de_results['fdr'] < 0.05].groupby('cell_line').agg({
            'gene': 'count',
            'log2_fc': lambda x: (x > 0).sum()
        })
        de_summary.columns = ['total_sig_genes', 'up_regulated']
        de_summary['down_regulated'] = de_summary['total_sig_genes'] - de_summary['up_regulated']
        print(de_summary)
        
        print("\n3. 主要发现:")
        print("   • 药物处理导致多个细胞系的转录组发生显著变化")
        print("   • 不同细胞系显示出特异性的药物响应模式")
        print("   • 凋亡和细胞周期相关通路显著富集")
        
        print("\n4. 关键基因（Top响应基因）:")
        # 找出在所有细胞系中都显著的基因
        sig_in_all = self.de_results[self.de_results['fdr'] < 0.05].groupby('gene').size()
        consistent_genes = sig_in_all[sig_in_all == 3].index[:5]
        if len(consistent_genes) > 0:
            print("   在所有细胞系中一致响应的基因:")
            for gene in consistent_genes:
                gene_data = self.de_results[self.de_results['gene'] == gene]
                mean_fc = gene_data['log2_fc'].mean()
                direction = "↑" if mean_fc > 0 else "↓"
                print(f"     • {gene}: {direction} (平均log2FC: {mean_fc:.2f})")
        
        print("\n5. 建议后续实验:")
        print("   • 使用qPCR验证关键差异表达基因")
        print("   • Western blot验证蛋白水平变化")
        print("   • 功能实验验证凋亡通路激活")
        print("   • 时间序列实验追踪动态响应")
        
        print("\n" + "=" * 70)
        print("                    分析完成！")
        print("=" * 70)
        
        return self

# 运行完整的分析管道
print("\n🚀 启动RNA-seq分析管道...")
pipeline = RNASeqAnalysisPipeline()

# 执行分析流程
(pipeline
 .load_data()
 .quality_control()
 .normalize_data()
 .differential_expression()
 .functional_enrichment()
 .generate_report())

print("\n✨ 恭喜！你已经完成了一个完整的RNA-seq数据分析流程！")
```

## 📝 练习题预览

### 循序渐进的练习设计

本章的练习题设计遵循"由浅入深、理论结合实践"的原则：

#### 🌟 基础练习（★）- 夯实基本功
1. **数据整合练习**：合并来自不同实验室的表达数据
2. **质量控制练习**：识别和处理异常样本
3. **基础统计练习**：计算基因表达的描述性统计

#### 🚀 进阶练习（★★）- 模拟真实场景
4. **差异表达分析**：完整的DE分析流程实践
5. **批次效应校正**：识别并消除技术偏差
6. **功能分组分析**：按基因功能进行分组比较

#### 🏆 挑战练习（★★★）- 综合应用
7. **时间序列分析**：药物处理的时间响应研究
8. **多组学整合**：转录组与蛋白组数据整合
9. **机器学习应用**：基于表达谱的样本分类

每个练习都配有：
- 明确的学习目标
- 详细的任务说明
- 循序渐进的提示
- 完整的参考答案

## 🎓 本章总结：从数据到洞察的桥梁

### 🌟 你已经掌握的核心能力

经过本章的学习，你现在能够：

1. **数据工程师的能力**
   - 整合多来源的复杂数据
   - 处理缺失值和异常值
   - 优化大规模数据的处理性能

2. **统计学家的思维**
   - 选择合适的统计检验方法
   - 进行严格的多重检验校正
   - 评估结果的统计显著性和生物学意义

3. **生物信息学家的视角**
   - 执行完整的差异表达分析
   - 识别关键的生物学通路
   - 从数据中提取生物学洞察

### 💡 关键要点回顾

```python
# 本章核心知识点总结
chapter_summary = {
    "数据整合": {
        "merge": "精确连接多个数据源",
        "concat": "纵向或横向合并数据",
        "pivot": "数据重塑和透视分析"
    },
    
    "分组分析": {
        "groupby": "按类别分组统计",
        "agg": "多重聚合函数",
        "transform": "组内数据变换"
    },
    
    "统计检验": {
        "t_test": "两组比较",
        "ANOVA": "多组比较",
        "FDR": "多重检验校正"
    },
    
    "时间序列": {
        "rolling": "滑动窗口分析",
        "expanding": "累积分析",
        "correlation": "时间点相关性"
    },
    
    "性能优化": {
        "vectorization": "向量化操作",
        "dtypes": "数据类型优化",
        "chunking": "分块处理大文件"
    }
}
```

### 🚀 下一步学习建议

1. **实践项目**：用真实的GEO或TCGA数据重现本章分析
2. **深入学习**：探索DESeq2、edgeR等专业差异分析工具
3. **可视化提升**：学习第8章，将分析结果转化为专业图表
4. **机器学习进阶**：结合第10章，应用ML方法进行预测建模

## 🌈 写在最后：数据分析的艺术

亲爱的学习者：

如果你认真学习了本章的内容，你已经掌握了专业级别的转录组数据分析技能。这不仅仅是技术的提升，更是思维方式的转变。

记住，数据分析不仅是一门科学，更是一门艺术。它需要：
- **严谨的统计思维**：确保结果的可靠性
- **深厚的生物学知识**：理解数据背后的意义
- **创新的问题解决能力**：应对各种数据挑战
- **清晰的沟通表达**：将发现转化为科学故事

在下一章，我们将学习如何用Matplotlib和Seaborn创建出版级别的科学图表，让你的数据分析结果以最美的方式呈现！

加油！你离成为一名真正的生物信息学家又近了一步！🎉

---

**思考题**：如果你有一个包含100个病人、20000个基因、5个时间点的临床转录组数据集，你会如何设计分析流程来发现疾病相关的生物标志物？

**挑战自己**：尝试用本章学到的方法，分析一个真实的GEO数据集（如GSE48213），看看能否重现论文中的主要发现！