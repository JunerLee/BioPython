#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 06: Pandas入门 - 实验数据的电子表格

生物学问题：如何高效处理和分析基因表达实验的数据？

本章将学习：
1. 理解Pandas作为"数字化实验记录本"的概念
2. 处理真实的基因表达数据
3. 进行基础统计分析
4. 识别差异表达基因

生物学场景：
你刚完成了一个药物处理实验，测量了多个基因在处理前后的表达水平。
现在需要分析哪些基因受到了药物影响。
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


def demonstrate_pandas_basics():
    """
    演示pandas基本数据结构
    
    生物学类比：
    - Series像一个试管架，每个位置存储一个测量值
    - DataFrame像一个96孔板，行列交叉存储所有数据
    """
    print("[BIO] 第一步：理解Pandas的基本数据结构")
    print("=" * 50)
    
    # 场景：你测量了5个关键基因在4个样本中的表达
    print("\n实验背景：药物处理对关键基因表达的影响")
    print("- 5个基因：BRCA1(肿瘤抑制), TP53(细胞凋亡), GAPDH(管家基因), ACTB(管家基因), VEGFA(血管生成)")
    print("- 4个样本：2个对照组，2个药物处理组")
    
    # 创建基因列表（这些都是真实的重要基因）
    genes = ['BRCA1', 'TP53', 'GAPDH', 'ACTB', 'VEGFA']
    samples = ['Control_1', 'Control_2', 'Treated_1', 'Treated_2']
    
    # 模拟真实的表达数据（使用对数正态分布，因为基因表达通常呈偏态分布）
    np.random.seed(42)  # 确保结果可重现
    # 不同基因的基础表达水平不同
    base_expression = {
        'BRCA1': 5.5,    # 中等表达
        'TP53': 6.0,     # 中等表达
        'GAPDH': 8.0,    # 高表达（管家基因）
        'ACTB': 8.2,     # 高表达（管家基因）
        'VEGFA': 4.5     # 低表达
    }
    
    # 创建更真实的表达数据
    expression_data = []
    for gene in genes:
        gene_data = np.random.lognormal(mean=base_expression[gene], sigma=0.5, size=4)
        # 模拟药物效应：某些基因在处理组中表达变化
        if gene == 'TP53':  # TP53在处理后上调
            gene_data[2:] *= 1.8
        elif gene == 'VEGFA':  # VEGFA在处理后上调
            gene_data[2:] *= 2.2
        elif gene == 'BRCA1':  # BRCA1在处理后下调
            gene_data[2:] *= 0.6
        expression_data.append(gene_data)
    
    # 创建DataFrame - 这是Pandas的核心数据结构
    print("\n[DATA] 创建DataFrame（基因表达矩阵）:")
    df = pd.DataFrame(expression_data, index=genes, columns=samples)
    print(df.round(2))  # 保留2位小数便于阅读
    
    # 解释DataFrame的结构
    print(f"\n[CHART] 理解DataFrame结构:")
    print(f"  - 形状(shape): {df.shape} = ({df.shape[0]}个基因, {df.shape[1]}个样本)")
    print(f"  - 行索引(index): {list(df.index)} = 基因名")
    print(f"  - 列索引(columns): {list(df.columns)} = 样本名")
    print(f"  - 数据类型: 所有值都是浮点数（表达量）")
    
    # Series示例 - DataFrame的单行或单列
    print(f"\n[SEARCH] Series示例1：单个基因在所有样本中的表达（横向切片）")
    brca1_expression = df.loc['BRCA1']  # 使用loc按标签选择
    print(f"BRCA1基因的表达模式:")
    print(brca1_expression.round(2))
    print(f"  - 数据类型: {type(brca1_expression).__name__}")
    print(f"  - 平均表达: {brca1_expression.mean():.2f}")
    print(f"  - 变化程度(标准差): {brca1_expression.std():.2f}")
    
    # 单个样本的表达谱
    print(f"\n[SEARCH] Series示例2：单个样本中所有基因的表达（纵向切片）")
    control1_profile = df['Control_1']  # 直接用列名选择
    print(f"Control_1样本的表达谱:")
    print(control1_profile.round(2))
    print(f"  - 高表达基因(>1000): {list(control1_profile[control1_profile > 1000].index)}")
    print(f"  - 低表达基因(<100): {list(control1_profile[control1_profile < 100].index)}")
    
    return df


def load_gene_expression_data():
    """
    加载基因表达数据
    
    生物学背景：
    基因表达数据通常来自：
    1. RNA-seq: 高通量测序，可以检测所有基因
    2. Microarray: 芯片技术，检测预设的基因
    3. qRT-PCR: 定量PCR，精确测量少数基因
    """
    print("\n" + "=" * 50)
    print("[BIO] 第二步：加载真实的基因表达数据")
    print("=" * 50)
    
    # 构建数据文件路径
    data_file = os.path.join("..", "data", "gene_expression.csv")
    
    try:
        # 读取CSV文件 - 最常见的数据格式
        print("尝试读取CSV文件...")
        df = pd.read_csv(data_file)
        print("[OK] 数据加载成功!")
        
        # 显示数据概览
        print(f"\n[DATA] 数据概览:")
        print(f"  - 数据维度: {df.shape[0]}行 × {df.shape[1]}列")
        print(f"  - 内存占用: {df.memory_usage().sum() / 1024:.2f} KB")
        print(f"  - 列名: {list(df.columns)}")
        
        # 检查数据质量
        print(f"\n[SEARCH] 数据质量检查:")
        print(f"  - 缺失值总数: {df.isnull().sum().sum()}")
        print(f"  - 重复行数: {df.duplicated().sum()}")
        
        # 显示前几行数据
        print(f"\n[LIST] 数据预览（前5行）:")
        print(df.head())
        
        # 数据类型信息
        print(f"\n[NOTE] 列数据类型:")
        for col, dtype in df.dtypes.items():
            print(f"  - {col}: {dtype}")
        
        # 数值列的统计信息
        print(f"\n[DATA] 数值列统计摘要:")
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            stats = df[numeric_columns].describe()
            print(stats.round(2))
            
            # 解释统计量的生物学意义
            print("\n[BOOK] 统计量解释:")
            print("  - count: 非缺失值数量")
            print("  - mean: 平均表达水平")
            print("  - std: 表达变异程度")
            print("  - min/max: 表达范围")
            print("  - 25%/50%/75%: 四分位数，显示数据分布")
        
        return df
        
    except FileNotFoundError:
        print("[ERROR] 真实数据文件未找到，创建模拟数据用于学习...")
        return create_sample_data()


def create_sample_data():
    """
    创建示例基因表达数据
    
    模拟真实的RNA-seq数据特征：
    1. 管家基因（GAPDH, ACTB）高表达
    2. 肿瘤相关基因（BRCA2, TP53）中等表达
    3. 特定功能基因（VEGFA）低到中等表达
    4. 药物处理引起特定基因表达变化
    """
    print("\n创建模拟的基因表达数据集...")
    
    # 使用真实的Ensembl基因ID和基因名
    genes_data = {
        'gene_id': [
            'ENSG00000139618',  # BRCA2 - 乳腺癌易感基因
            'ENSG00000141510',  # TP53 - 肿瘤抑制基因，"基因组守护者"
            'ENSG00000111640',  # GAPDH - 糖酵解关键酶，管家基因
            'ENSG00000075624',  # ACTB - β-肌动蛋白，管家基因
            'ENSG00000112715',  # VEGFA - 血管内皮生长因子
            'ENSG00000171862',  # PTEN - 肿瘤抑制基因
            'ENSG00000133703',  # KRAS - 原癌基因
            'ENSG00000149311',  # ATM - DNA损伤修复
            'ENSG00000121879',  # PIK3CA - PI3K信号通路
            'ENSG00000105976'   # MET - 受体酪氨酸激酶
        ],
        'gene_name': ['BRCA2', 'TP53', 'GAPDH', 'ACTB', 'VEGFA', 
                     'PTEN', 'KRAS', 'ATM', 'PIK3CA', 'MET'],
        'gene_type': ['tumor_suppressor', 'tumor_suppressor', 'housekeeping', 
                     'housekeeping', 'growth_factor', 'tumor_suppressor',
                     'oncogene', 'dna_repair', 'oncogene', 'oncogene'],
        'chromosome': ['chr13', 'chr17', 'chr12', 'chr7', 'chr6',
                      'chr10', 'chr12', 'chr11', 'chr3', 'chr7']
    }
    
    # 生成更真实的表达数据
    np.random.seed(42)
    
    # 对照组表达数据
    control_1 = []
    control_2 = []
    # 处理组表达数据（模拟药物效应）
    treated_1 = []
    treated_2 = []
    
    for gene_name, gene_type in zip(genes_data['gene_name'], genes_data['gene_type']):
        # 根据基因类型设置基础表达水平
        if gene_type == 'housekeeping':
            base_level = np.random.uniform(1000, 2000)  # 管家基因高表达
        elif gene_type == 'tumor_suppressor':
            base_level = np.random.uniform(100, 300)    # 肿瘤抑制基因中等表达
        elif gene_type == 'oncogene':
            base_level = np.random.uniform(50, 200)     # 原癌基因变化较大
        else:
            base_level = np.random.uniform(50, 150)     # 其他基因
        
        # 添加生物学变异（技术重复间的变异通常较小）
        control_1.append(base_level * np.random.uniform(0.9, 1.1))
        control_2.append(base_level * np.random.uniform(0.9, 1.1))
        
        # 模拟药物处理效应
        if gene_name in ['TP53', 'PTEN', 'ATM']:  # 这些基因上调
            fold_change = np.random.uniform(1.5, 2.5)
        elif gene_name in ['VEGFA', 'MET']:  # 这些基因也上调
            fold_change = np.random.uniform(1.8, 2.2)
        elif gene_name in ['BRCA2', 'PIK3CA']:  # 这些基因下调
            fold_change = np.random.uniform(0.4, 0.7)
        else:  # 管家基因和其他基因变化较小
            fold_change = np.random.uniform(0.9, 1.1)
        
        treated_1.append(base_level * fold_change * np.random.uniform(0.9, 1.1))
        treated_2.append(base_level * fold_change * np.random.uniform(0.9, 1.1))
    
    # 添加表达数据到字典
    genes_data['sample_control_1'] = [round(x, 1) for x in control_1]
    genes_data['sample_control_2'] = [round(x, 1) for x in control_2]
    genes_data['sample_treated_1'] = [round(x, 1) for x in treated_1]
    genes_data['sample_treated_2'] = [round(x, 1) for x in treated_2]
    
    df = pd.DataFrame(genes_data)
    
    print("[OK] 模拟数据创建成功!")
    print(f"\n数据集特征:")
    print(f"  - 基因数: {len(df)}")
    print(f"  - 样本数: 4 (2个对照, 2个处理)")
    print(f"  - 基因类型: {df['gene_type'].value_counts().to_dict()}")
    
    return df


def analyze_gene_expression(df):
    """
    基因表达数据分析
    
    生物学目标：
    1. 评估数据质量（变异系数）
    2. 识别高表达和低表达基因
    3. 比较样本间的总体表达水平
    4. 为差异表达分析做准备
    """
    print("\n" + "=" * 50)
    print("[BIO] 第三步：基因表达数据的统计分析")
    print("=" * 50)
    
    # 提取表达数据列
    expression_columns = [col for col in df.columns if col.startswith('sample_')]
    expression_data = df[expression_columns]
    
    print("[DATA] 表达数据矩阵:")
    print(expression_data.round(1))
    
    # 计算每个基因的统计量
    print(f"\n[CHART] 基因水平的统计分析:")
    gene_stats = pd.DataFrame({
        'mean': expression_data.mean(axis=1),
        'std': expression_data.std(axis=1),
        'min': expression_data.min(axis=1),
        'max': expression_data.max(axis=1),
        'cv': expression_data.std(axis=1) / expression_data.mean(axis=1),  # 变异系数
        'range': expression_data.max(axis=1) - expression_data.min(axis=1)  # 表达范围
    })
    
    # 添加基因名称和类型
    if 'gene_name' in df.columns:
        gene_stats['gene_name'] = df['gene_name'].values
        if 'gene_type' in df.columns:
            gene_stats['gene_type'] = df['gene_type'].values
            gene_stats = gene_stats[['gene_name', 'gene_type', 'mean', 'std', 'cv', 'min', 'max', 'range']]
        else:
            gene_stats = gene_stats[['gene_name', 'mean', 'std', 'cv', 'min', 'max', 'range']]
    
    print(gene_stats.round(2))
    
    # 解释统计量的生物学意义
    print("\n[BOOK] 统计量的生物学解释:")
    print("  - Mean(均值): 基因的平均表达水平")
    print("  - CV(变异系数): <0.3表示稳定表达, >0.5表示高变异")
    print("  - Range(范围): 表达的动态范围，越大说明条件间差异越大")
    
    # 识别特殊基因
    print("\n[SEARCH] 特殊基因识别:")
    high_expr = gene_stats.nlargest(3, 'mean')['gene_name'] if 'gene_name' in gene_stats else gene_stats.nlargest(3, 'mean').index
    print(f"  - 高表达基因(Top 3): {list(high_expr)}")
    
    low_expr = gene_stats.nsmallest(3, 'mean')['gene_name'] if 'gene_name' in gene_stats else gene_stats.nsmallest(3, 'mean').index
    print(f"  - 低表达基因(Bottom 3): {list(low_expr)}")
    
    high_var = gene_stats.nlargest(3, 'cv')['gene_name'] if 'gene_name' in gene_stats else gene_stats.nlargest(3, 'cv').index
    print(f"  - 高变异基因(可能受处理影响): {list(high_var)}")
    
    # 计算每个样本的统计量
    print(f"\n[DATA] 样本水平的统计分析:")
    sample_stats = pd.DataFrame({
        'total_expression': expression_data.sum(axis=0),
        'mean_expression': expression_data.mean(axis=0),
        'median_expression': expression_data.median(axis=0),
        'std': expression_data.std(axis=0),
        'detected_genes': (expression_data > 10).sum(axis=0)  # 表达量>10的基因数
    })
    
    # 添加样本分组信息
    sample_stats['group'] = ['Control' if 'control' in col.lower() else 'Treated' 
                             for col in sample_stats.index]
    
    print(sample_stats.round(2))
    
    # 样本质量评估
    print("\n[OK] 样本质量评估:")
    print(f"  - 总表达量变异系数: {sample_stats['total_expression'].std() / sample_stats['total_expression'].mean():.3f}")
    if sample_stats['total_expression'].std() / sample_stats['total_expression'].mean() < 0.2:
        print("  - 样本间总表达量一致，数据质量良好")
    else:
        print("  - 样本间总表达量差异较大，需要标准化")
    
    return gene_stats, sample_stats


def demonstrate_data_selection(df):
    """
    演示数据选择和筛选
    
    生物学应用：
    - 提取感兴趣的基因子集
    - 选择特定实验条件的数据
    - 根据表达水平筛选基因
    - 识别差异表达基因
    """
    print("\n" + "=" * 50)
    print("[BIO] 第四步：数据选择和筛选技巧")
    print("=" * 50)
    
    # 方法1：选择特定列
    print("\n[1] 选择特定列（提取子数据集）:")
    if 'gene_name' in df.columns and 'sample_control_1' in df.columns:
        # 使用列表选择多列
        selected_data = df[['gene_name', 'sample_control_1']]
        print("选择基因名和第一个对照样本:")
        print(selected_data.head())
        print("\n[TIP] 技巧：使用df[['col1', 'col2']]选择多列")
    
    # 方法2：选择特定行
    print(f"\n[2] 选择特定行（基因子集）:")
    
    # 使用head/tail
    print("前3个基因:")
    first_three = df.head(3)
    print(first_three[['gene_name'] + [col for col in df.columns if col.startswith('sample_')]] 
          if 'gene_name' in df.columns else first_three)
    
    # 使用iloc（位置索引）
    print("\n使用iloc选择第2-4行:")
    subset = df.iloc[1:4]  # 注意：Python索引从0开始
    if 'gene_name' in df.columns:
        print(subset[['gene_name', 'sample_control_1', 'sample_treated_1']])
    
    print("\n[TIP] 技巧：iloc用于位置索引，loc用于标签索引")
    
    # 方法3：条件筛选（最重要的技能）
    print(f"\n[3] 条件筛选（识别感兴趣的基因）:")
    expression_columns = [col for col in df.columns if col.startswith('sample_')]
    if expression_columns:
        # 计算平均表达量
        df['mean_expression'] = df[expression_columns].mean(axis=1)
        
        # 定义表达水平阈值（基于生物学意义）
        high_threshold = df['mean_expression'].quantile(0.7)  # 前30%
        low_threshold = df['mean_expression'].quantile(0.3)   # 后30%
        
        # 筛选高表达基因
        high_expression = df[df['mean_expression'] > high_threshold]
        print(f"\n[CHART] 高表达基因 (表达量 > {high_threshold:.1f}):")
        if 'gene_name' in df.columns:
            print(high_expression[['gene_name', 'gene_type', 'mean_expression']].round(1) 
                  if 'gene_type' in df.columns 
                  else high_expression[['gene_name', 'mean_expression']].round(1))
        
        # 筛选低表达基因
        low_expression = df[df['mean_expression'] < low_threshold]
        print(f"\n📉 低表达基因 (表达量 < {low_threshold:.1f}):")
        if 'gene_name' in df.columns:
            print(low_expression[['gene_name', 'gene_type', 'mean_expression']].round(1) 
                  if 'gene_type' in df.columns 
                  else low_expression[['gene_name', 'mean_expression']].round(1))
        
        # 复合条件筛选
        print(f"\n[SEARCH] 复合条件筛选示例:")
        # 筛选：在对照组低表达但在处理组高表达的基因（潜在的药物靶标）
        control_cols = [col for col in expression_columns if 'control' in col.lower()]
        treated_cols = [col for col in expression_columns if 'treated' in col.lower()]
        
        if control_cols and treated_cols:
            df['control_mean'] = df[control_cols].mean(axis=1)
            df['treated_mean'] = df[treated_cols].mean(axis=1)
            
            upregulated = df[(df['control_mean'] < 150) & (df['treated_mean'] > 200)]
            if len(upregulated) > 0:
                print("药物处理后上调的基因:")
                if 'gene_name' in df.columns:
                    print(upregulated[['gene_name', 'control_mean', 'treated_mean']].round(1))
            else:
                print("未发现符合条件的基因")
        
        print("\n[TIP] 技巧：使用&(and), |(or), ~(not)组合多个条件")
    
    # 方法4：基于列表的筛选
    print(f"\n[4] 基于列表筛选（选择特定基因集）:")
    if 'gene_name' in df.columns:
        # 定义不同的基因集
        housekeeping_genes = ['GAPDH', 'ACTB']  # 管家基因
        tumor_genes = ['TP53', 'BRCA2', 'PTEN']  # 肿瘤相关基因
        
        # 筛选管家基因
        hk_data = df[df['gene_name'].isin(housekeeping_genes)]
        print(f"[HOME] 管家基因（用于标准化）:")
        print(hk_data[['gene_name'] + expression_columns].round(1))
        
        # 筛选肿瘤相关基因
        tumor_data = df[df['gene_name'].isin(tumor_genes)]
        if len(tumor_data) > 0:
            print(f"\n[TARGET] 肿瘤相关基因:")
            print(tumor_data[['gene_name'] + expression_columns].round(1))
        
        print("\n[TIP] 技巧：isin()方法用于检查值是否在列表中")
    
    # 方法5：使用query方法（更直观的语法）
    print(f"\n[5] 使用query方法（类SQL语法）:")
    if 'mean_expression' in df.columns:
        # query方法允许使用更自然的语法
        result = df.query('mean_expression > 100 and mean_expression < 500')
        print("中等表达基因（100 < 表达量 < 500）:")
        if 'gene_name' in result.columns:
            print(result[['gene_name', 'mean_expression']].round(1))
        
        print("\n[TIP] 技巧：query()方法让条件筛选更易读")


def demonstrate_data_transformation(df):
    """
    演示数据转换
    
    生物学意义：
    1. Log转换：处理基因表达的偏态分布
    2. 标准化：消除批次效应，使不同实验可比
    3. Fold Change：量化处理效应
    """
    print("\n" + "=" * 50)
    print("[BIO] 第五步：数据转换 - 为分析做准备")
    print("=" * 50)
    
    expression_columns = [col for col in df.columns if col.startswith('sample_')]
    
    if not expression_columns:
        print("[WARNING] 没有找到表达数据列")
        return
    
    # 展示原始数据
    print("\n[1] 原始表达数据:")
    original_data = df[expression_columns].head(5)
    print(original_data.round(1))
    
    # Log2转换 - 最常用的转换
    print(f"\n[2] Log2转换（处理偏态分布）:")
    print("\n为什么需要Log转换？")
    print("  - 基因表达数据通常呈偏态分布（少数基因极高表达）")
    print("  - Log转换使数据更接近正态分布")
    print("  - 便于识别倍数变化关系")
    
    log2_data = np.log2(df[expression_columns] + 1)  # +1是伪计数，避免log(0)
    print(f"\nLog2转换后的数据:")
    print(log2_data.head(5).round(2))
    
    # 比较转换前后的分布
    print(f"\n转换效果:")
    print(f"  原始数据范围: {df[expression_columns].min().min():.1f} - {df[expression_columns].max().max():.1f}")
    print(f"  Log2数据范围: {log2_data.min().min():.2f} - {log2_data.max().max():.2f}")
    
    # Z-score标准化
    print(f"\n[3] Z-score标准化（跨样本比较）:")
    print("\n为什么需要标准化？")
    print("  - 消除不同样本间的系统性差异（批次效应）")
    print("  - 使不同规模的数据可比")
    print("  - Z-score表示偏离平均值的标准差数")
    
    # 按行标准化（每个基因跨样本标准化）
    zscore_data = df[expression_columns].apply(lambda x: (x - x.mean()) / x.std(), axis=1)
    print(f"\n按基因标准化后的数据（每行均值=0，标准差=1）:")
    print(zscore_data.head(5).round(2))
    
    # 解释Z-score的含义
    print(f"\nZ-score解释:")
    print("  Z > 2: 显著高于平均水平")
    print("  -2 < Z < 2: 正常范围")
    print("  Z < -2: 显著低于平均水平")
    
    # Fold Change计算 - 差异表达分析的核心
    print(f"\n[4] Fold Change计算（量化处理效应）:")
    control_columns = [col for col in expression_columns if 'control' in col.lower()]
    treated_columns = [col for col in expression_columns if 'treated' in col.lower()]
    
    if control_columns and treated_columns:
        print("\n什么是Fold Change？")
        print("  - 衡量基因表达变化的倍数")
        print("  - FC = 处理组/对照组")
        print("  - Log2(FC) > 1: 上调2倍以上")
        print("  - Log2(FC) < -1: 下调2倍以上")
        
        # 计算各组平均值
        control_mean = df[control_columns].mean(axis=1)
        treated_mean = df[treated_columns].mean(axis=1)
        
        # 计算fold change
        fold_change = treated_mean / control_mean
        log2_fc = np.log2(fold_change)
        
        # 创建结果表
        fc_results = pd.DataFrame({
            'gene_name': df['gene_name'] if 'gene_name' in df.columns else df.index,
            'gene_type': df['gene_type'] if 'gene_type' in df.columns else 'unknown',
            'control_mean': control_mean,
            'treated_mean': treated_mean,
            'fold_change': fold_change,
            'log2_fc': log2_fc,
            'regulation': ['Up' if x > 1 else 'Down' if x < -1 else 'No change' for x in log2_fc]
        })
        
        # 按log2FC排序，显示变化最大的基因
        fc_results = fc_results.sort_values('log2_fc', ascending=False)
        
        print(f"\n[DATA] Fold Change分析结果:")
        print(fc_results.round(2))
        
        # 统计显著变化的基因
        print(f"\n[CHART] 差异表达统计:")
        upregulated = len(fc_results[fc_results['log2_fc'] > 1])
        downregulated = len(fc_results[fc_results['log2_fc'] < -1])
        unchanged = len(fc_results) - upregulated - downregulated
        
        print(f"  - 上调基因 (Log2FC > 1): {upregulated}个")
        print(f"  - 下调基因 (Log2FC < -1): {downregulated}个")
        print(f"  - 无显著变化: {unchanged}个")
        
        # 识别最显著的变化
        if len(fc_results) > 0:
            top_up = fc_results.iloc[0]
            top_down = fc_results.iloc[-1]
            print(f"\n[TARGET] 最显著的变化:")
            print(f"  - 最强上调: {top_up['gene_name']} (Log2FC = {top_up['log2_fc']:.2f})")
            print(f"  - 最强下调: {top_down['gene_name']} (Log2FC = {top_down['log2_fc']:.2f})")
    
    # 数据转换的实际应用提示
    print("\n[TIP] 数据转换选择指南:")
    print("  - 原始数据：用于计算绝对表达量")
    print("  - Log转换：用于可视化和统计检验")
    print("  - Z-score：用于聚类分析和热图")
    print("  - Fold Change：用于识别差异表达基因")


def create_basic_visualization(df):
    """
    创建基础可视化
    
    可视化的生物学意义：
    1. 分布图：检查数据质量
    2. 相关性热图：评估样本相似性
    3. 箱线图：比较不同条件
    4. 散点图：识别差异表达
    """
    print("\n" + "=" * 50)
    print("[BIO] 第六步：数据可视化 - 让数据说话")
    print("=" * 50)
    
    expression_columns = [col for col in df.columns if col.startswith('sample_')]
    
    if len(expression_columns) < 2:
        print("[WARNING] 表达数据列不足，跳过可视化")
        return
    
    # 设置图形样式和中文支持
    plt.style.use('default')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
    plt.rcParams['axes.unicode_minus'] = False    # 负号显示
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('基因表达数据分析可视化', fontsize=16, fontweight='bold')
    
    # 1. 表达量分布直方图
    all_values = df[expression_columns].values.flatten()
    axes[0, 0].hist(all_values, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].axvline(np.median(all_values), color='red', linestyle='--', label=f'中位数: {np.median(all_values):.1f}')
    axes[0, 0].axvline(np.mean(all_values), color='green', linestyle='--', label=f'均值: {np.mean(all_values):.1f}')
    axes[0, 0].set_title('表达量分布（检查数据质量）')
    axes[0, 0].set_xlabel('表达量')
    axes[0, 0].set_ylabel('频率')
    axes[0, 0].legend()
    axes[0, 0].set_xlim(0, np.percentile(all_values, 99))  # 去除极端值便于观察
    
    # 2. 样本间相关性热图
    if len(expression_columns) > 1:
        # 计算样本间的相关性（转置使样本成为行）
        corr_matrix = df[expression_columns].corr()
        im = axes[0, 1].imshow(corr_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
        axes[0, 1].set_title('样本间相关性（检查重复性）')
        axes[0, 1].set_xticks(range(len(expression_columns)))
        axes[0, 1].set_yticks(range(len(expression_columns)))
        axes[0, 1].set_xticklabels([col.replace('sample_', '') for col in expression_columns], rotation=45)
        axes[0, 1].set_yticklabels([col.replace('sample_', '') for col in expression_columns])
        
        # 添加相关系数文本
        for i in range(len(expression_columns)):
            for j in range(len(expression_columns)):
                text = axes[0, 1].text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                                      ha="center", va="center", color="black", fontsize=8)
        
        plt.colorbar(im, ax=axes[0, 1], label='相关系数')
    
    # 3. 样本表达量箱线图
    # 准备数据用于箱线图
    box_data = [df[col].values for col in expression_columns]
    box_labels = [col.replace('sample_', '') for col in expression_columns]
    
    # 设置颜色：对照组蓝色，处理组红色
    colors = ['lightblue' if 'control' in label.lower() else 'lightcoral' for label in box_labels]
    
    bp = axes[1, 0].boxplot(box_data, labels=box_labels, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    axes[1, 0].set_title('样本间表达分布（比较条件）')
    axes[1, 0].set_ylabel('表达量')
    axes[1, 0].set_xlabel('样本')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='lightblue', label='对照组'),
                      Patch(facecolor='lightcoral', label='处理组')]
    axes[1, 0].legend(handles=legend_elements, loc='upper right')
    
    # 4. MA图或散点图 (如果有对照和处理组)
    control_cols = [col for col in expression_columns if 'control' in col.lower()]
    treated_cols = [col for col in expression_columns if 'treated' in col.lower()]
    
    if control_cols and treated_cols:
        control_mean = df[control_cols].mean(axis=1)
        treated_mean = df[treated_cols].mean(axis=1)
        
        # 计算log2 fold change用于着色
        log2_fc = np.log2((treated_mean + 1) / (control_mean + 1))
        
        # 根据fold change着色
        colors = ['red' if fc > 1 else 'blue' if fc < -1 else 'gray' for fc in log2_fc]
        
        scatter = axes[1, 1].scatter(control_mean, treated_mean, alpha=0.6, c=colors, s=50)
        
        # 添加对角线（无变化线）
        max_val = max(control_mean.max(), treated_mean.max())
        axes[1, 1].plot([0, max_val], [0, max_val], 'k--', alpha=0.3, label='无变化')
        
        # 添加2倍变化线
        axes[1, 1].plot([0, max_val], [0, max_val*2], 'r--', alpha=0.3, label='2倍上调')
        axes[1, 1].plot([0, max_val], [0, max_val/2], 'b--', alpha=0.3, label='2倍下调')
        
        axes[1, 1].set_title('差异表达分析（对照 vs 处理）')
        axes[1, 1].set_xlabel('对照组平均表达量')
        axes[1, 1].set_ylabel('处理组平均表达量')
        axes[1, 1].legend(loc='upper left')
        axes[1, 1].set_xlim(0, max_val * 1.1)
        axes[1, 1].set_ylim(0, max_val * 1.1)
        
        # 标注显著变化的基因
        if 'gene_name' in df.columns:
            for i, gene in enumerate(df['gene_name']):
                if abs(log2_fc.iloc[i]) > 1.5:  # 标注变化大于1.5倍的基因
                    axes[1, 1].annotate(gene, (control_mean.iloc[i], treated_mean.iloc[i]),
                                       fontsize=8, alpha=0.7)
    
    plt.tight_layout()
    
    # 保存图片
    output_file = 'gene_expression_analysis.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n[OK] 可视化图表已保存为 '{output_file}'")
    
    # 解释每个图的意义
    print("\n[DATA] 图表解读:")
    print("  1. 分布图: 检查是否有异常值或批次效应")
    print("  2. 相关性热图: 技术重复应高度相关(>0.9)")
    print("  3. 箱线图: 比较不同条件的整体表达水平")
    print("  4. 散点图: 红点和蓝点代表差异表达基因")
    
    plt.show()


def main():
    """
    主函数 - 完整的基因表达数据分析流程
    
    这个分析流程模拟了真实的转录组数据分析：
    1. 数据加载和质量检查
    2. 探索性数据分析
    3. 差异表达分析
    4. 结果可视化
    """
    print("="*60)
    print("Chapter 06: Pandas入门 - 实验数据的电子表格")
    print("="*60)
    print("\n生物学问题：药物X对癌症相关基因表达有什么影响？")
    print("\n我们将通过Pandas分析一个模拟的基因表达实验数据，")
    print("学习如何用代码代替Excel处理生物数据。\n")
    
    # 第一步：理解基础概念
    print("\n" + "="*60)
    print("[BOOK] 学习路径：从简单到复杂的渐进式学习")
    print("="*60)
    
    demo_df = demonstrate_pandas_basics()
    
    print("\n继续加载真实数据...")
    
    # 第二步：加载实际数据
    df = load_gene_expression_data()
    
    print("\n继续进行数据分析...")
    
    # 第三步：统计分析
    gene_stats, sample_stats = analyze_gene_expression(df)
    
    print("\n继续学习数据筛选...")
    
    # 第四步：数据选择和筛选
    demonstrate_data_selection(df)
    
    print("\n继续学习数据转换...")
    
    # 第五步：数据转换
    demonstrate_data_transformation(df)
    
    print("\n生成可视化图表...")
    
    # 第六步：可视化
    try:
        create_basic_visualization(df)
    except Exception as e:
        print(f"[WARNING] 可视化创建失败: {e}")
        print("提示：可能需要安装matplotlib: pip install matplotlib")
    
    # 总结
    print("\n" + "=" * 60)
    print("[BOOK] 本章核心要点总结")
    print("=" * 60)
    
    print("\n[OK] 你已经掌握的技能:")
    print("\n1. **Pandas基础概念**")
    print("   - Series = 单个实验的测量值（一维数据）")
    print("   - DataFrame = 完整的实验数据表（二维数据）")
    print("   - Index = 数据的标签（基因名、样本名）")
    
    print("\n2. **数据操作技能**")
    print("   - 读取数据：pd.read_csv()")
    print("   - 查看数据：head(), info(), describe()")
    print("   - 选择数据：loc[], iloc[], 条件筛选")
    print("   - 转换数据：log转换, 标准化, fold change")
    
    print("\n3. **生物学应用**")
    print("   - 质量控制：检查数据分布和异常值")
    print("   - 差异分析：计算fold change识别变化基因")
    print("   - 数据标准化：消除批次效应")
    print("   - 结果可视化：理解数据模式")
    
    print("\n[TARGET] 实际应用场景:")
    print("   • RNA-seq数据分析")
    print("   • 蛋白质组学数据处理")
    print("   • ChIP-seq峰值分析")
    print("   • 临床数据统计")
    print("   • 多组学数据整合")
    
    print("\n[TIP] 关键要记住:")
    print("   Pandas不是要取代Excel，而是要超越Excel的限制。")
    print("   当你的数据超过几千行，或需要自动化分析时，")
    print("   Pandas就是你的最佳选择！")
    
    print("\n[GO] 下一章预告:")
    print("   Chapter 07: Pandas进阶 - 更强大的数据分析技巧")
    print("   • 数据分组和聚合（groupby）")
    print("   • 数据重塑（pivot, melt）")
    print("   • 多表连接（merge, join）")
    print("   • 时间序列分析")
    print("   • 大数据处理技巧")
    
    print("\n" + "=" * 60)
    print("[SUCCESS] 恭喜完成第6章！你已经掌握了Pandas的基础知识！")
    print("=" * 60)


if __name__ == "__main__":
    main()