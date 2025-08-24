# Chapter 01: Python基础 - 像处理DNA一样学编程

## 🧬 为什么从这里开始？

想象你刚到一个新实验室，第一件事是什么？当然是熟悉基本工具！Python就像是你的分子生物学实验室，而变量、字符串、函数就是你的移液器、离心机和PCR仪。

在这一章，我们将通过一个每个分子生物学家都熟悉的任务来学习Python：**计算DNA序列的GC含量**。

## 🎯 学习目标

学完本章后，你将能够：
- ✅ 在Python中存储和操作DNA序列（就像在试管中保存样品）
- ✅ 计算序列的基本特征（GC含量、长度、碱基组成）
- ✅ 验证序列数据的质量（检查是否含有无效字符）
- ✅ 用代码自动完成原本需要手工计算的任务

## 🔬 生物学背景：为什么GC含量很重要？

在开始编程之前，让我们回顾一下生物学知识：

### GC含量是什么？
GC含量是指DNA序列中鸟嘌呤(G)和胞嘧啶(C)碱基占总碱基的百分比。

```
序列: ATCGATCG
G和C的数量: 4个（2个C + 2个G）
总碱基数: 8个
GC含量 = 4/8 × 100% = 50%
```

### 为什么要关注GC含量？

1. **DNA稳定性**：G-C配对有3个氢键，A-T配对只有2个
   - 高GC含量 = 更稳定的DNA = 更高的熔解温度
   
2. **PCR引物设计**：
   - 理想的引物GC含量：40-60%
   - 太低：结合不牢固
   - 太高：容易形成二级结构

3. **物种鉴定**：
   - 人类基因组：约41% GC
   - 大肠杆菌：约51% GC
   - 某些嗜热菌：>65% GC

4. **基因预测**：
   - 编码区通常有特定的GC含量模式
   - CpG岛（高GC区域）常见于基因启动子

## 📚 核心概念：用DNA类比理解Python

### 1. 变量 = 试管 🧪

在实验室中，你用试管装样品。在Python中，你用**变量**装数据。

```python
# 就像给试管贴标签
dna_sample_1 = "ATCGATCG"  # 试管1装着DNA序列
gene_name = "BRCA1"        # 试管2装着基因名称
gc_content = 45.5          # 试管3装着GC含量数值
```

**关键理解**：
- 变量名就是试管上的标签
- 等号(=)就是"装入"的动作
- 变量的值就是试管里的内容

#### 变量命名规则（就像实验室标签规范）

✅ **好的命名**（清晰、有意义）：
```python
human_sequence = "ATCG"
mouse_sequence = "GCTA"
gc_percentage = 50.0
```

❌ **避免的命名**（模糊、违规）：
```python
s = "ATCG"           # 太简短，不知道是什么
1st_seq = "ATCG"     # 不能以数字开头！
for = "ATCG"         # 'for'是Python保留字！
```

### 2. 数据类型 = 不同的生物分子 🧬

就像实验室有DNA、RNA、蛋白质等不同分子，Python也有不同的数据类型：

```python
# 字符串(str) - 像DNA/RNA序列
dna_sequence = "ATCGATCG"      # 文本数据
rna_sequence = "AUCGAUCG"      

# 整数(int) - 像碱基计数
base_count = 8                 # 整数
g_count = 2

# 浮点数(float) - 像浓度或比例
concentration = 2.5             # 小数
gc_content = 50.0              # 百分比

# 布尔值(bool) - 像是/否的实验结果
is_valid_dna = True            # 是有效DNA
has_stop_codon = False         # 没有终止密码子
```

### 3. 字符串操作 = 序列编辑 ✂️

处理DNA序列就像在实验室中剪切、连接DNA：

```python
# 原始序列（可能来自测序仪）
raw_sequence = "atcgatcg"

# 1. 标准化（转大写） - 像标准化实验条件
clean_sequence = raw_sequence.upper()  # 结果: "ATCGATCG"

# 2. 计数 - 像计算特定碱基
g_count = clean_sequence.count('G')    # 结果: 2

# 3. 获取长度 - 像测量DNA片段大小
length = len(clean_sequence)           # 结果: 8

# 4. 切片 - 像用限制酶切割
first_three = clean_sequence[0:3]      # 结果: "ATC"
last_three = clean_sequence[-3:]       # 结果: "TCG"

# 5. 连接 - 像连接反应
primer = "GGG"
new_sequence = primer + clean_sequence # 结果: "GGGATCGATCG"
```

### 4. 函数 = 实验室仪器 🔬

函数就像实验室的仪器，输入样品，得到结果：

```python
# len()函数 - 像分光光度计测量长度
sequence = "ATCGATCG"
length = len(sequence)  # 输入序列，输出长度8

# count()方法 - 像流式细胞仪计数
g_count = sequence.count('G')  # 输入'G'，输出计数2

# print()函数 - 像显示屏显示结果
print(f"序列长度: {length}")  # 显示结果
```

## 🚀 渐进式学习：从手动到自动计算GC含量

### 第1步：完全手动计算（理解原理）

```python
# 就像用眼睛数碱基
sequence = "ATCG"

# 手动数每个碱基
# A - 1个
# T - 1个  
# C - 1个
# G - 1个

# 手动计算
gc_count = 1 + 1  # C和G各1个
total = 4
gc_content = (gc_count / total) * 100
print(f"GC含量: {gc_content}%")  # 输出: 50%
```

### 第2步：使用基本函数（减少手工）

```python
sequence = "ATCGATCG"

# 让Python帮我们数
c_count = sequence.count('C')  # Python数C: 2个
g_count = sequence.count('G')  # Python数G: 2个
total = len(sequence)          # Python数总数: 8个

# 我们只需要做计算
gc_content = ((c_count + g_count) / total) * 100
print(f"GC含量: {gc_content}%")  # 输出: 50%
```

### 第3步：创建自动化函数（完全自动）

```python
def calculate_gc_content(dna_sequence):
    """
    这个函数就像一台自动GC含量分析仪
    输入: DNA序列
    输出: GC含量百分比
    """
    # 标准化序列
    sequence = dna_sequence.upper()
    
    # 自动计数
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    
    # 计算并返回结果
    if total == 0:  # 避免除零错误
        return 0
    
    gc_content = ((g_count + c_count) / total) * 100
    return gc_content

# 使用我们的"仪器"
result = calculate_gc_content("ATCGATCG")
print(f"GC含量: {result}%")
```

## 💡 Python语法详解

### 缩进：Python的"实验步骤"

Python用缩进表示代码块，就像实验protocol中的子步骤：

```python
# 主实验步骤
if sequence_is_valid:
    # 子步骤1（缩进4个空格）
    print("序列有效")
    
    # 子步骤2
    gc = calculate_gc_content(sequence)
    
    # 子步骤2的子步骤（缩进8个空格）
    if gc > 60:
        print("高GC含量")
```

### 注释：实验记录本

```python
# 这是单行注释 - 像实验本上的简短笔记

"""
这是多行注释
像实验本上的详细说明
可以写很多行
"""

# 好的注释习惯
dna = "ATCG"  # 从患者样本提取的DNA序列
gc = 50.0     # GC含量，单位：百分比
```

### 条件判断：实验结果分析

```python
# 像根据实验结果做决定
gc_content = 65.0

if gc_content < 30:
    print("低GC含量 - 可能是AT富集区")
elif gc_content < 60:
    print("正常GC含量 - 典型序列")
else:
    print("高GC含量 - 可能是GC岛")
```

## 🧪 动手实验

### 实验1：你的第一个Python程序

```python
# 1. 定义一个DNA序列（装入试管）
my_dna = "ATCGATCGATCG"

# 2. 打印出来看看（观察样品）
print("我的DNA序列:", my_dna)

# 3. 计算长度（测量）
length = len(my_dna)
print("序列长度:", length, "bp")

# 4. 计算GC含量（分析）
g_count = my_dna.count('G')
c_count = my_dna.count('C')
gc_content = ((g_count + c_count) / length) * 100
print("GC含量:", gc_content, "%")
```

**运行后你会看到：**
```
我的DNA序列: ATCGATCGATCG
序列长度: 12 bp
GC含量: 50.0 %
```

### 实验2：处理真实数据

```python
# 人类BRCA1基因片段（真实数据）
brca1 = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCA"

# 清理数据（实验室标准操作）
brca1 = brca1.upper()  # 确保大写

# 质量检查
valid_bases = set(brca1)
print("序列中的碱基类型:", valid_bases)

# 如果只有ATCG，说明序列质量好
if valid_bases.issubset({'A', 'T', 'C', 'G'}):
    print("✅ 序列质量检查通过")
    
    # 计算GC含量
    gc = ((brca1.count('G') + brca1.count('C')) / len(brca1)) * 100
    print(f"BRCA1片段GC含量: {gc:.1f}%")
else:
    print("❌ 序列包含无效字符")
```

## 📊 练习题（从易到难）

### 热身题：打印DNA
```python
# 完成代码：打印你的名字和一个DNA序列
name = "你的名字"  # 改成你的名字
dna = "ATCG"      # 改成任意DNA序列
print(?)          # 填空：打印 "我是[名字]，我的DNA是[序列]"
```

### 基础题：计算AT含量
```python
# AT含量 = 100% - GC含量
sequence = "ATCGATCG"
# 写代码计算AT含量
```

### 进阶题：序列验证
```python
# 检查序列是否只包含ATCG
sequence = "ATCGATCGN"  # N是未知碱基
# 写代码验证序列
```

### 挑战题：找出最高GC含量
```python
# 给定多个序列，找出GC含量最高的
sequences = ["ATCG", "GGCC", "ATAT"]
# 写代码找出答案
```

## 🎓 本章总结

### 你学会了什么？

1. **变量存储数据** - 就像试管装样品
2. **字符串操作** - 就像编辑DNA序列
3. **函数自动化** - 就像使用实验仪器
4. **GC含量计算** - 真实的生物信息学应用

### 记住这些类比

| Python概念 | 实验室类比 | 例子 |
|-----------|-----------|------|
| 变量 | 试管 | `dna = "ATCG"` |
| 字符串 | DNA序列 | `"ATCGATCG"` |
| 函数 | 实验仪器 | `len()`, `count()` |
| 缩进 | 实验步骤层级 | 4个空格 |
| 注释 | 实验记录 | `# 这是注释` |

### 常见错误和解决方法

❌ **错误1：大小写混淆**
```python
sequence = "atcg"
g_count = sequence.count('G')  # 结果是0！G是大写
```
✅ **解决：标准化为大写**
```python
sequence = "atcg".upper()
g_count = sequence.count('G')  # 现在正确了
```

❌ **错误2：缩进错误**
```python
if True:
print("错误")  # 没有缩进！
```
✅ **解决：正确缩进**
```python
if True:
    print("正确")  # 缩进4个空格
```

## 🚀 下一步

恭喜你完成了第一章！你已经学会了Python的基础知识，并能计算GC含量了。

在下一章，你将学习：
- **列表**：像96孔板，可以存储多个序列
- **字典**：像实验室目录，用名字查找数据
- **密码子表**：将DNA翻译成蛋白质

继续前进，让我们用Python解决更多生物学问题！

---

💡 **学习建议**：
1. 先运行示例代码，看看结果
2. 修改代码，观察变化
3. 遇到错误不要怕，这是学习的机会
4. 完成所有练习题，巩固知识

记住：每个生物信息学家都是从第一行代码开始的！