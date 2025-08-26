#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 04: 函数 - 实验室的标准操作流程(SOP)

本章将函数比作实验室的SOP，演示核心概念：
1. 函数的必要性与重构过程
2. 函数设计与参数系统
3. 作用域与最佳实践
4. 函数组合与工具库构建
"""


def demo_why_functions():
    """
    演示为什么需要函数 - 对比重复代码与函数化代码
    """
    print("🔬 为什么需要函数？")
    print("=" * 50)
    
    print("\n场景：分析多个基因的GC含量")
    print("-" * 30)
    
    # 方法1：重复代码
    print("\n❌ 没有函数的重复代码：")
    genes = ["ATCGATCG", "CGCGCGAT", "ATATGCGC"]
    
    for i, gene in enumerate(genes, 1):
        gc_count = gene.count('G') + gene.count('C')
        gc_content = (gc_count / len(gene)) * 100
        print(f"基因{i}: {gene} → GC: {gc_content:.1f}%")
    
    print("\n✅ 使用函数的解决方案：")
    
    def calculate_gc_content(sequence):
        """计算GC含量的标准SOP"""
        return (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    
    for i, gene in enumerate(genes, 1):
        gc = calculate_gc_content(gene)
        print(f"基因{i}: {gene} → GC: {gc:.1f}%")
    
    print("\n优势：只写一次，处处复用，易于维护")


def demo_function_anatomy():
    """
    展示函数的完整结构 - 类比实验室SOP
    """
    print("\n\n🔬 函数的完整结构")
    print("=" * 50)
    
    # 完整的函数示例
    def extract_dna(sample_id, volume_ml=1.0, method="column"):
        """
        DNA提取标准操作流程
        
        参数:
            sample_id (str): 样品编号
            volume_ml (float): 样品体积，默认1.0ml
            method (str): 提取方法，默认"column"
        
        返回:
            dict: DNA浓度和纯度信息
        """
        print(f"提取{sample_id}: {volume_ml}ml, 方法:{method}")
        
        return {
            'sample_id': sample_id,
            'concentration': 150.5,
            'purity': 1.85,
            'volume': volume_ml * 50
        }
    
    # 函数调用示例
    result1 = extract_dna("SAMPLE_001", 2.0)
    print(f"结果1: {result1}")
    
    result2 = extract_dna("SAMPLE_002")  # 使用默认值
    print(f"结果2: {result2}")
    
    print("\n函数结构要点:")
    print("• def关键字 + 函数名")
    print("• 参数列表（必需在前，默认值在后）")
    print("• 文档字符串（说明功能和用法）")
    print("• 函数体（实现功能的代码）")
    print("• return语句（返回结果）")


def demo_refactoring_process():
    """
    展示从重复代码到函数的重构过程
    """
    print("\n\n🔬 重构过程演示")
    print("=" * 50)
    
    # 步骤1：发现重复
    print("\n步骤1: 发现重复代码")
    sequences = ["ATCGATCG", "ATCGXYZ", "atcgatcg"]
    
    print("原始重复代码:")
    for seq in sequences:
        valid = all(b in 'ATCG' for b in seq.upper())
        print(f"  {seq}: {valid}")
    
    # 步骤2：提取函数
    print("\n步骤2: 创建函数")
    
    def validate_dna(sequence):
        """验证DNA序列的SOP"""
        return all(base in 'ATCG' for base in sequence.upper())
    
    print("重构后的代码:")
    for seq in sequences:
        valid = validate_dna(seq)
        status = "✓" if valid else "✗"
        print(f"  {seq}: {status} {valid}")
    
    print("\n重构好处:")
    print("• 消除重复，集中逻辑")
    print("• 易于维护和修改")
    print("• 提高代码可读性")


def demo_design_principles():
    """
    展示函数设计的最佳实践
    """
    print("\n\n🔬 函数设计原则")
    print("=" * 50)
    
    print("\n1. 单一职责原则")
    print("-" * 30)
    
    # 好的设计 - 每个函数一个职责
    def validate_sequence(sequence):
        """只验证序列"""
        return all(base in 'ATCG' for base in sequence.upper())
    
    def calculate_gc_content(sequence):
        """只计算GC含量"""
        return (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    
    def transcribe_dna(sequence):
        """只转录DNA"""
        return sequence.replace('T', 'U')
    
    # 使用示例
    test_seq = "ATCGATCG"
    print(f"测试序列: {test_seq}")
    
    if validate_sequence(test_seq):
        gc = calculate_gc_content(test_seq)
        rna = transcribe_dna(test_seq)
        print(f"  ✓ 有效序列")
        print(f"  GC含量: {gc:.1f}%")
        print(f"  RNA: {rna}")
    
    print("\n2. 合理的参数设计")
    print("-" * 30)
    
    def format_sequence(sequence, line_length=60, add_numbers=False):
        """格式化序列显示"""
        lines = []
        for i in range(0, len(sequence), line_length):
            line = sequence[i:i+line_length]
            if add_numbers:
                line = f"{i+1:4d}: {line}"
            lines.append(line)
        return '\n'.join(lines)
    
    seq = "ATCGATCGATCGATCGATCG"
    print("默认格式:")
    print(format_sequence(seq, line_length=10))
    
    print("\n带行号:")
    print(format_sequence(seq, line_length=10, add_numbers=True))


def demo_error_handling():
    """
    展示函数中的错误处理策略
    """
    print("\n\n🔬 错误处理策略")
    print("=" * 50)
    
    def safe_gc_calculator(sequence):
        """
        健壮的GC含量计算器
        包含完整的输入验证和错误处理
        """
        # 输入验证
        if not isinstance(sequence, str):
            raise TypeError(f"序列必须是字符串，得到{type(sequence)}")
        
        if not sequence:
            return 0.0
        
        # 清理和验证
        sequence = sequence.strip().upper()
        valid_bases = set('ATCGN')
        invalid_bases = set(sequence) - valid_bases
        
        if invalid_bases:
            print(f"警告：忽略无效碱基 {invalid_bases}")
            sequence = ''.join(b for b in sequence if b in valid_bases)
        
        # 计算GC含量
        if not sequence:
            return 0.0
        
        gc_count = sequence.count('G') + sequence.count('C')
        valid_count = len(sequence) - sequence.count('N')
        
        return (gc_count / valid_count * 100) if valid_count > 0 else 0.0
    
    # 测试用例
    test_cases = [
        ("正常序列", "ATCGATCG"),
        ("包含N", "ATCGNNATCG"),
        ("空序列", ""),
        ("无效字符", "ATCG123"),
        ("小写", "atcgatcg")
    ]
    
    print("错误处理测试:")
    for label, test_seq in test_cases:
        print(f"\n{label}: '{test_seq}'")
        try:
            result = safe_gc_calculator(test_seq)
            print(f"  ✓ GC含量: {result:.1f}%")
        except (ValueError, TypeError) as e:
            print(f"  ✗ 错误: {e}")


def demo_function_composition():
    """
    展示函数组合构建复杂功能
    """
    print("\n\n🔬 函数组合")
    print("=" * 50)
    
    # 基础函数
    def complement_base(base):
        """获取互补碱基"""
        complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return complements.get(base.upper(), 'N')
    
    def reverse_complement(sequence):
        """生成反向互补序列"""
        return ''.join(complement_base(b) for b in sequence[::-1])
    
    def find_orfs(sequence):
        """查找开放阅读框"""
        orfs = []
        seq = sequence.upper()
        
        for i in range(len(seq) - 2):
            if seq[i:i+3] == 'ATG':  # 起始密码子
                for j in range(i + 3, len(seq), 3):
                    if j + 2 < len(seq) and seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
                        orfs.append({'start': i, 'end': j+3, 'length': j+3-i})
                        break
        return orfs
    
    # 本地GC计算函数
    def calculate_gc_content(sequence):
        """计算GC含量"""
        sequence = sequence.upper()
        if not sequence:
            return 0.0
        gc_count = sequence.count('G') + sequence.count('C')
        return gc_count / len(sequence) * 100
    
    # 综合分析函数 - 组合使用基础函数
    def analyze_sequence_comprehensive(sequence):
        """综合序列分析"""
        return {
            'length': len(sequence),
            'gc_content': calculate_gc_content(sequence),
            'reverse_complement': reverse_complement(sequence),
            'orfs': find_orfs(sequence)
        }
    
    # 测试组合
    test_seq = "ATGCGATCGTAAATGCCCTAG"
    print(f"测试序列: {test_seq}")
    
    result = analyze_sequence_comprehensive(test_seq)
    print(f"\n综合分析结果:")
    print(f"  长度: {result['length']} bp")
    print(f"  GC含量: {result['gc_content']:.1f}%")
    print(f"  反向互补: {result['reverse_complement']}")
    print(f"  找到ORF: {len(result['orfs'])}个")
    
    for i, orf in enumerate(result['orfs'], 1):
        print(f"    ORF{i}: {orf['start']}-{orf['end']} ({orf['length']}bp)")
    
    print("\n组合优势: 模块化、可重用、易维护")


def demo_function_library():
    """
    展示如何构建生物信息学函数库
    """
    print("\n\n🔬 构建函数工具库")
    print("=" * 50)
    
    # 工具库结构
    print("函数库层次结构:")
    print("""
    基础层: 单一功能函数
    ├── validate_sequence()  # 验证序列
    ├── calculate_gc()       # GC含量
    └── reverse_complement() # 反向互补
    
    应用层: 组合分析函数
    └── analyze_gene()       # 综合基因分析
    """)
    
    # 基础工具函数（已在前面定义）
    def validate_sequence(seq):
        return all(b in 'ATCG' for b in seq.upper())
    
    def calculate_gc(seq):
        return (seq.count('G') + seq.count('C')) / len(seq) * 100
    
    def reverse_complement(seq):
        comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(comp.get(b.upper(), 'N') for b in seq[::-1])
    
    # 高级工作流函数
    def analyze_gene_pipeline(sequence, gene_name):
        """
        基因分析流水线 - 组合使用基础函数
        """
        print(f"\n分析基因: {gene_name}")
        
        # 使用基础函数
        if not validate_sequence(sequence):
            return {'error': '序列无效'}
        
        return {
            'name': gene_name,
            'length': len(sequence),
            'gc_content': calculate_gc(sequence),
            'reverse_comp': reverse_complement(sequence),
            'valid': True
        }
    
    # 测试工具库
    test_gene = "ATGCGATCG"
    result = analyze_gene_pipeline(test_gene, "TEST_GENE")
    
    print(f"\n分析结果:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    
    print("\n函数库优势:")
    print("• 模块化设计，易于扩展")
    print("• 代码重用，减少重复")
    print("• 层次清晰，便于维护")


def demo_scope_concepts():
    """
    演示作用域概念 - 变量的作用范围
    """
    print("\n\n🔬 作用域概念")
    print("=" * 50)
    
    # 全局变量（像实验室的公共试剂）
    CODON_TABLE = {
        'ATG': 'M', 'TTT': 'F', 'TAA': '*'
    }
    
    def translate_codon(codon):
        """
        翻译密码子 - 访问全局变量
        """
        # 局部变量（函数内的临时变量）
        clean_codon = codon.upper().strip()
        
        # 访问全局变量
        return CODON_TABLE.get(clean_codon, 'X')
    
    def translate_sequence(dna):
        """
        翻译DNA序列 - 局部变量作用域
        """
        protein = ""  # 局部变量
        
        for i in range(0, len(dna), 3):
            codon = dna[i:i+3]  # 局部变量
            if len(codon) == 3:
                amino_acid = translate_codon(codon)
                if amino_acid == '*':  # 终止密码子
                    break
                protein += amino_acid
        
        return protein
    
    # 测试作用域
    test_dna = "ATGTTTTAA"
    result = translate_sequence(test_dna)
    
    print(f"DNA: {test_dna}")
    print(f"蛋白质: {result}")
    
    print("\n作用域要点:")
    print("• 全局变量: 整个程序可见")
    print("• 局部变量: 只在函数内可见")
    print("• 避免意外修改全局变量")
    print("• 优先使用局部变量和参数")


def main():
    """
    主函数 - 协调所有演示
    
    主函数像实验室的总体方案，
    协调各个SOP的执行顺序。
    """
    print("🧬 Chapter 04: 函数 - 实验室的标准操作流程")
    print("学习如何将重复代码封装为可重用函数")
    print("=" * 60)
    
    print("\n演示内容:")
    print("1. 为什么需要函数")
    print("2. 函数的完整结构")
    print("3. 代码重构过程")
    print("4. 函数设计原则")
    print("5. 错误处理策略")
    print("6. 函数组合应用")
    print("7. 构建工具库")
    print("8. 作用域概念")
    
    input("\n按Enter开始学习...")
    
    # 执行所有演示
    demo_why_functions()
    input("\n按Enter继续...")
    
    demo_function_anatomy()
    input("\n按Enter继续...")
    
    demo_refactoring_process()
    input("\n按Enter继续...")
    
    demo_design_principles()
    input("\n按Enter继续...")
    
    demo_error_handling()
    input("\n按Enter继续...")
    
    demo_function_composition()
    input("\n按Enter继续...")
    
    demo_function_library()
    input("\n按Enter继续...")
    
    demo_scope_concepts()
    
    print("\n" + "=" * 60)
    print("📚 核心要点总结:")
    print("• 函数消除重复，提高复用性")
    print("• 单一职责，接口清晰")
    print("• 合理参数，健壮错误处理")
    print("• 函数组合构建复杂功能")
    print("• 分层设计，构建工具库")
    print("• 理解作用域，避免变量冲突")
    
    print("\n🎯 记住:")
    print("函数是编程的基本构建块，")
    print("像SOP让实验标准化，")
    print("函数让代码模块化、可维护。")
    
    print("\n下一步: 完成practice.py练习！")


if __name__ == "__main__":
    main()