#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 00: 环境搭建 - 练习题参考答案（详细版）

这里是练习题的参考答案，每个答案都包含：
1. 完整的代码实现
2. 详细的注释说明
3. 多种实现方式（如果有）
4. 额外的知识扩展

记住：理解比记忆更重要！
"""

import sys
import os
import time
from pathlib import Path

# ========== 练习0：热身 - 确认环境正常 ==========
def practice_0_warmup():
    """
    练习0: 热身运动 - 参考答案
    
    学习要点：
    - print()函数是最基本的输出方式
    - Python可以打印中文和emoji
    """
    print("\n" + "="*50)
    print("🔍 练习0: 热身运动 - 参考答案")
    print("="*50)
    
    # 基础打印
    print("✅ 恭喜！如果你看到这行字，说明你的Python环境正常工作！")
    
    # 学员可能的答案示例
    print("我爱生物信息学！")
    print("Python比我想象的简单！")
    print("开始我的编程之旅！")
    
    # 额外展示：打印特殊字符
    print("\n知识扩展：")
    print("Python可以打印各种字符：")
    print("  中文：你好世界")
    print("  日文：こんにちは")
    print("  希腊字母：α β γ δ")
    print("  生物学符号：DNA 🧬 RNA 🦠")

# ========== 练习1：第一步 - Hello World ==========
def practice_1_hello_world():
    """
    练习1: Hello World! - 参考答案
    
    学习要点：
    - print()函数的基本用法
    - 字符串可以用单引号或双引号
    """
    print("\n" + "="*50)
    print("🔍 练习1: Hello World! - 参考答案")
    print("="*50)
    
    # 答案1.1: 基础Hello World
    print("Hello, BioPython!")
    
    # 答案1.2: 打印名字
    print("我是 生物信息学习者")
    
    # 答案1.3: 打印专业
    print("我的专业是: 生物信息学")
    
    # 知识扩展：不同的打印方式
    print("\n知识扩展 - 多种打印方式：")
    
    # 方式1：直接打印
    print("方式1: 直接打印字符串")
    
    # 方式2：打印多个值
    print("方式2:", "可以", "打印", "多个", "值")
    
    # 方式3：使用分隔符
    print("方式3", "自定义", "分隔符", sep=" | ")
    
    # 方式4：控制结尾
    print("方式4: 不换行", end=" ")
    print("（这是同一行）")

# ========== 练习2：变量 - 给数据贴标签 ==========
def practice_2_variables():
    """
    练习2: 变量 - 参考答案
    
    学习要点：
    - 变量命名规则
    - 基本数据类型
    - f-string格式化
    """
    print("\n" + "="*50)
    print("🔍 练习2: 变量基础 - 参考答案")
    print("="*50)
    
    # 示例变量
    sample_name = "HeLa细胞"
    cell_count = 1000000
    print(f"示例 - 样本: {sample_name}, 细胞数: {cell_count}")
    
    # 答案2.1: 创建DNA序列变量
    dna_sequence = "ATCGATCGATCG"
    
    # 答案2.2: 计算长度
    sequence_length = len(dna_sequence)
    
    # 答案2.3: 打印变量
    print(f"DNA序列: {dna_sequence}")
    print(f"序列长度: {sequence_length}")
    
    # 知识扩展：Python的数据类型
    print("\n知识扩展 - Python基本数据类型：")
    
    # 字符串 (str)
    gene_name = "BRCA1"
    print(f"字符串: {gene_name} (类型: {type(gene_name).__name__})")
    
    # 整数 (int)
    chromosome_number = 23
    print(f"整数: {chromosome_number} (类型: {type(chromosome_number).__name__})")
    
    # 浮点数 (float)
    melting_temp = 72.5
    print(f"浮点数: {melting_temp} (类型: {type(melting_temp).__name__})")
    
    # 布尔值 (bool)
    is_mutated = False
    print(f"布尔值: {is_mutated} (类型: {type(is_mutated).__name__})")
    
    # 列表 (list)
    amino_acids = ["Ala", "Cys", "Asp"]
    print(f"列表: {amino_acids} (类型: {type(amino_acids).__name__})")
    
    # 变量命名规则展示
    print("\n变量命名规则：")
    print("  ✅ 好的命名: dna_sequence, geneCount, is_valid")
    print("  ❌ 错误命名: 123abc（数字开头）, my-var（包含-）, class（保留字）")

# ========== 练习3：基本计算 - 生物学数据处理 ==========
def practice_3_basic_calculation():
    """
    练习3: 基本计算 - 参考答案
    
    学习要点：
    - 字符串方法（count, upper, lower）
    - 算术运算
    - 格式化输出
    """
    print("\n" + "="*50)
    print("🔍 练习3: 基本计算 - GC含量 - 参考答案")
    print("="*50)
    
    # 给定序列
    dna_sequence = "ATCGATCGATCG"
    print(f"给定DNA序列: {dna_sequence}")
    
    # 答案3.1: 计算长度
    length = len(dna_sequence)
    
    # 答案3.2: 计算G的个数
    g_count = dna_sequence.count('G')
    
    # 答案3.3: 计算C的个数
    c_count = dna_sequence.count('C')
    
    # 答案3.4: 计算GC含量
    gc_content = (g_count + c_count) / length * 100
    
    # 答案3.5: 打印结果
    print(f"序列长度: {length} bp")
    print(f"G的个数: {g_count}")
    print(f"C的个数: {c_count}")
    print(f"GC含量: {gc_content:.1f}%")
    
    # 知识扩展：更多计算
    print("\n知识扩展 - 更多序列分析：")
    
    # AT含量
    a_count = dna_sequence.count('A')
    t_count = dna_sequence.count('T')
    at_content = (a_count + t_count) / length * 100
    print(f"AT含量: {at_content:.1f}%")
    
    # 各碱基比例
    print("\n碱基组成：")
    for base in 'ATCG':
        count = dna_sequence.count(base)
        percentage = count / length * 100
        print(f"  {base}: {count} ({percentage:.1f}%)")
    
    # Tm计算（简化公式）
    # Wallace规则: Tm = 2*(A+T) + 4*(G+C)
    tm_wallace = 2 * (a_count + t_count) + 4 * (g_count + c_count)
    print(f"\nTm (Wallace): {tm_wallace}°C")
    
    # 更精确的Tm计算
    # Tm = 64.9 + 41 * (G+C-16.4) / (A+T+G+C)
    if length > 0:
        tm_accurate = 64.9 + 41 * (g_count + c_count - 16.4) / length
        print(f"Tm (精确): {tm_accurate:.1f}°C")

# ========== 练习4：使用Python模块 ==========
def practice_4_modules():
    """
    练习4: 使用Python模块 - 参考答案
    
    学习要点：
    - import语句
    - 模块的属性和方法
    - 系统信息获取
    """
    print("\n" + "="*50)
    print("🔍 练习4: Python模块使用 - 参考答案")
    print("="*50)
    
    # 答案4.2: Python版本
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    print(f"Python版本: {major}.{minor}.{micro}")
    
    # 答案4.3: Python路径
    python_path = sys.executable
    print(f"Python路径: {python_path}")
    
    # 答案4.4: 当前目录
    current_dir = os.getcwd()
    print(f"当前目录: {current_dir}")
    
    # 知识扩展：更多有用的模块信息
    print("\n知识扩展 - 更多系统信息：")
    
    # 平台信息
    import platform
    print(f"操作系统: {platform.system()}")
    print(f"系统版本: {platform.release()}")
    print(f"Python实现: {platform.python_implementation()}")
    
    # 环境变量
    print(f"\nPATH变量（前100字符）:")
    path = os.environ.get('PATH', '')[:100]
    print(f"  {path}...")
    
    # 模块搜索路径
    print(f"\nPython模块搜索路径（前3个）:")
    for path in sys.path[:3]:
        print(f"  {path}")
    
    # 使用Path（现代化的路径处理）
    from pathlib import Path
    current_path = Path.cwd()
    print(f"\n使用pathlib的当前路径: {current_path}")
    print(f"  父目录: {current_path.parent}")
    print(f"  是否存在: {current_path.exists()}")

# ========== 练习5：条件判断 ==========
def practice_5_conditions():
    """
    练习5: 条件判断 - 参考答案
    
    学习要点：
    - if-elif-else结构
    - 比较运算符
    - 逻辑运算符
    """
    print("\n" + "="*50)
    print("🔍 练习5: 条件判断 - 参考答案")
    print("="*50)
    
    # 测试序列
    test_sequences = [
        "ATATATATAT",  # 0% GC
        "ATCGATCGAT",  # 40% GC
        "GCGCGCGCGC",  # 100% GC
    ]
    
    for seq in test_sequences:
        print(f"\n分析序列: {seq}")
        
        # 答案5.1: 计算GC含量
        gc_count = seq.count('G') + seq.count('C')
        gc_content = gc_count / len(seq) * 100
        
        # 答案5.2: 判断退火温度
        if gc_content < 30:
            temperature = 55
            category = "低GC含量"
        elif gc_content <= 60:
            temperature = 60
            category = "中等GC含量"
        else:
            temperature = 65
            category = "高GC含量"
        
        # 答案5.3: 打印结果
        print(f"  GC含量: {gc_content:.1f}%")
        print(f"  类别: {category}")
        print(f"  建议退火温度: {temperature}°C")
    
    # 知识扩展：更复杂的条件判断
    print("\n知识扩展 - 复杂条件判断：")
    
    sequence = "ATCGATCGATCG"
    length = len(sequence)
    gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
    
    # 多条件组合
    if length < 20 and gc_content > 60:
        primer_quality = "短且GC含量高，可能形成二级结构"
    elif length < 20 and gc_content < 40:
        primer_quality = "短且GC含量低，Tm可能太低"
    elif 20 <= length <= 30 and 40 <= gc_content <= 60:
        primer_quality = "理想的引物"
    else:
        primer_quality = "需要进一步优化"
    
    print(f"引物评估: {primer_quality}")
    
    # 使用三元运算符（简化的if-else）
    is_long = "长序列" if length > 50 else "短序列"
    print(f"序列类型: {is_long}")

# ========== 练习6：函数定义 ==========
def practice_6_functions():
    """
    练习6: 定义自己的函数 - 参考答案
    
    学习要点：
    - 函数定义语法
    - 参数和返回值
    - 文档字符串
    """
    print("\n" + "="*50)
    print("🔍 练习6: 函数定义 - 参考答案")
    print("="*50)
    
    # 答案6.1: 计算序列长度的函数
    def get_sequence_length(sequence):
        """计算序列长度"""
        return len(sequence)
    
    # 答案6.2: 验证DNA序列的函数
    def is_valid_dna(sequence):
        """
        验证是否为有效的DNA序列
        
        参数:
            sequence: 待验证的序列字符串
        
        返回:
            bool: True如果有效，False如果无效
        """
        sequence = sequence.upper()
        valid_bases = set('ATCG')
        return all(base in valid_bases for base in sequence)
    
    # 答案6.3: DNA转RNA的函数
    def dna_to_rna(dna):
        """
        将DNA序列转换为RNA序列
        
        参数:
            dna: DNA序列字符串
        
        返回:
            str: 对应的RNA序列
        """
        return dna.upper().replace('T', 'U')
    
    # 测试序列
    test_dna = "ATCGATCG"
    print(f"测试序列: {test_dna}")
    
    # 答案6.4: 调用函数
    length = get_sequence_length(test_dna)
    is_valid = is_valid_dna(test_dna)
    rna = dna_to_rna(test_dna)
    
    print(f"序列长度: {length}")
    print(f"是否有效: {is_valid}")
    print(f"RNA序列: {rna}")
    
    # 知识扩展：更多函数示例
    print("\n知识扩展 - 高级函数功能：")
    
    # 带默认参数的函数
    def calculate_tm(sequence, salt_conc=50, primer_conc=50):
        """
        计算引物的Tm值
        
        参数:
            sequence: DNA序列
            salt_conc: 盐浓度(mM)，默认50
            primer_conc: 引物浓度(nM)，默认50
        """
        length = len(sequence)
        gc_count = sequence.count('G') + sequence.count('C')
        
        # 简化的Tm计算公式
        basic_tm = 64.9 + 41 * (gc_count - 16.4) / length
        
        # 盐浓度校正
        salt_correction = 12.5 * (salt_conc / 1000) ** 0.5
        
        return basic_tm + salt_correction
    
    tm1 = calculate_tm(test_dna)  # 使用默认参数
    tm2 = calculate_tm(test_dna, salt_conc=100)  # 修改盐浓度
    
    print(f"默认条件Tm: {tm1:.1f}°C")
    print(f"高盐条件Tm: {tm2:.1f}°C")
    
    # 返回多个值的函数
    def analyze_sequence_advanced(sequence):
        """返回多个分析结果"""
        length = len(sequence)
        gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
        at_content = 100 - gc_content
        
        return length, gc_content, at_content
    
    # 解包返回的多个值
    seq_len, gc_pct, at_pct = analyze_sequence_advanced(test_dna)
    print(f"\n高级分析结果:")
    print(f"  长度: {seq_len} bp")
    print(f"  GC%: {gc_pct:.1f}%")
    print(f"  AT%: {at_pct:.1f}%")

# ========== 练习7：文件操作 ==========
def practice_7_file_operations():
    """
    练习7: 文件操作 - 参考答案
    
    学习要点：
    - 文件的打开模式（r, w, a）
    - with语句的使用
    - 文件路径处理
    """
    print("\n" + "="*50)
    print("🔍 练习7: 文件操作 - 参考答案")
    print("="*50)
    
    filename = "my_first_sequence.txt"
    dna_sequence = "ATCGATCGATCGATCG"
    
    # 答案7.1: 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(">Sequence_1\n")
        f.write(dna_sequence)
    print(f"✅ 文件 {filename} 创建成功！")
    
    # 答案7.2: 读取文件
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"文件内容:\n{content}")
    
    # 答案7.3: 追加内容
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\n>Sequence_2\n")
        f.write("GCGCGCGCGCGC")
    print("✅ 新序列已添加！")
    
    # 重新读取验证
    with open(filename, 'r', encoding='utf-8') as f:
        updated_content = f.read()
    print(f"更新后的内容:\n{updated_content}")
    
    # 答案7.4: 删除文件
    if os.path.exists(filename):
        os.remove(filename)
        print(f"✅ 文件 {filename} 已删除")
    
    # 知识扩展：更多文件操作
    print("\n知识扩展 - 高级文件操作：")
    
    # 创建临时文件演示更多功能
    temp_file = "temp_demo.fasta"
    
    # 写入多行FASTA格式
    sequences = [
        (">Gene1 | Homo sapiens", "ATCGATCGATCGATCG"),
        (">Gene2 | Mus musculus", "GCGCGCGCGCGCGCGC"),
        (">Gene3 | Drosophila", "ATATATATATATATATAT")
    ]
    
    with open(temp_file, 'w', encoding='utf-8') as f:
        for header, seq in sequences:
            f.write(f"{header}\n{seq}\n")
    
    print("创建了多序列FASTA文件")
    
    # 逐行读取
    print("\n逐行读取文件:")
    with open(temp_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            print(f"  行{line_num}: {line.strip()}")
    
    # 读取并解析FASTA
    print("\n解析FASTA格式:")
    with open(temp_file, 'r', encoding='utf-8') as f:
        current_header = None
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_header = line[1:]  # 去掉>
                print(f"  发现序列: {current_header}")
            else:
                print(f"    序列内容: {line}")
    
    # 使用pathlib（现代化方式）
    from pathlib import Path
    path = Path(temp_file)
    
    print(f"\n使用pathlib:")
    print(f"  文件名: {path.name}")
    print(f"  文件大小: {path.stat().st_size} bytes")
    print(f"  绝对路径: {path.absolute()}")
    
    # 清理
    if path.exists():
        path.unlink()  # pathlib的删除方法
        print(f"✅ 临时文件已清理")

# ========== 练习8：综合练习 ==========
def practice_8_integration():
    """
    练习8: 综合练习 - 参考答案
    
    学习要点：
    - 综合运用所有知识
    - 错误处理
    - 代码组织
    """
    print("\n" + "="*50)
    print("🔍 练习8: 综合练习 - 序列分析器 - 参考答案")
    print("="*50)
    
    # 答案8.1: 综合分析函数
    def analyze_sequence(sequence):
        """
        分析DNA序列的综合函数
        
        参数:
            sequence: DNA序列字符串
        
        返回:
            dict: 包含分析结果的字典
        """
        # 转大写处理
        sequence = sequence.upper()
        
        # 验证序列
        valid_bases = set('ATCG')
        is_valid = all(base in valid_bases for base in sequence)
        
        if not is_valid:
            # 找出无效字符
            invalid_chars = set(sequence) - valid_bases
            return {"error": f"Invalid DNA sequence. Invalid characters: {invalid_chars}"}
        
        # 计算各种属性
        length = len(sequence)
        
        # 防止除零错误
        if length == 0:
            return {"error": "Empty sequence"}
        
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        a_count = sequence.count('A')
        t_count = sequence.count('T')
        
        gc_count = g_count + c_count
        gc_content = (gc_count / length) * 100
        at_content = 100 - gc_content
        
        # DNA转RNA
        rna = sequence.replace('T', 'U')
        
        # 计算Tm（简化公式）
        if length < 14:
            tm = 2 * (a_count + t_count) + 4 * (g_count + c_count)
        else:
            tm = 64.9 + 41 * (gc_count - 16.4) / length
        
        # 返回完整结果
        return {
            "sequence": sequence,
            "length": length,
            "gc_content": gc_content,
            "at_content": at_content,
            "rna": rna,
            "tm": tm,
            "base_counts": {
                "A": a_count,
                "T": t_count,
                "G": g_count,
                "C": c_count
            }
        }
    
    # 测试序列
    test_sequences = [
        "ATCGATCG",
        "GGCCGGCC",
        "ATATATATATAT",
        "INVALID123",
        "",  # 空序列
        "atcgatcg"  # 小写序列
    ]
    
    # 答案8.2: 分析并打印结果
    for seq in test_sequences:
        print(f"\n分析序列: '{seq}'")
        result = analyze_sequence(seq)
        
        if "error" in result:
            print(f"  ❌ 错误: {result['error']}")
        else:
            print(f"  ✅ 有效DNA序列")
            print(f"  长度: {result['length']} bp")
            print(f"  GC含量: {result['gc_content']:.1f}%")
            print(f"  AT含量: {result['at_content']:.1f}%")
            print(f"  RNA: {result['rna']}")
            print(f"  Tm: {result['tm']:.1f}°C")
            print(f"  碱基组成: A={result['base_counts']['A']}, "
                  f"T={result['base_counts']['T']}, "
                  f"G={result['base_counts']['G']}, "
                  f"C={result['base_counts']['C']}")
    
    # 知识扩展：创建序列分析报告
    print("\n" + "="*50)
    print("知识扩展 - 生成分析报告")
    print("="*50)
    
    def generate_report(sequence, output_file=None):
        """生成详细的序列分析报告"""
        result = analyze_sequence(sequence)
        
        if "error" in result:
            report = f"分析失败: {result['error']}"
        else:
            # 生成报告
            report_lines = [
                "=" * 50,
                "DNA序列分析报告",
                f"生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}",
                "=" * 50,
                "",
                "【序列信息】",
                f"原始序列: {result['sequence'][:50]}{'...' if len(result['sequence']) > 50 else ''}",
                f"序列长度: {result['length']} bp",
                "",
                "【碱基组成】",
                f"A: {result['base_counts']['A']} ({result['base_counts']['A']/result['length']*100:.1f}%)",
                f"T: {result['base_counts']['T']} ({result['base_counts']['T']/result['length']*100:.1f}%)",
                f"G: {result['base_counts']['G']} ({result['base_counts']['G']/result['length']*100:.1f}%)",
                f"C: {result['base_counts']['C']} ({result['base_counts']['C']/result['length']*100:.1f}%)",
                "",
                "【理化性质】",
                f"GC含量: {result['gc_content']:.2f}%",
                f"AT含量: {result['at_content']:.2f}%",
                f"预测Tm: {result['tm']:.1f}°C",
                "",
                "【转录产物】",
                f"RNA序列: {result['rna'][:50]}{'...' if len(result['rna']) > 50 else ''}",
                "",
                "=" * 50
            ]
            report = "\n".join(report_lines)
        
        # 打印或保存报告
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"报告已保存到: {output_file}")
        else:
            print(report)
        
        return report
    
    # 生成示例报告
    test_seq = "ATCGATCGATCGATCGATCGATCG"
    print(f"\n生成序列报告: {test_seq}")
    generate_report(test_seq)

# ========== 额外练习：进阶功能展示 ==========
def bonus_exercises():
    """
    额外练习: 展示更多Python功能
    
    这部分展示一些进阶但实用的功能
    """
    print("\n" + "="*60)
    print("🌟 额外练习: 进阶功能展示")
    print("="*60)
    
    # 1. 列表推导式
    print("\n1. 列表推导式 - 优雅的循环：")
    dna = "ATCGATCG"
    
    # 传统方式
    codons_traditional = []
    for i in range(0, len(dna), 3):
        codons_traditional.append(dna[i:i+3])
    print(f"传统方式: {codons_traditional}")
    
    # 列表推导式
    codons_elegant = [dna[i:i+3] for i in range(0, len(dna), 3)]
    print(f"列表推导式: {codons_elegant}")
    
    # 2. 字典的使用
    print("\n2. 字典 - 存储配对信息：")
    codon_table = {
        'ATG': 'Met',  # 起始密码子
        'TAA': 'Stop',  # 终止密码子
        'ATC': 'Ile',
        'GAT': 'Asp',
        'CGA': 'Arg',
        'TCG': 'Ser'
    }
    
    for codon in codons_elegant:
        amino_acid = codon_table.get(codon, 'Unknown')
        print(f"  {codon} -> {amino_acid}")
    
    # 3. 异常处理
    print("\n3. 异常处理 - 优雅地处理错误：")
    
    def safe_gc_calculation(sequence):
        """安全的GC含量计算"""
        try:
            if not sequence:
                raise ValueError("序列不能为空")
            
            sequence = sequence.upper()
            valid_bases = set('ATCG')
            
            if not all(base in valid_bases for base in sequence):
                raise ValueError("序列包含无效碱基")
            
            gc_count = sequence.count('G') + sequence.count('C')
            gc_content = (gc_count / len(sequence)) * 100
            
            return gc_content
            
        except ValueError as e:
            print(f"  错误: {e}")
            return None
        except Exception as e:
            print(f"  未知错误: {e}")
            return None
    
    # 测试异常处理
    test_cases = ["ATCG", "", "ATCX", None]
    for test in test_cases:
        result = safe_gc_calculation(test)
        if result is not None:
            print(f"  '{test}' -> GC含量: {result:.1f}%")
    
    # 4. 类的简单示例
    print("\n4. 面向对象 - DNA序列类：")
    
    class DNASequence:
        """简单的DNA序列类"""
        
        def __init__(self, sequence):
            self.sequence = sequence.upper()
        
        def length(self):
            return len(self.sequence)
        
        def gc_content(self):
            gc = self.sequence.count('G') + self.sequence.count('C')
            return (gc / len(self.sequence)) * 100 if self.sequence else 0
        
        def to_rna(self):
            return self.sequence.replace('T', 'U')
        
        def __str__(self):
            return f"DNA({self.sequence[:10]}{'...' if len(self.sequence) > 10 else ''})"
    
    # 使用类
    dna_obj = DNASequence("ATCGATCGATCGATCG")
    print(f"  对象: {dna_obj}")
    print(f"  长度: {dna_obj.length()} bp")
    print(f"  GC%: {dna_obj.gc_content():.1f}%")
    print(f"  RNA: {dna_obj.to_rna()}")

# ========== 主函数：运行所有练习 ==========
def main():
    """
    主函数: 运行所有练习的参考答案
    """
    print("="*60)
    print("🧬 Chapter 00 练习题 - 参考答案")
    print("="*60)
    print("\n这些是练习题的完整参考实现")
    print("包含详细注释和额外的知识扩展\n")
    
    # 运行所有练习答案
    practice_0_warmup()
    practice_1_hello_world()
    practice_2_variables()
    practice_3_basic_calculation()
    practice_4_modules()
    practice_5_conditions()
    practice_6_functions()
    practice_7_file_operations()
    practice_8_integration()
    
    # 额外内容
    bonus_exercises()
    
    print("\n" + "="*60)
    print("🎉 所有练习答案展示完成！")
    print("="*60)
    print("\n💡 学习要点总结:")
    print("1. print() - 输出信息的基本方法")
    print("2. 变量 - 存储数据的容器")
    print("3. len(), count() - 常用的字符串方法")
    print("4. if-elif-else - 条件判断")
    print("5. def - 定义函数")
    print("6. with open() - 安全的文件操作")
    print("7. import - 导入模块")
    print("8. 异常处理 - 让程序更健壮")
    
    print("\n📚 继续学习建议:")
    print("1. 尝试修改这些代码，看看会发生什么")
    print("2. 结合自己的研究数据练习")
    print("3. 遇到错误不要怕，这是学习的机会")
    print("4. 准备好进入Chapter 01的深入学习！")
    
    print("\n记住：编程是一门实践技能，多写代码才能进步！")

if __name__ == "__main__":
    main()