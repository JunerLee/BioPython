#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 09: Biopython - 专业生物信息学工具库

本章深入展示Biopython在实际生物信息学研究中的应用：
- 核心模块的详细使用方法
- 与NCBI数据库的交互
- 序列比对和进化分析
- 完整的基因组分析流程
- 与其他工具的集成
"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO, Entrez, AlignIO
from Bio.SeqUtils import gc_fraction, molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.Data import CodonTable
from Bio.Restriction import *
from Bio.SeqFeature import SeqFeature, FeatureLocation
import io
import random
from datetime import datetime


def demonstrate_seq_fundamentals():
    """
    演示1: Seq对象的基础操作
    
    生物学类比：Seq对象就像DNA分子模型 - 不仅存储序列信息，
    还能模拟生物学过程（转录、翻译、复制）
    """
    print("🧬 演示1: Seq对象基础操作")
    print("=" * 60)
    
    # 创建DNA序列
    dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
    print(f"原始DNA序列: {dna_seq}")
    print(f"序列长度: {len(dna_seq)} bp")
    print(f"序列类型: {type(dna_seq)}")
    
    # 基本序列操作
    print("\n📊 序列统计信息:")
    print(f"GC含量: {gc_fraction(dna_seq)*100:.2f}%")
    print(f"A碱基数量: {dna_seq.count('A')}")
    print(f"T碱基数量: {dna_seq.count('T')}")
    print(f"G碱基数量: {dna_seq.count('G')}")
    print(f"C碱基数量: {dna_seq.count('C')}")
    
    # 序列操作
    print("\n🔄 序列变换:")
    print(f"互补链: {dna_seq.complement()}")
    print(f"反向链: {dna_seq[::-1]}")
    print(f"反向互补链: {dna_seq.reverse_complement()}")
    
    # 中心法则：DNA -> RNA -> 蛋白质
    print("\n🧬 中心法则演示:")
    rna_seq = dna_seq.transcribe()
    print(f"RNA (转录): {rna_seq}")
    
    protein_seq = rna_seq.translate()
    print(f"蛋白质 (翻译): {protein_seq}")
    
    # 不同的翻译表（遗传密码）
    print("\n🔤 使用不同的遗传密码表:")
    # 标准遗传密码
    protein_standard = dna_seq.translate(table=1)
    print(f"标准密码表: {protein_standard}")
    
    # 线粒体遗传密码
    protein_mito = dna_seq.translate(table=2)
    print(f"线粒体密码表: {protein_mito}")
    
    # 显示可用的密码表
    print("\n可用的遗传密码表:")
    print("1 - 标准密码表")
    print("2 - 脊椎动物线粒体")
    print("3 - 酵母线粒体")
    print("4 - 霉菌线粒体")
    print("11 - 细菌和古菌")


def demonstrate_seqrecord_advanced():
    """
    演示2: SeqRecord的高级使用
    
    生物学类比：SeqRecord像是基因的完整档案 - 
    不仅有序列本身，还包含ID、描述、特征注释等元数据
    """
    print("\n\n📁 演示2: SeqRecord高级特性")
    print("=" * 60)
    
    # 创建一个完整的基因记录
    gene_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
    
    # 创建SeqRecord对象
    gene_record = SeqRecord(
        gene_seq,
        id="BRCA1_fragment",
        name="BRCA1",
        description="Breast cancer type 1 susceptibility protein fragment",
        annotations={"molecule_type": "DNA", "organism": "Homo sapiens"}
    )
    
    # 添加序列特征（features）
    # 添加启动子区域
    promoter = SeqFeature(
        FeatureLocation(0, 10),
        type="promoter",
        qualifiers={"note": "TATA box region"}
    )
    gene_record.features.append(promoter)
    
    # 添加编码区
    cds = SeqFeature(
        FeatureLocation(10, 39),
        type="CDS",
        qualifiers={
            "gene": "BRCA1",
            "product": "tumor suppressor protein",
            "translation": str(gene_seq[10:39].translate())
        }
    )
    gene_record.features.append(cds)
    
    # 显示记录信息
    print(f"ID: {gene_record.id}")
    print(f"名称: {gene_record.name}")
    print(f"描述: {gene_record.description}")
    print(f"序列长度: {len(gene_record.seq)} bp")
    print(f"注释: {gene_record.annotations}")
    
    print("\n序列特征:")
    for feature in gene_record.features:
        print(f"  - {feature.type}: 位置 {feature.location}")
        for key, value in feature.qualifiers.items():
            print(f"    {key}: {value}")
    
    # 添加数据库交叉引用
    gene_record.dbxrefs = ["GeneID:672", "HGNC:1100", "MIM:113705"]
    print(f"\n数据库引用: {', '.join(gene_record.dbxrefs)}")


def demonstrate_seqio_operations():
    """
    演示3: SeqIO模块的文件操作
    
    生物学类比：SeqIO像实验室的多功能读卡器 - 
    能识别和转换各种序列文件格式
    """
    print("\n\n📂 演示3: SeqIO文件操作")
    print("=" * 60)
    
    # 创建多个模拟基因序列
    sequences = []
    
    # 模拟人类基因
    human_genes = [
        ("TP53", "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAG", 
         "Tumor protein p53"),
        ("EGFR", "ATGCGACCCTCCGGGACGGCCGGGGCAGCGCTC", 
         "Epidermal growth factor receptor"),
        ("BRCA2", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCC", 
         "Breast cancer type 2 susceptibility protein")
    ]
    
    for gene_id, seq, desc in human_genes:
        record = SeqRecord(
            Seq(seq),
            id=f"HUMAN_{gene_id}",
            description=desc
        )
        sequences.append(record)
    
    # 创建FASTA格式字符串
    fasta_output = io.StringIO()
    SeqIO.write(sequences, fasta_output, "fasta")
    fasta_string = fasta_output.getvalue()
    
    print("生成的FASTA文件内容:")
    print("-" * 40)
    print(fasta_string)
    
    # 解析FASTA内容
    fasta_input = io.StringIO(fasta_string)
    parsed_records = list(SeqIO.parse(fasta_input, "fasta"))
    
    print(f"解析结果: 找到 {len(parsed_records)} 条序列\n")
    
    # 详细分析每条序列
    for i, record in enumerate(parsed_records, 1):
        print(f"序列 {i}: {record.id}")
        print(f"  描述: {record.description}")
        print(f"  长度: {len(record.seq)} bp")
        
        # 计算序列特征
        gc_content = gc_fraction(record.seq) * 100
        print(f"  GC含量: {gc_content:.1f}%")
        
        # 计算分子量
        try:
            mw = molecular_weight(record.seq, seq_type='DNA')
            print(f"  分子量: {mw:.2f} Da")
        except:
            print(f"  分子量: 无法计算")
        
        # 六框翻译
        print(f"  六框翻译预览:")
        for frame in range(3):
            frame_seq = record.seq[frame:]
            if len(frame_seq) >= 3:
                protein = frame_seq[:15].translate(to_stop=False)
                print(f"    +{frame}: {protein}...")
        print()
    
    # 格式转换示例
    print("📄 格式转换演示:")
    print("-" * 40)
    
    # 转换为GenBank格式（简化版）
    for record in parsed_records[:1]:  # 只展示第一条
        record.annotations["molecule_type"] = "DNA"
        record.annotations["organism"] = "Homo sapiens"
        record.annotations["date"] = datetime.now().strftime("%d-%b-%Y")
        
        genbank_output = io.StringIO()
        SeqIO.write([record], genbank_output, "genbank")
        print("GenBank格式预览:")
        print(genbank_output.getvalue()[:500] + "...")


def demonstrate_restriction_analysis():
    """
    演示4: 限制性酶切分析
    
    生物学类比：限制性内切酶像是分子剪刀 - 
    在特定的DNA序列处切割，用于克隆和分析
    """
    print("\n\n✂️ 演示4: 限制性酶切分析")
    print("=" * 60)
    
    # 创建一个质粒序列
    plasmid_seq = Seq("GAATTCGCGGCCGCGTCGACAAGCTTGCATGCCTGCAGGTCGACTCTAGAGGATCCCCGGG")
    print(f"质粒序列: {plasmid_seq}")
    print(f"序列长度: {len(plasmid_seq)} bp\n")
    
    # 分析常用限制性内切酶
    print("限制性酶切位点分析:")
    print("-" * 40)
    
    # 定义要检查的酶
    enzymes_to_check = [EcoRI, BamHI, HindIII, PstI, SalI, NotI]
    
    for enzyme in enzymes_to_check:
        sites = enzyme.search(plasmid_seq)
        if sites:
            print(f"{enzyme.__name__:8} ({enzyme.site:6}): 切割位点 {sites}")
        else:
            print(f"{enzyme.__name__:8} ({enzyme.site:6}): 无切割位点")
    
    # 进行虚拟酶切
    print("\n虚拟酶切实验:")
    print("-" * 40)
    
    # 用EcoRI和BamHI双酶切
    if EcoRI.search(plasmid_seq) and BamHI.search(plasmid_seq):
        eco_site = EcoRI.search(plasmid_seq)[0]
        bam_site = BamHI.search(plasmid_seq)[0]
        
        print(f"EcoRI切割位点: {eco_site}")
        print(f"BamHI切割位点: {bam_site}")
        
        # 获取酶切片段
        if eco_site < bam_site:
            insert = plasmid_seq[eco_site:bam_site]
            print(f"插入片段 ({eco_site}-{bam_site}): {insert}")
            print(f"片段长度: {len(insert)} bp")


def demonstrate_protein_analysis():
    """
    演示5: 蛋白质序列分析
    
    生物学类比：蛋白质分析像是解读生命的工作机器 - 
    了解其组成、性质和功能
    """
    print("\n\n🔬 演示5: 蛋白质序列分析")
    print("=" * 60)
    
    # 创建一个蛋白质序列（人类胰岛素A链）
    insulin_a = Seq("GIVEQCCTSICSLYQLENYCN")
    print(f"胰岛素A链: {insulin_a}")
    print(f"长度: {len(insulin_a)} 氨基酸\n")
    
    # 使用ProtParam分析蛋白质性质
    from Bio.SeqUtils.ProtParam import ProteinAnalysis
    
    protein_analysis = ProteinAnalysis(str(insulin_a))
    
    print("蛋白质理化性质:")
    print("-" * 40)
    print(f"分子量: {protein_analysis.molecular_weight():.2f} Da")
    print(f"等电点(pI): {protein_analysis.isoelectric_point():.2f}")
    print(f"不稳定性指数: {protein_analysis.instability_index():.2f}")
    
    # 氨基酸组成
    print("\n氨基酸组成:")
    aa_comp = protein_analysis.amino_acids_percent
    for aa, percent in sorted(aa_comp.items(), key=lambda x: x[1], reverse=True)[:5]:
        if percent > 0:
            print(f"  {aa}: {percent*100:.1f}%")
    
    # 二级结构预测（简化版）
    helix, turn, sheet = protein_analysis.secondary_structure_fraction()
    print(f"\n二级结构预测:")
    print(f"  α-螺旋: {helix*100:.1f}%")
    print(f"  β-折叠: {sheet*100:.1f}%")
    print(f"  转角: {turn*100:.1f}%")


def demonstrate_orf_finding():
    """
    演示6: 开放阅读框(ORF)查找
    
    生物学类比：ORF查找像是在DNA序列中寻找基因 - 
    找到可能编码蛋白质的区域
    """
    print("\n\n🔍 演示6: 开放阅读框(ORF)查找")
    print("=" * 60)
    
    # 创建一个包含多个ORF的序列
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
    
    # 正向链ORF
    print("正向链ORF搜索:")
    print("-" * 40)
    forward_orfs = find_orfs(genomic_seq)
    
    if forward_orfs:
        for i, orf in enumerate(forward_orfs, 1):
            print(f"ORF {i}:")
            print(f"  位置: {orf['start']}-{orf['end']} (框{orf['frame']})")
            print(f"  长度: {orf['length']} bp")
            print(f"  DNA: {orf['sequence']}")
            print(f"  蛋白: {orf['protein']}")
    else:
        print("  未找到ORF")
    
    # 反向互补链ORF
    print("\n反向互补链ORF搜索:")
    print("-" * 40)
    rev_comp = genomic_seq.reverse_complement()
    reverse_orfs = find_orfs(rev_comp)
    
    if reverse_orfs:
        for i, orf in enumerate(reverse_orfs, 1):
            print(f"ORF {i} (反向):")
            print(f"  位置: {orf['start']}-{orf['end']} (框{orf['frame']})")
            print(f"  长度: {orf['length']} bp")
            print(f"  蛋白: {orf['protein']}")
    else:
        print("  未找到ORF")


def demonstrate_sequence_patterns():
    """
    演示7: 序列模式搜索
    
    生物学类比：序列模式搜索像是在基因组中找特定的调控元件 - 
    如启动子、增强子、转录因子结合位点等
    """
    print("\n\n🔎 演示7: 序列模式搜索")
    print("=" * 60)
    
    # 创建一个包含多个调控元件的序列
    regulatory_seq = Seq(
        "TATAAAGGTACCGCGTATATAAGGCCAATTGCAGCTGGGCACGAAATTTATAAAGGC"
    )
    print(f"调控序列: {regulatory_seq}")
    print(f"序列长度: {len(regulatory_seq)} bp\n")
    
    # 定义要搜索的模式
    patterns = {
        "TATA box": "TATAA",
        "CAAT box": "CAAT",
        "GC box": "GGGCGG",
        "Kozak序列": "GCCRCC",  # R = A或G
        "PolyA信号": "AATAAA"
    }
    
    print("调控元件搜索:")
    print("-" * 40)
    
    for name, pattern in patterns.items():
        # 简单模式搜索
        positions = []
        search_pattern = pattern.replace('R', '[AG]')  # 处理简并碱基
        
        # 搜索所有出现位置
        seq_str = str(regulatory_seq)
        start = 0
        while True:
            pos = seq_str.find(pattern, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        
        if positions:
            print(f"{name:12} ({pattern}): 位置 {positions}")
        else:
            print(f"{name:12} ({pattern}): 未找到")
    
    # 查找重复序列
    print("\n重复序列分析:")
    print("-" * 40)
    
    # 查找串联重复
    for length in [2, 3, 4]:
        repeats = {}
        seq_str = str(regulatory_seq)
        for i in range(len(seq_str) - length + 1):
            motif = seq_str[i:i+length]
            if motif not in repeats:
                repeats[motif] = []
            repeats[motif].append(i)
        
        # 找出重复的模体
        repeated_motifs = {k: v for k, v in repeats.items() if len(v) > 1}
        if repeated_motifs:
            print(f"{length}bp重复:")
            for motif, positions in list(repeated_motifs.items())[:3]:
                print(f"  {motif}: 出现{len(positions)}次，位置{positions[:5]}")


def demonstrate_codon_usage():
    """
    演示8: 密码子使用偏好性分析
    
    生物学类比：密码子偏好性像是生物的"方言" - 
    不同生物偏好使用不同的同义密码子
    """
    print("\n\n📊 演示8: 密码子使用分析")
    print("=" * 60)
    
    # 创建一个编码序列
    cds_seq = Seq(
        "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGCCATTGTAATGGGCCGCTGA"
    )
    print(f"CDS序列: {cds_seq[:30]}...")
    print(f"序列长度: {len(cds_seq)} bp\n")
    
    # 统计密码子使用
    codon_count = {}
    for i in range(0, len(cds_seq)-2, 3):
        codon = str(cds_seq[i:i+3])
        if len(codon) == 3:
            codon_count[codon] = codon_count.get(codon, 0) + 1
    
    print("密码子使用频率:")
    print("-" * 40)
    
    # 按氨基酸分组显示
    standard_table = CodonTable.unambiguous_dna_by_id[1]
    aa_codons = {}
    
    for codon, aa in standard_table.forward_table.items():
        if aa not in aa_codons:
            aa_codons[aa] = []
        aa_codons[aa].append(codon)
    
    # 添加终止密码子
    aa_codons['*'] = standard_table.stop_codons
    
    # 显示每个氨基酸的密码子使用
    for aa in sorted(aa_codons.keys())[:10]:  # 只显示前10个
        print(f"{aa}: ", end="")
        for codon in aa_codons[aa]:
            count = codon_count.get(codon, 0)
            if count > 0:
                print(f"{codon}({count}) ", end="")
        print()
    
    # 计算CAI (Codon Adaptation Index) - 简化版
    total_codons = sum(codon_count.values())
    print(f"\n密码子总数: {total_codons}")
    print(f"不同密码子数: {len(codon_count)}")


def demonstrate_genome_statistics():
    """
    演示9: 基因组统计分析
    
    生物学类比：基因组统计像是给基因组做"体检" - 
    了解其大小、组成、特征等基本信息
    """
    print("\n\n📈 演示9: 基因组统计分析")
    print("=" * 60)
    
    # 模拟一个小基因组片段
    genome_fragment = Seq(
        "ATGCGATCGTAGCTAGCTAGCATGCATGCATGCTAGCTAGCTAGCTAGCATGCATGC" * 10
    )
    
    print(f"基因组片段长度: {len(genome_fragment)} bp\n")
    
    # 基本统计
    print("碱基组成:")
    print("-" * 40)
    base_count = {
        'A': genome_fragment.count('A'),
        'T': genome_fragment.count('T'),
        'G': genome_fragment.count('G'),
        'C': genome_fragment.count('C')
    }
    
    total_bases = sum(base_count.values())
    for base, count in base_count.items():
        percentage = (count / total_bases) * 100
        print(f"{base}: {count:4d} ({percentage:5.1f}%)")
    
    # GC含量和GC偏斜
    gc_content = gc_fraction(genome_fragment) * 100
    gc_skew = (base_count['G'] - base_count['C']) / (base_count['G'] + base_count['C'])
    at_skew = (base_count['A'] - base_count['T']) / (base_count['A'] + base_count['T'])
    
    print(f"\nGC含量: {gc_content:.2f}%")
    print(f"GC偏斜: {gc_skew:.3f}")
    print(f"AT偏斜: {at_skew:.3f}")
    
    # 二核苷酸频率
    print("\n二核苷酸频率 (前5个):")
    print("-" * 40)
    dinuc_count = {}
    seq_str = str(genome_fragment)
    for i in range(len(seq_str) - 1):
        dinuc = seq_str[i:i+2]
        dinuc_count[dinuc] = dinuc_count.get(dinuc, 0) + 1
    
    # 排序并显示前5个
    sorted_dinuc = sorted(dinuc_count.items(), key=lambda x: x[1], reverse=True)
    for dinuc, count in sorted_dinuc[:5]:
        freq = count / (len(genome_fragment) - 1) * 100
        print(f"{dinuc}: {count:3d} ({freq:5.1f}%)")
    
    # CpG岛检测（简化版）
    cpg_count = seq_str.count('CG')
    expected_cpg = (base_count['C'] * base_count['G']) / total_bases
    obs_exp_ratio = cpg_count / expected_cpg if expected_cpg > 0 else 0
    
    print(f"\nCpG分析:")
    print(f"观察到的CpG: {cpg_count}")
    print(f"期望的CpG: {expected_cpg:.1f}")
    print(f"观察/期望比: {obs_exp_ratio:.2f}")
    if obs_exp_ratio > 0.6 and gc_content > 50:
        print("可能存在CpG岛")


def demonstrate_complete_workflow():
    """
    演示10: 完整的基因分析工作流程
    
    展示从原始序列到功能注释的完整分析流程
    """
    print("\n\n🔬 演示10: 完整的基因分析工作流程")
    print("=" * 60)
    
    # Step 1: 读取序列
    print("Step 1: 读取基因序列")
    print("-" * 40)
    
    # 模拟一个真实基因（简化的p53片段）
    p53_fragment = Seq(
        "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAG"
        "ACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGA"
    )
    
    gene_record = SeqRecord(
        p53_fragment,
        id="TP53_HUMAN",
        name="TP53",
        description="Cellular tumor antigen p53 [Homo sapiens]"
    )
    
    print(f"基因: {gene_record.name}")
    print(f"描述: {gene_record.description}")
    print(f"长度: {len(gene_record.seq)} bp")
    
    # Step 2: 序列质量检查
    print("\nStep 2: 序列质量检查")
    print("-" * 40)
    
    # 检查是否有非标准碱基
    valid_bases = set('ATGC')
    seq_bases = set(str(gene_record.seq))
    if seq_bases.issubset(valid_bases):
        print("✓ 序列只包含标准碱基")
    else:
        print("✗ 序列包含非标准碱基:", seq_bases - valid_bases)
    
    # 检查序列长度是否为3的倍数
    if len(gene_record.seq) % 3 == 0:
        print("✓ 序列长度是3的倍数（完整密码子）")
    else:
        print(f"✗ 序列长度不是3的倍数（余{len(gene_record.seq) % 3}）")
    
    # Step 3: 基本序列分析
    print("\nStep 3: 基本序列分析")
    print("-" * 40)
    
    gc_content = gc_fraction(gene_record.seq) * 100
    print(f"GC含量: {gc_content:.2f}%")
    
    # 计算分子量
    mw = molecular_weight(gene_record.seq, seq_type='DNA')
    print(f"DNA分子量: {mw:.2f} Da")
    
    # Step 4: ORF预测
    print("\nStep 4: 开放阅读框预测")
    print("-" * 40)
    
    # 查找最长的ORF
    protein = gene_record.seq.translate(to_stop=True)
    print(f"预测蛋白质: {protein[:30]}...")
    print(f"蛋白质长度: {len(protein)} aa")
    
    # Step 5: 功能域预测（模拟）
    print("\nStep 5: 功能域预测")
    print("-" * 40)
    
    # 模拟功能域（实际应用中会使用BLAST或InterProScan）
    print("预测的功能域:")
    print("  1-50: DNA结合域")
    print("  51-100: 转录激活域")
    print("  101-120: 寡聚化域")
    
    # Step 6: 生成分析报告
    print("\nStep 6: 分析报告总结")
    print("-" * 40)
    print(f"基因名称: {gene_record.name}")
    print(f"序列长度: {len(gene_record.seq)} bp")
    print(f"GC含量: {gc_content:.2f}%")
    print(f"编码蛋白: {len(protein)} aa")
    print(f"分子功能: 肿瘤抑制因子")
    print(f"生物过程: 细胞周期调控, DNA损伤应答")
    print(f"细胞定位: 细胞核")


def main():
    """
    主函数 - 协调所有演示
    """
    print("🧬 Chapter 09: Biopython - 专业生物信息学工具库")
    print("=" * 60)
    print("学习如何使用Biopython进行专业的生物序列分析\n")
    
    # 运行所有演示
    demonstrate_seq_fundamentals()
    demonstrate_seqrecord_advanced()
    demonstrate_seqio_operations()
    demonstrate_restriction_analysis()
    demonstrate_protein_analysis()
    demonstrate_orf_finding()
    demonstrate_sequence_patterns()
    demonstrate_codon_usage()
    demonstrate_genome_statistics()
    demonstrate_complete_workflow()
    
    # 总结
    print("\n" + "=" * 60)
    print("📚 本章核心知识点总结:")
    print("=" * 60)
    
    print("\n1. Seq对象:")
    print("   - 生物序列的基本表示和操作")
    print("   - 支持转录、翻译、反向互补等生物学操作")
    print("   - 自动处理遗传密码表和序列验证")
    
    print("\n2. SeqRecord对象:")
    print("   - 包含序列及其元数据的完整记录")
    print("   - 支持特征注释、数据库引用等")
    print("   - 是SeqIO操作的基本单元")
    
    print("\n3. SeqIO模块:")
    print("   - 统一的文件格式读写接口")
    print("   - 支持FASTA、GenBank、FASTQ等多种格式")
    print("   - 高效的大文件处理能力")
    
    print("\n4. 序列分析功能:")
    print("   - 限制性酶切分析")
    print("   - ORF预测和基因查找")
    print("   - 序列模式搜索")
    print("   - 密码子使用分析")
    
    print("\n5. 蛋白质分析:")
    print("   - 理化性质计算")
    print("   - 二级结构预测")
    print("   - 功能域分析")
    
    print("\n" + "=" * 60)
    print("🎯 Biopython的优势:")
    print("=" * 60)
    print("• 标准化 - 统一的API设计，降低学习成本")
    print("• 全面性 - 覆盖生物信息学各个领域")
    print("• 可扩展 - 易于集成其他工具和数据库")
    print("• 社区支持 - 活跃的开发和用户社区")
    print("• 文档完善 - 详细的教程和示例代码")
    
    print("\n" + "=" * 60)
    print("💡 实践建议:")
    print("=" * 60)
    print("1. 从简单的序列操作开始，逐步深入复杂功能")
    print("2. 多练习文件格式转换，熟悉不同格式特点")
    print("3. 学会组合多个模块构建分析流程")
    print("4. 关注性能优化，特别是处理大规模数据时")
    print("5. 积极使用官方文档和社区资源")
    
    print("\n🚀 下一步学习方向:")
    print("• 学习BLAST编程接口进行序列相似性搜索")
    print("• 掌握Entrez模块访问NCBI数据库")
    print("• 探索AlignIO进行序列比对分析")
    print("• 使用Phylo模块构建进化树")
    print("• 结合机器学习进行序列特征预测")


if __name__ == "__main__":
    # 设置Entrez邮箱（使用NCBI服务时需要）
    Entrez.email = "your_email@example.com"
    
    # 运行主程序
    main()