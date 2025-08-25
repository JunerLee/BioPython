# Chapter 08: 数据可视化 - 让数据说话

## 📖 写在最前面 

在生物学研究中，数据可视化就像显微镜一样重要——它让我们"看见"数据中隐藏的规律。无论你的实验多么精彩，如果不能清晰地展示结果，就无法传达科学发现的价值。

## 🎯 学习目标

完成本章后你将能够：

✅ **基础绘图** - 掌握matplotlib核心操作  
✅ **专业图表** - 制作火山图、热图等生信常用图表  
✅ **配色美化** - 应用色盲友好的专业配色  
✅ **发表标准** - 创建符合期刊要求的组合图  

## 🛠️ 核心工具

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats
```

---

## 🧬 第一部分：Matplotlib基础

### 1.1 第一个科研图表

```python
import matplotlib.pyplot as plt
import numpy as np

print("🔬 创建你的第一个科研图表")
print("="*50)

# 模拟基因表达数据
time_points = [0, 2, 4, 6, 8, 12, 24]  # 小时
gene_expression = [100, 120, 150, 180, 160, 140, 130]  # 表达量

# 创建图表
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制数据
ax.plot(time_points, gene_expression, 'o-', 
        color='#0173B2', linewidth=2, markersize=8, 
        label='Gene A')

# 添加标签
ax.set_xlabel('Time (hours)', fontsize=12, fontweight='bold')
ax.set_ylabel('Expression Level (FPKM)', fontsize=12, fontweight='bold')
ax.set_title('Gene Expression Time Course', fontsize=14, fontweight='bold')

# 添加网格和图例
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(loc='best', frameon=True)

# 保存图表
plt.tight_layout()
plt.show()

# 发表级别保存（可选）
# plt.savefig('gene_expression.pdf', dpi=300, bbox_inches='tight')
```

### 1.2 图表基本元素

```python
print("\n📊 图表元素详解")
print("="*50)

# 创建示例数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
y2 = np.cos(x) + np.random.normal(0, 0.1, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 基础版（不推荐）
ax1.plot(x, y1, label='Dataset 1')
ax1.plot(x, y2, label='Dataset 2')
ax1.set_title('Basic Style')
ax1.legend()

# 专业版（推荐）
ax2.plot(x, y1, linewidth=2, color='#0173B2', 
         label='Control', alpha=0.9)
ax2.plot(x, y2, linewidth=2, color='#DE8F05', 
         label='Treatment', alpha=0.9)
ax2.set_xlabel('Time (s)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Signal Intensity (AU)', fontsize=11, fontweight='bold')
ax2.set_title('Professional Style', fontsize=12, fontweight='bold')
ax2.legend(loc='upper right', frameon=True, fancybox=False)
ax2.grid(True, alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

print("✅ 专业图表要素：")
print("   • 合适的颜色选择")
print("   • 清晰的标签和标题")
print("   • 简洁的网格和边框")
print("   • 统一的字体大小")
```

---

## 🧬 第二部分：生物信息学专业图表

### 2.1 火山图 - 差异表达分析利器

```python
def create_volcano_plot():
    """
    火山图：展示基因差异表达结果
    横轴：log2 fold change（倍数变化）
    纵轴：-log10 p-value（显著性）
    """
    print("\n🌋 火山图制作")
    print("="*50)
    
    # 生成模拟差异表达数据
    np.random.seed(42)
    n_genes = 3000
    
    # 大部分基因无显著变化
    log2_fc = np.random.normal(0, 0.5, n_genes)
    p_values = np.random.uniform(0.001, 1, n_genes)
    
    # 添加显著上调基因
    n_up = 150
    up_idx = np.random.choice(n_genes, n_up, replace=False)
    log2_fc[up_idx] = np.random.normal(2, 0.5, n_up)
    p_values[up_idx] = np.random.exponential(0.0001, n_up)
    
    # 添加显著下调基因  
    n_down = 120
    down_idx = np.random.choice(n_genes, n_down, replace=False)
    log2_fc[down_idx] = np.random.normal(-2, 0.5, n_down)
    p_values[down_idx] = np.random.exponential(0.0001, n_down)
    
    # 计算-log10(p-value)
    neg_log10_p = -np.log10(np.clip(p_values, 1e-300, 1))
    
    # 分类基因
    fc_threshold = 1.0
    p_threshold = 0.05
    colors = []
    
    for fc, p in zip(log2_fc, p_values):
        if fc > fc_threshold and p < p_threshold:
            colors.append('#D55E00')  # 上调：橙红色
        elif fc < -fc_threshold and p < p_threshold:
            colors.append('#0173B2')  # 下调：蓝色
        else:
            colors.append('#E5E5E5')  # 无显著变化：灰色
    
    # 绘制火山图
    fig, ax = plt.subplots(figsize=(10, 8))
    
    ax.scatter(log2_fc, neg_log10_p, c=colors, alpha=0.6, s=15)
    
    # 添加阈值线
    ax.axhline(y=-np.log10(p_threshold), color='black', 
               linestyle='--', linewidth=1, alpha=0.5)
    ax.axvline(x=fc_threshold, color='black', 
               linestyle='--', linewidth=1, alpha=0.5)
    ax.axvline(x=-fc_threshold, color='black', 
               linestyle='--', linewidth=1, alpha=0.5)
    
    # 美化图表
    ax.set_xlabel('Log₂ Fold Change', fontweight='bold', fontsize=12)
    ax.set_ylabel('-Log₁₀(P-value)', fontweight='bold', fontsize=12)
    ax.set_title('Volcano Plot - Differential Gene Expression', 
                 fontweight='bold', fontsize=14)
    ax.grid(True, alpha=0.2)
    
    # 添加统计信息
    n_up_sig = sum(1 for c in colors if c == '#D55E00')
    n_down_sig = sum(1 for c in colors if c == '#0173B2')
    
    ax.text(0.02, 0.98, 
            f'Up-regulated: {n_up_sig}\nDown-regulated: {n_down_sig}', 
            transform=ax.transAxes, fontsize=10,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
            verticalalignment='top')
    
    plt.tight_layout()
    plt.show()
    
    print(f"✅ 火山图完成！")
    print(f"   显著上调基因: {n_up_sig}")
    print(f"   显著下调基因: {n_down_sig}")

# 运行火山图演示
create_volcano_plot()
```

### 2.2 热图 - 表达模式的艺术展现

```python
def create_expression_heatmap():
    """
    热图：展示基因在不同条件下的表达模式
    """
    print("\n🔥 基因表达热图制作")
    print("="*50)
    
    # 生成模拟基因表达数据
    np.random.seed(42)
    n_genes = 30
    n_samples = 12
    
    # 创建三种表达模式的基因
    # 模式1：在处理组上调
    pattern1 = np.zeros((10, n_samples))
    pattern1[:, :6] = np.random.normal(5, 0.5, (10, 6))  # 对照组
    pattern1[:, 6:] = np.random.normal(8, 0.5, (10, 6))  # 处理组
    
    # 模式2：在处理组下调
    pattern2 = np.zeros((10, n_samples))
    pattern2[:, :6] = np.random.normal(7, 0.5, (10, 6))
    pattern2[:, 6:] = np.random.normal(4, 0.5, (10, 6))
    
    # 模式3：无显著变化
    pattern3 = np.random.normal(6, 0.8, (10, n_samples))
    
    # 合并数据
    data = np.vstack([pattern1, pattern2, pattern3])
    
    # 创建基因和样本标签
    gene_names = [f'Gene_{i:02d}' for i in range(1, n_genes + 1)]
    sample_names = [f'Ctrl_{i}' for i in range(1, 7)] + \
                   [f'Treat_{i}' for i in range(1, 7)]
    
    # Z-score标准化
    data_zscore = (data - data.mean(axis=1, keepdims=True)) / \
                  data.std(axis=1, keepdims=True)
    
    # 使用seaborn绘制热图
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    
    # 原始数据热图
    sns.heatmap(data, 
                xticklabels=sample_names,
                yticklabels=gene_names,
                cmap='Blues',
                ax=ax1,
                cbar_kws={'label': 'Expression'})
    ax1.set_title('Raw Expression Data', fontweight='bold', pad=20)
    
    # Z-score标准化热图（更常用）
    sns.heatmap(data_zscore, 
                xticklabels=sample_names,
                yticklabels=gene_names,
                cmap='RdBu_r',
                center=0,
                vmin=-2, vmax=2,
                ax=ax2,
                cbar_kws={'label': 'Z-score'})
    ax2.set_title('Z-score Normalized Heatmap', fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 热图制作完成！")
    print("   • 原始数据显示表达强度")
    print("   • Z-score标准化突出表达模式")
    print("   • 红色=高表达，蓝色=低表达")

# 运行热图演示
create_expression_heatmap()
```

### 2.3 箱线图 - 数据分布的全貌

```python
def create_expression_boxplot():
    """
    箱线图：比较不同组间的数据分布
    """
    print("\n📦 箱线图制作")
    print("="*50)
    
    # 生成模拟实验数据
    np.random.seed(42)
    
    # 三个处理组的基因表达数据
    control = np.random.normal(100, 15, 50)
    treatment_a = np.random.normal(130, 20, 50)
    treatment_b = np.random.normal(85, 12, 50)
    
    data = [control, treatment_a, treatment_b]
    labels = ['Control', 'Treatment A', 'Treatment B']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # 基础箱线图
    bp1 = ax1.boxplot(data, labels=labels)
    ax1.set_ylabel('Expression Level', fontweight='bold')
    ax1.set_title('Basic Boxplot', fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # 专业箱线图（带颜色和显著性）
    colors = ['#0173B2', '#DE8F05', '#029E73']
    bp2 = ax2.boxplot(data, labels=labels, patch_artist=True)
    
    # 设置颜色
    for patch, color in zip(bp2['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # 添加显著性标记
    y_max = 160
    ax2.plot([1, 2], [y_max, y_max], 'k-', linewidth=1)
    ax2.text(1.5, y_max + 2, '***', ha='center', fontsize=12)
    
    ax2.set_ylabel('Expression Level', fontweight='bold')
    ax2.set_title('Professional Boxplot with Significance', fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_ylim(40, 180)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 箱线图制作完成！")
    print("   • 箱子显示四分位数")
    print("   • 须线显示数据范围")
    print("   • 点表示离群值")
    print("   • ***表示p<0.001")

# 运行箱线图演示
create_expression_boxplot()
```

---

## 🧬 第三部分：配色与美化

### 3.1 色盲友好配色方案

```python
def demonstrate_color_schemes():
    """
    展示不同的专业配色方案
    """
    print("\n🎨 专业配色方案展示")
    print("="*50)
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # 示例数据
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    # 1. Wong色盲友好配色（推荐）
    ax1 = axes[0, 0]
    wong_colors = ['#E69F00', '#56B4E9', '#009E73', 
                   '#F0E442', '#0072B2']
    bars1 = ax1.bar(categories, values, color=wong_colors[:len(categories)])
    ax1.set_title('Wong Colorblind-Friendly\n(推荐)', fontweight='bold')
    ax1.set_ylabel('Value')
    
    # 2. Nature期刊配色
    ax2 = axes[0, 1]
    nature_colors = ['#3B4CC0', '#6F9BD1', '#F47E7A', 
                     '#EE442F', '#F89217']
    bars2 = ax2.bar(categories, values, color=nature_colors[:len(categories)])
    ax2.set_title('Nature Journal Colors', fontweight='bold')
    ax2.set_ylabel('Value')
    
    # 3. 渐变配色
    ax3 = axes[0, 2]
    gradient = plt.cm.viridis(np.linspace(0.2, 0.9, len(categories)))
    bars3 = ax3.bar(categories, values, color=gradient)
    ax3.set_title('Gradient Colors\n(适合连续数据)', fontweight='bold')
    ax3.set_ylabel('Value')
    
    # 4. 热力图配色对比
    ax4 = axes[1, 0]
    data = np.random.randn(5, 5)
    im1 = ax4.imshow(data, cmap='RdBu_r')
    ax4.set_title('RdBu_r (发散配色)\n适合上调/下调', fontweight='bold')
    
    # 5. 顺序配色
    ax5 = axes[1, 1] 
    im2 = ax5.imshow(np.abs(data), cmap='Blues')
    ax5.set_title('Blues (顺序配色)\n适合浓度/强度', fontweight='bold')
    
    # 6. 配色指南
    ax6 = axes[1, 2]
    ax6.axis('off')
    guidelines = """
    配色选择指南：
    
    1. 分类数据
       → Wong, Nature配色
    
    2. 连续数据
       → Blues, Viridis
    
    3. 发散数据（±）
       → RdBu_r, RdYlBu
    
    4. 避免红绿组合
       → 色盲无法区分
    
    5. 测试工具
       → colorbrewing.com
    """
    ax6.text(0.1, 0.9, guidelines, transform=ax6.transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.3))
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 配色要点：")
    print("   • 始终考虑色盲用户")
    print("   • 保持全文配色一致")
    print("   • 选择合适的配色类型")
    print("   • 测试黑白打印效果")

# 运行配色演示
demonstrate_color_schemes()
```

---

## 🧬 第四部分：多面板组合图

### 4.1 创建发表级别的Figure

```python
def create_publication_figure():
    """
    创建包含多个面板的发表级别Figure
    模拟RNA-seq分析结果展示
    """
    print("\n📊 多面板Figure制作")
    print("="*50)
    
    # 设置发表样式
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['font.size'] = 9
    plt.rcParams['font.weight'] = 'normal'
    
    # 创建图形布局
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # 生成示例数据
    np.random.seed(42)
    
    # Panel A: PCA分析
    ax_a = fig.add_subplot(gs[0, 0])
    ax_a.text(0.05, 0.95, 'A', fontsize=12, fontweight='bold', 
              transform=ax_a.transAxes)
    
    # 模拟PCA数据
    control_pc1 = np.random.normal(-15, 3, 3)
    control_pc2 = np.random.normal(0, 3, 3)
    treat_pc1 = np.random.normal(15, 3, 3)
    treat_pc2 = np.random.normal(0, 3, 3)
    
    ax_a.scatter(control_pc1, control_pc2, s=80, color='#0173B2', 
                 label='Control', alpha=0.8, edgecolors='black')
    ax_a.scatter(treat_pc1, treat_pc2, s=80, color='#DE8F05', 
                 label='Treatment', alpha=0.8, edgecolors='black')
    
    ax_a.set_xlabel('PC1 (45% variance)', fontweight='bold')
    ax_a.set_ylabel('PC2 (23% variance)', fontweight='bold')
    ax_a.set_title('Principal Component Analysis', fontweight='bold')
    ax_a.legend(loc='upper right')
    ax_a.grid(True, alpha=0.3)
    
    # Panel B: 火山图
    ax_b = fig.add_subplot(gs[0, 1:])
    ax_b.text(0.02, 0.98, 'B', fontsize=12, fontweight='bold', 
              transform=ax_b.transAxes)
    
    # 生成火山图数据
    n_genes = 2000
    log2_fc = np.random.normal(0, 0.8, n_genes)
    p_values = np.random.uniform(0.001, 1, n_genes)
    
    # 添加显著基因
    sig_up = np.random.choice(n_genes, 100, replace=False)
    log2_fc[sig_up] = np.random.normal(2, 0.4, 100)
    p_values[sig_up] = np.random.exponential(0.0001, 100)
    
    sig_down = np.random.choice(n_genes, 80, replace=False) 
    log2_fc[sig_down] = np.random.normal(-2, 0.4, 80)
    p_values[sig_down] = np.random.exponential(0.0001, 80)
    
    neg_log10_p = -np.log10(np.clip(p_values, 1e-300, 1))
    
    # 绘制火山图
    colors = ['#D55E00' if (fc > 1 and p < 0.05) 
              else '#0173B2' if (fc < -1 and p < 0.05) 
              else '#E5E5E5' 
              for fc, p in zip(log2_fc, p_values)]
    
    ax_b.scatter(log2_fc, neg_log10_p, c=colors, alpha=0.6, s=8)
    ax_b.axhline(y=-np.log10(0.05), color='black', linestyle='--', alpha=0.5)
    ax_b.axvline(x=1, color='black', linestyle='--', alpha=0.5)
    ax_b.axvline(x=-1, color='black', linestyle='--', alpha=0.5)
    
    ax_b.set_xlabel('Log₂ Fold Change', fontweight='bold')
    ax_b.set_ylabel('-Log₁₀(P-value)', fontweight='bold')
    ax_b.set_title('Differential Expression Analysis', fontweight='bold')
    
    # Panel C: 热图
    ax_c = fig.add_subplot(gs[1, :])
    ax_c.text(0.01, 0.97, 'C', fontsize=12, fontweight='bold', 
              transform=ax_c.transAxes)
    
    # 生成热图数据
    n_genes_hm = 20
    n_samples = 6
    heatmap_data = np.random.randn(n_genes_hm, n_samples)
    
    # 创建表达模式
    heatmap_data[:8, :3] = np.random.normal(-1, 0.3, (8, 3))  # 对照组低表达
    heatmap_data[:8, 3:] = np.random.normal(1, 0.3, (8, 3))   # 处理组高表达
    heatmap_data[8:16, :3] = np.random.normal(1, 0.3, (8, 3)) # 对照组高表达
    heatmap_data[8:16, 3:] = np.random.normal(-1, 0.3, (8, 3)) # 处理组低表达
    
    gene_labels = [f'Gene_{i:02d}' for i in range(1, n_genes_hm + 1)]
    sample_labels = ['Ctrl_1', 'Ctrl_2', 'Ctrl_3', 
                     'Treat_1', 'Treat_2', 'Treat_3']
    
    im = ax_c.imshow(heatmap_data, aspect='auto', cmap='RdBu_r', 
                     vmin=-2, vmax=2)
    
    ax_c.set_xticks(range(n_samples))
    ax_c.set_xticklabels(sample_labels, rotation=45, ha='right')
    ax_c.set_yticks(range(n_genes_hm))
    ax_c.set_yticklabels(gene_labels)
    ax_c.set_xlabel('Samples', fontweight='bold')
    ax_c.set_ylabel('Genes', fontweight='bold')
    ax_c.set_title('Gene Expression Heatmap (Z-score)', fontweight='bold')
    
    # 添加颜色条
    plt.colorbar(im, ax=ax_c, label='Z-score', shrink=0.8)
    
    # 添加总标题
    fig.suptitle('Figure 1. RNA-seq Analysis Results', 
                 fontsize=14, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 多面板Figure完成！")
    print("   Panel A: PCA显示样本分离")
    print("   Panel B: 火山图显示差异基因")
    print("   Panel C: 热图显示表达模式")
    print("   符合期刊发表标准")

# 运行多面板图演示
create_publication_figure()
```

---

## 📊 第五部分：图表保存与输出

### 5.1 不同格式的特点与选择

```python
def save_format_guide():
    """
    图表保存格式选择指南
    """
    print("\n💾 图表保存格式指南")
    print("="*50)
    
    # 创建示例图表
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y, linewidth=2, color='#0173B2')
    ax.set_xlabel('X axis', fontweight='bold')
    ax.set_ylabel('Y axis', fontweight='bold') 
    ax.set_title('Example Figure', fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    print("📋 保存格式对比：")
    print("-"*50)
    
    formats = {
        'PDF': {
            'use': '期刊投稿首选',
            'pros': '矢量图，可无限缩放，文件小',
            'cons': '不支持复杂透明效果',
            'command': "plt.savefig('figure.pdf', bbox_inches='tight')"
        },
        'PNG': {
            'use': 'PPT演示，网页展示',
            'pros': '支持透明背景，兼容性好',
            'cons': '位图，放大会模糊',
            'command': "plt.savefig('figure.png', dpi=300, bbox_inches='tight')"
        },
        'SVG': {
            'use': '网页展示，后期编辑',
            'pros': '矢量图，可在AI中编辑',
            'cons': '某些软件不支持',
            'command': "plt.savefig('figure.svg', bbox_inches='tight')"
        },
        'TIFF': {
            'use': '某些期刊要求',
            'pros': '无损压缩，颜色准确',
            'cons': '文件很大',
            'command': "plt.savefig('figure.tiff', dpi=300, bbox_inches='tight')"
        }
    }
    
    for fmt, info in formats.items():
        print(f"\n{fmt}格式:")
        print(f"  用途: {info['use']}")
        print(f"  优点: {info['pros']}")
        print(f"  缺点: {info['cons']}")
        print(f"  代码: {info['command']}")
    
    print("\n💡 选择建议:")
    print("  • 期刊投稿 → PDF")
    print("  • PPT演示 → PNG (300 DPI)")
    print("  • 网页展示 → SVG")
    print("  • 后期编辑 → SVG + 源代码")
    
    plt.show()

# 运行保存格式指南
save_format_guide()
```

---

## 📚 本章总结

### 核心知识回顾

| 图表类型 | 适用场景 | 关键函数 |
|----------|----------|----------|
| **散点图** | 变量关系、相关性分析 | `plt.scatter()` |
| **线图** | 时间序列、趋势变化 | `plt.plot()` |
| **柱状图** | 分类比较、统计展示 | `plt.bar()` |
| **箱线图** | 分布比较、离群检测 | `plt.boxplot()` |
| **火山图** | 差异分析、显著性展示 | `plt.scatter() + 阈值线` |
| **热图** | 表达模式、聚类结果 | `sns.heatmap()` |

### 最佳实践清单

✅ **配色方案**：使用色盲友好配色  
✅ **标签完整**：标题、坐标轴标签、图例  
✅ **字体规范**：统一字体大小和样式  
✅ **保存设置**：PDF矢量图 + 300 DPI位图  
✅ **风格一致**：全文使用统一的图表样式  

### 进阶学习建议

1. **收集模板**：建立个人图表代码库
2. **学习期刊要求**：了解目标期刊的图表规范  
3. **工具进阶**：探索plotly交互式可视化
4. **设计原则**：学习科学图表设计理论

## 🚀 下一步

恭喜完成数据可视化学习！现在你具备了：
- 制作专业科研图表的能力
- 选择合适配色方案的眼光  
- 创建发表级别组合图的技能
- 优化图表细节的经验

**下一章预告**：我们将学习BioPython库，掌握专业的生物序列分析工具，包括序列处理、BLAST搜索、系统发育分析等核心技能！

---

*"好的数据可视化不仅展示数据，更讲述科学故事。每一个像素都应该有其目的，每一种颜色都应该传达信息。"*

**—— 你的生物信息学导师**