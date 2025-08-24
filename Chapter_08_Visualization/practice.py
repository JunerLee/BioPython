#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 08: 数据可视化 - 练习题

通过实际练习掌握从基础到发表级别的科研图表制作。

难度分级：
★     基础：掌握基本绘图技能
★★    进阶：制作专业的科研图表
★★★   挑战：创建发表级别的组合图表
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats


def practice_1_basic_scatter():
    """
    练习1（★）：绘制基因表达散点图
    
    任务：
    1. 创建两组基因表达数据（对照组 vs 处理组）
    2. 绘制散点图
    3. 添加回归线和相关系数
    4. 使用色盲友好的配色
    
    生物学背景：
    比较两个条件下的基因表达，找出表达模式的相关性。
    """
    print("练习1（★）：基因表达散点图")
    print("-" * 40)
    
    # TODO: 生成模拟数据
    # 提示：使用 np.random.normal() 创建两组相关的数据
    # control = ?
    # treatment = ?
    
    # TODO: 创建散点图
    # 提示：使用 plt.scatter()，注意设置 alpha 透明度
    
    # TODO: 计算相关系数
    # 提示：使用 scipy.stats.pearsonr()
    
    # TODO: 添加回归线
    # 提示：使用 np.polyfit() 和 np.poly1d()
    
    # TODO: 添加图例和标签
    # 提示：xlabel, ylabel, title, legend
    
    pass


def practice_2_boxplot_with_significance():
    """
    练习2（★）：多组数据箱线图与显著性标记
    
    任务：
    1. 创建三组基因表达数据（不同处理条件）
    2. 绘制箱线图，显示中位数、四分位数和异常值
    3. 进行统计检验并标记显著性
    4. 使用专业的配色方案
    
    生物学背景：
    比较不同药物处理对基因表达的影响。
    """
    print("\n练习2（★）：箱线图与显著性标记")
    print("-" * 40)
    
    # TODO: 创建三组数据
    # 提示：模拟不同处理条件的基因表达
    # group1 = np.random.normal(100, 20, 50)  # 对照组
    # group2 = ?  # 处理组A
    # group3 = ?  # 处理组B
    
    # TODO: 绘制箱线图
    # 提示：使用 plt.boxplot() 或 sns.boxplot()
    
    # TODO: 进行t检验
    # 提示：使用 scipy.stats.ttest_ind()
    
    # TODO: 添加显著性标记
    # 提示：在显著差异的组之间画线并标记 * 或 **
    
    pass


def practice_3_professional_volcano():
    """
    练习3（★★）：制作专业的火山图
    
    任务：
    1. 生成差异表达分析数据（log2FC 和 p-value）
    2. 创建火山图，使用色盲友好配色
    3. 添加阈值线（FC = ±1.5, p = 0.05）
    4. 标注最显著的前10个基因
    5. 添加统计信息（上调/下调基因数量）
    
    生物学背景：
    展示RNA-seq差异表达分析结果。
    """
    print("\n练习3（★★）：专业火山图制作")
    print("-" * 40)
    
    # TODO: 生成差异表达数据
    # 提示：创建包含 log2FC 和 p-value 的数据
    # n_genes = 1000
    # log2_fc = np.random.normal(0, 1, n_genes)
    # p_values = ?
    
    # TODO: 分类基因（上调/下调/无变化）
    # 提示：根据阈值判断基因状态
    
    # TODO: 创建火山图
    # 提示：使用不同颜色标记不同类别的基因
    
    # TODO: 添加阈值线
    # 提示：使用 axhline() 和 axvline()
    
    # TODO: 标注重要基因
    # 提示：使用 annotate() 标注最显著的基因
    
    pass


def practice_4_clustered_heatmap():
    """
    练习4（★★）：聚类热图制作
    
    任务：
    1. 创建基因表达矩阵（20个基因 × 8个样本）
    2. 进行Z-score标准化
    3. 创建聚类热图
    4. 添加样本分组注释条
    5. 使用适合的配色（红蓝渐变）
    
    生物学背景：
    展示不同样本间的基因表达模式和聚类关系。
    """
    print("\n练习4（★★）：聚类热图制作")
    print("-" * 40)
    
    # TODO: 创建表达矩阵
    # 提示：创建有明显模式的数据
    # 部分基因在处理组上调，部分下调
    
    # TODO: Z-score标准化
    # 提示：(x - mean) / std，按行标准化
    
    # TODO: 创建聚类热图
    # 提示：使用 sns.clustermap()
    
    # TODO: 添加样本注释
    # 提示：使用 col_colors 参数
    
    pass


def practice_5_multi_panel_figure():
    """
    练习5（★★★）：创建发表级别的多面板图
    
    任务：
    创建一个包含6个子图的Figure，展示完整的基因表达分析：
    A. 样本质量控制（箱线图）
    B. 主成分分析（PCA散点图）
    C. 差异表达火山图
    D. 表达热图
    E. GO富集分析（柱状图）
    F. KEGG通路分析（点图）
    
    要求：
    - 统一的配色方案
    - 清晰的子图标号（A-F）
    - 适当的图例和标签
    - 发表级别的质量
    
    生物学背景：
    完整展示一个RNA-seq数据分析的主要结果。
    """
    print("\n练习5（★★★）：多面板组合图")
    print("-" * 40)
    
    # TODO: 创建 2×3 的子图布局
    # 提示：使用 plt.subplots() 或 gridspec
    
    # TODO: 子图A - 样本质量控制
    # 绘制各样本的表达量分布箱线图
    
    # TODO: 子图B - PCA分析
    # 绘制样本的PCA散点图
    
    # TODO: 子图C - 火山图
    # 展示差异表达分析结果
    
    # TODO: 子图D - 热图
    # 展示top差异基因的表达模式
    
    # TODO: 子图E - GO富集
    # 柱状图展示富集的生物过程
    
    # TODO: 子图F - KEGG通路
    # 点图展示富集的信号通路
    
    pass


def practice_6_interactive_plot():
    """
    练习6（★★★）：创建交互式图表
    
    任务：
    1. 使用plotly创建交互式散点图
    2. 悬停显示基因名称和表达值
    3. 支持缩放和平移
    4. 添加选择工具
    
    生物学背景：
    探索性数据分析，快速查看感兴趣的基因。
    """
    print("\n练习6（★★★）：交互式图表")
    print("-" * 40)
    
    # TODO: 安装plotly（如果未安装）
    # pip install plotly
    
    # TODO: 创建交互式散点图
    # 提示：使用 plotly.express.scatter()
    
    # TODO: 添加悬停信息
    # 提示：设置 hover_data 参数
    
    # TODO: 自定义样式
    # 提示：设置主题、颜色等
    
    pass


def bonus_publication_checklist():
    """
    附加内容：发表级别图表检查清单
    
    创建一个函数，自动检查图表是否符合发表要求。
    """
    print("\n📋 发表级别图表检查清单")
    print("-" * 40)
    
    checklist = {
        "字体大小 >= 8pt": False,
        "线条宽度 >= 1pt": False,
        "分辨率 >= 300 DPI": False,
        "包含坐标轴标签": False,
        "包含单位": False,
        "色盲友好配色": False,
        "包含图例": False,
        "包含统计信息": False,
        "无3D效果": True,
        "无过度装饰": True
    }
    
    # TODO: 实现自动检查功能
    # 提示：检查 matplotlib 的当前设置
    
    print("\n检查结果：")
    for item, status in checklist.items():
        symbol = "✓" if status else "✗"
        print(f"  {symbol} {item}")
    
    # 计算符合度
    compliance = sum(checklist.values()) / len(checklist) * 100
    print(f"\n符合度：{compliance:.1f}%")
    
    if compliance >= 80:
        print("状态：可以投稿 ✨")
    elif compliance >= 60:
        print("状态：需要改进 ⚠️")
    else:
        print("状态：需要大幅修改 ❌")


def main():
    """
    主函数：运行所有练习
    """
    print("=" * 60)
    print("Chapter 08: 数据可视化 - 练习题")
    print("=" * 60)
    print("\n目标：掌握从基础到发表级别的科研图表制作")
    print("\n提示：")
    print("1. 先完成基础练习，掌握基本技能")
    print("2. 进阶练习注重专业性和美观性")
    print("3. 挑战练习模拟真实的科研场景")
    print("\n" + "=" * 60 + "\n")
    
    # 基础练习
    practice_1_basic_scatter()
    practice_2_boxplot_with_significance()
    
    # 进阶练习
    practice_3_professional_volcano()
    practice_4_clustered_heatmap()
    
    # 挑战练习
    practice_5_multi_panel_figure()
    practice_6_interactive_plot()
    
    # 附加内容
    bonus_publication_checklist()
    
    print("\n" + "=" * 60)
    print("💡 练习建议：")
    print("1. 从简单的图表开始，逐步增加复杂度")
    print("2. 注意每个细节，包括字体、颜色、标签")
    print("3. 参考高影响因子期刊的图表风格")
    print("4. 保存不同版本，对比改进效果")
    print("5. 请同行评审你的图表")


if __name__ == "__main__":
    main()