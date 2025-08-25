#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 09: Biopython - 练习题参考答案

完整的练习题解答，包含详细的注释和多种解决方案。
"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.SeqUtils import GC, molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Restriction import *
import io
import math


def practice_1_basic_seq_solution():
    """
    练习1答案: Seq对象基本操作
    
    生物学类比：就像在实验室中处理DNA样本 - 
    提取、转录、翻译、反向互补等基本操作
    """
    print("🔍 练习1 [基础]: Seq对象基本操作 - 参考答案")
    print("-" * 50)
    
    # 创建DNA序列对象
    dna_seq = Seq("ATGCGATCGATCGATGCCC")
    print(f"DNA序列: {dna_seq}")
    
    # 计算GC含量
    gc_content = GC(dna_seq)
    print(f"GC含量: {gc_content:.2f}%")
    
    # 转录成RNA
    rna_seq = dna_seq.transcribe()
    print(f"RNA序列: {rna_seq}")
    
    # 翻译成蛋白质
    protein_seq = dna_seq.translate()
    print(f"蛋白质序列: {protein_seq}")
    
    # 获取反向互补序列
    rev_comp = dna_seq.reverse_complement()
    print(f"反向互补: {rev_comp}")
    
    # 额外分析
    print("\n额外分析:")
    print(f"序列长度: {len(dna_seq)} bp")
    print(f"A碱基数: {dna_seq.count('A')}")
    print(f"起始密码子位置: {dna_seq.find('ATG')}")
    
    # 六框翻译
    print("\n六框翻译:")
    for frame in range(3):
        print(f"正向框{frame}: {dna_seq[frame:].translate()}")
    for frame in range(3):
        print(f"反向框{frame}: {rev_comp[frame:].translate()}")


def practice_2_file_parsing_solution():
    """
    练习2答案: 文件解析与格式转换
    
    生物学类比：像实验室的数据管理系统 - 
    存储、读取、转换不同格式的序列数据
    """
    print("\n🔍 练习2 [基础]: 文件解析与格式转换 - 参考答案")
    print("-" * 50)
    
    # 示例序列数据
    sequences_data = [
        ("gene1", "ATGGCCATTGTAATGGGCCGCTG", "Example gene 1"),
        ("gene2", "ATGCGATCGATCGATGCCCTAGC", "Example gene 2"),
        ("gene3", "ATGTTTAAACCCGGGATGAAATG", "Example gene 3")
    ]
    
    # 创建SeqRecord对象列表
    records = []
    for gene_id, seq_str, desc in sequences_data:
        record = SeqRecord(
            Seq(seq_str),
            id=gene_id,
            description=desc
        )
        records.append(record)
    
    # 写入FASTA格式
    fasta_output = io.StringIO()
    SeqIO.write(records, fasta_output, "fasta")
    fasta_string = fasta_output.getvalue()
    
    print("生成的FASTA文件:")
    print(fasta_string)
    
    # 解析FASTA并分析
    fasta_input = io.StringIO(fasta_string)
    print("序列分析结果:")
    print("-" * 30)
    for record in SeqIO.parse(fasta_input, "fasta"):
        length = len(record.seq)
        gc = GC(record.seq)
        print(f"{record.id}:")
        print(f"  长度: {length} bp")
        print(f"  GC含量: {gc:.2f}%")
        print(f"  蛋白质: {record.seq.translate()}")
    
    # 格式转换示例 - 转换为GenBank格式
    print("\nGenBank格式转换:")
    for record in records[:1]:  # 只展示第一条
        record.annotations["molecule_type"] = "DNA"
        record.annotations["organism"] = "Unknown"
        genbank_output = io.StringIO()
        SeqIO.write([record], genbank_output, "genbank")
        print(genbank_output.getvalue()[:200] + "...")


def practice_2_bonus_real_data_solution():
    """
    练习2加分题答案: 使用真实生物数据
    
    生物学类比：这就像分析实验室收到的真实样本 - 
    每个基因都有其独特的"指纹"和生物学功能
    """
    print("\n🎯 练习2加分题 [基础]: 使用真实生物数据 - 参考答案")
    print("-" * 50)
    
    import os
    
    # 真实数据文件路径
    fasta_file = os.path.join("..", "data", "dna_sequence.fasta")
    
    print(f"尝试读取文件: {fasta_file}")
    
    # 检查文件是否存在
    if not os.path.exists(fasta_file):
        print(f"❌ 文件未找到: {fasta_file}")
        print("提示：请确保运行目录正确，或使用相对路径")
        return
    
    # 解析真实FASTA文件
    try:
        records = list(SeqIO.parse(fasta_file, "fasta"))
        print(f"✅ 成功读取 {len(records)} 条序列\n")
    except Exception as e:
        print(f"❌ 读取文件时出错: {e}")
        return
    
    # 存储分析结果
    gene_stats = []
    
    # 分析每个基因序列
    for i, record in enumerate(records, 1):
        print(f"--- 基因 {i}: {record.id} ---")
        print(f"描述: {record.description}")
        
        seq_len = len(record.seq)
        gc_content = GC(record.seq)
        
        print(f"序列长度: {seq_len} bp")
        print(f"GC含量: {gc_content:.2f}%")
        print(f"序列预览: {record.seq[:50]}...")
        
        # 分析序列组成
        seq_str = str(record.seq)
        a_count = seq_str.count('A')
        t_count = seq_str.count('T') 
        g_count = seq_str.count('G')
        c_count = seq_str.count('C')
        n_count = seq_str.count('N')
        
        print(f"碱基组成: A={a_count}, T={t_count}, G={g_count}, C={c_count}")
        if n_count > 0:
            print(f"未知碱基(N): {n_count}")
        
        # 计算AT/GC比例
        at_content = (a_count + t_count) / seq_len * 100
        print(f"AT含量: {at_content:.2f}%")
        
        # 检查起始和终止密码子
        starts_with_atg = str(record.seq[:3]) == 'ATG'
        ends_with_stop = str(record.seq[-3:]) in ['TAA', 'TAG', 'TGA']
        
        print(f"以ATG起始: {'是' if starts_with_atg else '否'}")
        print(f"以终止密码子结尾: {'是' if ends_with_stop else '否'}")
        
        # 存储统计信息
        gene_stats.append({
            'id': record.id,
            'description': record.description,
            'length': seq_len,
            'gc_content': gc_content,
            'starts_with_atg': starts_with_atg
        })
        
        print()
    
    # 比较分析
    print("=== 比较分析 ===")
    
    # 找出最长/最短序列
    longest = max(gene_stats, key=lambda x: x['length'])
    shortest = min(gene_stats, key=lambda x: x['length'])
    
    print(f"最长序列: {longest['id']} ({longest['length']} bp)")
    print(f"最短序列: {shortest['id']} ({shortest['length']} bp)")
    
    # 计算平均GC含量
    avg_gc = sum(g['gc_content'] for g in gene_stats) / len(gene_stats)
    print(f"平均GC含量: {avg_gc:.2f}%")
    
    # 识别管家基因特征
    housekeeping_genes = ['GAPDH', 'ACTB']  # 管家基因
    tumor_genes = ['BRCA1', 'TP53']         # 肿瘤相关基因
    
    print("\n--- 功能分类分析 ---")
    for gene in gene_stats:
        gene_name = gene['id'].split('_')[1] if '_' in gene['id'] else gene['id']
        
        if any(hk in gene_name for hk in housekeeping_genes):
            print(f"🏠 {gene_name}: 管家基因 (GC: {gene['gc_content']:.1f}%)")
        elif any(tg in gene_name for tg in tumor_genes):
            print(f"🎯 {gene_name}: 肿瘤相关基因 (GC: {gene['gc_content']:.1f}%)")
        else:
            print(f"🧬 {gene_name}: 其他功能基因 (GC: {gene['gc_content']:.1f}%)")
    
    print("\n💡 生物学洞察:")
    print("1. 管家基因(GAPDH, ACTB)通常GC含量较高，表达更稳定")
    print("2. 肿瘤抑制基因(BRCA1, TP53)长度较长，结构复杂")
    print("3. 不同功能基因的序列特征反映其生物学作用")
    print("4. 序列长度和GC含量是基因功能分类的重要指标")


def practice_3_orf_finding_solution():
    """
    练习3答案: 开放阅读框(ORF)查找
    
    生物学类比：像在基因组中寻找基因 - 
    识别起始和终止密码子之间的编码区域
    """
    print("\n🔍 练习3 [进阶]: ORF查找 - 参考答案")
    print("-" * 50)
    
    # 包含多个ORF的序列
    genomic_seq = Seq(
        "AGCCATGCCGAATTCGATGCCCAAATAATGAGCGGGCTTAAATAGGCTGAATAAGGAAGTAA"
    )
    
    print(f"基因组序列: {genomic_seq}")
    print(f"序列长度: {len(genomic_seq)} bp\n")
    
    def find_orfs(sequence, min_length=6):
        """查找所有可能的ORF"""
        orfs = []
        seq_len = len(sequence)
        
        # 检查三个阅读框
        for frame in range(3):
            for i in range(frame, seq_len - 2, 3):
                codon = sequence[i:i+3]
                # 查找起始密码子
                if str(codon) == 'ATG':
                    # 查找终止密码子
                    for j in range(i + 3, seq_len - 2, 3):
                        stop_codon = sequence[j:j+3]
                        if str(stop_codon) in ['TAA', 'TAG', 'TGA']:
                            orf_seq = sequence[i:j+3]
                            if len(orf_seq) >= min_length:
                                protein = orf_seq.translate()
                                orfs.append({
                                    'frame': frame,
                                    'start': i,
                                    'end': j+3,
                                    'length': len(orf_seq),
                                    'sequence': orf_seq,
                                    'protein': protein
                                })
                            break
        return orfs
    
    # 查找ORF
    orfs = find_orfs(genomic_seq)
    
    if orfs:
        print(f"找到 {len(orfs)} 个ORF:")
        for i, orf in enumerate(orfs, 1):
            print(f"\nORF {i}:")
            print(f"  位置: {orf['start']}-{orf['end']}")
            print(f"  阅读框: {orf['frame']}")
            print(f"  长度: {orf['length']} bp")
            print(f"  DNA: {orf['sequence']}")
            print(f"  蛋白质: {orf['protein']}")
        
        # 找出最长的ORF
        longest_orf = max(orfs, key=lambda x: x['length'])
        print(f"\n最长的ORF:")
        print(f"  位置: {longest_orf['start']}-{longest_orf['end']}")
        print(f"  长度: {longest_orf['length']} bp")
        print(f"  蛋白质: {longest_orf['protein']}")
    else:
        print("未找到ORF")


def practice_4_restriction_sites_solution():
    """
    练习4答案: 限制性酶切位点分析
    
    生物学类比：像分子克隆实验 - 
    选择合适的限制性内切酶进行DNA切割和连接
    """
    print("\n🔍 练习4 [进阶]: 限制性酶切分析 - 参考答案")
    print("-" * 50)
    
    # 质粒序列
    plasmid = Seq("GAATTCGCGGCCGCGTCGACAAGCTTGCATGCCTGCAGGTCGACTCTAGAGGATCCCCGGG")
    print(f"质粒序列: {plasmid}")
    print(f"序列长度: {len(plasmid)} bp\n")
    
    # 常见限制性酶识别序列
    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT",
        "PstI": "CTGCAG",
        "SalI": "GTCGAC",
        "NotI": "GCGGCCGC"
    }
    
    # 查找每个酶的切割位点
    enzyme_sites = {}
    print("限制性酶切位点:")
    for enzyme_name, site in enzymes.items():
        positions = []
        seq_str = str(plasmid)
        start = 0
        while True:
            pos = seq_str.find(site, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        
        enzyme_sites[enzyme_name] = positions
        if positions:
            print(f"{enzyme_name:8} ({site}): 位点 {positions}")
        else:
            print(f"{enzyme_name:8} ({site}): 无切割位点")
    
    # 计算双酶切片段大小
    print("\n双酶切策略分析:")
    if "EcoRI" in enzyme_sites and enzyme_sites["EcoRI"]:
        if "BamHI" in enzyme_sites and enzyme_sites["BamHI"]:
            eco_site = enzyme_sites["EcoRI"][0]
            bam_site = enzyme_sites["BamHI"][0]
            
            if eco_site < bam_site:
                fragment_size = bam_site - eco_site
                insert = plasmid[eco_site:bam_site]
                print(f"EcoRI-BamHI双酶切:")
                print(f"  EcoRI位点: {eco_site}")
                print(f"  BamHI位点: {bam_site}")
                print(f"  插入片段大小: {fragment_size} bp")
                print(f"  插入片段序列: {insert}")
                
                # 设计克隆策略
                print(f"\n克隆策略建议:")
                print(f"1. 用EcoRI和BamHI双酶切载体")
                print(f"2. 插入片段需要相容的末端")
                print(f"3. 片段大小 {fragment_size} bp 适合克隆")
                print(f"4. 可以使用T4 DNA连接酶连接")


def practice_5_protein_analysis_solution():
    """
    练习5答案: 蛋白质序列分析
    
    生物学类比：像蛋白质表征实验 - 
    测定分子量、等电点、氨基酸组成等理化性质
    """
    print("\n🔍 练习5 [进阶]: 蛋白质分析 - 参考答案")
    print("-" * 50)
    
    # 示例蛋白质序列（胰岛素B链）
    insulin_b = Seq("FVNQHLCGSHLVEALYLVCGERGFFYTPKT")
    print(f"胰岛素B链: {insulin_b}")
    print(f"长度: {len(insulin_b)} aa\n")
    
    # 使用ProteinAnalysis分析
    protein_analysis = ProteinAnalysis(str(insulin_b))
    
    # 计算分子量
    mw = protein_analysis.molecular_weight()
    print(f"分子量: {mw:.2f} Da")
    
    # 计算等电点
    pi = protein_analysis.isoelectric_point()
    print(f"等电点(pI): {pi:.2f}")
    
    # 计算不稳定性指数
    instability = protein_analysis.instability_index()
    print(f"不稳定性指数: {instability:.2f}")
    if instability < 40:
        print("  -> 蛋白质稳定")
    else:
        print("  -> 蛋白质不稳定")
    
    # 分析氨基酸组成
    print("\n氨基酸组成:")
    aa_percent = protein_analysis.get_amino_acids_percent()
    for aa in sorted(aa_percent.keys()):
        if aa_percent[aa] > 0:
            count = str(insulin_b).count(aa)
            print(f"  {aa}: {count:2d} ({aa_percent[aa]*100:5.1f}%)")
    
    # 二级结构预测
    helix, turn, sheet = protein_analysis.secondary_structure_fraction()
    print(f"\n二级结构预测:")
    print(f"  α-螺旋: {helix*100:.1f}%")
    print(f"  β-折叠: {sheet*100:.1f}%")
    print(f"  转角: {turn*100:.1f}%")
    
    # 亲疏水性分析
    print(f"\n亲疏水性分析:")
    print(f"  GRAVY值: {protein_analysis.gravy():.3f}")
    if protein_analysis.gravy() < 0:
        print("  -> 亲水性蛋白")
    else:
        print("  -> 疏水性蛋白")


def practice_6_sequence_alignment_solution():
    """
    练习6答案: 序列比对分析
    
    生物学类比：像比较不同物种的同源基因 - 
    识别保守区域和变异位点
    """
    print("\n🔍 练习6 [综合]: 序列比对分析 - 参考答案")
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
    
    def simple_alignment(seq1, seq2):
        """计算两条序列的相似度"""
        matches = 0
        for i in range(min(len(seq1), len(seq2))):
            if seq1[i] == seq2[i]:
                matches += 1
        similarity = matches / max(len(seq1), len(seq2)) * 100
        return similarity, matches
    
    # 计算所有序列对的相似度
    print("\n成对序列相似度矩阵:")
    print("     ", end="")
    for i in range(len(sequences)):
        print(f"Seq{i+1:1d}  ", end="")
    print()
    
    similarity_matrix = []
    for i in range(len(sequences)):
        print(f"Seq{i+1:1d} ", end="")
        row = []
        for j in range(len(sequences)):
            if i == j:
                sim = 100.0
            else:
                sim, _ = simple_alignment(sequences[i], sequences[j])
            row.append(sim)
            print(f"{sim:5.1f} ", end="")
        similarity_matrix.append(row)
        print()
    
    # 识别保守位点
    print("\n保守位点分析:")
    conserved_positions = []
    for pos in range(min(len(seq) for seq in sequences)):
        bases = [str(seq[pos]) for seq in sequences]
        if len(set(bases)) == 1:
            conserved_positions.append((pos, bases[0]))
    
    print(f"发现 {len(conserved_positions)} 个完全保守的位点:")
    for pos, base in conserved_positions[:10]:  # 只显示前10个
        print(f"  位置 {pos:2d}: {base}")
    
    # 识别变异位点
    variable_positions = []
    for pos in range(min(len(seq) for seq in sequences)):
        bases = [str(seq[pos]) for seq in sequences]
        if len(set(bases)) > 1:
            variable_positions.append((pos, bases))
    
    print(f"\n发现 {len(variable_positions)} 个变异位点:")
    for pos, bases in variable_positions[:5]:  # 只显示前5个
        print(f"  位置 {pos:2d}: {' '.join(bases)}")


def practice_7_genome_annotation_solution():
    """
    练习7答案: 基因组注释工作流
    
    生物学类比：像给新测序的基因组做功能注释 - 
    预测基因、分析功能、创建注释文件
    """
    print("\n🔍 练习7 [综合]: 基因组注释 - 参考答案")
    print("-" * 50)
    
    # 模拟小基因组片段
    genome_fragment = Seq(
        "TTACGATGCCGAATTCGATGCCCAAATAATGAGCGGGCTTAAATAGGCTGAATAAGGAAG"
        "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGCCATTGTAATGGGCCGCTGAT"
    )
    
    print(f"基因组片段长度: {len(genome_fragment)} bp\n")
    
    def find_all_orfs(sequence, min_length=9):
        """查找所有ORF"""
        orfs = []
        for strand, seq in [("+", sequence), ("-", sequence.reverse_complement())]:
            for frame in range(3):
                for i in range(frame, len(seq) - 2, 3):
                    if str(seq[i:i+3]) == 'ATG':
                        for j in range(i + 3, len(seq) - 2, 3):
                            if str(seq[j:j+3]) in ['TAA', 'TAG', 'TGA']:
                                if j + 3 - i >= min_length:
                                    orfs.append({
                                        'strand': strand,
                                        'frame': frame,
                                        'start': i if strand == "+" else len(sequence) - j - 3,
                                        'end': j + 3 if strand == "+" else len(sequence) - i,
                                        'sequence': seq[i:j+3],
                                        'protein': seq[i:j+3].translate()
                                    })
                                break
        return orfs
    
    # Step 1 - 查找所有ORF
    orfs = find_all_orfs(genome_fragment)
    print(f"Step 1: 找到 {len(orfs)} 个ORF")
    
    # Step 2 - 分析每个ORF
    print("\nStep 2: ORF分析")
    for i, orf in enumerate(orfs[:3], 1):  # 只显示前3个
        print(f"\nORF {i}:")
        print(f"  链: {orf['strand']}")
        print(f"  位置: {orf['start']}-{orf['end']}")
        print(f"  长度: {len(orf['sequence'])} bp")
        print(f"  蛋白质: {orf['protein']}")
        print(f"  蛋白质长度: {len(orf['protein'])} aa")
    
    # Step 3 - 创建注释记录
    print("\nStep 3: 创建基因组注释")
    
    gene_record = SeqRecord(
        genome_fragment,
        id="genome_fragment_001",
        name="Fragment001",
        description="Annotated genome fragment"
    )
    
    # 添加特征注释
    for i, orf in enumerate(orfs[:3], 1):
        # 创建基因特征
        gene_feature = SeqFeature(
            FeatureLocation(orf['start'], orf['end']),
            type="gene",
            strand=1 if orf['strand'] == "+" else -1,
            qualifiers={
                "gene": f"ORF{i:03d}",
                "locus_tag": f"FRAG001_{i:03d}"
            }
        )
        gene_record.features.append(gene_feature)
        
        # 创建CDS特征
        cds_feature = SeqFeature(
            FeatureLocation(orf['start'], orf['end']),
            type="CDS",
            strand=1 if orf['strand'] == "+" else -1,
            qualifiers={
                "gene": f"ORF{i:03d}",
                "translation": str(orf['protein']),
                "product": "hypothetical protein"
            }
        )
        gene_record.features.append(cds_feature)
    
    print(f"添加了 {len(gene_record.features)} 个特征注释")
    
    # Step 4 - 生成注释报告
    print("\nStep 4: 注释报告摘要")
    print(f"序列ID: {gene_record.id}")
    print(f"序列长度: {len(gene_record.seq)} bp")
    print(f"GC含量: {GC(gene_record.seq):.2f}%")
    print(f"预测基因数: {len([f for f in gene_record.features if f.type == 'gene'])}")
    print(f"CDS总长度: {sum(len(f) for f in gene_record.features if f.type == 'CDS')} bp")


def practice_8_blast_search_solution():
    """
    练习8答案: BLAST搜索模拟
    
    生物学类比：像在基因数据库中搜索相似序列 - 
    找到同源基因或功能相关的序列
    """
    print("\n🔍 练习8 [综合]: BLAST搜索模拟 - 参考答案")
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
    print(f"查询长度: {len(query)} bp")
    print(f"数据库大小: {len(database)} 条序列\n")
    
    def blast_search(query, database):
        """简化的BLAST搜索算法"""
        results = []
        query_len = len(query)
        db_size = sum(len(seq) for _, seq in database)
        
        for seq_id, subject in database:
            # 计算匹配分数
            matches = 0
            mismatches = 0
            for i in range(min(len(query), len(subject))):
                if i < len(query) and query[i] == subject[i]:
                    matches += 1
                else:
                    mismatches += 1
            
            # 计算得分（简化版）
            score = matches * 2 - mismatches
            
            # 计算相似度百分比
            identity = (matches / query_len) * 100 if query_len > 0 else 0
            
            # 计算E-value（极简化版）
            # E = K * m * n * exp(-λ * S)
            # 这里使用简化公式
            e_value = db_size * query_len * math.exp(-0.1 * score) if score > 0 else 1000
            
            results.append({
                'id': seq_id,
                'score': score,
                'identity': identity,
                'e_value': e_value,
                'matches': matches,
                'length': len(subject),
                'alignment': f"{str(query)[:20]}...\n{str(subject)[:20]}..."
            })
        
        # 按分数排序
        return sorted(results, key=lambda x: x['score'], reverse=True)
    
    # 执行搜索
    results = blast_search(query, database)
    
    print("BLAST搜索结果:")
    print("-" * 60)
    print(f"{'ID':<8} {'Score':<8} {'Identity':<10} {'E-value':<12} {'Length':<8}")
    print("-" * 60)
    
    for hit in results:
        print(f"{hit['id']:<8} {hit['score']:<8} {hit['identity']:<10.1f}% {hit['e_value']:<12.2e} {hit['length']:<8}")
    
    # 显示最佳匹配的详细信息
    if results:
        best_hit = results[0]
        print(f"\n最佳匹配: {best_hit['id']}")
        print(f"得分: {best_hit['score']}")
        print(f"相似度: {best_hit['identity']:.1f}%")
        print(f"E-value: {best_hit['e_value']:.2e}")
        print(f"\n比对预览:")
        print(best_hit['alignment'])


def practice_9_phylogenetic_analysis_solution():
    """
    练习9答案: 系统发育分析
    
    生物学类比：像构建物种进化树 - 
    通过序列相似度推断进化关系
    """
    print("\n🔍 练习9 [综合]: 系统发育分析 - 参考答案")
    print("-" * 50)
    
    # 物种序列集合
    species_sequences = {
        "Human": Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"),
        "Chimp": Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"),
        "Mouse": Seq("ATGGCCATTGTTATGGGCAGCTGAAAGGGTGCCCGATAG"),
        "Rat":   Seq("ATGGCCATTGTTATGGGCAGCTGAAAGGGTGCCCGATAG"),
        "Fly":   Seq("ATGGCAATTGTGATGGGTCGCTGAAAGGATGCCCGATAG")
    }
    
    print("物种序列集合:")
    for species, seq in species_sequences.items():
        print(f"{species:8}: {seq}")
    
    def calculate_distance(seq1, seq2):
        """计算Hamming距离"""
        differences = sum(1 for a, b in zip(seq1, seq2) if a != b)
        return differences / len(seq1)
    
    # 构建距离矩阵
    print("\n距离矩阵:")
    species_list = list(species_sequences.keys())
    distance_matrix = {}
    
    # 打印表头
    print("        ", end="")
    for sp in species_list:
        print(f"{sp:8}", end="")
    print()
    
    # 计算并打印距离
    for sp1 in species_list:
        print(f"{sp1:8}", end="")
        distance_matrix[sp1] = {}
        for sp2 in species_list:
            if sp1 == sp2:
                dist = 0.000
            else:
                dist = calculate_distance(
                    species_sequences[sp1],
                    species_sequences[sp2]
                )
            distance_matrix[sp1][sp2] = dist
            print(f"{dist:8.3f}", end="")
        print()
    
    # 使用UPGMA算法构建简单的树（简化版）
    print("\n系统发育关系（基于UPGMA）:")
    print("-" * 40)
    
    # 找出最近的物种对
    min_dist = float('inf')
    closest_pair = None
    for sp1 in species_list:
        for sp2 in species_list:
            if sp1 != sp2 and distance_matrix[sp1][sp2] < min_dist:
                min_dist = distance_matrix[sp1][sp2]
                closest_pair = (sp1, sp2)
    
    if closest_pair:
        print(f"最近的物种对: {closest_pair[0]} - {closest_pair[1]}")
        print(f"进化距离: {min_dist:.3f}")
    
    # 简单的聚类分析
    print("\n聚类分析:")
    # 灵长类
    primates = ["Human", "Chimp"]
    rodents = ["Mouse", "Rat"]
    
    print("灵长类分支: " + ", ".join(primates))
    primate_dist = calculate_distance(
        species_sequences["Human"],
        species_sequences["Chimp"]
    )
    print(f"  分支内距离: {primate_dist:.3f}")
    
    print("啮齿类分支: " + ", ".join(rodents))
    rodent_dist = calculate_distance(
        species_sequences["Mouse"],
        species_sequences["Rat"]
    )
    print(f"  分支内距离: {rodent_dist:.3f}")
    
    # 简单的进化树表示
    print("\n简化的进化树:")
    print("         ┌─── Human")
    print("    ┌────┤")
    print("    │    └─── Chimp")
    print("────┤")
    print("    │    ┌─── Mouse")
    print("    ├────┤")
    print("    │    └─── Rat")
    print("    │")
    print("    └──────── Fly")


def practice_10_complete_pipeline_solution():
    """
    练习10答案: 完整的基因分析流程
    
    展示从原始序列到最终报告的完整工作流程
    """
    print("\n🔍 练习10 [综合项目]: 完整分析流程 - 参考答案")
    print("-" * 50)
    
    # 模拟输入数据
    raw_sequence = Seq(
        "NNNATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGNNNN"
        "ATGCGATCGATCGATGCCCTAGCTAGCTAGCTAGCTAGCNNN"
        "ATGTTTAAACCCGGGATGAAATGAAATAGGCTGAATAAGGAAGTAA"
    )
    
    print(f"原始序列长度: {len(raw_sequence)} bp")
    print(f"序列预览: {raw_sequence[:50]}...\n")
    
    # Step 1 - 质量控制
    def quality_control(sequence):
        """去除低质量碱基"""
        # 去除N碱基
        clean_seq = str(sequence).replace('N', '')
        clean_seq = Seq(clean_seq)
        
        # 统计信息
        n_count = str(sequence).count('N')
        quality_score = (1 - n_count/len(sequence)) * 100
        
        return clean_seq, {
            'original_length': len(sequence),
            'clean_length': len(clean_seq),
            'n_bases_removed': n_count,
            'quality_score': quality_score
        }
    
    print("Step 1: 质量控制")
    print("-" * 30)
    clean_seq, qc_stats = quality_control(raw_sequence)
    print(f"原始长度: {qc_stats['original_length']} bp")
    print(f"清洁长度: {qc_stats['clean_length']} bp")
    print(f"去除N碱基: {qc_stats['n_bases_removed']}")
    print(f"质量分数: {qc_stats['quality_score']:.1f}%")
    
    # Step 2 - 基因预测
    def predict_genes(sequence):
        """预测可能的基因"""
        genes = []
        # 查找所有ATG起始的ORF
        for i in range(len(sequence) - 2):
            if str(sequence[i:i+3]) == 'ATG':
                # 查找最近的终止密码子
                for j in range(i + 3, len(sequence) - 2, 3):
                    if str(sequence[j:j+3]) in ['TAA', 'TAG', 'TGA']:
                        if j - i >= 30:  # 至少10个氨基酸
                            gene_seq = sequence[i:j+3]
                            genes.append({
                                'start': i,
                                'end': j + 3,
                                'length': j + 3 - i,
                                'sequence': gene_seq,
                                'protein': gene_seq.translate()
                            })
                        break
        return genes
    
    print("\nStep 2: 基因预测")
    print("-" * 30)
    predicted_genes = predict_genes(clean_seq)
    print(f"预测到 {len(predicted_genes)} 个潜在基因")
    for i, gene in enumerate(predicted_genes, 1):
        print(f"  基因{i}: 位置 {gene['start']}-{gene['end']}, 长度 {gene['length']} bp")
    
    # Step 3 - 功能注释
    def annotate_genes(genes):
        """模拟功能注释"""
        annotations = []
        for i, gene in enumerate(genes, 1):
            protein = gene['protein']
            
            # 简单的功能预测（基于氨基酸组成）
            if 'C' in protein and protein.count('C') >= 2:
                function = "可能含有二硫键的结构蛋白"
            elif protein.count('K') + protein.count('R') > len(protein) * 0.2:
                function = "可能的DNA结合蛋白"
            elif protein.count('L') + protein.count('I') + protein.count('V') > len(protein) * 0.3:
                function = "可能的疏水性膜蛋白"
            else:
                function = "功能未知的假设蛋白"
            
            annotations.append({
                'gene_id': f"GENE_{i:03d}",
                'position': f"{gene['start']}-{gene['end']}",
                'protein_length': len(protein),
                'predicted_function': function,
                'gc_content': GC(gene['sequence'])
            })
        
        return annotations
    
    print("\nStep 3: 功能注释")
    print("-" * 30)
    gene_annotations = annotate_genes(predicted_genes)
    for ann in gene_annotations:
        print(f"{ann['gene_id']}:")
        print(f"  位置: {ann['position']}")
        print(f"  蛋白长度: {ann['protein_length']} aa")
        print(f"  GC含量: {ann['gc_content']:.1f}%")
        print(f"  预测功能: {ann['predicted_function']}")
    
    # Step 4 - 生成分析报告
    def generate_report(qc_stats, genes, annotations):
        """生成综合分析报告"""
        report = []
        report.append("=" * 60)
        report.append("基因组分析报告")
        report.append("=" * 60)
        
        report.append("\n[质量控制]")
        report.append(f"• 原始序列长度: {qc_stats['original_length']} bp")
        report.append(f"• 高质量序列长度: {qc_stats['clean_length']} bp")
        report.append(f"• 序列质量分数: {qc_stats['quality_score']:.1f}%")
        
        report.append("\n[基因预测]")
        report.append(f"• 预测基因数: {len(genes)}")
        if genes:
            avg_length = sum(g['length'] for g in genes) / len(genes)
            report.append(f"• 平均基因长度: {avg_length:.1f} bp")
            total_coding = sum(g['length'] for g in genes)
            coding_density = (total_coding / qc_stats['clean_length']) * 100
            report.append(f"• 编码密度: {coding_density:.1f}%")
        
        report.append("\n[功能注释]")
        for ann in annotations:
            report.append(f"• {ann['gene_id']}: {ann['predicted_function']}")
        
        report.append("\n[统计摘要]")
        report.append(f"• 分析完成时间: 2024-01-01 12:00:00")
        report.append(f"• 分析流程版本: v1.0")
        
        return "\n".join(report)
    
    print("\nStep 4: 生成分析报告")
    print("-" * 30)
    final_report = generate_report(qc_stats, predicted_genes, gene_annotations)
    print(final_report)


def main():
    """
    主函数 - 运行所有练习答案
    """
    print("🧬 Chapter 09: Biopython 练习题参考答案")
    print("=" * 60)
    print("完整的练习题解答，包含详细注释和扩展分析\n")
    
    # 基础练习答案
    print("=" * 60)
    print("📘 基础练习答案")
    print("=" * 60)
    practice_1_basic_seq_solution()
    practice_2_file_parsing_solution()
    practice_2_bonus_real_data_solution()
    
    # 进阶练习答案
    print("\n" + "=" * 60)
    print("📙 进阶练习答案")
    print("=" * 60)
    practice_3_orf_finding_solution()
    practice_4_restriction_sites_solution()
    practice_5_protein_analysis_solution()
    
    # 综合练习答案
    print("\n" + "=" * 60)
    print("📕 综合练习答案")
    print("=" * 60)
    practice_6_sequence_alignment_solution()
    practice_7_genome_annotation_solution()
    practice_8_blast_search_solution()
    practice_9_phylogenetic_analysis_solution()
    practice_10_complete_pipeline_solution()
    
    print("\n" + "=" * 60)
    print("📚 学习总结")
    print("=" * 60)
    print("\n通过这些练习，你已经掌握了：")
    print("✓ Seq和SeqRecord对象的使用")
    print("✓ 文件格式的读写和转换")
    print("✓ ORF预测和基因查找")
    print("✓ 限制性酶切分析")
    print("✓ 蛋白质理化性质分析")
    print("✓ 序列比对和相似性分析")
    print("✓ 基因组注释流程")
    print("✓ BLAST搜索原理")
    print("✓ 系统发育分析基础")
    print("✓ 完整的生物信息学分析流程")
    
    print("\n💡 下一步建议：")
    print("1. 尝试用真实数据重现这些分析")
    print("2. 学习使用NCBI的在线工具")
    print("3. 探索更高级的Biopython模块")
    print("4. 结合其他Python库进行数据可视化")
    print("5. 开发自己的生物信息学工具")


if __name__ == "__main__":
    main()