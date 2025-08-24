#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 02: 数据结构 - 练习题完整答案

提供所有练习的详细解决方案。
"""

def practice_1_amino_acid_frequency():
    """
    练习1: 氨基酸频率统计 - 完整解答
    """
    print("🔍 练习1: 氨基酸频率统计")
    print("-" * 40)
    
    # 测试蛋白质序列
    protein_sequence = "MKLLSSIEQACDICRLKKLKCSKEKPKCAKCLKNNWECRYSPKTKRS"
    print(f"蛋白质序列: {protein_sequence}")
    
    # 创建一个字典来存储每个氨基酸的计数
    aa_counts = {}
    
    # 遍历序列，统计每个氨基酸的出现次数
    for aa in protein_sequence:
        aa_counts[aa] = aa_counts.get(aa, 0) + 1
    
    # 计算序列总长度
    total_length = len(protein_sequence)
    
    # 计算每个氨基酸的频率（百分比）
    aa_frequencies = {}
    for aa, count in aa_counts.items():
        aa_frequencies[aa] = (count / total_length) * 100
    
    # 找出最常见和最稀少的氨基酸
    most_common_aa = max(aa_counts, key=aa_counts.get)
    least_common_aa = min(aa_counts, key=aa_counts.get)
    
    # 打印统计结果
    print(f"\n📊 氨基酸频率统计:")
    print(f"序列长度: {total_length} 个氨基酸")
    print(f"\n各氨基酸统计:")
    
    # 按频率排序显示
    sorted_aa = sorted(aa_frequencies.items(), key=lambda x: x[1], reverse=True)
    for aa, freq in sorted_aa:
        count = aa_counts[aa]
        print(f"  {aa}: {count:2d} 次 ({freq:5.1f}%)")
    
    print(f"\n🎯 关键统计:")
    print(f"最常见氨基酸: {most_common_aa} ({aa_counts[most_common_aa]} 次)")
    print(f"最稀少氨基酸: {least_common_aa} ({aa_counts[least_common_aa]} 次)")
    print(f"氨基酸种类数: {len(aa_counts)}")


def practice_2_reverse_translation():
    """
    练习2: 反向翻译 - 完整解答
    """
    print("\n🔍 练习2: 反向翻译")
    print("-" * 40)
    
    # 创建完整的氨基酸到密码子的反向映射
    reverse_codon_table = {
        'A': ['GCT', 'GCC', 'GCA', 'GCG'],  # 丙氨酸
        'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],  # 精氨酸
        'N': ['AAT', 'AAC'],  # 天冬酰胺
        'D': ['GAT', 'GAC'],  # 天冬氨酸
        'C': ['TGT', 'TGC'],  # 半胱氨酸
        'E': ['GAA', 'GAG'],  # 谷氨酸
        'Q': ['CAA', 'CAG'],  # 谷氨酰胺
        'G': ['GGT', 'GGC', 'GGA', 'GGG'],  # 甘氨酸
        'H': ['CAT', 'CAC'],  # 组氨酸
        'I': ['ATT', 'ATC', 'ATA'],  # 异亮氨酸
        'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],  # 亮氨酸
        'K': ['AAA', 'AAG'],  # 赖氨酸
        'M': ['ATG'],  # 甲硫氨酸
        'F': ['TTT', 'TTC'],  # 苯丙氨酸
        'P': ['CCT', 'CCC', 'CCA', 'CCG'],  # 脯氨酸
        'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],  # 丝氨酸
        'T': ['ACT', 'ACC', 'ACA', 'ACG'],  # 苏氨酸
        'W': ['TGG'],  # 色氨酸
        'Y': ['TAT', 'TAC'],  # 酪氨酸
        'V': ['GTT', 'GTC', 'GTA', 'GTG'],  # 缬氨酸
        '*': ['TAA', 'TAG', 'TGA']  # 终止密码子
    }
    
    test_protein = "MFL"
    print(f"蛋白质序列: {test_protein}")
    
    # 为每个氨基酸找出对应的密码子
    print(f"\n🧬 各氨基酸对应的密码子:")
    possible_codons = []
    total_combinations = 1
    
    for aa in test_protein:
        codons = reverse_codon_table.get(aa, [])
        possible_codons.append(codons)
        total_combinations *= len(codons)
        
        aa_name = {'M': '甲硫氨酸', 'F': '苯丙氨酸', 'L': '亮氨酸'}.get(aa, aa)
        print(f"  {aa} ({aa_name}): {len(codons)} 个密码子 - {' '.join(codons)}")
    
    # 计算总的DNA序列组合数
    print(f"\n📊 组合统计:")
    print(f"总DNA序列组合数: {total_combinations}")
    
    # 列出前10种可能的DNA序列组合
    print(f"\n🎯 前10种可能的DNA序列:")
    import itertools
    
    all_combinations = list(itertools.product(*possible_codons))
    
    for i, combination in enumerate(all_combinations[:10]):
        dna_sequence = ''.join(combination)
        print(f"  {i+1:2d}: {dna_sequence}")
    
    if len(all_combinations) > 10:
        print(f"  ... (还有 {len(all_combinations)-10} 种组合)")


def practice_3_orf_finder():
    """
    练习3: 开放阅读框查找 - 完整解答
    """
    print("\n🔍 练习3: 开放阅读框查找")
    print("-" * 40)
    
    # 测试DNA序列
    dna_sequence = "ATGAAATTCTAAATGGGCAAATAG"
    print(f"DNA序列: {dna_sequence}")
    print(f"序列长度: {len(dna_sequence)} bp")
    
    # 查找所有ATG起始位点
    start_positions = []
    for i in range(len(dna_sequence) - 2):
        if dna_sequence[i:i+3] == 'ATG':
            start_positions.append(i)
    
    print(f"\n🎯 ATG起始位点:")
    for pos in start_positions:
        print(f"  位置 {pos+1}: {dna_sequence[pos:pos+3]}")
    
    # 查找所有终止密码子位点
    stop_codons = ['TAA', 'TAG', 'TGA']
    stop_positions = []
    
    for i in range(len(dna_sequence) - 2):
        codon = dna_sequence[i:i+3]
        if codon in stop_codons:
            stop_positions.append((i, codon))
    
    print(f"\n🛑 终止密码子位点:")
    for pos, codon in stop_positions:
        print(f"  位置 {pos+1}: {codon}")
    
    # 找出有效的ORF（从ATG到终止密码子，长度为3的倍数）
    orfs = []
    
    for start_pos in start_positions:
        for stop_pos, stop_codon in stop_positions:
            if stop_pos > start_pos and (stop_pos - start_pos) % 3 == 0:
                orf_seq = dna_sequence[start_pos:stop_pos+3]
                orfs.append({
                    'start': start_pos,
                    'stop': stop_pos + 2,
                    'length': len(orf_seq),
                    'sequence': orf_seq,
                    'stop_codon': stop_codon
                })
    
    print(f"\n🧬 发现的开放阅读框:")
    
    # 简单的密码子表
    codon_table = {
        'ATG': 'M', 'TTT': 'F', 'TTC': 'F', 'AAA': 'K', 'AAG': 'K',
        'GGG': 'G', 'GGC': 'G', 'GGA': 'G', 'GGT': 'G',
        'TAA': '*', 'TAG': '*', 'TGA': '*'
    }
    
    for i, orf in enumerate(orfs, 1):
        print(f"\n  ORF {i}:")
        print(f"    位置: {orf['start']+1} - {orf['stop']+1}")
        print(f"    长度: {orf['length']} bp")
        print(f"    序列: {orf['sequence']}")
        
        # 翻译ORF
        protein_seq = ""
        for j in range(0, len(orf['sequence']), 3):
            codon = orf['sequence'][j:j+3]
            if len(codon) == 3:
                aa = codon_table.get(codon, 'X')
                protein_seq += aa
        
        print(f"    蛋白质: {protein_seq}")
        print(f"    终止密码子: {orf['stop_codon']}")
    
    if not orfs:
        print("  未发现完整的开放阅读框")


def practice_4_gene_database():
    """
    练习4: 基因信息数据库 - 完整解答
    """
    print("\n🔍 练习4: 基因信息数据库")
    print("-" * 40)
    
    # 创建基因数据库字典
    gene_database = {}
    
    # 添加基因信息
    genes_to_add = [
        {
            'name': 'TP53',
            'chr': '17p13.1',
            'function': 'tumor suppressor',
            'full_name': 'tumor protein p53',
            'diseases': ['Li-Fraumeni syndrome', 'various cancers'],
            'protein_length': 393
        },
        {
            'name': 'BRCA1',
            'chr': '17q21.31',
            'function': 'DNA repair',
            'full_name': 'BRCA1 DNA repair associated',
            'diseases': ['hereditary breast cancer', 'ovarian cancer'],
            'protein_length': 1863
        },
        {
            'name': 'GAPDH',
            'chr': '12p13.31',
            'function': 'housekeeping',
            'full_name': 'glyceraldehyde-3-phosphate dehydrogenase',
            'diseases': [],
            'protein_length': 335
        },
        {
            'name': 'MYC',
            'chr': '8q24.21',
            'function': 'oncogene',
            'full_name': 'MYC proto-oncogene',
            'diseases': ['Burkitt lymphoma', 'various cancers'],
            'protein_length': 454
        },
        {
            'name': 'KRAS',
            'chr': '12p12.1',
            'function': 'oncogene',
            'full_name': 'KRAS proto-oncogene',
            'diseases': ['colorectal cancer', 'lung cancer', 'pancreatic cancer'],
            'protein_length': 189
        }
    ]
    
    # 将基因信息添加到数据库
    for gene_info in genes_to_add:
        gene_database[gene_info['name']] = gene_info
    
    print(f"✅ 基因数据库创建完成，包含 {len(gene_database)} 个基因")
    
    # 实现查询功能
    def search_gene(gene_name):
        """根据基因名查找信息"""
        gene_info = gene_database.get(gene_name.upper())
        if gene_info:
            print(f"\n🧬 {gene_name} 基因信息:")
            print(f"  全名: {gene_info['full_name']}")
            print(f"  染色体位置: {gene_info['chr']}")
            print(f"  功能分类: {gene_info['function']}")
            print(f"  蛋白质长度: {gene_info['protein_length']} aa")
            
            if gene_info['diseases']:
                print(f"  相关疾病: {', '.join(gene_info['diseases'])}")
            else:
                print(f"  相关疾病: 无直接疾病关联")
        else:
            print(f"❌ 未找到基因 {gene_name}")
        
        return gene_info
    
    # 实现按功能分类功能
    def classify_by_function():
        """按功能对基因进行分类"""
        function_groups = {}
        
        for gene_name, gene_info in gene_database.items():
            function = gene_info['function']
            if function not in function_groups:
                function_groups[function] = []
            function_groups[function].append(gene_name)
        
        print(f"\n📊 基因功能分类:")
        for function, genes in function_groups.items():
            print(f"  {function}: {', '.join(genes)} ({len(genes)}个)")
        
        return function_groups
    
    # 额外功能：按疾病关联分类
    def classify_by_disease():
        """按疾病关联对基因进行分类"""
        disease_genes = {}
        
        for gene_name, gene_info in gene_database.items():
            for disease in gene_info['diseases']:
                if disease not in disease_genes:
                    disease_genes[disease] = []
                disease_genes[disease].append(gene_name)
        
        print(f"\n🏥 疾病相关基因:")
        for disease, genes in disease_genes.items():
            print(f"  {disease}: {', '.join(genes)}")
        
        return disease_genes
    
    # 测试数据库功能
    print(f"\n🔍 功能测试:")
    
    # 测试基因查询
    test_genes = ['TP53', 'BRCA1', 'UNKNOWN']
    for gene in test_genes:
        search_gene(gene)
    
    # 测试功能分类
    classify_by_function()
    
    # 测试疾病分类
    classify_by_disease()
    
    # 统计信息
    print(f"\n📈 数据库统计:")
    total_genes = len(gene_database)
    total_diseases = len(set(disease for gene_info in gene_database.values() 
                            for disease in gene_info['diseases']))
    avg_protein_length = sum(gene_info['protein_length'] 
                           for gene_info in gene_database.values()) / total_genes
    
    print(f"  总基因数: {total_genes}")
    print(f"  涉及疾病数: {total_diseases}")
    print(f"  平均蛋白质长度: {avg_protein_length:.0f} aa")


def main():
    """
    主函数: 运行所有练习的完整解答
    """
    print("🧬 Chapter 02 数据结构练习题完整解答")
    print("展示列表和字典在生物信息学中的强大应用\n")
    
    practice_1_amino_acid_frequency()
    practice_2_reverse_translation()
    practice_3_orf_finder()
    practice_4_gene_database()
    
    print("\n" + "=" * 50)
    print("📚 解答要点总结:")
    
    print("\n1. 数据结构选择:")
    print("   - 字典: 键值映射关系，如氨基酸统计、密码子表")
    print("   - 列表: 有序数据集合，如密码子组合、位置信息")
    print("   - 嵌套结构: 复杂数据组织，如基因数据库")
    
    print("\n2. 算法技巧:")
    print("   - get()方法: 安全的字典访问")
    print("   - 列表推导式: 简洁的数据处理")
    print("   - itertools: 生成排列组合")
    print("   - enumerate(): 同时获取索引和值")
    
    print("\n3. 生物学应用:")
    print("   - 序列分析: ORF查找、翻译")
    print("   - 数据统计: 频率分析、组成计算")
    print("   - 信息管理: 基因数据库构建")
    print("   - 模式识别: 起始/终止信号检测")
    
    print("\n🎯 编程最佳实践:")
    print("- 选择合适的数据结构提高效率")
    print("- 使用有意义的变量名和注释")
    print("- 实现错误处理和输入验证")
    print("- 将复杂功能分解为小函数")


if __name__ == "__main__":
    main()