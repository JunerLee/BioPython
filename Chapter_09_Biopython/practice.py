#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 09: Biopython - 练习题

通过分级练习掌握Biopython的专业功能。
练习难度分为：基础、进阶、综合三个级别。
"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.SeqUtils import GC
import io


def practice_1_basic_seq():
    """
    练习1 [基础]: Seq对象基本操作
    
    任务：
    1. 创建DNA序列 "ATGCGATCGATCGATGCCC"
    2. 计算GC含量
    3. 进行转录和翻译
    4. 获取反向互补序列
    """
    print("🔍 练习1 [基础]: Seq对象基本操作")
    print("-" * 50)
    
    # TODO: 创建DNA序列对象
    # dna_seq = ?
    
    # TODO: 计算GC含量
    # gc_content = ?
    
    # TODO: 转录成RNA
    # rna_seq = ?
    
    # TODO: 翻译成蛋白质
    # protein_seq = ?
    
    # TODO: 获取反向互补序列
    # rev_comp = ?
    
    print("请完成上述任务...")


def practice_2_file_parsing():
    """
    练习2 [基础]: 文件解析与格式转换
    
    任务：
    1. 创建3条序列的FASTA文件（内存中）
    2. 解析文件并统计每条序列的长度和GC含量
    3. 将FASTA格式转换为其他格式
    """
    print("\n🔍 练习2 [基础]: 文件解析与格式转换")
    print("-" * 50)
    
    # 示例序列数据
    sequences_data = [
        ("gene1", "ATGGCCATTGTAATGGGCCGCTG", "Example gene 1"),
        ("gene2", "ATGCGATCGATCGATGCCCTAGC", "Example gene 2"),
        ("gene3", "ATGTTTAAACCCGGGATGAAATG", "Example gene 3")
    ]
    
    # TODO: 创建SeqRecord对象列表
    # records = []
    # for gene_id, seq_str, desc in sequences_data:
    #     record = ?
    #     records.append(record)
    
    # TODO: 写入FASTA格式
    # fasta_output = io.StringIO()
    # SeqIO.write(?, ?, ?)
    
    # TODO: 解析FASTA并分析
    # fasta_input = io.StringIO(fasta_output.getvalue())
    # for record in SeqIO.parse(?, ?):
    #     计算长度和GC含量
    
    print("请完成文件解析任务...")


def practice_2_bonus_real_data():
    """
    练习2加分题 [基础]: 使用真实生物数据
    
    任务：
    1. 读取data目录中的真实FASTA文件
    2. 分析每个基因的基本特征
    3. 比较不同基因的序列特点
    4. 识别最保守和最多样化的区域
    """
    print("\n🎯 练习2加分题 [基础]: 使用真实生物数据")
    print("-" * 50)
    
    import os
    
    # 真实数据文件路径
    fasta_file = os.path.join("..", "data", "dna_sequence.fasta")
    
    print(f"尝试读取文件: {fasta_file}")
    
    # TODO: 检查文件是否存在
    # if not os.path.exists(fasta_file):
    #     print(f"❌ 文件未找到: {fasta_file}")
    #     print("提示：请确保运行目录正确，或使用相对路径")
    #     return
    
    # TODO: 解析真实FASTA文件
    # try:
    #     records = list(SeqIO.parse(fasta_file, "fasta"))
    #     print(f"✅ 成功读取 {len(records)} 条序列")
    # except Exception as e:
    #     print(f"❌ 读取文件时出错: {e}")
    #     return
    
    # TODO: 分析每个基因序列
    # for i, record in enumerate(records, 1):
    #     print(f"\n--- 基因 {i}: {record.id} ---")
    #     print(f"描述: {record.description}")
    #     print(f"序列长度: {len(record.seq)} bp")
    #     print(f"GC含量: {GC(record.seq):.2f}%")
    #     print(f"序列预览: {record.seq[:50]}...")
    #     
    #     # 分析序列组成
    #     seq_str = str(record.seq)
    #     a_count = seq_str.count('A')
    #     t_count = seq_str.count('T') 
    #     g_count = seq_str.count('G')
    #     c_count = seq_str.count('C')
    #     print(f"碱基组成: A={a_count}, T={t_count}, G={g_count}, C={c_count}")
    
    # TODO: 比较分析
    # 找出最长/最短序列
    # 计算所有序列的平均GC含量
    # 识别共同的序列特征
    
    print("\n💡 分析提示:")
    print("1. BRCA1和TP53是重要的肿瘤抑制基因")
    print("2. GAPDH和ACTB是常用的管家基因")
    print("3. VEGFA与血管生成相关")
    print("4. 比较不同功能基因的序列特征差异")
    print("5. 思考：为什么管家基因通常GC含量较高？")
    
    print("请完成真实数据分析任务...")


def practice_3_orf_finding():
    """
    练习3 [进阶]: 开放阅读框(ORF)查找
    
    任务：
    1. 在给定序列中查找所有ORF
    2. 翻译每个ORF为蛋白质
    3. 找出最长的ORF
    """
    print("\n🔍 练习3 [进阶]: ORF查找")
    print("-" * 50)
    
    # 包含多个ORF的序列
    genomic_seq = Seq(
        "AGCCATGCCGAATTCGATGCCCAAATAATGAGCGGGCTTAAATAGGCTGAATAAGGAAGTAA"
    )
    
    print(f"基因组序列: {genomic_seq}")
    print(f"序列长度: {len(genomic_seq)} bp")
    
    # TODO: 实现ORF查找算法
    # def find_orfs(sequence):
    #     orfs = []
    #     # 查找ATG起始密码子
    #     # 查找TAA, TAG, TGA终止密码子
    #     # 返回所有ORF
    #     return orfs
    
    print("请实现ORF查找功能...")


def practice_4_restriction_sites():
    """
    练习4 [进阶]: 限制性酶切位点分析
    
    任务：
    1. 查找常见限制性酶的切割位点
    2. 计算酶切后的片段大小
    3. 设计克隆策略
    """
    print("\n🔍 练习4 [进阶]: 限制性酶切分析")
    print("-" * 50)
    
    # 质粒序列
    plasmid = Seq("GAATTCGCGGCCGCGTCGACAAGCTTGCATGCCTGCAGGTCGACTCTAGAGGATCCCCGGG")
    
    # 常见限制性酶识别序列
    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT",
        "PstI": "CTGCAG",
        "SalI": "GTCGAC"
    }
    
    # TODO: 查找每个酶的切割位点
    # for enzyme_name, site in enzymes.items():
    #     positions = ?
    #     print(f"{enzyme_name}: {positions}")
    
    # TODO: 计算双酶切片段大小
    
    print("请完成限制性酶切分析...")


def practice_5_protein_analysis():
    """
    练习5 [进阶]: 蛋白质序列分析
    
    任务：
    1. 计算蛋白质的分子量
    2. 计算等电点(pI)
    3. 分析氨基酸组成
    4. 预测二级结构
    """
    print("\n🔍 练习5 [进阶]: 蛋白质分析")
    print("-" * 50)
    
    # 示例蛋白质序列（胰岛素B链）
    insulin_b = Seq("FVNQHLCGSHLVEALYLVCGERGFFYTPKT")
    
    print(f"胰岛素B链: {insulin_b}")
    print(f"长度: {len(insulin_b)} aa")
    
    # TODO: 使用ProteinAnalysis分析
    # from Bio.SeqUtils.ProtParam import ProteinAnalysis
    # protein_analysis = ProteinAnalysis(str(insulin_b))
    
    # TODO: 计算分子量
    # mw = ?
    
    # TODO: 计算等电点
    # pi = ?
    
    # TODO: 分析氨基酸组成
    # aa_percent = ?
    
    print("请完成蛋白质分析任务...")


def practice_6_sequence_alignment():
    """
    练习6 [综合]: 序列比对分析
    
    任务：
    1. 比较多条相似序列
    2. 识别保守区域
    3. 计算序列相似度
    """
    print("\n🔍 练习6 [综合]: 序列比对分析")
    print("-" * 50)
    
    # 相似序列集合
    sequences = [
        Seq("ATGGCCATTGTAATGGGCCGCTG"),
        Seq("ATGGCCATTGTTATGGGCCGCTG"),
        Seq("ATGGCCATTGTAATGGGCAGCTG"),
        Seq("ATGGCCATTGTAATGGGCCGCTT")
    ]
    
    print("序列集合:")
    for i, seq in enumerate(sequences, 1):
        print(f"Seq{i}: {seq}")
    
    # TODO: 实现简单的序列比对
    # def simple_alignment(seq1, seq2):
    #     matches = 0
    #     for i in range(min(len(seq1), len(seq2))):
    #         if seq1[i] == seq2[i]:
    #             matches += 1
    #     similarity = matches / max(len(seq1), len(seq2)) * 100
    #     return similarity
    
    # TODO: 计算所有序列对的相似度
    
    print("请实现序列比对分析...")


def practice_7_genome_annotation():
    """
    练习7 [综合]: 基因组注释工作流
    
    任务：
    1. 预测基因位置（ORF）
    2. 翻译成蛋白质
    3. 预测功能
    4. 生成注释文件
    """
    print("\n🔍 练习7 [综合]: 基因组注释")
    print("-" * 50)
    
    # 模拟小基因组片段
    genome_fragment = Seq(
        "TTACGATGCCGAATTCGATGCCCAAATAATGAGCGGGCTTAAATAGGCTGAATAAGGAAG"
        "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGCCATTGTAATGGGCCGCTGAT"
    )
    
    print(f"基因组片段长度: {len(genome_fragment)} bp")
    
    # TODO: Step 1 - 查找所有ORF
    # orfs = find_all_orfs(genome_fragment)
    
    # TODO: Step 2 - 翻译ORF
    # proteins = [orf.translate() for orf in orfs]
    
    # TODO: Step 3 - 创建注释记录
    # from Bio.SeqFeature import SeqFeature, FeatureLocation
    # features = []
    # for orf_info in orfs:
    #     feature = SeqFeature(...)
    #     features.append(feature)
    
    # TODO: Step 4 - 生成GenBank格式
    
    print("请完成基因组注释流程...")


def practice_8_blast_search():
    """
    练习8 [综合]: BLAST搜索模拟
    
    任务：
    1. 创建本地序列数据库
    2. 实现简单的序列相似性搜索
    3. 计算E-value（简化版）
    4. 返回最佳匹配
    """
    print("\n🔍 练习8 [综合]: BLAST搜索模拟")
    print("-" * 50)
    
    # 查询序列
    query = Seq("ATGGCCATTGTAATGGGCC")
    
    # 数据库序列
    database = [
        ("seq1", Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")),
        ("seq2", Seq("ATGCGATCGATCGATGCCCTAGCTAGCTAGCTAGCTAGC")),
        ("seq3", Seq("ATGGCCATTGTTATGGGCCGCTGAAAGGGTGCCCGATAG")),
        ("seq4", Seq("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"))
    ]
    
    print(f"查询序列: {query}")
    print(f"数据库包含 {len(database)} 条序列")
    
    # TODO: 实现序列搜索算法
    # def blast_search(query, database):
    #     results = []
    #     for seq_id, subject in database:
    #         # 计算相似度分数
    #         # 计算E-value（简化）
    #         # 添加到结果
    #     return sorted(results, key=lambda x: x['score'], reverse=True)
    
    print("请实现BLAST搜索功能...")


def practice_9_phylogenetic_analysis():
    """
    练习9 [综合]: 系统发育分析
    
    任务：
    1. 计算序列间的进化距离
    2. 构建距离矩阵
    3. 生成简单的进化树
    """
    print("\n🔍 练习9 [综合]: 系统发育分析")
    print("-" * 50)
    
    # 物种序列集合
    species_sequences = {
        "Human": Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"),
        "Chimp": Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"),
        "Mouse": Seq("ATGGCCATTGTTATGGGCAGCTGAAAGGGTGCCCGATAG"),
        "Rat":   Seq("ATGGCCATTGTTATGGGCAGCTGAAAGGGTGCCCGATAG"),
        "Fly":   Seq("ATGGCAATTGTGATGGGTCGCTGAAAGGATGCCCGATAG")
    }
    
    print("物种序列:")
    for species, seq in species_sequences.items():
        print(f"{species:8}: {seq[:20]}...")
    
    # TODO: 计算成对距离
    # def calculate_distance(seq1, seq2):
    #     differences = sum(1 for a, b in zip(seq1, seq2) if a != b)
    #     return differences / len(seq1)
    
    # TODO: 构建距离矩阵
    # distance_matrix = {}
    # for sp1 in species_sequences:
    #     for sp2 in species_sequences:
    #         distance = calculate_distance(...)
    
    # TODO: 使用UPGMA算法构建树（简化版）
    
    print("请完成系统发育分析...")


def practice_10_complete_pipeline():
    """
    练习10 [综合项目]: 完整的基因分析流程
    
    任务：
    构建一个从原始序列到功能注释的完整分析流程
    1. 读取序列文件
    2. 质量控制
    3. 基因预测
    4. 功能注释
    5. 生成报告
    """
    print("\n🔍 练习10 [综合项目]: 完整分析流程")
    print("-" * 50)
    
    # 模拟输入数据
    raw_sequence = Seq(
        "NNNATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGNNNN"
        "ATGCGATCGATCGATGCCCTAGCTAGCTAGCTAGCTAGCNNN"
        "ATGTTTAAACCCGGGATGAAATGAAATAGGCTGAATAAGGAAGTAA"
    )
    
    print(f"原始序列长度: {len(raw_sequence)} bp")
    print(f"序列预览: {raw_sequence[:30]}...")
    
    # TODO: Step 1 - 质量控制
    # def quality_control(sequence):
    #     # 去除N碱基
    #     # 检查序列有效性
    #     # 返回清洁序列
    
    # TODO: Step 2 - 基因预测
    # def predict_genes(sequence):
    #     # 查找ORF
    #     # 评分和筛选
    #     # 返回预测基因
    
    # TODO: Step 3 - 功能注释
    # def annotate_genes(genes):
    #     # 序列相似性搜索
    #     # 功能域预测
    #     # GO注释
    
    # TODO: Step 4 - 生成报告
    # def generate_report(analysis_results):
    #     # 汇总统计信息
    #     # 格式化输出
    #     # 保存结果
    
    print("请构建完整的分析流程...")


def main():
    """
    主函数 - 运行所有练习
    """
    print("🧬 Chapter 09: Biopython 练习题")
    print("=" * 60)
    print("通过分级练习掌握Biopython的专业功能\n")
    
    # 基础练习
    print("=" * 60)
    print("📘 基础练习（适合初学者）")
    print("=" * 60)
    practice_1_basic_seq()
    practice_2_file_parsing()
    practice_2_bonus_real_data()
    
    # 进阶练习
    print("\n" + "=" * 60)
    print("📙 进阶练习（适合有经验者）")
    print("=" * 60)
    practice_3_orf_finding()
    practice_4_restriction_sites()
    practice_5_protein_analysis()
    
    # 综合练习
    print("\n" + "=" * 60)
    print("📕 综合练习（适合高级用户）")
    print("=" * 60)
    practice_6_sequence_alignment()
    practice_7_genome_annotation()
    practice_8_blast_search()
    practice_9_phylogenetic_analysis()
    practice_10_complete_pipeline()
    
    print("\n" + "=" * 60)
    print("💡 练习提示:")
    print("=" * 60)
    print("1. 从基础练习开始，逐步提升难度")
    print("2. 每个练习都有具体的任务要求")
    print("3. 参考main.py中的示例代码")
    print("4. 完成后对比practice_solution.py的答案")
    print("5. 尝试优化和扩展你的解决方案")
    
    print("\n📚 学习建议:")
    print("• 基础练习: 掌握Biopython的核心对象和方法")
    print("• 进阶练习: 学会使用专业的生物信息学功能")
    print("• 综合练习: 能够构建完整的分析流程")
    print("• 最终目标: 独立解决实际的生物信息学问题")


if __name__ == "__main__":
    main()