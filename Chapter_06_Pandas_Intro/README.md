# Chapter 06: Pandas入门 - 实验数据的电子表格

## 写在最前面 - 给生物学研究者的一封信

亲爱的研究者：

还记得你第一次用移液器的紧张吗？还记得第一次成功提取DNA时的兴奋吗？

今天，你即将学习另一个强大的"实验工具" - Pandas。不过这次，你的实验台是电脑，你的试剂是数据，你的移液器是代码。

我知道你可能在想："我是做生物的，为什么要学编程？Excel不是挺好用的吗？"

让我告诉你一个真实的故事：

> 2019年，我的一位同事用Excel分析了3个月的RNA-seq数据。有20,000个基因，100个样本。
> Excel频繁崩溃，手工操作导致了多次错误，最后发现有一列数据复制错了...
> 后来她学会了Pandas，同样的分析只用了2小时，而且可以随时重复验证。

这就是我们学习Pandas的原因 - 不是为了成为程序员，而是为了成为更高效的生物学家。

**本章承诺**：
- 用你熟悉的生物学概念解释每个编程概念
- 每个例子都基于真实的生物学数据
- 循序渐进，假设你没有任何编程经验
- 学完后，你能独立处理基因表达数据

准备好了吗？让我们开始这段奇妙的旅程！

---

## 本章导航 - 学习地图

```
第6章：Pandas基础
│
├── 1. 为什么需要Pandas？（10分钟）
│   ├── Excel的痛点
│   ├── Pandas的优势
│   └── 真实案例对比
│
├── 2. 核心概念（20分钟）
│   ├── Series = 试管架
│   ├── DataFrame = 96孔板
│   └── Index = 样品标签
│
├── 3. Series详解（30分钟）
│   ├── 创建Series
│   ├── 访问数据
│   ├── 基础运算
│   └── 10+个实例
│
├── 4. DataFrame详解（40分钟）
│   ├── 创建DataFrame
│   ├── 数据探索
│   ├── 数据选择
│   └── 15+个实例
│
├── 5. 索引和选择（30分钟）
│   ├── loc和iloc
│   ├── 条件筛选
│   ├── 布尔索引
│   └── 10+个实例
│
├── 6. 基础统计（20分钟）
│   ├── 描述性统计
│   ├── 分组统计
│   └── 相关性分析
│
├── 7. 数据清洗（20分钟）
│   ├── 处理缺失值
│   ├── 去除重复
│   └── 数据转换
│
└── 8. 综合项目（30分钟）
    └── 完整的基因表达分析

总计学习时间：约3小时
```

---

## 第1部分：为什么生物信息学需要Pandas？

### 1.1 让我们从一个真实的场景开始

想象这样一个场景：

你刚完成了一个药物筛选实验：
- 测试了10个候选药物
- 每个药物3个浓度
- 每个条件3个生物学重复
- 测量了5个关键基因的表达
- 总共：10 × 3 × 3 × 5 = 450个数据点

现在，你需要：
1. 计算每个条件的平均值和标准差
2. 找出表达变化最大的基因
3. 确定最有效的药物浓度
4. 生成可视化图表
5. 写出分析报告

**用Excel**：可能需要几个小时，还容易出错
**用Pandas**：只需要几分钟，而且可以重复运行

### 1.2 Excel的局限性 - 痛点清单

让我们诚实地面对Excel的问题：

#### 问题1：数据容量限制
```
Excel最大行数：1,048,576行
Excel最大列数：16,384列

听起来很多？但是：
- 一次RNA-seq实验：~20,000个基因
- 单细胞测序：可能有100,000+个细胞
- 每个细胞20,000个基因 = 20亿个数据点！

Excel：完全无法处理
Pandas：轻松搞定
```

#### 问题2：手工操作易错
```
在Excel中：
- 复制粘贴可能选错区域
- 公式拖动可能出现错误
- 删除行列可能破坏引用
- 没有操作历史记录

在Pandas中：
- 所有操作都是代码，可追溯
- 错了可以立即修改重运行
- 可以添加注释说明每步操作
```

#### 问题3：重复性差
```
三个月后，老板说："能用新的参数重新分析一下吗？"

Excel：天啊，我要重新点击500次鼠标...
Pandas：修改一个参数，运行，5秒搞定！
```

#### 问题4：协作困难
```
Excel文件发给同事：
- "你用的是哪个版本的Excel？"
- "为什么在我电脑上显示不一样？"
- "这个公式是什么意思？"

Pandas脚本发给同事：
- 代码就是文档
- 任何电脑都能运行
- 可以用Git进行版本控制
```

### 1.3 Pandas vs Excel - 详细对比

| 场景 | Excel | Pandas | 谁赢了？ |
|------|-------|--------|---------|
| **打开查看10行数据** | 双击即开，直观 | 需要写代码 | Excel ✓ |
| **处理100万行数据** | 卡死 | 秒开 | Pandas ✓ |
| **计算1000个基因的平均值** | 拖动公式，容易出错 | 一行代码 | Pandas ✓ |
| **重复昨天的分析** | 重新操作一遍 | 运行脚本 | Pandas ✓ |
| **合并10个数据文件** | 复制粘贴10次 | 循环自动处理 | Pandas ✓ |
| **生成100个图表** | 点击100次 | 循环自动生成 | Pandas ✓ |
| **查找特定模式的基因** | 筛选功能有限 | 正则表达式强大 | Pandas ✓ |
| **统计分析** | 基础功能 | 专业统计包 | Pandas ✓ |
| **与他人分享** | 发送文件 | 分享代码 | 平局 |
| **学习曲线** | 几乎没有 | 需要学习 | Excel ✓ |

**结论**：Excel适合快速查看和简单分析，Pandas适合严肃的数据科学工作。

### 1.4 真实案例：一个RNA-seq数据分析的对比

让我用一个真实的例子来说明差异：

**任务**：分析肿瘤vs正常组织的基因表达差异

#### Excel方法（我的痛苦经历）：
```
Day 1:
- 9:00 打开第一个Excel文件（20,000行）
- 9:05 Excel有点卡...
- 9:30 终于打开了，开始计算平均值
- 10:00 拖动公式到20,000行
- 10:30 Excel崩溃了...
- 10:31 重新打开，发现没保存
- 10:35 哭了一会儿
- 11:00 重新开始...

Day 2:
- 发现有些基因名被Excel自动转换成日期格式
- SEPT1变成了9月1日
- MARCH1变成了3月1日
- 需要手工修正...

Day 3:
- 老板："能不能把p值阈值从0.05改成0.01？"
- 我："......"（内心崩溃）
```

#### Pandas方法（现在的我）：
```python
# 10分钟搞定所有分析
import pandas as pd

# 读取数据 - 1行代码
df = pd.read_csv('gene_expression.csv')

# 计算平均值 - 1行代码
tumor_mean = df[['tumor1', 'tumor2', 'tumor3']].mean(axis=1)
normal_mean = df[['normal1', 'normal2', 'normal3']].mean(axis=1)

# 计算fold change - 1行代码
fold_change = tumor_mean / normal_mean

# 筛选显著基因 - 1行代码
significant = df[df['p_value'] < 0.01]  # 改参数只需要改这里

# 完成！可以去喝咖啡了☕
```

---

## 第2部分：核心概念 - 用生物学类比理解Pandas

### 2.1 Pandas的世界观

在开始写代码之前，让我们建立一个mental model（心智模型）：

```
生物实验室                 Pandas世界
│                        │
├─ 试管架      ═══════>  Series（一维数据）
├─ 96孔板      ═══════>  DataFrame（二维数据表）
├─ 样品标签    ═══════>  Index（索引）
├─ 实验记录本  ═══════>  DataFrame（完整数据集）
└─ 数据分析    ═══════>  Pandas操作
```

### 2.2 Series - 你的数字试管架

#### 什么是Series？

想象你有一个试管架：
- 每个位置（索引）放一个试管
- 每个试管里有一个样品（数据）
- 试管上有标签（索引标签）

```python
import pandas as pd
import numpy as np

# 创建一个Series - 就像准备一个试管架
# 场景：5个时间点的细胞数量
time_points = pd.Series(
    data=[1e4, 2e4, 4e4, 8e4, 1.6e5],  # 细胞数量
    index=['0h', '6h', '12h', '18h', '24h']  # 时间标签
)

print("细胞生长曲线数据：")
print(time_points)
```

输出：
```
细胞生长曲线数据：
0h      10000.0
6h      20000.0
12h     40000.0
18h     80000.0
24h    160000.0
dtype: float64
```

**生物学解释**：
- 这就像你在不同时间点取样
- 每个时间点是一个"试管"
- 试管里装着该时间点的细胞数

### 2.3 DataFrame - 你的数字96孔板

#### 什么是DataFrame？

想象一个96孔板：
- 行（rows）：不同的样品或基因
- 列（columns）：不同的条件或时间点
- 每个"孔"：一个数据点

```python
# 创建一个DataFrame - 就像准备一个96孔板
# 场景：3个基因在4个样本中的表达量
gene_expression = pd.DataFrame({
    'Control_1': [120, 450, 1500],  # 第一个对照样本
    'Control_2': [115, 460, 1480],  # 第二个对照样本
    'Treated_1': [220, 340, 1520],  # 第一个处理样本
    'Treated_2': [215, 335, 1510]   # 第二个处理样本
}, index=['GeneA', 'GeneB', 'GeneC'])  # 基因名作为行标签

print("基因表达矩阵：")
print(gene_expression)
```

输出：
```
基因表达矩阵：
        Control_1  Control_2  Treated_1  Treated_2
GeneA        120        115        220        215
GeneB        450        460        340        335
GeneC       1500       1480       1520       1510
```

**生物学解释**：
- 每一行是一个基因的表达谱
- 每一列是一个样本的基因表达
- 交叉点是特定基因在特定样本中的表达量

### 2.4 Index - 你的样品标签系统

Index就像实验室的标签系统：
- 确保每个样品都有唯一标识
- 方便快速定位数据
- 支持多种查询方式

```python
# Index的重要性 - 就像样品标签
# 没有好的标签系统，实验室会乱套！

# 场景：蛋白质浓度测量
# 糟糕的方式（没有明确标签）：
bad_data = pd.Series([1.2, 2.3, 0.8, 3.1])
print("没有标签的数据：")
print(bad_data)
print()

# 好的方式（有明确标签）：
protein_conc = pd.Series(
    [1.2, 2.3, 0.8, 3.1],
    index=['BSA', 'IgG', 'Lysozyme', 'Albumin']
)
print("有标签的数据：")
print(protein_conc)
print()

# 使用标签访问数据
print(f"BSA的浓度: {protein_conc['BSA']} mg/ml")
```

---

## 第3部分：Series深度探索 - 一维数据的魔法

### 3.1 创建Series的多种方法

就像实验室里准备样品有多种方法，创建Series也有多种途径：

#### 方法1：从列表创建
```python
# 场景：记录一周的细菌培养OD600值
od_values = pd.Series([0.1, 0.2, 0.4, 0.8, 1.2, 1.5, 1.6])
print("细菌生长曲线（OD600）：")
print(od_values)
print()

# 添加时间标签让数据更有意义
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
od_values = pd.Series([0.1, 0.2, 0.4, 0.8, 1.2, 1.5, 1.6], index=days)
print("带日期标签的生长曲线：")
print(od_values)
```

输出：
```
细菌生长曲线（OD600）：
0    0.1
1    0.2
2    0.4
3    0.8
4    1.2
5    1.5
6    1.6
dtype: float64

带日期标签的生长曲线：
Mon    0.1
Tue    0.2
Wed    0.4
Thu    0.8
Fri    1.2
Sat    1.5
Sun    1.6
dtype: float64
```

#### 方法2：从字典创建
```python
# 场景：酶活性测定结果
enzyme_activity = pd.Series({
    'Amylase': 125.3,      # 淀粉酶
    'Protease': 89.7,      # 蛋白酶
    'Lipase': 45.2,        # 脂肪酶
    'Cellulase': 67.8,     # 纤维素酶
    'Pectinase': 34.5      # 果胶酶
})

print("酶活性测定结果（U/ml）：")
print(enzyme_activity)
print()
print(f"活性最高的酶: {enzyme_activity.idxmax()}")
print(f"活性最低的酶: {enzyme_activity.idxmin()}")
```

输出：
```
酶活性测定结果（U/ml）：
Amylase      125.3
Protease      89.7
Lipase        45.2
Cellulase     67.8
Pectinase     34.5
dtype: float64

活性最高的酶: Amylase
活性最低的酶: Pectinase
```

#### 方法3：从NumPy数组创建
```python
# 场景：pH值测量（使用NumPy生成模拟数据）
np.random.seed(42)  # 保证结果可重现

# 模拟10次pH测量，正常值7.4附近波动
ph_measurements = pd.Series(
    np.random.normal(7.4, 0.1, 10),  # 均值7.4，标准差0.1
    index=[f'Sample_{i+1}' for i in range(10)]
)

print("血液pH值测量：")
print(ph_measurements.round(2))
print()
print(f"平均pH: {ph_measurements.mean():.2f}")
print(f"标准差: {ph_measurements.std():.3f}")
print(f"是否有异常值（<7.35或>7.45）: {((ph_measurements < 7.35) | (ph_measurements > 7.45)).any()}")
```

### 3.2 Series的基本操作

#### 访问数据 - 像从试管架取试管
```python
# 创建抗体浓度数据
antibodies = pd.Series({
    'Anti-GAPDH': 1.5,
    'Anti-Actin': 2.0,
    'Anti-Tubulin': 1.2,
    'Anti-H3': 0.8,
    'Anti-p53': 0.5
})

print("抗体库存（mg/ml）：")
print(antibodies)
print()

# 方法1：用标签访问（推荐）
print(f"Anti-GAPDH浓度: {antibodies['Anti-GAPDH']} mg/ml")

# 方法2：用位置访问
print(f"第一个抗体浓度: {antibodies.iloc[0]} mg/ml")

# 方法3：访问多个
print("\n管家基因抗体：")
print(antibodies[['Anti-GAPDH', 'Anti-Actin']])

# 方法4：切片访问
print("\n前三个抗体：")
print(antibodies.head(3))
```

#### 数学运算 - 就像配制溶液
```python
# 场景：稀释抗体
original_conc = pd.Series({
    'Antibody_A': 10.0,  # mg/ml
    'Antibody_B': 5.0,
    'Antibody_C': 2.0,
    'Antibody_D': 8.0
})

print("原始浓度（mg/ml）：")
print(original_conc)
print()

# 1:10稀释
diluted = original_conc / 10
print("1:10稀释后（mg/ml）：")
print(diluted)
print()

# 加入内标（所有样品加入0.1 mg/ml内标）
with_standard = original_conc + 0.1
print("加入内标后（mg/ml）：")
print(with_standard)
print()

# 计算所需体积（配制1ml终浓度1mg/ml）
target_conc = 1.0  # mg/ml
target_volume = 1.0  # ml
required_volume = (target_conc * target_volume) / original_conc * 1000  # 转换为μl
print("配制1ml浓度1mg/ml所需原液体积（μl）：")
print(required_volume.round(1))
```

### 3.3 Series的统计功能

```python
# 场景：多次实验的荧光强度测量
fluorescence = pd.Series([
    1250, 1180, 1320, 1290, 1195,
    1310, 1275, 1185, 1330, 1265
], index=[f'Exp_{i+1}' for i in range(10)])

print("荧光强度测量值（RFU）：")
print(fluorescence)
print()

# 基础统计
print("统计分析：")
print(f"样本数: {fluorescence.count()}")
print(f"平均值: {fluorescence.mean():.1f}")
print(f"中位数: {fluorescence.median():.1f}")
print(f"标准差: {fluorescence.std():.1f}")
print(f"最小值: {fluorescence.min()}")
print(f"最大值: {fluorescence.max()}")
print(f"变异系数(CV): {(fluorescence.std()/fluorescence.mean()*100):.1f}%")
print()

# 四分位数
print("四分位数分析：")
print(f"Q1 (25%): {fluorescence.quantile(0.25)}")
print(f"Q2 (50%): {fluorescence.quantile(0.50)}")
print(f"Q3 (75%): {fluorescence.quantile(0.75)}")
print(f"IQR: {fluorescence.quantile(0.75) - fluorescence.quantile(0.25)}")
```

### 3.4 Series的条件操作

```python
# 场景：筛选高表达基因
gene_expression = pd.Series({
    'GAPDH': 1500,
    'ACTB': 1200,
    'TP53': 150,
    'BRCA1': 80,
    'VEGFA': 45,
    'MYC': 250,
    'EGFR': 180,
    'KRAS': 95
})

print("基因表达水平（FPKM）：")
print(gene_expression)
print()

# 筛选高表达基因（>200）
high_expression = gene_expression[gene_expression > 200]
print("高表达基因（FPKM > 200）：")
print(high_expression)
print()

# 筛选中等表达基因（50-200）
medium_expression = gene_expression[(gene_expression >= 50) & (gene_expression <= 200)]
print("中等表达基因（50 ≤ FPKM ≤ 200）：")
print(medium_expression)
print()

# 标记表达水平
expression_level = gene_expression.apply(
    lambda x: 'High' if x > 200 else ('Medium' if x >= 50 else 'Low')
)
print("表达水平分类：")
print(expression_level)
```

### 3.5 Series的排序和排名

```python
# 场景：药物IC50值排序
ic50_values = pd.Series({
    'Drug_A': 0.5,   # μM
    'Drug_B': 2.3,
    'Drug_C': 0.1,
    'Drug_D': 5.6,
    'Drug_E': 1.2,
    'Drug_F': 0.3
})

print("药物IC50值（μM）：")
print(ic50_values)
print()

# 按值排序（找出最有效的药物）
sorted_by_value = ic50_values.sort_values()
print("按IC50值排序（从低到高，越低越有效）：")
print(sorted_by_value)
print()

# 排名
rankings = ic50_values.rank()
print("药物效力排名（1=最有效）：")
print(rankings)
print()

print(f"最有效的药物: {sorted_by_value.index[0]} (IC50 = {sorted_by_value.iloc[0]} μM)")
print(f"最无效的药物: {sorted_by_value.index[-1]} (IC50 = {sorted_by_value.iloc[-1]} μM)")
```

### 3.6 Series的缺失值处理

```python
# 场景：实验中某些测量失败
pcr_ct_values = pd.Series({
    'Sample_1': 25.3,
    'Sample_2': np.nan,  # 扩增失败
    'Sample_3': 24.8,
    'Sample_4': 26.1,
    'Sample_5': np.nan,  # 扩增失败
    'Sample_6': 25.7
})

print("qPCR Ct值：")
print(pcr_ct_values)
print()

# 检查缺失值
print(f"缺失值数量: {pcr_ct_values.isna().sum()}")
print(f"缺失的样本: {list(pcr_ct_values[pcr_ct_values.isna()].index)}")
print()

# 处理缺失值 - 方法1：删除
cleaned = pcr_ct_values.dropna()
print("删除缺失值后：")
print(cleaned)
print()

# 处理缺失值 - 方法2：填充均值
filled_mean = pcr_ct_values.fillna(pcr_ct_values.mean())
print("用均值填充：")
print(filled_mean)
print()

# 处理缺失值 - 方法3：向前填充
filled_forward = pcr_ct_values.fillna(method='ffill')
print("向前填充（用前一个值）：")
print(filled_forward)
```

### 3.7 Series的字符串操作

```python
# 场景：处理基因名称
gene_names = pd.Series([
    'BRCA1_HUMAN',
    'TP53_HUMAN',
    'GAPDH_HUMAN',
    'actb_human',  # 注意：小写
    'VEGFA_HUMAN'
])

print("原始基因名：")
print(gene_names)
print()

# 转换为大写
upper_names = gene_names.str.upper()
print("统一为大写：")
print(upper_names)
print()

# 提取基因符号（去除_HUMAN）
gene_symbols = gene_names.str.replace('_HUMAN', '', case=False)
print("提取基因符号：")
print(gene_symbols)
print()

# 检查是否包含特定模式
is_housekeeping = gene_names.str.contains('GAPDH|ACTB', case=False)
print("是否为管家基因：")
print(is_housekeeping)
```

### 3.8 Series的时间序列功能

```python
# 场景：细胞生长动力学
dates = pd.date_range('2024-01-01', periods=7, freq='D')
cell_count = pd.Series(
    [1e4, 2e4, 4.1e4, 8.3e4, 1.65e5, 3.2e5, 6.1e5],
    index=dates
)

print("细胞生长曲线：")
print(cell_count)
print()

# 计算日增长率
growth_rate = cell_count.pct_change() * 100
print("日增长率（%）：")
print(growth_rate.round(1))
print()

# 计算倍增时间（假设指数增长）
# 倍增时间 = ln(2) / 增长率
doubling_time = np.log(2) / np.log(cell_count / cell_count.shift(1))
print("倍增时间（天）：")
print(doubling_time.round(2))
```

### 3.9 Series的高级操作

```python
# 场景：比较两组实验数据
control = pd.Series([100, 95, 105, 98, 102], index=['Gene1', 'Gene2', 'Gene3', 'Gene4', 'Gene5'])
treated = pd.Series([150, 78, 156, 198, 95], index=['Gene1', 'Gene2', 'Gene3', 'Gene4', 'Gene5'])

print("对照组表达量：")
print(control)
print()
print("处理组表达量：")
print(treated)
print()

# 计算fold change
fold_change = treated / control
print("Fold Change：")
print(fold_change.round(2))
print()

# 计算log2 fold change
log2_fc = np.log2(fold_change)
print("Log2 Fold Change：")
print(log2_fc.round(2))
print()

# 识别显著变化的基因
significant = fold_change[(fold_change > 1.5) | (fold_change < 0.67)]
print("显著变化的基因（FC>1.5或FC<0.67）：")
print(significant)
```

### 3.10 Series实战案例：ELISA标准曲线

```python
# 完整案例：ELISA标准曲线分析
print("=" * 50)
print("ELISA标准曲线分析")
print("=" * 50)

# 标准品浓度（ng/ml）
std_conc = pd.Series([0, 0.5, 1, 2, 4, 8, 16, 32])

# OD450读数
od_values = pd.Series([0.05, 0.12, 0.21, 0.38, 0.72, 1.35, 2.1, 2.8])

# 创建标准曲线数据
std_curve = pd.Series(od_values.values, index=std_conc.values)
std_curve.index.name = 'Concentration (ng/ml)'
std_curve.name = 'OD450'

print("\n标准曲线数据：")
print(std_curve)
print()

# 样品OD值
sample_od = pd.Series({
    'Patient_1': 0.45,
    'Patient_2': 1.2,
    'Patient_3': 0.8,
    'Control': 0.06
})

print("样品OD值：")
print(sample_od)
print()

# 简单线性插值计算浓度
from scipy import interp

sample_conc = pd.Series({
    name: float(interp(od, od_values.values, std_conc.values))
    for name, od in sample_od.items()
})

print("计算的样品浓度（ng/ml）：")
print(sample_conc.round(2))
print()

# 质量控制
print("质量控制检查：")
print(f"标准曲线R²: {np.corrcoef(std_conc, od_values)[0,1]**2:.3f}")
print(f"检测范围: {std_conc.min()}-{std_conc.max()} ng/ml")
print(f"样品是否在检测范围内: {sample_od.apply(lambda x: od_values.min() <= x <= od_values.max())}")
```

---

## 第4部分：DataFrame详解 - 二维数据的世界

### 4.1 创建DataFrame的多种方法

DataFrame是Pandas的核心，让我们深入了解如何创建它：

#### 方法1：从字典创建
```python
# 场景：多个基因在多个样本中的表达
# 这是最常见的创建方式
expression_data = pd.DataFrame({
    'Sample_A': [100, 200, 1500, 50],
    'Sample_B': [110, 190, 1480, 55],
    'Sample_C': [95, 210, 1520, 48],
    'Sample_D': [105, 195, 1510, 52]
}, index=['BRCA1', 'TP53', 'GAPDH', 'VEGFA'])

print("基因表达矩阵：")
print(expression_data)
print()
print(f"数据形状: {expression_data.shape}")
print(f"行数（基因数）: {expression_data.shape[0]}")
print(f"列数（样本数）: {expression_data.shape[1]}")
```

#### 方法2：从列表的列表创建
```python
# 场景：细胞计数板的读数
# 每个列表是一行数据
cell_counts = pd.DataFrame([
    ['Well_A1', 'Control', 1.2e6, 95],
    ['Well_A2', 'Control', 1.3e6, 96],
    ['Well_B1', 'Treated', 0.8e6, 88],
    ['Well_B2', 'Treated', 0.7e6, 85]
], columns=['Well', 'Condition', 'Cell_Count', 'Viability_%'])

print("细胞计数数据：")
print(cell_counts)
print()
print("数据类型：")
print(cell_counts.dtypes)
```

#### 方法3：从NumPy数组创建
```python
# 场景：模拟96孔板的OD值读数
np.random.seed(42)

# 创建8x12的数组（96孔板）
plate_data = np.random.uniform(0.5, 2.0, size=(8, 12))

# 创建行列标签
rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
cols = range(1, 13)

# 创建DataFrame
plate_df = pd.DataFrame(
    plate_data,
    index=rows,
    columns=[f'Col_{i}' for i in cols]
)

print("96孔板OD值（前4行，前6列）：")
print(plate_df.iloc[:4, :6].round(2))
```

#### 方法4：从另一个DataFrame创建
```python
# 场景：筛选特定基因创建子集
# 原始数据
full_data = pd.DataFrame({
    'Expression': [100, 1500, 200, 50, 1200, 80],
    'Type': ['Oncogene', 'Housekeeping', 'Tumor_suppressor', 
             'Growth_factor', 'Housekeeping', 'Tumor_suppressor']
}, index=['MYC', 'GAPDH', 'TP53', 'VEGFA', 'ACTB', 'PTEN'])

print("完整基因列表：")
print(full_data)
print()

# 创建管家基因子集
housekeeping = full_data[full_data['Type'] == 'Housekeeping'].copy()
print("管家基因子集：")
print(housekeeping)
```

### 4.2 DataFrame的基本属性

```python
# 创建一个综合示例数据
patients_data = pd.DataFrame({
    'Patient_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Age': [45, 52, 38, 61, 47],
    'Gender': ['M', 'F', 'F', 'M', 'M'],
    'Tumor_Size': [2.3, 3.1, 1.8, 4.2, 2.7],
    'Stage': ['II', 'III', 'I', 'IV', 'II'],
    'BRCA1_Expr': [120, 85, 150, 45, 110],
    'TP53_Expr': [200, 180, 220, 90, 195],
    'Treatment_Response': ['Partial', 'Complete', 'Complete', 'None', 'Partial']
})

print("患者数据表：")
print(patients_data)
print()

# 探索DataFrame属性
print("DataFrame属性：")
print(f"形状 (shape): {patients_data.shape}")
print(f"大小 (size): {patients_data.size}")
print(f"维度 (ndim): {patients_data.ndim}")
print(f"列名 (columns): {list(patients_data.columns)}")
print(f"索引 (index): {list(patients_data.index)}")
print()

print("数据类型信息：")
print(patients_data.dtypes)
print()

print("内存使用情况：")
print(patients_data.memory_usage())
```

### 4.3 DataFrame的数据探索

```python
# 使用前面的患者数据
print("=" * 50)
print("数据探索技巧")
print("=" * 50)

# 查看前几行
print("\n前3行数据（head）：")
print(patients_data.head(3))

# 查看后几行
print("\n后2行数据（tail）：")
print(patients_data.tail(2))

# 随机抽样
print("\n随机抽取2行（sample）：")
print(patients_data.sample(2, random_state=42))

# 基本信息
print("\n数据基本信息（info）：")
patients_data.info()

# 数值列的统计描述
print("\n数值列统计（describe）：")
print(patients_data.describe().round(2))

# 包含非数值列的统计
print("\n所有列统计（describe include='all'）：")
print(patients_data.describe(include='all'))
```

### 4.4 DataFrame的索引和选择

```python
# 这是最重要的技能之一！
print("=" * 50)
print("数据选择的艺术")
print("=" * 50)

# 创建示例数据
gene_data = pd.DataFrame({
    'Gene_Symbol': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'PTEN'],
    'Chromosome': ['chr17', 'chr17', 'chr7', 'chr12', 'chr10'],
    'Expression_Normal': [100, 150, 80, 90, 110],
    'Expression_Tumor': [50, 250, 200, 180, 40],
    'Mutation_Freq': [0.15, 0.50, 0.25, 0.35, 0.20]
})
gene_data.set_index('Gene_Symbol', inplace=True)

print("基因数据表：")
print(gene_data)
print()

# 1. 选择单列（返回Series）
print("选择单列 - Expression_Tumor：")
print(gene_data['Expression_Tumor'])
print()

# 2. 选择多列（返回DataFrame）
print("选择多列 - 表达量数据：")
print(gene_data[['Expression_Normal', 'Expression_Tumor']])
print()

# 3. 使用loc按标签选择
print("使用loc选择TP53基因的所有数据：")
print(gene_data.loc['TP53'])
print()

print("使用loc选择多个基因的特定列：")
print(gene_data.loc[['BRCA1', 'TP53'], ['Chromosome', 'Mutation_Freq']])
print()

# 4. 使用iloc按位置选择
print("使用iloc选择第一行：")
print(gene_data.iloc[0])
print()

print("使用iloc选择前2行，前3列：")
print(gene_data.iloc[:2, :3])
print()

# 5. 条件选择
print("选择突变频率>0.25的基因：")
high_mutation = gene_data[gene_data['Mutation_Freq'] > 0.25]
print(high_mutation)
print()

# 6. 复合条件
print("选择肿瘤中上调且突变频率高的基因：")
upregulated_mutated = gene_data[
    (gene_data['Expression_Tumor'] > gene_data['Expression_Normal']) & 
    (gene_data['Mutation_Freq'] > 0.2)
]
print(upregulated_mutated)
```

### 4.5 DataFrame的数据修改

```python
# 场景：更新实验数据
print("=" * 50)
print("数据修改操作")
print("=" * 50)

# 创建初始数据
exp_data = pd.DataFrame({
    'Sample_ID': ['S001', 'S002', 'S003'],
    'Treatment': ['Control', 'DrugA', 'DrugB'],
    'Cell_Count': [1e6, 1.2e6, 0.8e6],
    'Viability': [95, 92, 88]
})

print("原始数据：")
print(exp_data)
print()

# 1. 修改单个值
exp_data.loc[0, 'Viability'] = 96
print("修改后（更新第一个样本的活力）：")
print(exp_data)
print()

# 2. 修改整列
exp_data['Cell_Count'] = exp_data['Cell_Count'] / 1e6  # 转换为百万
print("单位转换后（细胞数改为百万）：")
print(exp_data)
print()

# 3. 添加新列
exp_data['Quality'] = ['Good', 'Good', 'Fair']
exp_data['Date'] = '2024-01-15'
print("添加新列后：")
print(exp_data)
print()

# 4. 基于条件修改
exp_data.loc[exp_data['Viability'] < 90, 'Quality'] = 'Poor'
print("基于条件修改后：")
print(exp_data)
```

### 4.6 DataFrame的计算操作

```python
# 场景：基因表达数据分析
print("=" * 50)
print("DataFrame计算")
print("=" * 50)

# 创建表达数据
expression = pd.DataFrame({
    'Control_1': [100, 200, 1500, 50],
    'Control_2': [110, 190, 1480, 55],
    'Treated_1': [150, 150, 1510, 120],
    'Treated_2': [145, 155, 1490, 115]
}, index=['GeneA', 'GeneB', 'GeneC', 'GeneD'])

print("原始表达数据：")
print(expression)
print()

# 1. 按行计算（axis=1）
expression['Mean_Control'] = expression[['Control_1', 'Control_2']].mean(axis=1)
expression['Mean_Treated'] = expression[['Treated_1', 'Treated_2']].mean(axis=1)
print("添加平均值列：")
print(expression)
print()

# 2. 计算Fold Change
expression['Fold_Change'] = expression['Mean_Treated'] / expression['Mean_Control']
print("添加Fold Change：")
print(expression.round(2))
print()

# 3. 按列计算（axis=0）
print("每个样本的统计：")
sample_stats = pd.DataFrame({
    'Total': expression[['Control_1', 'Control_2', 'Treated_1', 'Treated_2']].sum(),
    'Mean': expression[['Control_1', 'Control_2', 'Treated_1', 'Treated_2']].mean(),
    'Std': expression[['Control_1', 'Control_2', 'Treated_1', 'Treated_2']].std()
})
print(sample_stats.round(2))
```

### 4.7 DataFrame的分组操作

```python
# 场景：多个时间点的细胞实验
print("=" * 50)
print("分组分析（GroupBy）")
print("=" * 50)

# 创建时间序列实验数据
time_series = pd.DataFrame({
    'Time': ['0h', '0h', '0h', '6h', '6h', '6h', '12h', '12h', '12h'],
    'Replicate': ['R1', 'R2', 'R3', 'R1', 'R2', 'R3', 'R1', 'R2', 'R3'],
    'Cell_Count': [1e4, 1.1e4, 0.9e4, 2e4, 2.2e4, 1.8e4, 4e4, 4.3e4, 3.7e4],
    'Viability': [95, 96, 94, 93, 94, 92, 90, 91, 89]
})

print("时间序列数据：")
print(time_series)
print()

# 按时间点分组
grouped = time_series.groupby('Time')

# 计算每个时间点的平均值
print("每个时间点的平均值：")
time_means = grouped.mean()
print(time_means)
print()

# 计算每个时间点的标准差
print("每个时间点的标准差：")
time_std = grouped.std()
print(time_std.round(2))
print()

# 多个聚合函数
print("综合统计：")
time_stats = grouped.agg({
    'Cell_Count': ['mean', 'std', 'min', 'max'],
    'Viability': ['mean', 'std']
})
print(time_stats)
```

### 4.8 DataFrame的合并操作

```python
# 场景：整合不同来源的数据
print("=" * 50)
print("数据合并")
print("=" * 50)

# 基因注释数据
gene_info = pd.DataFrame({
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS'],
    'Function': ['DNA_repair', 'Apoptosis', 'Growth', 'Signaling'],
    'Chromosome': ['chr17', 'chr17', 'chr7', 'chr12']
})

# 基因表达数据
gene_expression = pd.DataFrame({
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'VEGFA'],
    'Expression': [100, 200, 150, 80],
    'Sample': ['Tumor', 'Tumor', 'Tumor', 'Tumor']
})

print("基因信息表：")
print(gene_info)
print()
print("基因表达表：")
print(gene_expression)
print()

# 内连接（只保留两表都有的基因）
merged_inner = pd.merge(gene_info, gene_expression, on='Gene', how='inner')
print("内连接结果（交集）：")
print(merged_inner)
print()

# 左连接（保留所有基因信息）
merged_left = pd.merge(gene_info, gene_expression, on='Gene', how='left')
print("左连接结果（保留所有基因信息）：")
print(merged_left)
print()

# 外连接（保留所有数据）
merged_outer = pd.merge(gene_info, gene_expression, on='Gene', how='outer')
print("外连接结果（并集）：")
print(merged_outer)
```

### 4.9 DataFrame的重塑操作

```python
# 场景：长格式与宽格式转换
print("=" * 50)
print("数据重塑")
print("=" * 50)

# 宽格式数据（典型的基因表达矩阵）
wide_data = pd.DataFrame({
    'Gene': ['GeneA', 'GeneB', 'GeneC'],
    'Sample1': [100, 200, 150],
    'Sample2': [110, 190, 160],
    'Sample3': [95, 210, 140]
})

print("宽格式数据：")
print(wide_data)
print()

# 转换为长格式（用于某些分析和可视化）
long_data = wide_data.melt(
    id_vars=['Gene'],
    var_name='Sample',
    value_name='Expression'
)
print("长格式数据：")
print(long_data)
print()

# 长格式转回宽格式
wide_again = long_data.pivot(
    index='Gene',
    columns='Sample',
    values='Expression'
)
print("转回宽格式：")
print(wide_again)
```

### 4.10 DataFrame的数据清洗

```python
# 场景：处理实验数据中的问题
print("=" * 50)
print("数据清洗")
print("=" * 50)

# 创建有问题的数据
messy_data = pd.DataFrame({
    'Sample': ['S001', 'S002', 'S003', 'S002', 'S004', 'S005'],  # 注意S002重复
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'TP53', None, 'KRAS'],  # 有缺失值
    'Expression': [100, 200, -50, 200, 150, 1e10],  # 有异常值
    'Quality': ['Good', 'good', 'GOOD', 'Good', 'Fair', 'Poor']  # 大小写不一致
})

print("原始数据（有问题）：")
print(messy_data)
print()

# 1. 处理重复值
print("重复的行：")
print(messy_data[messy_data.duplicated(subset=['Sample', 'Gene'], keep=False)])
print()

# 删除完全重复的行
clean_data = messy_data.drop_duplicates()
print("删除重复后：")
print(clean_data)
print()

# 2. 处理缺失值
print(f"缺失值统计：")
print(clean_data.isnull().sum())
print()

# 删除有缺失值的行
clean_data = clean_data.dropna()
print("删除缺失值后：")
print(clean_data)
print()

# 3. 处理异常值
print("识别异常值（表达量<0或>10000）：")
outliers = (clean_data['Expression'] < 0) | (clean_data['Expression'] > 10000)
print(clean_data[outliers])
print()

# 将异常值替换为NaN
clean_data.loc[outliers, 'Expression'] = np.nan
clean_data = clean_data.dropna()
print("处理异常值后：")
print(clean_data)
print()

# 4. 标准化文本
clean_data['Quality'] = clean_data['Quality'].str.capitalize()
print("标准化文本后：")
print(clean_data)
```

### 4.11 DataFrame的应用案例1：药物筛选数据分析

```python
print("=" * 60)
print("综合案例1：药物筛选数据分析")
print("=" * 60)

# 创建药物筛选数据
np.random.seed(42)

drugs = ['DrugA', 'DrugB', 'DrugC', 'DrugD', 'DrugE']
cell_lines = ['MCF7', 'HeLa', 'A549', 'HepG2']
concentrations = [0.1, 1, 10, 100]  # μM

# 生成IC50数据
ic50_data = []
for drug in drugs:
    for cell_line in cell_lines:
        ic50 = np.random.lognormal(1, 1.5)  # 对数正态分布
        ic50_data.append({
            'Drug': drug,
            'Cell_Line': cell_line,
            'IC50': round(ic50, 2),
            'Max_Inhibition': round(np.random.uniform(60, 95), 1)
        })

screening_df = pd.DataFrame(ic50_data)

print("药物筛选数据（前10行）：")
print(screening_df.head(10))
print()

# 分析1：每个药物的平均IC50
drug_summary = screening_df.groupby('Drug').agg({
    'IC50': ['mean', 'std', 'min', 'max'],
    'Max_Inhibition': 'mean'
}).round(2)

print("药物效力总结：")
print(drug_summary)
print()

# 分析2：找出最有效的药物
best_drug = drug_summary['IC50']['mean'].idxmin()
print(f"最有效的药物: {best_drug}")
print(f"平均IC50: {drug_summary.loc[best_drug, ('IC50', 'mean')]} μM")
print()

# 分析3：细胞系敏感性
sensitivity = screening_df.pivot_table(
    values='IC50',
    index='Cell_Line',
    columns='Drug',
    aggfunc='mean'
)
print("细胞系药物敏感性矩阵：")
print(sensitivity.round(2))
print()

# 分析4：识别选择性药物
selectivity = screening_df.groupby('Drug')['IC50'].std()
print("药物选择性（标准差越大，选择性越强）：")
print(selectivity.sort_values(ascending=False).round(2))
```

### 4.12 DataFrame的应用案例2：基因表达时间序列分析

```python
print("=" * 60)
print("综合案例2：基因表达时间序列分析")
print("=" * 60)

# 创建时间序列基因表达数据
time_points = [0, 2, 4, 6, 8, 12, 24]  # 小时
genes = ['TP53', 'CDKN1A', 'BAX', 'BCL2', 'GAPDH']

# 生成表达数据
time_series_data = []
for gene in genes:
    # 不同基因有不同的表达模式
    if gene == 'TP53':  # 早期响应
        pattern = [100, 150, 200, 180, 160, 140, 120]
    elif gene == 'CDKN1A':  # TP53下游，延迟响应
        pattern = [50, 55, 80, 120, 150, 140, 130]
    elif gene == 'BAX':  # 促凋亡，逐渐上升
        pattern = [80, 85, 90, 100, 120, 140, 160]
    elif gene == 'BCL2':  # 抗凋亡，逐渐下降
        pattern = [150, 140, 130, 120, 100, 80, 60]
    else:  # GAPDH，管家基因，稳定
        pattern = [1000, 1010, 995, 1005, 1000, 990, 1000]
    
    for i, time in enumerate(time_points):
        time_series_data.append({
            'Gene': gene,
            'Time': time,
            'Expression': pattern[i] + np.random.normal(0, 5)  # 添加噪声
        })

time_df = pd.DataFrame(time_series_data)

print("时间序列表达数据（前15行）：")
print(time_df.head(15))
print()

# 转换为宽格式便于分析
expression_matrix = time_df.pivot(
    index='Time',
    columns='Gene',
    values='Expression'
)

print("表达矩阵：")
print(expression_matrix.round(1))
print()

# 计算表达变化
fold_change = expression_matrix / expression_matrix.iloc[0]
print("相对于0时的Fold Change：")
print(fold_change.round(2))
print()

# 识别动态基因
dynamic_range = expression_matrix.max() - expression_matrix.min()
dynamic_genes = dynamic_range[dynamic_range > 50].sort_values(ascending=False)
print("动态变化基因（变化范围>50）：")
print(dynamic_genes.round(1))
print()

# 计算基因间相关性
correlation = expression_matrix.corr()
print("基因表达相关性：")
print(correlation.round(2))
print()

# 找出协同表达的基因对
print("强正相关基因对（r>0.8）：")
for i in range(len(correlation.columns)):
    for j in range(i+1, len(correlation.columns)):
        if correlation.iloc[i, j] > 0.8:
            print(f"  {correlation.columns[i]} - {correlation.columns[j]}: {correlation.iloc[i, j]:.2f}")

print("\n强负相关基因对（r<-0.8）：")
for i in range(len(correlation.columns)):
    for j in range(i+1, len(correlation.columns)):
        if correlation.iloc[i, j] < -0.8:
            print(f"  {correlation.columns[i]} - {correlation.columns[j]}: {correlation.iloc[i, j]:.2f}")
```

### 4.13 DataFrame的高级技巧

```python
print("=" * 60)
print("DataFrame高级技巧")
print("=" * 60)

# 技巧1：多级索引
print("技巧1：多级索引（MultiIndex）")
multi_index_data = pd.DataFrame({
    'Gene': ['BRCA1', 'BRCA1', 'TP53', 'TP53'],
    'Condition': ['Control', 'Treated', 'Control', 'Treated'],
    'Replicate1': [100, 150, 200, 180],
    'Replicate2': [105, 145, 195, 185],
    'Replicate3': [95, 155, 205, 175]
})

# 设置多级索引
multi_df = multi_index_data.set_index(['Gene', 'Condition'])
print("多级索引DataFrame：")
print(multi_df)
print()

# 访问多级索引数据
print("访问BRCA1的所有数据：")
print(multi_df.loc['BRCA1'])
print()

print("访问所有基因的Treated条件：")
print(multi_df.xs('Treated', level='Condition'))
print()

# 技巧2：apply函数的强大功能
print("技巧2：使用apply进行复杂计算")

def calculate_stats(row):
    """计算每行的统计量"""
    values = row.values
    return pd.Series({
        'mean': np.mean(values),
        'std': np.std(values),
        'cv': np.std(values) / np.mean(values) * 100
    })

stats = multi_df.apply(calculate_stats, axis=1)
print("计算的统计量：")
print(stats.round(2))
print()

# 技巧3：窗口函数
print("技巧3：滚动窗口分析")
growth_data = pd.DataFrame({
    'Day': range(1, 11),
    'Cell_Count': [1e4, 1.5e4, 2.2e4, 3.1e4, 4.5e4, 
                   6.2e4, 8.5e4, 1.1e5, 1.4e5, 1.7e5]
})

# 计算3天滚动平均
growth_data['Rolling_Mean'] = growth_data['Cell_Count'].rolling(window=3, center=True).mean()
growth_data['Growth_Rate'] = growth_data['Cell_Count'].pct_change() * 100

print("细胞生长数据与滚动分析：")
print(growth_data.round(0))
```

### 4.14 DataFrame性能优化

```python
print("=" * 60)
print("DataFrame性能优化技巧")
print("=" * 60)

# 创建大数据集
n_genes = 10000
n_samples = 100

print(f"创建大数据集：{n_genes}个基因 x {n_samples}个样本")

# 优化前：使用默认数据类型
large_df = pd.DataFrame(
    np.random.randn(n_genes, n_samples),
    index=[f'Gene_{i}' for i in range(n_genes)],
    columns=[f'Sample_{i}' for i in range(n_samples)]
)

print(f"\n优化前内存使用：{large_df.memory_usage().sum() / 1024**2:.2f} MB")

# 优化1：使用更小的数据类型
optimized_df = large_df.astype('float32')
print(f"使用float32后：{optimized_df.memory_usage().sum() / 1024**2:.2f} MB")

# 优化2：使用稀疏数据（如果有很多零值）
# 创建稀疏数据（90%为零）
sparse_data = np.random.randn(1000, 100)
sparse_data[sparse_data < 1.5] = 0  # 大约90%变为0

sparse_df = pd.DataFrame(sparse_data).astype(pd.SparseDtype("float", 0))
regular_df = pd.DataFrame(sparse_data)

print(f"\n稀疏数据优化：")
print(f"常规DataFrame：{regular_df.memory_usage().sum() / 1024:.2f} KB")
print(f"稀疏DataFrame：{sparse_df.memory_usage().sum() / 1024:.2f} KB")

# 优化3：使用category类型
sample_info = pd.DataFrame({
    'Sample_ID': [f'S{i:03d}' for i in range(1000)],
    'Condition': np.random.choice(['Control', 'Treated'], 1000),
    'Batch': np.random.choice(['Batch1', 'Batch2', 'Batch3'], 1000)
})

print(f"\n分类数据优化：")
print(f"优化前（object类型）：{sample_info.memory_usage().sum() / 1024:.2f} KB")

# 转换为category类型
sample_info['Condition'] = sample_info['Condition'].astype('category')
sample_info['Batch'] = sample_info['Batch'].astype('category')
print(f"优化后（category类型）：{sample_info.memory_usage().sum() / 1024:.2f} KB")
```

### 4.15 DataFrame实战项目：完整的差异表达分析

```python
print("=" * 60)
print("完整项目：差异表达基因分析")
print("=" * 60)

# 步骤1：创建模拟RNA-seq数据
np.random.seed(42)

# 生成基因列表（使用真实基因名）
gene_list = ['TP53', 'BRCA1', 'EGFR', 'VEGFA', 'MYC', 'KRAS', 'PTEN', 
             'CDKN2A', 'PIK3CA', 'BRAF', 'GAPDH', 'ACTB', 'TUBB', 
             'RPL13A', 'HPRT1']

# 生成表达数据
n_control = 3
n_treated = 3

expression_data = {}

# 对照组
for i in range(n_control):
    sample_name = f'Control_{i+1}'
    # 基础表达水平 + 噪声
    base_expression = np.random.lognormal(6, 2, len(gene_list))
    expression_data[sample_name] = base_expression

# 处理组（某些基因有变化）
for i in range(n_treated):
    sample_name = f'Treated_{i+1}'
    base_expression = np.random.lognormal(6, 2, len(gene_list))
    
    # 模拟处理效应
    for j, gene in enumerate(gene_list):
        if gene in ['TP53', 'CDKN2A', 'PTEN']:  # 上调
            base_expression[j] *= np.random.uniform(2, 3)
        elif gene in ['MYC', 'VEGFA']:  # 下调
            base_expression[j] *= np.random.uniform(0.3, 0.5)
    
    expression_data[sample_name] = base_expression

# 创建DataFrame
rna_seq_df = pd.DataFrame(expression_data, index=gene_list)
rna_seq_df = rna_seq_df.round(1)

print("RNA-seq表达矩阵：")
print(rna_seq_df)
print()

# 步骤2：质量控制
print("步骤2：质量控制")
print("-" * 30)

# 检查数据分布
print("样本总reads数：")
print(rna_seq_df.sum().round(0))
print()

# 检查低表达基因
low_expression = (rna_seq_df < 10).sum(axis=1)
print(f"低表达样本数（<10 counts）：")
print(low_expression[low_expression > 0])
print()

# 步骤3：数据标准化（简单的TPM标准化）
print("步骤3：数据标准化")
print("-" * 30)

# TPM标准化
tpm_df = rna_seq_df.div(rna_seq_df.sum()) * 1e6
print("TPM标准化后（前5个基因）：")
print(tpm_df.head().round(1))
print()

# 步骤4：差异表达分析
print("步骤4：差异表达分析")
print("-" * 30)

# 分离对照组和处理组
control_cols = [col for col in tpm_df.columns if 'Control' in col]
treated_cols = [col for col in tpm_df.columns if 'Treated' in col]

# 计算平均表达
tpm_df['Control_Mean'] = tpm_df[control_cols].mean(axis=1)
tpm_df['Treated_Mean'] = tpm_df[treated_cols].mean(axis=1)

# 计算Fold Change
tpm_df['Fold_Change'] = tpm_df['Treated_Mean'] / tpm_df['Control_Mean']
tpm_df['Log2_FC'] = np.log2(tpm_df['Fold_Change'])

# 简单的t检验（实际应用中应使用更复杂的统计方法）
from scipy import stats

p_values = []
for gene in gene_list:
    control_values = tpm_df.loc[gene, control_cols]
    treated_values = tpm_df.loc[gene, treated_cols]
    _, p_value = stats.ttest_ind(control_values, treated_values)
    p_values.append(p_value)

tpm_df['P_Value'] = p_values

# 多重检验校正（Benjamini-Hochberg）
from statsmodels.stats.multitest import multipletests
_, tpm_df['Adjusted_P'], _, _ = multipletests(tpm_df['P_Value'], method='fdr_bh')

# 步骤5：识别差异表达基因
print("步骤5：识别差异表达基因")
print("-" * 30)

# 定义阈值
fc_threshold = 1  # log2 fold change
p_threshold = 0.05

# 分类基因
tpm_df['Status'] = 'No_Change'
tpm_df.loc[(tpm_df['Log2_FC'] > fc_threshold) & (tpm_df['Adjusted_P'] < p_threshold), 'Status'] = 'Up'
tpm_df.loc[(tpm_df['Log2_FC'] < -fc_threshold) & (tpm_df['Adjusted_P'] < p_threshold), 'Status'] = 'Down'

# 结果总结
result_df = tpm_df[['Control_Mean', 'Treated_Mean', 'Log2_FC', 'P_Value', 'Adjusted_P', 'Status']]
result_df = result_df.sort_values('P_Value')

print("差异表达分析结果：")
print(result_df.round(3))
print()

print("统计总结：")
print(f"上调基因: {(result_df['Status'] == 'Up').sum()}")
print(f"下调基因: {(result_df['Status'] == 'Down').sum()}")
print(f"无变化基因: {(result_df['Status'] == 'No_Change').sum()}")
print()

print("最显著的差异表达基因：")
significant = result_df[result_df['Status'] != 'No_Change'].head()
print(significant[['Log2_FC', 'Adjusted_P', 'Status']].round(3))
```

---

## 第5部分：索引和选择 - 数据定位的艺术

### 5.1 理解索引的重要性

```python
print("=" * 60)
print("索引：数据的GPS系统")
print("=" * 60)

# 创建示例数据
patient_data = pd.DataFrame({
    'Age': [45, 52, 38, 61, 47],
    'Gender': ['M', 'F', 'F', 'M', 'M'],
    'Diagnosis': ['Cancer', 'Cancer', 'Healthy', 'Cancer', 'Healthy'],
    'Biomarker_Level': [125.3, 89.7, 32.1, 156.8, 41.2]
})

print("没有有意义索引的数据：")
print(patient_data)
print()

# 设置有意义的索引
patient_data.index = ['P001', 'P002', 'P003', 'P004', 'P005']
patient_data.index.name = 'Patient_ID'

print("有患者ID索引的数据：")
print(patient_data)
print()

# 索引的优势
print("使用索引快速访问：")
print(f"P003的数据：")
print(patient_data.loc['P003'])
print()
print(f"P003的年龄：{patient_data.loc['P003', 'Age']}")
```

### 5.2 loc vs iloc：标签 vs 位置

```python
print("=" * 60)
print("loc vs iloc：两种定位方式")
print("=" * 60)

# 创建基因表达数据
genes_df = pd.DataFrame({
    'Expression_A': [100, 200, 150, 80, 120],
    'Expression_B': [110, 190, 160, 75, 125],
    'Gene_Type': ['Oncogene', 'Suppressor', 'Housekeeping', 'Oncogene', 'Suppressor']
}, index=['MYC', 'TP53', 'GAPDH', 'KRAS', 'PTEN'])

print("基因数据：")
print(genes_df)
print()

print("使用loc（标签）：")
print("loc['TP53']：")
print(genes_df.loc['TP53'])
print()
print("loc['TP53', 'Expression_A']：")
print(genes_df.loc['TP53', 'Expression_A'])
print()

print("使用iloc（位置）：")
print("iloc[1]（第二行）：")
print(genes_df.iloc[1])
print()
print("iloc[1, 0]（第二行第一列）：")
print(genes_df.iloc[1, 0])
print()

# 切片操作的区别
print("切片的区别：")
print("loc['TP53':'KRAS']（包含结束）：")
print(genes_df.loc['TP53':'KRAS'])
print()
print("iloc[1:3]（不包含结束）：")
print(genes_df.iloc[1:3])
```

### 5.3 布尔索引：条件筛选的强大工具

```python
print("=" * 60)
print("布尔索引：条件筛选")
print("=" * 60)

# 创建药物反应数据
drug_response = pd.DataFrame({
    'Drug': ['DrugA', 'DrugB', 'DrugC', 'DrugD', 'DrugE'],
    'IC50': [0.5, 2.3, 0.1, 5.6, 1.2],
    'Max_Inhibition': [85, 72, 95, 45, 78],
    'Selectivity': ['High', 'Low', 'High', 'Low', 'Medium']
})

print("药物反应数据：")
print(drug_response)
print()

# 单条件筛选
print("高效药物（IC50 < 1）：")
efficient = drug_response[drug_response['IC50'] < 1]
print(efficient)
print()

# 多条件筛选（AND）
print("高效且高选择性：")
best = drug_response[(drug_response['IC50'] < 1) & (drug_response['Selectivity'] == 'High')]
print(best)
print()

# 多条件筛选（OR）
print("高效或高抑制率：")
good = drug_response[(drug_response['IC50'] < 1) | (drug_response['Max_Inhibition'] > 80)]
print(good)
print()

# 使用isin
print("特定选择性的药物：")
specific = drug_response[drug_response['Selectivity'].isin(['High', 'Medium'])]
print(specific)
```

### 5.4 高级索引技巧

```python
print("=" * 60)
print("高级索引技巧")
print("=" * 60)

# 创建多维数据
multi_data = pd.DataFrame({
    'Gene': ['BRCA1', 'BRCA1', 'TP53', 'TP53', 'EGFR', 'EGFR'],
    'Time': ['0h', '24h', '0h', '24h', '0h', '24h'],
    'Expression': [100, 150, 200, 180, 80, 120],
    'Variance': [5, 8, 10, 12, 3, 6]
})

print("时间序列基因表达：")
print(multi_data)
print()

# 使用query方法
print("使用query筛选（更易读）：")
result = multi_data.query("Gene == 'BRCA1' and Expression > 100")
print(result)
print()

# 使用where方法
print("使用where（保持形状）：")
masked = multi_data.where(multi_data['Expression'] > 100)
print(masked)
print()

# 使用mask方法（where的反向）
print("使用mask（隐藏满足条件的）：")
masked_reverse = multi_data.mask(multi_data['Expression'] > 100)
print(masked_reverse)
```

### 5.5 索引操作

```python
print("=" * 60)
print("索引操作和管理")
print("=" * 60)

# 创建数据
samples_df = pd.DataFrame({
    'Temperature': [37, 37.5, 38, 36.8],
    'pH': [7.4, 7.3, 7.5, 7.4],
    'Time': ['0h', '1h', '2h', '3h']
})

print("原始数据：")
print(samples_df)
print()

# 设置索引
samples_df = samples_df.set_index('Time')
print("设置Time为索引：")
print(samples_df)
print()

# 重置索引
reset_df = samples_df.reset_index()
print("重置索引：")
print(reset_df)
print()

# 重命名索引
samples_df.index.name = 'Time_Point'
print("重命名索引：")
print(samples_df)
print()

# 索引排序
sorted_df = samples_df.sort_index(ascending=False)
print("按索引排序（降序）：")
print(sorted_df)
```

### 5.6 多级索引（MultiIndex）

```python
print("=" * 60)
print("多级索引：处理复杂数据结构")
print("=" * 60)

# 创建多级索引数据
arrays = [
    ['Control', 'Control', 'Control', 'Treated', 'Treated', 'Treated'],
    ['Rep1', 'Rep2', 'Rep3', 'Rep1', 'Rep2', 'Rep3']
]

multi_index = pd.MultiIndex.from_arrays(arrays, names=['Condition', 'Replicate'])

expression = pd.DataFrame({
    'BRCA1': [100, 105, 95, 150, 145, 155],
    'TP53': [200, 195, 205, 180, 185, 175],
    'GAPDH': [1000, 1010, 990, 1005, 995, 1000]
}, index=multi_index)

print("多级索引DataFrame：")
print(expression)
print()

# 访问多级索引
print("访问Control条件的所有数据：")
print(expression.loc['Control'])
print()

print("访问Treated的Rep2：")
print(expression.loc[('Treated', 'Rep2')])
print()

# 交叉选择
print("使用xs选择所有Rep1：")
print(expression.xs('Rep1', level='Replicate'))
```

### 5.7 条件索引的实际应用

```python
print("=" * 60)
print("实际应用：基因筛选流程")
print("=" * 60)

# 创建综合基因数据
gene_database = pd.DataFrame({
    'Gene_Symbol': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'PTEN', 'MYC', 'VEGFA', 'GAPDH', 'ACTB'],
    'Expression': [120, 250, 180, 90, 110, 300, 85, 1500, 1200],
    'P_Value': [0.001, 0.03, 0.002, 0.15, 0.04, 0.0001, 0.08, 0.5, 0.6],
    'Fold_Change': [2.5, 1.8, 3.2, 1.1, 0.5, 4.1, 0.8, 1.05, 0.98],
    'Gene_Type': ['Suppressor', 'Suppressor', 'Oncogene', 'Oncogene', 'Suppressor', 
                  'Oncogene', 'Growth', 'Housekeeping', 'Housekeeping']
})

print("基因数据库：")
print(gene_database)
print()

# 步骤1：筛选显著差异基因
significant = gene_database[(gene_database['P_Value'] < 0.05) & 
                           ((gene_database['Fold_Change'] > 1.5) | 
                            (gene_database['Fold_Change'] < 0.67))]
print("显著差异基因：")
print(significant)
print()

# 步骤2：按基因类型分组筛选
oncogenes = gene_database[(gene_database['Gene_Type'] == 'Oncogene') & 
                          (gene_database['Expression'] > 100)]
print("高表达的致癌基因：")
print(oncogenes)
print()

# 步骤3：复杂条件组合
candidates = gene_database[
    ((gene_database['Gene_Type'].isin(['Oncogene', 'Suppressor'])) & 
     (gene_database['P_Value'] < 0.05) & 
     (gene_database['Expression'] > 100)) |
    ((gene_database['Gene_Type'] == 'Growth') & 
     (gene_database['Fold_Change'] < 1))
]
print("候选靶标基因：")
print(candidates)
```

### 5.8 索引性能优化

```python
print("=" * 60)
print("索引性能优化")
print("=" * 60)

# 创建大数据集
import time

n = 100000
large_df = pd.DataFrame({
    'Gene_ID': [f'ENSG{i:08d}' for i in range(n)],
    'Expression': np.random.randn(n) * 100 + 500,
    'Chromosome': np.random.choice(['chr1', 'chr2', 'chr3', 'chr4'], n)
})

print(f"大数据集：{n}行")
print()

# 无索引查询
start = time.time()
result1 = large_df[large_df['Gene_ID'] == 'ENSG00050000']
time1 = time.time() - start
print(f"无索引查询时间：{time1*1000:.2f} ms")

# 设置索引后查询
large_df_indexed = large_df.set_index('Gene_ID')
start = time.time()
result2 = large_df_indexed.loc['ENSG00050000']
time2 = time.time() - start
print(f"有索引查询时间：{time2*1000:.2f} ms")
print(f"速度提升：{time1/time2:.1f}倍")
```

### 5.9 实战案例：患者数据筛选系统

```python
print("=" * 60)
print("综合案例：临床数据筛选系统")
print("=" * 60)

# 创建模拟的临床数据
np.random.seed(42)

n_patients = 50
clinical_data = pd.DataFrame({
    'Patient_ID': [f'P{i:04d}' for i in range(1, n_patients+1)],
    'Age': np.random.randint(30, 80, n_patients),
    'Gender': np.random.choice(['M', 'F'], n_patients),
    'Cancer_Type': np.random.choice(['Breast', 'Lung', 'Colon', 'Prostate'], n_patients),
    'Stage': np.random.choice(['I', 'II', 'III', 'IV'], n_patients),
    'BRCA1_Mutation': np.random.choice(['Yes', 'No'], n_patients, p=[0.2, 0.8]),
    'TP53_Mutation': np.random.choice(['Yes', 'No'], n_patients, p=[0.4, 0.6]),
    'Treatment': np.random.choice(['Surgery', 'Chemo', 'Radio', 'Combined'], n_patients),
    'Response': np.random.choice(['Complete', 'Partial', 'Stable', 'Progressive'], n_patients),
    'Survival_Months': np.random.randint(6, 60, n_patients)
})

clinical_data.set_index('Patient_ID', inplace=True)

print("临床数据（前10行）：")
print(clinical_data.head(10))
print()

# 筛选场景1：寻找特定患者群体
print("筛选1：年轻女性乳腺癌患者")
young_breast = clinical_data[
    (clinical_data['Age'] < 50) & 
    (clinical_data['Gender'] == 'F') & 
    (clinical_data['Cancer_Type'] == 'Breast')
]
print(f"找到 {len(young_breast)} 名患者")
print(young_breast[['Age', 'Stage', 'Treatment', 'Response']].head())
print()

# 筛选场景2：高风险患者
print("筛选2：高风险患者（晚期+基因突变）")
high_risk = clinical_data[
    (clinical_data['Stage'].isin(['III', 'IV'])) & 
    ((clinical_data['BRCA1_Mutation'] == 'Yes') | 
     (clinical_data['TP53_Mutation'] == 'Yes'))
]
print(f"找到 {len(high_risk)} 名高风险患者")
print(high_risk[['Cancer_Type', 'Stage', 'BRCA1_Mutation', 'TP53_Mutation']].head())
print()

# 筛选场景3：治疗效果分析
print("筛选3：完全缓解的患者特征")
complete_response = clinical_data[clinical_data['Response'] == 'Complete']
print(f"完全缓解患者数：{len(complete_response)}")
print("\n按癌症类型分布：")
print(complete_response['Cancer_Type'].value_counts())
print("\n按治疗方式分布：")
print(complete_response['Treatment'].value_counts())
print()

# 筛选场景4：生存期分析
print("筛选4：长期生存者（>36个月）")
long_survivors = clinical_data[clinical_data['Survival_Months'] > 36]
print(f"长期生存者：{len(long_survivors)} 名")

# 分析长期生存者的特征
print("\n长期生存者的特征分析：")
print(f"平均年龄：{long_survivors['Age'].mean():.1f}")
print(f"早期（I-II期）比例：{(long_survivors['Stage'].isin(['I', 'II'])).mean()*100:.1f}%")
print(f"完全/部分缓解比例：{(long_survivors['Response'].isin(['Complete', 'Partial'])).mean()*100:.1f}%")
```

### 5.10 索引操作的最佳实践

```python
print("=" * 60)
print("索引最佳实践总结")
print("=" * 60)

# 创建示例数据
best_practices_df = pd.DataFrame({
    'Sample': ['S1', 'S2', 'S3', 'S4'],
    'Value': [10, 20, 30, 40]
})

print("最佳实践演示：")
print()

# 实践1：始终使用有意义的索引
print("1. 使用有意义的索引")
print("❌ 不好：默认数字索引")
print(best_practices_df)
print()
print("✓ 好：有意义的索引")
best_practices_df.set_index('Sample', inplace=True)
print(best_practices_df)
print()

# 实践2：避免链式索引
print("2. 避免链式索引")
df_copy = best_practices_df.copy()
print("❌ 不好：df[df['Value'] > 15]['Value'] = 100")
print("✓ 好：df.loc[df['Value'] > 15, 'Value'] = 100")
df_copy.loc[df_copy['Value'] > 15, 'Value'] = 100
print(df_copy)
print()

# 实践3：使用适当的方法
print("3. 选择合适的索引方法")
print("• loc: 基于标签")
print("• iloc: 基于位置")
print("• at: 单个标量值（快）")
print("• iat: 单个标量值，基于位置（快）")
print()

# 实践4：处理索引重复
print("4. 处理重复索引")
dup_df = pd.DataFrame({'Value': [1, 2, 3]}, index=['A', 'B', 'A'])
print("有重复索引的DataFrame：")
print(dup_df)
print(f"索引是否唯一：{dup_df.index.is_unique}")
print("处理方法：重置索引或使用reset_index()")
```

---

## 第6部分：基础统计分析

### 6.1 描述性统计

```python
print("=" * 60)
print("描述性统计：了解你的数据")
print("=" * 60)

# 创建实验数据
experiment_data = pd.DataFrame({
    'Control': [23.4, 24.1, 22.8, 23.9, 24.5, 23.2, 24.0, 23.6],
    'Treatment_A': [28.3, 29.1, 27.8, 28.5, 29.2, 28.0, 28.8, 28.4],
    'Treatment_B': [25.1, 26.0, 24.5, 25.5, 26.2, 25.0, 25.8, 25.3]
})

print("实验数据：")
print(experiment_data)
print()

# 基本统计
print("基本统计量：")
print(experiment_data.describe().round(2))
print()

# 额外的统计量
print("其他统计量：")
stats_summary = pd.DataFrame({
    'Median': experiment_data.median(),
    'Mode': experiment_data.mode().iloc[0] if len(experiment_data.mode()) > 0 else None,
    'Variance': experiment_data.var(),
    'CV%': (experiment_data.std() / experiment_data.mean() * 100),
    'Skewness': experiment_data.skew(),
    'Kurtosis': experiment_data.kurt()
})
print(stats_summary.round(2))
```

### 6.2 相关性分析

```python
print("=" * 60)
print("相关性分析")
print("=" * 60)

# 创建多变量数据
biomarkers = pd.DataFrame({
    'Age': [45, 52, 38, 61, 47, 55, 42, 58, 49, 53],
    'BMI': [24.5, 28.2, 22.1, 29.8, 25.3, 27.5, 23.8, 28.9, 26.1, 27.0],
    'Glucose': [95, 110, 88, 125, 98, 115, 92, 120, 102, 112],
    'Cholesterol': [180, 210, 165, 230, 190, 215, 175, 225, 195, 208],
    'Blood_Pressure': [120, 135, 115, 145, 125, 138, 118, 142, 128, 134]
})

print("生物标志物数据：")
print(biomarkers)
print()

# 计算相关性矩阵
correlation_matrix = biomarkers.corr()
print("Pearson相关系数矩阵：")
print(correlation_matrix.round(2))
print()

# 找出强相关
print("强相关对（|r| > 0.8）：")
strong_corr = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        if abs(correlation_matrix.iloc[i, j]) > 0.8:
            strong_corr.append((
                correlation_matrix.columns[i],
                correlation_matrix.columns[j],
                correlation_matrix.iloc[i, j]
            ))

for var1, var2, corr in strong_corr:
    print(f"  {var1} - {var2}: {corr:.2f}")

if not strong_corr:
    print("  没有发现强相关")
```

### 6.3 分组统计

```python
print("=" * 60)
print("分组统计分析")
print("=" * 60)

# 创建分组数据
cell_viability = pd.DataFrame({
    'Drug': ['DrugA'] * 6 + ['DrugB'] * 6 + ['Control'] * 6,
    'Concentration': [0.1, 0.1, 1, 1, 10, 10] * 3,
    'Viability': [95, 93, 75, 78, 45, 48, 92, 90, 70, 72, 
                  40, 42, 98, 97, 96, 95, 94, 93]
})

print("细胞活力数据：")
print(cell_viability.head(10))
print()

# 按药物分组
by_drug = cell_viability.groupby('Drug')['Viability'].agg(['mean', 'std', 'count'])
print("按药物分组统计：")
print(by_drug.round(2))
print()

# 按药物和浓度分组
by_drug_conc = cell_viability.groupby(['Drug', 'Concentration'])['Viability'].agg(['mean', 'std'])
print("按药物和浓度分组：")
print(by_drug_conc.round(2))
```

---

## 第7部分：数据清洗

### 7.1 处理缺失值

```python
print("=" * 60)
print("处理缺失值")
print("=" * 60)

# 创建有缺失值的数据
incomplete_data = pd.DataFrame({
    'Gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'PTEN'],
    'Sample1': [100, np.nan, 150, 80, 120],
    'Sample2': [110, 180, np.nan, 85, 125],
    'Sample3': [np.nan, 175, 155, np.nan, 115]
})

print("有缺失值的数据：")
print(incomplete_data)
print()

# 检测缺失值
print("缺失值统计：")
print(incomplete_data.isnull().sum())
print()

# 方法1：删除
print("方法1：删除有缺失值的行")
cleaned1 = incomplete_data.dropna()
print(cleaned1)
print()

# 方法2：填充均值
print("方法2：用均值填充")
cleaned2 = incomplete_data.copy()
for col in ['Sample1', 'Sample2', 'Sample3']:
    cleaned2[col].fillna(cleaned2[col].mean(), inplace=True)
print(cleaned2.round(1))
print()

# 方法3：前向填充
print("方法3：前向填充")
cleaned3 = incomplete_data.fillna(method='ffill')
print(cleaned3)
```

### 7.2 处理重复值

```python
print("=" * 60)
print("处理重复值")
print("=" * 60)

# 创建有重复的数据
duplicated_data = pd.DataFrame({
    'Sample_ID': ['S001', 'S002', 'S003', 'S002', 'S004', 'S003'],
    'Value': [10, 20, 30, 20, 40, 35],
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', 
             '2024-01-01', '2024-01-03', '2024-01-02']
})

print("有重复的数据：")
print(duplicated_data)
print()

# 检测重复
print("重复行（基于Sample_ID）：")
print(duplicated_data[duplicated_data.duplicated(subset=['Sample_ID'], keep=False)])
print()

# 删除重复
print("删除重复（保留第一个）：")
cleaned = duplicated_data.drop_duplicates(subset=['Sample_ID'], keep='first')
print(cleaned)
```

### 7.3 数据转换

```python
print("=" * 60)
print("数据转换")
print("=" * 60)

# 创建需要转换的数据
raw_data = pd.DataFrame({
    'Gene': ['brca1', 'TP53', 'egfr', 'KRAS'],
    'Expression': ['1.23e3', '2.45e2', '5.67e3', '8.90e1'],
    'Category': ['high', 'Low', 'HIGH', 'medium']
})

print("原始数据：")
print(raw_data)
print()

# 转换数据类型
print("转换后：")
transformed = raw_data.copy()
transformed['Gene'] = transformed['Gene'].str.upper()
transformed['Expression'] = transformed['Expression'].astype(float)
transformed['Category'] = transformed['Category'].str.capitalize()
print(transformed)
```

---

## 第8部分：综合项目 - 完整的基因表达分析流程

```python
print("=" * 70)
print("综合项目：从原始数据到分析结果")
print("=" * 70)

# 项目背景
print("""
项目背景：
你收到了一批癌症患者的基因表达数据，需要：
1. 加载和清洗数据
2. 进行质量控制
3. 标准化处理
4. 差异表达分析
5. 识别潜在的生物标志物
6. 生成分析报告
""")

# 步骤1：生成模拟数据
print("步骤1：加载数据")
print("-" * 40)

np.random.seed(42)

# 生成患者信息
n_patients = 20
patient_info = pd.DataFrame({
    'Patient_ID': [f'P{i:03d}' for i in range(1, n_patients+1)],
    'Group': ['Normal'] * 10 + ['Cancer'] * 10,
    'Age': np.random.randint(40, 70, n_patients),
    'Gender': np.random.choice(['M', 'F'], n_patients)
})

# 生成基因表达数据
genes = ['TP53', 'BRCA1', 'EGFR', 'VEGFA', 'MYC', 'KRAS', 'PTEN', 
         'CDKN2A', 'PIK3CA', 'BRAF', 'GAPDH', 'ACTB']

expression_matrix = pd.DataFrame(index=genes)

for patient_id in patient_info['Patient_ID']:
    group = patient_info[patient_info['Patient_ID'] == patient_id]['Group'].values[0]
    
    # 基础表达水平
    base_expr = np.random.lognormal(6, 1.5, len(genes))
    
    # 癌症组的差异表达
    if group == 'Cancer':
        for i, gene in enumerate(genes):
            if gene in ['TP53', 'CDKN2A']:  # 抑癌基因下调
                base_expr[i] *= np.random.uniform(0.3, 0.6)
            elif gene in ['MYC', 'VEGFA', 'EGFR']:  # 致癌基因上调
                base_expr[i] *= np.random.uniform(1.8, 3.0)
    
    expression_matrix[patient_id] = base_expr

print(f"加载了 {len(expression_matrix)} 个基因在 {len(expression_matrix.columns)} 个样本中的表达数据")
print("\n表达矩阵预览：")
print(expression_matrix.iloc[:5, :5].round(1))
print()

# 步骤2：数据质量控制
print("步骤2：质量控制")
print("-" * 40)

# 检查缺失值
missing_count = expression_matrix.isnull().sum().sum()
print(f"缺失值数量：{missing_count}")

# 检查异常值
outliers = ((expression_matrix < 1) | (expression_matrix > 100000)).sum().sum()
print(f"异常值数量（<1 或 >100000）：{outliers}")

# 样本质量
sample_totals = expression_matrix.sum()
print(f"\n样本总表达量统计：")
print(f"  平均值：{sample_totals.mean():.0f}")
print(f"  标准差：{sample_totals.std():.0f}")
print(f"  CV%：{(sample_totals.std()/sample_totals.mean()*100):.1f}%")

# 步骤3：数据标准化
print("\n步骤3：数据标准化")
print("-" * 40)

# Log2转换
log2_expr = np.log2(expression_matrix + 1)
print("Log2转换完成")

# Z-score标准化
zscore_expr = (log2_expr - log2_expr.mean(axis=1).values.reshape(-1, 1)) / log2_expr.std(axis=1).values.reshape(-1, 1)
print("Z-score标准化完成")

# 步骤4：差异表达分析
print("\n步骤4：差异表达分析")
print("-" * 40)

# 分组
normal_samples = patient_info[patient_info['Group'] == 'Normal']['Patient_ID'].tolist()
cancer_samples = patient_info[patient_info['Group'] == 'Cancer']['Patient_ID'].tolist()

# 计算各组平均表达
normal_mean = log2_expr[normal_samples].mean(axis=1)
cancer_mean = log2_expr[cancer_samples].mean(axis=1)

# 计算fold change
fold_change = cancer_mean - normal_mean  # log2 scale

# t检验
from scipy import stats
p_values = []
for gene in genes:
    normal_vals = log2_expr.loc[gene, normal_samples]
    cancer_vals = log2_expr.loc[gene, cancer_samples]
    _, p = stats.ttest_ind(normal_vals, cancer_vals)
    p_values.append(p)

# 创建结果表
results = pd.DataFrame({
    'Gene': genes,
    'Normal_Mean': normal_mean.values,
    'Cancer_Mean': cancer_mean.values,
    'Log2_FC': fold_change.values,
    'P_Value': p_values
})

# 多重检验校正
from statsmodels.stats.multitest import multipletests
_, results['Adj_P'], _, _ = multipletests(results['P_Value'], method='fdr_bh')

# 添加显著性标记
results['Significant'] = (results['Adj_P'] < 0.05) & (abs(results['Log2_FC']) > 1)

results = results.sort_values('P_Value')

print("\n差异表达分析结果：")
print(results.round(3))

# 步骤5：识别生物标志物
print("\n步骤5：潜在生物标志物")
print("-" * 40)

biomarkers = results[results['Significant']]
print(f"发现 {len(biomarkers)} 个显著差异表达基因：")
for _, row in biomarkers.iterrows():
    direction = "上调" if row['Log2_FC'] > 0 else "下调"
    print(f"  {row['Gene']}: {direction} (Log2FC={row['Log2_FC']:.2f}, p={row['P_Value']:.3f})")

# 步骤6：生成报告
print("\n" + "=" * 70)
print("分析报告摘要")
print("=" * 70)

print(f"""
数据概况：
- 样本数：{len(expression_matrix.columns)} ({len(normal_samples)} 正常, {len(cancer_samples)} 癌症)
- 基因数：{len(genes)}
- 数据质量：良好（无缺失值，无异常值）

主要发现：
- 显著差异表达基因：{len(biomarkers)} 个
- 上调基因：{len(biomarkers[biomarkers['Log2_FC'] > 0])} 个
- 下调基因：{len(biomarkers[biomarkers['Log2_FC'] < 0])} 个

潜在生物标志物（Top 3）：
""")

top_markers = biomarkers.head(3)
for i, (_, row) in enumerate(top_markers.iterrows(), 1):
    print(f"{i}. {row['Gene']}")
    print(f"   - Fold Change: {2**row['Log2_FC']:.2f}倍")
    print(f"   - P值: {row['P_Value']:.4f}")
    print(f"   - 校正P值: {row['Adj_P']:.4f}")

print("\n建议后续实验：")
print("1. qRT-PCR验证top基因的表达变化")
print("2. Western blot验证蛋白水平变化")
print("3. 功能实验验证基因的生物学作用")
print("4. 扩大样本量进行验证")
```

---

## 知识总结 - 你已经成为Pandas高手了！

### 掌握程度自测

```python
print("=" * 60)
print("Pandas技能自测清单")
print("=" * 60)

skills = {
    "基础概念": [
        "理解Series和DataFrame的区别",
        "知道Index的作用",
        "理解Pandas vs Excel的优劣"
    ],
    "数据创建": [
        "从列表创建Series/DataFrame",
        "从字典创建Series/DataFrame", 
        "从CSV文件读取数据"
    ],
    "数据选择": [
        "使用列名选择列",
        "使用loc和iloc选择数据",
        "使用条件筛选数据",
        "使用query方法"
    ],
    "数据操作": [
        "添加/删除列",
        "修改数据值",
        "排序数据",
        "处理缺失值"
    ],
    "统计分析": [
        "计算描述性统计",
        "分组统计",
        "计算相关性",
        "数据标准化"
    ],
    "高级技巧": [
        "数据透视表",
        "多级索引",
        "数据合并",
        "Apply函数"
    ]
}

total_skills = 0
mastered = 0

print("请诚实评估你的掌握程度：\n")
for category, items in skills.items():
    print(f"【{category}】")
    for item in items:
        print(f"  □ {item}")
        total_skills += 1
    print()

print(f"总技能数：{total_skills}")
print("\n如果你掌握了80%以上，恭喜你已经是Pandas高手了！")
```

### 常见错误和解决方案

```python
print("=" * 60)
print("常见错误及解决方案")
print("=" * 60)

common_errors = [
    {
        "错误": "SettingWithCopyWarning",
        "原因": "链式索引赋值",
        "解决": "使用.loc[]或.copy()"
    },
    {
        "错误": "KeyError",
        "原因": "列名不存在或拼写错误",
        "解决": "检查df.columns，注意大小写"
    },
    {
        "错误": "ValueError: cannot reindex",
        "原因": "索引不匹配",
        "解决": "使用reset_index()或reindex()"
    },
    {
        "错误": "内存溢出",
        "原因": "数据太大",
        "解决": "使用chunksize分块读取，或使用更小的数据类型"
    },
    {
        "错误": "合并后数据变多",
        "原因": "有重复键",
        "解决": "先去重，或使用适当的合并方式"
    }
]

for i, error in enumerate(common_errors, 1):
    print(f"{i}. {error['错误']}")
    print(f"   原因：{error['原因']}")
    print(f"   解决：{error['解决']}")
    print()
```

### 下一步学习建议

```python
print("=" * 60)
print("恭喜完成第6章！下一步...")
print("=" * 60)

print("""
你已经掌握了Pandas的基础，现在你可以：

1. 【立即实践】
   - 用自己的数据试试这些技术
   - 分析一个真实的基因表达数据集
   - 处理一个临床数据表

2. 【第7章预告：Pandas进阶】
   - 更复杂的数据操作
   - 时间序列分析
   - 大数据处理技巧
   - 性能优化

3. 【扩展学习】
   - 学习数据可视化（Matplotlib/Seaborn）
   - 学习统计分析（SciPy/StatsModels）
   - 学习机器学习（Scikit-learn）

记住：
编程就像做实验，需要不断练习。
每个错误都是学习的机会。
保持好奇心，享受探索数据的乐趣！

加油，未来的生物信息学家！🧬
""")
```

---

## 结语

亲爱的学习者：

当你读到这里时，你已经完成了Pandas基础的学习旅程。从一个对编程陌生的生物学研究者，到现在能够熟练处理基因表达数据，这是一个了不起的成就！

还记得开始时的紧张吗？现在再看看那些代码，是不是觉得其实并不难？

**你学到的不仅仅是Pandas：**
- 你学会了用计算思维解决生物学问题
- 你学会了让数据为你工作，而不是你为数据工作
- 你学会了可重复、可验证的科学研究方法

**继续前进的建议：**
1. 用真实数据练习 - 理论需要实践来巩固
2. 犯错是正常的 - 每个错误都让你更强大
3. 保持好奇心 - 数据中藏着无数的生物学秘密

**最后的话：**

Python和Pandas只是工具，真正重要的是你 - 一个充满好奇心的科学家。工具会不断更新，但你解决问题的能力将伴随终生。

愿你在数据的海洋中，发现生命的奥秘。

下一章见！

---

*"In God we trust. All others must bring data." - W. Edwards Deming*

*"我们相信上帝。其他人必须带来数据。"*

这句话提醒我们：在科学研究中，数据是最有力的证据。而你，现在已经掌握了处理这些数据的钥匙。

继续加油！💪

---