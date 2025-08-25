# 数据文件说明

本目录包含BioPython教程中使用的生物数据文件。这些文件用于演示真实生物信息学数据的处理和分析。

## 文件列表

### 📊 `gene_expression.csv` 
**用途：** Chapter_06_Pandas_Intro 数据分析演示  
**内容：** 基因表达矩阵，包含20个癌症相关基因的表达数据  
**格式：** CSV格式，包含基因ID、基因名称和4个样本的表达值  
**样本：** 2个对照样本 + 2个处理样本  
**基因：** BRCA2, TP53, GAPDH, ACTB, VEGFA等重要生物标志物  

**使用示例：**
```python
import pandas as pd
df = pd.read_csv('data/gene_expression.csv')
print(df.head())
```

### 🧬 `dna_sequence.fasta`
**用途：** 可选练习 - 真实DNA序列分析  
**内容：** 5个重要基因的DNA序列片段  
**格式：** FASTA格式  
**基因：** 
- BRCA1 (乳腺癌易感基因1)
- TP53 (肿瘤抑制基因，"基因组守护者")
- GAPDH (管家基因)
- ACTB (β-肌动蛋白，细胞骨架)
- VEGFA (血管内皮生长因子A)

**使用示例：**
```python
from Bio import SeqIO
for record in SeqIO.parse('data/dna_sequence.fasta', 'fasta'):
    print(f">{record.id}")
    print(f"Length: {len(record.seq)} bp")
```

### 📍 `gff_features.gff`
**用途：** 高级练习 - 基因组注释文件解析  
**内容：** 基因结构注释信息  
**格式：** GFF3格式  
**包含：** 基因、mRNA、外显子、CDS等特征  
**染色体：** chr17, chr12, chr7, chr6  

**使用示例：**
```python
import pandas as pd
gff = pd.read_csv('data/gff_features.gff', sep='\t', comment='#',
                  names=['seqid', 'source', 'type', 'start', 'end', 
                         'score', 'strand', 'phase', 'attributes'])
```

## 数据来源和真实性

- **基因表达数据：** 基于真实RNA-seq实验的典型数值范围
- **DNA序列：** 来自NCBI GenBank的真实基因序列片段
- **GFF注释：** 基于Ensembl基因组注释的标准格式

## 教学设计理念

这些数据文件遵循以下教学原则：

1. **真实性：** 使用真实的生物学数据和序列
2. **适度性：** 文件大小适中，不会影响加载速度
3. **代表性：** 选择的基因都是生物学研究中的重要标志物
4. **可扩展性：** 可用于多种分析场景和练习

## 使用建议

- **初学者：** 主要关注`gene_expression.csv`，用于学习数据分析
- **进阶学习：** 使用`dna_sequence.fasta`练习序列分析
- **高级用户：** 解析`gff_features.gff`学习基因组注释处理

## 文件完整性

所有文件都经过验证，确保：
- ✅ 格式正确
- ✅ 内容完整
- ✅ 编码标准
- ✅ 与教程代码兼容

如有任何问题，请查看对应章节的说明文档。