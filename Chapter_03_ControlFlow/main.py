#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 03: 控制流 - 给程序装上"大脑"的决策系统

生物学场景：从简单判断到复杂分析流程

📚 本章演示内容：
1. if语句 - 程序的决策能力
2. for循环 - 批量处理利器
3. while循环 - 条件监测器
4. 流程控制 - break、continue、pass
5. 综合应用 - 构建完整分析系统

💡 编程思维：
控制流让程序从"机械执行"变成"智能决策"
就像经验丰富的实验员，知道何时做什么决策。
"""


def demo_if_statements():
    """
    演示1：if语句的核心应用场景
    
    生物学背景：实验室中充满决策点，
    每个判断都影响后续流程。
    """
    print("=" * 60)
    print("🎭 演示1：if语句 - 让程序学会判断")
    print("=" * 60)
    
    # 1.1 单分支if
    print("\n📌 PCR产物长度检查")
    pcr_product = "ATGCGATCGATCGATCGATCGATCG"
    expected_length = 25
    
    print(f"实际长度: {len(pcr_product)} bp")
    if len(pcr_product) == expected_length:
        print("✅ PCR成功！产物长度正确")
    
    # 1.2 双分支if-else
    print("\n📌 酶切位点检查")
    plasmid = "ATGCGAATTCGATCG"
    ecori_site = "GAATTC"
    
    if ecori_site in plasmid:
        position = plasmid.find(ecori_site)
        print(f"✅ 发现EcoRI位点在位置 {position}")
    else:
        print("❌ 未发现EcoRI位点，需要选择其他限制酶")
    
    # 1.3 多分支if-elif-else
    print("\n📌 测序质量分级")
    samples = [42, 35, 25, 15]
    
    for q_score in samples:
        print(f"Q{q_score}: ", end="")
        if q_score >= 40:
            print("极高质量")
        elif q_score >= 30:
            print("高质量")
        elif q_score >= 20:
            print("中等质量")
        else:
            print("低质量")
    
    # 1.4 复合条件
    print("\n📌 引物设计标准")
    primer = "ATGGCGATCGATCGATCGAT"
    length = len(primer)
    gc_content = (primer.count('G') + primer.count('C')) / length * 100
    
    print(f"引物: {primer}")
    print(f"长度: {length} bp, GC: {gc_content:.1f}%")
    
    if 18 <= length <= 25 and 40 <= gc_content <= 60:
        print("✅ 引物设计合格")
    else:
        print("❌ 引物需要重新设计")


def demo_for_loops():
    """
    演示2：for循环的批量处理能力
    
    生物学背景：实验室的重复操作，
    如96孔板加样、批量样品处理。
    """
    print("\n" + "=" * 60)
    print("🔄 演示2：for循环 - 批量处理的利器")
    print("=" * 60)
    
    # 2.1 基础遍历
    print("\n📌 碱基逐个分析")
    dna = "ATGCGATCG"
    
    print(f"分析序列: {dna}")
    for base in dna:
        bond_type = "2个氢键" if base in "AT" else "3个氢键"
        print(f"  {base} - {bond_type}")
    
    # 2.2 批量样品处理
    print("\n📌 批量DNA标准化")
    samples = ["Sample_A", "Sample_B", "Sample_C"]
    concentrations = [150, 230, 180]  # ng/μL
    
    for i in range(len(samples)):
        dilution = concentrations[i] / 100  # 目标：100 ng/μL
        print(f"{samples[i]}: {concentrations[i]} ng/μL → 稀释{dilution:.1f}x")
    
    # 2.3 range函数
    print("\n📌 PCR扩增模拟")
    copies = 100
    for cycle in range(1, 6):
        copies *= 2
        print(f"第{cycle}轮循环: {copies:,} 个拷贝")
    
    # 2.4 嵌套循环
    print("\n📌 三阅读框扫描")
    dna = "CCATGGCATGAAATGTAG"
    
    for frame in range(3):
        print(f"阅读框 {frame}:", end=" ")
        found_atg = False
        for i in range(frame, len(dna) - 2, 3):
            codon = dna[i:i+3]
            if len(codon) == 3 and codon == "ATG":
                print(f"ATG@{i}", end=" ")
                found_atg = True
        if not found_atg:
            print("无ATG", end="")
        print()
    
    # 2.5 列表推导式
    print("\n📌 列表推导式")
    sequences = ["ATGC", "CGTA", "GGCC"]
    
    print("原始序列:", sequences)
    reverse_seqs = [seq[::-1] for seq in sequences]
    print("反向序列:", reverse_seqs)
    
    gc_rich = [seq for seq in sequences 
               if (seq.count('G') + seq.count('C'))/len(seq) > 0.5]
    print("GC>50%:", gc_rich)


def demo_while_loops():
    """
    演示3：while循环的条件监测
    
    生物学背景：需要持续监测的实验条件，
    如细胞培养、透析进度等。
    """
    print("\n" + "=" * 60)
    print("⏰ 演示3：while循环 - 条件监测器")
    print("=" * 60)
    
    # 3.1 序列搜索
    print("\n📌 搜索第一个ATG")
    sequence = "CCGATCCATGAAATGCCCTAG"
    position = 0
    
    print(f"搜索序列: {sequence}")
    while position <= len(sequence) - 3:
        if sequence[position:position+3] == "ATG":
            print(f"✓ 找到ATG在位置 {position}")
            break
        position += 1
    else:
        print("未找到ATG")
    
    # 3.2 迭代优化
    print("\n📌 寻找最佳pH（二分法）")
    ph_low, ph_high = 6.0, 8.0
    target_activity = 95
    iteration = 0
    
    print("目标: 找到酶活性≥95%的pH")
    
    while ph_high - ph_low > 0.5 and iteration < 5:
        iteration += 1
        ph_mid = (ph_low + ph_high) / 2
        
        # 模拟酶活性（最佳pH是7.2）
        activity = 100 - abs(ph_mid - 7.2) * 50
        
        print(f"  迭代{iteration}: pH={ph_mid:.1f}, 活性={activity:.1f}%")
        
        if activity >= target_activity:
            print(f"找到最佳pH: {ph_mid:.1f}")
            break
        elif ph_mid < 7.2:
            ph_low = ph_mid
        else:
            ph_high = ph_mid
    
    # 3.3 培养监测
    print("\n📌 细胞培养模拟")
    cells = 10000
    target = 100000
    hours = 0
    
    print(f"初始: {cells:,} 个细胞，目标: {target:,}")
    
    while cells < target:
        hours += 24  # 每天检查
        cells *= 2   # 每天翻倍
        print(f"  {hours}h: {cells:,} 个细胞")
        if hours >= 120:  # 最多5天
            break
    
    print(f"培养{hours/24:.1f}天完成")


def demo_flow_control():
    """
    演示4：流程控制语句
    
    展示break、continue、pass的使用场景
    """
    print("\n" + "=" * 60)
    print("🎮 演示4：流程控制 - break、continue、pass")
    print("=" * 60)
    
    # 4.1 break：找到就停止
    print("\n📌 break：基因库搜索")
    databases = {
        "GenBank": ["BRCA1", "TP53", "EGFR"],
        "RefSeq": ["MYC", "KRAS", "BRCA2"],
        "Ensembl": ["BRAF", "BRCA1", "APC"]
    }
    
    target = "BRCA1"
    print(f"搜索基因: {target}")
    
    found = False
    for db_name, genes in databases.items():
        print(f"  搜索 {db_name}...", end=" ")
        if target in genes:
            print("找到了！")
            found = True
            break
        print("未找到")
    
    # 4.2 continue：跳过无效数据
    print("\n📌 continue：质量过滤")
    reads = [
        {"id": "read1", "quality": 35},
        {"id": "read2", "quality": 15},  # 低质量
        {"id": "read3", "quality": 38},
    ]
    
    processed = 0
    for read in reads:
        if read["quality"] < 30:
            print(f"  ⚠️ 跳过{read['id']}: 质量太低")
            continue
        
        print(f"  ✅ 处理{read['id']}: Q{read['quality']}")
        processed += 1
    
    print(f"处理了 {processed} 条序列")
    
    # 4.3 pass：占位符
    print("\n📌 pass：程序框架")
    
    def analyze_sequence(seq):
        print(f"分析序列: {seq}")
        
        if len(seq) < 10:
            print("  序列太短")
            pass  # TODO: 详细检查
        else:
            print("  长度合格")
        
        # TODO: 更多分析步骤
        pass
        
        return "分析完成"
    
    result = analyze_sequence("ATGCGATC")
    print(f"结果: {result}")


def demo_comprehensive_analysis():
    """
    演示5：综合应用 - 序列质控分析系统
    
    综合使用所有控制流结构
    """
    print("\n" + "=" * 60)
    print("🔧 演示5：综合应用 - 序列质控系统")
    print("=" * 60)
    
    # 模拟数据
    sequences = [
        {"id": "READ001", "seq": "ATGGCGATCGATCGATCGTAG", "qual": 38},
        {"id": "READ002", "seq": "NATGCCNNNATCGATCGATCG", "qual": 25},
        {"id": "READ003", "seq": "ATGAAACCCTAGATGGGGTAA", "qual": 42},
        {"id": "READ004", "seq": "CCGATGGCGATCGATCGATCG", "qual": 35},
    ]
    
    # 分析参数
    min_quality = 30
    max_n_percent = 10
    target_motif = "GATC"
    
    print(f"分析参数: Q≥{min_quality}, N≤{max_n_percent}%, 搜索motif: {target_motif}")
    
    # 结果统计
    passed = []
    motif_found = []
    
    # 主分析循环
    for seq_data in sequences:
        seq_id = seq_data["id"]
        sequence = seq_data["seq"]
        quality = seq_data["qual"]
        
        print(f"\n分析 {seq_id} (Q{quality}):")
        
        # 质量检查
        if quality < min_quality:
            print("  ❌ 质量太低")
            continue
        
        # N含量检查
        n_percent = (sequence.count('N') / len(sequence)) * 100
        if n_percent > max_n_percent:
            print(f"  ❌ N含量过高 ({n_percent:.1f}%)")
            continue
        
        print("  ✅ 通过质控")
        passed.append(seq_id)
        
        # 计算GC含量
        gc = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        print(f"  📊 GC含量: {gc:.1f}%")
        
        # 搜索motif
        if target_motif in sequence:
            print(f"  🔍 发现motif: {target_motif}")
            motif_found.append(seq_id)
    
    # 生成报告
    print(f"\n📈 分析报告:")
    print(f"  通过质控: {len(passed)}/{len(sequences)}")
    print(f"  含motif: {len(motif_found)} 条")
    print(f"  高质量ID: {passed}")
    
    return passed


def main():
    """主函数：运行所有演示"""
    print("=" * 70)
    print("  🧬 Chapter 03: 控制流 - 程序的决策系统")
    print("=" * 70)
    
    print("\n📚 本章演示：")
    print("  1. if语句 - 程序决策能力")
    print("  2. for循环 - 批量处理利器")
    print("  3. while循环 - 条件监测器")
    print("  4. 流程控制 - break、continue、pass")
    print("  5. 综合应用 - 完整分析系统")
    
    input("\n按Enter开始学习...")
    
    # 运行所有演示
    demo_if_statements()
    input("\n按Enter继续...")
    
    demo_for_loops()
    input("\n按Enter继续...")
    
    demo_while_loops()
    input("\n按Enter继续...")
    
    demo_flow_control()
    input("\n按Enter继续...")
    
    demo_comprehensive_analysis()
    
    # 总结
    print("\n" + "=" * 70)
    print("📚 知识要点总结")
    print("=" * 70)
    
    print("\n🎯 核心概念:")
    print("  • if语句: 单分支、双分支、多分支、复合条件")
    print("  • for循环: 序列遍历、range函数、嵌套循环、列表推导")
    print("  • while循环: 条件监测、迭代优化、培养监控")
    print("  • 流程控制: break停止、continue跳过、pass占位")
    
    print("\n💡 实际应用:")
    print("  • 序列质量控制和筛选")
    print("  • 批量样品处理分析")
    print("  • 基因预测和注释")
    print("  • 实验条件优化")
    
    print("\n🚀 下一步:")
    print("  1. 完成practice.py中的练习")
    print("  2. 尝试修改参数观察结果")
    print("  3. 查看practice_solution.py学习最佳实践")
    
    print("\n" + "=" * 70)
    print("🎉 Chapter 03 完成！下一章学习函数模块化")
    print("=" * 70)


if __name__ == "__main__":
    main()