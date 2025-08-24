#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 07: Pandas高级数据分析 - 完整的RNA-seq分析流程

生物学问题：如何从转录组数据中发现疾病相关基因？
编程概念：Pandas的高级数据操作就像实验室的多通道移液器，能同时处理多个样本

本章演示：
1. 多实验数据整合 - 像整合多个实验室的数据
2. 批次效应校正 - 消除实验批次带来的系统性偏差
3. 统计检验 - 严格的假设检验确保结果可靠
4. 时间序列分析 - 追踪基因表达的动态变化
5. 功能分组分析 - 按基因功能或位置分组研究
"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multitest import multipletests
import warnings
warnings.filterwarnings('ignore')


def demonstrate_data_integration():
    """
    演示多个RNA-seq实验数据的整合
    
    生物学类比：就像合并多个实验室的Western blot结果，
    需要标准化和对齐数据
    """
    print("🧬 数据整合：合并多个转录组实验")
    print("=" * 60)
    
    # 模拟三个不同实验的数据（如不同时间点或不同处理）
    np.random.seed(42)
    genes = [f"GENE_{i:04d}" for i in range(1, 101)]
    
    # 实验1：早期时间点
    exp1 = pd.DataFrame({
        'gene_id': genes,
        'sample1': np.random.lognormal(8, 1.5, 100),
        'sample2': np.random.lognormal(8, 1.5, 100),
        'sample3': np.random.lognormal(8, 1.5, 100),
        'timepoint': 'T0'
    })
    
    # 实验2：中期时间点
    exp2 = pd.DataFrame({
        'gene_id': genes,
        'sample1': np.random.lognormal(8.5, 1.5, 100),
        'sample2': np.random.lognormal(8.5, 1.5, 100),
        'sample3': np.random.lognormal(8.5, 1.5, 100),
        'timepoint': 'T6'
    })
    
    # 实验3：晚期时间点
    exp3 = pd.DataFrame({
        'gene_id': genes,
        'sample1': np.random.lognormal(9, 1.5, 100),
        'sample2': np.random.lognormal(9, 1.5, 100),
        'sample3': np.random.lognormal(9, 1.5, 100),
        'timepoint': 'T24'
    })
    
    # 合并数据 - 纵向堆叠
    all_data = pd.concat([exp1, exp2, exp3], ignore_index=True)
    
    # 数据重塑 - 从宽格式转换为长格式
    long_data = pd.melt(all_data, 
                        id_vars=['gene_id', 'timepoint'],
                        value_vars=['sample1', 'sample2', 'sample3'],
                        var_name='sample',
                        value_name='expression')
    
    print("整合后的数据结构（前10行）：")
    print(long_data.head(10))
    
    # 创建透视表分析
    pivot_table = long_data.pivot_table(
        index='gene_id',
        columns='timepoint',
        values='expression',
        aggfunc='mean'
    )
    
    print("\n基因表达透视表（前5个基因）：")
    print(pivot_table.head().round(2))
    
    return long_data, pivot_table


def perform_differential_expression_analysis():
    """
    执行完整的差异表达分析流程
    
    生物学类比：像做qPCR验证，需要多个技术重复和生物学重复，
    还要进行统计检验确保结果可靠
    """
    print("\n📊 差异表达分析：识别疾病相关基因")
    print("=" * 60)
    
    # 创建模拟的RNA-seq计数数据
    np.random.seed(42)
    n_genes = 500
    gene_ids = [f"GENE_{i:04d}" for i in range(1, n_genes + 1)]
    
    # 生成对照组数据（3个生物学重复）
    control_mean = np.random.lognormal(8, 2, n_genes)
    control_data = np.column_stack([
        np.random.poisson(control_mean * np.random.uniform(0.8, 1.2)) 
        for _ in range(3)
    ])
    
    # 生成处理组数据（部分基因上调或下调）
    treatment_mean = control_mean.copy()
    # 20%基因上调
    up_genes = np.random.choice(n_genes, size=int(n_genes * 0.2), replace=False)
    treatment_mean[up_genes] *= np.random.uniform(2, 5, len(up_genes))
    # 20%基因下调
    down_genes = np.random.choice(
        [i for i in range(n_genes) if i not in up_genes], 
        size=int(n_genes * 0.2), 
        replace=False
    )
    treatment_mean[down_genes] *= np.random.uniform(0.2, 0.5, len(down_genes))
    
    treatment_data = np.column_stack([
        np.random.poisson(treatment_mean * np.random.uniform(0.8, 1.2))
        for _ in range(3)
    ])
    
    # 创建表达矩阵
    expression_df = pd.DataFrame({
        'gene_id': gene_ids,
        'control_1': control_data[:, 0],
        'control_2': control_data[:, 1],
        'control_3': control_data[:, 2],
        'treatment_1': treatment_data[:, 0],
        'treatment_2': treatment_data[:, 1],
        'treatment_3': treatment_data[:, 2]
    })
    
    # 计算统计指标
    expression_df['control_mean'] = expression_df[['control_1', 'control_2', 'control_3']].mean(axis=1)
    expression_df['treatment_mean'] = expression_df[['treatment_1', 'treatment_2', 'treatment_3']].mean(axis=1)
    expression_df['fold_change'] = expression_df['treatment_mean'] / (expression_df['control_mean'] + 1)  # 加1避免除零
    expression_df['log2_fc'] = np.log2(expression_df['fold_change'] + 0.01)  # 加小值避免log(0)
    
    # 执行t检验
    p_values = []
    for i in range(len(expression_df)):
        control_values = expression_df.iloc[i][['control_1', 'control_2', 'control_3']].values
        treatment_values = expression_df.iloc[i][['treatment_1', 'treatment_2', 'treatment_3']].values
        _, p_value = stats.ttest_ind(control_values, treatment_values)
        p_values.append(p_value)
    
    expression_df['p_value'] = p_values
    
    # FDR校正（控制假阳性）
    _, fdr_corrected, _, _ = multipletests(expression_df['p_value'].values, 
                                           method='fdr_bh')
    expression_df['fdr'] = fdr_corrected
    
    # 筛选显著差异表达基因
    sig_threshold = 0.05
    fc_threshold = 2
    
    sig_genes = expression_df[
        (expression_df['fdr'] < sig_threshold) & 
        (np.abs(expression_df['log2_fc']) > np.log2(fc_threshold))
    ].copy()
    
    # 分类：上调和下调
    sig_genes['regulation'] = sig_genes['log2_fc'].apply(
        lambda x: 'up' if x > 0 else 'down'
    )
    
    print(f"总基因数: {len(expression_df)}")
    print(f"显著差异表达基因: {len(sig_genes)}")
    print(f"  - 上调: {len(sig_genes[sig_genes['regulation'] == 'up'])}")
    print(f"  - 下调: {len(sig_genes[sig_genes['regulation'] == 'down'])}")
    
    print("\n最显著的上调基因（Top 5）:")
    top_up = sig_genes[sig_genes['regulation'] == 'up'].nlargest(5, 'log2_fc')
    print(top_up[['gene_id', 'fold_change', 'p_value', 'fdr']].round(4))
    
    print("\n最显著的下调基因（Top 5）:")
    top_down = sig_genes[sig_genes['regulation'] == 'down'].nsmallest(5, 'log2_fc')
    print(top_down[['gene_id', 'fold_change', 'p_value', 'fdr']].round(4))
    
    return expression_df, sig_genes


def analyze_time_series_expression():
    """
    分析基因表达的时间动态变化
    
    生物学类比：就像观察细胞分化过程中的基因表达变化，
    需要在多个时间点采样并追踪变化模式
    """
    print("\n⏰ 时间序列分析：追踪基因表达动态")
    print("=" * 60)
    
    # 创建时间序列数据
    time_points = [0, 2, 4, 6, 8, 12, 24]  # 小时
    n_genes = 50
    gene_ids = [f"GENE_{i:04d}" for i in range(1, n_genes + 1)]
    
    # 生成不同表达模式的基因
    expression_patterns = []
    pattern_types = []
    
    for i in range(n_genes):
        if i < 10:  # 早期响应基因
            pattern = np.array([100 * np.exp(-t/5) + 20 for t in time_points])
            pattern_types.append('early_response')
        elif i < 20:  # 晚期响应基因
            pattern = np.array([20 + 80 * (1 - np.exp(-t/10)) for t in time_points])
            pattern_types.append('late_response')
        elif i < 30:  # 周期性基因
            pattern = np.array([50 + 30 * np.sin(t * np.pi / 12) for t in time_points])
            pattern_types.append('oscillating')
        else:  # 稳定表达基因
            pattern = np.array([50 + np.random.normal(0, 5, len(time_points))])
            pattern_types.append('stable')
        
        # 添加噪声
        pattern = pattern * np.random.uniform(0.9, 1.1, len(time_points))
        expression_patterns.append(pattern)
    
    # 创建时间序列DataFrame
    time_series_data = pd.DataFrame(expression_patterns, 
                                   columns=[f'T{t}h' for t in time_points])
    time_series_data['gene_id'] = gene_ids
    time_series_data['pattern_type'] = pattern_types
    
    # 重新排列列
    cols = ['gene_id', 'pattern_type'] + [f'T{t}h' for t in time_points]
    time_series_data = time_series_data[cols]
    
    # 计算时间序列统计
    time_cols = [f'T{t}h' for t in time_points]
    time_series_data['mean_expression'] = time_series_data[time_cols].mean(axis=1)
    time_series_data['std_expression'] = time_series_data[time_cols].std(axis=1)
    time_series_data['cv'] = (time_series_data['std_expression'] / 
                              time_series_data['mean_expression'])
    
    # 计算最大变化幅度
    time_series_data['max_change'] = (time_series_data[time_cols].max(axis=1) - 
                                      time_series_data[time_cols].min(axis=1))
    
    print("时间序列数据概览：")
    print(time_series_data.groupby('pattern_type').agg({
        'mean_expression': 'mean',
        'cv': 'mean',
        'max_change': 'mean'
    }).round(2))
    
    print("\n高变异基因（CV > 0.3）：")
    high_var_genes = time_series_data[time_series_data['cv'] > 0.3]
    print(high_var_genes[['gene_id', 'pattern_type', 'cv', 'max_change']].head(10).round(3))
    
    # 计算相关性矩阵（找出相似表达模式的基因）
    correlation_matrix = time_series_data[time_cols].T.corr()
    
    print("\n基因表达相关性分析：")
    print(f"相关性矩阵大小: {correlation_matrix.shape}")
    
    # 找出高度相关的基因对
    high_corr_pairs = []
    for i in range(len(correlation_matrix)):
        for j in range(i+1, len(correlation_matrix)):
            if abs(correlation_matrix.iloc[i, j]) > 0.9:
                high_corr_pairs.append({
                    'gene1': gene_ids[i],
                    'gene2': gene_ids[j],
                    'correlation': correlation_matrix.iloc[i, j]
                })
    
    if high_corr_pairs:
        high_corr_df = pd.DataFrame(high_corr_pairs).head(5)
        print(f"高度相关的基因对（|r| > 0.9，前5对）：")
        print(high_corr_df.round(3))
    
    return time_series_data


def perform_functional_grouping_analysis():
    """
    按基因功能或染色体位置进行分组分析
    
    生物学类比：就像将基因按照GO功能分类或按染色体位置分组，
    研究不同功能模块或基因组区域的表达特征
    """
    print("\n🔬 功能分组分析：研究基因功能模块")
    print("=" * 60)
    
    # 创建基因注释数据
    np.random.seed(42)
    n_genes = 200
    gene_ids = [f"GENE_{i:04d}" for i in range(1, n_genes + 1)]
    
    # 模拟基因功能分类
    functions = ['metabolism', 'cell_cycle', 'immune_response', 
                'transcription', 'signal_transduction']
    gene_functions = np.random.choice(functions, n_genes)
    
    # 模拟染色体位置
    chromosomes = [f'chr{i}' for i in range(1, 23)] + ['chrX', 'chrY']
    gene_chromosomes = np.random.choice(chromosomes[:10], n_genes)  # 使用前10条染色体
    
    # 模拟基因表达数据（不同功能的基因有不同的表达模式）
    expression_data = []
    for func in gene_functions:
        if func == 'metabolism':
            expr = np.random.lognormal(8, 1)
        elif func == 'cell_cycle':
            expr = np.random.lognormal(7, 1.5)
        elif func == 'immune_response':
            expr = np.random.lognormal(6, 2)
        elif func == 'transcription':
            expr = np.random.lognormal(9, 0.5)
        else:  # signal_transduction
            expr = np.random.lognormal(7.5, 1)
        expression_data.append(expr)
    
    # 创建综合数据框
    gene_annotation_df = pd.DataFrame({
        'gene_id': gene_ids,
        'function': gene_functions,
        'chromosome': gene_chromosomes,
        'expression': expression_data,
        'length': np.random.randint(500, 5000, n_genes)  # 基因长度
    })
    
    # 按功能分组分析
    print("按功能分组的表达分析：")
    function_stats = gene_annotation_df.groupby('function').agg({
        'expression': ['mean', 'std', 'count'],
        'length': 'mean'
    }).round(2)
    function_stats.columns = ['_'.join(col).strip() for col in function_stats.columns]
    print(function_stats)
    
    # 按染色体分组分析
    print("\n按染色体分组的基因分布：")
    chr_stats = gene_annotation_df.groupby('chromosome').agg({
        'gene_id': 'count',
        'expression': 'mean',
        'length': 'sum'
    }).rename(columns={'gene_id': 'gene_count', 
                       'expression': 'mean_expression',
                       'length': 'total_length'})
    chr_stats = chr_stats.sort_values('gene_count', ascending=False).head(5)
    print(chr_stats.round(2))
    
    # 功能富集分析（模拟）
    print("\n功能富集分析（模拟超几何检验）：")
    # 假设我们有一组差异表达基因
    n_deg = 50  # 差异表达基因数
    deg_indices = np.random.choice(n_genes, n_deg, replace=False)
    deg_functions = gene_annotation_df.iloc[deg_indices]['function'].value_counts()
    
    enrichment_results = []
    for func in functions:
        n_func_in_deg = deg_functions.get(func, 0)
        n_func_total = (gene_annotation_df['function'] == func).sum()
        # 简化的富集分数计算
        enrichment_score = (n_func_in_deg / n_deg) / (n_func_total / n_genes)
        enrichment_results.append({
            'function': func,
            'genes_in_DEG': n_func_in_deg,
            'genes_total': n_func_total,
            'enrichment_score': enrichment_score
        })
    
    enrichment_df = pd.DataFrame(enrichment_results)
    enrichment_df = enrichment_df.sort_values('enrichment_score', ascending=False)
    print(enrichment_df.round(3))
    
    return gene_annotation_df, enrichment_df


def demonstrate_advanced_operations():
    """
    演示其他高级Pandas操作
    
    包括：窗口函数、数据透视、多级索引等
    """
    print("\n🎯 高级数据操作技巧")
    print("=" * 60)
    
    # 创建多级索引数据
    np.random.seed(42)
    
    # 模拟多个实验条件的数据
    conditions = ['control', 'treatment_A', 'treatment_B']
    replicates = ['rep1', 'rep2', 'rep3']
    genes = [f'GENE_{i:03d}' for i in range(1, 21)]
    
    # 创建多级索引
    index = pd.MultiIndex.from_product([conditions, replicates], 
                                      names=['condition', 'replicate'])
    
    # 生成表达数据
    data = np.random.lognormal(8, 1, (9, 20))
    multi_index_df = pd.DataFrame(data, index=index, columns=genes)
    
    print("多级索引数据结构：")
    print(multi_index_df.head())
    
    # 使用groupby和transform
    print("\n计算每个条件的z-score标准化：")
    # 按条件分组，计算z-score
    zscore_df = multi_index_df.groupby(level='condition').transform(
        lambda x: (x - x.mean()) / x.std()
    )
    print(zscore_df.head().round(2))
    
    # 滑动窗口计算
    print("\n滑动窗口分析（模拟时间序列）：")
    time_series = pd.Series(np.random.randn(20).cumsum(), 
                           index=pd.date_range('2024-01-01', periods=20))
    
    # 计算3天移动平均
    rolling_mean = time_series.rolling(window=3).mean()
    rolling_std = time_series.rolling(window=3).std()
    
    result_df = pd.DataFrame({
        'original': time_series,
        'rolling_mean': rolling_mean,
        'rolling_std': rolling_std
    })
    print(result_df.tail(10).round(3))
    
    return multi_index_df


def main():
    """
    主函数 - 完整的RNA-seq数据分析流程
    """
    print("=" * 70)
    print("Chapter 07: Pandas高级数据分析 - 完整RNA-seq分析流程")
    print("=" * 70)
    print("\n从原始数据到生物学发现的完整分析管道\n")
    
    # 1. 数据整合
    long_data, pivot_table = demonstrate_data_integration()
    
    # 2. 差异表达分析
    expression_df, sig_genes = perform_differential_expression_analysis()
    
    # 3. 时间序列分析
    time_series_data = analyze_time_series_expression()
    
    # 4. 功能分组分析
    gene_annotation_df, enrichment_df = perform_functional_grouping_analysis()
    
    # 5. 高级操作演示
    multi_index_df = demonstrate_advanced_operations()
    
    # 总结
    print("\n" + "=" * 70)
    print("📊 本章核心要点总结")
    print("=" * 70)
    
    print("""
    1. 数据整合：多个实验数据的标准化合并
       - 使用concat、merge、join整合数据
       - 数据重塑：pivot、melt、stack/unstack
    
    2. 统计分析：严格的假设检验流程
       - t检验识别差异表达
       - FDR校正控制假阳性
       - 效应大小（fold change）评估生物学意义
    
    3. 时间序列：动态表达模式分析
       - 识别早期/晚期响应基因
       - 相关性分析找出共表达基因
       - 变异系数评估表达稳定性
    
    4. 功能分析：基因功能模块研究
       - 按功能或位置分组
       - 富集分析识别关键通路
       - 多维度数据整合
    
    5. 高级技巧：
       - 多级索引处理复杂实验设计
       - 窗口函数进行局部分析
       - 向量化操作提升性能
    """)
    
    print("\n💡 生物学洞察：")
    print("   通过系统的数据分析，我们可以：")
    print("   • 识别疾病相关的关键基因")
    print("   • 理解基因表达的时空动态")
    print("   • 发现功能相关的基因模块")
    print("   • 为后续实验验证提供候选靶点")
    
    print("\n🚀 下一步：学习数据可视化，将这些分析结果转化为直观的图表！")


if __name__ == "__main__":
    main()