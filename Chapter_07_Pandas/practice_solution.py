#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 07: Pandas高级数据分析 - 练习题参考答案

完整的转录组数据分析流程实现。
每个练习都有详细的注释说明关键步骤。
"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multitest import multipletests
import warnings
warnings.filterwarnings('ignore')


def practice_1_data_integration():
    """
    练习1参考答案：数据整合
    
    生物学类比：就像合并不同实验室的数据，需要对齐和标准化
    """
    print("练习1（★）：数据整合 - 参考答案")
    print("-" * 50)
    
    # 创建三个批次的模拟数据（有部分基因重叠）
    np.random.seed(42)
    
    # 批次1：100个基因
    batch1_genes = [f'GENE_{i:04d}' for i in range(1, 101)]
    batch1 = pd.DataFrame({
        'gene_id': batch1_genes,
        'batch1_sample1': np.random.lognormal(8, 1, 100),
        'batch1_sample2': np.random.lognormal(8, 1, 100),
        'batch1_sample3': np.random.lognormal(8, 1, 100)
    })
    
    # 批次2：80个基因（60个与批次1重叠）
    batch2_genes = [f'GENE_{i:04d}' for i in range(41, 121)]
    batch2 = pd.DataFrame({
        'gene_id': batch2_genes,
        'batch2_sample1': np.random.lognormal(8.2, 1, 80),
        'batch2_sample2': np.random.lognormal(8.2, 1, 80),
        'batch2_sample3': np.random.lognormal(8.2, 1, 80)
    })
    
    # 批次3：90个基因（部分重叠）
    batch3_genes = [f'GENE_{i:04d}' for i in range(21, 111)]
    batch3 = pd.DataFrame({
        'gene_id': batch3_genes,
        'batch3_sample1': np.random.lognormal(7.8, 1, 90),
        'batch3_sample2': np.random.lognormal(7.8, 1, 90),
        'batch3_sample3': np.random.lognormal(7.8, 1, 90)
    })
    
    # 合并数据 - 使用outer join保留所有基因
    merged = batch1.merge(batch2, on='gene_id', how='outer')
    merged = merged.merge(batch3, on='gene_id', how='outer')
    
    print(f"合并前：")
    print(f"  批次1: {len(batch1)} 个基因")
    print(f"  批次2: {len(batch2)} 个基因")
    print(f"  批次3: {len(batch3)} 个基因")
    
    print(f"\n合并后：")
    print(f"  总基因数: {len(merged)}")
    print(f"  总样本数: {len(merged.columns) - 1}")
    
    # 处理缺失值
    missing_before = merged.isnull().sum().sum()
    print(f"\n缺失值处理：")
    print(f"  处理前缺失值: {missing_before}")
    
    # 使用基因的平均值填充缺失值
    for col in merged.columns[1:]:  # 跳过gene_id列
        merged[col] = merged[col].fillna(merged[col].median())
    
    missing_after = merged.isnull().sum().sum()
    print(f"  处理后缺失值: {missing_after}")
    
    # 数据概况
    print(f"\n数据概况：")
    print(merged.describe().round(2))
    
    return merged


def practice_2_quality_control():
    """
    练习2参考答案：质量控制
    
    生物学类比：就像检查PCR产物的质量，需要识别失败的反应
    """
    print("\n练习2（★）：质量控制 - 参考答案")
    print("-" * 50)
    
    # 创建包含质量问题的数据
    np.random.seed(42)
    n_genes = 200
    n_samples = 10
    
    # 正常样本
    normal_data = np.random.lognormal(8, 1.5, (n_genes, n_samples-2))
    
    # 添加低质量样本（总reads很低）
    low_quality = np.random.lognormal(5, 1, (n_genes, 1))
    
    # 添加异常样本（极端值）
    outlier = np.random.lognormal(12, 0.5, (n_genes, 1))
    
    # 合并数据
    all_data = np.hstack([normal_data, low_quality, outlier])
    
    # 创建DataFrame
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    sample_ids = [f'Sample_{i}' for i in range(1, n_samples + 1)]
    
    df = pd.DataFrame(all_data, index=gene_ids, columns=sample_ids)
    
    # 计算质量指标
    total_reads = df.sum(axis=0)
    detected_genes = (df > 10).sum(axis=0)
    
    quality_metrics = pd.DataFrame({
        'total_reads': total_reads,
        'detected_genes': detected_genes,
        'avg_expression': df.mean(axis=0)
    })
    
    print("样本质量指标：")
    print(quality_metrics.round(2))
    
    # 识别离群样本（使用IQR方法）
    Q1 = quality_metrics['total_reads'].quantile(0.25)
    Q3 = quality_metrics['total_reads'].quantile(0.75)
    IQR = Q3 - Q1
    
    outlier_threshold_low = Q1 - 1.5 * IQR
    outlier_threshold_high = Q3 + 1.5 * IQR
    
    outliers = quality_metrics[
        (quality_metrics['total_reads'] < outlier_threshold_low) |
        (quality_metrics['total_reads'] > outlier_threshold_high)
    ]
    
    print(f"\n识别的异常样本：")
    if len(outliers) > 0:
        print(outliers.index.tolist())
    else:
        print("未发现异常样本")
    
    # 过滤低表达基因
    gene_mean = df.mean(axis=1)
    low_exp_threshold = 10
    high_exp_genes = df[gene_mean >= low_exp_threshold]
    
    print(f"\n基因过滤：")
    print(f"  过滤前基因数: {len(df)}")
    print(f"  过滤后基因数: {len(high_exp_genes)}")
    print(f"  被过滤的低表达基因: {len(df) - len(high_exp_genes)}")
    
    return df, quality_metrics


def practice_3_basic_statistics():
    """
    练习3参考答案：基本统计
    
    生物学类比：就像分析酶活性数据，需要了解数据的分布和变异
    """
    print("\n练习3（★）：基本统计 - 参考答案")
    print("-" * 50)
    
    # 创建基因表达数据
    np.random.seed(42)
    n_genes = 100
    n_samples = 6
    
    # 创建不同变异程度的基因
    expression_data = []
    gene_types = []
    
    for i in range(n_genes):
        if i < 20:  # 高变异基因
            expr = np.random.lognormal(8, 2, n_samples)
            gene_types.append('high_var')
        elif i < 40:  # 中等变异基因
            expr = np.random.lognormal(8, 1, n_samples)
            gene_types.append('medium_var')
        else:  # 低变异基因（管家基因）
            expr = np.random.lognormal(8, 0.3, n_samples)
            gene_types.append('low_var')
        expression_data.append(expr)
    
    # 创建DataFrame
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    sample_ids = [f'Sample_{i}' for i in range(1, n_samples + 1)]
    
    df = pd.DataFrame(expression_data, index=gene_ids, columns=sample_ids)
    df['gene_type'] = gene_types
    
    # 计算描述性统计
    stats_df = pd.DataFrame({
        'mean': df[sample_ids].mean(axis=1),
        'median': df[sample_ids].median(axis=1),
        'std': df[sample_ids].std(axis=1),
        'min': df[sample_ids].min(axis=1),
        'max': df[sample_ids].max(axis=1)
    })
    
    # 计算变异系数（CV = std/mean）
    stats_df['cv'] = stats_df['std'] / stats_df['mean']
    
    print("基因表达统计概览：")
    print(stats_df.describe().round(3))
    
    # 按基因类型分组统计
    print("\n按基因类型分组的CV统计：")
    cv_by_type = df.groupby('gene_type').apply(
        lambda x: (x[sample_ids].std(axis=1) / x[sample_ids].mean(axis=1)).mean()
    )
    print(cv_by_type.round(3))
    
    # 找出最稳定和最不稳定的基因
    n_top = 5
    most_stable = stats_df.nsmallest(n_top, 'cv')
    most_variable = stats_df.nlargest(n_top, 'cv')
    
    print(f"\n最稳定的{n_top}个基因（低CV）：")
    print(most_stable[['mean', 'cv']].round(3))
    
    print(f"\n最不稳定的{n_top}个基因（高CV）：")
    print(most_variable[['mean', 'cv']].round(3))
    
    return df, stats_df


def practice_4_differential_analysis():
    """
    练习4参考答案：差异表达分析
    
    生物学类比：就像比较两种细胞类型的蛋白表达差异
    """
    print("\n练习4（★★）：差异表达分析 - 参考答案")
    print("-" * 50)
    
    # 创建疾病组和健康组数据
    np.random.seed(42)
    n_genes = 300
    
    # 健康组（3个样本）
    healthy_mean = np.random.lognormal(8, 1.5, n_genes)
    healthy_data = np.column_stack([
        np.random.poisson(healthy_mean * np.random.uniform(0.9, 1.1))
        for _ in range(3)
    ])
    
    # 疾病组（3个样本）- 部分基因差异表达
    disease_mean = healthy_mean.copy()
    
    # 30%基因上调（如炎症相关基因）
    up_genes = np.random.choice(n_genes, size=int(n_genes * 0.3), replace=False)
    disease_mean[up_genes] *= np.random.uniform(2, 4, len(up_genes))
    
    # 20%基因下调（如代谢相关基因）
    remaining = [i for i in range(n_genes) if i not in up_genes]
    down_genes = np.random.choice(remaining, size=int(n_genes * 0.2), replace=False)
    disease_mean[down_genes] *= np.random.uniform(0.2, 0.5, len(down_genes))
    
    disease_data = np.column_stack([
        np.random.poisson(disease_mean * np.random.uniform(0.9, 1.1))
        for _ in range(3)
    ])
    
    # 创建DataFrame
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    
    df = pd.DataFrame({
        'gene_id': gene_ids,
        'healthy_1': healthy_data[:, 0],
        'healthy_2': healthy_data[:, 1],
        'healthy_3': healthy_data[:, 2],
        'disease_1': disease_data[:, 0],
        'disease_2': disease_data[:, 1],
        'disease_3': disease_data[:, 2]
    })
    
    # 计算fold change
    df['healthy_mean'] = df[['healthy_1', 'healthy_2', 'healthy_3']].mean(axis=1)
    df['disease_mean'] = df[['disease_1', 'disease_2', 'disease_3']].mean(axis=1)
    df['fold_change'] = (df['disease_mean'] + 1) / (df['healthy_mean'] + 1)
    df['log2_fc'] = np.log2(df['fold_change'])
    
    # 执行t检验
    p_values = []
    for i in range(len(df)):
        healthy_vals = df.iloc[i][['healthy_1', 'healthy_2', 'healthy_3']].values
        disease_vals = df.iloc[i][['disease_1', 'disease_2', 'disease_3']].values
        _, p_val = stats.ttest_ind(healthy_vals, disease_vals)
        p_values.append(p_val)
    
    df['p_value'] = p_values
    
    # FDR校正
    _, fdr_values, _, _ = multipletests(df['p_value'].values, method='fdr_bh')
    df['fdr'] = fdr_values
    
    # 筛选差异基因
    sig_threshold = 0.05
    fc_threshold = 2
    
    deg = df[
        (df['fdr'] < sig_threshold) & 
        (np.abs(df['log2_fc']) > np.log2(fc_threshold))
    ].copy()
    
    deg['regulation'] = deg['log2_fc'].apply(lambda x: 'UP' if x > 0 else 'DOWN')
    
    print(f"差异表达分析结果：")
    print(f"  总基因数: {len(df)}")
    print(f"  显著差异基因: {len(deg)}")
    print(f"    - 上调: {len(deg[deg['regulation'] == 'UP'])}")
    print(f"    - 下调: {len(deg[deg['regulation'] == 'DOWN'])}")
    
    print(f"\nTop 5 上调基因：")
    top_up = deg[deg['regulation'] == 'UP'].nlargest(5, 'log2_fc')
    print(top_up[['gene_id', 'fold_change', 'p_value', 'fdr']].round(4))
    
    print(f"\nTop 5 下调基因：")
    top_down = deg[deg['regulation'] == 'DOWN'].nsmallest(5, 'log2_fc')
    print(top_down[['gene_id', 'fold_change', 'p_value', 'fdr']].round(4))
    
    return df, deg


def practice_5_batch_correction():
    """
    练习5参考答案：批次效应校正
    
    生物学类比：就像校正不同批次抗体的背景信号差异
    """
    print("\n练习5（★★）：批次效应校正 - 参考答案")
    print("-" * 50)
    
    # 创建包含批次效应的数据
    np.random.seed(42)
    n_genes = 100
    
    # 批次1（3个样本）- 基线
    batch1 = np.random.lognormal(8, 1, (n_genes, 3))
    
    # 批次2（3个样本）- 系统性偏高
    batch2 = np.random.lognormal(8.5, 1, (n_genes, 3))
    
    # 批次3（3个样本）- 系统性偏低
    batch3 = np.random.lognormal(7.5, 1, (n_genes, 3))
    
    # 合并数据
    data = np.hstack([batch1, batch2, batch3])
    
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    sample_ids = [f'B{b}_S{s}' for b in range(1, 4) for s in range(1, 4)]
    batch_labels = ['Batch1'] * 3 + ['Batch2'] * 3 + ['Batch3'] * 3
    
    df = pd.DataFrame(data, index=gene_ids, columns=sample_ids)
    
    print("批次效应检测：")
    batch_means = {
        'Batch1': df.iloc[:, 0:3].mean().mean(),
        'Batch2': df.iloc[:, 3:6].mean().mean(),
        'Batch3': df.iloc[:, 6:9].mean().mean()
    }
    print("各批次平均表达量：")
    for batch, mean_val in batch_means.items():
        print(f"  {batch}: {mean_val:.2f}")
    
    # Z-score标准化校正
    print("\n应用Z-score标准化校正...")
    
    # 按批次分组标准化
    corrected_data = []
    for i in range(3):
        batch_data = df.iloc[:, i*3:(i+1)*3]
        # 计算每个基因在该批次的z-score
        batch_mean = batch_data.mean(axis=1)
        batch_std = batch_data.std(axis=1)
        batch_zscore = batch_data.sub(batch_mean, axis=0).div(batch_std, axis=0)
        corrected_data.append(batch_zscore)
    
    df_corrected = pd.concat(corrected_data, axis=1)
    
    # 验证校正效果
    print("\n校正后各批次平均z-score：")
    corrected_means = {
        'Batch1': df_corrected.iloc[:, 0:3].mean().mean(),
        'Batch2': df_corrected.iloc[:, 3:6].mean().mean(),
        'Batch3': df_corrected.iloc[:, 6:9].mean().mean()
    }
    for batch, mean_val in corrected_means.items():
        print(f"  {batch}: {mean_val:.4f}")
    
    print("\n批次效应校正成功！所有批次现在中心化为0")
    
    return df, df_corrected


def practice_6_functional_grouping():
    """
    练习6参考答案：功能分组分析
    
    生物学类比：就像将蛋白质按照GO功能分类研究
    """
    print("\n练习6（★★）：功能分组分析 - 参考答案")
    print("-" * 50)
    
    # 创建基因功能注释
    np.random.seed(42)
    n_genes = 150
    
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    
    # 功能类别
    functions = ['metabolism', 'immune', 'cell_cycle', 'transcription', 'signaling']
    gene_functions = np.random.choice(functions, n_genes, p=[0.3, 0.2, 0.2, 0.15, 0.15])
    
    # 不同功能的基因有不同的表达模式
    expression_data = []
    for func in gene_functions:
        if func == 'metabolism':
            expr = np.random.lognormal(9, 0.5, 6)  # 高表达，低变异
        elif func == 'immune':
            expr = np.random.lognormal(7, 2, 6)    # 中等表达，高变异
        elif func == 'cell_cycle':
            expr = np.random.lognormal(8, 1.5, 6)  # 中等表达和变异
        elif func == 'transcription':
            expr = np.random.lognormal(8.5, 1, 6)  # 较高表达
        else:  # signaling
            expr = np.random.lognormal(7.5, 1.5, 6)  # 中低表达
        expression_data.append(expr)
    
    # 创建DataFrame
    sample_ids = [f'Sample_{i}' for i in range(1, 7)]
    df = pd.DataFrame(expression_data, index=gene_ids, columns=sample_ids)
    df['function'] = gene_functions
    
    # 按功能分组分析
    print("按功能分组的表达分析：")
    function_stats = df.groupby('function')[sample_ids].agg(['mean', 'std', 'count'])
    
    # 整理输出格式
    summary = pd.DataFrame()
    for sample in sample_ids[:2]:  # 只显示前两个样本
        summary[f'{sample}_mean'] = function_stats[sample]['mean']
    summary['gene_count'] = function_stats[sample_ids[0]]['count']
    summary['avg_expression'] = df.groupby('function')[sample_ids].mean().mean(axis=1)
    summary['avg_std'] = df.groupby('function')[sample_ids].std().mean(axis=1)
    
    print(summary.round(2))
    
    # 功能富集分析（假设有一组感兴趣的基因）
    print("\n功能富集分析（模拟）：")
    
    # 随机选择50个基因作为"差异表达基因"
    deg_indices = np.random.choice(n_genes, 50, replace=False)
    deg_functions = df.iloc[deg_indices]['function'].value_counts()
    
    # 计算富集分数
    enrichment_results = []
    for func in functions:
        observed = deg_functions.get(func, 0)
        expected = (df['function'] == func).sum() * (50 / n_genes)
        enrichment = observed / expected if expected > 0 else 0
        
        enrichment_results.append({
            'function': func,
            'observed': observed,
            'expected': round(expected, 1),
            'enrichment_score': enrichment,
            'enriched': 'Yes' if enrichment > 1.5 else 'No'
        })
    
    enrichment_df = pd.DataFrame(enrichment_results)
    enrichment_df = enrichment_df.sort_values('enrichment_score', ascending=False)
    print(enrichment_df.round(2))
    
    return df, enrichment_df


def practice_7_time_series():
    """
    练习7参考答案：时间序列分析
    
    生物学类比：就像追踪药物处理后细胞的响应动态
    """
    print("\n练习7（★★★）：时间序列分析 - 参考答案")
    print("-" * 50)
    
    # 创建时间序列数据
    np.random.seed(42)
    time_points = [0, 1, 2, 4, 8, 24]  # 小时
    n_genes = 60
    
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    
    # 生成不同响应模式
    time_series_data = []
    response_patterns = []
    
    for i in range(n_genes):
        if i < 15:  # 早期响应（快速上升后下降）
            pattern = [50, 150, 120, 80, 60, 50]
            pattern = [p * np.random.uniform(0.8, 1.2) for p in pattern]
            response_patterns.append('early_response')
        elif i < 30:  # 晚期响应（缓慢上升）
            pattern = [50, 55, 65, 85, 120, 150]
            pattern = [p * np.random.uniform(0.8, 1.2) for p in pattern]
            response_patterns.append('late_response')
        elif i < 40:  # 瞬时响应（单峰）
            pattern = [50, 60, 150, 70, 55, 50]
            pattern = [p * np.random.uniform(0.8, 1.2) for p in pattern]
            response_patterns.append('transient')
        elif i < 50:  # 持续下调
            pattern = [100, 80, 60, 40, 30, 25]
            pattern = [p * np.random.uniform(0.8, 1.2) for p in pattern]
            response_patterns.append('sustained_down')
        else:  # 无响应
            pattern = [50 + np.random.normal(0, 5) for _ in time_points]
            response_patterns.append('no_response')
        
        time_series_data.append(pattern)
    
    # 创建DataFrame
    time_cols = [f'T{t}h' for t in time_points]
    df = pd.DataFrame(time_series_data, index=gene_ids, columns=time_cols)
    df['pattern'] = response_patterns
    
    # 分析表达变化趋势
    df['fold_change_max'] = df[time_cols].max(axis=1) / df['T0h']
    df['time_to_peak'] = df[time_cols].idxmax(axis=1)
    df['expression_range'] = df[time_cols].max(axis=1) - df[time_cols].min(axis=1)
    
    print("时间序列模式分析：")
    pattern_summary = df.groupby('pattern').agg({
        'fold_change_max': 'mean',
        'expression_range': 'mean',
        'T0h': 'count'
    }).rename(columns={'T0h': 'gene_count'})
    print(pattern_summary.round(2))
    
    # 识别早期响应基因（1-2小时内显著变化）
    early_threshold = 1.5  # 1.5倍变化
    early_genes = df[
        (df['T1h'] / df['T0h'] > early_threshold) |
        (df['T2h'] / df['T0h'] > early_threshold)
    ]
    
    print(f"\n早期响应基因（1-2小时内变化>{early_threshold}倍）：")
    print(f"  发现 {len(early_genes)} 个早期响应基因")
    if len(early_genes) > 0:
        print(f"  前5个: {early_genes.index[:5].tolist()}")
    
    # 计算基因间相关性（找出共调控基因）
    correlation_matrix = df[time_cols].T.corr()
    
    # 找出高度相关的基因对
    high_corr_pairs = []
    for i in range(len(correlation_matrix)):
        for j in range(i+1, len(correlation_matrix)):
            corr_val = correlation_matrix.iloc[i, j]
            if abs(corr_val) > 0.95:
                high_corr_pairs.append({
                    'gene1': gene_ids[i],
                    'gene2': gene_ids[j],
                    'correlation': corr_val,
                    'pattern1': df.iloc[i]['pattern'],
                    'pattern2': df.iloc[j]['pattern']
                })
    
    if high_corr_pairs:
        print(f"\n高度相关的基因对（|r| > 0.95）：")
        corr_df = pd.DataFrame(high_corr_pairs).head(5)
        print(corr_df[['gene1', 'gene2', 'correlation', 'pattern1']].round(3))
    
    return df


def practice_8_multi_omics_integration():
    """
    练习8参考答案：多组学数据整合
    
    生物学类比：整合Western blot（蛋白）和qPCR（mRNA）数据
    """
    print("\n练习8（★★★）：多组学整合 - 参考答案")
    print("-" * 50)
    
    # 创建转录组数据
    np.random.seed(42)
    n_genes = 100
    n_samples = 6
    
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    sample_ids = [f'Sample_{i}' for i in range(1, n_samples + 1)]
    
    # mRNA表达数据
    mrna_data = np.random.lognormal(8, 1.5, (n_genes, n_samples))
    mrna_df = pd.DataFrame(mrna_data, index=gene_ids, columns=sample_ids)
    
    # 蛋白质表达数据（与mRNA相关但不完全一致）
    protein_data = []
    regulation_types = []
    
    for i in range(n_genes):
        mrna_level = mrna_data[i]
        
        if i < 60:  # 60%基因：mRNA和蛋白质相关
            protein_level = mrna_level * np.random.uniform(0.8, 1.2) + np.random.normal(0, 100, n_samples)
            regulation_types.append('normal')
        elif i < 80:  # 20%基因：转录后抑制（mRNA高但蛋白低）
            protein_level = mrna_level * np.random.uniform(0.2, 0.4) + np.random.normal(0, 50, n_samples)
            regulation_types.append('post_transcriptional_repression')
        else:  # 20%基因：翻译增强（mRNA低但蛋白高）
            protein_level = mrna_level * np.random.uniform(2, 3) + np.random.normal(0, 200, n_samples)
            regulation_types.append('translational_enhancement')
        
        protein_data.append(protein_level)
    
    protein_df = pd.DataFrame(protein_data, index=gene_ids, columns=sample_ids)
    
    # 数据标准化（Z-score）
    mrna_zscore = (mrna_df - mrna_df.mean()) / mrna_df.std()
    protein_zscore = (protein_df - protein_df.mean()) / protein_df.std()
    
    # 计算mRNA-蛋白质相关性
    correlations = []
    for gene in gene_ids:
        corr = np.corrcoef(mrna_zscore.loc[gene], protein_zscore.loc[gene])[0, 1]
        correlations.append(corr)
    
    # 整合数据
    integrated_df = pd.DataFrame({
        'gene_id': gene_ids,
        'mrna_mean': mrna_df.mean(axis=1).values,
        'protein_mean': protein_df.mean(axis=1).values,
        'mrna_protein_corr': correlations,
        'regulation_type': regulation_types
    })
    
    # 计算mRNA/蛋白质比率
    integrated_df['mrna_protein_ratio'] = integrated_df['mrna_mean'] / (integrated_df['protein_mean'] + 1)
    
    print("多组学数据整合结果：")
    print(integrated_df.groupby('regulation_type').agg({
        'mrna_protein_corr': 'mean',
        'mrna_protein_ratio': 'mean',
        'gene_id': 'count'
    }).rename(columns={'gene_id': 'gene_count'}).round(3))
    
    # 识别转录后调控基因
    print("\n转录后调控基因识别：")
    
    # 低相关性基因可能受转录后调控
    low_corr_genes = integrated_df[integrated_df['mrna_protein_corr'] < 0.3]
    print(f"  低mRNA-蛋白相关基因（r < 0.3）: {len(low_corr_genes)} 个")
    
    # 高比率差异基因
    ratio_threshold_high = integrated_df['mrna_protein_ratio'].quantile(0.9)
    ratio_threshold_low = integrated_df['mrna_protein_ratio'].quantile(0.1)
    
    repressed = integrated_df[integrated_df['mrna_protein_ratio'] > ratio_threshold_high]
    enhanced = integrated_df[integrated_df['mrna_protein_ratio'] < ratio_threshold_low]
    
    print(f"  转录后抑制（高mRNA/蛋白比）: {len(repressed)} 个")
    print(f"  翻译增强（低mRNA/蛋白比）: {len(enhanced)} 个")
    
    return integrated_df


def practice_9_machine_learning():
    """
    练习9参考答案：机器学习应用
    
    生物学类比：就像根据基因表达谱诊断疾病亚型
    """
    print("\n练习9（★★★）：机器学习 - 参考答案")
    print("-" * 50)
    
    # 创建带标签的表达数据
    np.random.seed(42)
    n_samples = 60
    n_genes = 200
    
    # 三种癌症亚型
    labels = ['TypeA'] * 20 + ['TypeB'] * 20 + ['TypeC'] * 20
    
    # 为每种类型创建特征性表达模式
    expression_data = []
    
    for label in labels:
        if label == 'TypeA':
            # TypeA特征：某些基因高表达
            expr = np.random.lognormal(8, 1, n_genes)
            expr[0:30] *= 2  # 前30个基因高表达
        elif label == 'TypeB':
            # TypeB特征：另一组基因高表达
            expr = np.random.lognormal(8, 1, n_genes)
            expr[50:80] *= 2  # 中间30个基因高表达
        else:  # TypeC
            # TypeC特征：第三组基因高表达
            expr = np.random.lognormal(8, 1, n_genes)
            expr[100:130] *= 2  # 另外30个基因高表达
        
        expression_data.append(expr)
    
    # 创建DataFrame
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    sample_ids = [f'Sample_{i:03d}' for i in range(1, n_samples + 1)]
    
    df = pd.DataFrame(expression_data, columns=gene_ids, index=sample_ids)
    df['cancer_type'] = labels
    
    # 特征选择：选择高变异基因
    gene_std = df[gene_ids].std()
    top_genes = gene_std.nlargest(50).index.tolist()  # 选择50个高变异基因
    
    print(f"特征选择：")
    print(f"  总基因数: {n_genes}")
    print(f"  选择的特征基因: {len(top_genes)}")
    
    # 数据标准化
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X = scaler.fit_transform(df[top_genes])
    y = df['cancer_type'].values
    
    # 划分训练集和测试集
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"\n数据集划分：")
    print(f"  训练集: {len(X_train)} 样本")
    print(f"  测试集: {len(X_test)} 样本")
    
    # 使用简单的k近邻分类器
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score, classification_report
    
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    # 预测
    y_pred = knn.predict(X_test)
    
    # 评估
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n分类性能：")
    print(f"  准确率: {accuracy:.2%}")
    
    print(f"\n详细分类报告：")
    print(classification_report(y_test, y_pred))
    
    # 特征重要性（使用方差分析）
    from scipy.stats import f_oneway
    
    print(f"\n最具区分力的基因（ANOVA）：")
    f_scores = []
    for gene in top_genes[:10]:  # 只分析前10个基因
        groups = [df[df['cancer_type'] == t][gene].values for t in ['TypeA', 'TypeB', 'TypeC']]
        f_stat, p_val = f_oneway(*groups)
        f_scores.append({'gene': gene, 'f_score': f_stat, 'p_value': p_val})
    
    f_scores_df = pd.DataFrame(f_scores).sort_values('f_score', ascending=False)
    print(f_scores_df.head(5).round(4))
    
    return df, accuracy


def bonus_challenge():
    """
    额外挑战参考答案：完整的RNA-seq分析管道
    """
    print("\n🏆 额外挑战：完整RNA-seq分析管道 - 参考答案")
    print("-" * 50)
    
    print("实现完整分析流程...")
    
    # Step 1: 数据加载和质控
    print("\nStep 1: 数据加载和质控")
    np.random.seed(42)
    
    # 模拟原始计数矩阵
    n_genes = 500
    n_samples = 12  # 6个对照，6个处理
    
    raw_counts = np.random.negative_binomial(10, 0.3, (n_genes, n_samples))
    gene_ids = [f'GENE_{i:04d}' for i in range(1, n_genes + 1)]
    sample_ids = [f'Control_{i}' for i in range(1, 7)] + [f'Treatment_{i}' for i in range(1, 7)]
    
    counts_df = pd.DataFrame(raw_counts, index=gene_ids, columns=sample_ids)
    
    # 质控：过滤低表达基因
    min_count = 10
    min_samples = 3
    keep_genes = (counts_df >= min_count).sum(axis=1) >= min_samples
    filtered_df = counts_df[keep_genes]
    
    print(f"  过滤前: {len(counts_df)} 基因")
    print(f"  过滤后: {len(filtered_df)} 基因")
    
    # Step 2: 标准化（TPM）
    print("\nStep 2: TPM标准化")
    # 模拟基因长度
    gene_lengths = np.random.randint(500, 5000, len(filtered_df))
    
    # 计算TPM
    rpk = filtered_df.div(gene_lengths / 1000, axis=0)
    tpm = rpk.div(rpk.sum()) * 1e6
    
    print(f"  TPM标准化完成")
    print(f"  每个样本总TPM: {tpm.sum().mean():.0f}")
    
    # Step 3: 批次效应校正
    print("\nStep 3: 批次效应校正")
    # 假设前6个和后6个样本来自不同批次
    batch1_mean = tpm.iloc[:, :6].mean().mean()
    batch2_mean = tpm.iloc[:, 6:].mean().mean()
    print(f"  批次1平均: {batch1_mean:.2f}")
    print(f"  批次2平均: {batch2_mean:.2f}")
    
    # 简单的中心化校正
    tpm_corrected = tpm.copy()
    tpm_corrected.iloc[:, :6] = tpm_corrected.iloc[:, :6] - (batch1_mean - tpm.mean().mean())
    tpm_corrected.iloc[:, 6:] = tpm_corrected.iloc[:, 6:] - (batch2_mean - tpm.mean().mean())
    
    # Step 4: 差异表达分析
    print("\nStep 4: 差异表达分析")
    control_cols = [col for col in tpm_corrected.columns if 'Control' in col]
    treatment_cols = [col for col in tpm_corrected.columns if 'Treatment' in col]
    
    # 计算fold change和p值
    results = []
    for gene in tpm_corrected.index:
        control_vals = tpm_corrected.loc[gene, control_cols].values
        treatment_vals = tpm_corrected.loc[gene, treatment_cols].values
        
        fc = treatment_vals.mean() / (control_vals.mean() + 0.01)
        _, p_val = stats.ttest_ind(control_vals, treatment_vals)
        
        results.append({
            'gene': gene,
            'fold_change': fc,
            'log2_fc': np.log2(fc + 0.01),
            'p_value': p_val
        })
    
    deg_df = pd.DataFrame(results)
    
    # FDR校正
    _, fdr, _, _ = multipletests(deg_df['p_value'].values, method='fdr_bh')
    deg_df['fdr'] = fdr
    
    # 筛选差异基因
    sig_genes = deg_df[(deg_df['fdr'] < 0.05) & (np.abs(deg_df['log2_fc']) > 1)]
    
    print(f"  显著差异基因: {len(sig_genes)}")
    print(f"    - 上调: {len(sig_genes[sig_genes['log2_fc'] > 0])}")
    print(f"    - 下调: {len(sig_genes[sig_genes['log2_fc'] < 0])}")
    
    # Step 5: 功能富集分析（简化版）
    print("\nStep 5: 功能富集分析")
    # 模拟GO注释
    go_terms = ['metabolism', 'immune_response', 'cell_cycle', 'apoptosis', 'signaling']
    gene_go = {gene: np.random.choice(go_terms) for gene in filtered_df.index}
    
    # 富集分析
    sig_gene_list = sig_genes['gene'].tolist()
    sig_go_counts = pd.Series([gene_go[g] for g in sig_gene_list if g in gene_go]).value_counts()
    total_go_counts = pd.Series(list(gene_go.values())).value_counts()
    
    enrichment = (sig_go_counts / len(sig_gene_list)) / (total_go_counts / len(gene_go))
    
    print("  GO富集结果：")
    for term, score in enrichment.head().items():
        print(f"    {term}: {score:.2f}x")
    
    print("\n✅ 完整分析流程完成！")
    
    return deg_df


def main():
    """
    主函数 - 运行所有练习答案
    """
    print("=" * 70)
    print("Chapter 07: Pandas高级数据分析 - 练习题参考答案")
    print("=" * 70)
    print()
    
    # 基础练习
    print("【基础练习参考答案】\n")
    merged_data = practice_1_data_integration()
    df_raw, quality_metrics = practice_2_quality_control()
    df_expr, stats_df = practice_3_basic_statistics()
    
    # 进阶练习
    print("\n【进阶练习参考答案】\n")
    diff_df, deg = practice_4_differential_analysis()
    batch_df, corrected_df = practice_5_batch_correction()
    func_df, enrichment = practice_6_functional_grouping()
    
    # 挑战练习
    print("\n【挑战练习参考答案】\n")
    time_df = practice_7_time_series()
    integrated = practice_8_multi_omics_integration()
    ml_df, accuracy = practice_9_machine_learning()
    
    # 额外挑战
    print("\n【额外挑战参考答案】\n")
    final_results = bonus_challenge()
    
    print("\n" + "=" * 70)
    print("学习要点总结：")
    print("=" * 70)
    print("""
    1. 数据整合：处理多来源数据的缺失值和格式差异
    2. 质量控制：识别和处理异常样本是分析的第一步
    3. 统计分析：理解数据分布和变异是关键
    4. 差异分析：多重检验校正防止假阳性
    5. 批次校正：消除技术变异，保留生物学信号
    6. 功能分析：从基因列表到生物学意义
    7. 时间序列：理解动态变化过程
    8. 多组学整合：综合多层次信息
    9. 机器学习：从数据中学习模式
    
    关键提醒：
    • 始终进行数据质控
    • 注意统计学原理
    • 结果需要生物学解释
    • 可视化帮助理解数据
    """)


if __name__ == "__main__":
    main()