#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 01: Python基础 - 渐进式练习题

这些练习题从最简单开始，逐步增加难度。
就像在实验室，从简单的移液开始，逐步学会复杂的实验。

完成提示：
1. 先尝试自己解决
2. 如果卡住了，看看提示
3. 实在不会，参考 practice_solution.py
4. 重要的是理解，不是答案
"""


def warmup_print_dna():
    """
    热身题：你的第一行代码
    
    难度：⭐
    目标：学会使用print函数
    生物背景：显示实验结果是研究的第一步
    """
    print("\n" + "="*50)
    print("热身题：打印DNA序列")
    print("="*50)
    
    # TODO: 完成下面的代码
    # 提示：print()函数可以显示任何内容
    
    # 1. 打印一个简单的DNA序列
    my_dna = "ATCG"
    # 在下面写代码打印my_dna
    # ???
    
    # 2. 打印带说明的序列
    # 打印："我的DNA序列是: ATCG"
    # ???
    
    # 3. 使用变量打印你的名字和序列
    your_name = "你的名字"  # 改成你的真实名字
    # 打印："我是[你的名字]，我的序列是[my_dna]"
    # ???
    
    print("\n如果你看到了DNA序列，恭喜你完成了第一个练习！")


def practice_1_simple_variables():
    """
    练习1：创建和使用变量
    
    难度：⭐
    目标：理解变量就像试管
    生物背景：实验室中需要标记和存储不同的样品
    """
    print("\n" + "="*50)
    print("练习1：变量练习 - 试管标签")
    print("="*50)
    
    print("场景：你收到了3个DNA样品，需要标记它们")
    
    # TODO: 创建变量存储以下信息
    # 提示：变量名 = 值
    
    # 1. 第一个样品：人类DNA序列 "ATCGATCG"
    # human_dna = ???
    
    # 2. 第二个样品：小鼠DNA序列 "GCTAGCTA"
    # mouse_dna = ???
    
    # 3. 第三个样品：细菌DNA序列 "CGCGCGCG"
    # bacteria_dna = ???
    
    # 4. 实验温度：37度
    # temperature = ???
    
    # 5. 是否是活体样品：False
    # is_living = ???
    
    # TODO: 打印所有变量
    # print("人类DNA:", ???)
    # print("小鼠DNA:", ???)
    # print("细菌DNA:", ???)
    # print("温度:", ???, "°C")
    # print("活体样品:", ???)


def practice_2_string_length():
    """
    练习2：测量序列长度
    
    难度：⭐⭐
    目标：学会使用len()函数
    生物背景：序列长度是最基本的序列特征
    """
    print("\n" + "="*50)
    print("练习2：测量DNA序列长度")
    print("="*50)
    
    print("场景：PCR产物长度检测")
    
    # 给定的PCR产物序列
    pcr_product = "ATCGATCGATCGATCGATCG"
    print(f"PCR产物: {pcr_product}")
    
    # TODO: 计算序列长度
    # 提示：使用len()函数
    
    # 1. 计算PCR产物长度
    # product_length = ???
    # print(f"PCR产物长度: ??? bp")
    
    # 2. 判断长度是否符合预期（预期20bp）
    expected_length = 20
    # is_correct_length = product_length == expected_length
    # print(f"长度是否正确: ???")
    
    # 3. 计算引物序列长度
    forward_primer = "ATCG"
    reverse_primer = "CGAT"
    # forward_length = ???
    # reverse_length = ???
    # print(f"正向引物长度: ??? bp")
    # print(f"反向引物长度: ??? bp")


def practice_3_string_upper_lower():
    """
    练习3：序列标准化
    
    难度：⭐⭐
    目标：学会大小写转换
    生物背景：不同来源的序列数据格式可能不同
    """
    print("\n" + "="*50)
    print("练习3：标准化序列格式")
    print("="*50)
    
    print("场景：整合不同实验室的测序数据")
    
    # 不同格式的序列
    lab1_sequence = "atcgatcg"      # 实验室1：小写
    lab2_sequence = "ATCGATCG"      # 实验室2：大写
    lab3_sequence = "AtCgAtCg"      # 实验室3：混合
    
    print("原始数据:")
    print(f"实验室1: {lab1_sequence}")
    print(f"实验室2: {lab2_sequence}")
    print(f"实验室3: {lab3_sequence}")
    
    # TODO: 标准化所有序列为大写
    # 提示：使用.upper()方法
    
    # 1. 转换实验室1的序列
    # lab1_standard = ???
    
    # 2. 转换实验室2的序列（已经是大写）
    # lab2_standard = ???
    
    # 3. 转换实验室3的序列
    # lab3_standard = ???
    
    # print("\n标准化后:")
    # print(f"实验室1: ???")
    # print(f"实验室2: ???")
    # print(f"实验室3: ???")
    
    # 4. 检查是否所有序列现在都相同
    # all_same = (lab1_standard == lab2_standard == lab3_standard)
    # print(f"\n所有序列是否相同: ???")


def practice_4_count_bases():
    """
    练习4：统计碱基数量
    
    难度：⭐⭐
    目标：学会使用count()方法
    生物背景：碱基组成分析是序列分析的基础
    """
    print("\n" + "="*50)
    print("练习4：碱基组成分析")
    print("="*50)
    
    print("场景：分析启动子序列的碱基组成")
    
    # 启动子序列
    promoter = "TATAAAAATCGATCGATCG"
    print(f"启动子序列: {promoter}")
    
    # TODO: 统计各碱基数量
    # 提示：使用.count()方法
    
    # 1. 统计A的数量
    # a_count = ???
    # print(f"A的数量: ???")
    
    # 2. 统计T的数量
    # t_count = ???
    # print(f"T的数量: ???")
    
    # 3. 统计C的数量
    # c_count = ???
    # print(f"C的数量: ???")
    
    # 4. 统计G的数量
    # g_count = ???
    # print(f"G的数量: ???")
    
    # 5. 验证总数是否正确
    # total_counted = a_count + t_count + c_count + g_count
    # sequence_length = len(promoter)
    # print(f"\n统计总数: ???")
    # print(f"序列长度: ???")
    # print(f"计数是否正确: ???")


def practice_5_calculate_at_content():
    """
    练习5：计算AT含量
    
    难度：⭐⭐⭐
    目标：结合count和len计算百分比
    生物背景：AT含量与DNA稳定性相关
    """
    print("\n" + "="*50)
    print("练习5：计算AT含量")
    print("="*50)
    
    print("场景：分析AT富集区域")
    
    # AT富集序列
    at_rich_sequence = "AAATTTAAATTTAAATTT"
    print(f"序列: {at_rich_sequence}")
    
    # TODO: 计算AT含量
    # 提示：AT含量 = (A数量 + T数量) / 总长度 × 100
    
    # 1. 统计A和T
    # a_count = ???
    # t_count = ???
    
    # 2. 获取序列长度
    # total_length = ???
    
    # 3. 计算AT碱基总数
    # at_bases = ???
    
    # 4. 计算AT含量百分比
    # at_content = ???
    
    # 5. 计算GC含量（提示：GC含量 = 100 - AT含量）
    # gc_content = ???
    
    # print(f"\nA的数量: ???")
    # print(f"T的数量: ???")
    # print(f"AT碱基总数: ???")
    # print(f"序列总长度: ???")
    # print(f"AT含量: ???%")
    # print(f"GC含量: ???%")


def practice_6_sequence_slicing():
    """
    练习6：序列切片
    
    难度：⭐⭐⭐
    目标：学会提取序列片段
    生物背景：提取密码子、识别序列模体
    """
    print("\n" + "="*50)
    print("练习6：提取序列片段")
    print("="*50)
    
    print("场景：从基因序列中提取密码子")
    
    # 基因序列（包含起始密码子ATG）
    gene = "ATGGATTTATCTGCTCTTCGCG"
    print(f"基因序列: {gene}")
    print("位置索引: 0123456789...")  # 帮助理解
    
    # TODO: 提取不同片段
    # 提示：序列[起始:结束]，序列[-n:]获取最后n个
    
    # 1. 提取起始密码子（前3个碱基）
    # start_codon = ???
    # print(f"起始密码子: ???")
    
    # 2. 提取第二个密码子（位置3-6）
    # second_codon = ???
    # print(f"第二个密码子: ???")
    
    # 3. 提取前10个碱基
    # first_ten = ???
    # print(f"前10个碱基: ???")
    
    # 4. 提取最后5个碱基
    # last_five = ???
    # print(f"最后5个碱基: ???")
    
    # 5. 提取中间片段（位置5到15）
    # middle_part = ???
    # print(f"中间片段[5:15]: ???")


def practice_7_find_pattern():
    """
    练习7：查找序列模式
    
    难度：⭐⭐⭐
    目标：学会查找和验证序列特征
    生物背景：识别启动子、终止子等调控元件
    """
    print("\n" + "="*50)
    print("练习7：查找生物学模式")
    print("="*50)
    
    print("场景：在序列中查找TATA box")
    
    # 启动子区域序列
    promoter_region = "GCGCTATAAAAGCGCGCATGGATTTATCTGC"
    print(f"启动子序列: {promoter_region}")
    
    # TODO: 查找特定模式
    # 提示：使用 in 操作符和 .find() 方法
    
    # 1. 检查是否包含TATA box (TATAAA)
    tata_box = "TATAAA"
    # has_tata = ???  # 提示：使用 in
    # print(f"包含TATA box: ???")
    
    # 2. 如果有，找出位置
    # if has_tata:
    #     position = ???  # 提示：使用.find()
    #     print(f"TATA box位置: ???")
    
    # 3. 检查是否有起始密码子ATG
    # has_atg = ???
    # print(f"包含起始密码子ATG: ???")
    
    # 4. 统计GC出现的次数
    # gc_count = ???  # 提示：使用.count()
    # print(f"'GC'模式出现次数: ???")


def practice_8_calculate_gc_content():
    """
    练习8：完整的GC含量计算
    
    难度：⭐⭐⭐⭐
    目标：综合运用所学知识
    生物背景：GC含量是序列分析的核心指标
    """
    print("\n" + "="*50)
    print("练习8：GC含量计算（综合练习）")
    print("="*50)
    
    print("场景：分析不同物种的GC含量")
    
    # 不同物种的序列
    sequences = {
        "人类": "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTAC",
        "大肠杆菌": "GCGCGCGCATCGATCGATCGATCGCGCGCGC",
        "酵母": "ATATATATATGCGCGCGCATATATATAT"
    }
    
    for species, sequence in sequences.items():
        print(f"\n{species}序列: {sequence}")
        
        # TODO: 计算每个物种的GC含量
        
        # 1. 标准化序列
        # clean_seq = ???
        
        # 2. 计算G和C的数量
        # g_count = ???
        # c_count = ???
        
        # 3. 计算总长度
        # total = ???
        
        # 4. 计算GC含量
        # gc_content = ???
        
        # 5. 根据GC含量分类
        # if gc_content < 40:
        #     category = "低GC含量"
        # elif gc_content < 60:
        #     category = "中等GC含量"
        # else:
        #     category = "高GC含量"
        
        # print(f"  GC含量: ???%")
        # print(f"  分类: ???")


def practice_9_sequence_validation():
    """
    练习9：序列质量控制
    
    难度：⭐⭐⭐⭐
    目标：验证序列数据质量
    生物背景：确保数据质量是分析的第一步
    """
    print("\n" + "="*50)
    print("练习9：序列质量验证")
    print("="*50)
    
    print("场景：验证测序数据质量")
    
    # 待验证的序列
    test_sequences = [
        "ATCGATCG",          # 正常序列
        "ATCGATCGN",         # 含有N
        "atcgatcg",          # 小写
        "ATCG ATCG",         # 含有空格
        "ATCGATCG123",       # 含有数字
        "ATCG-ATCG"          # 含有连字符
    ]
    
    for i, seq in enumerate(test_sequences, 1):
        print(f"\n序列{i}: '{seq}'")
        
        # TODO: 验证序列
        
        # 1. 先转为大写
        # upper_seq = ???
        
        # 2. 检查每个字符是否都是ATCG
        # valid = True
        # invalid_chars = []
        # for char in upper_seq:
        #     if char not in 'ATCG':
        #         valid = False
        #         invalid_chars.append(char)
        
        # 3. 输出验证结果
        # if valid:
        #     print("  ✅ 有效序列")
        # else:
        #     print(f"  ❌ 无效序列，包含: ???")
        
        # 4. 如果可以修复，显示清理后的序列
        # cleaned = ""
        # for char in upper_seq:
        #     if char in 'ATCG':
        #         cleaned += char
        # if cleaned and not valid:
        #     print(f"  清理后: ???")


def challenge_comprehensive_analysis():
    """
    挑战题：综合序列分析
    
    难度：⭐⭐⭐⭐⭐
    目标：完成一个完整的序列分析任务
    生物背景：模拟真实的序列分析流程
    """
    print("\n" + "="*50)
    print("挑战题：综合序列分析")
    print("="*50)
    
    print("场景：你收到了一个未知基因序列，需要完整分析")
    
    # 未知序列
    unknown_seq = "atgGATTTATCTgctcttcgcgTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCtaa"
    
    print(f"原始序列: {unknown_seq}")
    print("\n请完成以下分析任务:")
    
    # TODO: 完成综合分析
    
    # 任务1：数据清理和标准化
    # - 转为大写
    # - 检查是否只包含ATCG
    # clean_seq = ???
    
    # 任务2：基本统计
    # - 序列长度
    # - 各碱基数量和比例
    # length = ???
    # a_count = ???
    # t_count = ???
    # c_count = ???
    # g_count = ???
    
    # 任务3：计算GC含量和AT含量
    # gc_content = ???
    # at_content = ???
    
    # 任务4：查找生物学特征
    # - 是否有起始密码子ATG
    # - 是否有终止密码子(TAA, TAG, TGA)
    # has_start = ???
    # has_stop = ???
    
    # 任务5：提取ORF（开放阅读框）
    # - 从ATG开始到终止密码子
    # if has_start and has_stop:
    #     start_pos = clean_seq.find('ATG')
    #     # 查找终止密码子...
    #     orf = ???
    
    # 任务6：生成分析报告
    # print("\n=== 序列分析报告 ===")
    # print(f"序列长度: ??? bp")
    # print(f"GC含量: ???%")
    # print(f"AT含量: ???%")
    # print(f"碱基组成: A:???, T:???, C:???, G:???")
    # print(f"起始密码子: ???")
    # print(f"终止密码子: ???")
    # 根据GC含量推测可能的来源...


def main():
    """
    主函数：运行所有练习
    """
    print("="*50)
    print("Chapter 01: Python基础 - 渐进式练习")
    print("="*50)
    print("\n从最简单的开始，一步步掌握Python！")
    print("每完成一个练习，你就离成为生物信息学家更近一步。")
    
    # 热身
    print("\n" + "🔥 热身运动")
    warmup_print_dna()
    
    # 基础练习
    print("\n" + "📚 基础练习")
    practice_1_simple_variables()
    practice_2_string_length()
    practice_3_string_upper_lower()
    practice_4_count_bases()
    
    # 进阶练习
    print("\n" + "🚀 进阶练习")
    practice_5_calculate_at_content()
    practice_6_sequence_slicing()
    practice_7_find_pattern()
    
    # 综合练习
    print("\n" + "💪 综合练习")
    practice_8_calculate_gc_content()
    practice_9_sequence_validation()
    
    # 挑战题
    print("\n" + "🏆 挑战题")
    challenge_comprehensive_analysis()
    
    print("\n" + "="*50)
    print("练习指南")
    print("="*50)
    print("\n完成建议：")
    print("1. 先尝试自己解决，不要急于看答案")
    print("2. 如果卡住超过10分钟，看看提示")
    print("3. 完成后对比 practice_solution.py")
    print("4. 理解比答案更重要")
    
    print("\n学习技巧：")
    print("- 每个练习都基于前面的知识")
    print("- 遇到错误是正常的，这是学习过程")
    print("- 多尝试不同的方法解决同一个问题")
    print("- 记住生物学背景，让编程更有意义")
    
    print("\n加油！你可以的！🧬")


if __name__ == "__main__":
    main()