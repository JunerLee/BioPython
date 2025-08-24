#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 04: 函数 - 渐进式练习参考答案

完整的参考答案，展示函数设计的最佳实践。
每个练习都包含详细的注释和解释。
"""


def practice_1_your_first_function():
    """
    练习1答案: 你的第一个函数 - AT含量计算
    
    学习要点：
    - 使用def定义函数
    - 接收参数
    - 返回计算结果
    """
    print("🔬 练习1答案: 创建你的第一个函数")
    print("-" * 40)
    
    def calculate_at_content(sequence):
        """
        计算DNA序列的AT含量
        
        这是你的第一个"实验室SOP"：
        1. 接收DNA样品（sequence参数）
        2. 计数A和T碱基
        3. 计算百分比
        4. 返回结果
        """
        # 步骤1: 统计A的数量
        a_count = sequence.count('A')
        
        # 步骤2: 统计T的数量
        t_count = sequence.count('T')
        
        # 步骤3: 计算总长度
        total_length = len(sequence)
        
        # 步骤4: 计算百分比并返回
        if total_length == 0:  # 避免除零错误
            return 0.0
        
        at_content = (a_count + t_count) / total_length * 100
        return at_content
    
    # 测试函数
    test_sequences = [
        "ATCGATCG",     # 50% AT
        "AAAATTTT",     # 100% AT
        "CCCCGGGG"      # 0% AT
    ]
    
    print("测试序列:")
    for seq in test_sequences:
        at_content = calculate_at_content(seq)
        print(f"  {seq}")
        print(f"    AT含量: {at_content:.1f}%")
    
    print("\n✓ 关键点:")
    print("• 函数名清晰表达功能")
    print("• 参数名有意义")
    print("• 包含文档字符串")
    print("• 处理了边界情况（空序列）")


def practice_2_function_with_validation():
    """
    练习2答案: 带验证的函数
    
    学习要点：
    - 输入验证
    - 数据标准化
    - 错误处理
    """
    print("\n🔬 练习2答案: 添加输入验证")
    print("-" * 40)
    
    def calculate_at_content_safe(sequence):
        """
        安全的AT含量计算器
        
        包含质控步骤：
        1. 检查输入是否为空
        2. 转换为大写（标准化）
        3. 验证是否只包含ATCG
        4. 计算并返回结果
        """
        # 质控步骤1: 检查是否为空
        if not sequence:
            return 0.0
        
        # 质控步骤2: 标准化（转大写）
        sequence = sequence.upper()
        
        # 质控步骤3: 验证碱基
        valid_bases = set('ATCG')
        for base in sequence:
            if base not in valid_bases:
                return -1.0  # 返回-1表示错误
        
        # 计算AT含量
        a_count = sequence.count('A')
        t_count = sequence.count('T')
        at_content = (a_count + t_count) / len(sequence) * 100
        
        return at_content
    
    # 测试各种输入
    test_cases = [
        "ATCGATCG",     # 正常
        "atcgatcg",     # 小写
        "",             # 空序列
        "ATCGXYZ"       # 包含无效字符
    ]
    
    print("测试带验证的函数:")
    for seq in test_cases:
        result = calculate_at_content_safe(seq)
        print(f"  输入: '{seq}'")
        if result >= 0:
            print(f"    AT含量: {result:.1f}%")
        else:
            print(f"    错误: 序列包含无效字符")
    
    print("\n✓ 关键点:")
    print("• 验证输入的有效性")
    print("• 标准化数据（转大写）")
    print("• 使用特殊返回值表示错误")
    print("• 清晰的错误提示")


def practice_3_function_with_parameters():
    """
    练习3答案: 灵活的参数设计
    
    学习要点：
    - 默认参数
    - 可选功能
    - 参数组合
    """
    print("\n🔬 练习3答案: 设计灵活的参数")
    print("-" * 40)
    
    def format_sequence_output(sequence, line_length=10, show_position=False):
        """
        格式化序列输出
        
        参数:
            sequence: DNA序列
            line_length: 每行字符数（默认10）
            show_position: 是否显示位置（默认False）
        """
        if not sequence:
            return ""
        
        lines = []
        
        # 将序列分成指定长度的片段
        for i in range(0, len(sequence), line_length):
            line = sequence[i:i+line_length]
            
            # 如果show_position为True，添加位置编号
            if show_position:
                line = f"{i+1:4d}: {line}"
            
            lines.append(line)
        
        # 返回格式化的字符串
        return '\n'.join(lines)
    
    # 测试序列
    test_seq = "ATCGATCGATCGATCGATCG"
    
    print(f"原始序列: {test_seq}")
    print("\n不同参数的效果:")
    
    print("\n1. 默认参数:")
    print(format_sequence_output(test_seq))
    
    print("\n2. 每行5个字符:")
    print(format_sequence_output(test_seq, line_length=5))
    
    print("\n3. 显示位置:")
    print(format_sequence_output(test_seq, show_position=True))
    
    print("\n4. 组合参数:")
    print(format_sequence_output(test_seq, line_length=5, show_position=True))
    
    print("\n✓ 关键点:")
    print("• 合理的默认值")
    print("• 参数命名清晰")
    print("• 功能可组合")
    print("• 保持函数简单")


def practice_4_function_refactoring():
    """
    练习4答案: 重构重复代码
    
    学习要点：
    - 识别重复模式
    - 提取共同逻辑
    - 数据驱动设计
    """
    print("\n🔬 练习4答案: 重构重复代码")
    print("-" * 40)
    
    def analyze_gene(sequence, gene_name):
        """
        分析单个基因
        
        将重复的分析步骤封装为标准流程
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
    
    # 使用函数重构
    genes = {
        "基因1": "ATCGATCGATCG",
        "基因2": "CGCGCGCGATAT",
        "基因3": "ATATATATGCGC"
    }
    
    print("重构前: 代码重复3次")
    print("重构后: 使用函数消除重复\n")
    
    print("分析结果:")
    for name, seq in genes.items():
        result = analyze_gene(seq, name)
        print(f"{result['name']}: "
              f"长度={result['length']}, "
              f"GC={result['gc_content']:.1f}%, "
              f"AT={result['at_content']:.1f}%")
    
    # 展示函数的可扩展性
    print("\n扩展功能（添加新基因）:")
    new_gene = analyze_gene("GCGCGCGCATAT", "基因4")
    print(f"{new_gene['name']}: "
          f"长度={new_gene['length']}, "
          f"GC={new_gene['gc_content']:.1f}%, "
          f"AT={new_gene['at_content']:.1f}%")
    
    print("\n✓ 关键点:")
    print("• 消除了代码重复")
    print("• 逻辑集中管理")
    print("• 易于添加新数据")
    print("• 返回结构化数据")


def practice_5_function_composition():
    """
    练习5答案: 函数组合
    
    学习要点：
    - 单一职责
    - 函数组合
    - 流水线设计
    """
    print("\n🔬 练习5答案: 组合函数构建流水线")
    print("-" * 40)
    
    def validate_sequence(sequence):
        """步骤1: 验证序列"""
        if not sequence:
            return False
        valid_bases = set('ATCG')
        return all(base.upper() in valid_bases for base in sequence)
    
    def clean_sequence(sequence):
        """步骤2: 清理序列"""
        # 去除空格，转大写
        return sequence.replace(' ', '').upper()
    
    def calculate_metrics(sequence):
        """步骤3: 计算指标"""
        length = len(sequence)
        gc_count = sequence.count('G') + sequence.count('C')
        at_count = sequence.count('A') + sequence.count('T')
        
        return {
            'length': length,
            'gc_content': (gc_count / length * 100) if length > 0 else 0,
            'at_content': (at_count / length * 100) if length > 0 else 0,
            'base_counts': {
                'A': sequence.count('A'),
                'T': sequence.count('T'),
                'C': sequence.count('C'),
                'G': sequence.count('G')
            }
        }
    
    def generate_report(sequence, metrics):
        """步骤4: 生成报告"""
        report = []
        report.append(f"序列: {sequence[:20]}..." if len(sequence) > 20 else f"序列: {sequence}")
        report.append(f"长度: {metrics['length']} bp")
        report.append(f"GC含量: {metrics['gc_content']:.1f}%")
        report.append(f"AT含量: {metrics['at_content']:.1f}%")
        report.append(f"碱基分布: A={metrics['base_counts']['A']}, "
                     f"T={metrics['base_counts']['T']}, "
                     f"C={metrics['base_counts']['C']}, "
                     f"G={metrics['base_counts']['G']}")
        return '\n  '.join(report)
    
    def analyze_sequence_pipeline(raw_sequence):
        """
        完整的分析流水线
        组合所有步骤，像完整的实验方案
        """
        # 步骤1: 清理
        cleaned = clean_sequence(raw_sequence)
        
        # 步骤2: 验证
        if not validate_sequence(cleaned):
            return f"错误: 序列 '{raw_sequence}' 包含无效字符"
        
        # 步骤3: 分析
        metrics = calculate_metrics(cleaned)
        
        # 步骤4: 报告
        report = generate_report(cleaned, metrics)
        
        return f"分析成功:\n  {report}"
    
    # 测试流水线
    test_sequences = [
        "ATCGATCG",
        " atcg atcg ",
        "ATCGXYZ"
    ]
    
    print("测试分析流水线:")
    for seq in test_sequences:
        print(f"\n输入: '{seq}'")
        result = analyze_sequence_pipeline(seq)
        print(result)
    
    print("\n✓ 关键点:")
    print("• 每个函数一个职责")
    print("• 函数按顺序组合")
    print("• 清晰的数据流")
    print("• 易于调试和测试")


def practice_6_advanced_function_design():
    """
    练习6答案: 高级函数设计
    
    学习要点：
    - 复杂算法实现
    - 数据结构设计
    - 函数协作
    """
    print("\n🔬 练习6答案: 设计ORF查找器")
    print("-" * 40)
    
    def find_all_orfs(sequence, min_length=9):
        """
        查找所有可能的开放阅读框
        
        ORF定义:
        - 从ATG开始
        - 到终止密码子(TAA/TAG/TGA)结束
        - 长度是3的倍数
        - 最小长度min_length
        """
        orfs = []
        sequence = sequence.upper()
        stop_codons = {'TAA', 'TAG', 'TGA'}
        
        # 查找所有ATG位置
        for i in range(len(sequence) - 2):
            if sequence[i:i+3] == 'ATG':
                # 从ATG开始，查找终止密码子
                for j in range(i + 3, len(sequence) - 2, 3):
                    codon = sequence[j:j+3]
                    if codon in stop_codons:
                        orf_length = j + 3 - i
                        if orf_length >= min_length:
                            orfs.append({
                                'start': i,
                                'end': j + 3,
                                'length': orf_length,
                                'sequence': sequence[i:j+3]
                            })
                        break  # 找到第一个终止密码子即停止
        
        return orfs
    
    def translate_orf(orf_sequence):
        """
        将ORF翻译为蛋白质序列
        
        使用简化的密码子表
        """
        # 简化的密码子表
        codon_table = {
            'ATG': 'M',  # 甲硫氨酸（起始）
            'TAA': '*', 'TAG': '*', 'TGA': '*',  # 终止
            'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # 丙氨酸
            'TGT': 'C', 'TGC': 'C',  # 半胱氨酸
            'GAT': 'D', 'GAC': 'D',  # 天冬氨酸
            'GAA': 'E', 'GAG': 'E',  # 谷氨酸
            'TTT': 'F', 'TTC': 'F',  # 苯丙氨酸
            'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',  # 甘氨酸
            'AAA': 'K', 'AAG': 'K',  # 赖氨酸
            'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',  # 亮氨酸
            'AAT': 'N', 'AAC': 'N',  # 天冬酰胺
            'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # 脯氨酸
            'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',  # 丝氨酸
            'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # 苏氨酸
        }
        
        protein = []
        for i in range(0, len(orf_sequence), 3):
            codon = orf_sequence[i:i+3]
            if len(codon) == 3:
                amino_acid = codon_table.get(codon, 'X')  # X表示未知
                protein.append(amino_acid)
        
        return ''.join(protein)
    
    def analyze_coding_potential(sequence):
        """
        综合分析序列的编码潜力
        """
        orfs = find_all_orfs(sequence)
        
        analysis = {
            'sequence_length': len(sequence),
            'orf_count': len(orfs),
            'orfs': []
        }
        
        for orf in orfs:
            protein = translate_orf(orf['sequence'])
            analysis['orfs'].append({
                'position': f"{orf['start']}-{orf['end']}",
                'length': orf['length'],
                'protein': protein,
                'protein_length': len(protein.replace('*', ''))
            })
        
        return analysis
    
    # 测试序列（包含多个ORF）
    test_sequence = "ATGAAATTTCCCTAAATGGGGTAG"
    
    print(f"分析序列: {test_sequence}")
    print(f"序列长度: {len(test_sequence)} bp")
    
    # 运行分析
    orfs = find_all_orfs(test_sequence)
    print(f"\n找到 {len(orfs)} 个ORF:")
    
    for i, orf in enumerate(orfs, 1):
        protein = translate_orf(orf['sequence'])
        print(f"  ORF{i}:")
        print(f"    位置: {orf['start']}-{orf['end']}")
        print(f"    长度: {orf['length']} bp")
        print(f"    序列: {orf['sequence']}")
        print(f"    蛋白: {protein}")
    
    # 综合分析
    print("\n综合分析:")
    result = analyze_coding_potential(test_sequence)
    print(f"  总ORF数: {result['orf_count']}")
    if result['orfs']:
        print(f"  最长ORF: {max(orf['length'] for orf in result['orfs'])} bp")
    
    print("\n✓ 关键点:")
    print("• 实现了复杂的生物学算法")
    print("• 合理的数据结构设计")
    print("• 函数之间良好协作")
    print("• 返回详细的分析结果")


def practice_7_error_handling():
    """
    练习7答案: 完善的错误处理
    
    学习要点：
    - 异常处理
    - 输入验证
    - 错误报告
    """
    print("\n🔬 练习7答案: 添加错误处理")
    print("-" * 40)
    
    def robust_sequence_analyzer(sequence, analysis_type="basic"):
        """
        健壮的序列分析器
        
        能处理各种异常情况
        """
        try:
            # 检查输入类型
            if sequence is None:
                return False, "错误: 序列为None"
            
            if not isinstance(sequence, str):
                return False, f"错误: 序列必须是字符串，得到{type(sequence).__name__}"
            
            # 检查是否为空
            if not sequence.strip():
                return False, "错误: 序列为空"
            
            # 标准化序列
            sequence = sequence.upper().strip()
            
            # 验证序列
            valid_bases = set('ATCGN')
            invalid_bases = set(sequence) - valid_bases
            if invalid_bases:
                return False, f"错误: 序列包含无效字符 {invalid_bases}"
            
            # 根据分析类型执行分析
            if analysis_type == "basic":
                # 基础分析
                length = len(sequence)
                gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
                at_content = (sequence.count('A') + sequence.count('T')) / length * 100
                
                result = {
                    'type': 'basic',
                    'length': length,
                    'gc_content': round(gc_content, 1),
                    'at_content': round(at_content, 1)
                }
                return True, result
                
            elif analysis_type == "advanced":
                # 高级分析
                orfs = find_all_orfs(sequence)
                result = {
                    'type': 'advanced',
                    'length': len(sequence),
                    'orf_count': len(orfs),
                    'has_coding_potential': len(orfs) > 0
                }
                return True, result
                
            else:
                return False, f"错误: 不支持的分析类型 '{analysis_type}'"
                
        except Exception as e:
            return False, f"未预期的错误: {str(e)}"
    
    # 测试各种异常情况
    test_cases = [
        ("ATCGATCG", "basic"),      # 正常
        ("", "basic"),               # 空序列
        (12345, "basic"),            # 错误类型
        ("ATCGXYZ", "basic"),        # 无效字符
        ("ATCGATCG", "unknown"),     # 未知分析类型
        (None, "basic"),             # None输入
        ("ATGATGTAG", "advanced"),   # 高级分析
    ]
    
    print("测试错误处理:")
    for sequence, analysis_type in test_cases:
        print(f"\n输入: {repr(sequence)}, 类型: {analysis_type}")
        success, result = robust_sequence_analyzer(sequence, analysis_type)
        if success:
            print(f"  ✓ 成功: {result}")
        else:
            print(f"  ✗ {result}")
    
    print("\n✓ 关键点:")
    print("• 完整的输入验证")
    print("• 清晰的错误信息")
    print("• 使用try-except捕获异常")
    print("• 返回成功/失败状态")


def main():
    """
    主函数: 运行所有练习答案
    
    展示函数设计的完整学习路径
    """
    print("🧬 Chapter 04: 函数 - 渐进式练习参考答案")
    print("完整展示从基础到高级的函数设计")
    print("=" * 60)
    
    # 按难度递增运行答案
    practice_1_your_first_function()
    practice_2_function_with_validation()
    practice_3_function_with_parameters()
    practice_4_function_refactoring()
    practice_5_function_composition()
    practice_6_advanced_function_design()
    practice_7_error_handling()
    
    print("\n" + "=" * 60)
    print("📚 函数设计总结:")
    print("\n基础原则:")
    print("1. 单一职责 - 每个函数只做一件事")
    print("2. 清晰命名 - 函数名表达其功能")
    print("3. 文档完整 - 包含docstring说明")
    print("4. 参数合理 - 数量适中，有默认值")
    print("5. 返回一致 - 返回值类型稳定")
    
    print("\n进阶技巧:")
    print("1. 输入验证 - 检查参数有效性")
    print("2. 错误处理 - 优雅处理异常")
    print("3. 函数组合 - 小函数构建大功能")
    print("4. 代码重构 - 消除重复，提取函数")
    print("5. 测试驱动 - 先写测试，再写代码")
    
    print("\n🎯 最佳实践:")
    print("• 从简单开始，逐步改进")
    print("• 保持函数短小精悍（<20行）")
    print("• 避免副作用，保持纯函数")
    print("• 编写可测试的代码")
    print("• 持续重构和优化")
    
    print("\n🧬 应用建议:")
    print("将这些函数设计原则应用到你的生物信息学项目中，")
    print("构建可靠、可维护、可扩展的分析工具。")
    print("\n记住：好的函数就像精心设计的实验室SOP，")
    print("让复杂的分析变得简单、可靠、可重复！")


if __name__ == "__main__":
    main()