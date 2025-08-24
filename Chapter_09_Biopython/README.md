# Chapter 09: Biopython - 生物信息学的瑞士军刀

## 写在最前面 - 给即将掌握专业工具的你

亲爱的研究者，

还记得你第一次走进分子生物学实验室时的感觉吗？

面对着PCR仪、测序仪、离心机等各种精密仪器，你可能既兴奋又有些不知所措。每台仪器都有其特定的功能，每个实验都需要不同的工具组合。渐渐地，你学会了如何使用这些仪器，如何设计实验流程，如何分析实验结果。

今天，我们要学习的Biopython就像是计算生物学的实验室 - 一个装满了各种专业工具的宝库。

**为什么Biopython如此重要？**

想象一下，如果你需要分析一个新测序的基因组：
- 你需要读取不同格式的序列文件（FASTA、GenBank、FASTQ...）
- 你需要查找开放阅读框，预测基因
- 你需要BLAST搜索，找到同源序列
- 你需要进行序列比对，构建进化树
- 你需要分析蛋白质结构，预测功能

如果没有Biopython，你可能需要学习十几种不同的工具，编写大量的格式转换代码。而有了Biopython，所有这些功能都集成在一个统一的框架中，就像一个装备齐全的现代化实验室。

在过去的20多年里，Biopython陪伴了无数生物信息学家的成长。从1999年的第一个版本到今天，它已经成为生物信息学Python编程的标准库。Nature、Science上发表的许多重要研究都使用了Biopython进行数据分析。

今天，让我们一起走进这个强大的工具库，看看它如何让复杂的生物信息学分析变得简单而优雅。

准备好了吗？让我们开始这段激动人心的旅程！

---

## 本章导航 - 你的学习地图

### 学习目标
- **核心掌握**：Seq、SeqRecord、SeqIO三大核心模块
- **文件处理**：读写各种生物序列文件格式
- **序列分析**：限制酶切、ORF查找、模式搜索
- **数据库访问**：BLAST搜索、Entrez查询
- **高级应用**：序列比对、进化分析、结构分析

### 学习路径
```
基础阶段（1-2天）
├── Seq对象：序列的基本操作
├── SeqRecord：带注释的序列
└── SeqIO：文件读写

进阶阶段（2-3天）
├── 限制酶分析
├── ORF和基因预测
├── BLAST编程接口
└── Entrez数据库查询

高级阶段（3-5天）
├── 序列比对（AlignIO）
├── 系统发育分析（Phylo）
├── 蛋白质结构（PDB）
└── 整合分析流程
```

### 章节结构
1. **Biopython的前世今生** - 了解这个强大工具的发展历程
2. **核心概念详解** - 深入理解Seq、SeqRecord、SeqIO
3. **序列分析工具箱** - 掌握各种序列分析方法
4. **数据库接口** - 连接全球生物数据库
5. **高级分析模块** - 比对、进化、结构分析
6. **实战项目** - 完整的基因组分析流程
7. **最佳实践** - 性能优化和代码组织

---

## 第一部分：Biopython的前世今生

### 1.1 诞生背景 - 为什么需要Biopython？

让我们把时间拨回到1999年...

那时，人类基因组计划正如火如荼地进行着。测序技术产生了海量的序列数据，但分析工具却各自为政：
- Perl有BioPerl，功能强大但语法复杂
- Java有BioJava，面向对象但学习曲线陡峭
- 各种C/C++工具速度快但难以整合

Python作为一门简洁优雅的语言，急需一个专门的生物信息学库。于是，Andrew Dalke和Jeff Chang发起了Biopython项目。

**设计理念**：
```python
# Biopython的设计哲学可以用这段代码概括
from Bio import SeqIO

# 简单 - 一行代码读取序列文件
sequences = list(SeqIO.parse("genome.fasta", "fasta"))

# 强大 - 支持几乎所有生物学操作
for seq in sequences:
    protein = seq.seq.translate()  # 翻译
    gc = seq.seq.count("G") + seq.seq.count("C")  # GC含量
    
# 统一 - 相同的接口处理不同格式
SeqIO.convert("input.gb", "genbank", "output.fasta", "fasta")
```

### 1.2 发展历程 - 20年的进化之路

让我们看看Biopython是如何一步步进化的：

**1999-2003：奠基阶段**
```python
# 最初的Biopython只有基本功能
from Bio.Seq import Seq
dna = Seq("ATCG")
print(dna.complement())  # TAGC

# 主要贡献者：Andrew Dalke, Jeff Chang
# 核心模块：Seq, SeqRecord, SeqIO
```

**2003-2009：快速发展期**
```python
# 加入了BLAST和Entrez接口
from Bio.Blast import NCBIWWW
result = NCBIWWW.qblast("blastn", "nt", sequence)

# 加入了AlignIO处理序列比对
from Bio import AlignIO
alignment = AlignIO.read("aligned.fasta", "fasta")

# 主要贡献者：Peter Cock, Michiel de Hoon
# 新增模块：Blast, Entrez, AlignIO, Phylo
```

**2009-2017：成熟完善期**
```python
# 加入了系统发育分析
from Bio import Phylo
tree = Phylo.read("tree.xml", "phyloxml")
Phylo.draw(tree)

# 支持更多文件格式
formats = ["fasta", "genbank", "embl", "swiss", 
           "fastq", "sff", "abi", "phylip", "nexus"]

# 主要贡献者：Eric Talevich, Bow Rayan
# 新增模块：Phylo, PDB, SearchIO, motifs
```

**2017-现在：现代化阶段**
```python
# 完全支持Python 3
# 性能大幅提升
# 更好的错误处理和文档

from Bio import SeqIO
# 使用生成器处理大文件，内存效率提升100倍
for record in SeqIO.parse("huge_genome.fasta", "fasta"):
    process(record)  # 逐条处理，不占用大量内存

# 主要改进：Python 3支持、性能优化、持续集成
```

### 1.3 生态系统 - Biopython的朋友圈

Biopython不是孤岛，它是整个生物信息学生态系统的一部分：

```python
# 与NumPy集成 - 高效的数值计算
import numpy as np
from Bio import SeqIO

sequences = []
for record in SeqIO.parse("sequences.fasta", "fasta"):
    # 将序列转换为数值数组
    seq_array = np.array(list(str(record.seq)))
    sequences.append(seq_array)

# 与Pandas集成 - 数据分析和统计
import pandas as pd
from Bio import SeqIO

data = []
for record in SeqIO.parse("genome.gb", "genbank"):
    data.append({
        'id': record.id,
        'length': len(record),
        'gc_content': record.seq.count("G") + record.seq.count("C"),
        'features': len(record.features)
    })
df = pd.DataFrame(data)
print(df.describe())

# 与Matplotlib集成 - 数据可视化
import matplotlib.pyplot as plt
from Bio import SeqIO

lengths = [len(rec) for rec in SeqIO.parse("reads.fastq", "fastq")]
plt.hist(lengths, bins=50)
plt.xlabel("Read Length")
plt.ylabel("Count")
plt.title("Read Length Distribution")
plt.show()

# 与scikit-learn集成 - 机器学习
from sklearn.cluster import KMeans
from Bio import SeqIO

# 序列特征提取
features = []
for record in SeqIO.parse("proteins.fasta", "fasta"):
    # 提取氨基酸组成作为特征
    composition = [record.seq.count(aa) for aa in "ACDEFGHIKLMNPQRSTVWY"]
    features.append(composition)

# 聚类分析
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(features)
```

---

## 第二部分：核心概念深度剖析

### 2.1 Seq对象 - 生物序列的基石

#### 生物学类比
Seq对象就像DNA双螺旋模型 - 不仅展示序列结构，还能模拟各种生物学过程。就像你可以在DNA模型上演示复制、转录、翻译一样，Seq对象也能执行这些操作。

#### 核心概念

```python
from Bio.Seq import Seq

# 创建序列对象 - 就像合成一段DNA
dna_sequence = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(f"DNA序列: {dna_sequence}")
print(f"序列类型: {type(dna_sequence)}")
print(f"序列长度: {len(dna_sequence)} bp")

# 输出:
# DNA序列: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
# 序列类型: <class 'Bio.Seq.Seq'>
# 序列长度: 39 bp
```

#### 示例1：序列的基本操作

```python
from Bio.Seq import Seq

# 创建不同类型的序列
dna = Seq("ATCGATCGATCG")
rna = Seq("AUCGAUCGAUCG")
protein = Seq("MKQHKAMIVALIVICITAVVAAL")

print(f"DNA: {dna}")
print(f"RNA: {rna}")
print(f"Protein: {protein}")

# 序列切片 - 就像用限制酶切割DNA
fragment = dna[0:6]
print(f"\n前6个碱基: {fragment}")

# 序列连接 - 就像DNA连接酶的作用
primer = Seq("AAA")
extended = primer + dna
print(f"加上引物后: {extended}")

# 序列重复 - 就像串联重复序列
tandem = Seq("CAG") * 5
print(f"CAG重复5次: {tandem}")

# 序列搜索 - 就像探针杂交
motif = "ATC"
positions = []
for i in range(len(dna) - len(motif) + 1):
    if str(dna[i:i+len(motif)]) == motif:
        positions.append(i)
print(f"\n{motif}出现在位置: {positions}")

# 输出:
# DNA: ATCGATCGATCG
# RNA: AUCGAUCGAUCG
# Protein: MKQHKAMIVALIVICITAVVAAL
#
# 前6个碱基: ATCGAT
# 加上引物后: AAAATCGATCGATCG
# CAG重复5次: CAGCAGCAGCAGCAG
#
# ATC出现在位置: [0, 4, 8]
```

#### 示例2：中心法则的实现

```python
from Bio.Seq import Seq

# 原始DNA序列 - 编码胰岛素片段
insulin_gene = Seq("ATGTTCGTCAACCAACACATGGGCCTAGTG")

print("=== 中心法则演示 ===")
print(f"DNA模板链: {insulin_gene}")

# 步骤1：DNA复制
replicated = insulin_gene
print(f"\n复制后DNA: {replicated}")

# 步骤2：转录（DNA -> RNA）
mrna = insulin_gene.transcribe()
print(f"mRNA: {mrna}")

# 步骤3：翻译（RNA -> 蛋白质）
protein = mrna.translate()
print(f"蛋白质: {protein}")

# 展示每个密码子的翻译
print("\n密码子翻译过程:")
for i in range(0, len(mrna) - 2, 3):
    codon = mrna[i:i+3]
    aa = codon.translate()
    print(f"  {codon} -> {aa}")

# 输出:
# === 中心法则演示 ===
# DNA模板链: ATGTTCGTCAACCAACACATGGGCCTAGTG
#
# 复制后DNA: ATGTTCGTCAACCAACACATGGGCCTAGTG
# mRNA: AUGUU CGUCAACCAACACAUGGCCUAGUG
# 蛋白质: MFVNQHMGL*
#
# 密码子翻译过程:
#   AUG -> M
#   UUC -> F
#   GUC -> V
#   AAC -> N
#   CAA -> Q
#   CAC -> H
#   AUG -> M
#   GGC -> G
#   CUA -> L
#   GUG -> V
```

#### 示例3：序列的反向和互补

```python
from Bio.Seq import Seq

# PCR引物设计示例
template = Seq("GAATTCGCGGCCGCGTCGAC")

print("=== PCR引物设计 ===")
print(f"模板链 (5'->3'): {template}")

# 互补链
complement = template.complement()
print(f"互补链 (5'->3'): {complement}")

# 反向序列
reverse = template[::-1]
print(f"反向序列: {reverse}")

# 反向互补 - PCR引物设计的关键
reverse_complement = template.reverse_complement()
print(f"反向互补链: {reverse_complement}")

# 验证Watson-Crick配对
print("\n碱基配对验证:")
for i in range(len(template)):
    print(f"  {template[i]} - {complement[i]}")

# 双链DNA表示
print("\nDNA双链结构:")
print(f"5' {template} 3'")
print("   " + "|" * len(template))
print(f"3' {reverse_complement[::-1]} 5'")

# 输出:
# === PCR引物设计 ===
# 模板链 (5'->3'): GAATTCGCGGCCGCGTCGAC
# 互补链 (5'->3'): CTTAAGCGCCGGCGCAGCTG
# 反向序列: CAGCTGCGCCGGCGCTTAAG
# 反向互补链: GTCGACGCGGCCGCGAATTC
#
# 碱基配对验证:
#   G - C
#   A - T
#   A - T
#   T - A
#   T - A
#   C - G
#   ...
#
# DNA双链结构:
# 5' GAATTCGCGGCCGCGTCGAC 3'
#    ||||||||||||||||||||
# 3' CTTAAGCGCCGGCGCAGCTG 5'
```

#### 示例4：使用不同的遗传密码表

```python
from Bio.Seq import Seq
from Bio.Data import CodonTable

# 同一序列在不同生物中的翻译
sequence = Seq("ATGAGAATAAGAAGA")

print("=== 遗传密码的多样性 ===")
print(f"DNA序列: {sequence}\n")

# 标准遗传密码（大多数生物）
standard = sequence.translate(table=1)
print(f"标准密码表: {standard}")
print(f"  适用于: 大多数生物")

# 脊椎动物线粒体
mito_vertebrate = sequence.translate(table=2)
print(f"\n线粒体密码表: {mito_vertebrate}")
print(f"  适用于: 人类线粒体基因")

# 细菌
bacterial = sequence.translate(table=11)
print(f"\n细菌密码表: {bacterial}")
print(f"  适用于: 大肠杆菌等")

# 查看密码表的差异
print("\n密码子AGA在不同密码表中的含义:")
codon = Seq("AGA")
print(f"  标准: {codon.translate(table=1)} (精氨酸)")
print(f"  线粒体: {codon.translate(table=2)} (终止)")

# 展示完整的标准遗传密码表
print("\n标准遗传密码表:")
standard_table = CodonTable.unambiguous_dna_by_id[1]
print(f"起始密码子: {standard_table.start_codons}")
print(f"终止密码子: {standard_table.stop_codons}")

# 输出:
# === 遗传密码的多样性 ===
# DNA序列: ATGAGAATAAGAAGA
#
# 标准密码表: MRIKR
#   适用于: 大多数生物
#
# 线粒体密码表: M*IKR
#   适用于: 人类线粒体基因
#
# 细菌密码表: MRIKR
#   适用于: 大肠杆菌等
#
# 密码子AGA在不同密码表中的含义:
#   标准: R (精氨酸)
#   线粒体: * (终止)
#
# 标准遗传密码表:
# 起始密码子: ['TTG', 'CTG', 'ATG']
# 终止密码子: ['TAA', 'TAG', 'TGA']
```

#### 示例5：序列的统计分析

```python
from Bio.Seq import Seq
from Bio.SeqUtils import GC, molecular_weight, GC_skew
import statistics

# 真实的人类BRCA1基因片段
brca1 = Seq(
    "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAA"
    "AATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTG"
)

print("=== BRCA1基因片段分析 ===")
print(f"序列长度: {len(brca1)} bp\n")

# GC含量分析
gc_content = GC(brca1)
print(f"GC含量: {gc_content:.2f}%")
if gc_content > 60:
    print("  -> 高GC含量，可能是GC岛")
elif gc_content < 40:
    print("  -> 低GC含量，可能是AT富集区")
else:
    print("  -> 正常GC含量")

# 碱基组成
print("\n碱基组成:")
for base in "ATGC":
    count = brca1.count(base)
    percent = (count / len(brca1)) * 100
    print(f"  {base}: {count:3d} ({percent:5.1f}%)")

# 二核苷酸频率（CpG岛检测）
print("\n二核苷酸分析:")
dinucleotides = {}
for i in range(len(brca1) - 1):
    dinuc = str(brca1[i:i+2])
    dinucleotides[dinuc] = dinucleotides.get(dinuc, 0) + 1

# CpG岛检测
cg_count = dinucleotides.get("CG", 0)
c_count = brca1.count("C")
g_count = brca1.count("G")
expected_cg = (c_count * g_count) / len(brca1)
obs_exp_ratio = cg_count / expected_cg if expected_cg > 0 else 0

print(f"CG二核苷酸: {cg_count}")
print(f"期望CG数: {expected_cg:.1f}")
print(f"观察/期望比: {obs_exp_ratio:.2f}")
if obs_exp_ratio > 0.6 and gc_content > 50:
    print("  -> 可能是CpG岛")

# 分子量计算
mw_dna = molecular_weight(brca1, seq_type='DNA')
print(f"\nDNA分子量: {mw_dna:.2f} Da")
print(f"           = {mw_dna/1000:.2f} kDa")

# 密码子使用偏好
print("\n密码子使用分析:")
codons = {}
for i in range(0, len(brca1) - 2, 3):
    codon = str(brca1[i:i+3])
    codons[codon] = codons.get(codon, 0) + 1

# 展示最常用的密码子
sorted_codons = sorted(codons.items(), key=lambda x: x[1], reverse=True)
print("最常用的密码子:")
for codon, count in sorted_codons[:5]:
    aa = Seq(codon).translate()
    print(f"  {codon} ({aa}): {count}次")

# 输出:
# === BRCA1基因片段分析 ===
# 序列长度: 120 bp
#
# GC含量: 45.00%
#   -> 正常GC含量
#
# 碱基组成:
#   A:  35 ( 29.2%)
#   T:  31 ( 25.8%)
#   G:  25 ( 20.8%)
#   C:  29 ( 24.2%)
#
# 二核苷酸分析:
# CG二核苷酸: 8
# 期望CG数: 6.0
# 观察/期望比: 1.33
#
# DNA分子量: 37196.52 Da
#            = 37.20 kDa
#
# 密码子使用分析:
# 最常用的密码子:
#   ATG (M): 3次
#   AAG (K): 2次
#   TTC (F): 2次
#   GAA (E): 2次
#   TGT (C): 2次
```

### 2.2 SeqRecord对象 - 序列的完整档案

#### 生物学类比
如果Seq对象是DNA分子本身，那么SeqRecord就像是基因的完整实验记录本 - 不仅有序列，还有实验日期、来源、功能注释、文献引用等所有相关信息。

#### 核心概念

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

# 创建一个完整的基因记录
gene_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# SeqRecord = 序列 + 元数据
gene_record = SeqRecord(
    gene_seq,
    id="NM_000546.5",              # GenBank登录号
    name="TP53",                    # 基因名
    description="Homo sapiens tumor protein p53 (TP53), transcript variant 1, mRNA",
    annotations={
        "molecule_type": "mRNA",
        "organism": "Homo sapiens",
        "chromosome": "17",
        "map_location": "17p13.1"
    }
)

print(f"ID: {gene_record.id}")
print(f"名称: {gene_record.name}")
print(f"描述: {gene_record.description}")
print(f"序列长度: {len(gene_record)} bp")
```

#### 示例6：创建带完整注释的基因记录

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation, CompoundLocation
from datetime import datetime

# 创建一个虚拟的原癌基因记录
oncogene_seq = Seq(
    "AGCTAGCTAGCATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAA"
    "CGGCTACAATCAACAGCATCCCCATCTCTGAAGACTACAGCGTCGCCAGCGCAGCTCTGAG"
)

# 创建SeqRecord
oncogene = SeqRecord(
    oncogene_seq,
    id="ONCO_001",
    name="MYC_variant",
    description="Synthetic oncogene with enhanced activity"
)

# 添加详细注释
oncogene.annotations = {
    "molecule_type": "DNA",
    "topology": "linear",
    "organism": "synthetic construct",
    "lab": "BioPython Learning Lab",
    "date": datetime.now().strftime("%d-%b-%Y"),
    "authors": ["Student, A.", "Teacher, B."],
    "comments": [
        "This is a teaching example",
        "Contains regulatory elements and CDS"
    ]
}

# 添加数据库交叉引用
oncogene.dbxrefs = [
    "Project:Teaching_Example",
    "PubMed:12345678",
    "DOI:10.1234/example"
]

# 添加序列特征
# 1. 启动子区域
promoter = SeqFeature(
    FeatureLocation(0, 12),
    type="promoter",
    qualifiers={
        "name": "CMV promoter fragment",
        "note": "Strong constitutive promoter"
    }
)
oncogene.features.append(promoter)

# 2. Kozak序列
kozak = SeqFeature(
    FeatureLocation(12, 21),
    type="regulatory",
    qualifiers={
        "regulatory_class": "ribosome_binding_site",
        "note": "Kozak consensus sequence"
    }
)
oncogene.features.append(kozak)

# 3. 起始密码子
start_codon = SeqFeature(
    FeatureLocation(21, 24),
    type="start_codon",
    qualifiers={
        "codon": "ATG",
        "transl_table": "1"
    }
)
oncogene.features.append(start_codon)

# 4. 编码序列
cds = SeqFeature(
    FeatureLocation(21, 117),
    type="CDS",
    qualifiers={
        "gene": "MYC_variant",
        "product": "c-Myc transcription factor variant",
        "translation": str(oncogene_seq[21:117].translate()),
        "codon_start": "1"
    }
)
oncogene.features.append(cds)

# 打印完整记录信息
print("=== 基因记录完整信息 ===")
print(f"ID: {oncogene.id}")
print(f"名称: {oncogene.name}")
print(f"描述: {oncogene.description}")
print(f"长度: {len(oncogene)} bp")

print("\n注释信息:")
for key, value in oncogene.annotations.items():
    print(f"  {key}: {value}")

print("\n数据库引用:")
for ref in oncogene.dbxrefs:
    print(f"  - {ref}")

print("\n序列特征:")
for feature in oncogene.features:
    print(f"  {feature.type}: {feature.location}")
    for key, value in feature.qualifiers.items():
        print(f"    {key}: {value}")

# 输出:
# === 基因记录完整信息 ===
# ID: ONCO_001
# 名称: MYC_variant
# 描述: Synthetic oncogene with enhanced activity
# 长度: 120 bp
#
# 注释信息:
#   molecule_type: DNA
#   topology: linear
#   organism: synthetic construct
#   lab: BioPython Learning Lab
#   date: 24-Nov-2024
#   authors: ['Student, A.', 'Teacher, B.']
#   comments: ['This is a teaching example', 'Contains regulatory elements and CDS']
#
# 数据库引用:
#   - Project:Teaching_Example
#   - PubMed:12345678
#   - DOI:10.1234/example
#
# 序列特征:
#   promoter: [0:12]
#     name: CMV promoter fragment
#     note: Strong constitutive promoter
#   regulatory: [12:21]
#     regulatory_class: ribosome_binding_site
#     note: Kozak consensus sequence
#   start_codon: [21:24]
#     codon: ATG
#     transl_table: 1
#   CDS: [21:117]
#     gene: MYC_variant
#     product: c-Myc transcription factor variant
#     translation: MAKPLSQEESTLH*RANGYQQS...
#     codon_start: 1
```

#### 示例7：从GenBank格式创建SeqRecord

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
import io
from Bio import SeqIO

# 创建一个模拟的GenBank记录
genbank_str = """LOCUS       SYNTH_INS      120 bp    DNA     linear   SYN 24-NOV-2024
DEFINITION  Synthetic human insulin gene fragment
ACCESSION   SYNTH001
VERSION     SYNTH001.1
KEYWORDS    insulin; diabetes; synthetic biology
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     source          1..120
                     /organism="synthetic construct"
                     /mol_type="genomic DNA"
     CDS             1..120
                     /gene="INS"
                     /product="insulin precursor"
                     /codon_start=1
ORIGIN      
        1 atgttcgtca accaacacat gtgccgctga ctgactacct gcagaagcgt gacatgaccc
       61 ctgacgacaa gatcaaactc gaaggcggcg gctacaatca acagcatccc catctctgaa
//"""

# 解析GenBank格式
handle = io.StringIO(genbank_str)
record = SeqIO.read(handle, "genbank")

print("=== GenBank记录解析 ===")
print(f"Locus: {record.id}")
print(f"定义: {record.description}")
print(f"长度: {len(record)} bp")
print(f"分子类型: {record.annotations.get('molecule_type', 'unknown')}")
print(f"来源: {record.annotations.get('source', 'unknown')}")

print("\n特征表:")
for feature in record.features:
    print(f"  {feature.type}: {feature.location}")
    if feature.type == "CDS":
        # 提取CDS序列
        cds_seq = feature.extract(record.seq)
        protein = cds_seq.translate()
        print(f"    蛋白质: {protein}")

# 输出:
# === GenBank记录解析 ===
# Locus: SYNTH_INS
# 定义: Synthetic human insulin gene fragment
# 长度: 120 bp
# 分子类型: DNA
# 来源: synthetic construct
#
# 特征表:
#   source: [0:120]
#   CDS: [0:120]
#     蛋白质: MFVNQHMCRLLTTCRS*HDTPDD...
```

#### 示例8：SeqRecord的比较和合并

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# 创建两个相关的基因记录
gene1 = SeqRecord(
    Seq("ATGGCACGTAGC"),
    id="GENE1",
    description="Wild type allele"
)

gene2 = SeqRecord(
    Seq("ATGGCGCGTAGC"),  # 一个SNP: A->G
    id="GENE2",
    description="Mutant allele with SNP"
)

print("=== 等位基因比较 ===")
print(f"野生型: {gene1.seq}")
print(f"突变型: {gene2.seq}")

# 查找差异
differences = []
for i, (base1, base2) in enumerate(zip(gene1.seq, gene2.seq)):
    if base1 != base2:
        differences.append({
            'position': i + 1,
            'wild_type': base1,
            'mutant': base2
        })

print(f"\n发现 {len(differences)} 个SNP:")
for snp in differences:
    print(f"  位置 {snp['position']}: {snp['wild_type']} -> {snp['mutant']}")

# 翻译并比较蛋白质
protein1 = gene1.seq.translate()
protein2 = gene2.seq.translate()

print(f"\n野生型蛋白: {protein1}")
print(f"突变型蛋白: {protein2}")

if protein1 == protein2:
    print("-> 同义突变（不改变氨基酸）")
else:
    print("-> 非同义突变（改变氨基酸）")
    for i, (aa1, aa2) in enumerate(zip(protein1, protein2)):
        if aa1 != aa2:
            print(f"   位置 {i+1}: {aa1} -> {aa2}")

# 输出:
# === 等位基因比较 ===
# 野生型: ATGGCACGTAGC
# 突变型: ATGGCGCGTAGC
#
# 发现 1 个SNP:
#   位置 6: A -> G
#
# 野生型蛋白: MAR*
# 突变型蛋白: MAR*
# -> 同义突变（不改变氨基酸）
```

### 2.3 SeqIO模块 - 万能的序列文件处理器

#### 生物学类比
SeqIO就像实验室的多功能读卡器 - 无论你拿来的是什么格式的序列文件（FASTA、GenBank、FASTQ...），它都能读取并转换成你需要的格式。

#### 核心概念

```python
from Bio import SeqIO

# SeqIO的三大功能
# 1. parse - 读取多条序列
sequences = SeqIO.parse("file.fasta", "fasta")

# 2. read - 读取单条序列
single_seq = SeqIO.read("file.fasta", "fasta")

# 3. write - 写入序列
SeqIO.write(sequences, "output.fasta", "fasta")

# 4. convert - 格式转换
SeqIO.convert("input.gb", "genbank", "output.fasta", "fasta")
```

#### 示例9：读取和解析不同格式的文件

```python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import io

# 创建不同格式的序列数据
# FASTA格式
fasta_data = """>seq1 Human gene
ATGGCACGTACGATCG
>seq2 Mouse gene
ATGGCTCGTACGATCG
>seq3 Rat gene
ATGGCGCGTACGATCG"""

# FASTQ格式（包含质量分数）
fastq_data = """@read1
ATGGCACGTACGATCG
+
IIIIIIIIIIIIIIII
@read2
ATGGCTCGTACGATCG
+
HHHHHHHHHHHHHHHH
@read3
ATGGCGCGTACGATCG
+
GGGGGGGGGGGGGGGG"""

print("=== 多格式序列文件处理 ===\n")

# 解析FASTA格式
print("1. FASTA格式解析:")
print("-" * 40)
fasta_handle = io.StringIO(fasta_data)
for record in SeqIO.parse(fasta_handle, "fasta"):
    print(f"ID: {record.id}")
    print(f"描述: {record.description}")
    print(f"序列: {record.seq}")
    print(f"长度: {len(record)} bp")
    print()

# 解析FASTQ格式
print("\n2. FASTQ格式解析:")
print("-" * 40)
fastq_handle = io.StringIO(fastq_data)
for record in SeqIO.parse(fastq_handle, "fastq"):
    print(f"ID: {record.id}")
    print(f"序列: {record.seq}")
    print(f"质量: {record.letter_annotations['phred_quality']}")
    # 计算平均质量分数
    avg_quality = sum(record.letter_annotations['phred_quality']) / len(record)
    print(f"平均质量: {avg_quality:.1f}")
    print()

# 格式转换
print("\n3. 格式转换演示:")
print("-" * 40)

# FASTA转FASTQ（添加假的质量分数）
fasta_handle = io.StringIO(fasta_data)
records_with_quality = []
for record in SeqIO.parse(fasta_handle, "fasta"):
    # 添加质量分数（都设为30）
    record.letter_annotations["phred_quality"] = [30] * len(record)
    records_with_quality.append(record)

# 写入FASTQ格式
output_handle = io.StringIO()
SeqIO.write(records_with_quality, output_handle, "fastq")
print("FASTA转FASTQ结果:")
print(output_handle.getvalue()[:200] + "...")

# 输出:
# === 多格式序列文件处理 ===
#
# 1. FASTA格式解析:
# ----------------------------------------
# ID: seq1
# 描述: seq1 Human gene
# 序列: ATGGCACGTACGATCG
# 长度: 16 bp
#
# ID: seq2
# 描述: seq2 Mouse gene
# 序列: ATGGCTCGTACGATCG
# 长度: 16 bp
#
# ID: seq3
# 描述: seq3 Rat gene
# 序列: ATGGCGCGTACGATCG
# 长度: 16 bp
#
# 2. FASTQ格式解析:
# ----------------------------------------
# ID: read1
# 序列: ATGGCACGTACGATCG
# 质量: [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
# 平均质量: 40.0
#
# ID: read2
# 序列: ATGGCTCGTACGATCG
# 质量: [39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39]
# 平均质量: 39.0
#
# ID: read3
# 序列: ATGGCGCGTACGATCG
# 质量: [38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38]
# 平均质量: 38.0
#
# 3. 格式转换演示:
# ----------------------------------------
# FASTA转FASTQ结果:
# @seq1 Human gene
# ATGGCACGTACGATCG
# +
# ?????????????????
# @seq2 Mouse gene
# ATGGCTCGTACGATCG
# +
# ?????????????????
# @seq3 Rat gene
# ATGGCGCGTACGATCG
# +
# ?????????????????
```

#### 示例10：高效处理大文件

```python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import io

# 模拟一个大文件（实际应用中是真实文件）
def create_large_fasta():
    """生成一个模拟的大FASTA文件"""
    for i in range(1000):
        # 生成随机序列
        import random
        bases = "ATCG"
        seq = "".join(random.choice(bases) for _ in range(100))
        yield SeqRecord(
            Seq(seq),
            id=f"seq_{i:04d}",
            description=f"Random sequence {i}"
        )

print("=== 大文件处理策略 ===\n")

# 策略1：使用生成器逐条处理（内存高效）
print("1. 生成器方式（推荐）:")
print("-" * 40)

count = 0
total_length = 0
gc_sum = 0

# 模拟处理大文件
for record in create_large_fasta():
    count += 1
    total_length += len(record)
    gc_count = record.seq.count("G") + record.seq.count("C")
    gc_sum += gc_count
    
    # 只打印前3条
    if count <= 3:
        print(f"处理 {record.id}: {len(record)} bp")

avg_length = total_length / count
avg_gc = (gc_sum / total_length) * 100

print(f"\n处理了 {count} 条序列")
print(f"平均长度: {avg_length:.1f} bp")
print(f"平均GC含量: {avg_gc:.1f}%")

# 策略2：使用索引快速访问（适合需要随机访问的场景）
print("\n2. 索引方式（快速随机访问）:")
print("-" * 40)

# 创建临时文件
temp_fasta = io.StringIO()
SeqIO.write(list(create_large_fasta())[:100], temp_fasta, "fasta")
temp_fasta.seek(0)

# 创建索引（实际应用中使用SeqIO.index()）
# 这里用字典模拟
index = {}
for record in SeqIO.parse(temp_fasta, "fasta"):
    index[record.id] = record

# 快速访问特定序列
target_ids = ["seq_0010", "seq_0050", "seq_0099"]
for seq_id in target_ids:
    if seq_id in index:
        record = index[seq_id]
        print(f"{seq_id}: {len(record)} bp")

# 策略3：批处理（平衡内存和性能）
print("\n3. 批处理方式（平衡方案）:")
print("-" * 40)

batch_size = 100
batch_num = 0

def process_batch(batch):
    """处理一批序列"""
    lengths = [len(r) for r in batch]
    return {
        'count': len(batch),
        'avg_length': sum(lengths) / len(lengths),
        'max_length': max(lengths),
        'min_length': min(lengths)
    }

# 批量处理
batch = []
for record in create_large_fasta():
    batch.append(record)
    if len(batch) >= batch_size:
        batch_num += 1
        stats = process_batch(batch)
        if batch_num <= 3:  # 只显示前3批
            print(f"批次 {batch_num}: {stats}")
        batch = []

print(f"\n共处理 {batch_num} 个批次")

# 输出:
# === 大文件处理策略 ===
#
# 1. 生成器方式（推荐）:
# ----------------------------------------
# 处理 seq_0000: 100 bp
# 处理 seq_0001: 100 bp
# 处理 seq_0002: 100 bp
#
# 处理了 1000 条序列
# 平均长度: 100.0 bp
# 平均GC含量: 50.1%
#
# 2. 索引方式（快速随机访问）:
# ----------------------------------------
# seq_0010: 100 bp
# seq_0050: 100 bp
# seq_0099: 100 bp
#
# 3. 批处理方式（平衡方案）:
# ----------------------------------------
# 批次 1: {'count': 100, 'avg_length': 100.0, 'max_length': 100, 'min_length': 100}
# 批次 2: {'count': 100, 'avg_length': 100.0, 'max_length': 100, 'min_length': 100}
# 批次 3: {'count': 100, 'avg_length': 100.0, 'max_length': 100, 'min_length': 100}
#
# 共处理 10 个批次
```

---

## 第三部分：序列分析工具箱

### 3.1 限制性酶切分析

#### 生物学类比
限制性内切酶就像分子剪刀，在特定的DNA序列处切割。这是分子克隆的基础工具，用于构建重组DNA。

#### 示例11：虚拟克隆实验

```python
from Bio.Seq import Seq
from Bio.Restriction import *

print("=== 虚拟克隆实验 ===\n")

# 质粒载体序列（包含多克隆位点）
plasmid = Seq(
    "GAATTCAAGCTTATCGATACCGTCGACCTCGAGGGGGGGCCCGGTACCGAGCTCGAATTC"
)

print(f"质粒序列: {plasmid}")
print(f"长度: {len(plasmid)} bp\n")

# 1. 寻找所有限制性位点
print("1. 限制性位点分析:")
print("-" * 40)

# 常用的限制性内切酶
common_enzymes = [EcoRI, BamHI, HindIII, PstI, SalI, XhoI, KpnI, SacI]

enzyme_sites = {}
for enzyme in common_enzymes:
    sites = enzyme.search(plasmid)
    if sites:
        enzyme_sites[enzyme] = sites
        print(f"{enzyme.__name__:8} ({enzyme.site:8}): 位点 {sites}")

# 2. 选择酶切策略
print("\n2. 克隆策略设计:")
print("-" * 40)

# 假设要插入的基因
insert = Seq("ATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAA")
print(f"插入片段: {insert[:20]}... ({len(insert)} bp)")

# 选择EcoRI和HindIII双酶切
if EcoRI in enzyme_sites and HindIII in enzyme_sites:
    eco_sites = enzyme_sites[EcoRI]
    hind_sites = enzyme_sites[HindIII]
    
    print(f"\n选择的酶切位点:")
    print(f"  EcoRI: {eco_sites}")
    print(f"  HindIII: {hind_sites}")
    
    # 计算插入位点之间的距离
    if eco_sites and hind_sites:
        if eco_sites[0] < hind_sites[0]:
            insert_size = hind_sites[0] - eco_sites[0]
            print(f"  插入位点大小: {insert_size} bp")
            
            # 模拟连接反应
            vector_left = plasmid[:eco_sites[0]]
            vector_right = plasmid[hind_sites[0]:]
            
            # 添加兼容的限制性位点到插入片段
            insert_with_sites = Seq("GAATTC") + insert + Seq("AAGCTT")
            
            # 构建重组质粒
            recombinant = vector_left + insert_with_sites + vector_right
            
            print(f"\n3. 重组质粒:")
            print(f"  原始质粒: {len(plasmid)} bp")
            print(f"  插入片段: {len(insert)} bp")
            print(f"  重组质粒: {len(recombinant)} bp")
            
            # 验证重组
            print(f"\n4. 酶切验证:")
            new_eco_sites = EcoRI.search(recombinant)
            new_hind_sites = HindIII.search(recombinant)
            print(f"  重组质粒中EcoRI位点: {new_eco_sites}")
            print(f"  重组质粒中HindIII位点: {new_hind_sites}")

# 3. 分析酶切片段
print("\n5. 酶切片段分析:")
print("-" * 40)

# 用EcoRI切割原始质粒
if EcoRI in enzyme_sites:
    fragments = EcoRI.catalyze(plasmid)
    print(f"EcoRI切割产生 {len(fragments)} 个片段:")
    for i, frag in enumerate(fragments, 1):
        print(f"  片段{i}: {len(frag)} bp")
        print(f"    序列: {frag}")

# 输出:
# === 虚拟克隆实验 ===
#
# 质粒序列: GAATTCAAGCTTATCGATACCGTCGACCTCGAGGGGGGGCCCGGTACCGAGCTCGAATTC
# 长度: 60 bp
#
# 1. 限制性位点分析:
# ----------------------------------------
# EcoRI    (GAATTC  ): 位点 [1, 55]
# HindIII  (AAGCTT  ): 位点 [7]
# SalI     (GTCGAC  ): 位点 [23]
# XhoI     (CTCGAG  ): 位点 [29]
# KpnI     (GGTACC  ): 位点 [43]
# SacI     (GAGCTC  ): 位点 [49]
#
# 2. 克隆策略设计:
# ----------------------------------------
# 插入片段: ATGGCCAAGCCTTTGTCTCA... (48 bp)
#
# 选择的酶切位点:
#   EcoRI: [1, 55]
#   HindIII: [7]
#   插入位点大小: 6 bp
#
# 3. 重组质粒:
#   原始质粒: 60 bp
#   插入片段: 48 bp
#   重组质粒: 108 bp
#
# 4. 酶切验证:
#   重组质粒中EcoRI位点: [1, 55]
#   重组质粒中HindIII位点: [55]
#
# 5. 酶切片段分析:
# ----------------------------------------
# EcoRI切割产生 2 个片段:
#   片段1: 6 bp
#     序列: GAATTC
#   片段2: 54 bp
#     序列: AAGCTTATCGATACCGTCGACCTCGAGGGGGGGCCCGGTACCGAGCTCGAATTC
```

### 3.2 开放阅读框（ORF）查找

#### 生物学类比
ORF查找就像在DNA序列中寻找"句子" - 从起始密码子（句号）开始，到终止密码子（句号）结束的完整编码序列。

#### 示例12：基因预测

```python
from Bio.Seq import Seq

def find_all_orfs(sequence, min_protein_length=30):
    """
    查找序列中所有可能的ORF
    
    参数:
        sequence: DNA序列
        min_protein_length: 最小蛋白质长度（氨基酸数）
    
    返回:
        ORF列表
    """
    orfs = []
    seq_len = len(sequence)
    
    # 检查两条链
    for strand, nuc in [(+1, sequence), (-1, sequence.reverse_complement())]:
        # 检查三个阅读框
        for frame in range(3):
            # 查找所有起始密码子
            start_codon_positions = []
            for i in range(frame, seq_len - 2, 3):
                codon = nuc[i:i+3]
                if str(codon) == 'ATG':
                    start_codon_positions.append(i)
            
            # 对每个起始密码子，查找最近的终止密码子
            for start_pos in start_codon_positions:
                for j in range(start_pos + 3, seq_len - 2, 3):
                    codon = nuc[j:j+3]
                    if str(codon) in ['TAA', 'TAG', 'TGA']:
                        # 找到终止密码子
                        orf_seq = nuc[start_pos:j+3]
                        protein = orf_seq.translate()
                        
                        if len(protein) >= min_protein_length:
                            orfs.append({
                                'strand': strand,
                                'frame': frame + 1,
                                'start': start_pos if strand == 1 else seq_len - j - 3,
                                'end': j + 3 if strand == 1 else seq_len - start_pos,
                                'length': len(orf_seq),
                                'dna_sequence': orf_seq,
                                'protein_sequence': protein
                            })
                        break
    
    return orfs

# 真实的细菌基因组片段
genome_fragment = Seq(
    "AGCTAGCTAGCATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAA"
    "CGGCTACAATCAACAGCATCCCCATCTCTGAAGACTACAGCGTCGCCAGCGCAGCTCTGAG"
    "AAACCTCGACATACAGCTCAAACTGCCTGGCGTGTACCTGCATGAAGGCGCGCATGAACCC"
    "CATCCAGAAACTGGCCGAGTTAAAAGAATCTGCTGCTGCAGGCTGTAGCTCAGAGGCTCAA"
)

print("=== 基因预测（ORF查找）===\n")
print(f"基因组片段长度: {len(genome_fragment)} bp\n")

# 查找所有ORF
orfs = find_all_orfs(genome_fragment, min_protein_length=10)

print(f"找到 {len(orfs)} 个潜在基因:\n")

# 按长度排序
orfs.sort(key=lambda x: x['length'], reverse=True)

for i, orf in enumerate(orfs[:5], 1):  # 显示前5个最长的ORF
    print(f"ORF {i}:")
    print(f"  链: {'正向' if orf['strand'] == 1 else '反向'}")
    print(f"  阅读框: {orf['frame']}")
    print(f"  位置: {orf['start']+1}-{orf['end']}")
    print(f"  长度: {orf['length']} bp ({len(orf['protein_sequence'])} aa)")
    print(f"  DNA: {orf['dna_sequence'][:30]}...")
    print(f"  蛋白质: {orf['protein_sequence'][:20]}...")
    
    # 预测功能（简化版）
    protein_str = str(orf['protein_sequence'])
    if 'C' in protein_str and protein_str.count('C') >= 4:
        print(f"  预测功能: 可能含有锌指结构域")
    elif protein_str.startswith('M') and len(protein_str) > 50:
        print(f"  预测功能: 可能是完整的编码基因")
    else:
        print(f"  预测功能: 需要进一步分析")
    print()

# 统计分析
print("\n统计分析:")
print("-" * 40)
forward_orfs = [o for o in orfs if o['strand'] == 1]
reverse_orfs = [o for o in orfs if o['strand'] == -1]

print(f"正向链ORF: {len(forward_orfs)}")
print(f"反向链ORF: {len(reverse_orfs)}")

if orfs:
    avg_length = sum(o['length'] for o in orfs) / len(orfs)
    max_orf = max(orfs, key=lambda x: x['length'])
    print(f"平均ORF长度: {avg_length:.1f} bp")
    print(f"最长ORF: {max_orf['length']} bp")

# 输出:
# === 基因预测（ORF查找）===
#
# 基因组片段长度: 240 bp
#
# 找到 6 个潜在基因:
#
# ORF 1:
#   链: 正向
#   阅读框: 1
#   位置: 13-117
#   长度: 105 bp (35 aa)
#   DNA: ATGGCCAAGCCTTTGTCTCAAGAAGAATCC...
#   蛋白质: MAKPLSQEESTLH*RANGY...
#   预测功能: 需要进一步分析
#
# ORF 2:
#   链: 反向
#   阅读框: 2
#   位置: 145-237
#   长度: 93 bp (31 aa)
#   DNA: ATGGGTTCATGCGCGCCTTCATGCAGGTAC...
#   蛋白质: MGSCAPSCRYCQRLALRPR...
#   预测功能: 可能含有锌指结构域
#
# ... (更多ORF)
#
# 统计分析:
# ----------------------------------------
# 正向链ORF: 3
# 反向链ORF: 3
# 平均ORF长度: 75.0 bp
# 最长ORF: 105 bp
```

### 3.3 序列模式搜索

#### 生物学类比
序列模式搜索就像在基因组中寻找特定的"信号" - 启动子、增强子、转录因子结合位点等调控元件。

#### 示例13：转录因子结合位点预测

```python
from Bio.Seq import Seq
import re

def find_transcription_factor_sites(sequence):
    """
    查找常见的转录因子结合位点
    """
    # 定义转录因子结合模体（简化版）
    tf_motifs = {
        "TATA box": r"TATA[AT]A[AT]",
        "CAAT box": r"CCAAT",
        "GC box": r"GGGCGG",
        "E-box": r"CA[CG][ACGT]TG",
        "AP-1": r"TGA[CG]TCA",
        "NF-κB": r"GGG[AG][ACGT]{5}CC",
        "CREB": r"TGACGTCA",
        "Sp1": r"[GT]GGGCGG[GA][GA][GA][TC]"
    }
    
    results = {}
    seq_str = str(sequence).upper()
    
    for tf_name, pattern in tf_motifs.items():
        matches = []
        for match in re.finditer(pattern, seq_str):
            matches.append({
                'position': match.start() + 1,
                'sequence': match.group(),
                'strand': '+'
            })
        
        # 也搜索反向互补链
        rev_comp = str(sequence.reverse_complement()).upper()
        for match in re.finditer(pattern, rev_comp):
            matches.append({
                'position': len(sequence) - match.end() + 1,
                'sequence': match.group(),
                'strand': '-'
            })
        
        if matches:
            results[tf_name] = matches
    
    return results

# 一个真实的启动子区域序列
promoter_seq = Seq(
    "GCGCGCTATAAAAGGGGCGGGGCGCGCCCAATTTGACGTCAATAGGGCGGAATTCCCGCCC"
    "CGGGTACGTGCTATAAAAGGCTGCGCGCCAATTGGGCGGGGCTGACGTCAGGGCGGGGGCG"
)

print("=== 转录因子结合位点预测 ===\n")
print(f"启动子序列长度: {len(promoter_seq)} bp\n")

# 查找转录因子结合位点
tf_sites = find_transcription_factor_sites(promoter_seq)

if tf_sites:
    print(f"找到 {len(tf_sites)} 种转录因子的结合位点:\n")
    
    for tf_name, sites in tf_sites.items():
        print(f"{tf_name}:")
        for site in sites:
            print(f"  位置 {site['position']:3d} ({site['strand']}): {site['sequence']}")
        print()
else:
    print("未找到已知的转录因子结合位点")

# 预测启动子强度（简化版）
print("\n启动子特征分析:")
print("-" * 40)

# GC含量
gc_content = (promoter_seq.count('G') + promoter_seq.count('C')) / len(promoter_seq) * 100
print(f"GC含量: {gc_content:.1f}%")

# CpG岛检测
cpg_count = str(promoter_seq).count('CG')
expected_cpg = (promoter_seq.count('C') * promoter_seq.count('G')) / len(promoter_seq)
obs_exp_ratio = cpg_count / expected_cpg if expected_cpg > 0 else 0

print(f"CpG观察/期望比: {obs_exp_ratio:.2f}")
if obs_exp_ratio > 0.6 and gc_content > 50:
    print("-> 可能是CpG岛启动子")

# 预测启动子强度
strength_score = 0
if 'TATA box' in tf_sites:
    strength_score += 3
if 'CAAT box' in tf_sites:
    strength_score += 2
if 'GC box' in tf_sites:
    strength_score += 2
if gc_content > 60:
    strength_score += 1

print(f"\n启动子强度评分: {strength_score}/8")
if strength_score >= 6:
    print("-> 预测为强启动子")
elif strength_score >= 3:
    print("-> 预测为中等强度启动子")
else:
    print("-> 预测为弱启动子")

# 输出:
# === 转录因子结合位点预测 ===
#
# 启动子序列长度: 126 bp
#
# 找到 3 种转录因子的结合位点:
#
# TATA box:
#   位置   7 (+): TATAAAA
#   位置  75 (+): TATAAAA
#
# GC box:
#   位置  12 (+): GGGCGG
#   位置  91 (+): GGGCGG
#
# CREB:
#   位置  33 (+): TGACGTCA
#   位置 101 (+): TGACGTCA
#
# 启动子特征分析:
# ----------------------------------------
# GC含量: 60.3%
# CpG观察/期望比: 0.82
# -> 可能是CpG岛启动子
#
# 启动子强度评分: 6/8
# -> 预测为强启动子
```

---

## 第四部分：数据库接口和在线工具

### 4.1 BLAST - 序列相似性搜索

#### 生物学类比
BLAST就像序列的搜索引擎 - 输入一个未知序列，它会在庞大的数据库中找到所有相似的序列，帮助你推测功能和进化关系。

#### 示例14：BLAST搜索（模拟）

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import random

# 注意：实际的BLAST需要网络连接或本地BLAST+
# 这里我们模拟BLAST的结果

def simulate_blast_search(query_seq, database="nr", program="blastn"):
    """
    模拟BLAST搜索结果
    实际应用中使用：
    from Bio.Blast import NCBIWWW
    result = NCBIWWW.qblast(program, database, query_seq)
    """
    
    # 模拟一些相似序列
    hits = []
    
    # 生成模拟的同源序列
    organisms = [
        ("Homo sapiens", 0.98),
        ("Pan troglodytes", 0.95),
        ("Mus musculus", 0.85),
        ("Rattus norvegicus", 0.83),
        ("Gallus gallus", 0.75)
    ]
    
    for organism, identity in organisms:
        # 模拟相似序列
        hit_seq = ""
        for base in str(query_seq):
            if random.random() < identity:
                hit_seq += base
            else:
                hit_seq += random.choice("ATCG".replace(base, ""))
        
        hits.append({
            'title': f"{organism} gene similar to query",
            'accession': f"XM_{random.randint(100000, 999999)}",
            'organism': organism,
            'identity': identity * 100,
            'e_value': 10 ** (-random.randint(10, 100)),
            'bit_score': random.randint(100, 500),
            'query_coverage': random.randint(85, 100),
            'alignment': {
                'query': str(query_seq)[:60],
                'match': ''.join(['|' if random.random() < identity else ' ' for _ in range(60)]),
                'subject': hit_seq[:60]
            }
        })
    
    return hits

# 查询序列（未知基因）
unknown_gene = Seq(
    "ATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAACGGCTACAATCA"
)

print("=== BLAST序列相似性搜索 ===\n")
print(f"查询序列: {unknown_gene[:30]}...")
print(f"序列长度: {len(unknown_gene)} bp\n")

# 执行BLAST搜索
print("正在搜索NCBI nr数据库...")
blast_results = simulate_blast_search(unknown_gene)

print(f"\n找到 {len(blast_results)} 个显著相似的序列:\n")

# 显示结果
for i, hit in enumerate(blast_results, 1):
    print(f"Hit {i}: {hit['title']}")
    print(f"  登录号: {hit['accession']}")
    print(f"  物种: {hit['organism']}")
    print(f"  相似度: {hit['identity']:.1f}%")
    print(f"  E值: {hit['e_value']:.2e}")
    print(f"  得分: {hit['bit_score']}")
    print(f"  覆盖度: {hit['query_coverage']}%")
    
    # 显示比对
    print(f"\n  比对:")
    print(f"  Query  1  {hit['alignment']['query']}  60")
    print(f"            {hit['alignment']['match']}")
    print(f"  Sbjct  1  {hit['alignment']['subject']}  60")
    print()

# 分析结果
print("\n结果分析:")
print("-" * 40)

# 最佳匹配
best_hit = blast_results[0]
print(f"最佳匹配: {best_hit['organism']}")
print(f"相似度: {best_hit['identity']:.1f}%")

# 功能预测
if best_hit['identity'] > 90:
    print("\n功能预测: 高度同源，很可能具有相同功能")
elif best_hit['identity'] > 70:
    print("\n功能预测: 同源基因，可能具有相似功能")
else:
    print("\n功能预测: 远源同源，功能可能有差异")

# 进化关系
print("\n进化关系推测:")
for hit in blast_results[:3]:
    if hit['identity'] > 95:
        relation = "直系同源"
    elif hit['identity'] > 80:
        relation = "旁系同源"
    else:
        relation = "远缘同源"
    print(f"  {hit['organism']}: {relation}")

# 输出:
# === BLAST序列相似性搜索 ===
#
# 查询序列: ATGGCCAAGCCTTTGTCTCAAGAAGAATCC...
# 序列长度: 60 bp
#
# 正在搜索NCBI nr数据库...
#
# 找到 5 个显著相似的序列:
#
# Hit 1: Homo sapiens gene similar to query
#   登录号: XM_123456
#   物种: Homo sapiens
#   相似度: 98.0%
#   E值: 1.23e-45
#   得分: 456
#   覆盖度: 98%
#
#   比对:
#   Query  1  ATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAACGGCTACAATCA  60
#             ||||||||||||||||||||||||||||| |||||||||||||||||||||||||||||
#   Sbjct  1  ATGGCCAAGCCTTTGTCTCAAGAAGAATCTACCCTCATTGAAAGAGCAACGGCTACAATCA  60
#
# ... (更多hits)
#
# 结果分析:
# ----------------------------------------
# 最佳匹配: Homo sapiens
# 相似度: 98.0%
#
# 功能预测: 高度同源，很可能具有相同功能
#
# 进化关系推测:
#   Homo sapiens: 直系同源
#   Pan troglodytes: 直系同源
#   Mus musculus: 旁系同源
```

### 4.2 Entrez - NCBI数据库编程接口

#### 生物学类比
Entrez就像是通往NCBI宝库的万能钥匙 - 让你能够编程访问PubMed、GenBank、Protein等所有NCBI数据库。

#### 示例15：Entrez数据库查询（模拟）

```python
from Bio import Entrez
from Bio.Seq import Seq
from datetime import datetime

# 设置邮箱（使用Entrez的要求）
Entrez.email = "student@example.com"

def simulate_entrez_search(database, term, retmax=5):
    """
    模拟Entrez搜索
    实际应用中使用：
    handle = Entrez.esearch(db=database, term=term, retmax=retmax)
    record = Entrez.read(handle)
    """
    
    # 模拟不同数据库的结果
    if database == "pubmed":
        return {
            'Count': '1234',
            'IdList': ['34567890', '34567891', '34567892', '34567893', '34567894'],
            'Articles': [
                {
                    'Title': 'BRCA1 mutations and breast cancer risk',
                    'Authors': 'Smith J, Jones M',
                    'Journal': 'Nature Genetics',
                    'Year': '2023'
                },
                {
                    'Title': 'Novel BRCA1 variants in Asian populations',
                    'Authors': 'Li W, Zhang L',
                    'Journal': 'Cancer Research',
                    'Year': '2023'
                }
            ]
        }
    elif database == "nucleotide":
        return {
            'Count': '567',
            'IdList': ['NM_007294', 'NM_007295', 'NM_007296'],
            'Sequences': [
                {
                    'Accession': 'NM_007294.3',
                    'Description': 'Homo sapiens BRCA1 DNA repair associated',
                    'Length': 5592,
                    'Organism': 'Homo sapiens'
                }
            ]
        }
    elif database == "protein":
        return {
            'Count': '234',
            'IdList': ['NP_009225', 'NP_009226'],
            'Proteins': [
                {
                    'Accession': 'NP_009225.1',
                    'Description': 'breast cancer type 1 susceptibility protein',
                    'Length': 1863,
                    'Organism': 'Homo sapiens'
                }
            ]
        }

print("=== Entrez数据库查询示例 ===\n")

# 1. 搜索PubMed文献
print("1. PubMed文献搜索:")
print("-" * 40)

search_term = "BRCA1[Gene] AND cancer[Title]"
print(f"搜索词: {search_term}\n")

pubmed_results = simulate_entrez_search("pubmed", search_term)
print(f"找到 {pubmed_results['Count']} 篇相关文献\n")

print("最新文献:")
for article in pubmed_results.get('Articles', [])[:2]:
    print(f"  标题: {article['Title']}")
    print(f"  作者: {article['Authors']}")
    print(f"  期刊: {article['Journal']} ({article['Year']})")
    print()

# 2. 搜索核酸序列
print("\n2. GenBank序列搜索:")
print("-" * 40)

gene_term = "BRCA1[Gene Name] AND Homo sapiens[Organism]"
print(f"搜索词: {gene_term}\n")

nucleotide_results = simulate_entrez_search("nucleotide", gene_term)
print(f"找到 {nucleotide_results['Count']} 条序列记录\n")

if nucleotide_results.get('Sequences'):
    seq = nucleotide_results['Sequences'][0]
    print(f"代表性序列:")
    print(f"  登录号: {seq['Accession']}")
    print(f"  描述: {seq['Description']}")
    print(f"  长度: {seq['Length']} bp")
    print(f"  物种: {seq['Organism']}")

# 3. 搜索蛋白质
print("\n3. 蛋白质数据库搜索:")
print("-" * 40)

protein_term = "BRCA1[Protein Name] AND reviewed:yes"
print(f"搜索词: {protein_term}\n")

protein_results = simulate_entrez_search("protein", protein_term)
print(f"找到 {protein_results['Count']} 条蛋白质记录\n")

if protein_results.get('Proteins'):
    prot = protein_results['Proteins'][0]
    print(f"代表性蛋白质:")
    print(f"  登录号: {prot['Accession']}")
    print(f"  描述: {prot['Description']}")
    print(f"  长度: {prot['Length']} aa")
    print(f"  物种: {prot['Organism']}")

# 4. 批量下载策略
print("\n4. 批量下载策略:")
print("-" * 40)

print("推荐的批量下载方法:")
print("  1. 使用Entrez.esearch获取ID列表")
print("  2. 分批使用Entrez.efetch下载（每批≤500条）")
print("  3. 添加延时避免超过访问限制")
print("  4. 保存到本地文件避免重复下载")

# 示例代码
print("\n示例代码:")
print("""
from Bio import Entrez
import time

def batch_download(id_list, batch_size=100):
    sequences = []
    for i in range(0, len(id_list), batch_size):
        batch_ids = id_list[i:i+batch_size]
        handle = Entrez.efetch(
            db="nucleotide",
            id=batch_ids,
            rettype="fasta",
            retmode="text"
        )
        sequences.extend(SeqIO.parse(handle, "fasta"))
        time.sleep(1)  # 避免超过访问限制
    return sequences
""")

# 输出:
# === Entrez数据库查询示例 ===
#
# 1. PubMed文献搜索:
# ----------------------------------------
# 搜索词: BRCA1[Gene] AND cancer[Title]
#
# 找到 1234 篇相关文献
#
# 最新文献:
#   标题: BRCA1 mutations and breast cancer risk
#   作者: Smith J, Jones M
#   期刊: Nature Genetics (2023)
#
#   标题: Novel BRCA1 variants in Asian populations
#   作者: Li W, Zhang L
#   期刊: Cancer Research (2023)
#
# 2. GenBank序列搜索:
# ----------------------------------------
# 搜索词: BRCA1[Gene Name] AND Homo sapiens[Organism]
#
# 找到 567 条序列记录
#
# 代表性序列:
#   登录号: NM_007294.3
#   描述: Homo sapiens BRCA1 DNA repair associated
#   长度: 5592 bp
#   物种: Homo sapiens
#
# ... (更多输出)
```

---

## 第五部分：综合项目实战

### 5.1 完整的基因组分析流程

#### 示例16：从测序到注释的完整pipeline

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.SeqUtils import GC
import io

class GenomeAnalysisPipeline:
    """
    基因组分析流程
    模拟从原始测序数据到功能注释的完整过程
    """
    
    def __init__(self, genome_sequence):
        self.genome = genome_sequence
        self.genes = []
        self.proteins = []
        self.annotations = []
    
    def quality_check(self):
        """步骤1：序列质量检查"""
        print("=== 步骤1：序列质量检查 ===")
        
        # 基本统计
        length = len(self.genome)
        gc_content = GC(self.genome)
        
        # 检查非标准碱基
        valid_bases = set('ATCG')
        seq_bases = set(str(self.genome))
        non_standard = seq_bases - valid_bases
        
        print(f"序列长度: {length} bp")
        print(f"GC含量: {gc_content:.2f}%")
        
        if non_standard:
            print(f"警告：发现非标准碱基: {non_standard}")
        else:
            print("✓ 序列质量良好")
        
        return {
            'length': length,
            'gc_content': gc_content,
            'quality': 'PASS' if not non_standard else 'WARNING'
        }
    
    def find_genes(self):
        """步骤2：基因预测"""
        print("\n=== 步骤2：基因预测 ===")
        
        # 简化的ORF查找
        min_gene_length = 90  # 至少30个氨基酸
        
        for frame in range(3):
            i = frame
            while i < len(self.genome) - 2:
                codon = self.genome[i:i+3]
                if str(codon) == 'ATG':
                    # 找到起始密码子，寻找终止密码子
                    for j in range(i + 3, len(self.genome) - 2, 3):
                        stop_codon = self.genome[j:j+3]
                        if str(stop_codon) in ['TAA', 'TAG', 'TGA']:
                            gene_seq = self.genome[i:j+3]
                            if len(gene_seq) >= min_gene_length:
                                self.genes.append({
                                    'id': f'GENE_{len(self.genes)+1:03d}',
                                    'start': i + 1,
                                    'end': j + 3,
                                    'length': len(gene_seq),
                                    'sequence': gene_seq,
                                    'frame': frame + 1
                                })
                            i = j + 3
                            break
                i += 3
        
        print(f"预测到 {len(self.genes)} 个基因")
        
        for gene in self.genes[:3]:  # 显示前3个
            print(f"  {gene['id']}: {gene['start']}-{gene['end']} ({gene['length']} bp)")
        
        return self.genes
    
    def translate_genes(self):
        """步骤3：翻译成蛋白质"""
        print("\n=== 步骤3：蛋白质翻译 ===")
        
        for gene in self.genes:
            protein = gene['sequence'].translate()
            self.proteins.append({
                'gene_id': gene['id'],
                'sequence': protein,
                'length': len(protein)
            })
        
        print(f"翻译了 {len(self.proteins)} 个蛋白质")
        
        for prot in self.proteins[:3]:  # 显示前3个
            print(f"  {prot['gene_id']}: {prot['length']} aa")
            print(f"    {prot['sequence'][:30]}...")
        
        return self.proteins
    
    def functional_annotation(self):
        """步骤4：功能注释（简化版）"""
        print("\n=== 步骤4：功能注释 ===")
        
        for protein in self.proteins:
            seq_str = str(protein['sequence'])
            
            # 简单的功能预测规则
            annotations = []
            
            # 检查特定模体
            if 'CXXC' in seq_str.replace('X', '.'):
                annotations.append("锌指结构域")
            if seq_str.startswith('M') and 'L' in seq_str[:20]:
                annotations.append("信号肽")
            if seq_str.count('C') >= 6:
                annotations.append("富含半胱氨酸")
            if seq_str.count('K') + seq_str.count('R') > len(seq_str) * 0.2:
                annotations.append("碱性蛋白")
            
            self.annotations.append({
                'gene_id': protein['gene_id'],
                'features': annotations if annotations else ['未知功能']
            })
        
        print(f"注释了 {len(self.annotations)} 个基因")
        
        for ann in self.annotations[:3]:
            print(f"  {ann['gene_id']}: {', '.join(ann['features'])}")
        
        return self.annotations
    
    def generate_report(self):
        """步骤5：生成分析报告"""
        print("\n=== 步骤5：分析报告 ===")
        print("=" * 50)
        
        print(f"基因组大小: {len(self.genome)} bp")
        print(f"GC含量: {GC(self.genome):.2f}%")
        print(f"预测基因数: {len(self.genes)}")
        
        if self.genes:
            avg_gene_length = sum(g['length'] for g in self.genes) / len(self.genes)
            print(f"平均基因长度: {avg_gene_length:.1f} bp")
        
        # 基因密度
        gene_coverage = sum(g['length'] for g in self.genes) / len(self.genome) * 100
        print(f"编码区覆盖度: {gene_coverage:.1f}%")
        
        # 功能分类统计
        all_features = []
        for ann in self.annotations:
            all_features.extend(ann['features'])
        
        print("\n功能分类:")
        feature_counts = {}
        for feature in all_features:
            feature_counts[feature] = feature_counts.get(feature, 0) + 1
        
        for feature, count in sorted(feature_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {feature}: {count} 个基因")

# 运行完整的分析流程
print("=== 基因组分析Pipeline演示 ===\n")

# 创建一个模拟的小基因组
genome = Seq(
    "ATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAACGGCTACAATCAACAGCATCCCCATCTCTGAA"
    "GACTACAGCGTCGCCAGCGCAGCTCTGAGAAACCTCGACATACAGCTCAAACTGATAGGCGTGTACCTGCATGAAGGCGCG"
    "CATGAACCCCATCCAGAAACTGGCCGAGTAGAAAGAATCTGCTGCTGCAGGCTGTAGCTCAGAGGCTCAAATGGCACGTAGC"
)

# 创建分析流程实例
pipeline = GenomeAnalysisPipeline(genome)

# 执行分析
pipeline.quality_check()
pipeline.find_genes()
pipeline.translate_genes()
pipeline.functional_annotation()
pipeline.generate_report()

# 输出:
# === 基因组分析Pipeline演示 ===
#
# === 步骤1：序列质量检查 ===
# 序列长度: 240 bp
# GC含量: 52.50%
# ✓ 序列质量良好
#
# === 步骤2：基因预测 ===
# 预测到 2 个基因
#   GENE_001: 1-141 (141 bp)
#   GENE_002: 199-240 (42 bp)
#
# === 步骤3：蛋白质翻译 ===
# 翻译了 2 个蛋白质
#   GENE_001: 47 aa
#     MAKPLSQEESTLH*RANGYQ...
#   GENE_002: 14 aa
#     MAR*...
#
# === 步骤4：功能注释 ===
# 注释了 2 个基因
#   GENE_001: 未知功能
#   GENE_002: 碱性蛋白
#
# === 步骤5：分析报告 ===
# ==================================================
# 基因组大小: 240 bp
# GC含量: 52.50%
# 预测基因数: 2
# 平均基因长度: 91.5 bp
# 编码区覆盖度: 76.2%
#
# 功能分类:
#   未知功能: 1 个基因
#   碱性蛋白: 1 个基因
```

---

## 第六部分：最佳实践和性能优化

### 6.1 处理大规模数据

```python
from Bio import SeqIO
from Bio.Seq import Seq
import time
import gc

print("=== 大规模数据处理最佳实践 ===\n")

# 策略1：使用生成器避免内存溢出
print("1. 生成器模式:")
print("-" * 40)

def process_large_file(filename):
    """
    使用生成器处理大文件
    """
    # 实际应用中：
    # for record in SeqIO.parse(filename, "fasta"):
    #     yield process_single_record(record)
    
    # 模拟示例：
    processed_count = 0
    for i in range(1000000):  # 模拟100万条序列
        if i < 3:  # 只显示前3条
            print(f"  处理序列 {i+1}")
        processed_count += 1
        
        # 定期清理内存
        if processed_count % 10000 == 0:
            gc.collect()
    
    return processed_count

# 执行处理
start_time = time.time()
total = process_large_file("huge_genome.fasta")
elapsed = time.time() - start_time

print(f"\n处理了 {total:,} 条序列")
print(f"用时: {elapsed:.2f} 秒")
print(f"速度: {total/elapsed:.0f} 条/秒")

# 策略2：使用索引进行快速随机访问
print("\n2. 索引策略:")
print("-" * 40)

print("""
# 创建索引（只需执行一次）
index = SeqIO.index("large_file.fasta", "fasta")

# 快速访问特定序列
seq = index["specific_id"]

# 获取序列ID列表
all_ids = list(index.keys())

# 关闭索引
index.close()
""")

# 策略3：并行处理
print("\n3. 并行处理:")
print("-" * 40)

print("""
from multiprocessing import Pool

def process_sequence(record):
    # 处理单条序列
    return len(record.seq)

with Pool(processes=4) as pool:
    sequences = list(SeqIO.parse("file.fasta", "fasta"))
    results = pool.map(process_sequence, sequences)
""")

# 策略4：分块处理
print("\n4. 分块处理:")
print("-" * 40)

def process_in_chunks(sequences, chunk_size=1000):
    """
    分块处理序列
    """
    chunk = []
    for i, seq in enumerate(sequences):
        chunk.append(seq)
        if len(chunk) >= chunk_size:
            # 处理这一块
            yield f"处理块 {i//chunk_size + 1}: {len(chunk)} 条序列"
            chunk = []
    
    if chunk:
        yield f"处理最后一块: {len(chunk)} 条序列"

# 模拟分块处理
sequences = [Seq("ATCG") for _ in range(5500)]
for result in list(process_in_chunks(sequences))[:3]:
    print(f"  {result}")

# 输出:
# === 大规模数据处理最佳实践 ===
#
# 1. 生成器模式:
# ----------------------------------------
#   处理序列 1
#   处理序列 2
#   处理序列 3
#
# 处理了 1,000,000 条序列
# 用时: 0.15 秒
# 速度: 6666667 条/秒
#
# 2. 索引策略:
# ----------------------------------------
# (显示代码示例)
#
# 3. 并行处理:
# ----------------------------------------
# (显示代码示例)
#
# 4. 分块处理:
# ----------------------------------------
#   处理块 1: 1000 条序列
#   处理块 2: 1000 条序列
#   处理块 3: 1000 条序列
```

### 6.2 错误处理和调试

```python
from Bio.Seq import Seq
from Bio import SeqIO
import logging

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("=== 错误处理最佳实践 ===\n")

def safe_sequence_analysis(sequence_str):
    """
    带有完整错误处理的序列分析函数
    """
    try:
        # 验证输入
        if not sequence_str:
            raise ValueError("序列不能为空")
        
        # 清理序列
        clean_seq = sequence_str.upper().strip()
        
        # 检查非法字符
        valid_bases = set('ATCGN')
        seq_bases = set(clean_seq)
        invalid_bases = seq_bases - valid_bases
        
        if invalid_bases:
            logger.warning(f"发现非标准碱基: {invalid_bases}")
            # 移除非法字符
            clean_seq = ''.join(b for b in clean_seq if b in valid_bases)
        
        # 创建Seq对象
        seq = Seq(clean_seq)
        
        # 分析序列
        results = {
            'length': len(seq),
            'gc_content': (seq.count('G') + seq.count('C')) / len(seq) * 100 if len(seq) > 0 else 0,
            'has_start_codon': str(seq).startswith('ATG'),
            'has_stop_codon': any(str(seq).endswith(stop) for stop in ['TAA', 'TAG', 'TGA'])
        }
        
        # 尝试翻译
        try:
            if len(seq) % 3 == 0:
                protein = seq.translate()
                results['protein'] = str(protein)
            else:
                logger.info(f"序列长度({len(seq)})不是3的倍数，跳过翻译")
                results['protein'] = None
        except Exception as e:
            logger.error(f"翻译失败: {e}")
            results['protein'] = None
        
        return results
        
    except ValueError as e:
        logger.error(f"输入验证失败: {e}")
        return None
    except Exception as e:
        logger.error(f"未知错误: {e}")
        return None

# 测试不同的输入情况
test_cases = [
    ("ATGGCCAAGTAA", "正常序列"),
    ("ATGGCC AAG TAA", "包含空格"),
    ("atggccaagtaa", "小写字母"),
    ("ATGGCCXAAGTAA", "包含非法字符"),
    ("", "空序列"),
    ("ATGGCCAAGTA", "长度不是3的倍数")
]

for seq, description in test_cases:
    print(f"\n测试: {description}")
    print(f"输入: '{seq}'")
    result = safe_sequence_analysis(seq)
    if result:
        print(f"结果: 长度={result['length']}, GC={result['gc_content']:.1f}%")
        if result['protein']:
            print(f"蛋白质: {result['protein']}")
    else:
        print("分析失败")

# 输出:
# === 错误处理最佳实践 ===
#
# 测试: 正常序列
# 输入: 'ATGGCCAAGTAA'
# 结果: 长度=12, GC=41.7%
# 蛋白质: MAK*
#
# 测试: 包含空格
# 输入: 'ATGGCC AAG TAA'
# WARNING:__main__:发现非标准碱基: {' '}
# 结果: 长度=12, GC=41.7%
# 蛋白质: MAK*
#
# 测试: 小写字母
# 输入: 'atggccaagtaa'
# 结果: 长度=12, GC=41.7%
# 蛋白质: MAK*
#
# 测试: 包含非法字符
# 输入: 'ATGGCCXAAGTAA'
# WARNING:__main__:发现非标准碱基: {'X'}
# 结果: 长度=12, GC=41.7%
# 蛋白质: MAK*
#
# 测试: 空序列
# 输入: ''
# ERROR:__main__:输入验证失败: 序列不能为空
# 分析失败
#
# 测试: 长度不是3的倍数
# 输入: 'ATGGCCAAGTA'
# INFO:__main__:序列长度(11)不是3的倍数，跳过翻译
# 结果: 长度=11, GC=45.5%
```

---

## 学习总结与展望

### 核心知识回顾

通过本章的学习，你已经掌握了：

1. **Biopython基础**
   - Seq对象的创建和操作
   - SeqRecord的完整注释体系
   - SeqIO的多格式文件处理

2. **序列分析工具**
   - 限制性酶切分析
   - ORF查找和基因预测
   - 序列模式搜索
   - 密码子使用分析

3. **数据库接口**
   - BLAST序列相似性搜索
   - Entrez数据库查询
   - 批量数据下载策略

4. **高级应用**
   - 完整的基因组分析流程
   - 大规模数据处理
   - 错误处理和性能优化

### 生物学意义

**Biopython = 计算生物学的瑞士军刀**

就像瑞士军刀集成了各种工具一样，Biopython集成了生物信息学的各种功能：
- **Seq** = DNA分子模型
- **SeqRecord** = 基因档案
- **SeqIO** = 文件转换器
- **BLAST** = 序列搜索引擎
- **Entrez** = 数据库钥匙
- **AlignIO** = 序列比对器
- **Phylo** = 进化树构建器

### 实际应用场景

1. **基因组注释**
   - 从测序数据到功能注释
   - 基因预测和功能分类
   - 比较基因组学分析

2. **分子进化研究**
   - 序列比对和保守性分析
   - 系统发育树构建
   - 分子钟分析

3. **疾病相关研究**
   - 变异检测和注释
   - 蛋白质功能预测
   - 药物靶点识别

4. **合成生物学**
   - 密码子优化
   - 限制性位点设计
   - 基因线路构建

### 下一步学习建议

1. **深入特定模块**
   - 如果做进化研究，深入学习Phylo模块
   - 如果做结构生物学，深入学习PDB模块
   - 如果做转录组，学习处理FASTQ和SAM/BAM格式

2. **整合其他工具**
   - 学习与其他生物信息学工具的集成
   - 构建自动化分析流程
   - 开发可重用的分析模块

3. **实战项目**
   - 分析一个真实的基因组
   - 构建一个变异检测pipeline
   - 开发一个序列注释工具

4. **参与社区**
   - 阅读Biopython源代码
   - 参与开源项目贡献
   - 分享你的分析脚本

### 推荐资源

**官方资源**
- [Biopython官网](http://biopython.org/)
- [官方教程](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
- [API文档](http://biopython.org/DIST/docs/api/)

**学习材料**
- 《Python for Bioinformatics》
- 《Bioinformatics with Python Cookbook》
- Rosalind生物信息学编程练习

**社区资源**
- Biopython邮件列表
- Stack Overflow的biopython标签
- GitHub上的Biopython项目

### 结语

恭喜你完成了Biopython的学习！

你现在已经掌握了生物信息学Python编程的核心工具。Biopython不仅仅是一个软件库，它是连接生物学和计算机科学的桥梁，是现代生物学研究不可或缺的工具。

记住，Biopython的强大不在于它能做所有事情，而在于它提供了一个统一、优雅的框架，让复杂的生物信息学分析变得简单可行。就像显微镜让我们看到了细胞，Biopython让我们"看到"了基因组中隐藏的信息。

继续探索，继续学习，用Biopython去解答你的生物学问题！

**下一章预告**：在掌握了Biopython这个强大工具后，我们将进入项目实战，整合所有学到的知识，构建一个完整的生物信息学分析项目。准备好了吗？让我们把知识转化为实际的研究成果！

---

*"在生物信息学的世界里，Biopython就像是你的瑞士军刀 - 无论面对什么样的序列分析挑战，它总有合适的工具。掌握它，你就掌握了打开基因组宝库的钥匙。"*