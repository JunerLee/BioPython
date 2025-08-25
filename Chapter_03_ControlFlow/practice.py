#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 03 练习：控制流应用

通过实际的生物信息学问题，练习控制流的使用。
练习难度逐步提升，每题都有详细提示。

⭐ 初级：基础语法练习
⭐⭐ 中级：组合使用控制流
⭐⭐⭐ 高级：解决实际问题

💡 学习建议：
1. 先自己尝试，遇到困难再看提示
2. 完成后对比参考答案
3. 尝试优化你的解决方案
"""


def exercise_1_quality_filter():
    """
    练习1：序列质量过滤 ⭐
    
    生物学背景：
    测序仪产生的reads质量参差不齐，需要过滤低质量序列。
    Phred质量分数Q30表示99.9%的准确率，是常用的质量阈值。
    
    任务：
    1. 筛选质量分数 >= 30 的序列
    2. 要求N含量 <= 10%
    3. 统计通过率
    
    编程要点：使用if语句和for循环
    """
    print("=" * 60)
    print("练习1：序列质量过滤 ⭐")
    print("=" * 60)
    
    # 测试数据
    sequences = [
        {"id": "read001", "seq": "ATGCGATCGATC", "quality": 38},
        {"id": "read002", "seq": "NATGNNNATCNN", "quality": 25},
        {"id": "read003", "seq": "GCGATCGATCGA", "quality": 41},
        {"id": "read004", "seq": "NNATGCGANNNN", "quality": 32},
        {"id": "read005", "seq": "ATGCGATCGNAT", "quality": 35},
    ]
    
    print(f"总序列数: {len(sequences)}")
    print(f"质控标准: 质量≥30, N含量≤10%")
    print("-" * 40)
    
    # TODO: 完成质量过滤
    # 提示：
    # 1. 创建列表存储通过的序列: passed = []
    # 2. 使用for循环遍历sequences
    # 3. 对每条序列检查质量和N含量
    # 4. N含量 = (序列.count('N') / len(序列)) * 100
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_2_restriction_sites():
    """
    练习2：限制性酶切位点搜索 ⭐⭐
    
    生物学背景：
    限制性内切酶识别特定的DNA序列并在该位置切割。
    需要在质粒中找到所有的酶切位点。
    
    任务：
    1. 在DNA序列中查找多种限制酶的位点
    2. 记录每个位点的位置
    3. 统计每种酶的切点数量
    
    编程要点：使用字符串搜索和循环
    """
    print("\n" + "=" * 60)
    print("练习2：限制性酶切位点搜索 ⭐⭐")
    print("=" * 60)
    
    # 质粒序列
    plasmid = "CGGAATTCATGGATCCTAGAATTCGCGGATCCAAGAATTC"
    
    # 限制酶识别序列
    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
    }
    
    print(f"质粒序列 ({len(plasmid)} bp):")
    print(plasmid)
    print("\n搜索的限制酶:")
    for enzyme, site in enzymes.items():
        print(f"  {enzyme}: {site}")
    print("-" * 40)
    
    # TODO: 查找所有酶切位点
    # 提示：
    # 1. 遍历每种酶
    # 2. 在质粒序列中搜索该酶的识别序列
    # 3. 记录找到的位置
    # 4. 可以使用字符串的find()方法
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_3_orf_finder():
    """
    练习3：开放阅读框(ORF)预测器 ⭐⭐⭐
    
    生物学背景：
    ORF是从起始密码子(ATG)到终止密码子(TAA/TAG/TGA)的序列，
    可能编码蛋白质。需要在三个阅读框中搜索。
    
    任务：
    1. 在三个阅读框中搜索ORF
    2. 找出最长的ORF
    3. 计算氨基酸长度
    
    编程要点：使用嵌套循环和break控制
    """
    print("\n" + "=" * 60)
    print("练习3：开放阅读框(ORF)预测器 ⭐⭐⭐")
    print("=" * 60)
    
    # 包含多个ORF的序列
    dna = "CGATGAAACCCTAGATGGGGTAACGATGCCCTGAATGAAATAACCC"
    
    print(f"DNA序列 ({len(dna)} bp):")
    print(dna)
    print("\n搜索参数:")
    print("  起始密码子: ATG")
    print("  终止密码子: TAA, TAG, TGA")
    print("-" * 40)
    
    # TODO: 找出所有ORF
    # 提示：
    # 1. 终止密码子列表: stop_codons = ["TAA", "TAG", "TGA"]
    # 2. 三个阅读框: for frame in range(3)
    # 3. 在每个阅读框搜索ATG开始的ORF
    # 4. 记录ORF的起始位置、长度等信息
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_4_gc_sliding_window():
    """
    练习4：滑动窗口GC分析 ⭐⭐
    
    生物学背景：
    GC含量在基因组中分布不均。通过滑动窗口分析，
    可以找到GC富集区(可能的CpG岛)。
    
    任务：
    1. 用固定窗口分析GC含量分布
    2. 找出GC含量最高和最低的区域
    3. 识别可能的CpG岛(GC>60%)
    
    编程要点：滑动窗口技术
    """
    print("\n" + "=" * 60)
    print("练习4：滑动窗口GC分析 ⭐⭐")
    print("=" * 60)
    
    # 测试序列(包含不同GC含量区域)
    dna = "GCGCGCGCGCGCATATATATATATATATCGCGCGCGCGCGATATATATA"
    window_size = 10
    
    print(f"DNA序列 ({len(dna)} bp):")
    print(dna)
    print(f"窗口大小: {window_size} bp")
    print("-" * 40)
    
    # TODO: 实现滑动窗口GC分析
    # 提示：
    # 1. 滑动窗口: for i in range(len(dna) - window_size + 1)
    # 2. 提取窗口序列: window = dna[i:i+window_size]
    # 3. 计算GC含量: (window.count('G') + window.count('C')) / window_size * 100
    # 4. 记录位置和GC含量
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_5_codon_usage():
    """
    练习5：密码子使用频率统计 ⭐⭐⭐
    
    生物学背景：
    不同物种偏好使用不同的密码子编码同一氨基酸。
    这种偏好性影响基因表达，在基因工程中很重要。
    
    任务：
    1. 统计编码序列中每种密码子的使用次数
    2. 计算使用频率
    3. 找出最常用的密码子
    
    编程要点：字典使用和统计
    """
    print("\n" + "=" * 60)
    print("练习5：密码子使用频率统计 ⭐⭐⭐")
    print("=" * 60)
    
    # 编码序列
    cds = "ATGCCCATGAAATGGATGTTTAAATAGATGCCCATGAAATAGATGAAA"
    
    print(f"CDS序列 ({len(cds)} bp):")
    print(cds)
    print(f"密码子数: {len(cds)//3}")
    print("-" * 40)
    
    # TODO: 统计密码子使用频率
    # 提示：
    # 1. 创建字典存储计数: codon_count = {}
    # 2. 提取密码子: for i in range(0, len(cds)-2, 3)
    # 3. 统计每个密码子出现次数
    # 4. 计算频率并排序
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def comprehensive_analysis():
    """
    综合应用：序列质控分析系统
    
    综合使用所有控制流知识，构建完整的分析流程
    """
    print("\n" + "=" * 60)
    print("综合应用：序列质控分析系统")
    print("=" * 60)
    
    # 模拟数据
    sequences = [
        {"id": "READ001", "seq": "ATGGCGATCGATCGATCGTAG", "qual": 38},
        {"id": "READ002", "seq": "NATGCCNNNATCGATCGATCG", "qual": 25},
        {"id": "READ003", "seq": "ATGAAACCCTAGATGGGGTAA", "qual": 42},
        {"id": "READ004", "seq": "CCGATGGCGATCGATCGATCG", "qual": 35},
    ]
    
    print(f"数据: {len(sequences)} 条序列")
    print("分析: 质量过滤 → GC分析 → motif搜索")
    print("-" * 40)
    
    # TODO: 构建完整分析流程
    # 这是一个开放性练习，综合运用所学知识！
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def main():
    """主函数：运行所有练习"""
    print("=" * 70)
    print("Chapter 03 控制流练习")
    print("=" * 70)
    print("\n练习说明：")
    print("• 每个练习都有生物学背景和编程提示")
    print("• 从简单开始，逐步挑战更难的题目")
    print("• 完成后查看practice_solution.py对比答案")
    print("• 重点是理解思路，不是死记代码")
    
    print("\n可用的练习：")
    print("1. 序列质量过滤 ⭐")
    print("2. 限制酶切位点搜索 ⭐⭐")
    print("3. ORF预测器 ⭐⭐⭐")
    print("4. 滑动窗口GC分析 ⭐⭐")
    print("5. 密码子使用统计 ⭐⭐⭐")
    print("6. 综合应用")
    
    print("\n" + "=" * 70)
    print("开始练习...")
    print("=" * 70)
    
    # 运行练习（完成一个后取消注释下一个）
    exercise_1_quality_filter()
    # exercise_2_restriction_sites()
    # exercise_3_orf_finder()
    # exercise_4_gc_sliding_window()
    # exercise_5_codon_usage()
    # comprehensive_analysis()
    
    print("\n" + "=" * 70)
    print("💡 学习建议：")
    print("• 遇到困难时，先理解生物学背景")
    print("• 将大问题分解成小步骤")
    print("• 使用print()调试，查看中间结果")
    print("• 完成后思考：还有其他解法吗？")
    print("=" * 70)


if __name__ == "__main__":
    main()