#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 06: Pandas入门 - 练习题

通过这些练习，你将学会：
1. 理解Series和DataFrame的基本概念
2. 创建和操作实验数据表格
3. 进行基础的数据筛选和统计
4. 分析真实的生物学实验数据

练习难度：
⭐ 初级 - Series基础操作
⭐⭐ 中级 - DataFrame数据处理
⭐⭐⭐ 高级 - 实际生物学应用

生物学背景：
这些练习基于真实的分子生物学实验场景，包括：
- 基因表达分析
- 酶活性测定
- PCR结果统计
- 蛋白质组学数据处理
"""

import pandas as pd
import numpy as np


def practice_1_series_basics():
    """
    练习1: Series基础操作 ⭐
    
    生物学场景：你测定了5种酶的活性，需要进行统计分析
    
    任务：
    1. 创建包含酶活性数据的Series
    2. 进行基本统计计算
    3. 数据筛选和排序
    """
    print("=" * 60)
    print("练习1: 酶活性数据分析 ⭐")
    print("-" * 60)
    print("生物学背景：测定了5种消化酶的活性（单位：U/mg蛋白）")
    
    # TODO: 创建Series存储酶活性数据
    # 酶名称和活性数据如下：
    # Amylase(淀粉酶): 125.3
    # Protease(蛋白酶): 89.7  
    # Lipase(脂肪酶): 45.2
    # Cellulase(纤维素酶): 67.8
    # Invertase(转化酶): 156.9
    
    # enzyme_activity = pd.Series({
    #     'Amylase': 125.3,
    #     'Protease': 89.7,
    #     'Lipase': 45.2,
    #     'Cellulase': 67.8,
    #     'Invertase': 156.9
    # })
    
    print("任务1: 显示酶活性数据")
    # print("酶活性测定结果:")
    # print(enzyme_activity)
    
    print("\n任务2: 计算基本统计量")
    # print(f"平均酶活性: {enzyme_activity.mean():.2f} U/mg")
    # print(f"最高活性: {enzyme_activity.max():.2f} U/mg ({enzyme_activity.idxmax()})")
    # print(f"最低活性: {enzyme_activity.min():.2f} U/mg ({enzyme_activity.idxmin()})")
    # print(f"标准差: {enzyme_activity.std():.2f}")
    
    print("\n任务3: 数据筛选")
    # high_activity = enzyme_activity[enzyme_activity > 100]
    # print(f"高活性酶(>100 U/mg): {list(high_activity.index)}")
    # print(high_activity)
    
    print("\n任务4: 数据排序")
    # sorted_enzymes = enzyme_activity.sort_values(ascending=False)
    # print("按活性从高到低排序:")
    # print(sorted_enzymes)
    
    # 提示：去掉注释符号完成练习


def practice_2_dataframe_creation():
    """
    练习2: DataFrame创建和基本操作 ⭐⭐
    
    生物学场景：PCR实验结果需要整理成表格形式
    
    任务：
    1. 创建PCR结果的DataFrame
    2. 查看数据基本信息
    3. 选择特定行列数据
    """
    print("\n" + "=" * 60)
    print("练习2: PCR实验结果整理 ⭐⭐")
    print("-" * 60)
    print("生物学背景：对4个样本进行了3个基因的PCR检测")
    
    # TODO: 创建PCR结果DataFrame
    # 样本: Sample1, Sample2, Sample3, Sample4
    # 基因: GAPDH, ACTB, RPL13A (都是常用的管家基因)
    # Ct值数据（Ct值越小表示表达量越高）:
    # GAPDH: [18.5, 19.2, 18.8, 19.0]
    # ACTB:  [19.8, 20.1, 19.5, 20.3]
    # RPL13A: [20.2, 19.9, 20.5, 20.0]
    
    # # 方法1：从字典创建
    # pcr_data = {
    #     'Sample1': [18.5, 19.8, 20.2],
    #     'Sample2': [19.2, 20.1, 19.9],
    #     'Sample3': [18.8, 19.5, 20.5], 
    #     'Sample4': [19.0, 20.3, 20.0]
    # }
    # df_pcr = pd.DataFrame(pcr_data, index=['GAPDH', 'ACTB', 'RPL13A'])
    
    print("任务1: 显示完整的PCR结果表")
    # print("PCR Ct值结果:")
    # print(df_pcr)
    
    print("\n任务2: 查看DataFrame基本信息")
    # print(f"数据形状: {df_pcr.shape}")
    # print(f"行索引(基因): {list(df_pcr.index)}")
    # print(f"列索引(样本): {list(df_pcr.columns)}")
    # print(f"数据类型:\n{df_pcr.dtypes}")
    
    print("\n任务3: 数据选择操作")
    # print("GAPDH基因在所有样本中的Ct值:")
    # print(df_pcr.loc['GAPDH'])
    # 
    # print("\nSample1的所有基因Ct值:")
    # print(df_pcr['Sample1'])
    # 
    # print("\n选择特定基因和样本的交叉数据:")
    # print(f"Sample1中GAPDH的Ct值: {df_pcr.loc['GAPDH', 'Sample1']}")
    
    print("\n任务4: 基本统计")
    # print("每个基因的平均Ct值:")
    # print(df_pcr.mean(axis=1).round(2))  # axis=1表示按行计算
    # 
    # print("每个样本的平均Ct值:")
    # print(df_pcr.mean(axis=0).round(2))  # axis=0表示按列计算


def practice_3_gene_expression_analysis():
    """
    练习3: 基因表达数据分析 ⭐⭐⭐
    
    生物学场景：药物处理实验，分析哪些基因发生了显著变化
    
    任务：
    1. 创建基因表达数据
    2. 计算fold change
    3. 识别差异表达基因
    4. 生成分析报告
    """
    print("\n" + "=" * 60)
    print("练习3: 差异表达基因识别 ⭐⭐⭐")
    print("-" * 60)
    print("生物学背景：比较药物处理前后8个关键基因的表达变化")
    
    # TODO: 创建基因表达数据
    # 基因列表（这些都是重要的癌症相关基因）:
    # BRCA1, TP53, MYC, EGFR, VEGFA, CDKN1A, BCL2, PTEN
    
    # 表达数据 (FPKM值):
    # Control组平均值: [120, 89, 156, 78, 45, 234, 167, 98]
    # Treated组平均值: [78, 234, 145, 189, 123, 456, 89, 78]
    
    # genes = ['BRCA1', 'TP53', 'MYC', 'EGFR', 'VEGFA', 'CDKN1A', 'BCL2', 'PTEN']
    # control_expression = [120, 89, 156, 78, 45, 234, 167, 98]
    # treated_expression = [78, 234, 145, 189, 123, 456, 89, 78]
    # 
    # # 创建DataFrame
    # expression_df = pd.DataFrame({
    #     'Control': control_expression,
    #     'Treated': treated_expression
    # }, index=genes)
    
    print("任务1: 显示基因表达数据")
    # print("基因表达水平 (FPKM):")
    # print(expression_df)
    
    print("\n任务2: 计算Fold Change")
    # expression_df['Fold_Change'] = expression_df['Treated'] / expression_df['Control']
    # expression_df['Log2_FC'] = np.log2(expression_df['Fold_Change'])
    # print("添加fold change计算:")
    # print(expression_df.round(3))
    
    print("\n任务3: 识别差异表达基因")
    # # 通常认为|Log2FC| > 1 (即FC > 2或 < 0.5)为显著差异
    # upregulated = expression_df[expression_df['Log2_FC'] > 1]
    # downregulated = expression_df[expression_df['Log2_FC'] < -1]
    # 
    # print(f"上调基因 (FC > 2): {len(upregulated)} 个")
    # if len(upregulated) > 0:
    #     print(upregulated[['Fold_Change', 'Log2_FC']].round(3))
    # 
    # print(f"\n下调基因 (FC < 0.5): {len(downregulated)} 个")
    # if len(downregulated) > 0:
    #     print(downregulated[['Fold_Change', 'Log2_FC']].round(3))
    
    print("\n任务4: 生成分析报告")
    # stable_genes = expression_df[(expression_df['Log2_FC'] >= -1) & (expression_df['Log2_FC'] <= 1)]
    # print(f"稳定表达基因 (-1 <= Log2FC <= 1): {len(stable_genes)} 个")
    # print(list(stable_genes.index))
    # 
    # print(f"\n变化最大的基因: {expression_df['Log2_FC'].abs().idxmax()}")
    # max_change_gene = expression_df['Log2_FC'].abs().idxmax()
    # print(f"  Log2FC = {expression_df.loc[max_change_gene, 'Log2_FC']:.3f}")
    # print(f"  生物学意义: {'上调' if expression_df.loc[max_change_gene, 'Log2_FC'] > 0 else '下调'}")


def practice_4_data_filtering():
    """
    练习4: 数据筛选和条件查询 ⭐⭐
    
    生物学场景：蛋白质组学实验数据筛选
    
    任务：
    1. 根据多个条件筛选蛋白质
    2. 分组统计
    3. 数据排序
    """
    print("\n" + "=" * 60)
    print("练习4: 蛋白质组学数据筛选 ⭐⭐")
    print("-" * 60)
    print("生物学背景：分析蛋白质组学实验中检测到的蛋白质")
    
    # 创建模拟的蛋白质数据
    np.random.seed(42)
    proteins = [f"Protein_{i:03d}" for i in range(1, 21)]
    
    protein_data = pd.DataFrame({
        'Protein_ID': proteins,
        'Molecular_Weight': np.random.uniform(10, 200, 20).round(1),  # kDa
        'Expression_Level': np.random.uniform(0.1, 100, 20).round(2),  # FPKM
        'Peptides_Detected': np.random.randint(1, 15, 20),  # 检测到的肽段数
        'Cellular_Location': np.random.choice(['Nucleus', 'Cytoplasm', 'Membrane', 'Mitochondria'], 20)
    })
    
    print("蛋白质组学数据（前10个）:")
    print(protein_data.head(10))
    
    print("\n任务1: 高可信度蛋白质筛选")
    print("筛选条件：检测肽段数≥5 且 表达水平≥10 FPKM")
    # TODO: 完成筛选条件
    # high_confidence = protein_data[(protein_data['Peptides_Detected'] >= 5) & 
    #                                (protein_data['Expression_Level'] >= 10)]
    # print(f"高可信度蛋白质: {len(high_confidence)} 个")
    # print(high_confidence[['Protein_ID', 'Expression_Level', 'Peptides_Detected']])
    
    print("\n任务2: 按细胞定位分组统计")
    # location_stats = protein_data.groupby('Cellular_Location').agg({
    #     'Expression_Level': ['count', 'mean', 'std'],
    #     'Molecular_Weight': 'mean'
    # }).round(2)
    # print("各细胞区域的蛋白质统计:")
    # print(location_stats)
    
    print("\n任务3: 寻找大分子量高表达蛋白")
    print("条件：分子量>100 kDa 且 表达水平>50 FPKM")
    # large_abundant = protein_data[(protein_data['Molecular_Weight'] > 100) & 
    #                               (protein_data['Expression_Level'] > 50)]
    # print(f"符合条件的蛋白质: {len(large_abundant)} 个")
    # if len(large_abundant) > 0:
    #     print(large_abundant[['Protein_ID', 'Molecular_Weight', 'Expression_Level']])


def practice_5_missing_data():
    """
    练习5: 缺失数据处理 ⭐⭐
    
    生物学场景：实验数据中的缺失值处理
    
    任务：
    1. 检测缺失值
    2. 处理缺失值
    3. 数据完整性分析
    """
    print("\n" + "=" * 60)
    print("练习5: 实验数据缺失值处理 ⭐⭐")
    print("-" * 60)
    print("生物学背景：qPCR实验中某些样本检测失败，产生缺失值")
    
    # 创建包含缺失值的数据
    qpcr_data = pd.DataFrame({
        'Sample_A': [2.3, 4.5, np.nan, 3.8, 2.1],
        'Sample_B': [3.2, np.nan, 5.1, 4.2, np.nan],
        'Sample_C': [1.9, 3.4, 4.8, np.nan, 2.8],
        'Sample_D': [2.8, 4.1, 5.3, 4.6, 3.2]
    }, index=['Gene_1', 'Gene_2', 'Gene_3', 'Gene_4', 'Gene_5'])
    
    print("qPCR相对表达量数据（包含缺失值）:")
    print(qpcr_data)
    
    print("\n任务1: 检测缺失值")
    # print("缺失值统计:")
    # print(f"总缺失值数量: {qpcr_data.isnull().sum().sum()}")
    # print("每个样本的缺失值:")
    # print(qpcr_data.isnull().sum())
    # print("每个基因的缺失值:")
    # print(qpcr_data.isnull().sum(axis=1))
    
    print("\n任务2: 不同的缺失值处理方法")
    
    print("方法1: 删除包含缺失值的行")
    # clean_data_dropna = qpcr_data.dropna()
    # print(f"删除后剩余: {len(clean_data_dropna)} 个基因")
    # print(clean_data_dropna)
    
    print("\n方法2: 用均值填补缺失值")
    # filled_mean = qpcr_data.fillna(qpcr_data.mean())
    # print("用均值填补后:")
    # print(filled_mean.round(2))
    
    print("\n方法3: 用中位数填补缺失值")
    # filled_median = qpcr_data.fillna(qpcr_data.median())
    # print("用中位数填补后:")
    # print(filled_median.round(2))
    
    print("\n任务3: 评估数据完整性")
    # completeness = (1 - qpcr_data.isnull().sum() / len(qpcr_data)) * 100
    # print("各样本数据完整性:")
    # for sample, percent in completeness.items():
    #     print(f"  {sample}: {percent:.1f}%")


def main():
    """
    运行所有练习
    """
    print("🧬 Chapter 06: Pandas入门 - 练习题")
    print("学习使用Pandas分析生物学实验数据")
    print("=" * 60)
    
    print("\n📋 练习列表:")
    print("1. Series基础操作 - 酶活性数据分析 ⭐")
    print("2. DataFrame创建 - PCR结果整理 ⭐⭐") 
    print("3. 基因表达分析 - 差异表达基因识别 ⭐⭐⭐")
    print("4. 数据筛选 - 蛋白质组学数据处理 ⭐⭐")
    print("5. 缺失数据处理 - qPCR数据清洗 ⭐⭐")
    
    print("\n💡 学习提示:")
    print("• 每个练习都有详细的TODO注释")
    print("• 去掉注释符号运行代码")
    print("• 尝试修改参数观察结果变化")
    print("• 完成后查看practice_solution.py对比答案")
    
    # 运行所有练习
    practice_1_series_basics()
    practice_2_dataframe_creation()
    practice_3_gene_expression_analysis()
    practice_4_data_filtering()
    practice_5_missing_data()
    
    print("\n" + "=" * 60)
    print("🎉 练习完成!")
    print("通过这些练习，你已经掌握了:")
    print("✅ Pandas基本数据结构（Series和DataFrame）")
    print("✅ 数据创建、选择和筛选")
    print("✅ 基础统计分析")
    print("✅ 缺失值处理")
    print("✅ 生物学数据的实际应用")
    
    print("\n🚀 下一步:")
    print("完成这些基础练习后，可以学习Chapter 07的高级Pandas操作：")
    print("• 数据合并和连接")
    print("• 复杂的分组统计")
    print("• 时间序列分析")
    print("• 数据透视表")


if __name__ == "__main__":
    main()