#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 07: Pandas高级数据分析 - 练习题

通过实际练习掌握转录组数据的完整分析流程。
练习按难度分级：
- 基础练习（★）：数据操作基本功
- 进阶练习（★★）：实际分析场景
- 挑战练习（★★★）：综合应用
"""

import pandas as pd
import numpy as np
from scipy import stats


def practice_1_data_integration():
    """
    练习1（★）：数据整合
    
    任务：合并来自三个不同批次的基因表达数据
    要求：
    1. 读取并合并多个数据文件
    2. 处理缺失值
    3. 标准化数据格式
    """
    print("练习1（★）：数据整合 - 合并多批次实验数据")
    print("-" * 50)
    
    # TODO: 创建三个批次的模拟数据
    # 提示：每个批次可能有不同的基因列表
    
    # TODO: 使用pd.merge或pd.concat合并数据
    
    # TODO: 处理缺失值（某些基因可能只在部分批次中检测到）
    
    # TODO: 输出合并后的数据概况
    
    pass


def practice_2_quality_control():
    """
    练习2（★）：质量控制
    
    任务：识别和过滤低质量样本
    要求：
    1. 计算每个样本的总reads数
    2. 识别异常样本（离群值）
    3. 过滤低表达基因
    """
    print("\n练习2（★）：质量控制 - 识别低质量数据")
    print("-" * 50)
    
    # TODO: 创建包含质量问题的模拟数据
    
    # TODO: 计算质量指标（总reads、检测到的基因数等）
    
    # TODO: 使用统计方法识别离群样本
    
    # TODO: 过滤低表达基因（如平均表达量<10）
    
    pass


def practice_3_basic_statistics():
    """
    练习3（★）：基本统计
    
    任务：计算基因表达的描述性统计
    要求：
    1. 计算每个基因的均值、中位数、标准差
    2. 计算变异系数（CV）
    3. 识别高变异基因
    """
    print("\n练习3（★）：基本统计 - 描述性分析")
    print("-" * 50)
    
    # TODO: 创建基因表达数据
    
    # TODO: 计算描述性统计量
    
    # TODO: 计算并解释变异系数
    
    # TODO: 找出最稳定和最不稳定的基因
    
    pass


def practice_4_differential_analysis():
    """
    练习4（★★）：差异表达分析
    
    任务：执行完整的差异表达分析流程
    要求：
    1. 比较两组样本（如疾病vs健康）
    2. 执行统计检验
    3. 进行多重检验校正
    4. 筛选显著差异基因
    """
    print("\n练习4（★★）：差异表达分析 - 疾病vs健康")
    print("-" * 50)
    
    # TODO: 创建疾病组和健康组的表达数据
    
    # TODO: 计算fold change和log2 fold change
    
    # TODO: 执行t检验或Wilcoxon检验
    
    # TODO: FDR校正
    
    # TODO: 根据p值和fold change筛选差异基因
    
    pass


def practice_5_batch_correction():
    """
    练习5（★★）：批次效应校正
    
    任务：识别并校正批次效应
    要求：
    1. 检测批次效应的存在
    2. 使用合适的方法校正
    3. 验证校正效果
    """
    print("\n练习5（★★）：批次效应校正")
    print("-" * 50)
    
    # TODO: 创建包含批次效应的数据
    # 提示：同一基因在不同批次中系统性偏移
    
    # TODO: 可视化批次效应（如PCA）
    
    # TODO: 实施批次效应校正
    # 提示：可以使用ComBat方法或简单的z-score标准化
    
    # TODO: 验证校正效果
    
    pass


def practice_6_functional_grouping():
    """
    练习6（★★）：功能分组分析
    
    任务：按基因功能或染色体位置分组分析
    要求：
    1. 将基因分配到功能类别
    2. 比较不同功能组的表达模式
    3. 识别富集的功能类别
    """
    print("\n练习6（★★）：功能分组分析")
    print("-" * 50)
    
    # TODO: 创建基因功能注释数据
    
    # TODO: 按功能分组计算平均表达
    
    # TODO: 比较不同功能组的表达差异
    
    # TODO: 执行简单的富集分析
    
    pass


def practice_7_time_series():
    """
    练习7（★★★）：时间序列分析
    
    任务：分析药物处理后的时间响应
    要求：
    1. 分析多个时间点的表达数据
    2. 识别不同的响应模式
    3. 聚类相似表达模式的基因
    4. 找出早期和晚期响应基因
    """
    print("\n练习7（★★★）：时间序列分析 - 药物响应")
    print("-" * 50)
    
    # TODO: 创建时间序列数据（0, 1, 2, 4, 8, 24小时）
    
    # TODO: 计算每个基因的表达变化趋势
    
    # TODO: 识别不同的表达模式（上升、下降、瞬时、振荡）
    
    # TODO: 使用相关性或聚类方法分组基因
    
    # TODO: 识别关键时间点和转折点
    
    pass


def practice_8_multi_omics_integration():
    """
    练习8（★★★）：多组学数据整合
    
    任务：整合转录组和蛋白组数据
    要求：
    1. 合并不同类型的组学数据
    2. 处理不同数据的标准化
    3. 分析mRNA-蛋白质相关性
    4. 识别转录后调控的基因
    """
    print("\n练习8（★★★）：多组学整合 - 转录组+蛋白组")
    print("-" * 50)
    
    # TODO: 创建转录组数据
    
    # TODO: 创建对应的蛋白组数据
    # 提示：蛋白质水平可能与mRNA不完全一致
    
    # TODO: 数据标准化和整合
    
    # TODO: 计算mRNA-蛋白质相关性
    
    # TODO: 识别转录后调控（mRNA高但蛋白低，或相反）
    
    pass


def practice_9_machine_learning():
    """
    练习9（★★★）：机器学习应用
    
    任务：基于表达谱进行样本分类
    要求：
    1. 特征选择（选择信息量大的基因）
    2. 数据预处理和标准化
    3. 构建分类模型
    4. 评估模型性能
    """
    print("\n练习9（★★★）：机器学习 - 样本分类")
    print("-" * 50)
    
    # TODO: 创建带标签的表达数据（如癌症类型）
    
    # TODO: 特征选择（选择高变异或差异表达基因）
    
    # TODO: 数据标准化
    
    # TODO: 划分训练集和测试集
    
    # TODO: 构建简单的分类器（如基于距离的分类）
    
    # TODO: 评估分类准确率
    
    pass


def bonus_challenge():
    """
    额外挑战：完整的RNA-seq分析管道
    
    任务：实现一个完整的分析流程
    从原始计数矩阵到最终的生物学解释
    """
    print("\n🏆 额外挑战：完整RNA-seq分析管道")
    print("-" * 50)
    
    # TODO: 实现完整的分析流程
    # 1. 数据加载和质控
    # 2. 标准化（如TPM或FPKM）
    # 3. 批次效应校正
    # 4. 差异表达分析
    # 5. 功能富集分析
    # 6. 结果可视化准备
    
    pass


def main():
    """
    主函数 - 运行所有练习
    """
    print("=" * 60)
    print("Chapter 07: Pandas高级数据分析 - 练习题")
    print("=" * 60)
    print()
    
    # 基础练习（★）
    print("【基础练习】")
    practice_1_data_integration()
    practice_2_quality_control()
    practice_3_basic_statistics()
    
    # 进阶练习（★★）
    print("\n【进阶练习】")
    practice_4_differential_analysis()
    practice_5_batch_correction()
    practice_6_functional_grouping()
    
    # 挑战练习（★★★）
    print("\n【挑战练习】")
    practice_7_time_series()
    practice_8_multi_omics_integration()
    practice_9_machine_learning()
    
    # 额外挑战
    print("\n【额外挑战】")
    bonus_challenge()
    
    print("\n" + "=" * 60)
    print("练习提示：")
    print("1. 先完成基础练习，掌握基本操作")
    print("2. 进阶练习模拟真实分析场景")
    print("3. 挑战练习需要综合运用多个概念")
    print("4. 参考答案在practice_solution.py中")
    print("=" * 60)


if __name__ == "__main__":
    main()