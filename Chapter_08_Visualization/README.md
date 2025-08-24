# Chapter 08: 数据可视化 - 让实验结果说话

## 写在最前面 - 给每一位研究者的信

亲爱的研究者：

还记得第一次看到Western blot条带时的兴奋吗？还记得第一次在显微镜下看到荧光信号时的激动吗？数据可视化就是将这些激动人心的发现转化为清晰、专业的科学语言。

在实验室里，我们用各种仪器"看见"生物学现象：
- 凝胶成像系统让我们看见DNA条带
- 流式细胞仪让我们看见细胞群体
- 显微镜让我们看见细胞结构
- 测序仪让我们看见基因表达

而Python的数据可视化，就是将这些"看见"转化为可以发表、可以分享、可以让全世界理解的图表。

**为什么这一章如此重要？**

因为无论你的实验做得多么完美，数据分析多么深入，如果不能清晰地展示结果，就像把珍贵的实验样本锁在冰箱里 - 没有人能看到它的价值。

在这一章，我们将一起学习：
- 如何选择最合适的图表类型（就像选择最合适的实验方法）
- 如何制作从草图到发表级别的专业图表
- 如何让你的数据"说话"，讲述科学故事
- 如何确保每个人（包括色盲读者）都能理解你的图表

让我们开始这段"让数据可见"的旅程吧！

---

## 本章导航 - 你的学习地图

### 🎯 学习目标
```
初级目标（第1-3天）
├── 理解数据可视化的本质
├── 掌握matplotlib基础操作
├── 学会选择合适的图表类型
└── 制作简单清晰的科研图表

中级目标（第4-5天）
├── 掌握专业配色方案
├── 制作复杂的生物信息学图表
├── 学会图表美化和优化
└── 理解期刊投稿要求

高级目标（第6-7天）
├── 制作发表级别的组合图
├── 掌握交互式可视化
├── 建立自己的图表模板库
└── 能独立完成论文配图
```

### 📚 章节结构
```
本章内容
├── 1. 为什么数据可视化如此重要（认知篇）
├── 2. matplotlib基础 - 你的画笔（基础篇）
├── 3. 图表类型选择指南（方法篇）
├── 4. 生物信息学专业图表（应用篇）
├── 5. 配色方案与设计原则（美学篇）
├── 6. 从草图到发表（进阶篇）
├── 7. 多面板组合图制作（高级篇）
├── 8. 综合项目实战（实战篇）
└── 9. 练习与思考（巩固篇）
```

### 🛠️ 本章工具箱
```python
核心库：
- matplotlib: 基础绘图引擎
- seaborn: 统计图表增强
- pandas: 数据处理
- numpy: 数值计算
- scipy: 统计分析

可选库：
- plotly: 交互式图表
- bokeh: Web可视化
- altair: 声明式可视化
```

---

## 第1部分：为什么数据可视化如此重要

### 1.1 一张图胜过千言万语

想象这个场景：你刚完成了一个为期6个月的RNA-seq实验，分析了10000个基因在5个时间点的表达变化。现在组会上，导师问："你发现了什么？"

**选项A：口头描述**
"嗯...在0小时，基因A的表达量是100，2小时后变成了150，4小时是200...然后基因B在0小时是80，2小时是60..."

**选项B：数据表格**
```
Gene    0h    2h    4h    6h    8h
GeneA   100   150   200   180   160
GeneB   80    60    40    45    50
GeneC   120   125   130   128   126
...（还有9997行）
```

**选项C：一张时间序列图**
清晰展示三类基因的表达模式：上调、下调、无变化

显然，选项C最有效！这就是数据可视化的力量。

### 1.2 科研图表的三个层次

```
层次1：探索性图表（给自己看）
目的：快速了解数据分布和模式
特点：简单、快速、不需要美化
场景：日常数据分析

层次2：展示性图表（给同行看）
目的：在组会、学术会议上展示
特点：清晰、专业、重点突出
场景：PPT演示、海报展示

层次3：发表级图表（给审稿人看）
目的：发表在学术期刊
特点：规范、精确、可重复
场景：论文投稿、学位论文
```

### 1.3 图表 = 实验结果的展示窗口

就像实验室的展示橱窗：
- **橱窗玻璃** = 图表框架（要透明、不影响观看）
- **展品摆放** = 数据布局（要有逻辑、易于理解）
- **标签说明** = 图例和注释（要准确、完整）
- **灯光效果** = 颜色和样式（要专业、不喧宾夺主）

---

## 第2部分：matplotlib基础 - 你的科研画笔

### 2.1 认识matplotlib：图表的基本结构

matplotlib就像实验室的显微镜：
- **Figure（画布）** = 载玻片
- **Axes（坐标轴）** = 视野
- **Plot（图形）** = 样本
- **Legend（图例）** = 标记

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建你的第一个科研图表
# 就像准备显微镜观察一样

# 1. 准备载玻片（创建画布）
fig = plt.figure(figsize=(8, 6))  # 8英寸宽，6英寸高

# 2. 调整视野（添加坐标轴）
ax = fig.add_subplot(111)  # 1行1列的第1个图

# 3. 放置样本（绘制数据）
time_points = [0, 2, 4, 6, 8, 12, 24]  # 时间点（小时）
gene_expression = [100, 120, 150, 180, 160, 140, 130]  # 基因表达量

ax.plot(time_points, gene_expression, 'o-', color='#0173B2', 
        linewidth=2, markersize=8, label='Gene A')

# 4. 添加标记（标签和标题）
ax.set_xlabel('Time (hours)', fontsize=12, fontweight='bold')
ax.set_ylabel('Expression Level (FPKM)', fontsize=12, fontweight='bold')
ax.set_title('Gene Expression Time Course', fontsize=14, fontweight='bold')

# 5. 添加图例
ax.legend(loc='best', frameon=True)

# 6. 添加网格（可选，但有助于读数）
ax.grid(True, alpha=0.3, linestyle='--')

# 展示结果
plt.tight_layout()  # 自动调整布局，防止标签重叠
plt.show()

# 保存图片（发表级别）
# plt.savefig('gene_expression.pdf', dpi=300, bbox_inches='tight')
```

### 2.2 图表元素详解 - 每个部分都很重要

#### 2.2.1 坐标轴（Axes）- 数据的参考系

```python
# 坐标轴就像实验的对照组，提供参考标准

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 示例1：线性坐标轴（最常用）
ax1 = axes[0, 0]
x = np.linspace(0, 10, 100)
y = 2 * x + 5
ax1.plot(x, y)
ax1.set_title('Linear Scale\n(线性坐标轴 - 用于大部分数据)')
ax1.set_xlabel('Concentration (μM)')
ax1.set_ylabel('Absorbance (OD600)')

# 示例2：对数坐标轴（用于跨越多个数量级的数据）
ax2 = axes[0, 1]
x = np.logspace(0, 4, 100)  # 10^0 到 10^4
y = x ** 2
ax2.loglog(x, y)  # 双对数坐标
ax2.set_title('Log Scale\n(对数坐标轴 - 用于病毒载量、细胞计数等)')
ax2.set_xlabel('Viral Load (copies/mL)')
ax2.set_ylabel('Antibody Titer')
ax2.grid(True, which="both", alpha=0.3)

# 示例3：双Y轴（展示两个不同量纲的变量）
ax3 = axes[1, 0]
time = np.arange(0, 25, 1)
od600 = np.exp(time * 0.1)  # 细菌生长曲线
glucose = 10 - time * 0.3    # 葡萄糖消耗

color = '#0173B2'
ax3.plot(time, od600, color=color, linewidth=2)
ax3.set_xlabel('Time (hours)')
ax3.set_ylabel('OD600', color=color)
ax3.tick_params(axis='y', labelcolor=color)

ax3_twin = ax3.twinx()  # 创建共享X轴的第二个Y轴
color = '#DE8F05'
ax3_twin.plot(time, glucose, color=color, linewidth=2)
ax3_twin.set_ylabel('Glucose (g/L)', color=color)
ax3_twin.tick_params(axis='y', labelcolor=color)
ax3.set_title('Dual Y-axis\n(双Y轴 - 展示相关但量纲不同的数据)')

# 示例4：极坐标（用于周期性数据）
ax4 = plt.subplot(2, 2, 4, projection='polar')
theta = np.linspace(0, 2*np.pi, 24)  # 24小时
r = 5 + 3*np.sin(3*theta)  # 模拟昼夜节律基因表达
ax4.plot(theta, r, linewidth=2)
ax4.set_title('Polar Coordinates\n(极坐标 - 用于昼夜节律等周期性数据)')
ax4.set_theta_zero_location('N')  # 0点在顶部
ax4.set_theta_direction(-1)  # 顺时针

plt.tight_layout()
plt.show()
```

#### 2.2.2 图例（Legend）- 你的图表说明书

```python
# 图例就像实验记录本的标注，让人知道每条线代表什么

fig, ax = plt.subplots(figsize=(10, 6))

# 生成多组数据
time = np.linspace(0, 24, 100)
control = 100 * np.ones_like(time) + np.random.normal(0, 5, len(time))
treatment_a = 100 * (1 + 0.5 * time/24) + np.random.normal(0, 8, len(time))
treatment_b = 100 * (1 - 0.3 * time/24) + np.random.normal(0, 6, len(time))
treatment_c = 100 * np.exp(-time/10) + np.random.normal(0, 7, len(time))

# 绘制数据（注意每条线都有清晰的label）
ax.plot(time, control, label='Control', 
        color='#808080', linewidth=2, linestyle='-')
ax.plot(time, treatment_a, label='Drug A (Activator)', 
        color='#D55E00', linewidth=2, linestyle='-')
ax.plot(time, treatment_b, label='Drug B (Mild Inhibitor)', 
        color='#0173B2', linewidth=2, linestyle='-')
ax.plot(time, treatment_c, label='Drug C (Strong Inhibitor)', 
        color='#009E73', linewidth=2, linestyle='-')

# 设置图例的最佳实践
ax.legend(
    loc='best',  # 自动选择最佳位置
    frameon=True,  # 显示边框
    fancybox=False,  # 不要圆角（更专业）
    shadow=False,  # 不要阴影（期刊不喜欢）
    ncol=1,  # 单列显示
    fontsize=10,
    title='Treatment Groups',
    title_fontsize=11
)

ax.set_xlabel('Time (hours)', fontsize=12)
ax.set_ylabel('Cell Viability (%)', fontsize=12)
ax.set_title('Drug Response Time Course', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

# 添加注释说明关键点
ax.annotate('IC50 reached', 
            xy=(10, 60), xytext=(14, 40),
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
            fontsize=10, color='red')

plt.tight_layout()
plt.show()
```

#### 2.2.3 颜色选择 - 不只是好看那么简单

```python
# 颜色就像实验中的染料，要选择合适的，确保每个人都能看清

import matplotlib.patches as mpatches

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 1. 顺序配色（Sequential）- 用于连续数据
ax1 = axes[0, 0]
data = np.random.randn(10, 10).cumsum(axis=0)
im1 = ax1.imshow(data, cmap='Blues', aspect='auto')
ax1.set_title('Sequential Colormap\n(顺序配色 - 用于浓度、表达量等)')
plt.colorbar(im1, ax=ax1, label='Expression Level')

# 2. 发散配色（Diverging）- 用于有中心点的数据
ax2 = axes[0, 1]
data_centered = np.random.randn(10, 10)
im2 = ax2.imshow(data_centered, cmap='RdBu_r', aspect='auto', 
                  vmin=-3, vmax=3, center=0)
ax2.set_title('Diverging Colormap\n(发散配色 - 用于上调/下调、正/负)')
plt.colorbar(im2, ax=ax2, label='Log2 Fold Change')

# 3. 分类配色（Qualitative）- 用于分类数据
ax3 = axes[0, 2]
categories = ['Control', 'Treatment A', 'Treatment B', 'Treatment C']
values = [100, 150, 80, 120]
colors_qual = ['#E69F00', '#56B4E9', '#009E73', '#F0E442']
bars = ax3.bar(categories, values, color=colors_qual)
ax3.set_title('Qualitative Colors\n(分类配色 - 用于不同组别)')
ax3.set_ylabel('Measurement')

# 4. 色盲友好配色展示
ax4 = axes[1, 0]
# Wong色盲友好配色方案
wong_colors = ['#E69F00', '#56B4E9', '#009E73', 
               '#F0E442', '#0072B2', '#D55E00', '#CC79A7']
y_pos = np.arange(len(wong_colors))
for i, color in enumerate(wong_colors):
    ax4.barh(i, 1, color=color, height=0.8)
    ax4.text(0.5, i, f'Color {i+1}', ha='center', va='center', 
             color='white' if i in [4, 5] else 'black', fontweight='bold')
ax4.set_xlim(0, 1)
ax4.set_ylim(-0.5, len(wong_colors)-0.5)
ax4.set_title('Colorblind-Friendly Palette\n(色盲友好配色 - Wong方案)')
ax4.set_yticks([])
ax4.set_xticks([])

# 5. 不推荐的配色（反面教材）
ax5 = axes[1, 1]
bad_colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
values_bad = [100, 120, 80, 110, 90, 105]
ax5.bar(range(len(values_bad)), values_bad, color=bad_colors)
ax5.set_title('NOT Recommended\n(不推荐 - 红绿色盲无法区分)')
ax5.set_ylabel('Value')
ax5.set_xlabel('Category')

# 6. 配色使用指南
ax6 = axes[1, 2]
ax6.axis('off')
guidelines = """
配色选择指南：

1. 顺序配色（浓度、强度）
   - Blues, Greens, Oranges
   
2. 发散配色（正负、上下调）
   - RdBu_r, PiYG, PRGn
   
3. 分类配色（不同组别）
   - Set2, Set3, Paired
   
4. 永远测试色盲友好性
   - 使用在线工具检查
   - 避免红-绿组合
   
5. 保持一致性
   - 全文使用同一配色方案
"""
ax6.text(0.1, 0.9, guidelines, transform=ax6.transAxes,
         fontsize=11, verticalalignment='top')

plt.suptitle('Color Selection Guide for Scientific Figures', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 2.3 基础图表类型实战

#### 2.3.1 散点图 - 探索变量关系

```python
# 散点图就像在培养皿上数菌落，每个点都是一个独立的观察

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 示例1：基础散点图 - 基因表达相关性
ax1 = axes[0, 0]
np.random.seed(42)
gene1 = np.random.normal(100, 20, 200)
gene2 = 0.8 * gene1 + np.random.normal(0, 15, 200)

ax1.scatter(gene1, gene2, alpha=0.6, s=30, color='#0173B2', edgecolors='black', linewidth=0.5)
ax1.set_xlabel('Gene A Expression (FPKM)')
ax1.set_ylabel('Gene B Expression (FPKM)')
ax1.set_title('Basic Scatter Plot\n(基础散点图 - 展示相关性)')

# 添加相关系数
from scipy import stats
r, p = stats.pearsonr(gene1, gene2)
ax1.text(0.05, 0.95, f'r = {r:.3f}\np < 0.001', transform=ax1.transAxes,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 示例2：分组散点图 - 不同条件的比较
ax2 = axes[0, 1]
control_x = np.random.normal(50, 10, 100)
control_y = np.random.normal(50, 10, 100)
treatment_x = np.random.normal(70, 12, 100)
treatment_y = np.random.normal(80, 15, 100)

ax2.scatter(control_x, control_y, alpha=0.6, s=40, color='#0173B2', 
           label='Control', edgecolors='black', linewidth=0.5)
ax2.scatter(treatment_x, treatment_y, alpha=0.6, s=40, color='#DE8F05', 
           label='Treatment', edgecolors='black', linewidth=0.5)
ax2.set_xlabel('Protein A Level')
ax2.set_ylabel('Protein B Level')
ax2.set_title('Grouped Scatter Plot\n(分组散点图 - 比较不同条件)')
ax2.legend()

# 示例3：气泡图 - 三维信息展示
ax3 = axes[1, 0]
x = np.random.normal(100, 20, 50)
y = np.random.normal(100, 20, 50)
sizes = np.random.uniform(20, 500, 50)  # 第三维：细胞大小
colors = np.random.uniform(0, 100, 50)  # 第四维：荧光强度

scatter = ax3.scatter(x, y, s=sizes, c=colors, alpha=0.6, 
                      cmap='viridis', edgecolors='black', linewidth=0.5)
ax3.set_xlabel('Forward Scatter')
ax3.set_ylabel('Side Scatter')
ax3.set_title('Bubble Plot\n(气泡图 - 多维信息展示)')
plt.colorbar(scatter, ax=ax3, label='Fluorescence Intensity')

# 示例4：带置信椭圆的散点图
ax4 = axes[1, 1]
from matplotlib.patches import Ellipse
from scipy.stats import chi2

def confidence_ellipse(x, y, ax, n_std=2.0, **kwargs):
    """添加置信椭圆"""
    mean = [np.mean(x), np.mean(y)]
    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      **kwargs)
    
    scale_x = np.sqrt(cov[0, 0]) * n_std
    scale_y = np.sqrt(cov[1, 1]) * n_std
    
    transf = transforms.Affine2D() \
        .scale(scale_x, scale_y) \
        .translate(mean[0], mean[1])
    
    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

# 生成两组数据
group1_x = np.random.multivariate_normal([100, 100], [[200, 50], [50, 200]], 100)
group2_x = np.random.multivariate_normal([150, 80], [[300, -100], [-100, 250]], 100)

ax4.scatter(group1_x[:, 0], group1_x[:, 1], alpha=0.5, color='#0173B2', label='WT')
ax4.scatter(group2_x[:, 0], group2_x[:, 1], alpha=0.5, color='#DE8F05', label='Mutant')

# 添加95%置信椭圆
confidence_ellipse(group1_x[:, 0], group1_x[:, 1], ax4, n_std=2,
                  alpha=0.2, facecolor='#0173B2', edgecolor='#0173B2', linewidth=2)
confidence_ellipse(group2_x[:, 0], group2_x[:, 1], ax4, n_std=2,
                  alpha=0.2, facecolor='#DE8F05', edgecolor='#DE8F05', linewidth=2)

ax4.set_xlabel('Parameter 1')
ax4.set_ylabel('Parameter 2')
ax4.set_title('Scatter with Confidence Ellipses\n(带置信椭圆的散点图)')
ax4.legend()

plt.tight_layout()
plt.show()
```

#### 2.3.2 线图 - 展示趋势变化

```python
# 线图就像记录细菌生长曲线，展示随时间的变化

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 示例1：基础线图 - 生长曲线
ax1 = axes[0, 0]
time = np.linspace(0, 24, 100)
od600 = 0.1 * np.exp(0.2 * time) / (1 + np.exp(0.2 * (time - 12)))  # Logistic growth

ax1.plot(time, od600, linewidth=2, color='#0173B2')
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('OD600')
ax1.set_title('Growth Curve\n(生长曲线)')
ax1.grid(True, alpha=0.3)

# 标记关键生长阶段
ax1.axvspan(0, 4, alpha=0.2, color='green', label='Lag phase')
ax1.axvspan(4, 12, alpha=0.2, color='orange', label='Log phase')
ax1.axvspan(12, 24, alpha=0.2, color='red', label='Stationary phase')
ax1.legend(loc='upper left')

# 示例2：多条线图 - 剂量响应
ax2 = axes[0, 1]
doses = np.logspace(-3, 2, 100)
ic50_values = [0.1, 0.5, 1.0, 5.0]
colors = ['#0173B2', '#DE8F05', '#029E73', '#CC78BC']

for ic50, color in zip(ic50_values, colors):
    response = 100 / (1 + (doses/ic50))
    ax2.semilogx(doses, response, linewidth=2, color=color, 
                 label=f'IC50 = {ic50} μM')

ax2.set_xlabel('Drug Concentration (μM)')
ax2.set_ylabel('Cell Viability (%)')
ax2.set_title('Dose-Response Curves\n(剂量响应曲线)')
ax2.legend()
ax2.grid(True, alpha=0.3, which='both')

# 示例3：带误差线的线图
ax3 = axes[0, 2]
time_points = np.array([0, 2, 4, 6, 8, 12, 24])
mean_values = np.array([100, 120, 150, 145, 130, 110, 105])
std_values = np.array([5, 8, 12, 10, 9, 7, 6])

ax3.errorbar(time_points, mean_values, yerr=std_values,
             fmt='o-', linewidth=2, markersize=8,
             color='#0173B2', ecolor='gray', 
             capsize=5, capthick=2,
             label='Mean ± SD (n=3)')

ax3.set_xlabel('Time (hours)')
ax3.set_ylabel('Gene Expression (FPKM)')
ax3.set_title('Time Course with Error Bars\n(带误差线的时间序列)')
ax3.legend()
ax3.grid(True, alpha=0.3)

# 示例4：面积图 - 展示累积或比例
ax4 = axes[1, 0]
time = np.linspace(0, 24, 100)
phase_g1 = 40 + 10 * np.sin(time/24 * 2 * np.pi)
phase_s = 30 + 5 * np.cos(time/24 * 2 * np.pi)
phase_g2m = 100 - phase_g1 - phase_s

ax4.fill_between(time, 0, phase_g1, alpha=0.7, color='#0173B2', label='G1 phase')
ax4.fill_between(time, phase_g1, phase_g1+phase_s, alpha=0.7, color='#DE8F05', label='S phase')
ax4.fill_between(time, phase_g1+phase_s, 100, alpha=0.7, color='#029E73', label='G2/M phase')

ax4.set_xlabel('Time (hours)')
ax4.set_ylabel('Cell Population (%)')
ax4.set_title('Cell Cycle Distribution\n(细胞周期分布)')
ax4.legend(loc='upper right')
ax4.set_ylim(0, 100)

# 示例5：带标注的线图
ax5 = axes[1, 1]
time = np.array([0, 1, 2, 3, 4, 5, 6])
treatment_response = np.array([100, 98, 85, 60, 40, 45, 50])

ax5.plot(time, treatment_response, 'o-', linewidth=2, markersize=8, color='#D55E00')

# 标注关键事件
ax5.annotate('Drug added', xy=(1, 98), xytext=(1.5, 105),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, color='red', fontweight='bold')

ax5.annotate('Min response', xy=(4, 40), xytext=(4.5, 25),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2),
            fontsize=10, color='blue', fontweight='bold')

ax5.axhline(y=50, color='gray', linestyle='--', alpha=0.5)
ax5.text(6.2, 50, 'IC50', fontsize=10, va='center')

ax5.set_xlabel('Time (hours)')
ax5.set_ylabel('Cell Viability (%)')
ax5.set_title('Annotated Time Course\n(带标注的时间序列)')
ax5.set_ylim(0, 110)
ax5.grid(True, alpha=0.3)

# 示例6：平滑曲线拟合
ax6 = axes[1, 2]
from scipy.interpolate import make_interp_spline

# 原始数据点
x_points = np.array([0, 2, 4, 6, 8, 10, 12])
y_points = np.array([0, 15, 35, 50, 55, 52, 50])

# 创建平滑曲线
x_smooth = np.linspace(x_points.min(), x_points.max(), 300)
spl = make_interp_spline(x_points, y_points, k=3)  # 三次样条
y_smooth = spl(x_smooth)

ax6.scatter(x_points, y_points, color='#D55E00', s=50, zorder=5, label='Observed data')
ax6.plot(x_smooth, y_smooth, color='#0173B2', linewidth=2, label='Fitted curve')

ax6.set_xlabel('Time (days)')
ax6.set_ylabel('Tumor Volume (mm³)')
ax6.set_title('Smoothed Curve Fitting\n(平滑曲线拟合)')
ax6.legend()
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

#### 2.3.3 柱状图 - 比较不同类别

```python
# 柱状图就像比较不同试管中的液体高度，直观展示差异

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 示例1：基础柱状图
ax1 = axes[0, 0]
categories = ['Control', 'Drug A', 'Drug B', 'Drug C']
values = [100, 150, 80, 120]
colors = ['#808080', '#D55E00', '#0173B2', '#029E73']

bars = ax1.bar(categories, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1)

# 在柱子上添加数值
for bar, val in zip(bars, values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
             f'{val}', ha='center', va='bottom', fontweight='bold')

ax1.set_ylabel('Response (%)')
ax1.set_title('Basic Bar Chart\n(基础柱状图)')
ax1.set_ylim(0, 170)

# 示例2：分组柱状图
ax2 = axes[0, 1]
labels = ['Gene A', 'Gene B', 'Gene C', 'Gene D']
control_values = [100, 100, 100, 100]
treatment1_values = [150, 80, 120, 90]
treatment2_values = [180, 60, 110, 85]

x = np.arange(len(labels))
width = 0.25

bars1 = ax2.bar(x - width, control_values, width, label='Control', color='#808080')
bars2 = ax2.bar(x, treatment1_values, width, label='Treatment 1', color='#D55E00')
bars3 = ax2.bar(x + width, treatment2_values, width, label='Treatment 2', color='#0173B2')

ax2.set_xlabel('Genes')
ax2.set_ylabel('Expression Level')
ax2.set_title('Grouped Bar Chart\n(分组柱状图)')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.legend()

# 示例3：堆叠柱状图
ax3 = axes[0, 2]
categories = ['Sample 1', 'Sample 2', 'Sample 3', 'Sample 4']
values1 = [20, 35, 30, 25]
values2 = [25, 25, 30, 30]
values3 = [55, 40, 40, 45]

bars1 = ax3.bar(categories, values1, color='#0173B2', label='Species A')
bars2 = ax3.bar(categories, values2, bottom=values1, color='#DE8F05', label='Species B')
bars3 = ax3.bar(categories, values3, bottom=np.array(values1)+np.array(values2), 
                color='#029E73', label='Species C')

ax3.set_ylabel('Relative Abundance (%)')
ax3.set_title('Stacked Bar Chart\n(堆叠柱状图 - 展示组成)')
ax3.legend()
ax3.set_ylim(0, 110)

# 示例4：带误差线的柱状图
ax4 = axes[1, 0]
categories = ['WT', 'Mutant A', 'Mutant B', 'Mutant C']
means = [100, 75, 120, 90]
stds = [10, 8, 15, 12]

bars = ax4.bar(categories, means, yerr=stds, alpha=0.7,
               color='#56B4E9', edgecolor='black', linewidth=1,
               capsize=5, error_kw={'linewidth': 2})

# 添加显著性标记
ax4.plot([0, 1], [115, 115], 'k-', linewidth=1)
ax4.text(0.5, 117, '***', ha='center', fontsize=12)

ax4.plot([0, 2], [140, 140], 'k-', linewidth=1)
ax4.text(1, 142, '*', ha='center', fontsize=12)

ax4.set_ylabel('Protein Level (% of WT)')
ax4.set_title('Bar Chart with Significance\n(带显著性标记的柱状图)')
ax4.set_ylim(0, 150)

# 示例5：水平柱状图
ax5 = axes[1, 1]
go_terms = ['Cell cycle', 'DNA repair', 'Apoptosis', 
            'Metabolism', 'Signal transduction']
enrichment_scores = [4.5, 3.8, 3.2, 2.5, 2.0]

bars = ax5.barh(go_terms, enrichment_scores, color='#029E73', alpha=0.7)

# 添加显著性阈值线
ax5.axvline(x=1.3, color='red', linestyle='--', alpha=0.5, label='P = 0.05')

# 在柱子末端添加数值
for bar, val in zip(bars, enrichment_scores):
    ax5.text(val + 0.1, bar.get_y() + bar.get_height()/2,
             f'{val:.1f}', va='center')

ax5.set_xlabel('-Log₁₀(P-value)')
ax5.set_title('Horizontal Bar Chart\n(水平柱状图 - GO富集分析)')
ax5.legend()

# 示例6：双向柱状图
ax6 = axes[1, 2]
categories = ['Gene 1', 'Gene 2', 'Gene 3', 'Gene 4', 'Gene 5']
upregulation = [2.5, 1.8, 3.2, 0, 2.0]
downregulation = [0, 0, 0, -1.5, -2.3]

bars_up = ax6.bar(categories, upregulation, color='#D55E00', alpha=0.7, label='Up-regulated')
bars_down = ax6.bar(categories, downregulation, color='#0173B2', alpha=0.7, label='Down-regulated')

ax6.axhline(y=0, color='black', linewidth=0.8)
ax6.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
ax6.axhline(y=-1, color='gray', linestyle='--', alpha=0.5)

ax6.set_ylabel('Log₂ Fold Change')
ax6.set_title('Bidirectional Bar Chart\n(双向柱状图 - 上下调基因)')
ax6.legend()
ax6.set_ylim(-3, 4)

plt.tight_layout()
plt.show()
```

---

## 第3部分：生物信息学专业图表

### 3.1 火山图 - 差异表达分析的标配

```python
# 火山图就像火山喷发，显著差异的基因像熔岩一样"喷出"

def create_volcano_plot_tutorial():
    """
    火山图完整教程：从基础到发表级别
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # 生成模拟数据
    np.random.seed(42)
    n_genes = 5000
    
    # 大部分基因无显著变化
    log2_fc = np.random.normal(0, 0.5, n_genes)
    p_values = np.random.uniform(0.001, 1, n_genes)
    
    # 添加显著上调基因
    n_up = 200
    up_idx = np.random.choice(n_genes, n_up, replace=False)
    log2_fc[up_idx] = np.random.normal(2, 0.5, n_up)
    p_values[up_idx] = np.random.exponential(0.0001, n_up)
    
    # 添加显著下调基因
    n_down = 150
    down_idx = np.random.choice(n_genes, n_down, replace=False)
    log2_fc[down_idx] = np.random.normal(-2, 0.5, n_down)
    p_values[down_idx] = np.random.exponential(0.0001, n_down)
    
    # 计算-log10(p-value)
    neg_log10_p = -np.log10(np.clip(p_values, 1e-300, 1))
    
    # 图1：基础火山图
    ax1 = axes[0, 0]
    ax1.scatter(log2_fc, neg_log10_p, alpha=0.5, s=10, c='gray')
    ax1.set_xlabel('Log₂ Fold Change')
    ax1.set_ylabel('-Log₁₀(P-value)')
    ax1.set_title('Step 1: Basic Volcano Plot\n(基础火山图)')
    ax1.grid(True, alpha=0.3)
    
    # 图2：添加阈值线
    ax2 = axes[0, 1]
    ax2.scatter(log2_fc, neg_log10_p, alpha=0.5, s=10, c='gray')
    
    # 阈值线
    fc_threshold = 1.0
    p_threshold = 0.05
    ax2.axhline(y=-np.log10(p_threshold), color='blue', linestyle='--', 
                linewidth=1, alpha=0.5, label='P = 0.05')
    ax2.axvline(x=fc_threshold, color='blue', linestyle='--', 
                linewidth=1, alpha=0.5, label='|FC| = 2')
    ax2.axvline(x=-fc_threshold, color='blue', linestyle='--', 
                linewidth=1, alpha=0.5)
    
    ax2.set_xlabel('Log₂ Fold Change')
    ax2.set_ylabel('-Log₁₀(P-value)')
    ax2.set_title('Step 2: Add Thresholds\n(添加阈值线)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 图3：颜色分类
    ax3 = axes[1, 0]
    
    # 分类基因
    colors = []
    for fc, p in zip(log2_fc, p_values):
        if fc > fc_threshold and p < p_threshold:
            colors.append('#D55E00')  # 上调
        elif fc < -fc_threshold and p < p_threshold:
            colors.append('#0173B2')  # 下调
        else:
            colors.append('#E5E5E5')  # 无显著变化
    
    ax3.scatter(log2_fc, neg_log10_p, alpha=0.6, s=10, c=colors)
    ax3.axhline(y=-np.log10(p_threshold), color='black', 
                linestyle='--', linewidth=1, alpha=0.3)
    ax3.axvline(x=fc_threshold, color='black', 
                linestyle='--', linewidth=1, alpha=0.3)
    ax3.axvline(x=-fc_threshold, color='black', 
                linestyle='--', linewidth=1, alpha=0.3)
    
    ax3.set_xlabel('Log₂ Fold Change')
    ax3.set_ylabel('-Log₁₀(P-value)')
    ax3.set_title('Step 3: Color by Significance\n(按显著性着色)')
    ax3.grid(True, alpha=0.3)
    
    # 图4：发表级别火山图
    ax4 = axes[1, 1]
    
    # 分别绘制不同类别
    ns_mask = np.array([c == '#E5E5E5' for c in colors])
    up_mask = np.array([c == '#D55E00' for c in colors])
    down_mask = np.array([c == '#0173B2' for c in colors])
    
    ax4.scatter(log2_fc[ns_mask], neg_log10_p[ns_mask], 
               alpha=0.5, s=15, c='#E5E5E5', 
               label=f'Not significant (n={ns_mask.sum()})')
    ax4.scatter(log2_fc[up_mask], neg_log10_p[up_mask], 
               alpha=0.7, s=20, c='#D55E00', 
               label=f'Up-regulated (n={up_mask.sum()})')
    ax4.scatter(log2_fc[down_mask], neg_log10_p[down_mask], 
               alpha=0.7, s=20, c='#0173B2', 
               label=f'Down-regulated (n={down_mask.sum()})')
    
    # 阈值线
    ax4.axhline(y=-np.log10(p_threshold), color='black', 
                linestyle='--', linewidth=1, alpha=0.3)
    ax4.axvline(x=fc_threshold, color='black', 
                linestyle='--', linewidth=1, alpha=0.3)
    ax4.axvline(x=-fc_threshold, color='black', 
                linestyle='--', linewidth=1, alpha=0.3)
    
    # 标注最显著的基因
    top_genes_idx = np.argsort(neg_log10_p)[-5:]
    for idx in top_genes_idx:
        ax4.annotate(f'Gene_{idx}', 
                    xy=(log2_fc[idx], neg_log10_p[idx]),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8, 
                    bbox=dict(boxstyle='round,pad=0.3', 
                             fc='yellow', alpha=0.3),
                    arrowprops=dict(arrowstyle='->', 
                                  connectionstyle='arc3,rad=0'))
    
    ax4.set_xlabel('Log₂ Fold Change', fontweight='bold')
    ax4.set_ylabel('-Log₁₀(P-value)', fontweight='bold')
    ax4.set_title('Step 4: Publication-Ready Volcano Plot\n(发表级别火山图)')
    ax4.legend(loc='upper left', frameon=True)
    ax4.grid(True, alpha=0.2)
    
    # 添加统计信息
    ax4.text(0.02, 0.98, 
            f'Total genes: {n_genes:,}\nFC threshold: ±{fc_threshold}\nP-value threshold: {p_threshold}',
            transform=ax4.transAxes, fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.suptitle('Volcano Plot Tutorial: From Basic to Publication-Ready', 
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# 运行教程
create_volcano_plot_tutorial()
```

### 3.2 热图 - 展示表达矩阵的艺术

```python
# 热图就像基因芯片的扫描图像，颜色深浅代表表达强度

def create_heatmap_tutorial():
    """
    热图完整教程：从基础到聚类分析
    """
    fig = plt.figure(figsize=(16, 12))
    
    # 生成示例数据
    np.random.seed(42)
    n_genes = 30
    n_samples = 12
    
    # 创建三种表达模式
    # 模式1：在处理组上调
    pattern1 = np.zeros((10, n_samples))
    pattern1[:, :6] = np.random.normal(5, 0.5, (10, 6))
    pattern1[:, 6:] = np.random.normal(8, 0.5, (10, 6))
    
    # 模式2：在处理组下调
    pattern2 = np.zeros((10, n_samples))
    pattern2[:, :6] = np.random.normal(7, 0.5, (10, 6))
    pattern2[:, 6:] = np.random.normal(4, 0.5, (10, 6))
    
    # 模式3：无变化
    pattern3 = np.random.normal(6, 0.8, (10, n_samples))
    
    # 合并数据
    data = np.vstack([pattern1, pattern2, pattern3])
    
    # 创建基因和样本名称
    gene_names = [f'Gene_{i:02d}' for i in range(1, n_genes + 1)]
    sample_names = [f'Ctrl_{i}' for i in range(1, 7)] + \
                  [f'Treat_{i}' for i in range(1, 7)]
    
    # 子图1：原始数据热图
    ax1 = plt.subplot(2, 3, 1)
    im1 = ax1.imshow(data, aspect='auto', cmap='RdBu_r')
    ax1.set_title('Raw Data Heatmap\n(原始数据热图)')
    ax1.set_xlabel('Samples')
    ax1.set_ylabel('Genes')
    plt.colorbar(im1, ax=ax1, label='Expression')
    
    # 子图2：Z-score标准化热图
    ax2 = plt.subplot(2, 3, 2)
    # Z-score标准化（按行）
    data_zscore = (data - data.mean(axis=1, keepdims=True)) / data.std(axis=1, keepdims=True)
    im2 = ax2.imshow(data_zscore, aspect='auto', cmap='RdBu_r', 
                     vmin=-2, vmax=2)
    ax2.set_title('Z-score Normalized\n(Z-score标准化)')
    ax2.set_xlabel('Samples')
    ax2.set_ylabel('Genes')
    plt.colorbar(im2, ax=ax2, label='Z-score')
    
    # 子图3：添加标签的热图
    ax3 = plt.subplot(2, 3, 3)
    im3 = ax3.imshow(data_zscore[:10, :], aspect='auto', cmap='RdBu_r', 
                     vmin=-2, vmax=2)
    ax3.set_title('With Labels\n(带标签)')
    ax3.set_xticks(range(n_samples))
    ax3.set_xticklabels(sample_names, rotation=45, ha='right')
    ax3.set_yticks(range(10))
    ax3.set_yticklabels(gene_names[:10])
    plt.colorbar(im3, ax=ax3, label='Z-score')
    
    # 子图4-6：使用seaborn创建聚类热图
    import seaborn as sns
    
    # 准备数据
    df = pd.DataFrame(data_zscore, index=gene_names, columns=sample_names)
    
    # 创建样本颜色标注
    sample_colors = ['#4CAF50'] * 6 + ['#FF9800'] * 6
    
    # 子图4：基础聚类热图
    ax4 = plt.subplot(2, 3, 4)
    sns.heatmap(df.iloc[:15, :], cmap='RdBu_r', center=0,
                vmin=-2, vmax=2, ax=ax4,
                cbar_kws={'label': 'Z-score'})
    ax4.set_title('Basic Clustered Heatmap\n(基础聚类热图)')
    
    # 子图5：带树状图的聚类热图
    g = sns.clustermap(df, cmap='RdBu_r', center=0,
                       vmin=-2, vmax=2,
                       col_cluster=False,  # 不对列聚类
                       row_cluster=True,   # 对行聚类
                       col_colors=sample_colors,
                       figsize=(6, 8),
                       cbar_kws={'label': 'Z-score'})
    g.ax_heatmap.set_title('With Dendrogram\n(带聚类树)')
    
    plt.suptitle('Heatmap Tutorial: From Basic to Advanced', 
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

# 运行教程
create_heatmap_tutorial()
```

### 3.3 箱线图 - 数据分布的全景图

```python
# 箱线图就像查看不同批次实验的质量控制图

def create_boxplot_tutorial():
    """
    箱线图完整教程：展示数据分布和统计比较
    """
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # 生成示例数据
    np.random.seed(42)
    
    # 图1：基础箱线图
    ax1 = axes[0, 0]
    data1 = [np.random.normal(100, 20, 100),
             np.random.normal(120, 25, 100),
             np.random.normal(90, 15, 100)]
    
    bp1 = ax1.boxplot(data1, labels=['Control', 'Treatment A', 'Treatment B'])
    ax1.set_ylabel('Expression Level')
    ax1.set_title('Basic Boxplot\n(基础箱线图)')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # 图2：带缺口的箱线图（显示中位数置信区间）
    ax2 = axes[0, 1]
    bp2 = ax2.boxplot(data1, labels=['Control', 'Treatment A', 'Treatment B'],
                      notch=True,  # 添加缺口
                      showmeans=True,  # 显示均值
                      meanprops=dict(marker='D', markeredgecolor='red', 
                                   markerfacecolor='red'))
    ax2.set_ylabel('Expression Level')
    ax2.set_title('Notched Boxplot with Means\n(带缺口和均值的箱线图)')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # 图3：彩色箱线图
    ax3 = axes[0, 2]
    bp3 = ax3.boxplot(data1, labels=['Control', 'Treatment A', 'Treatment B'],
                      patch_artist=True)  # 允许填充颜色
    
    colors = ['#0173B2', '#DE8F05', '#029E73']
    for patch, color in zip(bp3['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax3.set_ylabel('Expression Level')
    ax3.set_title('Colored Boxplot\n(彩色箱线图)')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # 图4：带显著性标记的箱线图
    ax4 = axes[1, 0]
    bp4 = ax4.boxplot(data1, labels=['Control', 'Treatment A', 'Treatment B'],
                      patch_artist=True)
    
    for patch, color in zip(bp4['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # 添加显著性标记
    y_max = 180
    # Control vs Treatment A
    ax4.plot([1, 2], [y_max, y_max], 'k-', linewidth=1)
    ax4.text(1.5, y_max + 2, '***', ha='center', fontsize=12)
    
    # Control vs Treatment B
    ax4.plot([1, 3], [y_max + 15, y_max + 15], 'k-', linewidth=1)
    ax4.text(2, y_max + 17, 'ns', ha='center', fontsize=10)
    
    ax4.set_ylabel('Expression Level')
    ax4.set_title('With Significance Markers\n(带显著性标记)')
    ax4.set_ylim(40, 200)
    ax4.grid(True, alpha=0.3, axis='y')
    
    # 图5：小提琴图（箱线图的升级版）
    ax5 = axes[1, 1]
    parts = ax5.violinplot(data1, positions=[1, 2, 3], 
                           widths=0.7, showmeans=True, showmedians=True)
    
    for pc, color in zip(parts['bodies'], colors):
        pc.set_facecolor(color)
        pc.set_alpha(0.7)
    
    ax5.set_xticks([1, 2, 3])
    ax5.set_xticklabels(['Control', 'Treatment A', 'Treatment B'])
    ax5.set_ylabel('Expression Level')
    ax5.set_title('Violin Plot\n(小提琴图 - 显示完整分布)')
    ax5.grid(True, alpha=0.3, axis='y')
    
    # 图6：群组箱线图
    ax6 = axes[1, 2]
    
    # 生成分组数据
    data_male = [np.random.normal(100, 20, 50),
                 np.random.normal(110, 22, 50),
                 np.random.normal(95, 18, 50)]
    data_female = [np.random.normal(105, 18, 50),
                   np.random.normal(125, 20, 50),
                   np.random.normal(88, 15, 50)]
    
    positions_male = [1, 3, 5]
    positions_female = [1.6, 3.6, 5.6]
    
    bp_male = ax6.boxplot(data_male, positions=positions_male, 
                          widths=0.5, patch_artist=True)
    bp_female = ax6.boxplot(data_female, positions=positions_female, 
                           widths=0.5, patch_artist=True)
    
    # 设置颜色
    for patch in bp_male['boxes']:
        patch.set_facecolor('#0173B2')
        patch.set_alpha(0.7)
    for patch in bp_female['boxes']:
        patch.set_facecolor('#DE8F05')
        patch.set_alpha(0.7)
    
    ax6.set_xticks([1.3, 3.3, 5.3])
    ax6.set_xticklabels(['Control', 'Treatment A', 'Treatment B'])
    ax6.set_ylabel('Expression Level')
    ax6.set_title('Grouped Boxplot\n(分组箱线图)')
    
    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#0173B2', alpha=0.7, label='Male'),
                      Patch(facecolor='#DE8F05', alpha=0.7, label='Female')]
    ax6.legend(handles=legend_elements)
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Boxplot Tutorial: Various Styles and Applications', 
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# 运行教程
create_boxplot_tutorial()
```

---

## 第4部分：图表美化与专业化

### 4.1 配色方案选择指南

```python
def demonstrate_color_palettes():
    """
    专业配色方案展示和选择指南
    """
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    
    # 生成示例数据
    categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    values = np.random.randint(50, 150, len(categories))
    
    # 1. Nature配色方案
    ax1 = axes[0, 0]
    nature_colors = ['#3B4CC0', '#6F9BD1', '#A6CEE3', '#F47E7A', 
                    '#EE442F', '#940000', '#F89217', '#FDDF33']
    bars1 = ax1.bar(categories, values, color=nature_colors[:len(categories)])
    ax1.set_title('Nature Journal Colors\n(Nature期刊配色)', fontweight='bold')
    ax1.set_ylabel('Value')
    
    # 2. Science配色方案
    ax2 = axes[0, 1]
    science_colors = ['#3B4992', '#EE0000', '#008B45', '#631879', 
                     '#008280', '#BB0021', '#5F559B', '#A20056']
    bars2 = ax2.bar(categories, values, color=science_colors[:len(categories)])
    ax2.set_title('Science Journal Colors\n(Science期刊配色)', fontweight='bold')
    ax2.set_ylabel('Value')
    
    # 3. Cell配色方案
    ax3 = axes[0, 2]
    cell_colors = ['#0C5DA5', '#00B945', '#FF9500', '#FF2C00', 
                  '#845B97', '#474747', '#9E9E9E', '#00B5F7']
    bars3 = ax3.bar(categories, values, color=cell_colors[:len(categories)])
    ax3.set_title('Cell Journal Colors\n(Cell期刊配色)', fontweight='bold')
    ax3.set_ylabel('Value')
    
    # 4. Wong色盲友好配色
    ax4 = axes[1, 0]
    wong_colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', 
                  '#0072B2', '#D55E00', '#CC79A7', '#999999']
    bars4 = ax4.bar(categories, values, color=wong_colors[:len(categories)])
    ax4.set_title('Wong Colorblind-Friendly\n(Wong色盲友好配色)', fontweight='bold')
    ax4.set_ylabel('Value')
    
    # 5. Paul Tol配色
    ax5 = axes[1, 1]
    tol_colors = ['#332288', '#88CCEE', '#44AA99', '#117733', 
                 '#999933', '#DDCC77', '#CC6677', '#882255']
    bars5 = ax5.bar(categories, values, color=tol_colors[:len(categories)])
    ax5.set_title('Paul Tol Colors\n(Paul Tol配色)', fontweight='bold')
    ax5.set_ylabel('Value')
    
    # 6. Okabe-Ito配色
    ax6 = axes[1, 2]
    okabe_colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442',
                   '#0072B2', '#D55E00', '#CC79A7', '#000000']
    bars6 = ax6.bar(categories, values, color=okabe_colors[:len(categories)])
    ax6.set_title('Okabe-Ito Colors\n(Okabe-Ito配色)', fontweight='bold')
    ax6.set_ylabel('Value')
    
    # 7. 渐变配色示例
    ax7 = axes[2, 0]
    gradient = plt.cm.viridis(np.linspace(0.2, 0.9, len(categories)))
    bars7 = ax7.bar(categories, values, color=gradient)
    ax7.set_title('Gradient Colors\n(渐变配色)', fontweight='bold')
    ax7.set_ylabel('Value')
    
    # 8. 双色配色（用于二分类）
    ax8 = axes[2, 1]
    binary_colors = ['#0173B2' if i < len(categories)/2 else '#DE8F05' 
                    for i in range(len(categories))]
    bars8 = ax8.bar(categories, values, color=binary_colors)
    ax8.set_title('Binary Colors\n(二分类配色)', fontweight='bold')
    ax8.set_ylabel('Value')
    
    # 9. 配色选择指南
    ax9 = axes[2, 2]
    ax9.axis('off')
    guidelines = """
    配色选择决策树：
    
    1. 数据类型？
       ├─ 连续型 → 渐变色
       ├─ 分类型 → 分类色
       └─ 二分类 → 双色
    
    2. 发表需求？
       ├─ Nature系 → Nature配色
       ├─ Science系 → Science配色
       └─ Cell系 → Cell配色
    
    3. 可访问性？
       └─ 必须色盲友好 → Wong/Tol
    
    4. 打印需求？
       └─ 黑白打印 → 灰度测试
    """
    ax9.text(0.1, 0.9, guidelines, transform=ax9.transAxes,
            fontsize=10, verticalalignment='top', fontfamily='monospace')
    
    plt.suptitle('Professional Color Palettes for Scientific Publication', 
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# 运行演示
demonstrate_color_palettes()
```

### 4.2 图表样式优化

```python
def optimize_figure_style():
    """
    图表样式优化：从普通到专业
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 生成示例数据
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
    y2 = np.cos(x) + np.random.normal(0, 0.1, 100)
    
    # 图1：默认样式（不推荐）
    ax1 = axes[0, 0]
    ax1.plot(x, y1, label='Dataset 1')
    ax1.plot(x, y2, label='Dataset 2')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Default Style (Not Recommended)')
    ax1.legend()
    
    # 图2：基础优化
    ax2 = axes[0, 1]
    ax2.plot(x, y1, linewidth=2, alpha=0.8, label='Dataset 1')
    ax2.plot(x, y2, linewidth=2, alpha=0.8, label='Dataset 2')
    ax2.set_xlabel('Time (s)', fontsize=11)
    ax2.set_ylabel('Signal Intensity', fontsize=11)
    ax2.set_title('Basic Optimization', fontsize=12, fontweight='bold')
    ax2.legend(frameon=True, fancybox=False)
    ax2.grid(True, alpha=0.3)
    
    # 图3：专业优化
    ax3 = axes[1, 0]
    ax3.plot(x, y1, linewidth=2, color='#0173B2', 
            label='Control', alpha=0.9)
    ax3.plot(x, y2, linewidth=2, color='#DE8F05', 
            label='Treatment', alpha=0.9)
    ax3.set_xlabel('Time (s)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Signal Intensity (AU)', fontsize=12, fontweight='bold')
    ax3.set_title('Professional Style', fontsize=13, fontweight='bold')
    ax3.legend(loc='upper right', frameon=True, fancybox=False,
              edgecolor='black', framealpha=0.9)
    ax3.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.tick_params(axis='both', which='major', labelsize=10)
    
    # 图4：发表级别
    ax4 = axes[1, 1]
    
    # 使用误差带
    y1_smooth = np.convolve(y1, np.ones(5)/5, mode='same')
    y2_smooth = np.convolve(y2, np.ones(5)/5, mode='same')
    y1_std = np.random.uniform(0.05, 0.15, len(x))
    y2_std = np.random.uniform(0.05, 0.15, len(x))
    
    ax4.plot(x, y1_smooth, linewidth=2.5, color='#0173B2', 
            label='Control (n=3)', zorder=3)
    ax4.fill_between(x, y1_smooth - y1_std, y1_smooth + y1_std,
                     color='#0173B2', alpha=0.2)
    
    ax4.plot(x, y2_smooth, linewidth=2.5, color='#DE8F05', 
            label='Treatment (n=3)', zorder=3)
    ax4.fill_between(x, y2_smooth - y2_std, y2_smooth + y2_std,
                     color='#DE8F05', alpha=0.2)
    
    ax4.set_xlabel('Time (s)', fontsize=12, fontweight='bold')
    ax4.set_ylabel('Signal Intensity (AU)', fontsize=12, fontweight='bold')
    ax4.set_title('Publication-Ready', fontsize=13, fontweight='bold')
    
    # 精细调整
    ax4.legend(loc='upper right', frameon=True, fancybox=False,
              edgecolor='none', framealpha=0.9, fontsize=10)
    ax4.grid(True, alpha=0.15, linestyle='-', linewidth=0.5, zorder=0)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['left'].set_linewidth(1.2)
    ax4.spines['bottom'].set_linewidth(1.2)
    ax4.tick_params(axis='both', which='major', labelsize=10, 
                   width=1.2, length=5)
    ax4.set_xlim(0, 10)
    
    # 添加注释
    ax4.annotate('Peak response', xy=(1.57, 1.0), xytext=(3, 1.2),
                arrowprops=dict(arrowstyle='->', color='black', lw=1),
                fontsize=9)
    
    plt.suptitle('Figure Style Optimization: From Basic to Publication-Ready',
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# 运行优化演示
optimize_figure_style()
```

---

## 第5部分：多面板组合图制作

### 5.1 完整的Figure设计

```python
def create_complete_figure():
    """
    创建一个完整的多面板Figure，模拟真实论文图表
    主题：药物处理对细胞基因表达的影响
    """
    # 设置整体样式
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['font.size'] = 9
    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams['lines.linewidth'] = 1.5
    
    # 创建图形布局
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3,
                         height_ratios=[1, 1, 1.2],
                         width_ratios=[1, 1, 1])
    
    # 生成模拟数据
    np.random.seed(42)
    
    # Panel A: 实验设计示意图
    ax_a = fig.add_subplot(gs[0, 0])
    ax_a.axis('off')
    ax_a.text(0.5, 0.9, 'A', fontsize=14, fontweight='bold', 
             transform=ax_a.transAxes)
    
    # 绘制实验流程
    flow_text = """
    Experimental Design
    
    Cells (n=3)
        ↓
    ┌─────────┬─────────┐
    │ Control │Treatment│
    └─────────┴─────────┘
         ↓           ↓
    Time points:
    0, 2, 4, 6, 8, 12, 24h
         ↓           ↓
    RNA extraction
         ↓           ↓
    RNA-seq analysis
    """
    ax_a.text(0.5, 0.45, flow_text, transform=ax_a.transAxes,
             fontsize=9, ha='center', va='center',
             fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.3))
    
    # Panel B: 质量控制 - 样本相关性
    ax_b = fig.add_subplot(gs[0, 1])
    ax_b.text(0.05, 0.95, 'B', fontsize=14, fontweight='bold', 
             transform=ax_b.transAxes)
    
    # 生成相关性矩阵
    n_samples = 6
    corr_matrix = np.random.uniform(0.85, 1.0, (n_samples, n_samples))
    np.fill_diagonal(corr_matrix, 1.0)
    corr_matrix = (corr_matrix + corr_matrix.T) / 2
    
    im = ax_b.imshow(corr_matrix, cmap='RdBu_r', vmin=0.8, vmax=1.0)
    ax_b.set_title('Sample Correlation Matrix', fontweight='bold', pad=10)
    ax_b.set_xticks(range(n_samples))
    ax_b.set_yticks(range(n_samples))
    ax_b.set_xticklabels([f'S{i+1}' for i in range(n_samples)])
    ax_b.set_yticklabels([f'S{i+1}' for i in range(n_samples)])
    
    # 添加数值
    for i in range(n_samples):
        for j in range(n_samples):
            text = ax_b.text(j, i, f'{corr_matrix[i, j]:.2f}',
                           ha='center', va='center', color='white' if corr_matrix[i, j] < 0.9 else 'black',
                           fontsize=8)
    
    plt.colorbar(im, ax=ax_b, label='Pearson r')
    
    # Panel C: PCA分析
    ax_c = fig.add_subplot(gs[0, 2])
    ax_c.text(0.05, 0.95, 'C', fontsize=14, fontweight='bold', 
             transform=ax_c.transAxes)
    
    # 生成PCA数据
    control_pc1 = np.random.normal(-20, 5, 3)
    control_pc2 = np.random.normal(0, 5, 3)
    treat_pc1 = np.random.normal(20, 5, 3)
    treat_pc2 = np.random.normal(0, 5, 3)
    
    ax_c.scatter(control_pc1, control_pc2, s=100, color='#0173B2', 
                label='Control', alpha=0.7, edgecolors='black', linewidth=1)
    ax_c.scatter(treat_pc1, treat_pc2, s=100, color='#DE8F05', 
                label='Treatment', alpha=0.7, edgecolors='black', linewidth=1)
    
    ax_c.set_xlabel('PC1 (45% variance)', fontweight='bold')
    ax_c.set_ylabel('PC2 (23% variance)', fontweight='bold')
    ax_c.set_title('Principal Component Analysis', fontweight='bold', pad=10)
    ax_c.legend()
    ax_c.grid(True, alpha=0.3)
    ax_c.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax_c.axvline(x=0, color='gray', linestyle='-', linewidth=0.5)
    
    # Panel D: 火山图
    ax_d = fig.add_subplot(gs[1, :2])
    ax_d.text(0.02, 0.98, 'D', fontsize=14, fontweight='bold', 
             transform=ax_d.transAxes)
    
    # 生成火山图数据
    n_genes = 5000
    log2_fc = np.random.normal(0, 0.5, n_genes)
    p_values = np.random.uniform(0.001, 1, n_genes)
    
    # 添加显著基因
    sig_up = np.random.choice(n_genes, 200, replace=False)
    log2_fc[sig_up] = np.random.normal(2, 0.5, 200)
    p_values[sig_up] = np.random.exponential(0.0001, 200)
    
    sig_down = np.random.choice(n_genes, 150, replace=False)
    log2_fc[sig_down] = np.random.normal(-2, 0.5, 150)
    p_values[sig_down] = np.random.exponential(0.0001, 150)
    
    neg_log10_p = -np.log10(np.clip(p_values, 1e-300, 1))
    
    # 分类并绘制
    colors = []
    for fc, p in zip(log2_fc, p_values):
        if fc > 1 and p < 0.05:
            colors.append('#D55E00')
        elif fc < -1 and p < 0.05:
            colors.append('#0173B2')
        else:
            colors.append('#E5E5E5')
    
    ax_d.scatter(log2_fc, neg_log10_p, c=colors, alpha=0.6, s=10)
    ax_d.axhline(y=-np.log10(0.05), color='black', linestyle='--', 
                linewidth=1, alpha=0.3)
    ax_d.axvline(x=1, color='black', linestyle='--', linewidth=1, alpha=0.3)
    ax_d.axvline(x=-1, color='black', linestyle='--', linewidth=1, alpha=0.3)
    
    ax_d.set_xlabel('Log₂ Fold Change', fontweight='bold', fontsize=11)
    ax_d.set_ylabel('-Log₁₀(P-value)', fontweight='bold', fontsize=11)
    ax_d.set_title('Differential Expression Analysis', fontweight='bold', 
                  fontsize=12, pad=10)
    
    # 添加统计信息
    n_up = sum(1 for c in colors if c == '#D55E00')
    n_down = sum(1 for c in colors if c == '#0173B2')
    ax_d.text(0.02, 0.9, f'Up: {n_up}\nDown: {n_down}', 
             transform=ax_d.transAxes,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Panel E: GO富集分析
    ax_e = fig.add_subplot(gs[1, 2])
    ax_e.text(0.05, 0.95, 'E', fontsize=14, fontweight='bold', 
             transform=ax_e.transAxes)
    
    go_terms = ['Cell cycle', 'DNA repair', 'Apoptosis', 
                'Metabolism', 'Signal\ntransduction']
    enrichment = [4.5, 3.8, 3.2, 2.5, 2.0]
    gene_counts = [45, 38, 32, 25, 20]
    
    bars = ax_e.barh(go_terms, enrichment, color='#029E73', alpha=0.7)
    
    # 添加基因数量标签
    for i, (bar, count) in enumerate(zip(bars, gene_counts)):
        ax_e.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                 f'n={count}', va='center', fontsize=8)
    
    ax_e.axvline(x=1.3, color='red', linestyle='--', alpha=0.5)
    ax_e.text(1.3, -0.5, 'P=0.05', color='red', fontsize=8, ha='center')
    ax_e.set_xlabel('-Log₁₀(P-value)', fontweight='bold')
    ax_e.set_title('GO Enrichment', fontweight='bold', pad=10)
    ax_e.set_xlim(0, 5)
    
    # Panel F: 时间序列热图
    ax_f = fig.add_subplot(gs[2, :])
    ax_f.text(0.01, 0.97, 'F', fontsize=14, fontweight='bold', 
             transform=ax_f.transAxes)
    
    # 生成时间序列数据
    time_points = [0, 2, 4, 6, 8, 12, 24]
    n_genes_heatmap = 50
    
    # 创建不同的表达模式
    early_response = np.zeros((15, len(time_points)))
    for i in range(15):
        peak_time = np.random.choice([1, 2])
        for j, t in enumerate(time_points):
            early_response[i, j] = np.exp(-(t - time_points[peak_time])**2 / 10)
    
    late_response = np.zeros((15, len(time_points)))
    for i in range(15):
        for j, t in enumerate(time_points):
            late_response[i, j] = 1 / (1 + np.exp(-(t - 12) / 2))
    
    sustained = np.zeros((10, len(time_points)))
    for i in range(10):
        sustained[i, :] = np.linspace(0, 1, len(time_points)) + \
                         np.random.normal(0, 0.1, len(time_points))
    
    transient = np.zeros((10, len(time_points)))
    for i in range(10):
        transient[i, :] = -np.linspace(0, 1, len(time_points)) + \
                         np.random.normal(0, 0.1, len(time_points))
    
    # 合并数据
    heatmap_data = np.vstack([early_response, late_response, 
                             sustained, transient])
    
    # Z-score标准化
    heatmap_zscore = (heatmap_data - heatmap_data.mean(axis=1, keepdims=True)) / \
                     (heatmap_data.std(axis=1, keepdims=True) + 1e-8)
    
    im = ax_f.imshow(heatmap_zscore, aspect='auto', cmap='RdBu_r',
                     vmin=-2, vmax=2)
    
    ax_f.set_xticks(range(len(time_points)))
    ax_f.set_xticklabels([f'{t}h' for t in time_points])
    ax_f.set_xlabel('Time after treatment', fontweight='bold', fontsize=11)
    ax_f.set_ylabel('Genes', fontweight='bold', fontsize=11)
    ax_f.set_title('Temporal Expression Patterns', fontweight='bold', 
                  fontsize=12, pad=10)
    
    # 添加聚类标签
    ax_f.text(-1.5, 7.5, 'Early', rotation=90, va='center', fontweight='bold')
    ax_f.text(-1.5, 22.5, 'Late', rotation=90, va='center', fontweight='bold')
    ax_f.text(-1.5, 35, 'Sustained', rotation=90, va='center', fontweight='bold')
    ax_f.text(-1.5, 45, 'Transient', rotation=90, va='center', fontweight='bold')
    
    plt.colorbar(im, ax=ax_f, label='Z-score', pad=0.02)
    
    # 添加总标题
    fig.suptitle('Figure 1. Comprehensive Analysis of Drug Treatment Effects on Gene Expression',
                fontsize=14, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 完整的多面板Figure创建完成")
    print("   包含：实验设计、质控、PCA、火山图、GO富集、时间序列")
    print("   这是一个典型的转录组学分析结果展示")

# 创建完整图表
create_complete_figure()
```

---

## 第6部分：保存和输出设置

### 6.1 不同格式的选择

```python
def demonstrate_save_formats():
    """
    演示不同保存格式的特点和用途
    """
    # 创建一个示例图
    fig, ax = plt.subplots(figsize=(8, 6))
    
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    ax.plot(x, y1, linewidth=2, label='sin(x)', color='#0173B2')
    ax.plot(x, y2, linewidth=2, label='cos(x)', color='#DE8F05')
    ax.set_xlabel('X axis', fontweight='bold')
    ax.set_ylabel('Y axis', fontweight='bold')
    ax.set_title('Example Figure for Format Comparison', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 保存为不同格式
    formats_info = {
        'PDF': {
            'ext': '.pdf',
            'dpi': None,  # 矢量图不需要DPI
            'use': '期刊投稿首选，可无限缩放',
            'pros': '矢量图，文件小，质量高',
            'cons': '不支持透明度渐变'
        },
        'SVG': {
            'ext': '.svg',
            'dpi': None,
            'use': '网页展示，可编辑',
            'pros': '矢量图，可在Illustrator中编辑',
            'cons': '文件可能较大'
        },
        'PNG': {
            'ext': '.png',
            'dpi': 300,
            'use': '网页、PPT、海报',
            'pros': '支持透明背景，兼容性好',
            'cons': '位图，放大会模糊'
        },
        'TIFF': {
            'ext': '.tiff',
            'dpi': 300,
            'use': '某些期刊要求',
            'pros': '无损压缩，颜色准确',
            'cons': '文件很大'
        },
        'EPS': {
            'ext': '.eps',
            'dpi': None,
            'use': '老期刊系统',
            'pros': '矢量图，兼容性好',
            'cons': '不支持透明度'
        }
    }
    
    print("\n📊 图片保存格式对比")
    print("=" * 70)
    
    for format_name, info in formats_info.items():
        filename = f'example_figure{info["ext"]}'
        
        # 保存参数
        save_kwargs = {
            'bbox_inches': 'tight',
            'pad_inches': 0.1
        }
        
        if info['dpi']:
            save_kwargs['dpi'] = info['dpi']
        
        # 实际保存（注释掉以避免创建文件）
        # plt.savefig(filename, **save_kwargs)
        
        print(f"\n{format_name}格式:")
        print(f"  文件名: {filename}")
        print(f"  用途: {info['use']}")
        print(f"  优点: {info['pros']}")
        print(f"  缺点: {info['cons']}")
        if info['dpi']:
            print(f"  推荐DPI: {info['dpi']}")
    
    print("\n💡 选择建议：")
    print("  1. 期刊投稿 → PDF (矢量图)")
    print("  2. PPT演示 → PNG (300 DPI)")
    print("  3. 网页展示 → SVG 或 PNG")
    print("  4. 后期编辑 → SVG")
    print("  5. 存档备份 → PDF + 源代码")
    
    plt.show()

# 运行演示
demonstrate_save_formats()
```

---

## 第7部分：综合项目实战

### 7.1 完整的数据分析可视化流程

```python
def complete_analysis_project():
    """
    综合项目：模拟完整的药物筛选实验数据分析和可视化
    """
    print("\n🔬 综合项目：药物筛选数据分析可视化")
    print("=" * 60)
    
    # 1. 数据准备
    np.random.seed(42)
    
    # 模拟96孔板药物筛选数据
    drugs = ['Drug_' + chr(65+i) for i in range(8)]  # Drug_A 到 Drug_H
    concentrations = [0, 0.1, 0.3, 1, 3, 10, 30, 100]  # μM
    replicates = 3
    
    # 生成剂量响应数据
    data = {}
    for drug in drugs:
        ic50 = np.random.uniform(0.5, 10)  # 随机IC50
        hill = np.random.uniform(0.8, 1.5)  # Hill系数
        
        drug_data = []
        for conc in concentrations:
            if conc == 0:
                response = 100 + np.random.normal(0, 5, replicates)
            else:
                response = 100 / (1 + (conc/ic50)**hill) + \
                          np.random.normal(0, 5, replicates)
            drug_data.append(response)
        
        data[drug] = {
            'concentrations': concentrations,
            'responses': drug_data,
            'ic50_true': ic50,
            'hill_true': hill
        }
    
    # 2. 创建综合分析图
    fig = plt.figure(figsize=(18, 14))
    gs = fig.add_gridspec(4, 3, hspace=0.3, wspace=0.25)
    
    # Panel A: 96孔板热图
    ax_a = fig.add_subplot(gs[0, :2])
    ax_a.text(0.02, 0.95, 'A', fontsize=14, fontweight='bold', 
             transform=ax_a.transAxes, zorder=10)
    
    # 创建96孔板数据
    plate_data = np.random.uniform(20, 100, (8, 12))
    im_a = ax_a.imshow(plate_data, cmap='RdYlGn_r', aspect='auto')
    
    ax_a.set_title('96-Well Plate Heatmap - Cell Viability (%)', 
                  fontweight='bold', pad=10)
    ax_a.set_xticks(range(12))
    ax_a.set_xticklabels(range(1, 13))
    ax_a.set_yticks(range(8))
    ax_a.set_yticklabels(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    ax_a.set_xlabel('Column', fontweight='bold')
    ax_a.set_ylabel('Row', fontweight='bold')
    
    plt.colorbar(im_a, ax=ax_a, label='Viability (%)')
    
    # Panel B: 质量控制 - Z因子
    ax_b = fig.add_subplot(gs[0, 2])
    ax_b.text(0.05, 0.95, 'B', fontsize=14, fontweight='bold', 
             transform=ax_b.transAxes)
    
    plates = ['Plate 1', 'Plate 2', 'Plate 3', 'Plate 4']
    z_factors = [0.65, 0.72, 0.68, 0.75]
    colors_qc = ['red' if z < 0.5 else 'orange' if z < 0.7 else 'green' 
                 for z in z_factors]
    
    bars = ax_b.bar(plates, z_factors, color=colors_qc, alpha=0.7)
    ax_b.axhline(y=0.5, color='red', linestyle='--', alpha=0.5)
    ax_b.axhline(y=0.7, color='green', linestyle='--', alpha=0.5)
    ax_b.set_ylabel("Z' Factor", fontweight='bold')
    ax_b.set_title('Assay Quality Control', fontweight='bold', pad=10)
    ax_b.set_ylim(0, 1)
    
    # 添加标签
    for bar, z in zip(bars, z_factors):
        ax_b.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                 f'{z:.2f}', ha='center', fontsize=9)
    
    # Panel C: 剂量响应曲线
    ax_c = fig.add_subplot(gs[1, :])
    ax_c.text(0.01, 0.95, 'C', fontsize=14, fontweight='bold', 
             transform=ax_c.transAxes)
    
    colors_dr = plt.cm.tab10(np.linspace(0, 1, len(drugs)))
    
    for i, (drug, drug_data) in enumerate(data.items()):
        concs = drug_data['concentrations']
        responses = drug_data['responses']
        
        # 计算均值和标准差
        means = [np.mean(resp) for resp in responses]
        stds = [np.std(resp) for resp in responses]
        
        # 绘制数据点和误差线
        concs_plot = [c if c > 0 else 0.01 for c in concs]  # 处理0浓度
        ax_c.errorbar(concs_plot, means, yerr=stds, 
                     fmt='o-', label=f'{drug} (IC50={drug_data["ic50_true"]:.2f})',
                     color=colors_dr[i], markersize=5, linewidth=1.5,
                     capsize=3, alpha=0.8)
    
    ax_c.set_xscale('log')
    ax_c.set_xlabel('Drug Concentration (μM)', fontweight='bold', fontsize=11)
    ax_c.set_ylabel('Cell Viability (%)', fontweight='bold', fontsize=11)
    ax_c.set_title('Dose-Response Curves', fontweight='bold', fontsize=12, pad=10)
    ax_c.legend(ncol=4, loc='lower left', fontsize=8)
    ax_c.grid(True, alpha=0.3, which='both')
    ax_c.set_ylim(0, 120)
    
    # Panel D: IC50比较
    ax_d = fig.add_subplot(gs[2, 0])
    ax_d.text(0.05, 0.95, 'D', fontsize=14, fontweight='bold', 
             transform=ax_d.transAxes)
    
    ic50_values = [drug_data['ic50_true'] for drug_data in data.values()]
    drug_names_short = [d.replace('Drug_', '') for d in drugs]
    
    bars = ax_d.bar(drug_names_short, ic50_values, color='#56B4E9', alpha=0.7)
    ax_d.set_ylabel('IC₅₀ (μM)', fontweight='bold')
    ax_d.set_xlabel('Drug', fontweight='bold')
    ax_d.set_title('IC₅₀ Comparison', fontweight='bold', pad=10)
    
    # 标记最有效的药物
    min_idx = np.argmin(ic50_values)
    bars[min_idx].set_color('#D55E00')
    bars[min_idx].set_alpha(1.0)
    
    # Panel E: 选择性指数
    ax_e = fig.add_subplot(gs[2, 1])
    ax_e.text(0.05, 0.95, 'E', fontsize=14, fontweight='bold', 
             transform=ax_e.transAxes)
    
    # 模拟选择性数据
    cancer_ic50 = ic50_values
    normal_ic50 = [ic * np.random.uniform(2, 10) for ic in cancer_ic50]
    selectivity = [n/c for n, c in zip(normal_ic50, cancer_ic50)]
    
    ax_e.scatter(cancer_ic50, selectivity, s=100, alpha=0.6, 
                c=range(len(drugs)), cmap='viridis')
    
    # 添加药物标签
    for i, drug in enumerate(drug_names_short):
        ax_e.annotate(drug, (cancer_ic50[i], selectivity[i]),
                     xytext=(5, 5), textcoords='offset points',
                     fontsize=8)
    
    ax_e.axhline(y=10, color='red', linestyle='--', alpha=0.5)
    ax_e.text(8, 10.5, 'High selectivity', color='red', fontsize=8)
    ax_e.set_xlabel('IC₅₀ Cancer Cells (μM)', fontweight='bold')
    ax_e.set_ylabel('Selectivity Index', fontweight='bold')
    ax_e.set_title('Drug Selectivity', fontweight='bold', pad=10)
    ax_e.set_xlim(0, 12)
    
    # Panel F: 协同作用热图
    ax_f = fig.add_subplot(gs[2, 2])
    ax_f.text(0.05, 0.95, 'F', fontsize=14, fontweight='bold', 
             transform=ax_f.transAxes)
    
    # 模拟药物组合效应
    n_drugs_comb = 5
    synergy_matrix = np.random.uniform(-20, 30, (n_drugs_comb, n_drugs_comb))
    np.fill_diagonal(synergy_matrix, 0)
    synergy_matrix = (synergy_matrix + synergy_matrix.T) / 2
    
    im_f = ax_f.imshow(synergy_matrix, cmap='RdBu_r', vmin=-30, vmax=30)
    ax_f.set_title('Drug Combination Effects', fontweight='bold', pad=10)
    ax_f.set_xticks(range(n_drugs_comb))
    ax_f.set_yticks(range(n_drugs_comb))
    ax_f.set_xticklabels(['A', 'B', 'C', 'D', 'E'])
    ax_f.set_yticklabels(['A', 'B', 'C', 'D', 'E'])
    
    plt.colorbar(im_f, ax=ax_f, label='Synergy Score')
    
    # Panel G: 时间依赖性
    ax_g = fig.add_subplot(gs[3, :2])
    ax_g.text(0.02, 0.95, 'G', fontsize=14, fontweight='bold', 
             transform=ax_g.transAxes)
    
    time_points = [0, 6, 12, 24, 48, 72]
    selected_drugs = ['Drug_A', 'Drug_B', 'Drug_C']
    
    for drug in selected_drugs:
        viability = [100]
        for t in time_points[1:]:
            viability.append(100 * np.exp(-t/30) + np.random.normal(0, 5))
        ax_g.plot(time_points, viability, 'o-', label=drug, 
                 linewidth=2, markersize=6)
    
    ax_g.set_xlabel('Time (hours)', fontweight='bold')
    ax_g.set_ylabel('Cell Viability (%)', fontweight='bold')
    ax_g.set_title('Time-Dependent Drug Effects', fontweight='bold', pad=10)
    ax_g.legend()
    ax_g.grid(True, alpha=0.3)
    
    # Panel H: 统计总结
    ax_h = fig.add_subplot(gs[3, 2])
    ax_h.axis('off')
    ax_h.text(0.05, 0.95, 'H', fontsize=14, fontweight='bold', 
             transform=ax_h.transAxes)
    
    summary_text = f"""
    Statistical Summary
    
    Tested drugs: {len(drugs)}
    Concentrations: {len(concentrations)}
    Replicates: {replicates}
    
    Best IC₅₀: {min(ic50_values):.2f} μM
    Average IC₅₀: {np.mean(ic50_values):.2f} μM
    
    Quality Metrics:
    • Avg Z' factor: {np.mean(z_factors):.2f}
    • CV < 20%: Yes
    • R² > 0.95: Yes
    
    Recommendations:
    ✓ Drug {drug_names_short[min_idx]} for further study
    ✓ Combination A+C shows synergy
    ✓ Time point: 24-48h optimal
    """
    
    ax_h.text(0.1, 0.45, summary_text, transform=ax_h.transAxes,
             fontsize=9, fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.2))
    
    # 添加总标题
    fig.suptitle('Figure 2. Comprehensive Drug Screening Analysis Pipeline',
                fontsize=15, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.show()
    
    print("\n✅ 综合项目完成！")
    print("   展示了完整的药物筛选数据分析流程")
    print("   包含8个面板，涵盖质控、剂量响应、选择性等关键分析")

# 运行综合项目
complete_analysis_project()
```

---

## 第8部分：练习预览与学习建议

### 8.1 渐进式练习计划

```python
def practice_roadmap():
    """
    展示循序渐进的练习路线图
    """
    print("\n📚 数据可视化学习路线图")
    print("=" * 60)
    
    roadmap = {
        "Day 1-2: 基础绘图": {
            "目标": "掌握matplotlib基本操作",
            "练习": [
                "绘制第一个散点图",
                "添加标题、标签、图例",
                "保存图片为不同格式",
                "尝试不同的线型和颜色"
            ],
            "关键函数": ["plt.plot()", "plt.scatter()", "plt.xlabel()", "plt.savefig()"]
        },
        
        "Day 3: 统计图表": {
            "目标": "学会展示数据分布",
            "练习": [
                "绘制箱线图比较多组数据",
                "创建直方图查看分布",
                "制作带误差线的柱状图",
                "添加统计显著性标记"
            ],
            "关键函数": ["plt.boxplot()", "plt.hist()", "plt.bar()", "plt.errorbar()"]
        },
        
        "Day 4: 专业图表": {
            "目标": "掌握生物信息学常用图表",
            "练习": [
                "绘制基因表达热图",
                "创建差异分析火山图",
                "制作GO富集柱状图",
                "绘制剂量响应曲线"
            ],
            "关键函数": ["sns.heatmap()", "sns.clustermap()", "scipy.stats"]
        },
        
        "Day 5: 图表美化": {
            "目标": "提升图表专业性",
            "练习": [
                "应用色盲友好配色",
                "调整字体和线宽",
                "优化图表布局",
                "添加专业标注"
            ],
            "关键技巧": ["配色方案", "样式设置", "细节调整"]
        },
        
        "Day 6: 组合图表": {
            "目标": "创建发表级别Figure",
            "练习": [
                "设计多面板布局",
                "统一配色和样式",
                "添加子图标号",
                "制作完整的分析图"
            ],
            "关键函数": ["plt.subplots()", "gridspec", "fig.suptitle()"]
        },
        
        "Day 7: 综合项目": {
            "目标": "完成真实数据分析",
            "练习": [
                "分析RNA-seq数据",
                "创建完整的Figure",
                "准备期刊投稿图表",
                "制作可重复的分析流程"
            ],
            "成果": "一套完整的数据分析图表"
        }
    }
    
    for day, content in roadmap.items():
        print(f"\n{day}")
        print("-" * 40)
        print(f"学习目标: {content['目标']}")
        print("\n练习内容:")
        for practice in content['练习']:
            print(f"  ✓ {practice}")
        
        if '关键函数' in content:
            print(f"\n关键函数: {', '.join(content['关键函数'])}")
        elif '关键技巧' in content:
            print(f"\n关键技巧: {', '.join(content['关键技巧'])}")
        elif '成果' in content:
            print(f"\n最终成果: {content['成果']}")

# 显示学习路线图
practice_roadmap()
```

### 8.2 常见错误与解决方案

```python
def common_mistakes_and_solutions():
    """
    展示常见错误和解决方案
    """
    print("\n⚠️ 常见错误与解决方案")
    print("=" * 60)
    
    mistakes = {
        "1. 中文显示问题": {
            "错误表现": "中文显示为方框或乱码",
            "原因": "matplotlib默认字体不支持中文",
            "解决方案": """
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False
            """
        },
        
        "2. 图例遮挡数据": {
            "错误表现": "图例覆盖了重要数据点",
            "原因": "图例位置设置不当",
            "解决方案": """
# 方法1: 自动选择最佳位置
ax.legend(loc='best')

# 方法2: 放在图外
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            """
        },
        
        "3. 标签重叠": {
            "错误表现": "X轴标签相互重叠",
            "原因": "标签太长或太多",
            "解决方案": """
# 旋转标签
plt.xticks(rotation=45, ha='right')

# 或使用tight_layout
plt.tight_layout()
            """
        },
        
        "4. 颜色不当": {
            "错误表现": "红绿配色，色盲无法区分",
            "原因": "未考虑色盲用户",
            "解决方案": """
# 使用色盲友好配色
colors = ['#0173B2', '#DE8F05', '#029E73']  # 蓝、橙、绿
            """
        },
        
        "5. 分辨率太低": {
            "错误表现": "打印或放大后模糊",
            "原因": "DPI设置太低",
            "解决方案": """
# 保存时设置高DPI
plt.savefig('figure.png', dpi=300, bbox_inches='tight')

# 或使用矢量图
plt.savefig('figure.pdf')
            """
        },
        
        "6. 数据过度拟合": {
            "错误表现": "曲线过度平滑或复杂",
            "原因": "拟合阶数太高",
            "解决方案": """
# 使用合适的拟合阶数
z = np.polyfit(x, y, 2)  # 二次拟合，不要用太高的阶数
            """
        }
    }
    
    for problem, details in mistakes.items():
        print(f"\n{problem}")
        print("-" * 40)
        print(f"错误表现: {details['错误表现']}")
        print(f"原因: {details['原因']}")
        print(f"解决方案:{details['解决方案']}")

# 显示常见错误
common_mistakes_and_solutions()
```

---

## 学习资源与工具推荐

### 📚 推荐阅读
1. **Matplotlib官方教程**: 最权威的学习资源
2. **Seaborn文档**: 统计图表的最佳实践
3. **Scientific Figure Design**: 科研图表设计原则
4. **ColorBrewer**: 配色方案选择工具

### 🛠️ 实用工具
1. **在线配色检查**: colorbrinding.com
2. **图表类型选择器**: data-to-viz.com
3. **期刊图表要求**: 各大期刊的Author Guidelines
4. **图表灵感库**: Nature、Science、Cell的Figure展示

### 💡 专业建议
1. **保持简洁**: 少即是多，避免过度装饰
2. **保持一致**: 全文使用统一的样式和配色
3. **考虑读者**: 永远站在读者角度思考
4. **反复修改**: 好图表是改出来的，不是画出来的

---

## 本章小结 - 你已经掌握的技能

恭喜你！完成本章学习后，你已经掌握了：

### ✅ 基础技能
- 使用matplotlib创建各种基础图表
- 理解图表的组成元素和设置方法
- 选择合适的图表类型展示数据
- 保存不同格式的图片文件

### ✅ 进阶技能
- 制作专业的科研图表（火山图、热图等）
- 应用色盲友好的配色方案
- 创建多面板组合图
- 优化图表样式达到发表标准

### ✅ 专业素养
- 理解期刊对图表的要求
- 知道如何让数据"说话"
- 能够制作可重复的图表
- 建立了自己的图表模板库

### 🎯 下一步建议

1. **实践项目**: 用真实数据制作一套完整的图表
2. **收集模板**: 建立自己的图表代码库
3. **学习进阶**: 探索交互式可视化（plotly、bokeh）
4. **分享交流**: 在组会上展示你的图表，获取反馈

记住：**数据可视化是一门艺术，也是一门科学。**

好的图表不仅准确展示数据，更能讲述引人入胜的科学故事。每一个像素都应该有其目的，每一种颜色都应该传达信息。

继续前进，让你的数据发光发亮！

---

## 下一章预告

在掌握了数据可视化后，下一章我们将学习**Biopython** - 专门为生物信息学设计的Python库。你将学会：

- 处理各种生物序列格式（FASTA、GenBank等）
- 进行序列比对和BLAST搜索
- 访问在线生物数据库
- 构建系统发育树
- 分析蛋白质结构

准备好进入更专业的生物信息学领域了吗？让我们继续前进！

---

*"A picture is worth a thousand words, but a good scientific figure is worth a thousand experiments."*

*"一图胜千言，一张好的科研图表胜过千次实验。"*