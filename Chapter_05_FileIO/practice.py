#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 05: 文件IO与FASTA处理 - 练习题

通过这些练习，你将：
1. 掌握文件的基本操作
2. 学会解析真实的生物数据格式
3. 处理各种异常情况
4. 优化大文件处理性能

练习难度：
⭐ 初级 - 建立信心
⭐⭐ 中级 - 实际应用
⭐⭐⭐ 高级 - 研究级别
"""

import os


def practice_1_basic_file_operations():
    """
    练习1: 基础文件操作 ⭐
    
    生物学场景：你刚完成了一个PCR实验，需要记录实验结果
    
    任务：
    1. 创建一个实验记录文件
    2. 写入PCR结果数据
    3. 读取并分析序列组成
    """
    print("=" * 60)
    print("练习1: PCR实验数据记录 ⭐")
    print("-" * 60)
    
    # TODO: 完成以下任务
    # 1. 创建文件 "pcr_results.txt"
    # 2. 写入以下PCR产物序列（每条序列一行）：
    #    ATCGATCGATCGATCGATCGATCG
    #    GCTAGCTAGCTAGCTAGCTAGCTA
    #    TTTTAAAACCCCGGGGTTTTAAAA
    
    # 3. 读取文件并计算：
    #    - 总序列长度
    #    - 各碱基(A,T,C,G)的数量
    #    - GC含量百分比
    
    # 提示：使用with语句确保文件正确关闭
    
    pass


def practice_2_simple_fasta_parser():
    """
    练习2: 简单FASTA解析器 ⭐
    
    生物学场景：你收到了同事发来的FASTA格式序列文件
    
    任务：编写一个简单的FASTA解析器，提取序列信息
    """
    print("\n" + "=" * 60)
    print("练习2: FASTA格式解析 ⭐")
    print("-" * 60)
    
    # 创建示例FASTA文件
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
    
    print("已创建测试文件: test.fasta")
    
    # TODO: 完成解析器函数
    def parse_simple_fasta(filename):
        """
        解析FASTA文件
        
        返回格式: [(序列ID, 序列), ...]
        例如: [('gene_001', 'ATGGCTAGC...'), ...]
        """
        # 你的代码写在这里
        pass
    
    # 测试你的解析器
    # sequences = parse_simple_fasta("test.fasta")
    # print(f"找到 {len(sequences)} 条序列")
    # for seq_id, seq in sequences:
    #     print(f"  {seq_id}: {len(seq)} bp")
    
    # 清理文件
    os.remove("test.fasta")


def practice_3_fasta_quality_control():
    """
    练习3: FASTA质量控制 ⭐⭐
    
    生物学场景：测序公司发来了原始序列数据，需要质量控制
    
    任务：过滤低质量序列，生成清洁的FASTA文件
    """
    print("\n" + "=" * 60)
    print("练习3: 序列质量控制 ⭐⭐")
    print("-" * 60)
    
    # 创建包含不同质量序列的FASTA文件
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
    
    print("已创建原始序列文件: raw_sequences.fasta")
    
    # TODO: 实现质量控制函数
    def filter_sequences(input_file, output_file, min_length=50, max_n_percent=5):
        """
        过滤低质量序列
        
        过滤条件:
        1. 序列长度必须 >= min_length
        2. N的比例必须 <= max_n_percent%
        3. 去除低复杂度序列（同一碱基占比>80%）
        
        参数:
            input_file: 输入FASTA文件
            output_file: 输出FASTA文件
            min_length: 最小序列长度
            max_n_percent: 最大N比例
        
        返回:
            (保留序列数, 过滤序列数)
        """
        # 你的代码写在这里
        pass
    
    # 测试你的过滤函数
    # kept, filtered = filter_sequences("raw_sequences.fasta", "clean.fasta")
    # print(f"保留: {kept} 条序列")
    # print(f"过滤: {filtered} 条序列")
    
    # 清理文件
    os.remove("raw_sequences.fasta")
    # 如果创建了输出文件也要清理
    # if os.path.exists("clean.fasta"):
    #     os.remove("clean.fasta")


def practice_4_batch_processing():
    """
    练习4: 批量文件处理 ⭐⭐
    
    生物学场景：你有多个样本的测序数据，需要批量分析
    
    任务：批量处理多个FASTA文件，生成统计报告
    """
    print("\n" + "=" * 60)
    print("练习4: 批量序列分析 ⭐⭐")
    print("-" * 60)
    
    # 创建多个样本文件
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
    
    # 创建样本文件
    for filename, content in samples.items():
        with open(filename, "w") as f:
            f.write(content)
    
    print(f"已创建 {len(samples)} 个样本文件")
    
    # TODO: 实现批量分析函数
    def batch_analyze_fasta(file_pattern="*.fasta"):
        """
        批量分析FASTA文件
        
        对每个文件统计:
        1. 序列数量
        2. 总长度
        3. 平均长度
        4. GC含量
        
        返回:
            字典 {文件名: {统计信息}}
        """
        import glob
        
        results = {}
        # 你的代码写在这里
        
        return results
    
    # 测试批量分析
    # stats = batch_analyze_fasta("sample_*.fasta")
    # for filename, stat in stats.items():
    #     print(f"\n{filename}:")
    #     print(f"  序列数: {stat['count']}")
    #     print(f"  总长度: {stat['total_length']} bp")
    #     print(f"  平均长度: {stat['avg_length']:.1f} bp")
    #     print(f"  GC含量: {stat['gc_content']:.1f}%")
    
    # 清理文件
    for filename in samples.keys():
        os.remove(filename)


def practice_5_format_converter():
    """
    练习5: 格式转换器 ⭐⭐⭐
    
    生物学场景：不同软件需要不同的序列格式
    
    任务：实现FASTA到其他格式的转换器
    """
    print("\n" + "=" * 60)
    print("练习5: 序列格式转换 ⭐⭐⭐")
    print("-" * 60)
    
    # TODO: 实现格式转换器
    def fasta_to_tabular(input_file, output_file):
        """
        将FASTA转换为表格格式
        
        输出格式(制表符分隔):
        序列ID    长度    GC%    序列
        gene1     100     45.5   ATCG...
        """
        # 你的代码写在这里
        pass
    
    def fasta_to_phylip(input_file, output_file):
        """
        将FASTA转换为PHYLIP格式
        
        PHYLIP格式:
        第一行: 序列数 序列长度
        后续行: 序列名(10字符) 序列
        """
        # 你的代码写在这里
        pass
    
    print("请实现格式转换函数")
    print("1. fasta_to_tabular: FASTA → 表格")
    print("2. fasta_to_phylip: FASTA → PHYLIP")


def practice_6_large_genome_processor():
    """
    练习6: 大基因组处理 ⭐⭐⭐
    
    生物学场景：处理人类基因组（3GB）级别的大文件
    
    任务：实现内存友好的基因组处理器
    """
    print("\n" + "=" * 60)
    print("练习6: 大基因组文件处理 ⭐⭐⭐")
    print("-" * 60)
    
    # TODO: 实现大文件处理器
    def process_large_genome(filename, chunk_size=1000000):
        """
        使用生成器处理大型基因组文件
        
        功能:
        1. 逐条序列处理，不全部加载到内存
        2. 统计每条染色体的长度和GC含量
        3. 找出最长的序列
        
        使用生成器(yield)实现内存友好的处理
        """
        # 你的代码写在这里
        pass
    
    print("请实现大文件处理器")
    print("提示：使用yield创建生成器")
    print("目标：处理GB级别文件而不耗尽内存")


def challenge_fasta_database():
    """
    挑战题: 构建序列数据库 ⭐⭐⭐⭐
    
    生物学场景：构建本地BLAST数据库的索引系统
    
    任务：创建高效的序列索引和检索系统
    """
    print("\n" + "=" * 60)
    print("挑战题: 序列数据库系统 ⭐⭐⭐⭐")
    print("-" * 60)
    
    class FastaDatabase:
        """
        FASTA数据库类
        
        功能:
        1. 建立序列索引（不全部加载序列）
        2. 快速检索特定序列
        3. 支持模糊搜索（按ID或描述）
        4. 统计信息缓存
        """
        
        def __init__(self, fasta_file):
            """初始化数据库"""
            self.filename = fasta_file
            self.index = {}  # {seq_id: file_position}
            # TODO: 建立索引
            pass
        
        def build_index(self):
            """建立文件位置索引"""
            # TODO: 记录每条序列在文件中的位置
            pass
        
        def get_sequence(self, seq_id):
            """快速获取指定序列"""
            # TODO: 使用索引直接跳到文件位置
            pass
        
        def search(self, keyword):
            """搜索包含关键词的序列"""
            # TODO: 实现搜索功能
            pass
        
        def statistics(self):
            """返回数据库统计信息"""
            # TODO: 返回序列数、总长度等信息
            pass
    
    print("这是一个高级挑战！")
    print("目标：实现类似BLAST数据库的索引系统")
    print("应用：快速检索大型序列数据库")


def main():
    """
    主函数：运行所有练习
    """
    print("🧬 Chapter 05: 文件IO与FASTA处理 - 练习题")
    print("=" * 60)
    print("\n请依次完成以下练习：\n")
    
    # 基础练习
    practice_1_basic_file_operations()
    practice_2_simple_fasta_parser()
    
    # 中级练习
    practice_3_fasta_quality_control()
    practice_4_batch_processing()
    
    # 高级练习
    practice_5_format_converter()
    practice_6_large_genome_processor()
    
    # 挑战题
    challenge_fasta_database()
    
    print("\n" + "=" * 60)
    print("💡 练习提示：")
    print("1. 从简单的练习开始，逐步提升难度")
    print("2. 先让代码能运行，再考虑优化")
    print("3. 遇到困难时查看 practice_solution.py")
    print("4. 记住：文件操作一定要处理异常！")


if __name__ == "__main__":
    main()