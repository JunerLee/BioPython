#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 06: Pandas入门 - 练习参考答案

提供完整的解决方案和最佳实践，包括：
- 详细的代码实现
- 生物学背景解释
- 结果分析和解释
- 进一步学习建议

学习建议：先独立完成练习，再查看参考答案
"""

import pandas as pd
import numpy as np


def solution_1_series_basics():
    """
    练习1参考答案: Series基础操作
    
    学习要点：Series创建、索引、基本统计、数据筛选
    """
    print("=" * 60)
    print("练习1参考答案: 酶活性数据分析 ⭐")
    print("-" * 60)
    
    # 创建Series存储酶活性数据
    enzyme_activity = pd.Series({
        'Amylase': 125.3,      # 淀粉酶
        'Protease': 89.7,      # 蛋白酶
        'Lipase': 45.2,        # 脂肪酶
        'Cellulase': 67.8,     # 纤维素酶
        'Invertase': 156.9     # 转化酶
    })
    
    print("任务1: 酶活性数据")
    print("酶活性测定结果 (U/mg蛋白):")
    print(enzyme_activity)
    
    print(f"\n📊 数据特征:")
    print(f"  数据类型: {type(enzyme_activity).__name__}")
    print(f"  数据长度: {len(enzyme_activity)} 种酶")
    print(f"  索引类型: {type(enzyme_activity.index).__name__}")
    
    print("\n任务2: 基本统计量")
    print("统计分析结果:")
    print(f"  平均酶活性: {enzyme_activity.mean():.2f} U/mg")
    print(f"  最高活性: {enzyme_activity.max():.2f} U/mg ({enzyme_activity.idxmax()})")
    print(f"  最低活性: {enzyme_activity.min():.2f} U/mg ({enzyme_activity.idxmin()})")
    print(f"  标准差: {enzyme_activity.std():.2f}")
    print(f"  变异系数: {(enzyme_activity.std()/enzyme_activity.mean()*100):.1f}%")
    
    print("\n任务3: 数据筛选")
    high_activity = enzyme_activity[enzyme_activity > 100]
    print(f"高活性酶 (>100 U/mg): {len(high_activity)} 种")
    print(high_activity.round(2))
    
    # 更多筛选示例
    low_activity = enzyme_activity[enzyme_activity < 70]
    print(f"\n低活性酶 (<70 U/mg): {len(low_activity)} 种")
    print(low_activity.round(2))
    
    print("\n任务4: 数据排序")
    sorted_enzymes = enzyme_activity.sort_values(ascending=False)
    print("按活性从高到低排序:")
    print(sorted_enzymes.round(2))
    
    # 排序索引
    sorted_by_name = enzyme_activity.sort_index()
    print("\n按名称字母顺序排序:")
    print(sorted_by_name.round(2))
    
    print("\n🧬 生物学解释:")
    print("• Invertase活性最高，适合用于工业糖类转化")
    print("• Amylase活性较高，是重要的消化酶")
    print("• Lipase活性最低，可能需要优化反应条件")
    print("• 变异系数>30%，说明不同酶活性差异较大")


def solution_2_dataframe_creation():
    """
    练习2参考答案: DataFrame创建和基本操作
    
    学习要点：DataFrame创建、索引操作、数据选择
    """
    print("\n" + "=" * 60)
    print("练习2参考答案: PCR实验结果整理 ⭐⭐")
    print("-" * 60)
    
    # 方法1：从字典创建DataFrame
    pcr_data = {
        'Sample1': [18.5, 19.8, 20.2],
        'Sample2': [19.2, 20.1, 19.9],
        'Sample3': [18.8, 19.5, 20.5], 
        'Sample4': [19.0, 20.3, 20.0]
    }
    df_pcr = pd.DataFrame(pcr_data, index=['GAPDH', 'ACTB', 'RPL13A'])
    
    print("任务1: PCR结果表")
    print("qPCR Ct值结果:")
    print(df_pcr)
    
    print("\n任务2: DataFrame基本信息")
    print(f"数据形状: {df_pcr.shape} (基因数 × 样本数)")
    print(f"行索引(基因): {list(df_pcr.index)}")
    print(f"列索引(样本): {list(df_pcr.columns)}")
    print(f"总数据点: {df_pcr.size} 个Ct值")
    print("\n数据类型:")
    print(df_pcr.dtypes)
    
    print("\n任务3: 数据选择操作")
    print("3.1 行选择 - GAPDH基因在所有样本中的Ct值:")
    gapdh_values = df_pcr.loc['GAPDH']
    print(gapdh_values)
    print(f"     GAPDH平均Ct: {gapdh_values.mean():.2f}")
    
    print("\n3.2 列选择 - Sample1的所有基因Ct值:")
    sample1_values = df_pcr['Sample1']
    print(sample1_values)
    print(f"     Sample1平均Ct: {sample1_values.mean():.2f}")
    
    print("\n3.3 精确位置选择:")
    print(f"Sample1中GAPDH的Ct值: {df_pcr.loc['GAPDH', 'Sample1']}")
    print(f"Sample4中RPL13A的Ct值: {df_pcr.loc['RPL13A', 'Sample4']}")
    
    print("\n任务4: 基本统计分析")
    print("4.1 每个基因的平均Ct值 (跨样本):")
    gene_means = df_pcr.mean(axis=1).round(2)
    print(gene_means)
    
    print("\n4.2 每个样本的平均Ct值 (跨基因):")
    sample_means = df_pcr.mean(axis=0).round(2)
    print(sample_means)
    
    print("\n4.3 整体统计摘要:")
    print(df_pcr.describe().round(2))
    
    print("\n🧬 qPCR结果解读:")
    most_stable_gene = gene_means.idxmin()
    most_variable_sample = sample_means.idxmax()
    print(f"• 最稳定管家基因: {most_stable_gene} (平均Ct = {gene_means[most_stable_gene]})")
    print(f"• 表达量差异最大样本: {most_variable_sample} (平均Ct = {sample_means[most_variable_sample]})")
    print("• Ct值越小表示表达量越高")
    print("• 管家基因应该在不同样本间表达稳定")


def solution_3_gene_expression_analysis():
    """
    练习3参考答案: 基因表达数据分析
    
    学习要点：复杂数据处理、fold change计算、差异分析
    """
    print("\n" + "=" * 60)
    print("练习3参考答案: 差异表达基因识别 ⭐⭐⭐")
    print("-" * 60)
    
    # 创建基因表达数据
    genes = ['BRCA1', 'TP53', 'MYC', 'EGFR', 'VEGFA', 'CDKN1A', 'BCL2', 'PTEN']
    control_expression = [120, 89, 156, 78, 45, 234, 167, 98]
    treated_expression = [78, 234, 145, 189, 123, 456, 89, 78]
    
    expression_df = pd.DataFrame({
        'Control': control_expression,
        'Treated': treated_expression
    }, index=genes)
    
    print("任务1: 基因表达数据")
    print("基因表达水平 (FPKM):")
    print(expression_df)
    
    print("\n任务2: Fold Change计算")
    expression_df['Fold_Change'] = expression_df['Treated'] / expression_df['Control']
    expression_df['Log2_FC'] = np.log2(expression_df['Fold_Change'])
    
    # 添加变化方向标记
    expression_df['Change_Direction'] = expression_df['Log2_FC'].apply(
        lambda x: 'Up' if x > 1 else 'Down' if x < -1 else 'Stable'
    )
    
    print("完整分析结果:")
    display_df = expression_df.copy()
    display_df = display_df.round({'Fold_Change': 3, 'Log2_FC': 3})
    print(display_df)
    
    print("\n任务3: 差异表达基因识别")
    # 设置阈值：|Log2FC| > 1 认为是显著差异
    threshold = 1.0
    
    upregulated = expression_df[expression_df['Log2_FC'] > threshold]
    downregulated = expression_df[expression_df['Log2_FC'] < -threshold]
    stable = expression_df[abs(expression_df['Log2_FC']) <= threshold]
    
    print(f"显著上调基因 (Log2FC > {threshold}): {len(upregulated)} 个")
    if len(upregulated) > 0:
        print("基因名\t\t表达倍数\tLog2FC")
        for gene in upregulated.index:
            fc = upregulated.loc[gene, 'Fold_Change']
            log2fc = upregulated.loc[gene, 'Log2_FC']
            print(f"{gene}\t\t{fc:.2f}x\t\t{log2fc:.2f}")
    
    print(f"\n显著下调基因 (Log2FC < -{threshold}): {len(downregulated)} 个")
    if len(downregulated) > 0:
        print("基因名\t\t表达倍数\tLog2FC")
        for gene in downregulated.index:
            fc = downregulated.loc[gene, 'Fold_Change']
            log2fc = downregulated.loc[gene, 'Log2_FC']
            print(f"{gene}\t\t{fc:.2f}x\t\t{log2fc:.2f}")
    
    print(f"\n稳定表达基因: {len(stable)} 个")
    print(list(stable.index))
    
    print("\n任务4: 详细分析报告")
    
    # 最显著变化的基因
    max_up_gene = expression_df.loc[expression_df['Log2_FC'].idxmax()]
    max_down_gene = expression_df.loc[expression_df['Log2_FC'].idxmin()]
    
    print("🔍 关键发现:")
    print(f"• 最显著上调基因: {expression_df['Log2_FC'].idxmax()}")
    print(f"  表达倍数: {max_up_gene['Fold_Change']:.2f}x")
    print(f"  Log2FC: {max_up_gene['Log2_FC']:.2f}")
    
    print(f"• 最显著下调基因: {expression_df['Log2_FC'].idxmin()}")
    print(f"  表达倍数: {max_down_gene['Fold_Change']:.2f}x") 
    print(f"  Log2FC: {max_down_gene['Log2_FC']:.2f}")
    
    # 统计汇总
    total_genes = len(expression_df)
    print(f"\n📊 统计汇总:")
    print(f"• 总基因数: {total_genes}")
    print(f"• 上调基因: {len(upregulated)} ({len(upregulated)/total_genes*100:.1f}%)")
    print(f"• 下调基因: {len(downregulated)} ({len(downregulated)/total_genes*100:.1f}%)")
    print(f"• 稳定表达: {len(stable)} ({len(stable)/total_genes*100:.1f}%)")
    
    print("\n🧬 生物学解释:")
    print("• TP53和CDKN1A上调：细胞周期检查点激活，可能触发凋亡通路")
    print("• BRCA1下调：DNA修复能力下降，细胞更易发生突变")
    print("• VEGFA上调：可能促进血管生成，与肿瘤进展相关")
    print("• MYC稳定：细胞增殖相关基因未受显著影响")


def solution_4_data_filtering():
    """
    练习4参考答案: 数据筛选和条件查询
    
    学习要点：复杂筛选条件、分组操作、多重条件组合
    """
    print("\n" + "=" * 60)
    print("练习4参考答案: 蛋白质组学数据筛选 ⭐⭐")
    print("-" * 60)
    
    # 创建模拟的蛋白质数据
    np.random.seed(42)
    proteins = [f"Protein_{i:03d}" for i in range(1, 21)]
    
    protein_data = pd.DataFrame({
        'Protein_ID': proteins,
        'Molecular_Weight': np.random.uniform(10, 200, 20).round(1),
        'Expression_Level': np.random.uniform(0.1, 100, 20).round(2),
        'Peptides_Detected': np.random.randint(1, 15, 20),
        'Cellular_Location': np.random.choice(['Nucleus', 'Cytoplasm', 'Membrane', 'Mitochondria'], 20)
    })
    
    print("蛋白质组学数据总览:")
    print(protein_data.head(10))
    print(f"\n数据集大小: {len(protein_data)} 个蛋白质")
    
    print("\n任务1: 高可信度蛋白质筛选")
    print("筛选条件：检测肽段数≥5 且 表达水平≥10 FPKM")
    
    # 复合筛选条件
    high_confidence = protein_data[
        (protein_data['Peptides_Detected'] >= 5) & 
        (protein_data['Expression_Level'] >= 10)
    ]
    
    print(f"高可信度蛋白质: {len(high_confidence)} 个 ({len(high_confidence)/len(protein_data)*100:.1f}%)")
    
    if len(high_confidence) > 0:
        print("\n高可信度蛋白质列表:")
        display_cols = ['Protein_ID', 'Expression_Level', 'Peptides_Detected', 'Cellular_Location']
        print(high_confidence[display_cols].sort_values('Expression_Level', ascending=False))
        
        print(f"\n高可信度蛋白质统计:")
        print(f"• 平均表达水平: {high_confidence['Expression_Level'].mean():.2f} FPKM")
        print(f"• 平均检测肽段: {high_confidence['Peptides_Detected'].mean():.1f} 个")
    
    print("\n任务2: 按细胞定位分组统计")
    location_stats = protein_data.groupby('Cellular_Location').agg({
        'Expression_Level': ['count', 'mean', 'std', 'max'],
        'Molecular_Weight': ['mean', 'std'],
        'Peptides_Detected': 'mean'
    }).round(2)
    
    print("各细胞区域的蛋白质统计:")
    print(location_stats)
    
    # 更详细的分组分析
    print("\n各区域详细分析:")
    for location in protein_data['Cellular_Location'].unique():
        subset = protein_data[protein_data['Cellular_Location'] == location]
        print(f"\n{location}区域 ({len(subset)} 个蛋白质):")
        print(f"  • 表达水平: {subset['Expression_Level'].mean():.1f} ± {subset['Expression_Level'].std():.1f} FPKM")
        print(f"  • 分子量: {subset['Molecular_Weight'].mean():.1f} ± {subset['Molecular_Weight'].std():.1f} kDa")
        print(f"  • 平均肽段: {subset['Peptides_Detected'].mean():.1f} 个")
    
    print("\n任务3: 大分子量高表达蛋白")
    print("条件：分子量>100 kDa 且 表达水平>50 FPKM")
    
    large_abundant = protein_data[
        (protein_data['Molecular_Weight'] > 100) & 
        (protein_data['Expression_Level'] > 50)
    ]
    
    print(f"符合条件的蛋白质: {len(large_abundant)} 个")
    
    if len(large_abundant) > 0:
        print("\n大分子高表达蛋白质:")
        cols_to_show = ['Protein_ID', 'Molecular_Weight', 'Expression_Level', 'Cellular_Location']
        print(large_abundant[cols_to_show].sort_values('Expression_Level', ascending=False))
        
        print("\n🧬 生物学意义:")
        print("• 大分子量高表达蛋白通常是结构蛋白或酶类")
        print("• 在细胞中执行重要的生物学功能")
        print("• 可能是潜在的药物靶点或生物标志物")
    else:
        print("未发现符合条件的蛋白质")
    
    print("\n任务4: 综合质量评估")
    # 根据多个指标评估蛋白质质量
    protein_data['Quality_Score'] = (
        (protein_data['Expression_Level'] / protein_data['Expression_Level'].max()) * 0.4 +
        (protein_data['Peptides_Detected'] / protein_data['Peptides_Detected'].max()) * 0.6
    )
    
    high_quality = protein_data[protein_data['Quality_Score'] > 0.7].sort_values('Quality_Score', ascending=False)
    print(f"高质量蛋白质 (综合评分>0.7): {len(high_quality)} 个")
    
    if len(high_quality) > 0:
        print("\n质量评分最高的前5个蛋白质:")
        cols = ['Protein_ID', 'Expression_Level', 'Peptides_Detected', 'Quality_Score']
        print(high_quality[cols].head().round(3))


def solution_5_missing_data():
    """
    练习5参考答案: 缺失数据处理
    
    学习要点：缺失值检测、处理策略、数据完整性评估
    """
    print("\n" + "=" * 60)
    print("练习5参考答案: 实验数据缺失值处理 ⭐⭐")
    print("-" * 60)
    
    # 创建包含缺失值的qPCR数据
    qpcr_data = pd.DataFrame({
        'Sample_A': [2.3, 4.5, np.nan, 3.8, 2.1],
        'Sample_B': [3.2, np.nan, 5.1, 4.2, np.nan],
        'Sample_C': [1.9, 3.4, 4.8, np.nan, 2.8],
        'Sample_D': [2.8, 4.1, 5.3, 4.6, 3.2]
    }, index=['Gene_1', 'Gene_2', 'Gene_3', 'Gene_4', 'Gene_5'])
    
    print("原始qPCR相对表达量数据:")
    print(qpcr_data)
    
    print("\n任务1: 缺失值检测分析")
    
    # 基本缺失值统计
    total_missing = qpcr_data.isnull().sum().sum()
    total_values = qpcr_data.size
    missing_percent = (total_missing / total_values) * 100
    
    print(f"📊 总体统计:")
    print(f"• 总数据点: {total_values}")
    print(f"• 缺失值数量: {total_missing}")
    print(f"• 缺失比例: {missing_percent:.1f}%")
    
    print(f"\n按样本统计缺失值:")
    sample_missing = qpcr_data.isnull().sum()
    for sample, count in sample_missing.items():
        percent = (count / len(qpcr_data)) * 100
        print(f"• {sample}: {count} 个缺失 ({percent:.1f}%)")
    
    print(f"\n按基因统计缺失值:")
    gene_missing = qpcr_data.isnull().sum(axis=1)
    for gene, count in gene_missing.items():
        percent = (count / len(qpcr_data.columns)) * 100
        print(f"• {gene}: {count} 个缺失 ({percent:.1f}%)")
    
    print("\n任务2: 不同缺失值处理策略")
    
    # 策略1：删除包含缺失值的行
    print("\n策略1: 删除包含缺失值的行")
    clean_data_dropna = qpcr_data.dropna()
    print(f"删除后剩余: {len(clean_data_dropna)} 个基因 (损失 {len(qpcr_data) - len(clean_data_dropna)} 个)")
    print(clean_data_dropna)
    
    # 策略2：删除包含缺失值的列
    print("\n策略2: 删除包含缺失值的列")
    clean_data_drop_cols = qpcr_data.dropna(axis=1)
    remaining_samples = len(clean_data_drop_cols.columns)
    print(f"保留样本: {remaining_samples} 个 (删除 {len(qpcr_data.columns) - remaining_samples} 个)")
    if remaining_samples > 0:
        print(clean_data_drop_cols)
    
    # 策略3：用均值填补
    print("\n策略3: 用均值填补缺失值")
    filled_mean = qpcr_data.fillna(qpcr_data.mean())
    print("用各样本均值填补后:")
    print(filled_mean.round(2))
    
    # 显示填补的值
    print("\n填补的具体数值:")
    for col in qpcr_data.columns:
        mean_val = qpcr_data[col].mean()
        missing_positions = qpcr_data[col].isnull()
        if missing_positions.any():
            genes_filled = qpcr_data.index[missing_positions].tolist()
            print(f"• {col}: {genes_filled} 填补为 {mean_val:.2f}")
    
    # 策略4：用中位数填补
    print("\n策略4: 用中位数填补缺失值")
    filled_median = qpcr_data.fillna(qpcr_data.median())
    print("用各样本中位数填补后:")
    print(filled_median.round(2))
    
    # 策略5：前向填充
    print("\n策略5: 前向填充 (用上一行的值)")
    filled_ffill = qpcr_data.fillna(method='ffill')
    print(filled_ffill.round(2))
    
    print("\n任务3: 数据完整性评估")
    
    completeness = (1 - qpcr_data.isnull().sum() / len(qpcr_data)) * 100
    print("各样本数据完整性:")
    for sample, percent in completeness.items():
        status = "优秀" if percent == 100 else "良好" if percent >= 80 else "需改进"
        print(f"• {sample}: {percent:.1f}% ({status})")
    
    # 基因水平完整性
    gene_completeness = (1 - qpcr_data.isnull().sum(axis=1) / len(qpcr_data.columns)) * 100
    print(f"\n各基因数据完整性:")
    for gene, percent in gene_completeness.items():
        status = "完整" if percent == 100 else "部分缺失" if percent >= 75 else "严重缺失"
        print(f"• {gene}: {percent:.1f}% ({status})")
    
    print("\n任务4: 最佳处理策略建议")
    
    # 根据缺失模式给出建议
    if total_missing / total_values < 0.1:  # 缺失<10%
        recommendation = "均值填补"
        reason = "缺失比例较低，均值填补对结果影响小"
    elif sample_missing.max() <= 1:  # 每个样本缺失不超过1个
        recommendation = "中位数填补"
        reason = "缺失分布均匀，中位数填补更稳健"
    else:
        recommendation = "删除法结合填补法"
        reason = "缺失较多，需要综合考虑数据质量和样本量"
    
    print(f"🎯 推荐处理策略: {recommendation}")
    print(f"理由: {reason}")
    
    # 比较不同方法的效果
    print(f"\n📈 方法效果比较:")
    print(f"• 原始数据: {len(qpcr_data)} 基因 × {len(qpcr_data.columns)} 样本")
    print(f"• 删除行法: {len(clean_data_dropna)} 基因保留")
    print(f"• 均值填补: 数据完整，可能引入偏差")
    print(f"• 中位数填补: 数据完整，对异常值稳健")
    
    print(f"\n🧬 实验建议:")
    print("• 优先提高实验技术，减少缺失值产生")
    print("• 设计实验时考虑技术重复")
    print("• 关键基因的缺失值需特别关注")
    print("• 统计分析前明确报告缺失值处理方法")


def main():
    """
    运行所有练习的参考答案
    """
    print("🧬 Chapter 06: Pandas入门 - 练习参考答案")
    print("展示生物学数据分析的完整解决方案")
    print("=" * 60)
    
    # 运行所有答案演示
    solution_1_series_basics()
    solution_2_dataframe_creation()
    solution_3_gene_expression_analysis()
    solution_4_data_filtering()
    solution_5_missing_data()
    
    # 学习总结
    print("\n" + "=" * 60)
    print("📚 Pandas核心技能总结")
    print("=" * 60)
    
    print("\n🎯 你已经掌握了:")
    print("✅ Series和DataFrame的创建和操作")
    print("✅ 数据选择、筛选和排序")
    print("✅ 基础统计分析和聚合")
    print("✅ 缺失值检测和处理")
    print("✅ 生物学数据的实际应用")
    
    print("\n🔧 核心方法回顾:")
    print("• 数据创建: pd.Series(), pd.DataFrame()")
    print("• 数据选择: .loc[], .iloc[], 布尔索引")
    print("• 统计分析: .mean(), .std(), .describe()")
    print("• 数据清洗: .dropna(), .fillna(), .isnull()")
    print("• 分组操作: .groupby().agg()")
    
    print("\n🧬 生物学应用场景:")
    print("• 基因表达数据分析和差异检测")
    print("• qPCR结果处理和质量控制")
    print("• 蛋白质组学数据筛选和分类")
    print("• 实验数据的缺失值处理")
    print("• 多样本多指标的统计比较")
    
    print("\n🚀 进阶学习方向:")
    print("1. 高级Pandas操作 (Chapter 07):")
    print("   • 数据合并和连接")
    print("   • 数据透视表")
    print("   • 时间序列分析")
    print("   • 高级分组统计")
    
    print("\n2. 数据可视化 (Chapter 08):")
    print("   • 使用matplotlib和seaborn")
    print("   • 生物学数据的图表制作")
    print("   • 交互式可视化")
    
    print("\n3. 专业生信工具 (Chapter 09):")
    print("   • BioPython库应用")
    print("   • 序列分析自动化")
    print("   • 大规模数据处理")
    
    print("\n💡 学习建议:")
    print("• 多练习不同类型的生物学数据")
    print("• 关注数据质量控制")
    print("• 学会选择合适的统计方法")
    print("• 注重结果的生物学解释")
    
    print(f"\n🎉 恭喜完成Pandas入门学习!")
    print("现在你可以用Python像Excel一样分析数据，但功能更强大！")


if __name__ == "__main__":
    main()