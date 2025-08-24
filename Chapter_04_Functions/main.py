#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 04: 函数 - 实验室的标准操作流程(SOP)

本章将函数比作实验室的SOP，展示如何：
1. 识别重复代码并重构为函数
2. 设计清晰的函数接口
3. 构建层次化的函数库
4. 实现健壮的错误处理
5. 组合简单函数完成复杂任务
"""


def demonstrate_why_we_need_functions():
    """
    演示为什么需要函数 - 通过对比重复代码和函数化代码
    """
    print("🔬 为什么需要函数？")
    print("=" * 50)
    
    print("\n场景：分析多个基因的GC含量")
    print("-" * 40)
    
    # 方法1：不使用函数（重复代码）
    print("\n❌ 不使用函数的代码（重复且易错）：")
    
    # 基因1
    gene1 = "ATCGATCGATCG"
    gc_count1 = gene1.count('G') + gene1.count('C')
    gc_content1 = (gc_count1 / len(gene1)) * 100
    print(f"基因1: {gene1}")
    print(f"  GC含量: {gc_content1:.1f}%")
    
    # 基因2（重复相同代码）
    gene2 = "CGCGCGCGATAT"
    gc_count2 = gene2.count('G') + gene2.count('C')
    gc_content2 = (gc_count2 / len(gene2)) * 100
    print(f"基因2: {gene2}")
    print(f"  GC含量: {gc_content2:.1f}%")
    
    # 基因3（又重复一次）
    gene3 = "ATATATATGCGC"
    gc_count3 = gene3.count('G') + gene3.count('C')
    gc_content3 = (gc_count3 / len(gene3)) * 100
    print(f"基因3: {gene3}")
    print(f"  GC含量: {gc_content3:.1f}%")
    
    print("\n问题：")
    print("• 代码重复3次")
    print("• 修改算法需要改3个地方")
    print("• 容易出错（复制粘贴可能遗漏）")
    print("• 代码冗长，可读性差")
    
    # 方法2：使用函数
    print("\n✅ 使用函数的代码（简洁且可维护）：")
    
    def calculate_gc_content(sequence):
        """计算DNA序列的GC含量 - 标准操作流程(SOP)"""
        gc_count = sequence.count('G') + sequence.count('C')
        return (gc_count / len(sequence)) * 100
    
    # 使用函数处理相同的数据
    genes = {
        "基因1": "ATCGATCGATCG",
        "基因2": "CGCGCGCGATAT",
        "基因3": "ATATATATGCGC"
    }
    
    for name, sequence in genes.items():
        gc = calculate_gc_content(sequence)
        print(f"{name}: {sequence}")
        print(f"  GC含量: {gc:.1f}%")
    
    print("\n优势：")
    print("• 代码只写一次，多次复用")
    print("• 修改算法只需改一个地方")
    print("• 减少错误，提高一致性")
    print("• 代码简洁，意图清晰")


def demonstrate_function_anatomy():
    """
    详细解析函数的结构 - 类比实验室SOP
    """
    print("\n\n🔬 函数的完整结构（类比实验室SOP）")
    print("=" * 50)
    
    # 展示一个完整的函数定义
    def extract_dna(sample_id, volume_ml=1.0, method="column"):
        """
        DNA提取函数 - 完整的SOP示例
        
        这就像实验室的DNA提取SOP：
        - 函数名(extract_dna) = SOP名称
        - 参数(sample_id等) = 所需材料
        - 文档字符串 = 实验原理和步骤
        - 函数体 = 具体操作
        - 返回值 = 实验产物
        
        Args:
            sample_id (str): 样品编号（必需参数）
            volume_ml (float): 样品体积，默认1.0ml（可选参数）
            method (str): 提取方法，默认"column"（可选参数）
        
        Returns:
            dict: 包含DNA浓度和纯度的字典
        """
        # 函数体 - 实际的"实验步骤"
        print(f"\n执行DNA提取SOP:")
        print(f"1. 样品准备: {sample_id}, {volume_ml}ml")
        print(f"2. 提取方法: {method}")
        print(f"3. 加入裂解液...")
        print(f"4. 离心分离...")
        print(f"5. 纯化DNA...")
        
        # 模拟返回结果
        result = {
            'sample_id': sample_id,
            'concentration': 150.5,  # ng/μl
            'purity': 1.85,  # A260/A280
            'volume': volume_ml * 50  # 最终体积
        }
        
        return result
    
    # 调用函数 - 就像执行SOP
    print("\n调用函数（执行SOP）:")
    result = extract_dna("SAMPLE_001", volume_ml=2.0)
    print(f"\n提取结果: {result}")
    
    # 使用默认参数
    print("\n使用默认参数:")
    result2 = extract_dna("SAMPLE_002")  # 使用默认volume和method
    print(f"结果: {result2}")
    
    print("\n函数结构要点:")
    print("1. def关键字 - 定义函数的开始")
    print("2. 函数名 - 描述性的动词或动词短语")
    print("3. 参数 - 必需参数在前，可选参数（有默认值）在后")
    print("4. 文档字符串 - 函数的使用说明书")
    print("5. 函数体 - 缩进的代码块")
    print("6. return语句 - 返回结果给调用者")


def demonstrate_refactoring_process():
    """
    展示从重复代码到函数的重构过程
    """
    print("\n\n🔬 重构过程：从重复代码到函数")
    print("=" * 50)
    
    print("\n第一步：识别重复模式")
    print("-" * 40)
    
    print("原始代码（有重复）:")
    print("""
    # 验证序列1
    seq1 = "ATCGATCG"
    valid1 = all(b in 'ATCG' for b in seq1.upper())
    
    # 验证序列2（重复）
    seq2 = "ATCGXYZ"
    valid2 = all(b in 'ATCG' for b in seq2.upper())
    
    # 验证序列3（又重复）
    seq3 = "atcgatcg"
    valid3 = all(b in 'ATCG' for b in seq3.upper())
    """)
    
    print("\n第二步：提取共同逻辑")
    print("-" * 40)
    
    print("识别的重复模式:")
    print("• 转换为大写: sequence.upper()")
    print("• 检查每个字符: all(b in 'ATCG' for b in ...)")
    print("• 返回布尔值: True/False")
    
    print("\n第三步：创建函数")
    print("-" * 40)
    
    def validate_dna_sequence(sequence):
        """
        验证DNA序列 - 提取的共同逻辑
        
        这个函数封装了重复的验证逻辑，
        就像实验室的质控SOP。
        """
        sequence_upper = sequence.upper()
        valid_bases = set('ATCG')
        return all(base in valid_bases for base in sequence_upper)
    
    print("创建的函数:")
    print("""
    def validate_dna_sequence(sequence):
        sequence_upper = sequence.upper()
        valid_bases = set('ATCG')
        return all(base in valid_bases for base in sequence_upper)
    """)
    
    print("\n第四步：使用函数替换重复代码")
    print("-" * 40)
    
    # 测试序列
    test_sequences = [
        ("正常序列", "ATCGATCG"),
        ("包含无效字符", "ATCGXYZ"),
        ("小写序列", "atcgatcg"),
        ("包含N", "ATCGNNNN")
    ]
    
    print("重构后的代码:")
    for label, seq in test_sequences:
        is_valid = validate_dna_sequence(seq)
        status = "✓ 有效" if is_valid else "✗ 无效"
        print(f"{label}: '{seq}' → {status}")
    
    print("\n重构的好处:")
    print("• 消除了代码重复")
    print("• 逻辑集中在一处，易于维护")
    print("• 函数名清晰表达意图")
    print("• 可以添加更多功能（如错误处理）")


def demonstrate_function_design_principles():
    """
    展示函数设计的最佳实践
    """
    print("\n\n🔬 函数设计原则")
    print("=" * 50)
    
    print("\n1. 单一职责原则")
    print("-" * 40)
    
    # 不好的例子 - 做太多事
    def bad_analyze_sequence(sequence):
        """❌ 不好的设计 - 一个函数做太多事"""
        # 验证、计算、转换、打印全在一起
        if not all(b in 'ATCG' for b in sequence.upper()):
            print("Invalid")
            return
        gc = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        rna = sequence.replace('T', 'U')
        print(f"GC: {gc}%, RNA: {rna}")
    
    # 好的例子 - 每个函数一个职责
    def validate_sequence(sequence):
        """✓ 验证序列 - 只做验证"""
        return all(base in 'ATCG' for base in sequence.upper())
    
    def calculate_gc_content(sequence):
        """✓ 计算GC含量 - 只做计算"""
        gc_count = sequence.count('G') + sequence.count('C')
        return (gc_count / len(sequence)) * 100 if sequence else 0
    
    def transcribe_dna(sequence):
        """✓ 转录DNA - 只做转录"""
        return sequence.replace('T', 'U')
    
    # 使用示例
    test_seq = "ATCGATCGATCG"
    print(f"测试序列: {test_seq}")
    
    if validate_sequence(test_seq):
        gc = calculate_gc_content(test_seq)
        rna = transcribe_dna(test_seq)
        print(f"✓ 序列有效")
        print(f"  GC含量: {gc:.1f}%")
        print(f"  RNA: {rna}")
    else:
        print("✗ 序列无效")
    
    print("\n2. 清晰的参数设计")
    print("-" * 40)
    
    def format_sequence(sequence, line_length=60, uppercase=True, add_numbers=False):
        """
        格式化序列 - 展示参数设计
        
        参数设计原则:
        - sequence: 必需参数（无默认值）
        - line_length: 可选参数（有合理默认值）
        - uppercase: 布尔开关（默认True）
        - add_numbers: 功能开关（默认False）
        """
        result = sequence.upper() if uppercase else sequence
        
        lines = []
        for i in range(0, len(result), line_length):
            line = result[i:i+line_length]
            if add_numbers:
                line = f"{i+1:4d}: {line}"
            lines.append(line)
        
        return '\n'.join(lines)
    
    # 展示不同的调用方式
    seq = "atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg"
    
    print("默认格式化:")
    print(format_sequence(seq, line_length=20))
    
    print("\n带行号:")
    print(format_sequence(seq, line_length=20, add_numbers=True))
    
    print("\n3. 合理的返回值")
    print("-" * 40)
    
    def analyze_composition(sequence):
        """
        分析序列组成 - 展示不同的返回值模式
        
        返回值设计:
        - 使用字典返回结构化数据
        - 字段名清晰明确
        - 包含所有相关信息
        """
        if not sequence:
            return {'error': 'Empty sequence'}
        
        sequence = sequence.upper()
        
        return {
            'length': len(sequence),
            'bases': {
                'A': sequence.count('A'),
                'T': sequence.count('T'),
                'C': sequence.count('C'),
                'G': sequence.count('G')
            },
            'gc_content': calculate_gc_content(sequence),
            'at_content': 100 - calculate_gc_content(sequence),
            'purine_count': sequence.count('A') + sequence.count('G'),
            'pyrimidine_count': sequence.count('C') + sequence.count('T')
        }
    
    result = analyze_composition("ATCGATCGATCG")
    print(f"组成分析结果:")
    for key, value in result.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for k, v in value.items():
                print(f"    {k}: {v}")
        else:
            print(f"  {key}: {value}")


def demonstrate_error_handling():
    """
    展示函数中的错误处理策略
    """
    print("\n\n🔬 错误处理策略")
    print("=" * 50)
    
    def robust_gc_calculator(sequence):
        """
        健壮的GC含量计算器
        
        像实验室SOP的质控步骤：
        1. 样品检查（输入验证）
        2. 预处理（标准化）
        3. 质量控制（有效性检查）
        4. 计算分析（核心功能）
        5. 结果验证（输出检查）
        """
        # 步骤1: 输入验证
        if sequence is None:
            raise ValueError("序列不能为None")
        
        if not isinstance(sequence, str):
            raise TypeError(f"序列必须是字符串，得到{type(sequence).__name__}")
        
        if not sequence:
            return 0.0  # 空序列返回0
        
        # 步骤2: 标准化
        sequence = sequence.strip().upper()
        
        # 步骤3: 质量控制
        valid_bases = set('ATCGN')
        invalid_bases = set(sequence) - valid_bases
        if invalid_bases:
            raise ValueError(f"序列包含无效碱基: {invalid_bases}")
        
        # 步骤4: 核心计算
        gc_count = sequence.count('G') + sequence.count('C')
        valid_base_count = len(sequence) - sequence.count('N')
        
        # 步骤5: 结果验证
        if valid_base_count == 0:
            return 0.0  # 全是N
        
        return (gc_count / valid_base_count) * 100
    
    # 测试各种情况
    test_cases = [
        ("正常序列", "ATCGATCG"),
        ("包含N", "ATCGNNATCG"),
        ("空序列", ""),
        ("包含空格", " ATCG ATCG "),
        ("小写", "atcgatcg"),
        ("无效字符", "ATCG123"),
        ("None值", None),
        ("数字", 12345)
    ]
    
    print("测试错误处理:")
    for label, test_input in test_cases:
        print(f"\n{label}: {repr(test_input)}")
        try:
            result = robust_gc_calculator(test_input)
            print(f"  ✓ GC含量: {result:.1f}%")
        except (ValueError, TypeError) as e:
            print(f"  ✗ 错误: {e}")


def demonstrate_function_composition():
    """
    展示如何组合简单函数构建复杂功能
    """
    print("\n\n🔬 函数组合：构建复杂功能")
    print("=" * 50)
    
    # 第一层：基础工具函数
    def is_valid_base(base):
        """检查单个碱基"""
        return base.upper() in 'ATCG'
    
    def complement_base(base):
        """获取互补碱基"""
        complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return complements.get(base.upper(), 'N')
    
    # 第二层：序列操作函数
    def validate_sequence(sequence):
        """验证整个序列"""
        return all(is_valid_base(base) for base in sequence)
    
    def complement_sequence(sequence):
        """生成互补序列"""
        return ''.join(complement_base(base) for base in sequence)
    
    def reverse_complement(sequence):
        """生成反向互补序列"""
        return complement_sequence(sequence)[::-1]
    
    # 第三层：分析函数
    def find_start_codons(sequence):
        """查找所有起始密码子ATG的位置"""
        positions = []
        sequence = sequence.upper()
        for i in range(len(sequence) - 2):
            if sequence[i:i+3] == 'ATG':
                positions.append(i)
        return positions
    
    def find_stop_codons(sequence):
        """查找所有终止密码子的位置"""
        positions = []
        sequence = sequence.upper()
        stop_codons = ['TAA', 'TAG', 'TGA']
        for i in range(len(sequence) - 2):
            if sequence[i:i+3] in stop_codons:
                positions.append((i, sequence[i:i+3]))
        return positions
    
    # 第四层：综合分析函数
    def analyze_coding_potential(sequence):
        """
        分析序列的编码潜力
        组合使用多个基础函数
        """
        if not validate_sequence(sequence):
            return {'error': '序列包含无效碱基'}
        
        analysis = {
            'length': len(sequence),
            'gc_content': calculate_gc_content(sequence),
            'start_codons': find_start_codons(sequence),
            'stop_codons': find_stop_codons(sequence),
            'reverse_complement': reverse_complement(sequence)
        }
        
        # 查找可能的ORF
        orfs = []
        for start_pos in analysis['start_codons']:
            for stop_pos, stop_type in analysis['stop_codons']:
                if stop_pos > start_pos and (stop_pos - start_pos) % 3 == 0:
                    orfs.append({
                        'start': start_pos,
                        'stop': stop_pos + 3,
                        'length': stop_pos + 3 - start_pos,
                        'stop_codon': stop_type
                    })
                    break  # 找到第一个终止密码子即可
        
        analysis['potential_orfs'] = orfs
        
        return analysis
    
    # 使用组合函数
    test_sequence = "ATGCGATCGATCGTAAATGCCCTAG"
    
    print(f"分析序列: {test_sequence}")
    print(f"序列长度: {len(test_sequence)} bp")
    
    result = analyze_coding_potential(test_sequence)
    
    if 'error' not in result:
        print(f"\n分析结果:")
        print(f"  GC含量: {result['gc_content']:.1f}%")
        print(f"  起始密码子ATG: {len(result['start_codons'])}个 at {result['start_codons']}")
        print(f"  终止密码子: {len(result['stop_codons'])}个")
        for pos, codon in result['stop_codons']:
            print(f"    {codon} at position {pos}")
        print(f"  潜在ORF: {len(result['potential_orfs'])}个")
        for i, orf in enumerate(result['potential_orfs'], 1):
            print(f"    ORF{i}: {orf['start']}-{orf['stop']} ({orf['length']}bp)")
        print(f"  反向互补: {result['reverse_complement']}")
    else:
        print(f"错误: {result['error']}")
    
    print("\n函数组合的优势:")
    print("• 每个函数专注一个任务")
    print("• 函数可以独立测试")
    print("• 易于理解和维护")
    print("• 可以灵活组合创建新功能")
    print("• 代码复用性高")


def demonstrate_building_function_library():
    """
    展示如何构建一个生物信息学函数库
    """
    print("\n\n🔬 构建生物信息学函数库")
    print("=" * 50)
    
    print("\n函数库的层次结构:")
    print("""
    第一层：基础工具函数
    ├── is_valid_base()      # 验证单个碱基
    ├── complement_base()     # 获取互补碱基
    └── codon_to_amino()      # 密码子转氨基酸
    
    第二层：序列操作函数
    ├── validate_sequence()   # 验证序列
    ├── clean_sequence()      # 清理序列
    ├── reverse_complement()  # 反向互补
    └── transcribe_dna()      # DNA转RNA
    
    第三层：分析函数
    ├── calculate_gc_content() # GC含量
    ├── find_orfs()           # 查找ORF
    ├── find_motifs()         # 查找模体
    └── analyze_composition() # 组成分析
    
    第四层：工作流函数
    ├── analyze_gene()        # 基因分析
    ├── compare_sequences()   # 序列比较
    └── generate_report()     # 生成报告
    """)
    
    # 示例：完整的基因分析工作流
    def analyze_gene_workflow(sequence, gene_name="Unknown"):
        """
        完整的基因分析工作流
        组合多个层次的函数
        """
        print(f"\n执行基因分析工作流: {gene_name}")
        print("-" * 40)
        
        # 步骤1：质量控制
        print("步骤1: 质量控制")
        if not validate_sequence(sequence):
            print("  ✗ 序列验证失败")
            return None
        print("  ✓ 序列验证通过")
        
        # 步骤2：基础分析
        print("\n步骤2: 基础分析")
        gc = calculate_gc_content(sequence)
        print(f"  GC含量: {gc:.1f}%")
        print(f"  序列长度: {len(sequence)} bp")
        
        # 步骤3：功能分析
        print("\n步骤3: 功能分析")
        start_codons = find_start_codons(sequence)
        print(f"  起始密码子: {len(start_codons)}个")
        
        # 步骤4：生成报告
        print("\n步骤4: 生成分析报告")
        report = {
            'gene_name': gene_name,
            'status': 'completed',
            'quality': 'passed',
            'metrics': {
                'length': len(sequence),
                'gc_content': gc,
                'start_codons': len(start_codons)
            }
        }
        
        return report
    
    # 执行示例工作流
    sample_gene = "ATGCGATCGATCGATGCCCTAG"
    report = analyze_gene_workflow(sample_gene, "SAMPLE_GENE_001")
    
    if report:
        print("\n📊 最终报告:")
        print(f"  基因: {report['gene_name']}")
        print(f"  状态: {report['status']}")
        print(f"  质量: {report['quality']}")
        print(f"  指标: {report['metrics']}")


def main():
    """
    主函数 - 组织所有演示
    
    主函数的作用：
    1. 作为程序的入口点
    2. 组织程序的执行流程
    3. 协调各个功能模块
    
    这就像实验室的总体实验方案，
    协调各个SOP的执行顺序。
    """
    print("🧬 Chapter 04: 函数 - 实验室的标准操作流程(SOP)")
    print("学习如何将重复的代码封装为可重用的函数")
    print("=" * 60)
    
    # 按照学习顺序执行演示
    demonstrate_why_we_need_functions()
    demonstrate_function_anatomy()
    demonstrate_refactoring_process()
    demonstrate_function_design_principles()
    demonstrate_error_handling()
    demonstrate_function_composition()
    demonstrate_building_function_library()
    
    print("\n" + "=" * 60)
    print("📚 本章核心要点:")
    print("1. 函数消除代码重复，提高可维护性")
    print("2. 函数像实验室SOP，标准化操作流程")
    print("3. 好的函数遵循单一职责原则")
    print("4. 参数设计要合理，提供有用的默认值")
    print("5. 错误处理让函数更加健壮")
    print("6. 简单函数可以组合成复杂功能")
    print("7. 构建函数库是编程的重要技能")
    
    print("\n🎯 记住:")
    print("函数是编程的基本构建块。")
    print("就像实验室的SOP让实验可重复、可靠，")
    print("函数让代码可重用、可维护、可测试。")
    print("\n开始把重复的代码重构为函数吧！")


if __name__ == "__main__":
    # 程序入口点
    # 当直接运行此文件时执行main函数
    main()