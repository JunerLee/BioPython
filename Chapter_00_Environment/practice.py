#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 00: 环境搭建 - 渐进式练习题

通过完成这些练习，你将熟悉Python开发环境的基本操作。
每个练习都从极简单开始，逐步增加难度。

学习建议：
1. 不要着急，慢慢来
2. 遇到不会的，看提示
3. 实在不会，看参考答案（practice_solution.py）
4. 重要的是理解，不是死记硬背
"""

import sys
import os

# ========== 练习0：热身 - 确认环境正常 ==========
def practice_0_warmup():
    """
    练习0: 热身运动
    
    目标: 确认你的Python环境可以正常运行代码
    难度: ⭐（超级简单）
    """
    print("\n" + "="*50)
    print("🔍 练习0: 热身运动")
    print("="*50)
    
    # 这行代码已经为你写好了，运行看看效果！
    print("✅ 恭喜！如果你看到这行字，说明你的Python环境正常工作！")
    
    # TODO: 在下面添加一行代码，打印任何你想说的话
    # 提示: 复制上面的print语句，修改引号内的文字
    # 例如: print("我爱生物信息学！")
    
    # 在这里写你的代码：
    

# ========== 练习1：第一步 - Hello World ==========
def practice_1_hello_world():
    """
    练习1: Hello World!
    
    目标: 编写你的第一个Python程序
    难度: ⭐（非常简单）
    
    为什么要做这个练习？
    - "Hello World"是编程界的传统，就像做PCR前先跑个电泳确认DNA质量
    - 这是测试环境是否正常的最简单方法
    """
    print("\n" + "="*50)
    print("🔍 练习1: Hello World!")
    print("="*50)
    
    # TODO 1.1: 打印 "Hello, BioPython!"
    # 提示: 使用 print() 函数
    # 语法: print("你想打印的文字")
    # 在下面写你的代码：
    
    
    # TODO 1.2: 打印你的名字
    # 提示: print("我是 [你的名字]")
    # 在下面写你的代码：
    
    
    # TODO 1.3: 用一行代码打印你的专业
    # 提示: print("我的专业是: 生物信息学")  # 改成你的专业
    # 在下面写你的代码：
    
    
    pass  # 完成TODO后可以删除这行

# ========== 练习2：变量 - 给数据贴标签 ==========
def practice_2_variables():
    """
    练习2: 变量 - 数据的标签
    
    目标: 学习创建和使用变量
    难度: ⭐⭐（简单）
    
    类比理解：
    变量就像试管架上的标签，告诉你这个试管里装的是什么
    """
    print("\n" + "="*50)
    print("🔍 练习2: 变量基础")
    print("="*50)
    
    # 示例：这是如何创建变量
    sample_name = "HeLa细胞"  # 字符串变量
    cell_count = 1000000      # 整数变量
    print(f"示例 - 样本: {sample_name}, 细胞数: {cell_count}")
    
    # TODO 2.1: 创建一个变量存储DNA序列
    # 提示: 变量名 = "ATCG..."
    # 在下面写你的代码：
    dna_sequence = ""  # 修改这里，给它赋一个DNA序列
    
    
    # TODO 2.2: 创建一个变量存储序列的长度
    # 提示: 使用 len() 函数
    # 语法: sequence_length = len(dna_sequence)
    # 在下面写你的代码：
    
    
    # TODO 2.3: 打印这两个变量
    # 提示: print(f"DNA序列: {dna_sequence}")
    # 提示: print(f"序列长度: {sequence_length}")
    # 在下面写你的代码：
    
    
    pass  # 完成TODO后可以删除这行

# ========== 练习3：基本计算 - 生物学数据处理 ==========
def practice_3_basic_calculation():
    """
    练习3: 基本计算
    
    目标: 进行简单的生物学相关计算
    难度: ⭐⭐（简单）
    
    实际应用：
    GC含量影响DNA的稳定性和PCR退火温度
    """
    print("\n" + "="*50)
    print("🔍 练习3: 基本计算 - GC含量")
    print("="*50)
    
    # 给定的DNA序列
    dna_sequence = "ATCGATCGATCG"
    print(f"给定DNA序列: {dna_sequence}")
    
    # TODO 3.1: 计算序列长度
    # 提示: 使用 len() 函数
    # length = len(dna_sequence)
    # 在下面写你的代码：
    
    
    # TODO 3.2: 计算G的个数
    # 提示: 使用 count() 方法
    # 语法: g_count = dna_sequence.count('G')
    # 在下面写你的代码：
    
    
    # TODO 3.3: 计算C的个数
    # 提示: 类似上面，但是数'C'
    # 在下面写你的代码：
    
    
    # TODO 3.4: 计算GC含量百分比
    # 提示: GC% = (G个数 + C个数) / 总长度 * 100
    # 提示: gc_content = (g_count + c_count) / length * 100
    # 在下面写你的代码：
    
    
    # TODO 3.5: 打印结果
    # 提示: 使用f-string格式化输出
    # print(f"序列长度: {length} bp")
    # print(f"G的个数: {g_count}")
    # print(f"C的个数: {c_count}")  
    # print(f"GC含量: {gc_content:.1f}%")  # .1f表示保留1位小数
    # 在下面写你的代码：
    
    
    pass  # 完成TODO后可以删除这行

# ========== 练习4：使用Python模块 ==========
def practice_4_modules():
    """
    练习4: 使用Python模块
    
    目标: 学习导入和使用Python模块
    难度: ⭐⭐（简单）
    
    类比理解：
    模块就像实验室的不同仪器，每个都有特定功能
    """
    print("\n" + "="*50)
    print("🔍 练习4: Python模块使用")
    print("="*50)
    
    # TODO 4.1: 导入需要的模块
    # 提示: import语句通常放在文件开头，但这里为了练习放在函数内
    # 提示: import sys （已经在文件开头导入了）
    
    # TODO 4.2: 打印Python版本
    # 提示: 使用 sys.version_info
    # 提示: major = sys.version_info.major
    # 提示: minor = sys.version_info.minor
    # 在下面写你的代码：
    
    
    # TODO 4.3: 打印Python可执行文件路径
    # 提示: 使用 sys.executable
    # 提示: python_path = sys.executable
    # 提示: print(f"Python路径: {python_path}")
    # 在下面写你的代码：
    
    
    # TODO 4.4: 使用os模块获取当前目录
    # 提示: current_dir = os.getcwd()
    # 提示: print(f"当前目录: {current_dir}")
    # 在下面写你的代码：
    
    
    pass  # 完成TODO后可以删除这行

# ========== 练习5：条件判断 ==========
def practice_5_conditions():
    """
    练习5: 条件判断
    
    目标: 学习if-elif-else语句
    难度: ⭐⭐⭐（中等）
    
    实际应用：
    根据GC含量判断PCR退火温度
    """
    print("\n" + "="*50)
    print("🔍 练习5: 条件判断")
    print("="*50)
    
    # 测试序列
    test_sequences = [
        "ATATATATAT",  # 0% GC
        "ATCGATCGAT",  # 40% GC
        "GCGCGCGCGC",  # 100% GC
    ]
    
    for seq in test_sequences:
        print(f"\n分析序列: {seq}")
        
        # TODO 5.1: 计算GC含量
        # 提示: 复用练习3的方法
        # gc_count = seq.count('G') + seq.count('C')
        # gc_content = gc_count / len(seq) * 100
        # 在下面写你的代码：
        
        
        # TODO 5.2: 根据GC含量判断退火温度
        # 规则：
        # - GC含量 < 30%: 低温退火 (55°C)
        # - GC含量 30-60%: 中温退火 (60°C)
        # - GC含量 > 60%: 高温退火 (65°C)
        # 
        # 提示: 使用if-elif-else结构
        # if gc_content < 30:
        #     temperature = 55
        # elif gc_content <= 60:
        #     temperature = 60
        # else:
        #     temperature = 65
        # 在下面写你的代码：
        
        
        # TODO 5.3: 打印结果
        # 提示: print(f"  GC含量: {gc_content:.1f}%")
        # 提示: print(f"  建议退火温度: {temperature}°C")
        # 在下面写你的代码：
        
        
        pass  # 完成TODO后可以删除这行

# ========== 练习6：函数定义 ==========
def practice_6_functions():
    """
    练习6: 定义自己的函数
    
    目标: 学习创建可重用的函数
    难度: ⭐⭐⭐（中等）
    
    类比理解：
    函数就像实验Protocol，定义好后可以重复使用
    """
    print("\n" + "="*50)
    print("🔍 练习6: 函数定义")
    print("="*50)
    
    # TODO 6.1: 定义一个计算序列长度的函数
    # 提示: 函数结构
    # def get_sequence_length(sequence):
    #     """计算序列长度"""
    #     return len(sequence)
    # 在下面写你的函数：
    
    
    # TODO 6.2: 定义一个验证DNA序列的函数
    # 规则: 只包含A, T, C, G（大小写都可以）
    # 提示:
    # def is_valid_dna(sequence):
    #     """验证是否为有效的DNA序列"""
    #     sequence = sequence.upper()  # 转大写
    #     valid_bases = set('ATCG')
    #     return all(base in valid_bases for base in sequence)
    # 在下面写你的函数：
    
    
    # TODO 6.3: 定义一个DNA转RNA的函数
    # 规则: T -> U
    # 提示:
    # def dna_to_rna(dna):
    #     """将DNA序列转换为RNA序列"""
    #     return dna.upper().replace('T', 'U')
    # 在下面写你的函数：
    
    
    # 测试你的函数
    test_dna = "ATCGATCG"
    print(f"测试序列: {test_dna}")
    
    # TODO 6.4: 调用你定义的函数
    # 提示: length = get_sequence_length(test_dna)
    # 提示: is_valid = is_valid_dna(test_dna)
    # 提示: rna = dna_to_rna(test_dna)
    # 提示: print(f"序列长度: {length}")
    # 提示: print(f"是否有效: {is_valid}")
    # 提示: print(f"RNA序列: {rna}")
    # 在下面写你的代码：
    
    
    pass  # 完成TODO后可以删除这行

# ========== 练习7：文件操作 ==========
def practice_7_file_operations():
    """
    练习7: 文件操作
    
    目标: 学习创建、写入和读取文件
    难度: ⭐⭐⭐⭐（中等偏难）
    
    实际应用：
    生物信息学大量工作涉及文件读写（FASTA, CSV等）
    """
    print("\n" + "="*50)
    print("🔍 练习7: 文件操作")
    print("="*50)
    
    filename = "my_first_sequence.txt"
    dna_sequence = "ATCGATCGATCGATCG"
    
    # TODO 7.1: 将DNA序列写入文件
    # 提示: 使用with语句和open函数
    # with open(filename, 'w') as f:
    #     f.write(f">Sequence_1\n")  # FASTA格式的标题
    #     f.write(dna_sequence)
    # print(f"✅ 文件 {filename} 创建成功！")
    # 在下面写你的代码：
    
    
    # TODO 7.2: 从文件读取内容
    # 提示:
    # with open(filename, 'r') as f:
    #     content = f.read()
    # print(f"文件内容:\n{content}")
    # 在下面写你的代码：
    
    
    # TODO 7.3: 追加内容到文件
    # 提示: 使用 'a' 模式（append）
    # with open(filename, 'a') as f:
    #     f.write(f"\n>Sequence_2\n")
    #     f.write("GCGCGCGCGCGC")
    # print("✅ 新序列已添加！")
    # 在下面写你的代码：
    
    
    # TODO 7.4: 删除文件（清理）
    # 提示: 使用os.remove()
    # if os.path.exists(filename):
    #     os.remove(filename)
    #     print(f"✅ 文件 {filename} 已删除")
    # 在下面写你的代码：
    
    
    pass  # 完成TODO后可以删除这行

# ========== 练习8：综合练习 ==========
def practice_8_integration():
    """
    练习8: 综合练习 - 简单的序列分析工具
    
    目标: 综合运用所学知识
    难度: ⭐⭐⭐⭐⭐（有挑战）
    
    任务：创建一个分析DNA序列的小程序
    """
    print("\n" + "="*50)
    print("🔍 练习8: 综合练习 - 序列分析器")
    print("="*50)
    
    # TODO 8.1: 定义一个综合的序列分析函数
    # 这个函数应该：
    # 1. 验证序列是否有效
    # 2. 计算序列长度
    # 3. 计算GC含量
    # 4. 转换为RNA
    # 5. 返回一个包含所有信息的字典
    
    # 提示：函数框架
    # def analyze_sequence(sequence):
    #     """分析DNA序列的综合函数"""
    #     # 转大写
    #     sequence = sequence.upper()
    #     
    #     # 验证序列
    #     valid_bases = set('ATCG')
    #     is_valid = all(base in valid_bases for base in sequence)
    #     
    #     if not is_valid:
    #         return {"error": "Invalid DNA sequence"}
    #     
    #     # 计算各种属性
    #     length = len(sequence)
    #     gc_count = sequence.count('G') + sequence.count('C')
    #     gc_content = (gc_count / length * 100) if length > 0 else 0
    #     rna = sequence.replace('T', 'U')
    #     
    #     # 返回结果字典
    #     return {
    #         "sequence": sequence,
    #         "length": length,
    #         "gc_content": gc_content,
    #         "rna": rna,
    #         "at_content": 100 - gc_content
    #     }
    # 在下面写你的函数：
    
    
    # 测试序列
    test_sequences = [
        "ATCGATCG",
        "GGCCGGCC",
        "ATATATATATAT",
        "INVALID123"  # 无效序列
    ]
    
    # TODO 8.2: 分析每个序列并打印结果
    # 提示:
    # for seq in test_sequences:
    #     print(f"\n分析序列: {seq}")
    #     result = analyze_sequence(seq)
    #     
    #     if "error" in result:
    #         print(f"  ❌ 错误: {result['error']}")
    #     else:
    #         print(f"  长度: {result['length']} bp")
    #         print(f"  GC含量: {result['gc_content']:.1f}%")
    #         print(f"  AT含量: {result['at_content']:.1f}%")
    #         print(f"  RNA: {result['rna']}")
    # 在下面写你的代码：
    
    
    pass  # 完成TODO后可以删除这行

# ========== 主函数：运行所有练习 ==========
def main():
    """
    主函数: 运行所有练习
    """
    print("="*60)
    print("🧬 Chapter 00 渐进式练习题")
    print("="*60)
    print("\n提示：")
    print("1. 从练习0开始，逐步完成")
    print("2. 每个练习都有详细的提示")
    print("3. 完成一个练习后再做下一个")
    print("4. 遇到困难时查看practice_solution.py")
    
    # 运行所有练习
    practice_0_warmup()
    practice_1_hello_world()
    practice_2_variables()
    practice_3_basic_calculation()
    practice_4_modules()
    practice_5_conditions()
    practice_6_functions()
    practice_7_file_operations()
    practice_8_integration()
    
    print("\n" + "="*60)
    print("🎯 练习完成检查清单：")
    print("="*60)
    print("□ 练习0: 确认环境正常")
    print("□ 练习1: Hello World输出")
    print("□ 练习2: 变量的创建和使用")
    print("□ 练习3: GC含量计算")
    print("□ 练习4: 模块的使用")
    print("□ 练习5: 条件判断")
    print("□ 练习6: 函数定义")
    print("□ 练习7: 文件操作")
    print("□ 练习8: 综合应用")
    print("\n如果都完成了，恭喜你掌握了Python基础！")
    print("准备好进入Chapter 01的学习了！")

if __name__ == "__main__":
    main()