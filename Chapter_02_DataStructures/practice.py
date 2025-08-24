#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 02 练习：实验室数据管理
================================
现在是时候动手管理你自己的生物学数据了！
通过这些练习，你将掌握列表和字典在生物信息学中的应用。

记住：
- 列表 = 试管架（有序存储）
- 字典 = 标签系统（通过名称查找）
- 密码子表 = DNA到蛋白质的翻译字典
"""

# ========== 热身练习 ==========
print("="*60)
print("🏃 热身练习：确认你的实验室工具")
print("="*60)

# 练习0：导入模块（就像准备实验仪器）
# TODO: 导入random模块和collections模块的Counter
# 提示：import ... 和 from ... import ...
import random  # 用于随机选择
from collections import Counter  # 用于计数统计

print("✅ 模块导入成功！实验室工具准备就绪！")


# ========== 第1部分：列表操作（试管架管理） ==========
print("\n" + "="*60)
print("📝 练习1：管理DNA样品列表 ⭐")
print("="*60)

# 练习1.1：创建基因列表
print("\n1.1 创建你的基因列表")
# TODO: 创建一个包含5个癌症相关基因的列表
# 基因名：'TP53', 'KRAS', 'EGFR', 'BRAF', 'PIK3CA'
cancer_genes = ['TP53', 'KRAS', 'EGFR', 'BRAF', 'PIK3CA']  # 请补充完整
print(f"癌症基因列表: {cancer_genes}")

# 练习1.2：添加新基因
print("\n1.2 添加新发现的基因")
# TODO: 向列表末尾添加'MYC'基因
# 提示：使用append()方法
cancer_genes.append('MYC')  # 请补充代码
print(f"添加MYC后: {cancer_genes}")

# 练习1.3：插入基因
print("\n1.3 在特定位置插入基因")
# TODO: 在索引2的位置插入'ALK'基因
# 提示：使用insert(位置, 元素)方法
cancer_genes.insert(2, 'ALK')  # 请补充代码
print(f"插入ALK后: {cancer_genes}")

# 练习1.4：访问和修改
print("\n1.4 访问和修改基因")
# TODO: 1) 打印第一个基因
#       2) 打印最后一个基因
#       3) 将第二个基因改为'NRAS'
first_gene = cancer_genes[0]  # 请补充代码
last_gene = cancer_genes[-1]  # 请补充代码
cancer_genes[1] = 'NRAS'  # 请补充代码

print(f"第一个基因: {first_gene}")
print(f"最后一个基因: {last_gene}")
print(f"修改后的列表: {cancer_genes}")


# ========== 第2部分：字典操作（样品标签系统） ==========
print("\n" + "="*60)
print("📝 练习2：构建基因序列数据库 ⭐⭐")
print("="*60)

# 练习2.1：创建基因序列字典
print("\n2.1 创建基因-序列映射")
# TODO: 创建一个字典，包含3个基因及其序列
# 格式：{基因名: 序列}
gene_sequences = {
    'GAPDH': 'ATGGGAAAGGTGAAGGTC',  # 管家基因
    'ACTB': 'ATGGATGATGATATCGCC',   # β-肌动蛋白
    'TUBA1': 'ATGCGTGAGTGTATCTCC'   # α-微管蛋白
}  # 请补充完整

print("基因序列数据库:")
for gene, seq in gene_sequences.items():
    print(f"  {gene}: {seq}")

# 练习2.2：查找序列
print("\n2.2 通过基因名查找序列")
# TODO: 查找'GAPDH'基因的序列
# 提示：使用字典[键]或字典.get(键)
gapdh_seq = gene_sequences['GAPDH']  # 请补充代码
print(f"GAPDH序列: {gapdh_seq}")

# 练习2.3：添加新基因
print("\n2.3 添加新基因到数据库")
# TODO: 添加一个新基因'HSP90'，序列为'ATGGCCTCTGCTGAAGCC'
gene_sequences['HSP90'] = 'ATGGCCTCTGCTGAAGCC'  # 请补充代码
print(f"添加HSP90后，数据库有 {len(gene_sequences)} 个基因")

# 练习2.4：批量计算序列长度
print("\n2.4 计算所有序列长度")
# TODO: 创建一个新字典，存储每个基因的序列长度
# 格式：{基因名: 长度}
sequence_lengths = {}
for gene, seq in gene_sequences.items():
    sequence_lengths[gene] = len(seq)  # 请补充代码

print("序列长度统计:")
for gene, length in sequence_lengths.items():
    print(f"  {gene}: {length} bp")


# ========== 第3部分：密码子表构建 ==========
print("\n" + "="*60)
print("📝 练习3：构建简化密码子表 ⭐⭐⭐")
print("="*60)

# 练习3.1：创建密码子表
print("\n3.1 构建你的密码子表")
# TODO: 创建一个包含至少10个密码子的字典
# 必须包含：起始密码子ATG -> M，终止密码子TAA -> *
codon_table = {
    'ATG': 'M',  # 起始密码子（甲硫氨酸）
    'TAA': '*',  # 终止密码子
    'GCT': 'A',  # 丙氨酸
    'TGT': 'C',  # 半胱氨酸
    'GAT': 'D',  # 天冬氨酸
    'GAA': 'E',  # 谷氨酸
    'TTT': 'F',  # 苯丙氨酸
    'GGT': 'G',  # 甘氨酸
    'CAT': 'H',  # 组氨酸
    'AAA': 'K',  # 赖氨酸
}  # 请至少添加10个密码子

print(f"密码子表包含 {len(codon_table)} 个密码子")

# 练习3.2：翻译单个密码子
print("\n3.2 翻译密码子")
test_codons = ['ATG', 'GCT', 'TAA', 'AAA']
# TODO: 翻译每个密码子并打印结果
for codon in test_codons:
    amino_acid = codon_table.get(codon, '?')  # 请补充代码
    print(f"{codon} -> {amino_acid}")


# ========== 第4部分：DNA翻译实战 ==========
print("\n" + "="*60)
print("📝 练习4：实现DNA翻译 ⭐⭐⭐⭐")
print("="*60)

def translate_sequence(dna_sequence, codon_table):
    """
    将DNA序列翻译成蛋白质序列
    
    参数：
        dna_sequence: DNA序列字符串
        codon_table: 密码子表字典
    返回：
        蛋白质序列字符串
    """
    protein = []
    
    # TODO: 实现翻译逻辑
    # 步骤：
    # 1. 找到起始密码子ATG的位置
    # 2. 从起始密码子开始，每3个碱基读取一次
    # 3. 查找密码子表进行翻译
    # 4. 遇到终止密码子停止
    
    # 找到起始密码子
    start_pos = dna_sequence.find('ATG')
    if start_pos == -1:
        return "No start codon"
    
    # 从起始密码子开始翻译
    for i in range(start_pos, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]  # 请补充：提取3个碱基
        if len(codon) == 3:
            amino_acid = codon_table.get(codon, 'X')  # 请补充：查表翻译
            if amino_acid == '*':  # 遇到终止密码子
                break
            protein.append(amino_acid)
    
    return ''.join(protein)

# 测试翻译函数
test_dna = "GCAATGGCTAAAGAATAAGGG"
result = translate_sequence(test_dna, codon_table)
print(f"DNA序列: {test_dna}")
print(f"翻译结果: {result}")


# ========== 第5部分：综合应用 ==========
print("\n" + "="*60)
print("📝 练习5：基因表达数据分析 ⭐⭐⭐⭐⭐")
print("="*60)

# 练习5.1：创建基因表达数据
print("\n5.1 基因表达数据库")
# TODO: 创建一个嵌套字典，包含基因信息
# 每个基因应包含：name（全名）、expression（表达量）、type（类型）
gene_expression_db = {
    'TP53': {
        'name': 'Tumor protein p53',
        'expression': 125.3,
        'type': 'tumor_suppressor'
    },
    'MYC': {
        'name': 'MYC proto-oncogene',
        'expression': 234.5,
        'type': 'oncogene'
    },
    'GAPDH': {
        'name': 'Glyceraldehyde-3-phosphate dehydrogenase',
        'expression': 567.8,
        'type': 'housekeeping'
    }
    # TODO: 添加至少2个更多基因
}

# 练习5.2：数据分析
print("\n5.2 表达数据分析")
# TODO: 完成以下分析任务

# 1. 计算平均表达量
expression_values = [gene['expression'] for gene in gene_expression_db.values()]
avg_expression = sum(expression_values) / len(expression_values)  # 请补充代码
print(f"平均表达量: {avg_expression:.1f}")

# 2. 找出最高表达的基因
max_gene = None
max_value = 0
for gene_id, info in gene_expression_db.items():
    if info['expression'] > max_value:  # 请补充条件
        max_value = info['expression']
        max_gene = gene_id
print(f"最高表达基因: {max_gene} ({max_value})")

# 3. 按类型分组统计
type_groups = {}
for gene_id, info in gene_expression_db.items():
    gene_type = info['type']
    if gene_type not in type_groups:
        type_groups[gene_type] = []
    type_groups[gene_type].append(gene_id)  # 请补充代码

print("\n按类型分组:")
for gene_type, genes in type_groups.items():
    print(f"  {gene_type}: {genes}")


# ========== 挑战练习：批量序列分析 ==========
print("\n" + "="*60)
print("🏆 挑战练习：批量序列分析系统 ⭐⭐⭐⭐⭐⭐")
print("="*60)

def analyze_sequences(sequence_dict):
    """
    批量分析DNA序列，返回分析结果
    
    分析内容：
    1. 序列长度
    2. GC含量
    3. ATG（起始密码子）数量
    4. 最长的序列
    """
    results = {}
    
    # TODO: 实现批量分析
    for gene_id, sequence in sequence_dict.items():
        # 计算各项指标
        length = len(sequence)
        gc_count = sequence.count('G') + sequence.count('C')
        gc_content = (gc_count / length * 100) if length > 0 else 0
        atg_count = sequence.count('ATG')
        
        results[gene_id] = {
            'length': length,
            'gc_content': gc_content,
            'atg_count': atg_count
        }
    
    # 找出最长的序列
    if results:
        longest_gene = max(results.items(), key=lambda x: x[1]['length'])
        results['longest'] = longest_gene[0]
    
    return results

# 测试批量分析
test_sequences = {
    'Gene1': 'ATGGCGATCGATCGATCGATAA',
    'Gene2': 'ATGCCCGGGCCCATGATGTAA',
    'Gene3': 'GCGCGCATATGCGCGCTAA'
}

analysis_results = analyze_sequences(test_sequences)
print("序列分析结果:")
for gene_id, stats in analysis_results.items():
    if gene_id != 'longest':
        print(f"\n{gene_id}:")
        print(f"  长度: {stats['length']} bp")
        print(f"  GC含量: {stats['gc_content']:.1f}%")
        print(f"  起始密码子数: {stats['atg_count']}")

if 'longest' in analysis_results:
    print(f"\n最长的序列是: {analysis_results['longest']}")


# ========== 总结 ==========
print("\n" + "="*60)
print("🎊 练习完成情况总结")
print("="*60)

completed_exercises = [
    "✅ 热身：模块导入",
    "✅ 练习1：列表操作（试管架管理）",
    "✅ 练习2：字典操作（样品标签系统）",
    "✅ 练习3：密码子表构建",
    "✅ 练习4：DNA翻译实现",
    "✅ 练习5：基因表达数据分析",
    "✅ 挑战：批量序列分析系统"
]

print("完成的练习：")
for exercise in completed_exercises:
    print(f"  {exercise}")

print("\n💡 学习要点回顾：")
print("1. 列表适合有序数据的存储和遍历")
print("2. 字典适合键值对映射和快速查找")
print("3. 密码子表是生物信息学的核心数据结构")
print("4. 嵌套数据结构可以表示复杂的生物学信息")
print("5. 批量处理是生物信息学的常见需求")

print("\n🚀 下一步建议：")
print("1. 尝试构建完整的64个密码子表")
print("2. 实现反向互补序列功能")
print("3. 添加序列质量评分功能")
print("4. 学习使用Biopython处理更复杂的序列数据")

print("\n" + "="*60)
print("恭喜完成Chapter 02的所有练习！")
print("你已经掌握了生物数据管理的基础技能！")
print("="*60)