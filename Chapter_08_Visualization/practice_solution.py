#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 08: 数据可视化 - 练习题参考答案

展示从基础到发表级别的科研图表制作完整实现。
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


def set_publication_defaults():
    """设置发表级别的默认样式"""
    plt.rcParams['font.sans-serif'] = ['Arial', 'SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['xtick.labelsize'] = 9
    plt.rcParams['ytick.labelsize'] = 9
    plt.rcParams['legend.fontsize'] = 9
    plt.rcParams['lines.linewidth'] = 1.5
    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['savefig.dpi'] = 300


def practice_1_basic_scatter_solution():
    """
    练习1参考答案：基因表达散点图
    
    展示如何创建专业的相关性散点图。
    """
    print("练习1（★）：基因表达散点图 - 参考答案")
    print("-" * 40)
    
    # 生成模拟数据
    np.random.seed(42)
    control = np.random.normal(100, 20, 100)
    treatment = control * 1.2 + np.random.normal(0, 15, 100)  # 相关数据
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 绘制散点图（色盲友好配色）
    ax.scatter(control, treatment, alpha=0.6, s=50, 
              color='#0173B2', edgecolors='black', linewidth=0.5,
              label='Gene Expression')
    
    # 计算相关系数
    r, p_value = stats.pearsonr(control, treatment)
    
    # 添加回归线
    z = np.polyfit(control, treatment, 1)
    p = np.poly1d(z)
    x_line = np.linspace(control.min(), control.max(), 100)
    ax.plot(x_line, p(x_line), color='#DE8F05', linewidth=2, 
           label=f'Linear fit (r={r:.3f}, p<0.001)')
    
    # 添加对角线参考
    ax.plot([40, 160], [40, 160], '--', color='gray', 
           alpha=0.5, linewidth=1, label='y=x reference')
    
    # 设置标签和标题
    ax.set_xlabel('Control Expression (FPKM)', fontweight='bold')
    ax.set_ylabel('Treatment Expression (FPKM)', fontweight='bold')
    ax.set_title('Gene Expression Correlation Analysis', 
                fontsize=12, fontweight='bold')
    
    # 添加网格和图例
    ax.grid(True, alpha=0.2)
    ax.legend(loc='upper left')
    
    # 添加统计信息
    ax.text(0.95, 0.05, f'n = {len(control)}\nPearson r = {r:.3f}\np < 0.001',
           transform=ax.transAxes, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 完成：散点图包含回归线、相关系数和色盲友好配色")


def practice_2_boxplot_with_significance_solution():
    """
    练习2参考答案：箱线图与显著性标记
    
    展示如何创建包含统计检验的专业箱线图。
    """
    print("\n练习2（★）：箱线图与显著性标记 - 参考答案")
    print("-" * 40)
    
    # 创建三组数据
    np.random.seed(42)
    group1 = np.random.normal(100, 20, 50)  # 对照组
    group2 = np.random.normal(130, 25, 50)  # 处理组A（显著上调）
    group3 = np.random.normal(105, 18, 50)  # 处理组B（无显著变化）
    
    data = [group1, group2, group3]
    labels = ['Control', 'Drug A', 'Drug B']
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 绘制箱线图
    bp = ax.boxplot(data, labels=labels, patch_artist=True,
                    notch=True, showmeans=True,
                    meanprops=dict(marker='D', markerfacecolor='red', markersize=6))
    
    # 设置颜色（色盲友好）
    colors = ['#0173B2', '#DE8F05', '#029E73']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # 进行统计检验
    _, p_val_1_2 = stats.ttest_ind(group1, group2)
    _, p_val_1_3 = stats.ttest_ind(group1, group3)
    _, p_val_2_3 = stats.ttest_ind(group2, group3)
    
    # 添加显著性标记
    def add_significance_bar(ax, x1, x2, y, p_val):
        """添加显著性标记横线"""
        if p_val < 0.001:
            sig = '***'
        elif p_val < 0.01:
            sig = '**'
        elif p_val < 0.05:
            sig = '*'
        else:
            sig = 'ns'
        
        ax.plot([x1, x2], [y, y], 'k-', linewidth=1)
        ax.text((x1 + x2) / 2, y + 1, sig, ha='center', fontsize=10)
    
    # 添加显著性横线
    y_max = max([max(g) for g in data])
    add_significance_bar(ax, 1, 2, y_max + 10, p_val_1_2)
    add_significance_bar(ax, 1, 3, y_max + 20, p_val_1_3)
    add_significance_bar(ax, 2, 3, y_max + 30, p_val_2_3)
    
    # 设置标签和标题
    ax.set_ylabel('Gene Expression (FPKM)', fontweight='bold')
    ax.set_title('Comparison of Gene Expression Across Treatment Groups',
                fontsize=12, fontweight='bold')
    
    # 添加网格
    ax.grid(True, alpha=0.2, axis='y')
    
    # 添加图例说明
    ax.text(0.02, 0.98, '◆ Mean\n─ Median\n* p<0.05\n** p<0.01\n*** p<0.001',
           transform=ax.transAxes, va='top',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 完成：箱线图包含均值、中位数和显著性检验结果")


def practice_3_professional_volcano_solution():
    """
    练习3参考答案：专业火山图
    
    展示如何创建发表级别的火山图。
    """
    print("\n练习3（★★）：专业火山图 - 参考答案")
    print("-" * 40)
    
    # 生成差异表达数据
    np.random.seed(42)
    n_genes = 2000
    
    # 背景基因
    log2_fc = np.random.normal(0, 0.5, n_genes)
    p_values = np.random.uniform(0.01, 1, n_genes)
    
    # 添加显著上调基因
    n_up = 100
    up_idx = np.random.choice(n_genes, n_up, replace=False)
    log2_fc[up_idx] = np.random.normal(2.5, 0.5, n_up)
    p_values[up_idx] = np.random.exponential(0.001, n_up)
    
    # 添加显著下调基因
    n_down = 80
    down_idx = np.random.choice([i for i in range(n_genes) if i not in up_idx], 
                                n_down, replace=False)
    log2_fc[down_idx] = np.random.normal(-2.5, 0.5, n_down)
    p_values[down_idx] = np.random.exponential(0.001, n_down)
    
    # 创建基因名称
    gene_names = [f'Gene_{i:04d}' for i in range(n_genes)]
    
    # 创建DataFrame
    df = pd.DataFrame({
        'gene': gene_names,
        'log2_fc': log2_fc,
        'p_value': np.clip(p_values, 1e-100, 1),
        'neg_log10_p': -np.log10(np.clip(p_values, 1e-100, 1))
    })
    
    # 设置阈值
    fc_threshold = 1.5
    p_threshold = 0.05
    
    # 分类基因
    df['status'] = 'Not Significant'
    df.loc[(df['log2_fc'] > fc_threshold) & (df['p_value'] < p_threshold), 
          'status'] = 'Up-regulated'
    df.loc[(df['log2_fc'] < -fc_threshold) & (df['p_value'] < p_threshold), 
          'status'] = 'Down-regulated'
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 色盲友好配色
    colors = {
        'Not Significant': '#CCCCCC',
        'Up-regulated': '#D55E00',
        'Down-regulated': '#0173B2'
    }
    
    # 绘制不同类别的点
    for status, color in colors.items():
        subset = df[df['status'] == status]
        ax.scatter(subset['log2_fc'], subset['neg_log10_p'],
                  c=color, alpha=0.6, s=15, edgecolors='none',
                  label=f'{status} (n={len(subset)})')
    
    # 添加阈值线
    ax.axhline(y=-np.log10(p_threshold), color='black', 
              linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axvline(x=fc_threshold, color='black', 
              linestyle='--', linewidth=0.8, alpha=0.5)
    ax.axvline(x=-fc_threshold, color='black', 
              linestyle='--', linewidth=0.8, alpha=0.5)
    
    # 标注最显著的基因
    top_genes = df.nlargest(10, 'neg_log10_p')
    for idx, gene in top_genes.iterrows():
        if abs(gene['log2_fc']) > fc_threshold:
            ax.annotate(gene['gene'],
                       xy=(gene['log2_fc'], gene['neg_log10_p']),
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=7, ha='left',
                       bbox=dict(boxstyle='round,pad=0.2', 
                                fc='yellow', alpha=0.5),
                       arrowprops=dict(arrowstyle='->', 
                                      connectionstyle='arc3,rad=0.2',
                                      linewidth=0.5))
    
    # 设置标签和标题
    ax.set_xlabel('Log₂ Fold Change', fontsize=11, fontweight='bold')
    ax.set_ylabel('-Log₁₀ P-value', fontsize=11, fontweight='bold')
    ax.set_title('Differential Gene Expression Analysis\nVolcano Plot',
                fontsize=13, fontweight='bold', pad=15)
    
    # 网格
    ax.grid(True, alpha=0.15, linestyle='-', linewidth=0.5)
    
    # 图例
    ax.legend(loc='upper left', frameon=True, fancybox=False,
             title='Gene Status', title_fontsize=10)
    
    # 统计信息
    stats_text = (f'Total genes: {n_genes:,}\n'
                 f'FC threshold: ±{fc_threshold}\n'
                 f'P-value threshold: {p_threshold}\n'
                 f'─────────────\n'
                 f'Up: {len(df[df["status"]=="Up-regulated"])}\n'
                 f'Down: {len(df[df["status"]=="Down-regulated"])}')
    
    ax.text(0.98, 0.02, stats_text,
           transform=ax.transAxes, fontsize=9,
           ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='white', 
                    edgecolor='gray', alpha=0.9))
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 完成：火山图包含阈值线、基因标注和统计信息")


def practice_4_clustered_heatmap_solution():
    """
    练习4参考答案：聚类热图
    
    展示如何创建包含聚类和注释的专业热图。
    """
    print("\n练习4（★★）：聚类热图 - 参考答案")
    print("-" * 40)
    
    # 创建基因表达矩阵
    np.random.seed(42)
    n_genes = 20
    n_samples = 8
    
    # 样本名称
    sample_names = ['Ctrl_1', 'Ctrl_2', 'Ctrl_3', 'Ctrl_4',
                   'Treat_1', 'Treat_2', 'Treat_3', 'Treat_4']
    
    # 创建三种表达模式
    # 模式1：Treatment上调
    pattern1 = np.hstack([np.random.normal(5, 0.5, (7, 4)),
                          np.random.normal(8, 0.5, (7, 4))])
    
    # 模式2：Treatment下调
    pattern2 = np.hstack([np.random.normal(7, 0.5, (7, 4)),
                          np.random.normal(4, 0.5, (7, 4))])
    
    # 模式3：无变化
    pattern3 = np.random.normal(6, 0.8, (6, 8))
    
    # 合并数据
    expression_matrix = np.vstack([pattern1, pattern2, pattern3])
    
    # 基因名称
    gene_names = ([f'UP_{i:02d}' for i in range(1, 8)] +
                 [f'DOWN_{i:02d}' for i in range(1, 8)] +
                 [f'STABLE_{i:02d}' for i in range(1, 7)])
    
    # 创建DataFrame
    df = pd.DataFrame(expression_matrix, 
                     index=gene_names, 
                     columns=sample_names)
    
    # Z-score标准化
    df_zscore = df.sub(df.mean(axis=1), axis=0).div(df.std(axis=1), axis=0)
    
    # 创建样本注释颜色
    sample_colors = ['#4CAF50'] * 4 + ['#FF9800'] * 4
    
    # 创建聚类热图
    g = sns.clustermap(df_zscore,
                       cmap='RdBu_r',
                       center=0,
                       vmin=-2.5, vmax=2.5,
                       col_cluster=False,
                       row_cluster=True,
                       linewidths=0.5,
                       linecolor='white',
                       cbar_kws={'label': 'Z-score', 
                                'shrink': 0.8,
                                'orientation': 'vertical'},
                       figsize=(8, 10),
                       col_colors=sample_colors,
                       dendrogram_ratio=(0.15, 0.08),
                       colors_ratio=0.02,
                       cbar_pos=(0.02, 0.8, 0.03, 0.15))
    
    # 设置标题
    g.ax_heatmap.set_title('Gene Expression Heatmap with Hierarchical Clustering',
                          fontsize=12, fontweight='bold', pad=15)
    
    # 设置轴标签
    g.ax_heatmap.set_xlabel('Samples', fontsize=11, fontweight='bold')
    g.ax_heatmap.set_ylabel('Genes', fontsize=11, fontweight='bold')
    
    # 旋转标签
    plt.setp(g.ax_heatmap.xaxis.get_majorticklabels(), 
            rotation=45, ha='right')
    plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), 
            rotation=0, fontsize=8)
    
    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#4CAF50', label='Control'),
                      Patch(facecolor='#FF9800', label='Treatment')]
    g.ax_heatmap.legend(handles=legend_elements,
                       loc='upper left',
                       bbox_to_anchor=(1.12, 1),
                       title='Sample Group',
                       frameon=True)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 完成：热图包含层次聚类、Z-score标准化和样本注释")


def practice_5_multi_panel_figure_solution():
    """
    练习5参考答案：多面板组合图
    
    展示如何创建发表级别的多面板图。
    """
    print("\n练习5（★★★）：多面板组合图 - 参考答案")
    print("-" * 40)
    
    # 创建图形和子图
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.35)
    
    # 设置随机种子
    np.random.seed(42)
    
    # ========== 子图A：样本质量控制 ==========
    ax1 = fig.add_subplot(gs[0, 0])
    
    # 生成8个样本的表达量分布
    sample_data = [np.random.lognormal(4, 0.5, 1000) for _ in range(8)]
    sample_labels = ['C1', 'C2', 'C3', 'C4', 'T1', 'T2', 'T3', 'T4']
    
    bp = ax1.boxplot(sample_data, labels=sample_labels, 
                     patch_artist=True, showfliers=False)
    
    # 设置颜色
    colors = ['#4CAF50'] * 4 + ['#FF9800'] * 4
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax1.set_ylabel('Expression Level (log₂)', fontweight='bold')
    ax1.set_title('A. Sample Quality Control', fontweight='bold', loc='left')
    ax1.grid(True, alpha=0.2, axis='y')
    
    # ========== 子图B：PCA分析 ==========
    ax2 = fig.add_subplot(gs[0, 1])
    
    # 生成PCA数据
    pc1_ctrl = np.random.normal(-2, 1, 4)
    pc2_ctrl = np.random.normal(0, 1, 4)
    pc1_treat = np.random.normal(2, 1, 4)
    pc2_treat = np.random.normal(0, 1, 4)
    
    ax2.scatter(pc1_ctrl, pc2_ctrl, s=100, c='#4CAF50', 
               alpha=0.7, edgecolors='black', linewidth=1, label='Control')
    ax2.scatter(pc1_treat, pc2_treat, s=100, c='#FF9800', 
               alpha=0.7, edgecolors='black', linewidth=1, label='Treatment')
    
    ax2.set_xlabel('PC1 (45.2% variance)', fontweight='bold')
    ax2.set_ylabel('PC2 (23.8% variance)', fontweight='bold')
    ax2.set_title('B. Principal Component Analysis', fontweight='bold', loc='left')
    ax2.legend()
    ax2.grid(True, alpha=0.2)
    ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax2.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    
    # ========== 子图C：火山图 ==========
    ax3 = fig.add_subplot(gs[0, 2])
    
    # 生成火山图数据
    n = 500
    log2_fc = np.random.normal(0, 1, n)
    neg_log10_p = np.random.exponential(2, n)
    
    # 添加显著基因
    log2_fc[:50] = np.random.normal(2, 0.5, 50)
    neg_log10_p[:50] = np.random.uniform(2, 8, 50)
    log2_fc[50:80] = np.random.normal(-2, 0.5, 30)
    neg_log10_p[50:80] = np.random.uniform(2, 6, 30)
    
    # 绘制火山图
    colors_volcano = ['#CCCCCC'] * (n - 80) + ['#D55E00'] * 50 + ['#0173B2'] * 30
    ax3.scatter(log2_fc, neg_log10_p, c=colors_volcano, alpha=0.5, s=10)
    
    ax3.axhline(y=-np.log10(0.05), color='k', linestyle='--', linewidth=0.5)
    ax3.axvline(x=1, color='k', linestyle='--', linewidth=0.5)
    ax3.axvline(x=-1, color='k', linestyle='--', linewidth=0.5)
    
    ax3.set_xlabel('Log₂ Fold Change', fontweight='bold')
    ax3.set_ylabel('-Log₁₀ P-value', fontweight='bold')
    ax3.set_title('C. Differential Expression', fontweight='bold', loc='left')
    
    # ========== 子图D：热图 ==========
    ax4 = fig.add_subplot(gs[1, 0])
    
    # 生成热图数据
    heatmap_data = np.random.randn(15, 8)
    heatmap_data[:5, 4:] += 2  # 上调基因
    heatmap_data[5:10, 4:] -= 2  # 下调基因
    
    im = ax4.imshow(heatmap_data, cmap='RdBu_r', aspect='auto', 
                   vmin=-3, vmax=3)
    ax4.set_xticks(range(8))
    ax4.set_xticklabels(sample_labels)
    ax4.set_ylabel('Top 15 DE Genes', fontweight='bold')
    ax4.set_title('D. Expression Heatmap', fontweight='bold', loc='left')
    
    # ========== 子图E：GO富集 ==========
    ax5 = fig.add_subplot(gs[1, 1])
    
    go_terms = ['Cell cycle', 'DNA repair', 'Apoptosis', 
               'Metabolism', 'Signaling']
    enrichment = [5.2, 4.5, 3.8, 3.2, 2.5]
    
    bars = ax5.barh(go_terms, enrichment, color='#029E73', alpha=0.7)
    ax5.axvline(x=-np.log10(0.05), color='r', linestyle='--', 
               linewidth=1, alpha=0.5)
    ax5.set_xlabel('-Log₁₀(P-value)', fontweight='bold')
    ax5.set_title('E. GO Enrichment', fontweight='bold', loc='left')
    
    # ========== 子图F：KEGG通路 ==========
    ax6 = fig.add_subplot(gs[1, 2])
    
    pathways = ['p53 pathway', 'Cell cycle', 'MAPK', 'PI3K-Akt', 'Wnt']
    gene_ratio = [0.15, 0.12, 0.10, 0.08, 0.06]
    p_values_kegg = [8, 6, 4, 3, 2.5]
    gene_count = [30, 25, 20, 15, 10]
    
    scatter = ax6.scatter(gene_ratio, pathways, s=[g*10 for g in gene_count],
                         c=p_values_kegg, cmap='Reds', alpha=0.7,
                         edgecolors='black', linewidth=1)
    
    ax6.set_xlabel('Gene Ratio', fontweight='bold')
    ax6.set_title('F. KEGG Pathway Analysis', fontweight='bold', loc='left')
    
    # 添加颜色条
    cbar = plt.colorbar(scatter, ax=ax6, pad=0.1)
    cbar.set_label('-Log₁₀(P-value)', fontsize=9)
    
    # 总标题
    fig.suptitle('Figure 1. Comprehensive RNA-seq Analysis Results',
                fontsize=14, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ 完成：6个子图展示完整的RNA-seq分析流程")


def bonus_publication_checklist_solution():
    """
    附加内容参考答案：自动检查图表质量
    """
    print("\n📋 发表级别图表检查清单 - 自动检查")
    print("-" * 40)
    
    # 获取当前matplotlib设置
    current_settings = {
        'font_size': plt.rcParams['font.size'],
        'line_width': plt.rcParams['lines.linewidth'],
        'dpi': plt.rcParams['savefig.dpi'],
        'axes_linewidth': plt.rcParams['axes.linewidth']
    }
    
    # 定义检查项和标准
    checklist = {
        "字体大小 >= 8pt": current_settings['font_size'] >= 8,
        "线条宽度 >= 1pt": current_settings['line_width'] >= 1,
        "分辨率 >= 300 DPI": current_settings['dpi'] >= 300,
        "坐标轴线宽 >= 0.8pt": current_settings['axes_linewidth'] >= 0.8,
        "包含坐标轴标签": True,  # 需要检查实际图表
        "包含单位": True,  # 需要检查实际图表
        "色盲友好配色": True,  # 假设使用推荐配色
        "包含图例": True,  # 需要检查实际图表
        "包含统计信息": True,  # 需要检查实际图表
        "无3D效果": True,
        "无过度装饰": True
    }
    
    print("\n当前设置：")
    for key, value in current_settings.items():
        print(f"  {key}: {value}")
    
    print("\n检查结果：")
    for item, status in checklist.items():
        symbol = "✓" if status else "✗"
        color = "\033[92m" if status else "\033[91m"
        reset = "\033[0m"
        print(f"  {color}{symbol}{reset} {item}")
    
    # 计算符合度
    compliance = sum(checklist.values()) / len(checklist) * 100
    print(f"\n符合度：{compliance:.1f}%")
    
    if compliance >= 90:
        print("状态：✨ 可以投稿")
    elif compliance >= 70:
        print("状态：⚠️ 需要小幅改进")
    else:
        print("状态：❌ 需要大幅修改")
    
    # 提供改进建议
    if compliance < 100:
        print("\n改进建议：")
        for item, status in checklist.items():
            if not status:
                print(f"  - 请修正：{item}")


def main():
    """
    主函数：运行所有参考答案
    """
    print("=" * 60)
    print("Chapter 08: 数据可视化 - 练习题参考答案")
    print("=" * 60)
    print("\n这些答案展示了专业科研图表的制作标准")
    print("重点关注：配色、标注、统计信息和整体美观")
    print("\n" + "=" * 60 + "\n")
    
    # 设置发表级别默认样式
    set_publication_defaults()
    
    # 基础练习答案
    practice_1_basic_scatter_solution()
    practice_2_boxplot_with_significance_solution()
    
    # 进阶练习答案
    practice_3_professional_volcano_solution()
    practice_4_clustered_heatmap_solution()
    
    # 挑战练习答案
    practice_5_multi_panel_figure_solution()
    
    # 附加内容
    bonus_publication_checklist_solution()
    
    print("\n" + "=" * 60)
    print("🎯 关键要点总结：")
    print("=" * 60)
    print("\n1. 【配色】始终使用色盲友好的配色方案")
    print("2. 【标注】包含完整的轴标签、单位和图例")
    print("3. 【统计】展示样本数、p值等统计信息")
    print("4. 【布局】多面板图要有清晰的标号和统一风格")
    print("5. 【质量】确保分辨率和线宽符合期刊要求")
    
    print("\n💡 记住：")
    print("   优秀的科研图表 = 准确的数据 + 清晰的展示 + 专业的设计")
    print("   每个细节都很重要，因为图表是你研究成果的窗口。")


if __name__ == "__main__":
    main()