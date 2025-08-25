# Chapter 06: Pandas入门 - 实验数据的电子表格

## 📖 写在最前面 - 给生物学研究者

还记得你第一次用Excel分析实验数据时的痛苦吗？数据一多就卡死，公式拖错了也不知道，三个月后重做分析简直是噩梦...

今天，我们要学习一个强大的工具 - **Pandas**，它就像是程序员的Excel，但功能强大百倍。

**为什么需要Pandas？**
- Excel崩溃，Pandas不会
- Excel手工操作易错，Pandas可重复
- Excel处理不了大数据，Pandas轻松搞定
- Excel协作困难，Pandas代码就是文档

## 🎯 学习目标

完成本章后你将能够：
- 理解Series和DataFrame的核心概念  
- 创建、读取和操作数据表格
- 进行数据筛选、排序和分组统计
- 处理缺失值和数据清洗
- 完成基础的统计分析

## 🧬 核心概念 - 用生物学类比理解

```
生物实验室              Pandas世界
│                      │
├─ 试管架     ═══════>  Series（一维数据）
├─ 96孔板     ═══════>  DataFrame（二维数据表）  
├─ 样品标签   ═══════>  Index（索引）
└─ 实验记录本 ═══════>  DataFrame（完整数据集）
```

## 📊 第一部分：Series - 你的数字试管架

### 1.1 什么是Series？

Series就像一个试管架，每个位置放一个数据，每个位置都有标签：

```python
import pandas as pd

# 创建细胞生长曲线数据
time_points = pd.Series(
    data=[1e4, 2e4, 4e4, 8e4, 1.6e5],
    index=['0h', '6h', '12h', '18h', '24h']
)

print("细胞生长曲线：")
print(time_points)
```

输出：
```
0h      10000.0
6h      20000.0  
12h     40000.0
18h     80000.0
24h    160000.0
dtype: float64
```

### 1.2 Series的基本操作

```python
# 创建抗体浓度数据
antibodies = pd.Series({
    'Anti-GAPDH': 1.5,
    'Anti-Actin': 2.0,
    'Anti-Tubulin': 1.2,
    'Anti-p53': 0.8
})

print("抗体浓度：")
print(antibodies)

# 访问数据
print(f"GAPDH抗体浓度: {antibodies['Anti-GAPDH']} mg/ml")

# 筛选数据
high_conc = antibodies[antibodies > 1.5]
print("高浓度抗体:")
print(high_conc)

# 基础统计
print(f"平均浓度: {antibodies.mean():.2f} mg/ml")
print(f"最高浓度: {antibodies.max():.2f} mg/ml")
```

### 1.3 实战案例：酶活性分析

```python
# 酶活性测定结果
enzyme_activity = pd.Series({
    'Amylase': 125.3,      # 淀粉酶
    'Protease': 89.7,      # 蛋白酶  
    'Lipase': 45.2,        # 脂肪酶
    'Cellulase': 67.8,     # 纤维素酶
})

print("酶活性测定结果（U/ml）:")
print(enzyme_activity)

# 找出最活跃的酶
most_active = enzyme_activity.idxmax()
print(f"最活跃的酶: {most_active} ({enzyme_activity.max():.1f} U/ml)")

# 筛选高活性酶（>80 U/ml）
high_activity = enzyme_activity[enzyme_activity > 80]
print("高活性酶:")
print(high_activity)
```

## 📋 第二部分：DataFrame - 你的数字96孔板

### 2.1 什么是DataFrame？

DataFrame就像96孔板，有行（基因）、列（样本），每个交叉点是一个数据：

```python
# 创建基因表达矩阵
gene_expression = pd.DataFrame({
    'Control_1': [120, 450, 1500],
    'Control_2': [115, 460, 1480], 
    'Treated_1': [220, 340, 1520],
    'Treated_2': [215, 335, 1510]
}, index=['GeneA', 'GeneB', 'GeneC'])

print("基因表达矩阵：")
print(gene_expression)
```

输出：
```
        Control_1  Control_2  Treated_1  Treated_2
GeneA        120        115        220        215
GeneB        450        460        340        335
GeneC       1500       1480       1520       1510
```

### 2.2 DataFrame的基本属性

```python
print(f"数据形状: {gene_expression.shape}")
print(f"行数（基因数）: {gene_expression.shape[0]}")
print(f"列数（样本数）: {gene_expression.shape[1]}")
print(f"列名: {list(gene_expression.columns)}")
print(f"索引: {list(gene_expression.index)}")
```

### 2.3 数据选择和筛选

```python
# 选择单列（返回Series）
print("Control_1样本的表达量：")
print(gene_expression['Control_1'])

# 选择多列
print("对照组数据：")
print(gene_expression[['Control_1', 'Control_2']])

# 选择行（用loc）
print("GeneA的表达谱：")
print(gene_expression.loc['GeneA'])

# 条件筛选
print("高表达基因（平均表达>400）：")
mean_expression = gene_expression.mean(axis=1)
high_expr = gene_expression[mean_expression > 400]
print(high_expr)
```

### 2.4 数据计算

```python
# 计算平均值
gene_expression['Control_Mean'] = gene_expression[['Control_1', 'Control_2']].mean(axis=1)
gene_expression['Treated_Mean'] = gene_expression[['Treated_1', 'Treated_2']].mean(axis=1)

# 计算Fold Change
gene_expression['Fold_Change'] = gene_expression['Treated_Mean'] / gene_expression['Control_Mean']

print("添加计算列后：")
print(gene_expression.round(2))
```

## 🔍 第三部分：数据操作

### 3.1 数据筛选技巧

```python
# 创建药物筛选数据
drug_data = pd.DataFrame({
    'Drug': ['DrugA', 'DrugB', 'DrugC', 'DrugD', 'DrugE'],
    'IC50': [0.5, 2.3, 0.1, 5.6, 1.2],
    'Inhibition': [85, 72, 95, 45, 78],
    'Selectivity': ['High', 'Low', 'High', 'Low', 'Medium']
})

print("药物数据：")
print(drug_data)

# 单条件筛选
efficient_drugs = drug_data[drug_data['IC50'] < 1]
print("高效药物（IC50<1）：")
print(efficient_drugs)

# 多条件筛选（AND）
best_drugs = drug_data[
    (drug_data['IC50'] < 1) & 
    (drug_data['Selectivity'] == 'High')
]
print("最佳药物：")
print(best_drugs)

# 使用isin筛选
good_selectivity = drug_data[drug_data['Selectivity'].isin(['High', 'Medium'])]
print("好的选择性药物：")
print(good_selectivity)
```

### 3.2 数据分组统计

```python
# 创建实验数据
experiment = pd.DataFrame({
    'Treatment': ['Control', 'Control', 'DrugA', 'DrugA', 'DrugB', 'DrugB'],
    'Replicate': ['R1', 'R2', 'R1', 'R2', 'R1', 'R2'],
    'Cell_Count': [1e6, 1.1e6, 1.2e6, 1.3e6, 0.8e6, 0.9e6],
    'Viability': [95, 94, 88, 87, 75, 73]
})

print("实验数据：")
print(experiment)

# 按处理分组
by_treatment = experiment.groupby('Treatment')[['Cell_Count', 'Viability']].mean()
print("按处理分组的平均值：")
print(by_treatment)
```

### 3.3 数据清洗

```python
# 创建有问题的数据
messy_data = pd.DataFrame({
    'Gene': ['BRCA1', 'TP53', None, 'EGFR', 'BRCA1'],  # 有缺失值和重复
    'Expression': [100, np.nan, 150, 180, 100],         # 有缺失值
    'Quality': ['Good', 'good', 'GOOD', 'Fair', 'Good'] # 大小写不一致
})

print("原始数据（有问题）：")
print(messy_data)

# 1. 删除缺失值
cleaned = messy_data.dropna()
print("删除缺失值后：")
print(cleaned)

# 2. 删除重复
cleaned = cleaned.drop_duplicates()
print("删除重复后：")
print(cleaned)

# 3. 标准化文本
cleaned['Quality'] = cleaned['Quality'].str.capitalize()
print("标准化后：")
print(cleaned)
```

## 📊 第四部分：统计分析

### 4.1 描述性统计

```python
# 创建实验数据
measurement = pd.DataFrame({
    'Control': [23.4, 24.1, 22.8, 23.9, 24.5],
    'Treatment': [28.3, 29.1, 27.8, 28.5, 29.2]
})

print("测量数据：")
print(measurement)

# 基础统计
print("描述性统计：")
print(measurement.describe())

# 计算变异系数
cv = measurement.std() / measurement.mean() * 100
print(f"变异系数（CV%）：")
print(cv.round(2))
```

### 4.2 相关性分析

```python
# 创建多变量数据
biomarkers = pd.DataFrame({
    'Age': [45, 52, 38, 61, 47],
    'BMI': [24.5, 28.2, 22.1, 29.8, 25.3],
    'Glucose': [95, 110, 88, 125, 98],
    'Cholesterol': [180, 210, 165, 230, 190]
})

# 计算相关性矩阵
correlation = biomarkers.corr()
print("相关性矩阵：")
print(correlation.round(2))

# 找强相关
print("强相关对（|r|>0.7）：")
for i in range(len(correlation.columns)):
    for j in range(i+1, len(correlation.columns)):
        if abs(correlation.iloc[i, j]) > 0.7:
            print(f"{correlation.columns[i]} - {correlation.columns[j]}: {correlation.iloc[i, j]:.2f}")
```

## 🧪 第五部分：综合项目 - 基因表达分析

```python
# 完整的差异表达分析流程
import numpy as np
from scipy import stats

print("="*60)
print("项目：差异表达基因分析")  
print("="*60)

# 1. 创建模拟数据
np.random.seed(42)
genes = ['TP53', 'BRCA1', 'EGFR', 'MYC', 'GAPDH']

# 生成表达数据
expression_data = {}
for i in range(3):  # 3个对照样本
    sample = f'Control_{i+1}'
    expression_data[sample] = np.random.lognormal(5, 1, len(genes))

for i in range(3):  # 3个处理样本
    sample = f'Treated_{i+1}'
    base = np.random.lognormal(5, 1, len(genes))
    # 模拟某些基因的差异表达
    base[0] *= 2.5  # TP53上调
    base[1] *= 0.4  # BRCA1下调
    base[3] *= 3.0  # MYC上调
    expression_data[sample] = base

# 创建DataFrame
expr_df = pd.DataFrame(expression_data, index=genes)
print("表达矩阵：")
print(expr_df.round(1))

# 2. 差异分析
control_cols = [c for c in expr_df.columns if 'Control' in c]
treated_cols = [c for c in expr_df.columns if 'Treated' in c]

# 计算平均值和Fold Change
expr_df['Control_Mean'] = expr_df[control_cols].mean(axis=1)
expr_df['Treated_Mean'] = expr_df[treated_cols].mean(axis=1)  
expr_df['Fold_Change'] = expr_df['Treated_Mean'] / expr_df['Control_Mean']
expr_df['Log2_FC'] = np.log2(expr_df['Fold_Change'])

# t检验
p_values = []
for gene in genes:
    ctrl_vals = expr_df.loc[gene, control_cols]
    treat_vals = expr_df.loc[gene, treated_cols]
    _, p_val = stats.ttest_ind(ctrl_vals, treat_vals)
    p_values.append(p_val)

expr_df['P_Value'] = p_values

# 3. 结果展示
result = expr_df[['Control_Mean', 'Treated_Mean', 'Log2_FC', 'P_Value']]
result = result.sort_values('P_Value')

print("\n差异表达分析结果：")
print(result.round(3))

# 4. 识别显著差异基因
significant = result[(abs(result['Log2_FC']) > 1) & (result['P_Value'] < 0.05)]
print(f"\n发现 {len(significant)} 个显著差异基因：")
for gene, row in significant.iterrows():
    direction = "上调" if row['Log2_FC'] > 0 else "下调"
    print(f"  {gene}: {direction} ({row['Log2_FC']:.2f} fold, p={row['P_Value']:.3f})")
```

## 📚 本章总结

### 核心概念回顾

| 概念 | 类比 | 作用 | 示例 |
|------|------|------|------|
| **Series** | 试管架 | 一维数据容器 | `pd.Series([1,2,3])` |
| **DataFrame** | 96孔板 | 二维数据表格 | `pd.DataFrame(data)` |
| **Index** | 样品标签 | 数据标识符 | `df.index` |
| **loc** | 按标签选择 | 精确定位 | `df.loc['gene1']` |
| **groupby** | 分组统计 | 分类分析 | `df.groupby('type')` |

### 最佳实践

✅ **总是使用有意义的索引**
```python
df.set_index('Gene_Symbol')  # 而不是默认0,1,2...
```

✅ **用链式操作保持代码清洁**
```python
result = (df
    .dropna()
    .groupby('Treatment')
    .mean()
    .round(2))
```

✅ **处理数据前先了解数据**
```python
print(df.info())        # 数据类型和缺失值
print(df.describe())    # 数值统计  
print(df.head())        # 查看前几行
```

## 🚀 下一步

恭喜！你已经掌握了Pandas的基础。现在你可以：

- 轻松处理基因表达数据
- 进行质量控制和数据清洗
- 执行基础统计分析
- 筛选和分组数据

**下一章预告**：我们将学习数据可视化，让你的分析结果更直观！

---

*"数据是新时代的石油，而Pandas就是你的炼油厂。现在，你已经学会了如何提炼出有价值的洞察。"*

**—— 你的生物信息学导师**