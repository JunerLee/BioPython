#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 01: Python基础 - 像处理DNA一样学编程

这是你的第一个Python程序！我们将通过计算DNA序列的GC含量来学习Python基础。
就像在实验室中分析DNA样品一样，我们将一步步进行。

作者：BioPython教程
目标读者：没有编程经验的生物学研究者
"""


def lesson_1_variables_as_test_tubes():
    """
    第1课：变量就像试管
    
    在实验室中，你用试管装样品，贴上标签。
    在Python中，你用变量装数据，给它起名字。
    """
    print("\n" + "="*60)
    print("第1课：变量 = 试管")
    print("="*60)
    
    # 这是你的第一个变量！就像给试管贴标签
    my_first_dna = "ATCG"
    print("\n1. 创建第一个变量（装入试管）:")
    print(f"   my_first_dna = 'ATCG'")
    print(f"   变量名: my_first_dna")
    print(f"   变量值: {my_first_dna}")
    
    # 你可以有很多试管，装不同的东西
    print("\n2. 创建多个变量（多个试管）:")
    gene_name = "BRCA1"        # 试管1：基因名
    sample_id = "P001"         # 试管2：样品编号
    temperature = 37.5         # 试管3：温度值
    is_human = True           # 试管4：是否人类样品
    
    print(f"   基因名: {gene_name}")
    print(f"   样品编号: {sample_id}")
    print(f"   温度: {temperature}°C")
    print(f"   是人类样品: {is_human}")
    
    # 变量可以改变（就像更换试管内容）
    print("\n3. 修改变量值（更换试管内容）:")
    print(f"   原始DNA: {my_first_dna}")
    my_first_dna = "ATCGATCG"  # 放入新的DNA序列
    print(f"   新的DNA: {my_first_dna}")
    
    # 变量命名规则演示
    print("\n4. 变量命名规则（试管标签规范）:")
    print("   ✅ 好的命名:")
    human_dna = "ATCG"
    mouse_dna = "GCTA"
    experiment_001 = "PCR"
    print(f"      human_dna, mouse_dna, experiment_001")
    
    print("   ❌ 错误的命名（Python会报错）:")
    print("      1st_sample (不能以数字开头)")
    print("      my-dna (不能用减号)")
    print("      for (这是Python保留字)")


def lesson_2_data_types_as_molecules():
    """
    第2课：数据类型就像不同的生物分子
    
    实验室有DNA、RNA、蛋白质等不同分子。
    Python有字符串、数字、布尔值等不同数据类型。
    """
    print("\n" + "="*60)
    print("第2课：数据类型 = 不同的生物分子")
    print("="*60)
    
    # 字符串 - 像序列数据
    print("\n1. 字符串(str) - 文本数据，像DNA/RNA序列:")
    dna = "ATCGATCG"
    rna = "AUCGAUCG"
    protein = "MKVLWAALLVTFLAGCQA"
    
    print(f"   DNA序列: '{dna}' - 类型: {type(dna).__name__}")
    print(f"   RNA序列: '{rna}' - 类型: {type(rna).__name__}")
    print(f"   蛋白序列: '{protein}' - 类型: {type(protein).__name__}")
    
    # 整数 - 像计数结果
    print("\n2. 整数(int) - 整数，像碱基计数:")
    base_count = 8
    chromosome_number = 23
    read_length = 150
    
    print(f"   碱基数: {base_count} - 类型: {type(base_count).__name__}")
    print(f"   染色体数: {chromosome_number} - 类型: {type(chromosome_number).__name__}")
    print(f"   读长: {read_length} - 类型: {type(read_length).__name__}")
    
    # 浮点数 - 像测量值
    print("\n3. 浮点数(float) - 小数，像浓度或比例:")
    gc_content = 45.5
    ph_value = 7.4
    concentration = 2.5
    
    print(f"   GC含量: {gc_content}% - 类型: {type(gc_content).__name__}")
    print(f"   pH值: {ph_value} - 类型: {type(ph_value).__name__}")
    print(f"   浓度: {concentration} μg/μL - 类型: {type(concentration).__name__}")
    
    # 布尔值 - 像是/否的判断
    print("\n4. 布尔值(bool) - True/False，像实验结果:")
    is_valid_sequence = True
    has_mutation = False
    pcr_successful = True
    
    print(f"   序列有效: {is_valid_sequence} - 类型: {type(is_valid_sequence).__name__}")
    print(f"   有突变: {has_mutation} - 类型: {type(has_mutation).__name__}")
    print(f"   PCR成功: {pcr_successful} - 类型: {type(pcr_successful).__name__}")
    
    # 类型转换
    print("\n5. 类型转换（像分子转化）:")
    number_as_string = "42"
    number_as_int = int(number_as_string)
    print(f"   字符串'42' 转为整数: {number_as_int}")
    
    float_number = 3.14
    int_number = int(float_number)
    print(f"   浮点数3.14 转为整数: {int_number}")


def lesson_3_string_operations_step_by_step():
    """
    第3课：字符串操作 - 像在实验室编辑DNA序列
    
    学习如何像处理DNA一样处理字符串。
    每个操作都会详细展示过程和结果。
    """
    print("\n" + "="*60)
    print("第3课：字符串操作 = 序列编辑")
    print("="*60)
    
    # 从测序仪得到的原始数据
    print("\n实验场景：处理测序仪输出的DNA序列")
    print("-" * 40)
    
    raw_data = "atcgatcgatcg"  # 小写，像原始测序数据
    print(f"原始数据: '{raw_data}'")
    
    # 步骤1：标准化 - 转为大写
    print("\n步骤1：标准化序列（转大写）")
    print(f"   操作前: '{raw_data}'")
    clean_data = raw_data.upper()
    print(f"   操作后: '{clean_data}'")
    print(f"   使用方法: .upper()")
    
    # 步骤2：测量 - 获取长度
    print("\n步骤2：测量序列长度")
    length = len(clean_data)
    print(f"   序列: '{clean_data}'")
    print(f"   长度: {length} bp")
    print(f"   使用函数: len()")
    
    # 步骤3：计数 - 统计特定碱基
    print("\n步骤3：统计各碱基数量")
    print(f"   序列: '{clean_data}'")
    for base in ['A', 'T', 'C', 'G']:
        count = clean_data.count(base)
        print(f"   {base}的数量: {count}")
    print(f"   使用方法: .count()")
    
    # 步骤4：切片 - 获取序列片段
    print("\n步骤4：提取序列片段（像限制酶切割）")
    print(f"   完整序列: '{clean_data}'")
    print(f"   位置标记:  0123456789...")  # 帮助理解索引
    
    # 获取不同片段
    first_codon = clean_data[0:3]      # 前3个碱基
    last_codon = clean_data[-3:]       # 最后3个碱基
    middle = clean_data[3:6]           # 中间片段
    
    print(f"   前3个碱基 [0:3]: '{first_codon}'")
    print(f"   中间3个碱基 [3:6]: '{middle}'")
    print(f"   最后3个碱基 [-3:]: '{last_codon}'")
    
    # 步骤5：连接 - 添加接头序列
    print("\n步骤5：连接序列（像连接反应）")
    adaptor_5 = "GGG"  # 5'端接头
    adaptor_3 = "CCC"  # 3'端接头
    
    print(f"   原始序列: '{clean_data}'")
    print(f"   5'接头: '{adaptor_5}'")
    print(f"   3'接头: '{adaptor_3}'")
    
    full_sequence = adaptor_5 + clean_data + adaptor_3
    print(f"   连接后: '{full_sequence}'")
    print(f"   新长度: {len(full_sequence)} bp")
    
    # 步骤6：查找 - 搜索特定模式
    print("\n步骤6：查找序列模式")
    search_pattern = "TCG"
    print(f"   在序列 '{clean_data}' 中查找 '{search_pattern}'")
    
    if search_pattern in clean_data:
        position = clean_data.find(search_pattern)
        count = clean_data.count(search_pattern)
        print(f"   ✅ 找到! 首次出现位置: {position}")
        print(f"   出现次数: {count}")
    else:
        print(f"   ❌ 未找到该模式")


def lesson_4_progressive_gc_calculation():
    """
    第4课：渐进式学习GC含量计算
    
    从最简单的手动计算开始，逐步实现自动化。
    就像从手工实验到自动化仪器的过程。
    """
    print("\n" + "="*60)
    print("第4课：从手动到自动 - GC含量计算的进化")
    print("="*60)
    
    # 方法1：完全手动（像用眼睛数）
    print("\n方法1：完全手动计算（理解原理）")
    print("-" * 40)
    
    sequence = "ATCG"
    print(f"序列: {sequence}")
    print("手动数碱基:")
    print("  A - 1个")
    print("  T - 1个")
    print("  C - 1个")
    print("  G - 1个")
    
    # 手动计算
    gc_count_manual = 2  # C和G各1个，总共2个
    total_manual = 4
    gc_content_manual = (gc_count_manual / total_manual) * 100
    
    print(f"\n计算过程:")
    print(f"  GC数量 = 1(C) + 1(G) = {gc_count_manual}")
    print(f"  总数 = {total_manual}")
    print(f"  GC含量 = ({gc_count_manual}/{total_manual}) × 100 = {gc_content_manual}%")
    
    # 方法2：半自动（让Python帮忙数）
    print("\n方法2：半自动计算（使用Python函数）")
    print("-" * 40)
    
    sequence2 = "ATCGATCG"
    print(f"序列: {sequence2}")
    
    # Python帮我们数
    c_count = sequence2.count('C')
    g_count = sequence2.count('G')
    total = len(sequence2)
    
    print(f"Python帮我们数:")
    print(f"  C的数量: sequence2.count('C') = {c_count}")
    print(f"  G的数量: sequence2.count('G') = {g_count}")
    print(f"  总长度: len(sequence2) = {total}")
    
    # 我们只需要计算
    gc_content = ((c_count + g_count) / total) * 100
    
    print(f"\n计算过程:")
    print(f"  GC含量 = ({c_count} + {g_count})/{total} × 100")
    print(f"        = {c_count + g_count}/{total} × 100")
    print(f"        = {gc_content}%")
    
    # 方法3：完全自动（创建函数）
    print("\n方法3：完全自动化（创建GC含量分析仪）")
    print("-" * 40)
    
    def gc_analyzer(dna):
        """我们的GC含量自动分析仪"""
        # 显示分析过程
        print(f"[分析仪] 接收序列: {dna}")
        
        # 标准化
        dna = dna.upper()
        print(f"[分析仪] 标准化: {dna}")
        
        # 计数
        g = dna.count('G')
        c = dna.count('C')
        total = len(dna)
        print(f"[分析仪] G={g}, C={c}, 总长={total}")
        
        # 计算
        if total == 0:
            return 0
        gc = ((g + c) / total) * 100
        print(f"[分析仪] GC含量 = {gc:.1f}%")
        
        return gc
    
    # 测试多个序列
    test_sequences = [
        "ATCGATCG",      # 平衡序列
        "GGCCGGCC",      # 高GC
        "ATATATAT",      # 低GC
    ]
    
    print("\n测试自动分析仪:")
    for seq in test_sequences:
        print(f"\n分析序列 '{seq}':")
        result = gc_analyzer(seq)
        print(f"最终结果: {result:.1f}%")


def lesson_5_real_world_application():
    """
    第5课：真实应用 - 分析BRCA1基因片段
    
    使用真实的基因数据，展示完整的分析流程。
    """
    print("\n" + "="*60)
    print("第5课：真实应用 - 分析人类BRCA1基因")
    print("="*60)
    
    # BRCA1基因片段（真实序列）
    brca1 = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCC"
    
    print("\n研究背景:")
    print("BRCA1是重要的肿瘤抑制基因，其突变与乳腺癌风险相关。")
    print("我们来分析这个基因片段的序列特征。")
    
    print(f"\n原始序列（{len(brca1)} bp）:")
    print(brca1)
    
    # 步骤1：数据质量检查
    print("\n步骤1：数据质量检查")
    print("-" * 40)
    
    # 检查是否只包含有效碱基
    valid_bases = set('ATCG')
    sequence_bases = set(brca1.upper())
    
    print(f"序列中的字符: {sequence_bases}")
    print(f"有效DNA碱基: {valid_bases}")
    
    if sequence_bases.issubset(valid_bases):
        print("✅ 质量检查通过：序列只包含ATCG")
    else:
        invalid = sequence_bases - valid_bases
        print(f"❌ 发现无效字符: {invalid}")
    
    # 步骤2：基本统计
    print("\n步骤2：碱基组成统计")
    print("-" * 40)
    
    total_length = len(brca1)
    print(f"序列长度: {total_length} bp")
    
    # 统计每个碱基
    base_counts = {}
    for base in 'ATCG':
        count = brca1.count(base)
        percentage = (count / total_length) * 100
        base_counts[base] = {'count': count, 'percentage': percentage}
        print(f"{base}: {count:2d} 个 ({percentage:5.1f}%)")
    
    # 步骤3：GC含量分析
    print("\n步骤3：GC含量分析")
    print("-" * 40)
    
    gc_count = brca1.count('G') + brca1.count('C')
    at_count = brca1.count('A') + brca1.count('T')
    gc_content = (gc_count / total_length) * 100
    at_content = (at_count / total_length) * 100
    
    print(f"GC碱基总数: {gc_count}")
    print(f"AT碱基总数: {at_count}")
    print(f"GC含量: {gc_content:.1f}%")
    print(f"AT含量: {at_content:.1f}%")
    
    # 步骤4：序列特征分析
    print("\n步骤4：序列特征分析")
    print("-" * 40)
    
    # 检查起始密码子
    if brca1.startswith('ATG'):
        print("✅ 序列以ATG起始密码子开始")
    else:
        print("❌ 序列不以ATG开始")
    
    # GC含量分类
    if gc_content < 30:
        category = "低GC含量（<30%）"
        explanation = "可能是AT富集区域"
    elif gc_content < 45:
        category = "中等GC含量（30-45%）"
        explanation = "典型的人类基因组序列"
    elif gc_content < 60:
        category = "中高GC含量（45-60%）"
        explanation = "可能是功能活跃区域"
    else:
        category = "高GC含量（>60%）"
        explanation = "可能是CpG岛或启动子区域"
    
    print(f"GC含量分类: {category}")
    print(f"生物学意义: {explanation}")
    
    # 步骤5：可视化展示
    print("\n步骤5：结果可视化")
    print("-" * 40)
    
    # 用简单的文本图表展示碱基组成
    print("碱基组成柱状图:")
    for base in 'ATCG':
        count = base_counts[base]['count']
        bar = '█' * (count // 2)  # 每2个碱基用一个方块表示
        print(f"{base}: {bar} {count}")
    
    # 展示GC vs AT比例
    print("\nGC vs AT 比例:")
    gc_bar = '█' * int(gc_content // 2)
    at_bar = '█' * int(at_content // 2)
    print(f"GC: {gc_bar} {gc_content:.1f}%")
    print(f"AT: {at_bar} {at_content:.1f}%")


def main():
    """
    主程序：运行所有课程
    
    这是程序的入口点，依次运行所有教学内容。
    """
    print("="*60)
    print("Chapter 01: Python基础 - 像处理DNA一样学编程")
    print("="*60)
    print("\n欢迎来到Python生物信息学的世界！")
    print("我们将通过分析DNA序列来学习Python编程。")
    print("每一步都有详细解释，就像在实验室做实验一样。")
    
    # 运行所有课程
    lesson_1_variables_as_test_tubes()
    
    input("\n按Enter继续下一课...")
    lesson_2_data_types_as_molecules()
    
    input("\n按Enter继续下一课...")
    lesson_3_string_operations_step_by_step()
    
    input("\n按Enter继续下一课...")
    lesson_4_progressive_gc_calculation()
    
    input("\n按Enter继续下一课...")
    lesson_5_real_world_application()
    
    # 总结
    print("\n" + "="*60)
    print("🎉 恭喜完成第一章！")
    print("="*60)
    
    print("\n你已经学会了：")
    print("✅ 使用变量存储数据（像试管装样品）")
    print("✅ 理解不同数据类型（像不同的生物分子）")
    print("✅ 操作字符串（像编辑DNA序列）")
    print("✅ 计算GC含量（真实的生物信息学应用）")
    print("✅ 分析真实基因数据（BRCA1基因片段）")
    
    print("\n下一步：")
    print("1. 完成 practice.py 中的练习题")
    print("2. 对比 practice_solution.py 检查答案")
    print("3. 尝试分析你自己的DNA序列")
    
    print("\n记住：")
    print("编程就像做实验，需要：")
    print("- 耐心（实验不会一次成功）")
    print("- 练习（熟能生巧）")
    print("- 好奇心（探索新方法）")
    
    print("\n祝你学习愉快！🧬")


if __name__ == "__main__":
    # 这行代码的意思是：如果直接运行这个文件，就执行main()函数
    # 就像实验室的"开始"按钮
    main()