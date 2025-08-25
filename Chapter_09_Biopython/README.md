# Chapter 09: BioPython - 生物信息学利器

## 📖 写在前面

BioPython就像生物信息学研究者的瑞士军刀——集成了序列处理、数据库查询、序列比对等核心功能。无论是基因注释、进化分析还是结构预测，BioPython都能提供专业级的解决方案。

## 🎯 学习目标

✅ **核心模块** - 掌握Seq、SeqRecord、SeqIO三大基石  
✅ **序列分析** - 限制酶切、ORF查找、模式匹配  
✅ **数据库接口** - BLAST搜索、Entrez查询  
✅ **实际应用** - 完整的序列分析流程  

---

## 🧬 第一部分：核心对象详解

### 1.1 Seq对象 - 序列的数字化身

```python
from Bio.Seq import Seq
from Bio.SeqUtils import GC, molecular_weight

print("🔬 Seq对象演示")
print("="*40)

# 创建DNA序列
dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(f"DNA序列: {dna}")
print(f"长度: {len(dna)} bp")

# 基本统计
print(f"\n📊 序列分析:")
print(f"GC含量: {GC(dna):.1f}%")
print(f"分子量: {molecular_weight(dna, seq_type='DNA')/1000:.1f} kDa")

# 中心法则演示
print(f"\n🧬 中心法则:")
rna = dna.transcribe()              # DNA → RNA  
protein = rna.translate()            # RNA → 蛋白质
print(f"转录: {dna[:15]}... → {rna[:15]}...")
print(f"翻译: {rna[:15]}... → {protein[:5]}...")

# 序列操作
print(f"\n🔄 序列操作:")
print(f"互补: {dna.complement()[:20]}...")
print(f"反向互补: {dna.reverse_complement()[:20]}...")
```

### 1.2 SeqRecord - 带注释的序列

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

print("📝 SeqRecord演示")
print("="*40)

# 创建带完整信息的基因记录
gene_seq = Seq("ATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAA")
gene_record = SeqRecord(
    gene_seq,
    id="MYC_001",
    name="c-MYC",
    description="Human c-MYC oncogene fragment",
    annotations={
        "organism": "Homo sapiens",
        "gene": "MYC",
        "chromosome": "8q24.21"
    }
)

# 添加特征注释
cds_feature = SeqFeature(
    FeatureLocation(0, len(gene_seq)),
    type="CDS",
    qualifiers={
        "gene": "MYC",
        "product": "c-Myc transcription factor",
        "codon_start": "1"
    }
)
gene_record.features.append(cds_feature)

# 显示记录信息
print(f"基因ID: {gene_record.id}")
print(f"描述: {gene_record.description}")
print(f"长度: {len(gene_record)} bp")
print(f"特征数: {len(gene_record.features)}")

# 提取CDS并翻译
for feature in gene_record.features:
    if feature.type == "CDS":
        cds_seq = feature.extract(gene_record.seq)
        protein = cds_seq.translate()
        print(f"编码蛋白: {protein[:15]}...")
```

### 1.3 SeqIO - 万能文件处理器

```python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import io

print("💾 SeqIO文件处理演示")
print("="*40)

# 创建示例FASTA数据
fasta_data = """>gene1 Human p53
ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTC
AGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
>gene2 Human BRCA1
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAA
AATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTG
>gene3 Human MYC
ATGCCCCTCAACGTTAGCTTCACCAACAGGAACTATGACCTCGACTACGACTCGGTGCA"""

# 解析FASTA格式
print("1. 解析FASTA文件:")
handle = io.StringIO(fasta_data)
sequences = list(SeqIO.parse(handle, "fasta"))

for i, record in enumerate(sequences, 1):
    gc_content = (record.seq.count('G') + record.seq.count('C')) / len(record.seq) * 100
    print(f"  序列{i}: {record.id} ({len(record)} bp, GC: {gc_content:.1f}%)")

# 格式转换演示
print(f"\n2. 格式转换 (FASTA → GenBank):")
genbank_output = io.StringIO()
SeqIO.write(sequences, genbank_output, "genbank")
print(f"已转换 {len(sequences)} 条序列")

# 批量处理策略
print(f"\n3. 大文件处理策略:")
print("  ✓ 使用生成器: for record in SeqIO.parse(file, format)")
print("  ✓ 创建索引: index = SeqIO.index(file, format)")
print("  ✓ 分批处理: 每批1000条记录")
```

---

## 🧬 第二部分：序列分析工具

### 2.1 限制酶分析

```python
from Bio.Seq import Seq
from Bio.Restriction import *

print("✂️ 限制性酶切分析")
print("="*40)

# 质粒载体序列（多克隆位点）
plasmid = Seq("GAATTCAAGCTTATCGATACCGTCGACCTCGAGGGGGGGCCCGGTACCGAGCTC")
print(f"质粒序列: {plasmid}")

# 常用限制酶
enzymes = [EcoRI, HindIII, PstI, XhoI, KpnI, SacI]

print(f"\n🔍 限制酶位点分析:")
sites_found = {}
for enzyme in enzymes:
    sites = enzyme.search(plasmid)
    if sites:
        sites_found[enzyme.site] = sites
        print(f"  {enzyme.__name__:8} ({enzyme.site}): {sites}")

# 酶切策略设计
if sites_found:
    print(f"\n🎯 克隆策略:")
    print(f"  推荐使用EcoRI + HindIII双酶切")
    print(f"  可获得定向插入")
    print(f"  兼容性好，效率高")

# 模拟酶切
fragments = EcoRI.catalyze(plasmid)
print(f"\nEcoRI切割产生 {len(fragments)} 个片段:")
for i, frag in enumerate(fragments, 1):
    print(f"  片段{i}: {len(frag)} bp")
```

### 2.2 ORF查找和基因预测

```python
from Bio.Seq import Seq

def find_orfs(sequence, min_length=60):
    """查找开放阅读框"""
    orfs = []
    
    # 检查三个读码框
    for frame in range(3):
        i = frame
        while i < len(sequence) - 2:
            codon = sequence[i:i+3]
            if str(codon) == 'ATG':  # 起始密码子
                # 查找终止密码子
                for j in range(i + 3, len(sequence) - 2, 3):
                    stop_codon = sequence[j:j+3]
                    if str(stop_codon) in ['TAA', 'TAG', 'TGA']:
                        orf_len = j + 3 - i
                        if orf_len >= min_length:
                            orfs.append({
                                'start': i + 1,
                                'end': j + 3,
                                'length': orf_len,
                                'frame': frame + 1,
                                'sequence': sequence[i:j+3]
                            })
                        i = j + 3
                        break
                else:
                    i += 3
            else:
                i += 3
    
    return orfs

print("🎯 基因预测（ORF查找）")
print("="*40)

# 细菌基因组片段
genome = Seq(
    "AGCTAGCTAGCATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAA"
    "CGGCTACAATCAACAGCATCCCCATCTCTGAAGACTACAGCGTCGCCAGCGCAGCTCTGAG"
    "AAACCTCGACATACAGCTCAAACTGATAGGCGTGTACCTGCATGAAGGCGCGCATGAACCC"
)

orfs = find_orfs(genome)
print(f"基因组长度: {len(genome)} bp")
print(f"发现 {len(orfs)} 个潜在基因:\n")

for i, orf in enumerate(orfs, 1):
    protein = orf['sequence'].translate()
    print(f"ORF {i}:")
    print(f"  位置: {orf['start']}-{orf['end']} (框架{orf['frame']})")
    print(f"  长度: {orf['length']} bp ({len(protein)} aa)")
    print(f"  蛋白: {protein[:20]}...")
    
    # 简单功能预测
    if len(protein) > 50:
        print(f"  预测: 可能是完整编码基因")
    elif protein.count('C') >= 4:
        print(f"  预测: 可能含锌指结构域")
    else:
        print(f"  预测: 需进一步分析")
    print()
```

### 2.3 序列模式搜索

```python
from Bio.Seq import Seq
import re

def find_regulatory_elements(sequence):
    """查找调控元件"""
    elements = {
        "TATA box": r"TATA[AT]A[AT]",
        "CAAT box": r"CCAAT",
        "GC box": r"GGGCGG",
        "Kozak sequence": r"[AG]CCATGG",
        "Poly-A signal": r"AATAAA",
        "E-box": r"CA[CG][ACGT]TG"
    }
    
    results = {}
    seq_str = str(sequence).upper()
    
    for name, pattern in elements.items():
        matches = []
        for match in re.finditer(pattern, seq_str):
            matches.append({
                'position': match.start() + 1,
                'sequence': match.group()
            })
        if matches:
            results[name] = matches
    
    return results

print("🎯 转录调控元件预测")
print("="*40)

# 启动子序列
promoter = Seq(
    "GCGCGCTATAAAAGGGGCGGGGCGCGCCCAATTTGACGTCAATAGGGCGGAATTCCCGCCC"
    "CGGGTACGTGCTATAAAAGGCTGCGCGCCAATTGGGCGGGGCTGACGTCAGGGCGGGGGCG"
)

print(f"启动子序列: {len(promoter)} bp")
elements = find_regulatory_elements(promoter)

if elements:
    print(f"发现 {len(elements)} 种调控元件:")
    for element, sites in elements.items():
        print(f"\n{element}:")
        for site in sites:
            print(f"  位置 {site['position']:3d}: {site['sequence']}")
else:
    print("未发现已知调控元件")

# 启动子强度预测
gc_content = (promoter.count('G') + promoter.count('C')) / len(promoter) * 100
score = 0
if 'TATA box' in elements:
    score += 3
if 'CAAT box' in elements:
    score += 2
if 'GC box' in elements:
    score += 2
if gc_content > 60:
    score += 1

print(f"\n📊 启动子分析:")
print(f"GC含量: {gc_content:.1f}%")
print(f"强度评分: {score}/8")
if score >= 6:
    print("预测: 强启动子")
elif score >= 3:
    print("预测: 中等启动子")
else:
    print("预测: 弱启动子")
```

---

## 🧬 第三部分：数据库接口

### 3.1 BLAST序列搜索（模拟）

```python
from Bio.Seq import Seq
import random

def simulate_blast_search(query_seq, database="nr"):
    """模拟BLAST搜索结果"""
    hits = []
    
    organisms = [
        ("Homo sapiens", 0.98, "人类"),
        ("Pan troglodytes", 0.95, "黑猩猩"),  
        ("Mus musculus", 0.85, "小鼠"),
        ("Rattus norvegicus", 0.83, "大鼠"),
        ("Gallus gallus", 0.75, "鸡")
    ]
    
    for organism, identity, chinese_name in organisms:
        hits.append({
            'organism': organism,
            'chinese_name': chinese_name,
            'identity': identity * 100,
            'e_value': 10 ** (-random.randint(20, 100)),
            'coverage': random.randint(90, 100),
            'accession': f"NM_{random.randint(100000, 999999)}"
        })
    
    return hits

print("🔍 BLAST序列同源性搜索")
print("="*40)

# 查询序列
query = Seq("ATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAA")
print(f"查询序列: {query[:30]}... ({len(query)} bp)")

# 执行BLAST搜索
print(f"\n正在搜索NCBI数据库...")
hits = simulate_blast_search(query)

print(f"\n🎯 发现 {len(hits)} 个同源序列:")
for i, hit in enumerate(hits, 1):
    print(f"\nHit {i}: {hit['organism']} ({hit['chinese_name']})")
    print(f"  登录号: {hit['accession']}")
    print(f"  相似度: {hit['identity']:.1f}%")
    print(f"  E值: {hit['e_value']:.2e}")
    print(f"  覆盖度: {hit['coverage']}%")

# 结果分析
best_hit = hits[0]
print(f"\n📊 分析结果:")
print(f"最佳匹配: {best_hit['chinese_name']} ({best_hit['identity']:.1f}%)")

if best_hit['identity'] > 95:
    print("结论: 高度保守，功能相同")
elif best_hit['identity'] > 80:
    print("结论: 同源基因，功能相似") 
else:
    print("结论: 远缘同源，功能可能不同")
```

### 3.2 Entrez数据库查询（模拟）

```python
# 注意：实际使用需要设置 Entrez.email
# from Bio import Entrez
# Entrez.email = "your-email@example.com"

def simulate_entrez_query(database, term):
    """模拟Entrez查询结果"""
    if database == "pubmed":
        return {
            'count': 1234,
            'articles': [
                {
                    'title': 'BRCA1基因突变与乳腺癌风险研究',
                    'authors': 'Zhang L, Wang M',
                    'journal': 'Nature Genetics',
                    'year': 2023
                },
                {
                    'title': '亚洲人群BRCA1变异分析',
                    'authors': 'Li W, Chen H', 
                    'journal': 'Cancer Research',
                    'year': 2023
                }
            ]
        }
    elif database == "nucleotide":
        return {
            'count': 567,
            'sequences': [
                {
                    'accession': 'NM_007294.3',
                    'title': 'Homo sapiens BRCA1 mRNA',
                    'length': 5592,
                    'organism': 'Homo sapiens'
                }
            ]
        }

print("🗃️ NCBI数据库查询演示")
print("="*40)

# 1. PubMed文献搜索
print("1. PubMed文献搜索:")
pubmed_results = simulate_entrez_query("pubmed", "BRCA1[Gene] AND cancer")
print(f"找到 {pubmed_results['count']} 篇相关文献")

print("最新文献:")
for article in pubmed_results['articles']:
    print(f"  《{article['title']}》")
    print(f"  作者: {article['authors']}")
    print(f"  期刊: {article['journal']} ({article['year']})")

# 2. 序列数据搜索
print(f"\n2. GenBank序列搜索:")
seq_results = simulate_entrez_query("nucleotide", "BRCA1[Gene]")
print(f"找到 {seq_results['count']} 条序列")

for seq in seq_results['sequences']:
    print(f"  {seq['accession']}: {seq['title']}")
    print(f"  长度: {seq['length']} bp ({seq['organism']})")

print(f"\n💡 实际使用提示:")
print("  1. 设置邮箱: Entrez.email = 'your@email.com'")
print("  2. 使用Entrez.esearch()搜索")
print("  3. 使用Entrez.efetch()下载")
print("  4. 添加延时避免访问限制")
```

---

## 🧬 第四部分：综合应用

### 4.1 完整基因分析流程

```python
from Bio.Seq import Seq
from Bio.SeqUtils import GC, ProtParam

class GeneAnalyzer:
    """基因分析器 - 从序列到功能的完整分析"""
    
    def __init__(self, sequence):
        self.dna = Seq(sequence) if isinstance(sequence, str) else sequence
        self.results = {}
    
    def basic_analysis(self):
        """基础序列分析"""
        self.results['length'] = len(self.dna)
        self.results['gc_content'] = GC(self.dna)
        self.results['composition'] = {
            base: self.dna.count(base) for base in 'ATCG'
        }
        
        # 检查起始和终止密码子
        self.results['has_start'] = str(self.dna).startswith('ATG')
        self.results['has_stop'] = any(
            str(self.dna).endswith(stop) for stop in ['TAA', 'TAG', 'TGA']
        )
        
        return self.results
    
    def translate_analysis(self):
        """蛋白质翻译分析"""
        if len(self.dna) % 3 == 0:
            protein = self.dna.translate()
            self.results['protein'] = str(protein)
            self.results['protein_length'] = len(protein)
            
            # 蛋白质理化性质
            if '*' not in str(protein):
                param = ProtParam.ProteinAnalysis(str(protein))
                self.results['molecular_weight'] = param.molecular_weight()
                self.results['pI'] = param.isoelectric_point()
                self.results['instability'] = param.instability_index()
            
        return self.results
    
    def predict_function(self):
        """简单功能预测"""
        predictions = []
        
        if 'protein' in self.results:
            protein = self.results['protein']
            
            # 基于序列特征的预测
            if protein.count('C') >= 6:
                predictions.append("可能含锌指结构域")
            if protein.count('H') > len(protein) * 0.1:
                predictions.append("可能是组蛋白")
            if 'instability' in self.results:
                if self.results['instability'] < 40:
                    predictions.append("稳定蛋白")
                else:
                    predictions.append("不稳定蛋白")
        
        self.results['predictions'] = predictions or ["需要进一步分析"]
        return self.results
    
    def generate_report(self):
        """生成分析报告"""
        print("🧬 基因分析报告")
        print("=" * 40)
        
        print(f"序列长度: {self.results['length']} bp")
        print(f"GC含量: {self.results['gc_content']:.1f}%")
        
        print(f"\n碱基组成:")
        for base, count in self.results['composition'].items():
            percent = count / self.results['length'] * 100
            print(f"  {base}: {count:3d} ({percent:5.1f}%)")
        
        print(f"\n结构特征:")
        print(f"  起始密码子: {'✓' if self.results['has_start'] else '✗'}")
        print(f"  终止密码子: {'✓' if self.results['has_stop'] else '✗'}")
        
        if 'protein' in self.results:
            print(f"\n蛋白质信息:")
            print(f"  长度: {self.results['protein_length']} aa")
            print(f"  序列: {self.results['protein'][:30]}...")
            
            if 'molecular_weight' in self.results:
                print(f"  分子量: {self.results['molecular_weight']/1000:.1f} kDa")
                print(f"  等电点: {self.results['pI']:.2f}")
                print(f"  稳定性指数: {self.results['instability']:.1f}")
        
        print(f"\n功能预测:")
        for prediction in self.results['predictions']:
            print(f"  • {prediction}")

# 演示完整分析流程
print("🔬 完整基因分析演示")
print("=" * 50)

# 分析一个真实的基因序列（p53片段）
p53_sequence = (
    "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTC"
    "AGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA"
    "TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGT"
)

# 创建分析器并执行分析
analyzer = GeneAnalyzer(p53_sequence)
analyzer.basic_analysis()
analyzer.translate_analysis()  
analyzer.predict_function()
analyzer.generate_report()
```

---

## 📊 本章总结

### 核心模块掌握

| 模块 | 功能 | 核心方法 |
|------|------|----------|
| **Seq** | 序列操作 | `.transcribe()`, `.translate()`, `.reverse_complement()` |
| **SeqRecord** | 带注释序列 | `.features`, `.annotations`, `.dbxrefs` |
| **SeqIO** | 文件处理 | `.parse()`, `.read()`, `.write()`, `.convert()` |
| **Restriction** | 酶切分析 | `.search()`, `.catalyze()` |

### 实用分析流程

1. **序列质控** → 基础统计 + GC含量分析
2. **基因预测** → ORF查找 + 编码能力评估  
3. **功能注释** → 同源搜索 + 结构域预测
4. **进化分析** → 多序列比对 + 系统发育

### 最佳实践

✅ **大文件处理**：使用生成器和索引  
✅ **错误处理**：验证输入格式和内容  
✅ **性能优化**：分批处理和并行计算  
✅ **结果验证**：交叉验证和统计检验  

## 🚀 下一步

掌握BioPython后，你已经具备了专业生物信息学分析的核心技能。下一章我们将整合所有知识，构建完整的研究项目，将理论转化为实际的科研成果！

---

*"BioPython不仅是工具库，更是连接生物学与计算科学的桥梁。掌握它，你就拥有了解读生命密码的数字钥匙。"*

**—— 你的生物信息学导师**