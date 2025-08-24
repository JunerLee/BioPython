#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 04: 函数 - 渐进式练习

像学习实验室SOP一样学习函数：
从简单到复杂，逐步掌握函数的设计和使用。
"""


def practice_1_your_first_function():
    """
    练习1: 你的第一个函数 - AT含量计算
    
    难度：⭐ (入门级)
    
    目标：学会定义和调用简单函数
    类比：创建你的第一个实验室SOP
    """
    print("🔬 练习1: 创建你的第一个函数")
    print("-" * 40)
    print("目标: 定义一个计算AT含量的函数")
    print("就像编写DNA纯度检测的SOP\n")
    
    # TODO: 定义你的第一个函数
    # 提示：模仿GC含量计算，但计算A和T的含量
    
    # def calculate_at_content(sequence):
    #     """
    #     计算DNA序列的AT含量
    #     
    #     这是你的第一个"实验室SOP"：
    #     1. 接收DNA样品（sequence参数）
    #     2. 计数A和T碱基
    #     3. 计算百分比
    #     4. 返回结果
    #     """
    #     # 步骤1: 统计A的数量
    #     
    #     # 步骤2: 统计T的数量
    #     
    #     # 步骤3: 计算总长度
    #     
    #     # 步骤4: 计算百分比并返回
    #     pass
    
    # 测试你的函数
    test_sequences = [
        "ATCGATCG",     # 50% AT
        "AAAATTTT",     # 100% AT
        "CCCCGGGG"      # 0% AT
    ]
    
    print("测试序列:")
    for seq in test_sequences:
        print(f"  {seq}")
        # TODO: 调用你的函数并打印结果
        # at_content = calculate_at_content(seq)
        # print(f"    AT含量: {at_content:.1f}%")


def practice_2_function_with_validation():
    """
    练习2: 带验证的函数 - 改进版AT含量计算
    
    难度：⭐⭐ (初级)
    
    目标：学会在函数中添加输入验证
    类比：像实验室SOP的质控步骤
    """
    print("\n🔬 练习2: 添加输入验证")
    print("-" * 40)
    print("目标: 改进函数，添加输入验证")
    print("就像SOP中的样品质控步骤\n")
    
    # TODO: 定义带验证的函数
    # def calculate_at_content_safe(sequence):
    #     """
    #     安全的AT含量计算器
    #     
    #     包含质控步骤：
    #     1. 检查输入是否为空
    #     2. 转换为大写（标准化）
    #     3. 验证是否只包含ATCG
    #     4. 计算并返回结果
    #     """
    #     # 质控步骤1: 检查是否为空
    #     if not sequence:
    #         return 0.0
    #     
    #     # 质控步骤2: 标准化（转大写）
    #     
    #     # 质控步骤3: 验证碱基
    #     
    #     # 如果验证失败，返回-1表示错误
    #     
    #     # 计算AT含量
    #     pass
    
    # 测试各种输入
    test_cases = [
        "ATCGATCG",     # 正常
        "atcgatcg",     # 小写
        "",             # 空序列
        "ATCGXYZ"       # 包含无效字符
    ]
    
    print("测试带验证的函数:")
    for seq in test_cases:
        print(f"  输入: '{seq}'")
        # TODO: 调用函数并处理结果
        # result = calculate_at_content_safe(seq)
        # if result >= 0:
        #     print(f"    AT含量: {result:.1f}%")
        # else:
        #     print(f"    错误: 序列包含无效字符")


def practice_3_function_with_parameters():
    """
    练习3: 灵活的参数设计 - 序列格式化器
    
    难度：⭐⭐ (初级)
    
    目标：学会设计带默认参数的函数
    类比：可调节参数的实验方案
    """
    print("\n🔬 练习3: 设计灵活的参数")
    print("-" * 40)
    print("目标: 创建可定制的序列格式化函数")
    print("就像可调节温度、时间的PCR程序\n")
    
    # TODO: 定义带默认参数的函数
    # def format_sequence_output(sequence, line_length=10, show_position=False):
    #     """
    #     格式化序列输出
    #     
    #     参数:
    #         sequence: DNA序列
    #         line_length: 每行字符数（默认10）
    #         show_position: 是否显示位置（默认False）
    #     
    #     像PCR程序的可调参数：
    #     - 退火温度（line_length）
    #     - 循环数（show_position）
    #     """
    #     # 将序列分成指定长度的片段
    #     
    #     # 如果show_position为True，添加位置编号
    #     
    #     # 返回格式化的字符串
    #     pass
    
    # 测试序列
    test_seq = "ATCGATCGATCGATCGATCG"
    
    print(f"原始序列: {test_seq}")
    print("\n不同参数的效果:")
    
    # TODO: 测试不同参数组合
    # print("1. 默认参数:")
    # print(format_sequence_output(test_seq))
    # 
    # print("\n2. 每行5个字符:")
    # print(format_sequence_output(test_seq, line_length=5))
    # 
    # print("\n3. 显示位置:")
    # print(format_sequence_output(test_seq, show_position=True))


def practice_4_function_refactoring():
    """
    练习4: 重构重复代码 - 多序列分析
    
    难度：⭐⭐⭐ (中级)
    
    目标：识别重复代码并重构为函数
    类比：标准化多个相似的实验步骤
    """
    print("\n🔬 练习4: 重构重复代码")
    print("-" * 40)
    print("目标: 将重复的分析代码重构为函数")
    print("就像标准化DNA/RNA/蛋白质的检测流程\n")
    
    # 原始代码（有重复）
    print("原始代码分析3个基因（代码重复）:")
    
    # 基因1分析
    gene1 = "ATCGATCGATCG"
    gene1_length = len(gene1)
    gene1_gc = (gene1.count('G') + gene1.count('C')) / gene1_length * 100
    gene1_at = (gene1.count('A') + gene1.count('T')) / gene1_length * 100
    print(f"基因1: 长度={gene1_length}, GC={gene1_gc:.1f}%, AT={gene1_at:.1f}%")
    
    # 基因2分析（重复代码）
    gene2 = "CGCGCGCGATAT"
    gene2_length = len(gene2)
    gene2_gc = (gene2.count('G') + gene2.count('C')) / gene2_length * 100
    gene2_at = (gene2.count('A') + gene2.count('T')) / gene2_length * 100
    print(f"基因2: 长度={gene2_length}, GC={gene2_gc:.1f}%, AT={gene2_at:.1f}%")
    
    # 基因3分析（又重复）
    gene3 = "ATATATATGCGC"
    gene3_length = len(gene3)
    gene3_gc = (gene3.count('G') + gene3.count('C')) / gene3_length * 100
    gene3_at = (gene3.count('A') + gene3.count('T')) / gene3_length * 100
    print(f"基因3: 长度={gene3_length}, GC={gene3_gc:.1f}%, AT={gene3_at:.1f}%")
    
    print("\n" + "="*40)
    print("TODO: 重构上面的代码")
    print("提示: 创建一个analyze_gene()函数")
    
    # TODO: 定义分析函数
    # def analyze_gene(sequence, gene_name):
    #     """
    #     分析单个基因
    #     
    #     将重复的分析步骤封装为标准流程
    #     """
    #     # 计算各项指标
    #     
    #     # 返回分析结果
    #     pass
    
    # TODO: 使用函数重构
    # genes = {
    #     "基因1": "ATCGATCGATCG",
    #     "基因2": "CGCGCGCGATAT",
    #     "基因3": "ATATATATGCGC"
    # }
    # 
    # print("\n重构后的代码:")
    # for name, seq in genes.items():
    #     result = analyze_gene(seq, name)
    #     # 打印结果


def practice_5_function_composition():
    """
    练习5: 函数组合 - 构建分析流水线
    
    难度：⭐⭐⭐ (中级)
    
    目标：学会组合多个简单函数
    类比：组装完整的实验流程
    """
    print("\n🔬 练习5: 组合函数构建流水线")
    print("-" * 40)
    print("目标: 用小函数组装完整分析流程")
    print("就像组合多个SOP完成复杂实验\n")
    
    # TODO: 定义基础函数（小SOP）
    
    # def validate_sequence(sequence):
    #     """步骤1: 验证序列"""
    #     # 检查是否只包含ATCG
    #     pass
    # 
    # def clean_sequence(sequence):
    #     """步骤2: 清理序列"""
    #     # 转大写，去除空格
    #     pass
    # 
    # def calculate_metrics(sequence):
    #     """步骤3: 计算指标"""
    #     # 计算长度、GC含量等
    #     pass
    # 
    # def generate_report(sequence, metrics):
    #     """步骤4: 生成报告"""
    #     # 格式化输出结果
    #     pass
    # 
    # def analyze_sequence_pipeline(raw_sequence):
    #     """
    #     完整的分析流水线
    #     组合所有步骤，像完整的实验方案
    #     """
    #     # 步骤1: 验证
    #     
    #     # 步骤2: 清理
    #     
    #     # 步骤3: 分析
    #     
    #     # 步骤4: 报告
    #     
    #     pass
    
    # 测试流水线
    test_sequences = [
        "ATCGATCG",
        " atcg atcg ",
        "ATCGXYZ"
    ]
    
    print("测试分析流水线:")
    for seq in test_sequences:
        print(f"\n输入: '{seq}'")
        # TODO: 运行流水线
        # result = analyze_sequence_pipeline(seq)
        # print(result)


def practice_6_advanced_function_design():
    """
    练习6: 高级函数设计 - ORF查找器
    
    难度：⭐⭐⭐⭐ (高级)
    
    目标：设计复杂的生物信息学函数
    类比：设计新的实验方法
    """
    print("\n🔬 练习6: 设计ORF查找器")
    print("-" * 40)
    print("目标: 创建查找开放阅读框的函数")
    print("就像开发新的基因检测方法\n")
    
    # TODO: 实现ORF查找器
    # def find_all_orfs(sequence, min_length=9):
    #     """
    #     查找所有可能的开放阅读框
    #     
    #     ORF定义:
    #     - 从ATG开始
    #     - 到终止密码子(TAA/TAG/TGA)结束
    #     - 长度是3的倍数
    #     - 最小长度min_length
    #     
    #     返回: ORF列表，每个包含起始位置、结束位置、序列
    #     """
    #     orfs = []
    #     sequence = sequence.upper()
    #     
    #     # 查找所有ATG
    #     
    #     # 对每个ATG，查找下游的终止密码子
    #     
    #     # 验证长度要求
    #     
    #     return orfs
    # 
    # def translate_orf(orf_sequence):
    #     """
    #     将ORF翻译为蛋白质序列
    #     
    #     使用简化的密码子表
    #     """
    #     # 简化的密码子表
    #     codon_table = {
    #         'ATG': 'M',  # 起始
    #         'TAA': '*', 'TAG': '*', 'TGA': '*',  # 终止
    #         'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # 丙氨酸
    #         'TGT': 'C', 'TGC': 'C',  # 半胱氨酸
    #         # ... 可以添加更多
    #     }
    #     
    #     # 翻译序列
    #     pass
    # 
    # def analyze_coding_potential(sequence):
    #     """
    #     综合分析序列的编码潜力
    #     
    #     组合ORF查找和翻译功能
    #     """
    #     # 查找ORF
    #     
    #     # 翻译每个ORF
    #     
    #     # 生成分析报告
    #     
    #     pass
    
    # 测试序列（包含ORF）
    test_sequence = "ATGAAATTTCCCTAAATGGGGTAG"
    
    print(f"分析序列: {test_sequence}")
    print(f"序列长度: {len(test_sequence)} bp")
    
    # TODO: 运行分析
    # orfs = find_all_orfs(test_sequence)
    # print(f"\n找到 {len(orfs)} 个ORF:")
    # for i, orf in enumerate(orfs, 1):
    #     print(f"  ORF{i}: 位置 {orf['start']}-{orf['end']}")
    #     print(f"        序列: {orf['sequence']}")
    #     # protein = translate_orf(orf['sequence'])
    #     # print(f"        蛋白: {protein}")


def practice_7_error_handling():
    """
    练习7: 错误处理 - 健壮的函数
    
    难度：⭐⭐⭐⭐ (高级)
    
    目标：设计能处理各种异常的函数
    类比：实验失败的应急预案
    """
    print("\n🔬 练习7: 添加错误处理")
    print("-" * 40)
    print("目标: 创建健壮的序列分析函数")
    print("就像实验SOP中的故障排除部分\n")
    
    # TODO: 实现带完整错误处理的函数
    # def robust_sequence_analyzer(sequence, analysis_type="basic"):
    #     """
    #     健壮的序列分析器
    #     
    #     能处理各种异常情况：
    #     - 空输入
    #     - 错误的数据类型
    #     - 无效的序列字符
    #     - 不支持的分析类型
    #     
    #     返回: (success, result_or_error)
    #     """
    #     try:
    #         # 检查输入类型
    #         
    #         # 检查是否为空
    #         
    #         # 验证序列
    #         
    #         # 根据分析类型执行分析
    #         if analysis_type == "basic":
    #             # 基础分析
    #             pass
    #         elif analysis_type == "advanced":
    #             # 高级分析
    #             pass
    #         else:
    #             # 不支持的类型
    #             pass
    #             
    #     except Exception as e:
    #         return False, str(e)
    
    # 测试各种异常情况
    test_cases = [
        ("ATCGATCG", "basic"),      # 正常
        ("", "basic"),               # 空序列
        (12345, "basic"),            # 错误类型
        ("ATCGXYZ", "basic"),        # 无效字符
        ("ATCGATCG", "unknown"),     # 未知分析类型
        (None, "basic"),             # None输入
    ]
    
    print("测试错误处理:")
    for sequence, analysis_type in test_cases:
        print(f"\n输入: {repr(sequence)}, 类型: {analysis_type}")
        # TODO: 调用函数并处理结果
        # success, result = robust_sequence_analyzer(sequence, analysis_type)
        # if success:
        #     print(f"  ✓ 成功: {result}")
        # else:
        #     print(f"  ✗ 错误: {result}")


def main():
    """
    主函数: 运行所有练习
    
    学习路径：
    1. 基础：定义简单函数
    2. 验证：添加输入检查
    3. 参数：设计灵活接口
    4. 重构：消除重复代码
    5. 组合：构建复杂功能
    6. 高级：实现专业工具
    7. 健壮：完善错误处理
    """
    print("🧬 Chapter 04: 函数 - 渐进式练习")
    print("像学习实验室SOP一样掌握函数编程")
    print("=" * 50)
    
    # 按难度递增运行练习
    practice_1_your_first_function()
    practice_2_function_with_validation()
    practice_3_function_with_parameters()
    practice_4_function_refactoring()
    practice_5_function_composition()
    practice_6_advanced_function_design()
    practice_7_error_handling()
    
    print("\n" + "=" * 50)
    print("🎯 练习完成路线图:")
    print("□ 练习1: 定义第一个函数（入门）")
    print("□ 练习2: 添加输入验证（初级）")
    print("□ 练习3: 设计参数接口（初级）")
    print("□ 练习4: 重构重复代码（中级）")
    print("□ 练习5: 组合函数功能（中级）")
    print("□ 练习6: 设计复杂函数（高级）")
    print("□ 练习7: 完善错误处理（高级）")
    
    print("\n📚 学习建议:")
    print("1. 从练习1开始，逐步完成")
    print("2. 每个练习都要运行测试")
    print("3. 对比参考答案学习最佳实践")
    print("4. 尝试改进和扩展功能")
    print("5. 将学到的技巧应用到实际项目")
    
    print("\n🧬 记住:")
    print("函数就像实验室的SOP，")
    print("好的函数让你的代码：")
    print("• 更易理解（清晰的名称）")
    print("• 更易维护（集中的逻辑）")
    print("• 更易测试（独立的单元）")
    print("• 更易复用（标准的接口）")


if __name__ == "__main__":
    main()