#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 02: 实验室数据管理 - 列表、字典与密码子表
====================================================
生物学场景：你是一名分子生物学研究员，需要管理实验室的DNA样品，
         构建密码子表，并将DNA序列翻译成蛋白质序列。

学习目标：
1. 理解为什么需要不同的数据结构
2. 掌握列表（试管架）的使用
3. 掌握字典（标签系统）的使用
4. 构建和使用密码子表
5. 实现DNA到蛋白质的翻译

让我们开始这段数据管理之旅！
"""

# ========== 第一部分：导入实验室工具（模块） ==========
print("\n" + "="*60)
print("🧪 欢迎来到分子生物学数据管理实验室！")
print("="*60)

# 就像从实验室仓库借用仪器，我们导入Python模块
import random           # 随机数生成器 - 用于模拟随机突变
from collections import Counter  # 自动计数器 - 用于统计频率

# 稍后我们会看到这些"仪器"的强大功能！


def lesson_1_lists_as_tube_racks():
    """
    第1课：列表 - 你的数字试管架
    
    想象你有一个试管架，可以放置多个DNA样品。
    Python列表就是这样一个容器！
    """
    print("\n" + "="*50)
    print("📚 第1课：列表 - 数字试管架")
    print("="*50)
    
    # ========== 1.1 创建试管架（列表） ==========
    print("\n📦 1.1 创建你的第一个试管架")
    print("-" * 40)
    
    # 方法1：创建空试管架，然后添加样品
    dna_samples = []  # 空试管架
    print(f"空试管架: {dna_samples}")
    
    # 添加样品（就像把试管放入架子）
    dna_samples.append("ATCG")  # 第1个样品
    dna_samples.append("GCTA")  # 第2个样品
    dna_samples.append("TTAA")  # 第3个样品
    print(f"添加3个样品后: {dna_samples}")
    
    # 方法2：直接创建带样品的试管架
    gene_list = ["TP53", "BRCA1", "EGFR", "KRAS", "MYC"]
    print(f"\n基因列表: {gene_list}")
    print(f"试管架上有 {len(gene_list)} 个基因")
    
    # ========== 1.2 访问试管（索引） ==========
    print("\n📍 1.2 从试管架取样品（索引访问）")
    print("-" * 40)
    
    # Python索引从0开始（第1个位置是0）
    print(f"第1个基因（索引0）: {gene_list[0]}")
    print(f"第3个基因（索引2）: {gene_list[2]}")
    print(f"最后一个基因（索引-1）: {gene_list[-1]}")
    
    # 切片：取出一段连续的样品
    print(f"前3个基因: {gene_list[0:3]}")
    print(f"第2到第4个基因: {gene_list[1:4]}")
    
    # ========== 1.3 修改试管架 ==========
    print("\n🔧 1.3 管理你的试管架")
    print("-" * 40)
    
    # 替换样品（修改特定位置）
    print(f"原始列表: {gene_list}")
    gene_list[1] = "BRCA2"  # 把BRCA1换成BRCA2
    print(f"替换后: {gene_list}")
    
    # 插入新样品（在指定位置）
    gene_list.insert(2, "ALK")  # 在索引2的位置插入
    print(f"插入ALK后: {gene_list}")
    
    # 移除样品
    gene_list.remove("KRAS")  # 移除指定样品
    print(f"移除KRAS后: {gene_list}")
    
    # ========== 1.4 列表的强大功能 ==========
    print("\n💪 1.4 列表的实用操作")
    print("-" * 40)
    
    # 排序（按字母顺序整理）
    gene_list.sort()
    print(f"排序后: {gene_list}")
    
    # 反转顺序
    gene_list.reverse()
    print(f"反转后: {gene_list}")
    
    # 统计某个元素出现次数
    sequences = ["ATG", "TAA", "ATG", "TGA", "ATG", "TAA"]
    print(f"\n序列列表: {sequences}")
    print(f"ATG出现次数: {sequences.count('ATG')}")
    print(f"TAA出现次数: {sequences.count('TAA')}")
    
    input("\n按Enter继续学习字典...")


def lesson_2_dictionaries_as_labels():
    """
    第2课：字典 - 样品标签系统
    
    想象每个试管都有标签，你可以通过标签快速找到对应的样品。
    这就是字典的作用！
    """
    print("\n" + "="*50)
    print("📚 第2课：字典 - 样品标签系统")
    print("="*50)
    
    # ========== 2.1 创建标签系统 ==========
    print("\n🏷️ 2.1 创建你的标签系统")
    print("-" * 40)
    
    # 创建基因序列字典（基因名 -> 序列）
    gene_sequences = {
        "insulin": "ATGGCCCTGTGGATGCGC",
        "hemoglobin": "ATGGTGCATCTGACTCCT",
        "p53": "ATGGAGGAGCCGCAGTCA"
    }
    
    print("基因序列数据库:")
    for gene, seq in gene_sequences.items():
        print(f"  {gene}: {seq[:10]}...")  # 只显示前10个碱基
    
    # ========== 2.2 通过标签查找 ==========
    print("\n🔍 2.2 通过基因名查找序列")
    print("-" * 40)
    
    # 直接通过键（基因名）获取值（序列）
    insulin_seq = gene_sequences["insulin"]
    print(f"胰岛素基因序列: {insulin_seq}")
    
    # 安全查找（避免键不存在的错误）
    brca1_seq = gene_sequences.get("BRCA1", "序列未找到")
    print(f"BRCA1序列: {brca1_seq}")
    
    # ========== 2.3 更新标签系统 ==========
    print("\n✏️ 2.3 更新你的数据库")
    print("-" * 40)
    
    # 添加新基因
    gene_sequences["GAPDH"] = "ATGGGAAAGGTGAAGGTC"
    print("添加GAPDH基因后:")
    print(f"数据库中现有 {len(gene_sequences)} 个基因")
    
    # 更新现有序列
    gene_sequences["p53"] = "ATGGAGGAGCCGCAGTCAGATCC"  # 更完整的序列
    print(f"更新后的p53序列: {gene_sequences['p53']}")
    
    # ========== 2.4 实验数据管理 ==========
    print("\n📊 2.4 管理实验数据")
    print("-" * 40)
    
    # 样品浓度记录
    sample_concentrations = {
        "Sample_001": 125.3,  # ng/μL
        "Sample_002": 89.7,
        "Sample_003": 156.2,
        "Sample_004": 45.8
    }
    
    print("样品浓度数据:")
    for sample_id, conc in sample_concentrations.items():
        status = "✅ 合格" if conc > 50 else "⚠️ 浓度过低"
        print(f"  {sample_id}: {conc} ng/μL {status}")
    
    # 计算平均浓度
    avg_conc = sum(sample_concentrations.values()) / len(sample_concentrations)
    print(f"\n平均浓度: {avg_conc:.1f} ng/μL")
    
    input("\n按Enter继续学习密码子表...")


def lesson_3_codon_table():
    """
    第3课：构建密码子表 - 生命的翻译字典
    
    密码子表是生物学中最重要的"字典"之一。
    它定义了DNA三联体如何翻译成氨基酸。
    """
    print("\n" + "="*50)
    print("📚 第3课：密码子表 - 生命的翻译字典")
    print("="*50)
    
    # ========== 3.1 理解密码子 ==========
    print("\n🧬 3.1 什么是密码子？")
    print("-" * 40)
    print("""
    密码子 = 3个连续的DNA/RNA碱基
    例如: ATG, TAA, GCT
    
    为什么是3个？
    - 4种碱基，取1个：4种可能（太少）
    - 4种碱基，取2个：16种可能（不够20种氨基酸）
    - 4种碱基，取3个：64种可能（足够！还有冗余）
    """)
    
    # ========== 3.2 构建简化密码子表 ==========
    print("\n🔨 3.2 构建密码子表")
    print("-" * 40)
    
    # 先构建一个简化版本
    simple_codon_table = {
        # 起始密码子
        'ATG': 'M',  # 甲硫氨酸（起始）
        
        # 常见氨基酸
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # 丙氨酸
        'TGT': 'C', 'TGC': 'C',  # 半胱氨酸
        'GAT': 'D', 'GAC': 'D',  # 天冬氨酸
        'GAA': 'E', 'GAG': 'E',  # 谷氨酸
        'TTT': 'F', 'TTC': 'F',  # 苯丙氨酸
        
        # 终止密码子
        'TAA': '*', 'TAG': '*', 'TGA': '*'
    }
    
    print(f"简化密码子表包含 {len(simple_codon_table)} 个密码子")
    print("\n示例翻译:")
    test_codons = ['ATG', 'GCT', 'GAA', 'TAA']
    for codon in test_codons:
        amino_acid = simple_codon_table.get(codon, '?')
        aa_name = {
            'M': '甲硫氨酸', 'A': '丙氨酸', 
            'E': '谷氨酸', '*': '终止'
        }.get(amino_acid, '未知')
        print(f"  {codon} → {amino_acid} ({aa_name})")
    
    # ========== 3.3 完整密码子表 ==========
    print("\n📖 3.3 标准遗传密码子表")
    print("-" * 40)
    
    # 构建完整的密码子表
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    print(f"完整密码子表: {len(codon_table)} 个密码子")
    print(f"编码氨基酸: {len(set(codon_table.values()))} 种")
    
    # 分析密码子的简并性（多个密码子编码同一氨基酸）
    from collections import Counter
    aa_counts = Counter(codon_table.values())
    print("\n密码子简并性分析:")
    for aa, count in sorted(aa_counts.items()):
        if aa == '*':
            print(f"  终止信号: {count} 个密码子")
        else:
            print(f"  氨基酸 {aa}: {count} 个密码子")
    
    input("\n按Enter继续学习DNA翻译...")


def lesson_4_dna_translation():
    """
    第4课：DNA到蛋白质的翻译
    
    现在让我们用学到的数据结构实现中心法则：
    DNA → RNA → 蛋白质
    """
    print("\n" + "="*50)
    print("📚 第4课：实现DNA到蛋白质的翻译")
    print("="*50)
    
    # 标准密码子表
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    # ========== 4.1 简单翻译 ==========
    print("\n🔬 4.1 翻译你的第一个基因")
    print("-" * 40)
    
    # 示例：人类胰岛素基因片段
    dna_sequence = "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCA"
    print(f"DNA序列: {dna_sequence[:30]}...")
    print(f"序列长度: {len(dna_sequence)} bp")
    
    # 翻译过程
    protein = []
    for i in range(0, len(dna_sequence), 3):  # 每3个碱基一组
        codon = dna_sequence[i:i+3]
        if len(codon) == 3:  # 确保是完整的密码子
            amino_acid = codon_table.get(codon, '?')
            protein.append(amino_acid)
            if amino_acid == '*':  # 遇到终止密码子
                break
    
    protein_sequence = ''.join(protein)
    print(f"蛋白质序列: {protein_sequence}")
    print(f"蛋白质长度: {len(protein_sequence)} 个氨基酸")
    
    # ========== 4.2 翻译函数 ==========
    print("\n🛠️ 4.2 创建翻译函数")
    print("-" * 40)
    
    def translate_dna(dna, codon_table):
        """将DNA序列翻译成蛋白质序列"""
        protein = []
        
        # 找到起始密码子ATG
        start_pos = dna.find('ATG')
        if start_pos == -1:
            return "No start codon found"
        
        # 从起始密码子开始翻译
        for i in range(start_pos, len(dna), 3):
            codon = dna[i:i+3]
            if len(codon) == 3:
                amino_acid = codon_table.get(codon, 'X')
                if amino_acid == '*':
                    break
                protein.append(amino_acid)
        
        return ''.join(protein)
    
    # 测试不同的序列
    test_sequences = {
        "有效基因": "AAATGGCCTAAGGGTAA",
        "无起始密码子": "GCCTAAGGGTAAGGG",
        "多个起始密码子": "ATGGCCATGAAATAA"
    }
    
    for name, seq in test_sequences.items():
        result = translate_dna(seq, codon_table)
        print(f"{name}: {seq}")
        print(f"  翻译结果: {result}")
    
    # ========== 4.3 统计分析 ==========
    print("\n📊 4.3 氨基酸组成分析")
    print("-" * 40)
    
    # 分析蛋白质组成
    aa_counts = Counter(protein_sequence)
    print("氨基酸组成:")
    for aa, count in sorted(aa_counts.items()):
        percentage = (count / len(protein_sequence)) * 100
        print(f"  {aa}: {count} 个 ({percentage:.1f}%)")
    
    # 疏水性分析（简化版）
    hydrophobic = ['A', 'V', 'I', 'L', 'M', 'F', 'W', 'P', 'G']
    hydrophobic_count = sum(1 for aa in protein_sequence if aa in hydrophobic)
    hydrophobic_percent = (hydrophobic_count / len(protein_sequence)) * 100
    print(f"\n疏水性氨基酸: {hydrophobic_count} 个 ({hydrophobic_percent:.1f}%)")
    
    input("\n按Enter继续综合练习...")


def lesson_5_practical_application():
    """
    第5课：综合应用 - 管理基因表达数据
    
    结合列表和字典，管理和分析实验数据
    """
    print("\n" + "="*50)
    print("📚 第5课：综合应用 - 基因表达数据管理")
    print("="*50)
    
    # ========== 5.1 构建基因数据库 ==========
    print("\n🗄️ 5.1 构建综合基因数据库")
    print("-" * 40)
    
    # 基因信息数据库（嵌套字典）
    gene_database = {
        "TP53": {
            "name": "Tumor protein p53",
            "sequence": "ATGGAGGAGCCGCAGTCAGATCCTAGC",
            "expression": 125.3,  # FPKM值
            "function": "肿瘤抑制基因"
        },
        "BRCA1": {
            "name": "Breast cancer 1",
            "sequence": "ATGGATTTATCTGCTCTTCGCGTTGAA",
            "expression": 89.7,
            "function": "DNA修复"
        },
        "MYC": {
            "name": "MYC proto-oncogene",
            "sequence": "ATGCCCCTCAACGTTAGCTTCACCAAC",
            "expression": 234.5,
            "function": "细胞增殖调控"
        }
    }
    
    print("基因数据库内容:")
    for gene_id, info in gene_database.items():
        print(f"\n{gene_id}:")
        print(f"  全名: {info['name']}")
        print(f"  功能: {info['function']}")
        print(f"  表达量: {info['expression']} FPKM")
        print(f"  序列: {info['sequence'][:15]}...")
    
    # ========== 5.2 数据分析 ==========
    print("\n📈 5.2 表达数据分析")
    print("-" * 40)
    
    # 提取表达数据
    expression_values = [gene['expression'] for gene in gene_database.values()]
    gene_names = list(gene_database.keys())
    
    # 统计分析
    avg_expression = sum(expression_values) / len(expression_values)
    max_expression = max(expression_values)
    min_expression = min(expression_values)
    
    print(f"平均表达量: {avg_expression:.1f} FPKM")
    print(f"最高表达量: {max_expression} FPKM")
    print(f"最低表达量: {min_expression} FPKM")
    
    # 找出高表达基因
    high_expression_threshold = 100
    high_expressed_genes = [
        gene for gene, info in gene_database.items()
        if info['expression'] > high_expression_threshold
    ]
    print(f"\n高表达基因 (>{high_expression_threshold} FPKM):")
    for gene in high_expressed_genes:
        print(f"  - {gene}: {gene_database[gene]['expression']} FPKM")
    
    # ========== 5.3 批量处理 ==========
    print("\n⚡ 5.3 批量序列处理")
    print("-" * 40)
    
    # 批量计算GC含量
    gc_contents = {}
    for gene_id, info in gene_database.items():
        seq = info['sequence']
        gc_count = seq.count('G') + seq.count('C')
        gc_content = (gc_count / len(seq)) * 100
        gc_contents[gene_id] = gc_content
    
    print("各基因GC含量:")
    for gene_id, gc in gc_contents.items():
        print(f"  {gene_id}: {gc:.1f}%")
    
    # ========== 5.4 数据导出准备 ==========
    print("\n💾 5.4 准备数据导出")
    print("-" * 40)
    
    # 创建导出格式（模拟CSV）
    export_data = []
    export_data.append("Gene_ID,Name,Expression,GC_Content")
    
    for gene_id, info in gene_database.items():
        row = f"{gene_id},{info['name']},{info['expression']},{gc_contents[gene_id]:.1f}"
        export_data.append(row)
    
    print("导出数据预览（CSV格式）:")
    for line in export_data[:3]:  # 只显示前3行
        print(f"  {line}")
    print("  ...")
    
    print("\n✅ 数据已准备好导出!")


def main():
    """主函数：按顺序执行所有课程"""
    
    # 清屏效果（可选）
    print("\n" * 2)
    
    print("🧬 Chapter 02: 实验室数据管理")
    print("="*60)
    print("本章将学习如何使用Python数据结构管理生物学数据")
    print("就像管理实验室的样品和数据一样！")
    print("="*60)
    
    # 学习菜单
    lessons = [
        ("1", "列表 - 数字试管架", lesson_1_lists_as_tube_racks),
        ("2", "字典 - 样品标签系统", lesson_2_dictionaries_as_labels),
        ("3", "密码子表 - 生命的翻译字典", lesson_3_codon_table),
        ("4", "DNA翻译 - 中心法则实现", lesson_4_dna_translation),
        ("5", "综合应用 - 基因数据管理", lesson_5_practical_application),
    ]
    
    print("\n📚 课程列表:")
    for num, title, _ in lessons:
        print(f"  {num}. {title}")
    print("  A. 运行所有课程")
    print("  Q. 退出")
    
    while True:
        choice = input("\n请选择课程 (1-5/A/Q): ").strip().upper()
        
        if choice == 'Q':
            print("\n👋 感谢学习！记得完成practice.py中的练习！")
            break
        elif choice == 'A':
            for _, _, lesson_func in lessons:
                lesson_func()
            print("\n🎉 恭喜完成所有课程！")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            idx = int(choice) - 1
            lessons[idx][2]()
        else:
            print("无效选择，请重试")


if __name__ == "__main__":
    main()