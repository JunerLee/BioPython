#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 08: 数据可视化 - 让实验结果说话

数据可视化就像在实验室展示你的研究成果。
就像你精心准备实验报告一样，每个图表都需要：
- 准确展示数据（不能有误导）
- 清晰传达信息（让人一目了然）
- 专业美观（符合科研规范）

本章将带你从草图到发表级别，逐步掌握专业的科研图表制作。
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


def set_publication_style():
    """
    设置发表级别的图表样式
    
    就像实验室有标准操作流程（SOP）一样，
    科研图表也有专业的样式规范。
    """
    # 设置整体样式
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # 设置字体（确保中文显示）
    plt.rcParams['font.sans-serif'] = ['Arial', 'SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 设置字体大小（符合期刊要求）
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['xtick.labelsize'] = 9
    plt.rcParams['ytick.labelsize'] = 9
    plt.rcParams['legend.fontsize'] = 9
    
    # 设置线条宽度
    plt.rcParams['lines.linewidth'] = 1.5
    plt.rcParams['axes.linewidth'] = 1.0
    
    # 设置图形质量
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['savefig.dpi'] = 300
    
    print("✅ 发表级别样式已设置")


def demonstrate_chart_levels():
    """
    演示三个层次的图表制作：草图 → 汇报 → 发表
    
    就像实验数据的处理过程：
    1. 草图 = 实验记录本上的快速草图
    2. 汇报 = 组会PPT上的清晰图表
    3. 发表 = 期刊论文中的专业图表
    """
    print("\n📊 图表制作的三个层次")
    print("=" * 50)
    
    # 生成示例数据：两组基因表达数据
    np.random.seed(42)
    control = np.random.normal(100, 20, 50)
    treatment = control * 1.5 + np.random.normal(0, 15, 50)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 1. 草图级别：快速探索
    axes[0].scatter(control, treatment, alpha=0.5)
    axes[0].set_title('Level 1: 草图级别\n(快速探索数据)')
    axes[0].set_xlabel('Control')
    axes[0].set_ylabel('Treatment')
    
    # 2. 汇报级别：清晰展示
    axes[1].scatter(control, treatment, alpha=0.6, s=30, color='blue')
    axes[1].plot([50, 180], [50, 180], 'r--', alpha=0.5, label='y=x')
    axes[1].set_title('Level 2: 汇报级别\n(组会/会议展示)')
    axes[1].set_xlabel('Control Expression (FPKM)')
    axes[1].set_ylabel('Treatment Expression (FPKM)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # 3. 发表级别：专业规范
    # 计算相关系数
    r, p = stats.pearsonr(control, treatment)
    
    # 使用色盲友好的配色
    axes[2].scatter(control, treatment, alpha=0.7, s=40, 
                   color='#0173B2', edgecolors='black', linewidth=0.5)
    
    # 添加回归线和置信区间
    z = np.polyfit(control, treatment, 1)
    p_poly = np.poly1d(z)
    axes[2].plot(control, p_poly(control), 
                color='#DE8F05', linewidth=2, label=f'Linear fit (r={r:.3f}, p<0.001)')
    
    # 添加对角线参考
    axes[2].plot([50, 180], [50, 180], '--', 
                color='gray', alpha=0.5, linewidth=1, label='y=x reference')
    
    axes[2].set_title('Level 3: 发表级别\n(期刊论文标准)')
    axes[2].set_xlabel('Control Expression (FPKM)', fontweight='bold')
    axes[2].set_ylabel('Treatment Expression (FPKM)', fontweight='bold')
    axes[2].legend(loc='upper left', frameon=True, fancybox=False)
    axes[2].grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
    
    # 添加统计信息文本
    axes[2].text(0.95, 0.05, f'n = {len(control)}', 
                transform=axes[2].transAxes, ha='right', va='bottom')
    
    plt.suptitle('从草图到发表：图表制作的进化过程', fontsize=14, y=1.02)
    plt.tight_layout()
    plt.show()
    
    print("✅ 展示了三个层次的图表制作")
    print("   重点：每个层次都有其适用场景")


def create_professional_volcano_plot():
    """
    创建发表级别的火山图
    
    火山图就像实验室的显微镜照片：
    - 横轴（Fold Change）= 基因表达的变化倍数
    - 纵轴（-log10 P-value）= 统计显著性
    - 每个点 = 一个基因
    - 颜色 = 基因的调控状态（上调/下调/无变化）
    """
    print("\n🌋 发表级别火山图制作")
    print("=" * 50)
    
    # 生成模拟的差异表达数据
    np.random.seed(42)
    n_genes = 5000
    
    # 大部分基因无显著变化
    log2_fc = np.random.normal(0, 0.5, n_genes)
    p_values = np.random.uniform(0.001, 1, n_genes)
    
    # 添加显著上调基因
    n_up = 200
    up_indices = np.random.choice(n_genes, n_up, replace=False)
    log2_fc[up_indices] = np.random.normal(2, 0.5, n_up)
    p_values[up_indices] = np.random.exponential(0.0001, n_up)
    
    # 添加显著下调基因
    n_down = 150
    down_indices = np.random.choice(n_genes, n_down, replace=False)
    log2_fc[down_indices] = np.random.normal(-2, 0.5, n_down)
    p_values[down_indices] = np.random.exponential(0.0001, n_down)
    
    # 创建基因名称
    gene_names = [f'Gene_{i:04d}' for i in range(n_genes)]
    
    # 创建DataFrame
    volcano_df = pd.DataFrame({
        'gene': gene_names,
        'log2_fc': log2_fc,
        'p_value': np.clip(p_values, 1e-300, 1),
        'neg_log10_p': -np.log10(np.clip(p_values, 1e-300, 1))
    })
    
    # 设置阈值
    fc_threshold = 1.0  # 2倍变化
    p_threshold = 0.05
    
    # 分类基因
    volcano_df['status'] = 'Not Significant'
    volcano_df.loc[(volcano_df['log2_fc'] > fc_threshold) & 
                  (volcano_df['p_value'] < p_threshold), 'status'] = 'Up-regulated'
    volcano_df.loc[(volcano_df['log2_fc'] < -fc_threshold) & 
                  (volcano_df['p_value'] < p_threshold), 'status'] = 'Down-regulated'
    
    # 创建发表级别的火山图
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 使用色盲友好的配色
    colors = {
        'Not Significant': '#E5E5E5',  # 浅灰色
        'Up-regulated': '#D55E00',     # 红橙色
        'Down-regulated': '#0173B2'    # 蓝色
    }
    
    # 绘制不同类别的点
    for status, color in colors.items():
        subset = volcano_df[volcano_df['status'] == status]
        ax.scatter(subset['log2_fc'], subset['neg_log10_p'],
                  c=color, alpha=0.6, s=20, 
                  edgecolors='none', label=f'{status} (n={len(subset)})')
    
    # 添加阈值线
    ax.axhline(y=-np.log10(p_threshold), color='black', 
              linestyle='--', linewidth=1, alpha=0.5)
    ax.axvline(x=fc_threshold, color='black', 
              linestyle='--', linewidth=1, alpha=0.5)
    ax.axvline(x=-fc_threshold, color='black', 
              linestyle='--', linewidth=1, alpha=0.5)
    
    # 标注最显著的基因
    top_genes = volcano_df.nlargest(5, 'neg_log10_p')
    for _, gene in top_genes.iterrows():
        ax.annotate(gene['gene'], 
                   xy=(gene['log2_fc'], gene['neg_log10_p']),
                   xytext=(5, 5), textcoords='offset points',
                   fontsize=8, ha='left',
                   bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.3),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    # 设置标签和标题
    ax.set_xlabel('Log₂ Fold Change', fontsize=12, fontweight='bold')
    ax.set_ylabel('-Log₁₀ P-value', fontsize=12, fontweight='bold')
    ax.set_title('Differential Gene Expression Analysis\nVolcano Plot', 
                fontsize=14, fontweight='bold', pad=20)
    
    # 添加网格
    ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
    
    # 设置图例
    ax.legend(loc='upper left', frameon=True, fancybox=False, 
             title='Gene Status', title_fontsize=10)
    
    # 添加统计信息
    ax.text(0.02, 0.98, f'Total genes: {n_genes:,}\nFC threshold: ±{fc_threshold}\nP-value threshold: {p_threshold}',
           transform=ax.transAxes, fontsize=9, verticalalignment='top',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    print(f"✅ 火山图绘制完成")
    print(f"   上调基因: {len(volcano_df[volcano_df['status'] == 'Up-regulated'])} 个")
    print(f"   下调基因: {len(volcano_df[volcano_df['status'] == 'Down-regulated'])} 个")
    print(f"   无显著变化: {len(volcano_df[volcano_df['status'] == 'Not Significant'])} 个")


def create_publication_heatmap():
    """
    创建发表级别的聚类热图
    
    热图就像实验室的凝胶电泳图：
    - 每一行 = 一个基因
    - 每一列 = 一个样本
    - 颜色深浅 = 表达量高低
    - 聚类树 = 相似性分组
    """
    print("\n🔥 发表级别热图制作")
    print("=" * 50)
    
    # 生成模拟数据
    np.random.seed(42)
    
    # 创建三组不同表达模式的基因
    n_genes_per_group = 15
    n_samples = 8
    sample_names = ['Ctrl_1', 'Ctrl_2', 'Ctrl_3', 'Ctrl_4',
                   'Treat_1', 'Treat_2', 'Treat_3', 'Treat_4']
    
    # 组1：在Treatment中上调
    group1 = np.random.normal(5, 0.5, (n_genes_per_group, 4))
    group1_treat = np.random.normal(8, 0.5, (n_genes_per_group, 4))
    group1 = np.hstack([group1, group1_treat])
    
    # 组2：在Treatment中下调
    group2 = np.random.normal(7, 0.5, (n_genes_per_group, 4))
    group2_treat = np.random.normal(4, 0.5, (n_genes_per_group, 4))
    group2 = np.hstack([group2, group2_treat])
    
    # 组3：无变化
    group3 = np.random.normal(6, 0.8, (n_genes_per_group, n_samples))
    
    # 合并数据
    expression_matrix = np.vstack([group1, group2, group3])
    
    # 创建基因名称
    gene_names = []
    gene_names.extend([f'UP_{i:02d}' for i in range(1, n_genes_per_group + 1)])
    gene_names.extend([f'DOWN_{i:02d}' for i in range(1, n_genes_per_group + 1)])
    gene_names.extend([f'STABLE_{i:02d}' for i in range(1, n_genes_per_group + 1)])
    
    # 创建DataFrame
    expr_df = pd.DataFrame(expression_matrix, 
                          index=gene_names, 
                          columns=sample_names)
    
    # Z-score标准化（按行）
    expr_zscore = expr_df.sub(expr_df.mean(axis=1), axis=0).div(expr_df.std(axis=1), axis=0)
    
    # 创建图形
    fig = plt.figure(figsize=(10, 12))
    
    # 创建样本注释
    sample_colors = ['#4CAF50'] * 4 + ['#FF9800'] * 4  # 绿色=Control, 橙色=Treatment
    
    # 使用seaborn的clustermap创建聚类热图
    g = sns.clustermap(expr_zscore,
                       cmap='RdBu_r',
                       center=0,
                       vmin=-2, vmax=2,
                       col_cluster=False,  # 不对列聚类（保持样本顺序）
                       row_cluster=True,   # 对行聚类
                       linewidths=0.3,
                       linecolor='white',
                       cbar_kws={'label': 'Z-score', 'shrink': 0.8},
                       figsize=(10, 12),
                       col_colors=sample_colors,
                       dendrogram_ratio=(0.15, 0.05),
                       colors_ratio=0.02,
                       cbar_pos=(0.02, 0.83, 0.03, 0.15))
    
    # 设置标题
    g.ax_heatmap.set_title('Gene Expression Heatmap\nHierarchical Clustering Analysis', 
                          fontsize=14, fontweight='bold', pad=20)
    
    # 设置轴标签
    g.ax_heatmap.set_xlabel('Samples', fontsize=12, fontweight='bold')
    g.ax_heatmap.set_ylabel('Genes', fontsize=12, fontweight='bold')
    
    # 旋转样本标签
    plt.setp(g.ax_heatmap.xaxis.get_majorticklabels(), rotation=45, ha='right')
    plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
    
    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#4CAF50', label='Control'),
                      Patch(facecolor='#FF9800', label='Treatment')]
    g.ax_heatmap.legend(handles=legend_elements, 
                       loc='upper left', 
                       bbox_to_anchor=(1.15, 1),
                       title='Sample Group')
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 聚类热图绘制完成")
    print(f"   数据维度: {expr_df.shape[0]} 基因 × {expr_df.shape[1]} 样本")
    print("   已进行层次聚类和Z-score标准化")


def create_multi_panel_figure():
    """
    创建多面板组合图（期刊论文常见格式）
    
    就像实验报告中的Figure 1，包含多个相关的子图，
    共同讲述一个完整的科学故事。
    """
    print("\n📈 多面板组合图制作")
    print("=" * 50)
    
    # 创建4个子图的组合图
    fig = plt.figure(figsize=(14, 10))
    
    # 定义子图布局
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # 子图A：箱线图 - 比较基因表达分布
    ax1 = fig.add_subplot(gs[0, 0])
    np.random.seed(42)
    data_box = [np.random.normal(100, 20, 100),
                np.random.normal(120, 25, 100),
                np.random.normal(90, 15, 100)]
    
    bp = ax1.boxplot(data_box, labels=['Control', 'Treatment A', 'Treatment B'],
                     patch_artist=True, notch=True, showmeans=True)
    
    # 设置箱线图颜色（色盲友好）
    colors = ['#0173B2', '#DE8F05', '#029E73']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax1.set_ylabel('Expression Level (FPKM)', fontweight='bold')
    ax1.set_title('A. Gene Expression Distribution', fontweight='bold', loc='left')
    ax1.grid(True, alpha=0.2)
    
    # 添加显著性标记
    ax1.plot([1, 2], [180, 180], 'k-', linewidth=1)
    ax1.text(1.5, 182, '***', ha='center', fontsize=12)
    
    # 子图B：散点图 - 相关性分析
    ax2 = fig.add_subplot(gs[0, 1])
    x = np.random.normal(100, 20, 100)
    y = x * 0.8 + np.random.normal(0, 15, 100)
    
    ax2.scatter(x, y, alpha=0.6, s=30, color='#0173B2', edgecolors='black', linewidth=0.5)
    
    # 添加回归线
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    ax2.plot(np.sort(x), p(np.sort(x)), 'r-', linewidth=2, alpha=0.8)
    
    # 计算并显示相关系数
    r, p_val = stats.pearsonr(x, y)
    ax2.text(0.05, 0.95, f'r = {r:.3f}\np < 0.001', 
            transform=ax2.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax2.set_xlabel('Gene A Expression', fontweight='bold')
    ax2.set_ylabel('Gene B Expression', fontweight='bold')
    ax2.set_title('B. Expression Correlation', fontweight='bold', loc='left')
    ax2.grid(True, alpha=0.2)
    
    # 子图C：柱状图 - GO富集分析
    ax3 = fig.add_subplot(gs[1, 0])
    go_terms = ['Cell cycle', 'DNA repair', 'Apoptosis', 'Metabolism', 'Signal']
    enrichment = [4.5, 3.8, 3.2, 2.5, 2.0]
    
    bars = ax3.barh(go_terms, enrichment, color='#029E73', alpha=0.7)
    
    # 添加数值标签
    for i, (bar, val) in enumerate(zip(bars, enrichment)):
        ax3.text(val + 0.1, bar.get_y() + bar.get_height()/2, 
                f'{val:.1f}', va='center')
    
    ax3.set_xlabel('-Log₁₀(P-value)', fontweight='bold')
    ax3.set_title('C. GO Enrichment Analysis', fontweight='bold', loc='left')
    ax3.axvline(x=1.3, color='red', linestyle='--', alpha=0.5, label='P = 0.05')
    ax3.legend()
    ax3.grid(True, alpha=0.2, axis='x')
    
    # 子图D：折线图 - 时间序列
    ax4 = fig.add_subplot(gs[1, 1])
    time_points = [0, 2, 4, 6, 8, 12, 24]
    gene1 = [100, 120, 150, 180, 160, 140, 130]
    gene2 = [100, 95, 90, 85, 88, 92, 95]
    gene3 = [100, 105, 110, 108, 106, 104, 102]
    
    ax4.plot(time_points, gene1, 'o-', color='#D55E00', linewidth=2, 
            markersize=6, label='Up-regulated')
    ax4.plot(time_points, gene2, 's-', color='#0173B2', linewidth=2, 
            markersize=6, label='Down-regulated')
    ax4.plot(time_points, gene3, '^-', color='#999999', linewidth=2, 
            markersize=6, label='No change')
    
    ax4.set_xlabel('Time (hours)', fontweight='bold')
    ax4.set_ylabel('Relative Expression (%)', fontweight='bold')
    ax4.set_title('D. Time Course Expression', fontweight='bold', loc='left')
    ax4.legend(loc='best')
    ax4.grid(True, alpha=0.2)
    
    # 添加总标题
    fig.suptitle('Figure 1. Comprehensive Gene Expression Analysis', 
                fontsize=16, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 多面板组合图绘制完成")
    print("   包含4个子图：分布、相关性、富集分析、时间序列")


def demonstrate_color_schemes():
    """
    演示色盲友好的配色方案
    
    约8%的男性有不同程度的色觉异常，
    选择合适的配色就像选择合适的对照组一样重要。
    """
    print("\n🎨 色盲友好配色方案")
    print("=" * 50)
    
    # 定义不同的配色方案
    color_schemes = {
        '默认配色（不推荐）': ['red', 'green', 'blue', 'yellow', 'purple'],
        'Paul Tol配色': ['#0173B2', '#DE8F05', '#029E73', '#CC78BC', '#ECE133'],
        'Okabe-Ito配色': ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2'],
        '灰度安全': ['#000000', '#404040', '#808080', '#BFBFBF', '#FFFFFF']
    }
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()
    
    # 生成示例数据
    np.random.seed(42)
    categories = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
    values = np.random.randint(50, 150, 5)
    
    for idx, (name, colors) in enumerate(color_schemes.items()):
        ax = axes[idx]
        bars = ax.bar(categories, values, color=colors)
        ax.set_title(name, fontweight='bold')
        ax.set_ylabel('Value')
        ax.set_ylim(0, 160)
        
        # 添加数值标签
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                   str(val), ha='center', va='bottom')
    
    plt.suptitle('色盲友好配色方案对比', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    print("✅ 展示了4种配色方案")
    print("   推荐使用Paul Tol或Okabe-Ito配色")
    print("   避免红绿组合，这是最常见的色盲类型")


def save_publication_figure():
    """
    演示如何保存发表级别的图片
    
    就像保存实验数据一样，图片也需要：
    - 高分辨率（至少300 DPI）
    - 合适的格式（矢量图优先）
    - 规范的命名
    """
    print("\n💾 保存发表级别图片")
    print("=" * 50)
    
    # 创建一个简单的示例图
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y, linewidth=2, color='#0173B2')
    ax.set_xlabel('Time (s)', fontweight='bold')
    ax.set_ylabel('Signal Intensity', fontweight='bold')
    ax.set_title('Example Publication Figure', fontweight='bold')
    ax.grid(True, alpha=0.2)
    
    # 保存为不同格式
    formats = {
        'figure_1_vector.pdf': '矢量图，适合期刊印刷',
        'figure_1_vector.svg': '矢量图，可编辑',
        'figure_1_bitmap.png': '位图，适合网页展示',
        'figure_1_print.tiff': '位图，适合印刷'
    }
    
    print("\n保存格式说明：")
    for filename, description in formats.items():
        print(f"  - {filename}: {description}")
        # 注意：实际运行时会保存文件
        # plt.savefig(filename, dpi=300, bbox_inches='tight')
    
    plt.show()
    
    print("\n✅ 图片保存要点：")
    print("   1. DPI >= 300（印刷要求）")
    print("   2. bbox_inches='tight'（去除多余空白）")
    print("   3. 矢量图优先（PDF/SVG）")
    print("   4. 文件命名规范（figure_编号_描述）")


def main():
    """
    主函数：数据可视化完整教程
    
    记住：好的图表就像好的实验设计，
    每个元素都有其目的，没有多余的装饰。
    """
    print("=" * 60)
    print("Chapter 08: 数据可视化 - 让实验结果说话")
    print("=" * 60)
    print("\n就像精心设计的实验，专业的图表需要：")
    print("1. 明确的目的（要展示什么？）")
    print("2. 合适的方法（用什么图表？）")
    print("3. 规范的操作（遵循标准）")
    print("4. 清晰的结果（易于理解）")
    
    # 设置发表级别样式
    set_publication_style()
    
    # 演示不同内容
    demonstrate_chart_levels()
    create_professional_volcano_plot()
    create_publication_heatmap()
    create_multi_panel_figure()
    demonstrate_color_schemes()
    save_publication_figure()
    
    print("\n" + "=" * 60)
    print("🎯 本章关键要点：")
    print("=" * 60)
    print("\n1. 【图表层次】从草图到发表，逐步完善")
    print("2. 【选择原则】根据数据类型选择合适的图表")
    print("3. 【专业规范】字体、线宽、分辨率都有标准")
    print("4. 【色彩设计】使用色盲友好的配色方案")
    print("5. 【完整故事】组合图表讲述完整的科学发现")
    
    print("\n💡 记住：")
    print("   图表是科学交流的语言，")
    print("   好的图表让复杂的数据变得简单明了，")
    print("   就像好的实验设计让复杂的生物学问题变得可以回答。")


if __name__ == "__main__":
    main()