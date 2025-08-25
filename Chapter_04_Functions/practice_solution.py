#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 04: 函数练习参考答案

提供完整的函数实现，展示最佳实践：
- 清晰的函数设计
- 完善的错误处理  
- 详细的文档说明
- 实用的测试示例
"""


def solution_1_your_first_function():
    """
    练习1参考答案: AT含量计算函数
    
    学习要点：基本函数定义、参数和返回值
    """
    print("🔬 练习1参考答案: 创建第一个函数")
    print("=" * 50)
    
    def calculate_at_content(sequence):
        """
        计算DNA序列的AT含量
        
        参数:
            sequence (str): DNA序列
        
        返回:
            float: AT含量百分比
        """
        at_count = sequence.count('A') + sequence.count('T')
        return (at_count / len(sequence)) * 100
    
    # 测试函数
    test_sequences = [
        "ATCGATCG",     # 50% AT
        "AAAATTTT",     # 100% AT  
        "CCCCGGGG"      # 0% AT
    ]
    
    print("测试结果:")
    for seq in test_sequences:
        at_content = calculate_at_content(seq)
        print(f"  {seq}: AT含量 {at_content:.1f}%")
    
    print("\n✅ 学习要点:")
    print("• def关键字定义函数")
    print("• 使用描述性的函数名")
    print("• 参数接收输入数据")
    print("• return语句返回结果")
    print("• 文档字符串说明功能")


def solution_2_function_with_validation():
    """
    练习2参考答案: 带验证的安全函数
    
    学习要点：输入验证和边界条件处理
    """
    print("\n" + "=" * 50)
    print("🔬 练习2参考答案: 添加输入验证")
    print("=" * 50)
    
    def calculate_at_content_safe(sequence):
        """
        安全的AT含量计算器
        
        包含完整的输入验证和错误处理
        
        参数:
            sequence (str): DNA序列
        
        返回:
            float: AT含量百分比，如果输入无效返回-1
        """
        # 检查空序列
        if not sequence:
            return 0.0
        
        # 标准化：转为大写
        sequence = sequence.upper()
        
        # 验证序列只包含有效碱基
        valid_bases = set('ATCG')
        if not all(base in valid_bases for base in sequence):
            return -1  # 错误标识
        
        # 计算AT含量
        at_count = sequence.count('A') + sequence.count('T')
        return (at_count / len(sequence)) * 100
    
    # 测试各种输入情况
    test_cases = [
        ("ATCGATCG", "正常序列"),
        ("atcgatcg", "小写序列"),  
        ("", "空序列"),
        ("ATCGXYZ", "包含无效字符"),
        ("NNNNATCG", "包含N")
    ]
    
    print("测试结果:")
    for seq, description in test_cases:
        result = calculate_at_content_safe(seq)
        if result >= 0:
            print(f"  {description} '{seq}': AT含量 {result:.1f}%")
        else:
            print(f"  {description} '{seq}': ❌ 序列包含无效字符")
    
    print("\n✅ 学习要点:")
    print("• 输入验证是函数的重要组成部分")
    print("• 处理边界条件（空输入、无效数据）")
    print("• 使用错误码或异常表示错误状态")
    print("• 数据标准化（大小写转换）")


def solution_3_function_with_parameters():
    """
    练习3参考答案: 灵活的参数设计
    
    学习要点：默认参数、参数设计原则
    """
    print("\n" + "=" * 50)
    print("🔬 练习3参考答案: 设计灵活参数")
    print("=" * 50)
    
    def format_sequence_output(sequence, line_length=10, show_position=False):
        """
        格式化序列显示
        
        参数:
            sequence (str): DNA序列
            line_length (int): 每行显示的字符数，默认10
            show_position (bool): 是否显示位置编号，默认False
        
        返回:
            str: 格式化后的序列字符串
        """
        lines = []
        for i in range(0, len(sequence), line_length):
            line = sequence[i:i+line_length]
            if show_position:
                line = f"{i+1:3d}: {line}"
            lines.append(line)
        return '\n'.join(lines)
    
    # 测试不同参数组合
    test_seq = "ATCGATCGATCGATCGATCGATCG"
    
    print(f"原始序列: {test_seq}\n")
    
    # 测试1: 默认参数
    print("1. 默认参数（每行10字符）:")
    print(format_sequence_output(test_seq))
    
    # 测试2: 自定义行长度
    print("\n2. 每行5个字符:")
    print(format_sequence_output(test_seq, line_length=5))
    
    # 测试3: 显示位置
    print("\n3. 显示位置编号:")
    print(format_sequence_output(test_seq, show_position=True))
    
    # 测试4: 组合参数
    print("\n4. 每行8字符 + 显示位置:")
    print(format_sequence_output(test_seq, line_length=8, show_position=True))
    
    print("\n✅ 学习要点:")
    print("• 必需参数在前，可选参数在后")
    print("• 为可选参数提供合理的默认值")
    print("• 参数名要清晰表达含义")
    print("• 使用关键字参数增强可读性")


def solution_4_function_refactoring():
    """
    练习4参考答案: 重构重复代码
    
    学习要点：识别重复模式，提取公共逻辑
    """
    print("\n" + "=" * 50)
    print("🔬 练习4参考答案: 重构重复代码")
    print("=" * 50)
    
    def analyze_gene(sequence, gene_name):
        """
        分析单个基因的组成
        
        将重复的分析逻辑封装为函数
        
        参数:
            sequence (str): 基因序列
            gene_name (str): 基因名称
        
        返回:
            dict: 包含分析结果的字典
        """
        length = len(sequence)
        gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
        at_content = (sequence.count('A') + sequence.count('T')) / length * 100
        
        return {
            'name': gene_name,
            'length': length,
            'gc_content': gc_content,
            'at_content': at_content
        }
    
    # 使用函数分析多个基因
    genes = {
        "基因1": "ATCGATCGATCG",
        "基因2": "CGCGCGCGATAT", 
        "基因3": "ATATATATGCGC"
    }
    
    print("重构后的基因分析:")
    for name, sequence in genes.items():
        result = analyze_gene(sequence, name)
        print(f"{result['name']}: 长度={result['length']}, "
              f"GC={result['gc_content']:.1f}%, AT={result['at_content']:.1f}%")
    
    print("\n✅ 学习要点:")
    print("• 识别代码中的重复模式")
    print("• 提取公共逻辑为函数")
    print("• 函数名要表达清晰的意图")
    print("• 返回结构化数据（字典）")
    print("• 一次修改，处处生效")


def solution_5_function_composition():
    """
    练习5参考答案: 函数组合
    
    学习要点：模块化设计，函数协作
    """
    print("\n" + "=" * 50)
    print("🔬 练习5参考答案: 函数组合流水线")
    print("=" * 50)
    
    # 定义基础函数（小模块）
    def validate_sequence(sequence):
        """验证序列只包含有效碱基"""
        return all(b in 'ATCGN' for b in sequence.upper())
    
    def clean_sequence(sequence):
        """清理和标准化序列"""
        return sequence.strip().upper()
    
    def calculate_metrics(sequence):
        """计算序列的各项指标"""
        length = len(sequence)
        gc_content = (sequence.count('G') + sequence.count('C')) / length * 100 if length > 0 else 0
        n_count = sequence.count('N')
        
        return {
            'length': length,
            'gc_content': gc_content,
            'n_count': n_count,
            'quality': 'good' if n_count == 0 else 'poor'
        }
    
    def generate_report(sequence, metrics):
        """生成格式化的分析报告"""
        return (f"序列分析报告:\n"
                f"  原序列: {sequence}\n"
                f"  长度: {metrics['length']} bp\n"
                f"  GC含量: {metrics['gc_content']:.1f}%\n"
                f"  N碱基: {metrics['n_count']} 个\n"
                f"  质量评估: {metrics['quality']}")
    
    def analyze_sequence_pipeline(raw_sequence):
        """
        完整的序列分析流水线
        
        组合多个基础函数完成复杂任务
        """
        # 步骤1: 验证输入
        if not validate_sequence(raw_sequence):
            return "❌ 错误: 序列包含无效字符"
        
        # 步骤2: 清理数据
        clean_seq = clean_sequence(raw_sequence)
        
        # 步骤3: 计算指标
        metrics = calculate_metrics(clean_seq)
        
        # 步骤4: 生成报告
        return generate_report(clean_seq, metrics)
    
    # 测试流水线
    test_sequences = [
        "ATCGATCGATCG",     # 正常序列
        " atcg atcg ",       # 需要清理
        "ATCGNNNATCG",      # 包含N
        "ATCGXYZ"           # 无效字符
    ]
    
    print("测试分析流水线:")
    for seq in test_sequences:
        print(f"\n输入: '{seq}'")
        result = analyze_sequence_pipeline(seq)
        print(result)
    
    print("\n✅ 学习要点:")
    print("• 将复杂功能分解为小函数")
    print("• 每个函数专注单一任务") 
    print("• 函数之间通过参数和返回值协作")
    print("• 流水线式的数据处理")
    print("• 模块化便于测试和维护")


def solution_6_advanced_function_design():
    """
    练习6参考答案: 高级函数设计
    
    学习要点：复杂算法实现，数据结构设计
    """
    print("\n" + "=" * 50)
    print("🔬 练习6参考答案: ORF查找器")
    print("=" * 50)
    
    def find_all_orfs(sequence, min_length=9):
        """
        查找序列中的所有开放阅读框
        
        参数:
            sequence (str): DNA序列
            min_length (int): ORF最小长度，默认9bp
        
        返回:
            list: ORF信息列表
        """
        orfs = []
        sequence = sequence.upper()
        stop_codons = ['TAA', 'TAG', 'TGA']
        
        # 遍历每个可能的起始位置
        for i in range(len(sequence) - 2):
            if sequence[i:i+3] == 'ATG':  # 找到起始密码子
                # 寻找同框终止密码子
                for j in range(i + 3, len(sequence), 3):
                    if j + 2 < len(sequence):
                        codon = sequence[j:j+3]
                        if codon in stop_codons:
                            orf_length = j + 3 - i
                            if orf_length >= min_length:
                                orfs.append({
                                    'start': i + 1,  # 1-based位置
                                    'end': j + 3,
                                    'length': orf_length,
                                    'sequence': sequence[i:j+3]
                                })
                            break  # 找到终止密码子就停止
        
        return orfs
    
    def translate_orf(orf_sequence):
        """
        翻译ORF为氨基酸序列
        
        参数:
            orf_sequence (str): ORF的DNA序列
        
        返回:
            str: 氨基酸序列
        """
        # 简化的密码子表
        codon_table = {
            'ATG': 'M',  # 甲硫氨酸（起始）
            'TAA': '*', 'TAG': '*', 'TGA': '*',  # 终止
            'TTT': 'F', 'TTC': 'F',  # 苯丙氨酸
            'TTA': 'L', 'TTG': 'L',  # 亮氨酸
            'TCT': 'S', 'TCC': 'S',  # 丝氨酸
            'AAA': 'K', 'AAG': 'K',  # 赖氨酸
            'CCC': 'P', 'CCG': 'P',  # 脯氨酸
            'GGG': 'G', 'GGA': 'G'   # 甘氨酸
        }
        
        protein = ""
        for i in range(0, len(orf_sequence), 3):
            codon = orf_sequence[i:i+3]
            if len(codon) == 3:
                aa = codon_table.get(codon, 'X')  # X表示未知氨基酸
                protein += aa
                if aa == '*':  # 遇到终止密码子
                    break
        
        return protein
    
    # 测试ORF查找和翻译
    test_sequence = "ATGTTCTTATTGTAAATGCCCCCGGGTAG"
    
    print(f"分析序列: {test_sequence}")
    print(f"序列长度: {len(test_sequence)} bp")
    
    # 查找所有ORF
    orfs = find_all_orfs(test_sequence, min_length=6)
    
    print(f"\n找到 {len(orfs)} 个ORF:")
    for i, orf in enumerate(orfs, 1):
        protein = translate_orf(orf['sequence'])
        print(f"  ORF{i}: 位置 {orf['start']}-{orf['end']} ({orf['length']}bp)")
        print(f"        DNA: {orf['sequence']}")
        print(f"        蛋白质: {protein}")
    
    print("\n✅ 学习要点:")
    print("• 复杂算法的模块化分解")
    print("• 合理的数据结构设计")
    print("• 清晰的变量命名和注释")
    print("• 边界条件的仔细处理")
    print("• 生物学专业知识的编程实现")


def solution_7_error_handling():
    """
    练习7参考答案: 完善的错误处理
    
    学习要点：异常处理，健壮性设计
    """
    print("\n" + "=" * 50)
    print("🔬 练习7参考答案: 健壮的函数设计")
    print("=" * 50)
    
    def robust_sequence_analyzer(sequence, analysis_type="basic"):
        """
        健壮的序列分析器
        
        能优雅处理各种异常情况
        
        参数:
            sequence: DNA序列（任意类型）
            analysis_type (str): 分析类型
        
        返回:
            tuple: (成功标志, 结果或错误信息)
        """
        try:
            # 类型检查
            if sequence is None:
                raise ValueError("序列不能为None")
            
            if not isinstance(sequence, str):
                raise TypeError(f"序列必须是字符串，得到 {type(sequence).__name__}")
            
            # 空值检查
            if not sequence:
                raise ValueError("序列不能为空")
            
            # 序列验证和清理
            sequence = sequence.strip().upper()
            valid_bases = set('ATCGN')
            invalid_bases = set(sequence) - valid_bases
            
            if invalid_bases:
                raise ValueError(f"序列包含无效字符: {', '.join(sorted(invalid_bases))}")
            
            # 根据分析类型执行分析
            if analysis_type == "basic":
                if len(sequence) == 0:
                    raise ValueError("清理后的序列为空")
                
                gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
                return True, f"基础分析完成 - GC含量: {gc_content:.1f}%"
                
            elif analysis_type == "advanced":
                length = len(sequence)
                gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
                n_count = sequence.count('N')
                
                quality = "优秀" if n_count == 0 else "良好" if n_count < length * 0.1 else "较差"
                
                result = (f"高级分析完成:\n"
                         f"  长度: {length} bp\n"
                         f"  GC含量: {gc_content:.1f}%\n"
                         f"  N碱基: {n_count} 个\n"
                         f"  质量评估: {quality}")
                
                return True, result
                
            else:
                raise ValueError(f"不支持的分析类型: '{analysis_type}'，"
                               f"支持的类型: 'basic', 'advanced'")
                
        except (ValueError, TypeError) as e:
            return False, f"输入错误: {str(e)}"
        except Exception as e:
            return False, f"未知错误: {str(e)}"
    
    # 测试各种异常情况
    test_cases = [
        ("ATCGATCGATCG", "basic", "正常序列"),
        ("", "basic", "空序列"),
        (None, "basic", "None输入"),
        (12345, "basic", "数字输入"),
        ("ATCGXYZ", "basic", "无效字符"),
        ("  atcg  ", "basic", "需要清理的序列"),
        ("ATCGATCG", "advanced", "高级分析"),
        ("ATCGATCG", "unknown", "未知分析类型"),
        ("NNNNATCGNNN", "advanced", "包含N的序列"),
    ]
    
    print("测试错误处理:")
    for i, (sequence, analysis_type, description) in enumerate(test_cases, 1):
        print(f"\n{i}. {description}")
        print(f"   输入: {repr(sequence)}, 类型: '{analysis_type}'")
        
        success, result = robust_sequence_analyzer(sequence, analysis_type)
        
        if success:
            print(f"   ✅ 成功: {result}")
        else:
            print(f"   ❌ 失败: {result}")
    
    print("\n✅ 学习要点:")
    print("• 全面的输入验证（类型、值、格式）")
    print("• 使用try-except捕获和处理异常")
    print("• 返回标准化的结果格式")
    print("• 提供清晰有用的错误信息")
    print("• 区分不同类型的错误")
    print("• 优雅降级而不是崩溃")


def main():
    """
    运行所有练习的参考答案
    
    展示函数编程的完整学习路径
    """
    print("🧬 Chapter 04: 函数练习 - 完整参考答案")
    print("展示函数编程的最佳实践和设计模式")
    print("=" * 60)
    
    # 运行所有答案演示
    solution_1_your_first_function()
    solution_2_function_with_validation()
    solution_3_function_with_parameters()
    solution_4_function_refactoring()
    solution_5_function_composition()
    solution_6_advanced_function_design()
    solution_7_error_handling()
    
    # 总结
    print("\n" + "=" * 60)
    print("📚 函数编程核心总结")
    print("=" * 60)
    
    print("\n🎯 设计原则:")
    print("• 单一职责 - 一个函数做一件事")
    print("• 清晰命名 - 函数名表达明确意图") 
    print("• 合理参数 - 必需在前，可选在后")
    print("• 完善文档 - 说明功能、参数、返回值")
    print("• 错误处理 - 验证输入，处理异常")
    
    print("\n🔧 实现技巧:")
    print("• 输入验证和数据清理")
    print("• 返回结构化数据（字典、元组）")
    print("• 使用默认参数提高灵活性")
    print("• 模块化设计便于测试维护")
    print("• 函数组合构建复杂功能")
    
    print("\n🧬 生物信息学应用:")
    print("• 序列分析和质量控制")
    print("• 基因注释和功能预测")
    print("• 数据格式转换和标准化")
    print("• 生物学算法的模块化实现")
    print("• 分析流水线的自动化")
    
    print("\n🎉 学习成果:")
    print("通过这些练习，你已经掌握了：")
    print("✅ 函数的基本定义和使用")
    print("✅ 参数设计和默认值设置")
    print("✅ 输入验证和错误处理")
    print("✅ 代码重构和模块化思维")
    print("✅ 函数组合和流水线设计")
    print("✅ 复杂生物学算法的实现")
    print("✅ 健壮软件的设计原则")
    
    print(f"\n💡 记住：函数是编程的基石")
    print("好的函数设计让代码：更清晰、更可靠、更易维护！")


if __name__ == "__main__":
    main()