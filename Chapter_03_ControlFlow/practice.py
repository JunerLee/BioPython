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
4. 用真实数据测试你的代码
"""


def exercise_1_quality_filter():
    """
    练习1：序列质量过滤 ⭐
    
    生物学背景：
    测序仪产生的reads质量参差不齐，需要过滤低质量序列。
    Phred质量分数Q30表示99.9%的准确率，是常用的质量阈值。
    N表示测序时无法确定的碱基，过多的N意味着测序质量差。
    
    任务：
    1. 筛选质量分数 >= 30 的序列
    2. 同时要求N的含量 <= 10%
    3. 统计通过率
    4. 分别报告因质量和N含量被过滤的序列数
    
    编程要点：
    - 使用if语句进行条件判断
    - 使用for循环遍历序列
    - 计算百分比
    - 分类统计结果
    """
    print("=" * 60)
    print("练习1：序列质量过滤 ⭐")
    print("=" * 60)
    
    # 测试数据：模拟的测序reads
    sequences = [
        {"id": "read001", "seq": "ATGCGATCGATC", "quality": 38},  # 高质量，无N
        {"id": "read002", "seq": "NATGNNNATCNN", "quality": 25},  # 低质量，多N
        {"id": "read003", "seq": "GCGATCGATCGA", "quality": 41},  # 高质量，无N
        {"id": "read004", "seq": "NNATGCGANNNN", "quality": 32},  # 质量OK但N太多
        {"id": "read005", "seq": "ATGCGATCGNAT", "quality": 35},  # 质量OK，N少
        {"id": "read006", "seq": "ATGCGATCGATC", "quality": 18},  # 质量太低
        {"id": "read007", "seq": "GCGCGCGCGCGC", "quality": 45},  # 极高质量
    ]
    
    print(f"总序列数: {len(sequences)}")
    print(f"质控标准: 质量≥30, N含量≤10%")
    print("-" * 40)
    
    # TODO: 完成质量过滤
    # 步骤提示：
    # 1. 创建列表存储通过和未通过的序列
    #    passed_sequences = []
    #    failed_by_quality = []
    #    failed_by_n = []
    # 2. 使用for循环遍历每条序列
    # 3. 对每条序列：
    #    a. 检查质量分数是否 >= 30
    #    b. 计算N的百分比：(序列.count('N') / len(序列)) * 100
    #    c. 检查N百分比是否 <= 10
    #    d. 根据检查结果分类存储
    # 4. 输出详细的统计结果
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_2_find_restriction_sites():
    """
    练习2：查找限制性酶切位点 ⭐⭐
    
    生物学背景：
    限制性内切酶识别特定的DNA序列并在该位置切割DNA。
    不同的酶识别不同的序列，在分子克隆中需要选择合适的酶。
    
    任务：
    1. 在DNA序列中查找多种限制酶的识别位点
    2. 记录每个位点的位置和类型
    3. 计算酶切后产生的片段大小
    4. 找出最适合克隆的酶（产生2-3个片段）
    
    编程要点：
    - 使用for循环配合range()遍历序列
    - 使用字符串切片提取子序列
    - 使用字典存储不同酶的信息
    - 使用列表存储位点位置
    """
    print("\n" + "=" * 60)
    print("练习2：限制性酶切位点分析 ⭐⭐")
    print("=" * 60)
    
    # 质粒序列（模拟）
    plasmid = "CGGAATTCATGGATCCTAGAATTCGCGGATCCAAGAATTCCTGCAGGGATCCATG"
    
    # 限制酶识别序列
    enzymes = {
        "EcoRI": "GAATTC",   # 识别GAATTC
        "BamHI": "GGATCC",   # 识别GGATCC
        "PstI": "CTGCAG",    # 识别CTGCAG
    }
    
    print(f"质粒序列 ({len(plasmid)} bp):")
    print(plasmid)
    print("\n搜索的限制酶:")
    for enzyme, site in enzymes.items():
        print(f"  {enzyme}: {site}")
    print("-" * 40)
    
    # TODO: 查找所有的酶切位点
    # 步骤提示：
    # 1. 创建字典存储每种酶的切点位置
    #    site_positions = {}
    # 2. 对每种酶：
    #    a. 初始化位置列表
    #    b. 使用for i in range(len(plasmid) - len(site) + 1)遍历
    #    c. 提取子序列：plasmid[i:i+len(site)]
    #    d. 如果匹配，记录位置
    # 3. 计算每种酶切割后的片段数
    # 4. 显示结果和推荐
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_3_find_longest_orf():
    """
    练习3：找出最长的开放阅读框(ORF) ⭐⭐⭐
    
    生物学背景：
    开放阅读框(ORF)是从起始密码子(ATG)到终止密码子(TAA/TAG/TGA)
    之间的序列，可能编码蛋白质。最长的ORF通常最可能是真实的基因。
    在基因预测中，需要在三个阅读框中寻找所有ORF。
    
    任务：
    1. 在三个阅读框中搜索所有ORF
    2. 计算每个ORF的长度和编码的氨基酸数
    3. 找出最长的ORF
    4. 判断ORF的完整性（是否有起始和终止密码子）
    
    编程要点：
    - 嵌套循环（外层：阅读框，内层：搜索）
    - 使用while或for循环进行搜索
    - 使用break控制循环流程
    - 记录和比较最大值
    """
    print("\n" + "=" * 60)
    print("练习3：最长开放阅读框(ORF)预测 ⭐⭐⭐")
    print("=" * 60)
    
    # 包含多个ORF的序列
    dna = "CGATGAAACCCTAGATGGGGTAACGATGCCCTGAATGAAATAACCCATGACCGTATGCGATGAAATAGTAG"
    
    print(f"DNA序列 ({len(dna)} bp):")
    print(dna)
    print("\n搜索参数:")
    print("  起始密码子: ATG")
    print("  终止密码子: TAA, TAG, TGA")
    print("  最小ORF长度: 30 bp")
    print("-" * 40)
    
    # TODO: 找出最长的ORF
    # 步骤提示：
    # 1. 定义终止密码子列表：stop_codons = ["TAA", "TAG", "TGA"]
    # 2. 创建列表存储所有ORF
    # 3. 对每个阅读框（0, 1, 2）：
    #    for frame in range(3):
    #        # 在该阅读框中搜索
    #        for i in range(frame, len(dna) - 2, 3):
    #            if dna[i:i+3] == "ATG":
    #                # 从ATG开始找终止密码子
    #                for j in range(i+3, len(dna)-2, 3):
    #                    if dna[j:j+3] in stop_codons:
    #                        # 记录ORF
    #                        break
    # 4. 找出最长的ORF并输出详细信息
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_4_gc_content_windows():
    """
    练习4：滑动窗口分析GC含量 ⭐⭐
    
    生物学背景：
    GC含量在基因组中并不均匀分布。通过滑动窗口分析，
    可以找到GC富集区（可能是CpG岛、启动子区域）或AT富集区。
    这对基因预测和功能注释很重要。
    
    任务：
    1. 使用滑动窗口分析序列的GC含量分布
    2. 找出GC含量的峰值和谷值
    3. 识别可能的CpG岛（GC>60%的区域）
    4. 绘制简单的GC含量分布图（文本版）
    
    编程要点：
    - 滑动窗口技术（固定窗口大小，逐位移动）
    - 百分比计算
    - 找最大值和最小值
    - 简单的数据可视化
    """
    print("\n" + "=" * 60)
    print("练习4：滑动窗口GC含量分析 ⭐⭐")
    print("=" * 60)
    
    # 测试序列（包含GC富集和AT富集区域）
    dna = "GCGCGCGCGCGCGCATATATATATATATATCGCGCGCGCGCGCGATATATATATATATGCGCGCGCGC"
    window_size = 10
    step_size = 5  # 窗口移动步长
    
    print(f"DNA序列 ({len(dna)} bp):")
    print(dna)
    print(f"\n分析参数:")
    print(f"  窗口大小: {window_size} bp")
    print(f"  步长: {step_size} bp")
    print("-" * 40)
    
    # TODO: 实现滑动窗口GC分析
    # 步骤提示：
    # 1. 创建列表存储每个窗口的结果
    #    results = []
    # 2. 滑动窗口：
    #    for i in range(0, len(dna) - window_size + 1, step_size):
    #        window = dna[i:i+window_size]
    #        gc_count = window.count('G') + window.count('C')
    #        gc_percent = (gc_count / window_size) * 100
    #        results.append({"position": i, "gc": gc_percent})
    # 3. 找出最高和最低的GC含量窗口
    # 4. 识别CpG岛候选区域（GC > 60%）
    # 5. 绘制简单的分布图
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_5_codon_usage():
    """
    练习5：密码子使用频率统计 ⭐⭐⭐
    
    生物学背景：
    不同物种偏好使用不同的密码子编码同一个氨基酸（密码子偏好性）。
    这种偏好性影响基因表达水平，在异源表达和基因合成中很重要。
    
    任务：
    1. 将编码序列分成密码子
    2. 统计每种密码子的使用次数和频率
    3. 找出最常用和最少用的密码子
    4. 计算密码子适应指数(CAI)的简化版本
    5. 判断序列是否适合在大肠杆菌中表达
    
    编程要点：
    - 字典的使用（存储计数）
    - 嵌套的条件判断
    - 统计和排序
    - 百分比计算
    """
    print("\n" + "=" * 60)
    print("练习5：密码子使用偏好性分析 ⭐⭐⭐")
    print("=" * 60)
    
    # 编码序列（已经是正确的阅读框）
    cds = "ATGCCCATGAAATGGATGTTTAAATAGATGCCCATGAAATAGATGAAACCCATGGGGTAA"
    
    # 大肠杆菌偏好的密码子（简化版）
    ecoli_preferred = {
        "ATG": "M",  # 甲硫氨酸（起始）
        "CCC": "P",  # 脯氨酸（偏好）
        "AAA": "K",  # 赖氨酸（偏好）
        "GAA": "E",  # 谷氨酸（偏好）
        "GGG": "G",  # 甘氨酸（偏好）
    }
    
    print(f"CDS序列 ({len(cds)} bp):")
    print(cds)
    print(f"密码子数: {len(cds)//3}")
    print("\n大肠杆菌偏好密码子（示例）:")
    for codon, aa in ecoli_preferred.items():
        print(f"  {codon} → {aa}")
    print("-" * 40)
    
    # TODO: 统计密码子使用频率
    # 挑战提示：
    # 1. 创建字典存储密码子计数：
    #    codon_count = {}
    # 2. 提取所有密码子并统计：
    #    for i in range(0, len(cds)-2, 3):
    #        codon = cds[i:i+3]
    #        if len(codon) == 3:
    #            if codon in codon_count:
    #                codon_count[codon] += 1
    #            else:
    #                codon_count[codon] = 1
    # 3. 计算频率
    # 4. 找出最常用和最少用的密码子
    # 5. 计算偏好密码子的使用比例
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_6_sequence_alignment_check():
    """
    练习6：序列比对质量检查 ⭐⭐
    
    生物学背景：
    序列比对后需要评估比对质量，包括相似度、gap数量、
    保守区域等。这对进化分析和功能预测很重要。
    
    任务：
    1. 计算两条序列的相似度
    2. 统计匹配、错配和gap的数量
    3. 识别保守区域（连续匹配>=5bp）
    4. 计算比对得分
    
    编程要点：
    - 同时遍历两个序列
    - 条件判断和计数
    - 连续区域的识别
    """
    print("\n" + "=" * 60)
    print("练习6：序列比对质量检查 ⭐⭐")
    print("=" * 60)
    
    # 比对后的序列（-表示gap）
    seq1 = "ATGCGATCG-ATCGATCG"
    seq2 = "ATGC-ATCGGATC-ATCG"
    
    print("比对序列:")
    print(f"Seq1: {seq1}")
    print(f"Seq2: {seq2}")
    print(f"长度: {len(seq1)} bp")
    print("-" * 40)
    
    # TODO: 分析比对质量
    # 提示：
    # 1. 遍历两个序列的每个位置
    # 2. 统计：
    #    - 匹配（两个位置碱基相同且不是gap）
    #    - 错配（两个位置碱基不同且都不是gap）
    #    - gap（任一位置是'-'）
    # 3. 计算相似度 = 匹配数 / 总长度 * 100
    # 4. 识别保守区域
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def exercise_7_primer_design():
    """
    练习7：PCR引物设计验证 ⭐⭐⭐
    
    生物学背景：
    PCR引物设计需要满足多个条件：长度、GC含量、Tm值、
    二级结构、特异性等。好的引物是PCR成功的关键。
    
    任务：
    1. 验证引物对的基本参数
    2. 检查引物二聚体
    3. 检查发夹结构
    4. 计算PCR产物长度
    5. 给出综合评分
    
    编程要点：
    - 多条件判断
    - 字符串反向互补
    - 模式匹配
    - 评分系统设计
    """
    print("\n" + "=" * 60)
    print("练习7：PCR引物设计验证 ⭐⭐⭐")
    print("=" * 60)
    
    # 模板序列
    template = "ATGGCTTGAATGAAGGCCTAGGATCCGAATTCATGCAGCTGATGCACGGATCCTAGAATTCGCA"
    
    # 引物对
    forward_primer = "ATGGCTTGAATGAAGGCC"    # 正向引物
    reverse_primer = "TGCGAATTCTAGGATCCG"    # 反向引物（5'-3'方向）
    
    print(f"模板序列 ({len(template)} bp):")
    print(template)
    print(f"\n引物对:")
    print(f"  Forward: {forward_primer}")
    print(f"  Reverse: {reverse_primer}")
    print("-" * 40)
    
    # TODO: 验证引物设计
    # 挑战提示：
    # 1. 检查基本参数：
    #    - 长度（18-25bp）
    #    - GC含量（40-60%）
    #    - Tm值（简化计算：4*(G+C) + 2*(A+T)）
    # 2. 检查引物在模板上的位置
    # 3. 计算PCR产物长度
    # 4. 检查潜在问题：
    #    - 3'端是否为G或C（有利于延伸）
    #    - 是否有连续的相同碱基（>4个）
    # 5. 给出评分和建议
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def challenge_problem():
    """
    挑战题：基因表达数据分析 ⭐⭐⭐⭐
    
    综合运用所有控制流知识，实现一个基因表达数据分析流程。
    
    任务：
    1. 读取多个样品的基因表达数据
    2. 进行质量控制（过滤低表达基因）
    3. 识别差异表达基因
    4. 进行基因功能分类
    5. 生成分析报告
    
    这是一个接近真实应用的综合练习！
    """
    print("\n" + "=" * 60)
    print("挑战题：基因表达数据分析 ⭐⭐⭐⭐")
    print("=" * 60)
    
    # 模拟的基因表达数据（FPKM值）
    # 格式：基因ID -> [正常组表达值, 处理组表达值]
    expression_data = {
        "BRCA1": [2.5, 8.3],      # 上调基因
        "TP53": [5.6, 5.8],       # 无变化
        "MYC": [12.3, 3.1],       # 下调基因
        "EGFR": [0.2, 0.3],       # 低表达
        "KRAS": [4.5, 15.2],      # 显著上调
        "PTEN": [8.9, 2.1],       # 显著下调
        "APC": [0.0, 0.0],        # 不表达
        "BRAF": [3.2, 3.5],       # 无变化
        "PIK3CA": [1.8, 7.2],     # 上调
        "RB1": [6.5, 1.5],        # 下调
    }
    
    # 基因功能注释（简化）
    gene_functions = {
        "BRCA1": "DNA修复",
        "TP53": "肿瘤抑制",
        "MYC": "转录因子",
        "EGFR": "受体",
        "KRAS": "信号传导",
        "PTEN": "肿瘤抑制",
        "APC": "肿瘤抑制",
        "BRAF": "信号传导",
        "PIK3CA": "信号传导",
        "RB1": "细胞周期",
    }
    
    print("基因表达数据分析")
    print(f"基因数: {len(expression_data)}")
    print("样品: 正常组 vs 处理组")
    print("-" * 40)
    
    # TODO: 实现基因表达分析
    # 这是一个开放性的挑战，发挥你的创造力！
    # 
    # 建议的分析步骤：
    # 1. 质量控制：过滤掉表达量极低的基因（FPKM < 1）
    # 2. 计算fold change：处理组/正常组
    # 3. 识别差异表达基因：
    #    - 显著上调：fold change > 2
    #    - 显著下调：fold change < 0.5
    # 4. 按功能分类统计
    # 5. 生成报告
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def bonus_exercise_sequence_simulator():
    """
    附加练习：DNA序列模拟器 ⭐⭐⭐
    
    创建一个DNA序列模拟器，模拟突变和进化过程。
    
    任务：
    1. 生成随机DNA序列
    2. 模拟点突变
    3. 模拟插入和删除
    4. 计算突变前后的序列相似度
    5. 模拟自然选择（保留有利突变）
    """
    print("\n" + "=" * 60)
    print("附加练习：DNA序列进化模拟器 ⭐⭐⭐")
    print("=" * 60)
    
    import random
    
    # 原始序列
    original = "ATGGCATGAAACCCTAGGATCCGAATTC"
    
    print(f"原始序列 ({len(original)} bp):")
    print(original)
    print("\n模拟参数:")
    print("  突变率: 0.1 (10%)")
    print("  代数: 5")
    print("-" * 40)
    
    # TODO: 实现序列进化模拟
    # 提示：
    # 1. 复制原始序列
    # 2. 对每一代：
    #    - 随机选择突变位置
    #    - 随机选择突变类型（替换、插入、删除）
    #    - 应用突变
    #    - 计算与原始序列的相似度
    # 3. 记录进化历程
    
    # 在这里写你的代码
    pass  # 删除这行，写你的代码


def main():
    """主函数：运行所有练习"""
    print("=" * 70)
    print("Chapter 03 控制流练习")
    print("=" * 70)
    print("\n练习说明：")
    print("• 每个练习都有详细的背景介绍和步骤提示")
    print("• 从简单的开始，逐步挑战更难的题目")
    print("• 完成后对比practice_solution.py查看参考答案")
    print("• 重点是理解思路，而不是死记代码")
    print("• 尝试用不同方法解决同一问题")
    
    print("\n可用的练习：")
    print("1. 序列质量过滤 ⭐")
    print("2. 限制性酶切位点分析 ⭐⭐")
    print("3. 最长ORF预测 ⭐⭐⭐")
    print("4. 滑动窗口GC分析 ⭐⭐")
    print("5. 密码子使用频率统计 ⭐⭐⭐")
    print("6. 序列比对质量检查 ⭐⭐")
    print("7. PCR引物设计验证 ⭐⭐⭐")
    print("8. 基因表达数据分析（挑战题）⭐⭐⭐⭐")
    print("9. DNA序列进化模拟（附加题）⭐⭐⭐")
    
    print("\n" + "=" * 70)
    print("开始练习...")
    print("=" * 70)
    
    # 运行练习（完成一个后取消注释下一个）
    exercise_1_quality_filter()
    # exercise_2_find_restriction_sites()
    # exercise_3_find_longest_orf()
    # exercise_4_gc_content_windows()
    # exercise_5_codon_usage()
    # exercise_6_sequence_alignment_check()
    # exercise_7_primer_design()
    # challenge_problem()
    # bonus_exercise_sequence_simulator()
    
    print("\n" + "=" * 70)
    print("💡 学习建议：")
    print("• 如果遇到困难，先理解问题的生物学背景")
    print("• 将大问题分解成小步骤")
    print("• 使用print()调试，查看中间结果")
    print("• 完成后思考：还有其他解决方法吗？")
    print("• 尝试用真实的生物数据测试你的代码")
    print("=" * 70)


if __name__ == "__main__":
    main()