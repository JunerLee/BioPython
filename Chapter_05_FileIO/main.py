#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 05: 文件IO与FASTA处理 - 你的数字实验记录本

生物学问题：如何读取、解析和处理序列数据文件？

编程概念：文件IO就像实验记录本
- open() = 打开记录本
- read() = 阅读记录
- write() = 记录数据
- close() = 合上记录本

本章重点：从简单到复杂，逐步构建专业的FASTA解析器
"""

import os
import time


def demonstrate_file_as_notebook():
    """
    演示1：文件操作就像使用实验记录本
    """
    print("📔 演示1：文件就是你的数字实验记录本")
    print("=" * 60)
    
    # 创建实验数据
    pcr_results = """
实验日期：2024-01-15
实验类型：PCR扩增
引物：Forward: ATCGATCGATCG, Reverse: GCTAGCTAGCTA
    
PCR产物序列：
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
TTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCCGGGG
    """
    
    # 1. 写入实验记录（创建新记录本）
    print("\n1️⃣ 记录新实验数据...")
    with open("pcr_results.txt", "w", encoding="utf-8") as notebook:
        notebook.write(pcr_results)
        print("   ✓ 数据已保存到 pcr_results.txt")
    
    # 2. 读取实验记录（翻开记录本）
    print("\n2️⃣ 查看之前的实验记录...")
    with open("pcr_results.txt", "r", encoding="utf-8") as notebook:
        content = notebook.read()
        print("   记录内容：")
        print("   " + "-" * 40)
        for line in content.split("\n")[:5]:  # 显示前5行
            print(f"   {line}")
    
    # 3. 追加新数据（在原记录后补充）
    print("\n3️⃣ 追加今天的实验结果...")
    new_result = "\n补充：序列已验证，质量良好\n"
    with open("pcr_results.txt", "a", encoding="utf-8") as notebook:
        notebook.write(new_result)
        print("   ✓ 新结果已追加")
    
    # 清理演示文件
    os.remove("pcr_results.txt")
    print("\n   [演示文件已清理]")


def parse_fasta_v1_simple(filename):
    """
    FASTA解析器 v1：最简单的版本（概念演示）
    
    优点：代码简单，易于理解
    缺点：无法处理多行序列，内存占用大
    """
    print("\n🔬 版本1：简单解析器（初学者版本）")
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # 简单地按'>'分割
    raw_sequences = content.split('>')[1:]  # 跳过第一个空元素
    
    sequences = []
    for raw_seq in raw_sequences:
        lines = raw_seq.strip().split('\n')
        header = lines[0]
        sequence = ''.join(lines[1:])  # 拼接所有序列行
        sequences.append((header, sequence))
    
    return sequences


def parse_fasta_v2_improved(filename):
    """
    FASTA解析器 v2：改进版本（实用版本）
    
    优点：能正确处理多行序列，逐行读取节省内存
    缺点：没有错误处理
    """
    print("\n🔬 版本2：改进解析器（实用版本）")
    
    sequences = []
    current_header = None
    current_sequence = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            if not line:  # 跳过空行
                continue
                
            if line.startswith('>'):
                # 保存前一条序列
                if current_header is not None:
                    sequences.append((current_header, ''.join(current_sequence)))
                
                # 开始新序列
                current_header = line[1:]  # 去掉'>'
                current_sequence = []
            else:
                # 收集序列行
                current_sequence.append(line.upper())
        
        # 保存最后一条序列
        if current_header is not None:
            sequences.append((current_header, ''.join(current_sequence)))
    
    return sequences


def parse_fasta_v3_professional(filename):
    """
    FASTA解析器 v3：专业版本（生产级别）
    
    优点：完整错误处理，使用生成器节省内存，处理各种边界情况
    适用：大文件处理，生产环境
    """
    print("\n🔬 版本3：专业解析器（生产级别）")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            current_id = None
            current_desc = None
            current_seq = []
            
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # 跳过空行和注释行
                if not line or line.startswith('#'):
                    continue
                
                if line.startswith('>'):
                    # 输出前一条序列
                    if current_id is not None:
                        yield {
                            'id': current_id,
                            'description': current_desc,
                            'sequence': ''.join(current_seq),
                            'length': len(''.join(current_seq))
                        }
                    
                    # 解析新的标题行
                    header_parts = line[1:].split(None, 1)
                    current_id = header_parts[0] if header_parts else f"seq_{line_num}"
                    current_desc = header_parts[1] if len(header_parts) > 1 else ""
                    current_seq = []
                    
                else:
                    # 验证序列字符（DNA/RNA/蛋白质）
                    valid_chars = set('ATCGURNKMYSWHBVD')  # IUPAC核苷酸代码
                    cleaned_seq = ''.join(c for c in line.upper() if c in valid_chars)
                    if cleaned_seq:
                        current_seq.append(cleaned_seq)
            
            # 输出最后一条序列
            if current_id is not None:
                yield {
                    'id': current_id,
                    'description': current_desc,
                    'sequence': ''.join(current_seq),
                    'length': len(''.join(current_seq))
                }
                
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{filename}'")
        print("   提示：请检查文件路径是否正确")
    except PermissionError:
        print(f"❌ 错误：没有权限读取文件 '{filename}'")
    except UnicodeDecodeError:
        print(f"❌ 错误：文件编码问题，尝试用其他编码打开")
    except Exception as e:
        print(f"❌ 未知错误：{e}")


def demonstrate_fasta_parsing_evolution():
    """
    演示2：FASTA解析器的渐进式改进
    """
    print("\n\n🧬 演示2：逐步构建FASTA解析器")
    print("=" * 60)
    
    # 创建测试FASTA文件
    fasta_content = """>NM_001126114.2 Homo sapiens tumor protein p53 (TP53), transcript variant 2, mRNA
ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTC
AGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGT

>ENST00000619186.1 Homo sapiens BRCA1 DNA repair associated
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAA
AATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTG

>YP_009724390.1 surface glycoprotein [Severe acute respiratory syndrome coronavirus 2]
MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFS
NVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIV"""
    
    with open("test_sequences.fasta", "w") as f:
        f.write(fasta_content)
    
    print("📄 创建了测试文件：test_sequences.fasta")
    print("   包含3条序列（p53、BRCA1、SARS-CoV-2 spike蛋白）")
    
    # 测试三个版本的解析器
    print("\n" + "=" * 60)
    
    # 版本1：简单解析
    sequences_v1 = parse_fasta_v1_simple("test_sequences.fasta")
    print(f"   解析结果：找到 {len(sequences_v1)} 条序列")
    for header, seq in sequences_v1:
        print(f"   - {header[:30]}... ({len(seq)} bp)")
    
    # 版本2：改进解析
    sequences_v2 = parse_fasta_v2_improved("test_sequences.fasta")
    print(f"   解析结果：找到 {len(sequences_v2)} 条序列")
    for header, seq in sequences_v2:
        gc_content = (seq.count('G') + seq.count('C')) / len(seq) * 100
        print(f"   - {header[:30]}... (GC: {gc_content:.1f}%)")
    
    # 版本3：专业解析（使用生成器）
    print("   解析结果：")
    for seq_record in parse_fasta_v3_professional("test_sequences.fasta"):
        print(f"   - ID: {seq_record['id'][:20]}...")
        print(f"     长度: {seq_record['length']} bp")
        print(f"     描述: {seq_record['description'][:40]}...")
    
    # 清理测试文件
    os.remove("test_sequences.fasta")
    print("\n   [测试文件已清理]")


def demonstrate_large_file_handling():
    """
    演示3：大文件处理技巧
    """
    print("\n\n📊 演示3：大文件处理最佳实践")
    print("=" * 60)
    
    # 模拟创建一个"大"文件
    print("\n1️⃣ 创建模拟基因组文件...")
    with open("large_genome.fasta", "w") as f:
        # 模拟100条染色体序列
        for i in range(1, 101):
            f.write(f">chromosome_{i} Simulated sequence {i}\n")
            # 每条序列1000个碱基（实际会更长）
            import random
            for _ in range(10):  # 分10行写入
                seq = ''.join(random.choices('ATCG', k=100))
                f.write(seq + "\n")
    
    print("   ✓ 创建了包含100条序列的模拟基因组文件")
    
    # 方法1：不推荐 - 一次性读取
    print("\n2️⃣ 对比不同的文件处理方法：")
    
    print("\n   ❌ 方法1：一次性读取（占用大量内存）")
    start_time = time.time()
    with open("large_genome.fasta", "r") as f:
        all_content = f.read()  # 读取整个文件到内存
        line_count = all_content.count('\n')
    print(f"      耗时：{time.time() - start_time:.4f}秒")
    print(f"      行数：{line_count}")
    
    # 方法2：推荐 - 逐行处理
    print("\n   ✅ 方法2：逐行读取（内存友好）")
    start_time = time.time()
    total_length = 0
    sequence_count = 0
    
    with open("large_genome.fasta", "r") as f:
        for line in f:
            if line.startswith('>'):
                sequence_count += 1
            else:
                total_length += len(line.strip())
    
    print(f"      耗时：{time.time() - start_time:.4f}秒")
    print(f"      序列数：{sequence_count}")
    print(f"      总长度：{total_length:,} bp")
    
    # 方法3：使用生成器处理
    print("\n   ✅ 方法3：生成器处理（最优方案）")
    start_time = time.time()
    
    def process_sequences_generator(filename):
        """使用生成器处理序列，极其节省内存"""
        for seq_record in parse_fasta_v3_professional(filename):
            # 这里可以进行各种分析
            yield len(seq_record['sequence'])
    
    # 统计所有序列长度
    lengths = list(process_sequences_generator("large_genome.fasta"))
    print(f"      耗时：{time.time() - start_time:.4f}秒")
    print(f"      平均长度：{sum(lengths)/len(lengths):.1f} bp")
    print(f"      最长序列：{max(lengths)} bp")
    
    # 清理文件
    os.remove("large_genome.fasta")
    print("\n   [模拟文件已清理]")


def demonstrate_error_handling():
    """
    演示4：错误处理最佳实践
    """
    print("\n\n⚠️ 演示4：错误处理 - 让程序更稳健")
    print("=" * 60)
    
    def safe_fasta_reader(filename):
        """带完整错误处理的FASTA读取器"""
        try:
            # 检查文件是否存在
            if not os.path.exists(filename):
                raise FileNotFoundError(f"文件不存在：{filename}")
            
            # 检查文件大小
            file_size = os.path.getsize(filename)
            if file_size == 0:
                raise ValueError("文件为空")
            
            if file_size > 1_000_000_000:  # 1GB
                print(f"⚠️ 警告：文件较大 ({file_size/1_000_000:.1f} MB)")
                response = input("   是否继续？(y/n): ")
                if response.lower() != 'y':
                    return None
            
            # 尝试读取文件
            sequences = []
            with open(filename, 'r', encoding='utf-8') as f:
                # 检查是否为FASTA格式
                first_line = f.readline()
                if not first_line.startswith('>'):
                    raise ValueError("不是有效的FASTA文件（应以'>'开头）")
                
                # 重置文件指针
                f.seek(0)
                
                # 解析序列
                for seq in parse_fasta_v3_professional(filename):
                    sequences.append(seq)
            
            return sequences
            
        except FileNotFoundError as e:
            print(f"❌ 文件错误：{e}")
            print("   解决方案：请检查文件路径是否正确")
            
        except PermissionError:
            print("❌ 权限错误：没有读取文件的权限")
            print("   解决方案：请检查文件权限设置")
            
        except UnicodeDecodeError:
            print("❌ 编码错误：文件可能不是UTF-8编码")
            print("   解决方案：尝试用其他编码打开，如'latin-1'或'gbk'")
            
        except ValueError as e:
            print(f"❌ 格式错误：{e}")
            print("   解决方案：请确认文件是标准FASTA格式")
            
        except MemoryError:
            print("❌ 内存错误：文件太大，内存不足")
            print("   解决方案：使用逐行读取或生成器方式处理")
            
        except Exception as e:
            print(f"❌ 未知错误：{e}")
            print("   解决方案：请联系技术支持")
            
        return None
    
    # 测试各种错误情况
    print("\n测试错误处理：")
    
    print("\n1. 测试不存在的文件：")
    safe_fasta_reader("不存在的文件.fasta")
    
    print("\n2. 测试空文件：")
    with open("empty.fasta", "w") as f:
        pass  # 创建空文件
    safe_fasta_reader("empty.fasta")
    os.remove("empty.fasta")
    
    print("\n3. 测试非FASTA格式文件：")
    with open("not_fasta.txt", "w") as f:
        f.write("This is not a FASTA file\n")
    safe_fasta_reader("not_fasta.txt")
    os.remove("not_fasta.txt")


def main():
    """
    主函数：运行所有演示
    """
    print("🧬 Chapter 05: 文件IO与FASTA处理")
    print("把Python变成你的智能实验记录本")
    print("=" * 60)
    
    # 运行各个演示
    demonstrate_file_as_notebook()
    demonstrate_fasta_parsing_evolution()
    demonstrate_large_file_handling()
    demonstrate_error_handling()
    
    # 学习总结
    print("\n\n" + "=" * 60)
    print("📚 本章核心要点：")
    print()
    print("1. 文件操作三部曲：")
    print("   • open() → read/write() → close()")
    print("   • 使用with语句自动管理文件关闭")
    print()
    print("2. FASTA解析的演进：")
    print("   • v1: 简单分割（学习概念）")
    print("   • v2: 逐行处理（实际应用）")
    print("   • v3: 生成器+错误处理（生产级别）")
    print()
    print("3. 大文件处理技巧：")
    print("   • 避免read()一次性读取")
    print("   • 使用for line in file逐行处理")
    print("   • 生成器yield实现流式处理")
    print()
    print("4. 错误处理最佳实践：")
    print("   • 预期并处理常见错误")
    print("   • 提供有用的错误信息")
    print("   • 给出解决方案建议")
    print()
    print("🎯 关键收获：文件IO是连接程序与真实数据的桥梁！")


if __name__ == "__main__":
    main()