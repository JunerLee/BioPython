#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 05: 文件IO与FASTA处理 - 练习题参考答案

完整的参考实现，包含详细注释和最佳实践
"""

import os
import glob


def practice_1_basic_file_operations():
    """
    练习1参考答案: 基础文件操作 ⭐
    """
    print("=" * 60)
    print("练习1: PCR实验数据记录 ⭐ [参考答案]")
    print("-" * 60)
    
    # 1. 创建并写入PCR结果
    pcr_sequences = [
        "ATCGATCGATCGATCGATCGATCG",
        "GCTAGCTAGCTAGCTAGCTAGCTA",
        "TTTTAAAACCCCGGGGTTTTAAAA"
    ]
    
    # 写入文件
    with open("pcr_results.txt", "w", encoding="utf-8") as f:
        for seq in pcr_sequences:
            f.write(seq + "\n")
    print("✓ PCR结果已保存到 pcr_results.txt")
    
    # 2. 读取并分析序列
    total_length = 0
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    
    with open("pcr_results.txt", "r", encoding="utf-8") as f:
        for line in f:
            sequence = line.strip().upper()
            total_length += len(sequence)
            
            # 统计各碱基数量
            for base in sequence:
                if base in base_counts:
                    base_counts[base] += 1
    
    # 计算GC含量
    gc_count = base_counts['G'] + base_counts['C']
    gc_content = (gc_count / total_length * 100) if total_length > 0 else 0
    
    # 输出结果
    print(f"\n序列分析结果:")
    print(f"  总长度: {total_length} bp")
    print(f"  碱基组成:")
    for base, count in base_counts.items():
        percent = (count / total_length * 100) if total_length > 0 else 0
        print(f"    {base}: {count} ({percent:.1f}%)")
    print(f"  GC含量: {gc_content:.1f}%")
    
    # 清理文件
    os.remove("pcr_results.txt")
    print("\n✓ 临时文件已清理")


def practice_2_simple_fasta_parser():
    """
    练习2参考答案: 简单FASTA解析器 ⭐
    """
    print("\n" + "=" * 60)
    print("练习2: FASTA格式解析 ⭐ [参考答案]")
    print("-" * 60)
    
    # 创建测试文件
    fasta_content = """>gene_001 hypothetical protein
ATGGCTAGCTAGCTAGCTAGCTAGC
GCTAGCTAGCTAGCTAGCTAGCTAG
>gene_002 kinase
ATGAAACCCGGGTTTAAAACCCGGG
>gene_003 transcription factor
ATGATGATGATGATGATGATGATGA
TGATGATGATGATGATGATGATGAT
"""
    
    with open("test.fasta", "w") as f:
        f.write(fasta_content)
    
    def parse_simple_fasta(filename):
        """
        解析FASTA文件 - 简单实现
        """
        sequences = []
        current_id = None
        current_seq = []
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    
                    if not line:  # 跳过空行
                        continue
                    
                    if line.startswith('>'):
                        # 保存前一条序列
                        if current_id is not None:
                            sequences.append((current_id, ''.join(current_seq)))
                        
                        # 开始新序列
                        current_id = line[1:].split()[0]  # 只取ID部分
                        current_seq = []
                    else:
                        # 收集序列
                        current_seq.append(line.upper())
                
                # 保存最后一条序列
                if current_id is not None:
                    sequences.append((current_id, ''.join(current_seq)))
                    
        except FileNotFoundError:
            print(f"错误: 文件 {filename} 不存在")
            return []
        
        return sequences
    
    # 测试解析器
    sequences = parse_simple_fasta("test.fasta")
    print(f"\n✓ 找到 {len(sequences)} 条序列:")
    
    for seq_id, seq in sequences:
        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
        print(f"  {seq_id}: {len(seq)} bp (GC: {gc:.1f}%)")
    
    # 清理文件
    os.remove("test.fasta")


def practice_3_fasta_quality_control():
    """
    练习3参考答案: FASTA质量控制 ⭐⭐
    """
    print("\n" + "=" * 60)
    print("练习3: 序列质量控制 ⭐⭐ [参考答案]")
    print("-" * 60)
    
    # 创建测试文件
    raw_fasta = """>seq_001 good quality
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
>seq_002 too short
ATCG
>seq_003 contains N
ATCGATCGATCNNNNNGATCGATCGATCGATCGATCGATCGATCGATCG
>seq_004 good quality
TTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCCGGGG
AAAATTTTCCCCGGGGAAAATTTTCCCCGGGGAAAATTTTCCCCGGGG
>seq_005 low complexity
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
"""
    
    with open("raw_sequences.fasta", "w") as f:
        f.write(raw_fasta)
    
    def filter_sequences(input_file, output_file, min_length=50, max_n_percent=5):
        """
        过滤低质量序列 - 完整实现
        """
        kept_count = 0
        filtered_count = 0
        
        with open(output_file, 'w') as out_f:
            current_header = None
            current_seq = []
            
            with open(input_file, 'r') as in_f:
                for line in in_f:
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    if line.startswith('>'):
                        # 处理前一条序列
                        if current_header:
                            sequence = ''.join(current_seq).upper()
                            
                            # 质量检查
                            passed = True
                            reason = ""
                            
                            # 检查长度
                            if len(sequence) < min_length:
                                passed = False
                                reason = f"太短 ({len(sequence)} < {min_length})"
                            
                            # 检查N含量
                            elif sequence.count('N') > len(sequence) * max_n_percent / 100:
                                passed = False
                                n_percent = sequence.count('N') / len(sequence) * 100
                                reason = f"N含量过高 ({n_percent:.1f}%)"
                            
                            # 检查复杂度
                            else:
                                for base in 'ATCG':
                                    if sequence.count(base) > len(sequence) * 0.8:
                                        passed = False
                                        reason = f"低复杂度 ({base}占比>80%)"
                                        break
                            
                            # 输出结果
                            if passed:
                                out_f.write(f">{current_header}\n")
                                # 每60个字符换行（标准FASTA格式）
                                for i in range(0, len(sequence), 60):
                                    out_f.write(sequence[i:i+60] + "\n")
                                kept_count += 1
                            else:
                                filtered_count += 1
                                print(f"  过滤: {current_header.split()[0]} - {reason}")
                        
                        # 开始新序列
                        current_header = line[1:]
                        current_seq = []
                    else:
                        current_seq.append(line)
                
                # 处理最后一条序列
                if current_header:
                    sequence = ''.join(current_seq).upper()
                    
                    passed = True
                    if len(sequence) < min_length:
                        passed = False
                    elif sequence.count('N') > len(sequence) * max_n_percent / 100:
                        passed = False
                    else:
                        for base in 'ATCG':
                            if sequence.count(base) > len(sequence) * 0.8:
                                passed = False
                                break
                    
                    if passed:
                        out_f.write(f">{current_header}\n")
                        for i in range(0, len(sequence), 60):
                            out_f.write(sequence[i:i+60] + "\n")
                        kept_count += 1
                    else:
                        filtered_count += 1
        
        return kept_count, filtered_count
    
    # 执行质量控制
    kept, filtered = filter_sequences("raw_sequences.fasta", "clean.fasta")
    print(f"\n质量控制结果:")
    print(f"  ✓ 保留: {kept} 条高质量序列")
    print(f"  ✗ 过滤: {filtered} 条低质量序列")
    
    # 清理文件
    os.remove("raw_sequences.fasta")
    if os.path.exists("clean.fasta"):
        os.remove("clean.fasta")


def practice_4_batch_processing():
    """
    练习4参考答案: 批量文件处理 ⭐⭐
    """
    print("\n" + "=" * 60)
    print("练习4: 批量序列分析 ⭐⭐ [参考答案]")
    print("-" * 60)
    
    # 创建测试文件
    samples = {
        "sample_A.fasta": """>geneA1
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
>geneA2
GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC
""",
        "sample_B.fasta": """>geneB1
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
>geneB2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
>geneB3
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
""",
        "sample_C.fasta": """>geneC1
ATATATATATATATATATATATATATATATATATATATATATATATAT
"""
    }
    
    for filename, content in samples.items():
        with open(filename, "w") as f:
            f.write(content)
    
    def batch_analyze_fasta(file_pattern="*.fasta"):
        """
        批量分析FASTA文件 - 完整实现
        """
        results = {}
        
        # 获取所有匹配的文件
        files = glob.glob(file_pattern)
        
        for filepath in files:
            filename = os.path.basename(filepath)
            
            # 初始化统计
            seq_count = 0
            total_length = 0
            gc_count = 0
            
            # 解析文件
            with open(filepath, 'r') as f:
                current_seq = []
                
                for line in f:
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    if line.startswith('>'):
                        # 处理前一条序列
                        if current_seq:
                            sequence = ''.join(current_seq).upper()
                            seq_count += 1
                            total_length += len(sequence)
                            gc_count += sequence.count('G') + sequence.count('C')
                        
                        current_seq = []
                    else:
                        current_seq.append(line)
                
                # 处理最后一条序列
                if current_seq:
                    sequence = ''.join(current_seq).upper()
                    seq_count += 1
                    total_length += len(sequence)
                    gc_count += sequence.count('G') + sequence.count('C')
            
            # 计算统计信息
            results[filename] = {
                'count': seq_count,
                'total_length': total_length,
                'avg_length': total_length / seq_count if seq_count > 0 else 0,
                'gc_content': (gc_count / total_length * 100) if total_length > 0 else 0
            }
        
        return results
    
    # 执行批量分析
    stats = batch_analyze_fasta("sample_*.fasta")
    
    print(f"\n批量分析结果 ({len(stats)} 个文件):")
    for filename, stat in sorted(stats.items()):
        print(f"\n{filename}:")
        print(f"  序列数: {stat['count']}")
        print(f"  总长度: {stat['total_length']} bp")
        print(f"  平均长度: {stat['avg_length']:.1f} bp")
        print(f"  GC含量: {stat['gc_content']:.1f}%")
    
    # 清理文件
    for filename in samples.keys():
        os.remove(filename)


def practice_5_format_converter():
    """
    练习5参考答案: 格式转换器 ⭐⭐⭐
    """
    print("\n" + "=" * 60)
    print("练习5: 序列格式转换 ⭐⭐⭐ [参考答案]")
    print("-" * 60)
    
    # 创建测试FASTA文件
    test_fasta = """>seq1 test sequence 1
ATCGATCGATCGATCGATCGATCG
>seq2 test sequence 2
GCTAGCTAGCTAGCTAGCTAGCTA
>seq3 test sequence 3
TTTTAAAACCCCGGGGTTTTAAAA
"""
    
    with open("test.fasta", "w") as f:
        f.write(test_fasta)
    
    def fasta_to_tabular(input_file, output_file):
        """
        FASTA转表格格式 - 完整实现
        """
        with open(output_file, 'w') as out_f:
            # 写入表头
            out_f.write("序列ID\t长度\tGC%\t序列\n")
            
            # 解析FASTA
            current_id = None
            current_seq = []
            
            with open(input_file, 'r') as in_f:
                for line in in_f:
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    if line.startswith('>'):
                        # 输出前一条序列
                        if current_id:
                            sequence = ''.join(current_seq).upper()
                            length = len(sequence)
                            gc = (sequence.count('G') + sequence.count('C')) / length * 100
                            
                            # 如果序列太长，截断显示
                            display_seq = sequence if length <= 50 else sequence[:47] + "..."
                            
                            out_f.write(f"{current_id}\t{length}\t{gc:.1f}\t{display_seq}\n")
                        
                        # 新序列
                        current_id = line[1:].split()[0]
                        current_seq = []
                    else:
                        current_seq.append(line)
                
                # 输出最后一条
                if current_id:
                    sequence = ''.join(current_seq).upper()
                    length = len(sequence)
                    gc = (sequence.count('G') + sequence.count('C')) / length * 100
                    display_seq = sequence if length <= 50 else sequence[:47] + "..."
                    out_f.write(f"{current_id}\t{length}\t{gc:.1f}\t{display_seq}\n")
    
    def fasta_to_phylip(input_file, output_file):
        """
        FASTA转PHYLIP格式 - 完整实现
        """
        # 首先读取所有序列
        sequences = []
        current_id = None
        current_seq = []
        
        with open(input_file, 'r') as f:
            for line in f:
                line = line.strip()
                
                if not line:
                    continue
                
                if line.startswith('>'):
                    if current_id:
                        sequences.append((current_id, ''.join(current_seq).upper()))
                    
                    current_id = line[1:].split()[0][:10]  # PHYLIP限制10字符
                    current_seq = []
                else:
                    current_seq.append(line)
            
            if current_id:
                sequences.append((current_id, ''.join(current_seq).upper()))
        
        # 写入PHYLIP格式
        if sequences:
            with open(output_file, 'w') as f:
                # 第一行：序列数和长度
                seq_length = len(sequences[0][1])  # 假设所有序列等长
                f.write(f" {len(sequences)} {seq_length}\n")
                
                # 写入序列
                for seq_id, sequence in sequences:
                    # 确保ID为10个字符（右填充空格）
                    formatted_id = seq_id.ljust(10)
                    f.write(f"{formatted_id}{sequence}\n")
    
    # 执行转换
    print("\n格式转换演示:")
    
    # 转换为表格格式
    fasta_to_tabular("test.fasta", "test.tsv")
    print("\n1. FASTA → 表格格式 (test.tsv):")
    with open("test.tsv", "r") as f:
        for line in f:
            print(f"   {line.strip()}")
    
    # 转换为PHYLIP格式
    fasta_to_phylip("test.fasta", "test.phy")
    print("\n2. FASTA → PHYLIP格式 (test.phy):")
    with open("test.phy", "r") as f:
        for line in f:
            print(f"   {line.strip()}")
    
    # 清理文件
    for filename in ["test.fasta", "test.tsv", "test.phy"]:
        if os.path.exists(filename):
            os.remove(filename)


def practice_6_large_genome_processor():
    """
    练习6参考答案: 大基因组处理 ⭐⭐⭐
    """
    print("\n" + "=" * 60)
    print("练习6: 大基因组文件处理 ⭐⭐⭐ [参考答案]")
    print("-" * 60)
    
    # 创建模拟大文件
    with open("genome.fasta", "w") as f:
        for i in range(1, 11):  # 10条染色体
            f.write(f">chr{i} Chromosome {i}\n")
            # 每条染色体1000bp（实际会是百万级别）
            import random
            for _ in range(10):
                seq = ''.join(random.choices('ATCG', k=100))
                f.write(seq + "\n")
    
    def process_large_genome(filename, chunk_size=1000000):
        """
        大基因组处理器 - 使用生成器
        """
        with open(filename, 'r') as f:
            current_chr = None
            current_seq = []
            position = 0
            
            for line in f:
                line = line.strip()
                
                if not line:
                    continue
                
                if line.startswith('>'):
                    # 处理前一条染色体
                    if current_chr:
                        sequence = ''.join(current_seq)
                        length = len(sequence)
                        gc = sequence.count('G') + sequence.count('C')
                        gc_content = (gc / length * 100) if length > 0 else 0
                        
                        yield {
                            'chromosome': current_chr,
                            'length': length,
                            'gc_content': gc_content,
                            'position': position
                        }
                    
                    # 新染色体
                    current_chr = line[1:].split()[0]
                    current_seq = []
                    position = f.tell()  # 记录文件位置
                else:
                    current_seq.append(line.upper())
            
            # 处理最后一条
            if current_chr:
                sequence = ''.join(current_seq)
                length = len(sequence)
                gc = sequence.count('G') + sequence.count('C')
                gc_content = (gc / length * 100) if length > 0 else 0
                
                yield {
                    'chromosome': current_chr,
                    'length': length,
                    'gc_content': gc_content,
                    'position': position
                }
    
    # 使用生成器处理
    print("\n使用生成器处理大基因组:")
    print("(内存友好，适合处理GB级文件)")
    
    total_length = 0
    longest_chr = None
    longest_length = 0
    
    for chr_info in process_large_genome("genome.fasta"):
        print(f"  {chr_info['chromosome']}: "
              f"{chr_info['length']} bp, "
              f"GC: {chr_info['gc_content']:.1f}%")
        
        total_length += chr_info['length']
        
        if chr_info['length'] > longest_length:
            longest_length = chr_info['length']
            longest_chr = chr_info['chromosome']
    
    print(f"\n统计信息:")
    print(f"  总长度: {total_length:,} bp")
    print(f"  最长染色体: {longest_chr} ({longest_length} bp)")
    
    # 清理文件
    os.remove("genome.fasta")


def challenge_fasta_database():
    """
    挑战题参考答案: 构建序列数据库 ⭐⭐⭐⭐
    """
    print("\n" + "=" * 60)
    print("挑战题: 序列数据库系统 ⭐⭐⭐⭐ [参考答案]")
    print("-" * 60)
    
    # 创建测试数据库文件
    db_content = """>NM_001 p53 tumor suppressor
ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTC
>NM_002 BRCA1 breast cancer gene
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAA
>NM_003 EGFR epidermal growth factor receptor
MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNKC
>NM_004 insulin hormone
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKT
"""
    
    with open("sequence_db.fasta", "w") as f:
        f.write(db_content)
    
    class FastaDatabase:
        """
        高效的FASTA数据库实现
        """
        
        def __init__(self, fasta_file):
            """初始化数据库"""
            self.filename = fasta_file
            self.index = {}  # {seq_id: (file_position, length, description)}
            self._stats = None
            self.build_index()
        
        def build_index(self):
            """建立索引 - 不加载序列到内存"""
            with open(self.filename, 'r') as f:
                current_id = None
                current_pos = 0
                current_desc = ""
                seq_start = 0
                seq_length = 0
                
                while True:
                    position = f.tell()
                    line = f.readline()
                    
                    if not line:  # 文件结束
                        if current_id:
                            self.index[current_id] = (seq_start, seq_length, current_desc)
                        break
                    
                    line = line.strip()
                    
                    if line.startswith('>'):
                        # 保存前一条序列信息
                        if current_id:
                            self.index[current_id] = (seq_start, seq_length, current_desc)
                        
                        # 新序列
                        parts = line[1:].split(None, 1)
                        current_id = parts[0]
                        current_desc = parts[1] if len(parts) > 1 else ""
                        seq_start = f.tell()  # 序列开始位置
                        seq_length = 0
                    elif line and current_id:
                        seq_length += len(line)
        
        def get_sequence(self, seq_id):
            """快速获取指定序列"""
            if seq_id not in self.index:
                return None
            
            pos, length, desc = self.index[seq_id]
            
            with open(self.filename, 'r') as f:
                f.seek(pos)  # 直接跳到序列位置
                
                sequence = []
                read_length = 0
                
                while read_length < length:
                    line = f.readline().strip()
                    if line and not line.startswith('>'):
                        sequence.append(line)
                        read_length += len(line)
                
                return {
                    'id': seq_id,
                    'description': desc,
                    'sequence': ''.join(sequence)
                }
        
        def search(self, keyword):
            """搜索序列（按ID或描述）"""
            results = []
            
            for seq_id, (pos, length, desc) in self.index.items():
                if keyword.lower() in seq_id.lower() or keyword.lower() in desc.lower():
                    results.append({
                        'id': seq_id,
                        'description': desc,
                        'length': length
                    })
            
            return results
        
        def statistics(self):
            """返回数据库统计信息（带缓存）"""
            if self._stats is None:
                total_sequences = len(self.index)
                total_length = sum(info[1] for info in self.index.values())
                
                self._stats = {
                    'sequences': total_sequences,
                    'total_length': total_length,
                    'average_length': total_length / total_sequences if total_sequences > 0 else 0,
                    'sequence_ids': list(self.index.keys())
                }
            
            return self._stats
    
    # 测试数据库
    print("\n构建序列数据库...")
    db = FastaDatabase("sequence_db.fasta")
    
    # 显示统计信息
    stats = db.statistics()
    print(f"\n数据库统计:")
    print(f"  序列数: {stats['sequences']}")
    print(f"  总长度: {stats['total_length']} bp")
    print(f"  平均长度: {stats['average_length']:.1f} bp")
    
    # 测试快速检索
    print(f"\n快速检索测试:")
    seq = db.get_sequence("NM_002")
    if seq:
        print(f"  找到: {seq['id']} - {seq['description']}")
        print(f"  序列: {seq['sequence'][:50]}...")
    
    # 测试搜索功能
    print(f"\n搜索 'cancer':")
    results = db.search("cancer")
    for result in results:
        print(f"  {result['id']}: {result['description']} ({result['length']} bp)")
    
    # 清理文件
    os.remove("sequence_db.fasta")


def main():
    """
    主函数：运行所有参考答案
    """
    print("🧬 Chapter 05: 文件IO与FASTA处理 - 参考答案")
    print("=" * 60)
    print()
    
    # 运行所有练习的参考答案
    practice_1_basic_file_operations()
    practice_2_simple_fasta_parser()
    practice_3_fasta_quality_control()
    practice_4_batch_processing()
    practice_5_format_converter()
    practice_6_large_genome_processor()
    challenge_fasta_database()
    
    print("\n" + "=" * 60)
    print("📚 学习要点总结:")
    print()
    print("1. 文件操作基础:")
    print("   • 始终使用with语句确保文件关闭")
    print("   • 指定编码避免乱码问题")
    print("   • 处理异常情况")
    print()
    print("2. FASTA解析技巧:")
    print("   • 逐行读取节省内存")
    print("   • 正确处理多行序列")
    print("   • 验证序列格式")
    print()
    print("3. 性能优化:")
    print("   • 使用生成器处理大文件")
    print("   • 建立索引加速检索")
    print("   • 缓存计算结果")
    print()
    print("4. 最佳实践:")
    print("   • 模块化设计，函数单一职责")
    print("   • 完整的错误处理")
    print("   • 清晰的代码注释")


if __name__ == "__main__":
    main()