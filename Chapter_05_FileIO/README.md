# Chapter 05: 文件IO与FASTA处理 - 你的数字实验记录本

## 📌 写在最前面 - 给生物学研究者的一封信

亲爱的研究者：

还记得你第一次在实验室记录实验数据时的情景吗？你小心翼翼地打开实验记录本，工整地写下日期、实验条件、观察结果...每一个数据都是你辛苦实验的成果，每一页记录都见证着你的科研历程。

在计算机的世界里，文件就是我们的**数字实验记录本**。而今天，我要教你如何用Python来管理这些数字记录本——不仅能记录数据，还能自动整理、分析，甚至帮你发现那些人眼容易忽略的规律。

更重要的是，你将学会处理FASTA格式——这个在生物信息学领域无处不在的序列格式。无论是从NCBI下载的基因序列，还是测序公司发来的原始数据，掌握FASTA文件的处理就像掌握了打开基因密码宝库的钥匙。

让我们开始这段激动人心的学习之旅！

## 📚 本章导航

```python
学习路线图 = {
    "第一站": "理解文件的本质 - 为什么需要持久化存储",
    "第二站": "文件操作基础 - 打开、读取、写入、关闭",
    "第三站": "文件系统导航 - 路径、目录、文件管理",
    "第四站": "文本编码解密 - UTF-8、ASCII及其重要性",
    "第五站": "FASTA格式详解 - 生物信息学的通用语言",
    "第六站": "逐步构建解析器 - 从简单到专业",
    "第七站": "大文件处理策略 - 处理基因组级数据",
    "第八站": "错误处理艺术 - 让程序稳如泰山",
    "第九站": "实战项目 - 构建序列分析流程",
    "第十站": "性能优化 - 让程序飞起来"
}
```

## 🎯 学习目标

完成本章学习后，你将能够：

1. **文件操作自如**
   - 像使用实验记录本一样自然地操作文件
   - 理解文件系统的组织结构
   - 掌握各种文件操作模式

2. **FASTA格式精通**
   - 深入理解FASTA格式的设计哲学
   - 能够解析各种变体的FASTA文件
   - 会生成标准的FASTA格式输出

3. **大数据处理**
   - 处理GB级别的基因组文件
   - 使用生成器优化内存使用
   - 实现流式处理pipeline

4. **专业级编程**
   - 完善的错误处理机制
   - 模块化的代码设计
   - 可重用的工具函数

## 🔬 第一部分：为什么需要文件操作？

### 真实场景1：PCR产物测序结果

```python
"""
场景：你刚完成了一个重要基因的PCR扩增，测序公司发来了结果。
如果不保存下来，关闭程序后所有数据都会消失！
"""

# 没有文件操作时（数据只在内存中）
pcr_sequence = "ATGGAATTCGCTAGCTAG..."  # 程序关闭就消失了！

# 有了文件操作（数据永久保存）
with open("tp53_pcr_product.txt", "w") as file:
    file.write(pcr_sequence)  # 永久保存，随时可查

print("✅ 序列已保存！明天、明年都还能找到它")
```

### 真实场景2：批量样本处理

```python
"""
场景：你有100个病人的基因组数据需要分析
手动处理？那要累死了！让Python帮你自动化
"""

import os

# 获取所有样本文件
sample_files = [f for f in os.listdir("samples") if f.endswith(".fasta")]

# 批量处理
for sample in sample_files:
    print(f"正在分析 {sample}...")
    # 自动读取、分析、生成报告
    # 1小时的手工活，1分钟搞定！
```

### 真实场景3：实验数据追踪

```python
"""
场景：三个月后，导师问你："去年12月15号那个实验的数据呢？"
有了良好的文件管理，轻松找到！
"""

from datetime import datetime

# 自动命名文件，包含日期和实验信息
def save_experiment_data(data, experiment_type):
    today = datetime.now().strftime("%Y%m%d")
    filename = f"{today}_{experiment_type}_results.txt"
    
    with open(filename, "w") as f:
        f.write(f"实验日期：{datetime.now()}\n")
        f.write(f"实验类型：{experiment_type}\n")
        f.write(f"数据：\n{data}\n")
    
    return filename

# 使用示例
filename = save_experiment_data("ATCGATCG...", "PCR")
print(f"数据已保存到：{filename}")
# 输出：数据已保存到：20240115_PCR_results.txt
```

## 🗂️ 第二部分：文件系统基础 - 你的数字实验室

### 1. 理解文件系统层级

```python
"""
文件系统就像实验室的储物柜：
- 根目录 = 实验室大门
- 文件夹 = 不同的储物柜
- 文件 = 储物柜里的实验记录本
"""

import os

# 查看当前位置（你在实验室的哪个房间？）
current_dir = os.getcwd()
print(f"当前位置：{current_dir}")

# 列出当前目录的内容（这个房间有什么？）
contents = os.listdir(".")
print("\n当前目录包含：")
for item in contents:
    if os.path.isfile(item):
        print(f"  📄 文件：{item}")
    elif os.path.isdir(item):
        print(f"  📁 文件夹：{item}")
```

### 2. 路径的概念 - 寻找你的实验数据

```python
"""
路径就像实验室的地址：
- 绝对路径 = 完整地址（从实验楼大门开始）
- 相对路径 = 相对位置（从当前位置开始）
"""

import os

# 绝对路径（完整地址）
absolute_path = r"C:\Research\Projects\Gene_Analysis\data.fasta"
print(f"绝对路径示例：{absolute_path}")

# 相对路径（相对位置）
relative_path = "data/sequences.fasta"
print(f"相对路径示例：{relative_path}")

# 路径组合（拼接路径）
base_dir = "experiments"
filename = "pcr_results.txt"
full_path = os.path.join(base_dir, filename)
print(f"组合路径：{full_path}")  # experiments/pcr_results.txt

# 路径分解（拆分路径）
path = "data/2024/january/experiment.txt"
directory = os.path.dirname(path)  # data/2024/january
filename = os.path.basename(path)  # experiment.txt
print(f"目录：{directory}")
print(f"文件名：{filename}")
```

### 3. 创建目录结构 - 组织你的研究项目

```python
"""
良好的目录结构就像整洁的实验台，
让你的研究数据井井有条
"""

import os

def setup_project_structure(project_name):
    """
    创建标准的生物信息学项目结构
    """
    # 定义项目结构
    structure = {
        f"{project_name}": {
            "data": {
                "raw": "原始测序数据",
                "processed": "处理后的数据",
                "reference": "参考基因组"
            },
            "results": {
                "alignments": "序列比对结果",
                "variants": "变异分析结果",
                "figures": "图表输出"
            },
            "scripts": "分析脚本",
            "logs": "运行日志",
            "docs": "项目文档"
        }
    }
    
    # 创建目录
    def create_dirs(base_path, structure_dict):
        for dir_name, sub_structure in structure_dict.items():
            dir_path = os.path.join(base_path, dir_name)
            
            # 创建目录
            os.makedirs(dir_path, exist_ok=True)
            print(f"✅ 创建目录：{dir_path}")
            
            # 递归创建子目录
            if isinstance(sub_structure, dict):
                create_dirs(dir_path, sub_structure)
    
    create_dirs(".", structure)
    print(f"\n🎉 项目 '{project_name}' 结构创建完成！")

# 使用示例
# setup_project_structure("COVID19_Analysis")
```

## 📝 第三部分：文件操作详解 - 掌握你的数字记录本

### 1. 文件打开模式完全指南

```python
"""
文件打开模式就像使用实验记录本的不同方式：
每种模式都有特定的用途
"""

# 模式详解与示例
def demonstrate_file_modes():
    print("文件打开模式演示")
    print("=" * 60)
    
    # 模式 'r' - 只读模式（Read）
    print("\n1. 'r' 模式 - 查阅历史记录")
    print("   用途：读取现有文件，不能修改")
    try:
        with open("existing_data.txt", "r") as f:
            content = f.read()
            print(f"   读取内容：{content}")
    except FileNotFoundError:
        print("   注意：文件不存在时会报错！")
    
    # 模式 'w' - 写入模式（Write）
    print("\n2. 'w' 模式 - 全新记录")
    print("   用途：创建新文件或覆盖现有文件")
    with open("new_data.txt", "w") as f:
        f.write("这是全新的数据\n")
        f.write("之前的内容会被覆盖！")
        print("   ✅ 新文件已创建")
    
    # 模式 'a' - 追加模式（Append）
    print("\n3. 'a' 模式 - 续写记录")
    print("   用途：在文件末尾添加内容")
    with open("log.txt", "a") as f:
        f.write(f"新日志条目：实验完成\n")
        print("   ✅ 内容已追加")
    
    # 模式 'r+' - 读写模式
    print("\n4. 'r+' 模式 - 边读边改")
    print("   用途：读取并修改文件")
    with open("data.txt", "r+") as f:
        content = f.read()
        f.write("\n追加的内容")
        print("   ✅ 可以同时读写")
    
    # 模式 'x' - 独占创建模式
    print("\n5. 'x' 模式 - 独占创建")
    print("   用途：仅当文件不存在时创建")
    try:
        with open("unique.txt", "x") as f:
            f.write("这个文件之前不存在")
            print("   ✅ 独占文件已创建")
    except FileExistsError:
        print("   注意：文件已存在，无法创建！")
    
    # 二进制模式
    print("\n6. 'b' 标志 - 二进制模式")
    print("   用途：处理非文本文件（图像、压缩文件等）")
    with open("data.bin", "wb") as f:
        f.write(b'\x00\x01\x02\x03')  # 写入字节
        print("   ✅ 二进制数据已写入")
```

### 2. 读取文件的多种方法

```python
"""
读取文件就像翻阅实验记录本，
有时你想看全部，有时只想看某一页
"""

def demonstrate_reading_methods():
    # 先创建一个示例文件
    sample_content = """第一行：实验日期 2024-01-15
第二行：样本编号 S001
第三行：PCR结果 阳性
第四行：测序深度 100X
第五行：突变位点 c.215C>G"""
    
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(sample_content)
    
    print("文件读取方法演示")
    print("=" * 60)
    
    # 方法1：read() - 一次性读取全部
    print("\n方法1：read() - 读取全部内容")
    with open("sample.txt", "r", encoding="utf-8") as f:
        all_content = f.read()
        print("读取结果：")
        print(all_content)
        print(f"总字符数：{len(all_content)}")
    
    # 方法2：readline() - 逐行读取
    print("\n方法2：readline() - 读取一行")
    with open("sample.txt", "r", encoding="utf-8") as f:
        first_line = f.readline()
        second_line = f.readline()
        print(f"第一行：{first_line.strip()}")
        print(f"第二行：{second_line.strip()}")
    
    # 方法3：readlines() - 读取所有行到列表
    print("\n方法3：readlines() - 读取所有行到列表")
    with open("sample.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        print(f"共{len(all_lines)}行：")
        for i, line in enumerate(all_lines, 1):
            print(f"  行{i}：{line.strip()}")
    
    # 方法4：迭代器方式（推荐）
    print("\n方法4：迭代器 - 内存友好的逐行处理")
    with open("sample.txt", "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            print(f"  处理第{line_num}行：{line.strip()}")
    
    # 方法5：read(size) - 读取指定字节数
    print("\n方法5：read(size) - 分块读取")
    with open("sample.txt", "r", encoding="utf-8") as f:
        chunk1 = f.read(20)  # 读取20个字符
        chunk2 = f.read(20)  # 再读20个字符
        print(f"块1：{chunk1}")
        print(f"块2：{chunk2}")
    
    # 清理文件
    os.remove("sample.txt")

# 运行演示
demonstrate_reading_methods()
```

### 3. 写入文件的技巧

```python
"""
写入文件就像在实验记录本上记录数据，
需要清晰、有条理、易于查找
"""

def demonstrate_writing_techniques():
    print("文件写入技巧演示")
    print("=" * 60)
    
    # 技巧1：格式化写入
    print("\n技巧1：格式化写入 - 生成实验报告")
    
    experiment_data = {
        "date": "2024-01-15",
        "researcher": "Dr. Wang",
        "sample_id": "S001",
        "gene": "TP53",
        "mutation": "c.215C>G",
        "frequency": 0.45
    }
    
    with open("experiment_report.txt", "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("实验报告\n")
        f.write("=" * 50 + "\n\n")
        
        for key, value in experiment_data.items():
            # 使用格式化字符串
            f.write(f"{key:15s}: {value}\n")
        
        f.write("\n" + "=" * 50 + "\n")
    
    print("✅ 格式化报告已生成")
    
    # 技巧2：批量写入
    print("\n技巧2：writelines() - 批量写入多行")
    
    sequences = [
        ">seq1\n",
        "ATCGATCGATCG\n",
        ">seq2\n",
        "GCTAGCTAGCTA\n"
    ]
    
    with open("sequences.fasta", "w") as f:
        f.writelines(sequences)  # 一次写入多行
    
    print("✅ 批量数据已写入")
    
    # 技巧3：使用print函数写入文件
    print("\n技巧3：使用print写入 - 更灵活的方式")
    
    with open("analysis_log.txt", "w") as f:
        print("分析开始", file=f)
        print(f"时间：{datetime.now()}", file=f)
        print("参数设置：", file=f)
        print("  - 最小质量值：30", file=f)
        print("  - 最小覆盖度：10X", file=f)
        print("分析完成", file=f)
    
    print("✅ 日志文件已创建")
    
    # 技巧4：安全写入（先写临时文件）
    print("\n技巧4：安全写入 - 防止数据丢失")
    
    import shutil
    
    def safe_write(filename, content):
        """安全写入：先写临时文件，成功后替换"""
        temp_file = filename + ".tmp"
        
        try:
            # 写入临时文件
            with open(temp_file, "w") as f:
                f.write(content)
            
            # 成功后替换原文件
            shutil.move(temp_file, filename)
            return True
            
        except Exception as e:
            # 出错时删除临时文件
            if os.path.exists(temp_file):
                os.remove(temp_file)
            print(f"写入失败：{e}")
            return False
    
    # 使用安全写入
    important_data = "这是重要数据，不能丢失！"
    if safe_write("important.txt", important_data):
        print("✅ 重要数据已安全保存")
```

### 4. 文件位置控制

```python
"""
文件指针就像你的手指在书页上的位置，
可以精确控制从哪里开始读写
"""

def demonstrate_file_position():
    print("文件位置控制演示")
    print("=" * 60)
    
    # 创建示例文件
    with open("position_demo.txt", "w") as f:
        f.write("0123456789ABCDEFGHIJ")
    
    with open("position_demo.txt", "r+") as f:
        # tell() - 获取当前位置
        print(f"\n初始位置：{f.tell()}")  # 0
        
        # 读取5个字符
        data = f.read(5)
        print(f"读取 '{data}'")
        print(f"当前位置：{f.tell()}")  # 5
        
        # seek() - 移动到指定位置
        f.seek(10)  # 移动到第10个字符
        print(f"\n移动到位置10")
        data = f.read(5)
        print(f"读取 '{data}'")  # ABCDE
        
        # seek()的不同用法
        f.seek(0)  # 回到文件开头
        print(f"\n回到开头，位置：{f.tell()}")
        
        f.seek(0, 2)  # 移动到文件末尾
        print(f"移动到末尾，位置：{f.tell()}")
        
        # 在特定位置写入
        f.seek(5)
        f.write("***")  # 覆盖位置5-7的内容
        
        # 查看修改后的内容
        f.seek(0)
        final_content = f.read()
        print(f"\n修改后的内容：{final_content}")
    
    # 清理
    os.remove("position_demo.txt")
```

## 🧬 第四部分：文本编码 - 理解字符的数字密码

### 1. 编码基础概念

```python
"""
编码就像把文字翻译成计算机能理解的数字：
- ASCII：最早的编码，只能表示英文
- UTF-8：万国码，可以表示全世界的文字
- GBK：中文编码

在生物信息学中，我们通常使用UTF-8
"""

def demonstrate_encoding():
    print("文本编码演示")
    print("=" * 60)
    
    # 演示不同编码
    text = "DNA序列：ATCG"
    
    # UTF-8编码（推荐）
    print("\n1. UTF-8编码（推荐）")
    with open("utf8.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("✅ UTF-8文件已创建")
    
    # 读取时指定编码
    with open("utf8.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"读取内容：{content}")
    
    # 处理编码错误
    print("\n2. 处理编码错误")
    
    # 创建一个包含特殊字符的文件
    special_text = "基因：β-globin, 位置：11p15.5"
    with open("special.txt", "w", encoding="utf-8") as f:
        f.write(special_text)
    
    # 错误的编码方式
    try:
        with open("special.txt", "r", encoding="ascii") as f:
            content = f.read()
    except UnicodeDecodeError as e:
        print(f"❌ ASCII无法读取：{e}")
    
    # 正确的编码方式
    with open("special.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"✅ UTF-8正确读取：{content}")
    
    # 自动检测编码
    print("\n3. 自动检测文件编码")
    
    def detect_encoding(filename):
        """简单的编码检测"""
        encodings = ['utf-8', 'gbk', 'latin-1', 'ascii']
        
        for encoding in encodings:
            try:
                with open(filename, 'r', encoding=encoding) as f:
                    f.read()
                return encoding
            except UnicodeDecodeError:
                continue
        
        return None
    
    detected = detect_encoding("special.txt")
    print(f"检测到的编码：{detected}")
    
    # 清理文件
    for f in ["utf8.txt", "special.txt"]:
        if os.path.exists(f):
            os.remove(f)
```

### 2. 处理不同来源的文件

```python
"""
不同操作系统和软件可能使用不同的编码和换行符
Windows: \r\n
Linux/Mac: \n
"""

def handle_cross_platform_files():
    print("跨平台文件处理")
    print("=" * 60)
    
    # 处理不同的换行符
    print("\n1. 处理不同换行符")
    
    # Windows格式
    with open("windows.txt", "w", newline='\r\n') as f:
        f.write("第一行\r\n第二行\r\n")
    
    # Unix格式
    with open("unix.txt", "w", newline='\n') as f:
        f.write("第一行\n第二行\n")
    
    # Python自动处理（推荐）
    with open("windows.txt", "r") as f:
        lines = f.readlines()
        print("Windows文件的行：")
        for line in lines:
            print(f"  '{line.strip()}'")  # strip()去除换行符
    
    # 统一换行符
    print("\n2. 统一换行符格式")
    
    def normalize_line_endings(input_file, output_file):
        """将文件转换为统一的换行符格式"""
        with open(input_file, "r") as f_in:
            content = f_in.read()
        
        # 统一为\n
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        
        with open(output_file, "w", newline='\n') as f_out:
            f_out.write(content)
        
        print(f"✅ 已统一换行符：{output_file}")
    
    # 清理文件
    for f in ["windows.txt", "unix.txt"]:
        if os.path.exists(f):
            os.remove(f)
```

## 🧬 第五部分：FASTA格式深入剖析

### 1. FASTA格式的历史与演变

```python
"""
FASTA格式的故事：
1985年，William Pearson开发了FASTA算法
随之诞生的FASTA文件格式成为了生物信息学的标准

为什么FASTA如此成功？
1. 简单 - 任何文本编辑器都能打开
2. 灵活 - 可以存储各种序列信息
3. 通用 - 几乎所有生物信息学软件都支持
"""

def explore_fasta_format():
    print("FASTA格式深度解析")
    print("=" * 60)
    
    # FASTA格式规范
    print("\n1. 标准FASTA格式")
    
    standard_fasta = """>gi|123456|ref|NM_001234.5| Homo sapiens gene (GENE), mRNA
ATGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCG
GCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCG
GCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGGCG
>gi|789012|ref|NP_567890.1| protein name [Homo sapiens]
MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAG
QEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHQYREQIKRVKDSDDVPMVLVGNKCDL
"""
    
    print("标准FASTA示例：")
    print(standard_fasta)
    
    # 解析标题行
    print("\n2. 标题行格式解析")
    
    def parse_fasta_header(header):
        """解析FASTA标题行的不同格式"""
        # 去除开头的>
        header = header.lstrip('>')
        
        # NCBI格式
        if '|' in header:
            parts = header.split('|')
            return {
                'format': 'NCBI',
                'database': parts[0] if len(parts) > 0 else '',
                'id': parts[1] if len(parts) > 1 else '',
                'accession': parts[3] if len(parts) > 3 else '',
                'description': parts[4] if len(parts) > 4 else ''
            }
        
        # 简单格式
        else:
            parts = header.split(None, 1)
            return {
                'format': 'Simple',
                'id': parts[0] if parts else '',
                'description': parts[1] if len(parts) > 1 else ''
            }
    
    headers = [
        ">gi|123456|ref|NM_001234.5| Homo sapiens gene",
        ">ENSG00000141510 TP53 tumor protein p53",
        ">seq1",
        ">chr1:1000-2000 forward strand"
    ]
    
    for header in headers:
        parsed = parse_fasta_header(header)
        print(f"\n原始：{header}")
        print(f"解析：{parsed}")
    
    # FASTA变体
    print("\n3. FASTA格式变体")
    
    # 多行序列
    print("\n3a. 多行序列（标准）")
    multiline_fasta = """>sequence_1
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
TTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCC
"""
    print(multiline_fasta)
    
    # 单行序列
    print("3b. 单行序列（简化）")
    singleline_fasta = """>sequence_1
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTATTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCC
"""
    print(singleline_fasta)
    
    # 带质量值的FASTQ（相关格式）
    print("\n3c. FASTQ格式（FASTA的表亲）")
    fastq_example = """@sequence_1
ATCGATCGATCGATCGATCGATCG
+
IIIIIIIIHHHHHHHHHHHHHHHH
"""
    print(fastq_example)
```

### 2. FASTA文件的质量标准

```python
"""
什么是高质量的FASTA文件？
就像实验记录要规范一样，FASTA文件也有标准
"""

def check_fasta_quality():
    print("FASTA文件质量检查")
    print("=" * 60)
    
    def validate_fasta(filename):
        """
        全面检查FASTA文件质量
        返回质量报告
        """
        report = {
            'total_sequences': 0,
            'total_length': 0,
            'issues': [],
            'warnings': [],
            'stats': {}
        }
        
        valid_dna = set('ATCGN')
        valid_protein = set('ACDEFGHIKLMNPQRSTVWY*')
        
        with open(filename, 'r') as f:
            current_id = None
            current_seq = []
            line_num = 0
            
            for line in f:
                line_num += 1
                line = line.strip()
                
                # 空行
                if not line:
                    continue
                
                # 标题行
                if line.startswith('>'):
                    # 处理前一条序列
                    if current_id:
                        sequence = ''.join(current_seq).upper()
                        report['total_sequences'] += 1
                        report['total_length'] += len(sequence)
                        
                        # 检查序列内容
                        invalid_chars = set(sequence) - valid_dna - valid_protein
                        if invalid_chars:
                            report['warnings'].append(
                                f"序列 {current_id} 包含非标准字符: {invalid_chars}"
                            )
                        
                        # 检查序列长度
                        if len(sequence) == 0:
                            report['issues'].append(
                                f"序列 {current_id} 为空"
                            )
                        elif len(sequence) < 10:
                            report['warnings'].append(
                                f"序列 {current_id} 太短 ({len(sequence)} bp)"
                            )
                    
                    # 检查标题格式
                    if len(line) == 1:  # 只有>
                        report['issues'].append(
                            f"行 {line_num}: 空标题"
                        )
                        current_id = f"unnamed_{line_num}"
                    else:
                        current_id = line[1:].split()[0]
                    
                    current_seq = []
                
                # 序列行
                else:
                    if current_id is None:
                        report['issues'].append(
                            f"行 {line_num}: 序列出现在标题之前"
                        )
                    else:
                        current_seq.append(line)
            
            # 处理最后一条序列
            if current_id:
                sequence = ''.join(current_seq).upper()
                report['total_sequences'] += 1
                report['total_length'] += len(sequence)
        
        # 生成统计信息
        if report['total_sequences'] > 0:
            report['stats'] = {
                'average_length': report['total_length'] / report['total_sequences'],
                'quality_score': 100 - len(report['issues']) * 10 - len(report['warnings']) * 2
            }
        
        return report
    
    # 创建测试文件
    test_files = {
        "good.fasta": """>seq1 good sequence
ATCGATCGATCGATCGATCGATCG
>seq2 another good one
GCTAGCTAGCTAGCTAGCTAGCTA
""",
        "bad.fasta": """>
ATCG
>seq2
123ATCG456
>seq3
"""
    }
    
    for filename, content in test_files.items():
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"\n检查文件：{filename}")
        report = validate_fasta(filename)
        
        print(f"序列数：{report['total_sequences']}")
        print(f"总长度：{report['total_length']}")
        
        if report['issues']:
            print("❌ 严重问题：")
            for issue in report['issues']:
                print(f"  - {issue}")
        
        if report['warnings']:
            print("⚠️ 警告：")
            for warning in report['warnings']:
                print(f"  - {warning}")
        
        if report['stats']:
            print(f"质量分数：{report['stats']['quality_score']}/100")
        
        # 清理
        os.remove(filename)
```

## 🔧 第六部分：构建专业的FASTA解析器

### 1. 版本1：入门级解析器

```python
"""
第一步：能用就行
就像第一次做PCR，先让它跑起来！
"""

def build_parser_v1():
    print("构建FASTA解析器 - 版本1：入门级")
    print("=" * 60)
    
    def parse_fasta_basic(filename):
        """
        最简单的FASTA解析器
        优点：代码简单，易于理解
        缺点：内存占用大，功能有限
        """
        sequences = {}
        
        with open(filename, 'r') as f:
            content = f.read()
        
        # 按>分割获取每条序列
        entries = content.split('>')[1:]  # 跳过第一个空元素
        
        for entry in entries:
            lines = entry.strip().split('\n')
            if lines:
                header = lines[0]
                sequence = ''.join(lines[1:])
                seq_id = header.split()[0]
                sequences[seq_id] = sequence
        
        return sequences
    
    # 测试
    test_fasta = """>gene1
ATCGATCG
GCTAGCTA
>gene2
TTTTAAAA
CCCCGGGG
"""
    
    with open("test_v1.fasta", "w") as f:
        f.write(test_fasta)
    
    result = parse_fasta_basic("test_v1.fasta")
    print("\n解析结果：")
    for seq_id, sequence in result.items():
        print(f"  {seq_id}: {sequence}")
    
    print("\n✅ 优点：简单直观")
    print("❌ 缺点：大文件会占用大量内存")
    
    os.remove("test_v1.fasta")
```

### 2. 版本2：实用级解析器

```python
"""
第二步：更专业一点
像熟练的实验员，知道各种技巧
"""

def build_parser_v2():
    print("\n构建FASTA解析器 - 版本2：实用级")
    print("=" * 60)
    
    class FastaParser:
        """
        实用的FASTA解析器类
        支持多种输出格式和基本统计
        """
        
        def __init__(self, filename):
            self.filename = filename
            self.sequences = []
            self._parse()
        
        def _parse(self):
            """解析FASTA文件"""
            current_id = None
            current_desc = ""
            current_seq = []
            
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    if line.startswith('>'):
                        # 保存前一条序列
                        if current_id:
                            self.sequences.append({
                                'id': current_id,
                                'description': current_desc,
                                'sequence': ''.join(current_seq).upper()
                            })
                        
                        # 解析新标题
                        header_parts = line[1:].split(None, 1)
                        current_id = header_parts[0]
                        current_desc = header_parts[1] if len(header_parts) > 1 else ""
                        current_seq = []
                    else:
                        current_seq.append(line)
                
                # 保存最后一条
                if current_id:
                    self.sequences.append({
                        'id': current_id,
                        'description': current_desc,
                        'sequence': ''.join(current_seq).upper()
                    })
        
        def get_sequence(self, seq_id):
            """获取指定ID的序列"""
            for seq in self.sequences:
                if seq['id'] == seq_id:
                    return seq['sequence']
            return None
        
        def get_ids(self):
            """获取所有序列ID"""
            return [seq['id'] for seq in self.sequences]
        
        def statistics(self):
            """计算统计信息"""
            stats = {
                'count': len(self.sequences),
                'total_length': sum(len(seq['sequence']) for seq in self.sequences),
                'lengths': [len(seq['sequence']) for seq in self.sequences]
            }
            
            if stats['count'] > 0:
                stats['average_length'] = stats['total_length'] / stats['count']
                stats['min_length'] = min(stats['lengths'])
                stats['max_length'] = max(stats['lengths'])
            
            return stats
        
        def to_dict(self):
            """转换为字典格式"""
            return {seq['id']: seq['sequence'] for seq in self.sequences}
        
        def filter_by_length(self, min_length=0, max_length=float('inf')):
            """按长度过滤序列"""
            filtered = []
            for seq in self.sequences:
                length = len(seq['sequence'])
                if min_length <= length <= max_length:
                    filtered.append(seq)
            return filtered
    
    # 测试
    test_fasta = """>gene1 important gene
ATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTA
>gene2 another gene
TTTTAAAACCCCGGGG
>gene3 long gene
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
TTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCCGGGG
"""
    
    with open("test_v2.fasta", "w") as f:
        f.write(test_fasta)
    
    # 使用解析器
    parser = FastaParser("test_v2.fasta")
    
    print("\n解析结果：")
    print(f"序列数：{len(parser.sequences)}")
    print(f"序列ID：{parser.get_ids()}")
    
    print("\n统计信息：")
    stats = parser.statistics()
    for key, value in stats.items():
        if key != 'lengths':
            print(f"  {key}: {value}")
    
    print("\n长度过滤（>30bp）：")
    filtered = parser.filter_by_length(min_length=30)
    for seq in filtered:
        print(f"  {seq['id']}: {len(seq['sequence'])} bp")
    
    os.remove("test_v2.fasta")
```

### 3. 版本3：专业级解析器（生成器版本）

```python
"""
第三步：专业水准
像经验丰富的生物信息学家，优雅而高效
"""

def build_parser_v3():
    print("\n构建FASTA解析器 - 版本3：专业级")
    print("=" * 60)
    
    class ProfessionalFastaParser:
        """
        专业级FASTA解析器
        - 使用生成器，内存效率高
        - 完整的错误处理
        - 支持大文件
        - 可扩展的架构
        """
        
        def __init__(self, filename, validate=True):
            self.filename = filename
            self.validate = validate
            self._file_handle = None
            self._check_file()
        
        def _check_file(self):
            """检查文件有效性"""
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"文件不存在：{self.filename}")
            
            if os.path.getsize(self.filename) == 0:
                raise ValueError("文件为空")
            
            # 检查是否是FASTA格式
            with open(self.filename, 'r') as f:
                first_line = f.readline().strip()
                if not first_line.startswith('>'):
                    raise ValueError("不是有效的FASTA文件")
        
        def parse(self):
            """
            生成器方式解析FASTA
            逐条yield序列，不占用内存
            """
            current_record = None
            
            with open(self.filename, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # 跳过空行和注释
                    if not line or line.startswith('#'):
                        continue
                    
                    if line.startswith('>'):
                        # 输出前一条记录
                        if current_record and current_record['sequence']:
                            if self.validate:
                                self._validate_sequence(current_record)
                            yield current_record
                        
                        # 开始新记录
                        current_record = self._parse_header(line, line_num)
                    else:
                        # 累积序列
                        if current_record:
                            current_record['sequence'] += line.upper()
                        else:
                            raise ValueError(f"行 {line_num}: 序列出现在标题之前")
                
                # 输出最后一条
                if current_record and current_record['sequence']:
                    if self.validate:
                        self._validate_sequence(current_record)
                    yield current_record
        
        def _parse_header(self, line, line_num):
            """解析标题行"""
            header = line[1:].strip()
            
            if not header:
                header = f"unnamed_seq_{line_num}"
            
            parts = header.split(None, 1)
            
            return {
                'id': parts[0],
                'description': parts[1] if len(parts) > 1 else '',
                'sequence': '',
                'line_number': line_num
            }
        
        def _validate_sequence(self, record):
            """验证序列有效性"""
            sequence = record['sequence']
            
            # DNA/RNA碱基
            valid_nucleotides = set('ATCGUN')
            # 蛋白质氨基酸
            valid_amino_acids = set('ACDEFGHIKLMNPQRSTVWY*')
            
            # 判断序列类型
            seq_chars = set(sequence)
            
            if seq_chars <= valid_nucleotides:
                record['type'] = 'nucleotide'
                record['gc_content'] = self._calculate_gc(sequence)
            elif seq_chars <= valid_amino_acids:
                record['type'] = 'protein'
            else:
                invalid = seq_chars - valid_nucleotides - valid_amino_acids
                record['warnings'] = f"包含非标准字符: {invalid}"
        
        def _calculate_gc(self, sequence):
            """计算GC含量"""
            gc_count = sequence.count('G') + sequence.count('C')
            total = len(sequence)
            return (gc_count / total * 100) if total > 0 else 0
        
        def iterate_chunks(self, chunk_size=1000000):
            """
            按块迭代序列（用于超大序列）
            """
            for record in self.parse():
                sequence = record['sequence']
                record_info = {
                    'id': record['id'],
                    'description': record['description']
                }
                
                for i in range(0, len(sequence), chunk_size):
                    chunk = sequence[i:i + chunk_size]
                    yield {
                        **record_info,
                        'chunk_index': i // chunk_size,
                        'chunk': chunk
                    }
        
        def search(self, pattern, search_in='id'):
            """
            搜索序列
            search_in: 'id', 'description', 'sequence'
            """
            import re
            
            pattern_re = re.compile(pattern, re.IGNORECASE)
            
            for record in self.parse():
                if search_in == 'id' and pattern_re.search(record['id']):
                    yield record
                elif search_in == 'description' and pattern_re.search(record['description']):
                    yield record
                elif search_in == 'sequence' and pattern_re.search(record['sequence']):
                    yield record
        
        def extract_subset(self, id_list, output_file):
            """提取指定ID的序列子集"""
            id_set = set(id_list)
            found = set()
            
            with open(output_file, 'w') as out:
                for record in self.parse():
                    if record['id'] in id_set:
                        out.write(f">{record['id']} {record['description']}\n")
                        # 每60个字符换行
                        seq = record['sequence']
                        for i in range(0, len(seq), 60):
                            out.write(seq[i:i+60] + '\n')
                        found.add(record['id'])
            
            not_found = id_set - found
            if not_found:
                print(f"警告：未找到以下ID: {not_found}")
            
            return len(found)
    
    # 测试专业解析器
    test_fasta = """>NM_001 p53 tumor suppressor
ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTC
AGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
>NM_002 BRCA1 breast cancer gene  
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAA
AATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTG
>NP_003 myoglobin protein
MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASED
"""
    
    with open("test_v3.fasta", "w") as f:
        f.write(test_fasta)
    
    # 使用专业解析器
    parser = ProfessionalFastaParser("test_v3.fasta")
    
    print("\n使用生成器解析（内存友好）：")
    for record in parser.parse():
        print(f"\nID: {record['id']}")
        print(f"描述: {record['description']}")
        print(f"类型: {record.get('type', 'unknown')}")
        print(f"长度: {len(record['sequence'])} bp")
        if 'gc_content' in record:
            print(f"GC含量: {record['gc_content']:.1f}%")
    
    print("\n搜索功能演示：")
    print("搜索描述中包含'cancer'的序列：")
    for record in parser.search('cancer', search_in='description'):
        print(f"  找到: {record['id']} - {record['description']}")
    
    os.remove("test_v3.fasta")
```

## 💾 第七部分：大文件处理策略

### 1. 内存管理基础

```python
"""
处理大文件就像搬运货物：
- 一次性搬运（read()）：累死人，可能搬不动
- 分批搬运（生成器）：轻松高效
"""

def demonstrate_memory_management():
    print("大文件内存管理策略")
    print("=" * 60)
    
    import sys
    
    # 创建测试文件
    def create_large_file(filename, size_mb):
        """创建指定大小的测试文件"""
        import random
        
        size_bytes = size_mb * 1024 * 1024
        chunk_size = 1024  # 1KB chunks
        
        with open(filename, 'w') as f:
            written = 0
            seq_num = 1
            
            while written < size_bytes:
                # 写入FASTA格式
                f.write(f">sequence_{seq_num}\n")
                # 生成随机序列
                seq = ''.join(random.choices('ATCG', k=min(1000, size_bytes - written)))
                f.write(seq + '\n')
                
                written += len(f">sequence_{seq_num}\n") + len(seq) + 1
                seq_num += 1
        
        return seq_num - 1
    
    # 方法1：不推荐 - 一次性读取
    def process_all_at_once(filename):
        """内存密集型处理"""
        with open(filename, 'r') as f:
            content = f.read()  # 全部加载到内存！
            
        # 获取内存使用
        size = sys.getsizeof(content)
        return size, content.count('>')
    
    # 方法2：推荐 - 逐行处理
    def process_line_by_line(filename):
        """内存友好型处理"""
        count = 0
        max_line_size = 0
        
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('>'):
                    count += 1
                max_line_size = max(max_line_size, sys.getsizeof(line))
        
        return max_line_size, count
    
    # 方法3：最优 - 生成器处理
    def process_with_generator(filename):
        """使用生成器的专业处理"""
        def sequence_generator():
            with open(filename, 'r') as f:
                current_seq = None
                for line in f:
                    if line.startswith('>'):
                        if current_seq:
                            yield current_seq
                        current_seq = {'header': line.strip(), 'sequence': ''}
                    elif current_seq:
                        current_seq['sequence'] += line.strip()
                
                if current_seq:
                    yield current_seq
        
        count = 0
        total_length = 0
        
        for seq in sequence_generator():
            count += 1
            total_length += len(seq['sequence'])
        
        return count, total_length
    
    # 测试
    print("\n创建测试文件（1MB）...")
    num_seqs = create_large_file("test_large.fasta", 1)
    print(f"✅ 创建了包含 {num_seqs} 条序列的文件")
    
    # 比较内存使用
    print("\n内存使用比较：")
    
    print("\n1. 一次性读取：")
    memory, count = process_all_at_once("test_large.fasta")
    print(f"   内存占用：{memory / 1024:.1f} KB")
    print(f"   序列数：{count}")
    
    print("\n2. 逐行读取：")
    max_line_memory, count = process_line_by_line("test_large.fasta")
    print(f"   最大行内存：{max_line_memory / 1024:.1f} KB")
    print(f"   序列数：{count}")
    
    print("\n3. 生成器处理：")
    count, total_length = process_with_generator("test_large.fasta")
    print(f"   序列数：{count}")
    print(f"   总长度：{total_length} bp")
    print(f"   内存占用：极小（只存储当前序列）")
    
    # 清理
    os.remove("test_large.fasta")
```

### 2. 流式处理Pipeline

```python
"""
流式处理就像生产线：
数据像流水一样经过各个处理步骤，
不需要等待全部完成
"""

def build_streaming_pipeline():
    print("\n流式处理Pipeline")
    print("=" * 60)
    
    class SequencePipeline:
        """
        序列处理流水线
        每个步骤都是一个生成器，内存效率极高
        """
        
        @staticmethod
        def read_fasta(filename):
            """步骤1：读取FASTA文件"""
            with open(filename, 'r') as f:
                header = None
                sequence = []
                
                for line in f:
                    line = line.strip()
                    if line.startswith('>'):
                        if header:
                            yield {
                                'header': header,
                                'sequence': ''.join(sequence)
                            }
                        header = line[1:]
                        sequence = []
                    else:
                        sequence.append(line)
                
                if header:
                    yield {
                        'header': header,
                        'sequence': ''.join(sequence)
                    }
        
        @staticmethod
        def filter_length(sequences, min_length=100):
            """步骤2：过滤短序列"""
            for seq in sequences:
                if len(seq['sequence']) >= min_length:
                    yield seq
        
        @staticmethod
        def calculate_gc(sequences):
            """步骤3：计算GC含量"""
            for seq in sequences:
                sequence = seq['sequence'].upper()
                gc = sequence.count('G') + sequence.count('C')
                length = len(sequence)
                seq['gc_content'] = (gc / length * 100) if length > 0 else 0
                yield seq
        
        @staticmethod
        def filter_gc(sequences, min_gc=40, max_gc=60):
            """步骤4：按GC含量过滤"""
            for seq in sequences:
                if min_gc <= seq['gc_content'] <= max_gc:
                    yield seq
        
        @staticmethod
        def format_output(sequences):
            """步骤5：格式化输出"""
            for i, seq in enumerate(sequences, 1):
                yield {
                    'index': i,
                    'id': seq['header'].split()[0],
                    'length': len(seq['sequence']),
                    'gc': f"{seq['gc_content']:.1f}%",
                    'sequence': seq['sequence'][:50] + '...' if len(seq['sequence']) > 50 else seq['sequence']
                }
    
    # 创建测试数据
    test_data = """>seq1 short sequence
ATCG
>seq2 medium sequence
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
>seq3 high GC sequence
GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC
GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC
CGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG
>seq4 normal sequence
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
TTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCCGGGG
"""
    
    with open("pipeline_test.fasta", "w") as f:
        f.write(test_data)
    
    # 构建Pipeline
    print("\n构建处理流水线：")
    print("  1. 读取FASTA")
    print("  2. 过滤长度 >= 100bp")
    print("  3. 计算GC含量")
    print("  4. 过滤GC含量 40-60%")
    print("  5. 格式化输出")
    
    # 执行Pipeline
    pipeline = SequencePipeline()
    
    # 链式调用生成器
    sequences = pipeline.read_fasta("pipeline_test.fasta")
    sequences = pipeline.filter_length(sequences, min_length=100)
    sequences = pipeline.calculate_gc(sequences)
    sequences = pipeline.filter_gc(sequences, min_gc=40, max_gc=60)
    sequences = pipeline.format_output(sequences)
    
    # 输出结果
    print("\n处理结果：")
    for result in sequences:
        print(f"\n序列 {result['index']}:")
        print(f"  ID: {result['id']}")
        print(f"  长度: {result['length']} bp")
        print(f"  GC含量: {result['gc']}")
        print(f"  序列预览: {result['sequence']}")
    
    # 清理
    os.remove("pipeline_test.fasta")
```

### 3. 并行处理策略

```python
"""
并行处理就像多个实验员同时工作：
把大任务分给多个处理器，大大提高效率
"""

def demonstrate_parallel_processing():
    print("\n并行处理策略")
    print("=" * 60)
    
    from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
    import time
    
    def process_sequence(seq_data):
        """处理单条序列（模拟耗时操作）"""
        seq_id, sequence = seq_data
        
        # 模拟复杂计算
        gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        
        # 查找模式
        patterns_found = []
        if 'ATCG' in sequence:
            patterns_found.append('ATCG')
        if 'GGGG' in sequence:
            patterns_found.append('GGGG')
        
        return {
            'id': seq_id,
            'length': len(sequence),
            'gc_content': gc_content,
            'patterns': patterns_found
        }
    
    # 创建测试数据
    test_sequences = []
    for i in range(100):
        import random
        seq_id = f"seq_{i:03d}"
        sequence = ''.join(random.choices('ATCG', k=1000))
        test_sequences.append((seq_id, sequence))
    
    print(f"准备处理 {len(test_sequences)} 条序列")
    
    # 串行处理
    print("\n1. 串行处理：")
    start_time = time.time()
    
    serial_results = []
    for seq_data in test_sequences:
        result = process_sequence(seq_data)
        serial_results.append(result)
    
    serial_time = time.time() - start_time
    print(f"   耗时：{serial_time:.3f} 秒")
    
    # 线程并行（适合I/O密集型）
    print("\n2. 线程并行处理：")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_results = list(executor.map(process_sequence, test_sequences))
    
    thread_time = time.time() - start_time
    print(f"   耗时：{thread_time:.3f} 秒")
    print(f"   加速比：{serial_time/thread_time:.2f}x")
    
    # 进程并行（适合CPU密集型）
    print("\n3. 进程并行处理：")
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        process_results = list(executor.map(process_sequence, test_sequences))
    
    process_time = time.time() - start_time
    print(f"   耗时：{process_time:.3f} 秒")
    print(f"   加速比：{serial_time/process_time:.2f}x")
    
    # 批处理策略
    print("\n4. 批处理策略：")
    
    def process_batch(batch):
        """处理一批序列"""
        results = []
        for seq_data in batch:
            results.append(process_sequence(seq_data))
        return results
    
    # 将序列分批
    batch_size = 25
    batches = [test_sequences[i:i+batch_size] 
               for i in range(0, len(test_sequences), batch_size)]
    
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        batch_results = executor.map(process_batch, batches)
        
    # 展平结果
    final_results = []
    for batch_result in batch_results:
        final_results.extend(batch_result)
    
    batch_time = time.time() - start_time
    print(f"   批大小：{batch_size}")
    print(f"   批数量：{len(batches)}")
    print(f"   耗时：{batch_time:.3f} 秒")
    print(f"   加速比：{serial_time/batch_time:.2f}x")
```

## ⚠️ 第八部分：错误处理的艺术

### 1. 常见错误类型与处理

```python
"""
错误处理就像实验室的安全规程：
预防为主，处理为辅
"""

def demonstrate_error_handling():
    print("错误处理完全指南")
    print("=" * 60)
    
    # 1. 文件不存在错误
    print("\n1. 处理文件不存在错误：")
    
    def safe_read_file(filename):
        """安全读取文件，带错误处理"""
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"❌ 错误：文件 '{filename}' 不存在")
            print("💡 解决方案：")
            print("   1. 检查文件名是否正确")
            print("   2. 检查文件路径是否正确")
            print("   3. 确认文件确实存在")
            
            # 提供替代方案
            response = input("是否创建新文件？(y/n): ")
            if response.lower() == 'y':
                with open(filename, 'w') as f:
                    f.write("# 新建文件\n")
                print(f"✅ 已创建文件：{filename}")
                return "# 新建文件\n"
            return None
    
    # 测试
    content = safe_read_file("不存在的文件.txt")
    
    # 2. 编码错误
    print("\n2. 处理编码错误：")
    
    def read_with_encoding_detection(filename):
        """自动检测并处理编码"""
        encodings = ['utf-8', 'gbk', 'latin-1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(filename, 'r', encoding=encoding) as f:
                    content = f.read()
                print(f"✅ 成功使用 {encoding} 编码读取")
                return content
            except UnicodeDecodeError:
                continue
        
        # 如果所有编码都失败
        print("❌ 无法确定文件编码")
        print("💡 尝试二进制模式读取...")
        
        with open(filename, 'rb') as f:
            raw_bytes = f.read()
            print(f"读取了 {len(raw_bytes)} 字节的二进制数据")
            return raw_bytes
    
    # 3. 权限错误
    print("\n3. 处理权限错误：")
    
    def write_with_permission_check(filename, content):
        """检查权限并写入文件"""
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"✅ 成功写入：{filename}")
            
        except PermissionError:
            print(f"❌ 错误：没有写入权限 - {filename}")
            print("💡 解决方案：")
            print("   1. 检查文件是否被其他程序占用")
            print("   2. 检查文件夹权限设置")
            print("   3. 尝试使用管理员权限运行")
            
            # 尝试写入临时文件
            import tempfile
            temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
            temp_file.write(content)
            temp_file.close()
            print(f"✅ 已写入临时文件：{temp_file.name}")
            return temp_file.name
            
        return filename
    
    # 4. 内存错误
    print("\n4. 处理内存错误：")
    
    def process_large_file_safely(filename):
        """安全处理大文件"""
        try:
            # 检查文件大小
            file_size = os.path.getsize(filename)
            
            if file_size > 100 * 1024 * 1024:  # 100MB
                print(f"⚠️ 警告：文件较大 ({file_size / 1024 / 1024:.1f} MB)")
                print("使用流式处理避免内存溢出...")
                
                # 流式处理
                line_count = 0
                with open(filename, 'r') as f:
                    for line in f:
                        line_count += 1
                        # 处理每一行
                        if line_count % 10000 == 0:
                            print(f"  已处理 {line_count} 行...")
                
                return line_count
            else:
                # 小文件直接读取
                with open(filename, 'r') as f:
                    content = f.read()
                return len(content.splitlines())
                
        except MemoryError:
            print("❌ 内存错误：文件太大，内存不足")
            print("💡 解决方案：使用生成器或分块处理")
            return None
    
    # 5. 格式错误
    print("\n5. 处理格式错误：")
    
    def parse_fasta_with_validation(filename):
        """带格式验证的FASTA解析"""
        errors = []
        warnings = []
        sequences = []
        
        try:
            with open(filename, 'r') as f:
                current_id = None
                current_seq = []
                line_num = 0
                
                for line in f:
                    line_num += 1
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    if line.startswith('>'):
                        # 保存前一条序列
                        if current_id:
                            seq = ''.join(current_seq)
                            if not seq:
                                warnings.append(f"行 {line_num}: 序列 {current_id} 为空")
                            else:
                                sequences.append((current_id, seq))
                        
                        # 新序列
                        if len(line) == 1:
                            errors.append(f"行 {line_num}: 标题行为空")
                            current_id = f"unnamed_{line_num}"
                        else:
                            current_id = line[1:].split()[0]
                        current_seq = []
                        
                    else:
                        if current_id is None:
                            errors.append(f"行 {line_num}: 序列出现在标题之前")
                        else:
                            # 验证序列字符
                            valid_chars = set('ATCGUN')
                            invalid = set(line.upper()) - valid_chars
                            if invalid:
                                warnings.append(f"行 {line_num}: 包含非标准字符 {invalid}")
                            current_seq.append(line)
                
                # 保存最后一条
                if current_id:
                    seq = ''.join(current_seq)
                    if seq:
                        sequences.append((current_id, seq))
            
            # 报告结果
            print(f"\n解析完成：")
            print(f"  ✅ 成功解析 {len(sequences)} 条序列")
            
            if errors:
                print(f"  ❌ 发现 {len(errors)} 个错误：")
                for error in errors[:3]:  # 只显示前3个
                    print(f"     - {error}")
            
            if warnings:
                print(f"  ⚠️ 发现 {len(warnings)} 个警告：")
                for warning in warnings[:3]:  # 只显示前3个
                    print(f"     - {warning}")
            
            return sequences
            
        except Exception as e:
            print(f"❌ 解析失败：{e}")
            return []
```

### 2. 自定义错误类

```python
"""
自定义错误类就像特定的实验异常：
让错误信息更准确、更有帮助
"""

class FastaError(Exception):
    """FASTA相关错误的基类"""
    pass

class FastaFormatError(FastaError):
    """FASTA格式错误"""
    def __init__(self, message, line_number=None):
        self.line_number = line_number
        if line_number:
            message = f"行 {line_number}: {message}"
        super().__init__(message)

class SequenceError(FastaError):
    """序列内容错误"""
    def __init__(self, seq_id, message):
        self.seq_id = seq_id
        super().__init__(f"序列 {seq_id}: {message}")

class FastaIOError(FastaError):
    """文件IO错误"""
    pass

def use_custom_errors():
    print("\n自定义错误类演示")
    print("=" * 60)
    
    def strict_fasta_parser(filename):
        """严格的FASTA解析器，使用自定义错误"""
        
        if not os.path.exists(filename):
            raise FastaIOError(f"文件不存在：{filename}")
        
        with open(filename, 'r') as f:
            line_num = 0
            current_id = None
            
            for line in f:
                line_num += 1
                line = line.strip()
                
                if not line:
                    continue
                
                if line.startswith('>'):
                    if len(line) == 1:
                        raise FastaFormatError("标题行不能为空", line_num)
                    
                    current_id = line[1:].split()[0]
                    
                    if not current_id:
                        raise FastaFormatError("无法解析序列ID", line_num)
                    
                else:
                    if current_id is None:
                        raise FastaFormatError("序列出现在标题之前", line_num)
                    
                    # 检查序列内容
                    invalid = set(line.upper()) - set('ATCGUN')
                    if invalid:
                        raise SequenceError(current_id, f"包含无效字符：{invalid}")
    
    # 测试自定义错误
    test_cases = [
        ("", "空标题"),
        (">", "只有>"),
        ("ATCG\n>seq1", "序列在标题前"),
        (">seq1\nAT#CG", "无效字符")
    ]
    
    for content, description in test_cases:
        print(f"\n测试：{description}")
        
        with open("error_test.fasta", "w") as f:
            f.write(content)
        
        try:
            strict_fasta_parser("error_test.fasta")
            print("✅ 通过验证")
        except FastaFormatError as e:
            print(f"❌ 格式错误：{e}")
        except SequenceError as e:
            print(f"❌ 序列错误：{e}")
        except FastaIOError as e:
            print(f"❌ IO错误：{e}")
        finally:
            if os.path.exists("error_test.fasta"):
                os.remove("error_test.fasta")
```

## 🎯 第九部分：综合项目 - 构建完整的序列分析流程

### 项目：基因组序列分析系统

```python
"""
综合项目：构建一个完整的基因组序列分析系统
包含：文件管理、序列分析、质量控制、报告生成
"""

class GenomeAnalysisSystem:
    """
    基因组分析系统
    一个完整的、生产级别的序列分析工具
    """
    
    def __init__(self, project_name):
        self.project_name = project_name
        self.project_dir = f"analysis_{project_name}"
        self.statistics = {}
        self._setup_project()
    
    def _setup_project(self):
        """设置项目目录结构"""
        import os
        
        # 创建项目目录
        dirs = [
            self.project_dir,
            f"{self.project_dir}/data",
            f"{self.project_dir}/results",
            f"{self.project_dir}/logs",
            f"{self.project_dir}/reports"
        ]
        
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
        
        print(f"✅ 项目 '{self.project_name}' 初始化完成")
        print(f"   项目目录：{self.project_dir}")
    
    def import_sequences(self, fasta_file):
        """导入序列文件"""
        import shutil
        
        if not os.path.exists(fasta_file):
            raise FileNotFoundError(f"文件不存在：{fasta_file}")
        
        # 复制到项目目录
        dest = f"{self.project_dir}/data/input.fasta"
        shutil.copy(fasta_file, dest)
        
        # 验证文件
        self._validate_fasta(dest)
        
        print(f"✅ 序列文件已导入：{dest}")
        return dest
    
    def _validate_fasta(self, filename):
        """验证FASTA文件格式"""
        seq_count = 0
        total_length = 0
        
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('>'):
                    seq_count += 1
                else:
                    total_length += len(line.strip())
        
        if seq_count == 0:
            raise ValueError("文件中没有找到序列")
        
        self.statistics['input_sequences'] = seq_count
        self.statistics['input_total_length'] = total_length
        
        print(f"   验证通过：{seq_count} 条序列，总长度 {total_length} bp")
    
    def quality_control(self, min_length=100, max_n_percent=5):
        """质量控制：过滤低质量序列"""
        input_file = f"{self.project_dir}/data/input.fasta"
        output_file = f"{self.project_dir}/data/filtered.fasta"
        
        kept = 0
        filtered = 0
        
        with open(output_file, 'w') as out_f:
            current_header = None
            current_seq = []
            
            with open(input_file, 'r') as in_f:
                for line in in_f:
                    line = line.strip()
                    
                    if line.startswith('>'):
                        # 处理前一条序列
                        if current_header:
                            seq = ''.join(current_seq).upper()
                            
                            # 质量检查
                            if (len(seq) >= min_length and 
                                seq.count('N') <= len(seq) * max_n_percent / 100):
                                out_f.write(f">{current_header}\n")
                                out_f.write(f"{seq}\n")
                                kept += 1
                            else:
                                filtered += 1
                        
                        current_header = line[1:]
                        current_seq = []
                    else:
                        current_seq.append(line)
                
                # 最后一条
                if current_header:
                    seq = ''.join(current_seq).upper()
                    if (len(seq) >= min_length and 
                        seq.count('N') <= len(seq) * max_n_percent / 100):
                        out_f.write(f">{current_header}\n")
                        out_f.write(f"{seq}\n")
                        kept += 1
                    else:
                        filtered += 1
        
        self.statistics['kept_sequences'] = kept
        self.statistics['filtered_sequences'] = filtered
        
        print(f"✅ 质量控制完成")
        print(f"   保留：{kept} 条序列")
        print(f"   过滤：{filtered} 条序列")
        
        return output_file
    
    def analyze_sequences(self):
        """分析序列特征"""
        input_file = f"{self.project_dir}/data/filtered.fasta"
        
        results = {
            'sequences': [],
            'total_length': 0,
            'gc_content_overall': 0,
            'length_distribution': []
        }
        
        total_gc = 0
        total_bases = 0
        
        with open(input_file, 'r') as f:
            current_id = None
            current_seq = []
            
            for line in f:
                line = line.strip()
                
                if line.startswith('>'):
                    if current_id:
                        seq = ''.join(current_seq).upper()
                        length = len(seq)
                        gc = seq.count('G') + seq.count('C')
                        gc_percent = (gc / length * 100) if length > 0 else 0
                        
                        results['sequences'].append({
                            'id': current_id,
                            'length': length,
                            'gc_content': gc_percent
                        })
                        
                        results['length_distribution'].append(length)
                        total_gc += gc
                        total_bases += length
                    
                    current_id = line[1:].split()[0]
                    current_seq = []
                else:
                    current_seq.append(line)
            
            # 最后一条
            if current_id:
                seq = ''.join(current_seq).upper()
                length = len(seq)
                gc = seq.count('G') + seq.count('C')
                gc_percent = (gc / length * 100) if length > 0 else 0
                
                results['sequences'].append({
                    'id': current_id,
                    'length': length,
                    'gc_content': gc_percent
                })
                
                results['length_distribution'].append(length)
                total_gc += gc
                total_bases += length
        
        # 计算总体统计
        results['total_length'] = total_bases
        results['gc_content_overall'] = (total_gc / total_bases * 100) if total_bases > 0 else 0
        
        self.statistics['analysis_results'] = results
        
        print(f"✅ 序列分析完成")
        print(f"   总长度：{total_bases:,} bp")
        print(f"   整体GC含量：{results['gc_content_overall']:.1f}%")
        
        return results
    
    def generate_report(self):
        """生成分析报告"""
        from datetime import datetime
        
        report_file = f"{self.project_dir}/reports/analysis_report.txt"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            # 报告头
            f.write("=" * 60 + "\n")
            f.write("基因组序列分析报告\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"项目名称：{self.project_name}\n")
            f.write(f"分析日期：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n")
            
            # 输入数据统计
            f.write("输入数据统计\n")
            f.write("-" * 40 + "\n")
            f.write(f"原始序列数：{self.statistics.get('input_sequences', 0)}\n")
            f.write(f"原始总长度：{self.statistics.get('input_total_length', 0):,} bp\n")
            f.write("\n")
            
            # 质量控制结果
            f.write("质量控制结果\n")
            f.write("-" * 40 + "\n")
            f.write(f"保留序列数：{self.statistics.get('kept_sequences', 0)}\n")
            f.write(f"过滤序列数：{self.statistics.get('filtered_sequences', 0)}\n")
            filter_rate = (self.statistics.get('filtered_sequences', 0) / 
                          self.statistics.get('input_sequences', 1) * 100)
            f.write(f"过滤率：{filter_rate:.1f}%\n")
            f.write("\n")
            
            # 序列分析结果
            if 'analysis_results' in self.statistics:
                results = self.statistics['analysis_results']
                
                f.write("序列特征分析\n")
                f.write("-" * 40 + "\n")
                f.write(f"分析序列数：{len(results['sequences'])}\n")
                f.write(f"总长度：{results['total_length']:,} bp\n")
                f.write(f"平均长度：{results['total_length'] / len(results['sequences']):.1f} bp\n")
                f.write(f"最短序列：{min(results['length_distribution'])} bp\n")
                f.write(f"最长序列：{max(results['length_distribution'])} bp\n")
                f.write(f"整体GC含量：{results['gc_content_overall']:.2f}%\n")
                f.write("\n")
                
                # 详细序列列表
                f.write("序列详情（前10条）\n")
                f.write("-" * 40 + "\n")
                f.write(f"{'序列ID':<20} {'长度(bp)':<10} {'GC含量(%)':<10}\n")
                f.write("-" * 40 + "\n")
                
                for seq in results['sequences'][:10]:
                    f.write(f"{seq['id']:<20} {seq['length']:<10} {seq['gc_content']:<10.1f}\n")
                
                if len(results['sequences']) > 10:
                    f.write(f"... 还有 {len(results['sequences']) - 10} 条序列\n")
            
            f.write("\n" + "=" * 60 + "\n")
            f.write("报告结束\n")
        
        print(f"✅ 报告已生成：{report_file}")
        
        # 同时生成CSV格式
        csv_file = f"{self.project_dir}/reports/sequences.csv"
        with open(csv_file, 'w') as f:
            f.write("ID,Length,GC_Content\n")
            if 'analysis_results' in self.statistics:
                for seq in self.statistics['analysis_results']['sequences']:
                    f.write(f"{seq['id']},{seq['length']},{seq['gc_content']:.2f}\n")
        
        print(f"✅ CSV数据已生成：{csv_file}")
        
        return report_file

# 使用示例
def run_analysis_project():
    print("🧬 运行基因组分析项目")
    print("=" * 60)
    
    # 创建测试数据
    test_fasta = """>chr1_gene1
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
>chr1_gene2_short
ATCG
>chr1_gene3_with_N
ATCGATCGATCNNNNNGATCGATCGATCGATCGATCGATCGATCGATCG
>chr2_gene1
GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC
GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC
>chr2_gene2
ATATATATATATATATATATATATATATATATATATATATATATATAT
ATATATATATATATATATATATATATATATATATATATATATATATAT
"""
    
    with open("test_genome.fasta", "w") as f:
        f.write(test_fasta)
    
    # 创建分析系统
    system = GenomeAnalysisSystem("COVID19_Variants")
    
    try:
        # 步骤1：导入数据
        print("\n步骤1：导入序列数据")
        system.import_sequences("test_genome.fasta")
        
        # 步骤2：质量控制
        print("\n步骤2：质量控制")
        system.quality_control(min_length=50, max_n_percent=5)
        
        # 步骤3：序列分析
        print("\n步骤3：序列分析")
        system.analyze_sequences()
        
        # 步骤4：生成报告
        print("\n步骤4：生成报告")
        report = system.generate_report()
        
        # 显示报告内容
        print("\n" + "=" * 60)
        print("报告预览：")
        with open(report, 'r') as f:
            lines = f.readlines()[:20]  # 显示前20行
            for line in lines:
                print(line.rstrip())
        print("...")
        
    finally:
        # 清理测试文件
        if os.path.exists("test_genome.fasta"):
            os.remove("test_genome.fasta")
        
        # 可选：清理项目目录
        # import shutil
        # if os.path.exists(system.project_dir):
        #     shutil.rmtree(system.project_dir)

# 运行项目
# run_analysis_project()
```

## 💪 练习题预览

本章配套了丰富的练习题，从简单到复杂，帮助你巩固所学：

### 初级练习（建立信心）⭐
1. **基础文件操作** - PCR实验数据记录
2. **简单FASTA解析** - 提取序列信息

### 中级练习（实际应用）⭐⭐
3. **序列质量控制** - 过滤低质量序列
4. **批量文件处理** - 分析多个样本

### 高级练习（研究级别）⭐⭐⭐
5. **格式转换器** - FASTA到其他格式
6. **大基因组处理** - 内存优化技术

### 挑战题目 ⭐⭐⭐⭐
7. **序列数据库系统** - 构建索引和检索系统

## 📊 本章总结

### 核心知识点回顾

1. **文件操作本质**
   - 文件 = 持久化存储的数据
   - 文件系统 = 数据的组织结构
   - 路径 = 文件的地址

2. **文件操作三要素**
   - 打开（open）- 建立连接
   - 操作（read/write）- 数据交互
   - 关闭（close）- 释放资源

3. **FASTA格式精髓**
   - 简单性：文本格式，易读易写
   - 通用性：生物信息学标准
   - 灵活性：适应各种序列类型

4. **大文件处理策略**
   - 逐行读取 vs 一次性读取
   - 生成器的威力
   - 并行处理加速

5. **错误处理原则**
   - 预期常见错误
   - 提供有用信息
   - 优雅地失败

### 最佳实践清单

✅ **始终使用with语句管理文件**
```python
with open(filename, 'r') as f:
    # 文件会自动关闭
```

✅ **指定文件编码**
```python
with open(filename, 'r', encoding='utf-8') as f:
    # 避免编码问题
```

✅ **验证文件存在性**
```python
if os.path.exists(filename):
    # 安全操作
```

✅ **使用生成器处理大文件**
```python
def read_sequences():
    yield sequence  # 不是return
```

✅ **完整的错误处理**
```python
try:
    # 尝试操作
except SpecificError:
    # 处理特定错误
```

### 进阶学习路径

1. **深入学习Python标准库**
   - pathlib：现代路径操作
   - tempfile：临时文件处理
   - shutil：高级文件操作

2. **探索生物信息学库**
   - BioPython：专业的生物序列处理
   - pandas：表格数据处理
   - numpy：数值计算

3. **性能优化技术**
   - 多进程/多线程
   - 异步IO
   - 内存映射文件

## 🎯 关键要点

记住这三个核心概念，你就掌握了文件IO的精髓：

1. **文件是你的数字实验记录本** - 用来永久保存数据
2. **FASTA是序列的通用语言** - 简单、标准、通用
3. **生成器是处理大数据的秘密武器** - 省内存、够优雅

## 🚀 下一步

恭喜你完成了文件IO和FASTA处理的学习！你现在已经能够：

- ✅ 自如地读写各种文件
- ✅ 专业地解析FASTA格式
- ✅ 优雅地处理大型基因组文件
- ✅ 稳健地处理各种错误情况

下一章（Chapter 06），我们将学习**Pandas数据分析**——用Python处理表格数据的终极武器。你将学会像使用Excel一样轻松处理复杂的生物数据表格，但功能要强大100倍！

想象一下：
- 一行代码读取包含10万个基因表达数据的CSV文件
- 瞬间计算所有样本的统计信息
- 优雅地合并多个实验数据表
- 生成专业的数据可视化图表

准备好了吗？让我们继续这段激动人心的数据科学之旅！

---

*"In biology, nothing makes sense except in the light of data."*  
*"在生物学中，没有数据的支撑，一切都没有意义。"*

祝学习愉快！🧬💻📊