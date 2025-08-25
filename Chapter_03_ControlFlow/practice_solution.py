#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 03 练习参考答案：控制流应用

这里提供了所有练习题的参考答案，包括：
- 完整的代码实现
- 详细的注释说明
- 最佳实践建议

💡 学习建议：
1. 先尝试自己解决，再看答案
2. 理解每个解答的思路
3. 思考如何优化和改进

记住：编程没有唯一正确答案，重要的是理解思路！
"""


def solution_1_quality_filter():
    """
    练习1参考答案：序列质量过滤 ⭐
    
    展示基础的if条件判断和for循环使用
    """
    print("=" * 60)
    print("练习1：序列质量过滤 ⭐ - 参考答案")
    print("=" * 60)
    
    # 测试数据
    sequences = [
        {"id": "read001", "seq": "ATGCGATCGATC", "quality": 38},
        {"id": "read002", "seq": "NATGNNNATCNN", "quality": 25},
        {"id": "read003", "seq": "GCGATCGATCGA", "quality": 41},
        {"id": "read004", "seq": "NNATGCGANNNN", "quality": 32},
        {"id": "read005", "seq": "ATGCGATCGNAT", "quality": 35},
    ]
    
    # 过滤标准
    min_quality = 30
    max_n_percent = 10
    
    print(f"质控标准: 质量≥{min_quality}, N含量≤{max_n_percent}%")
    print("-" * 40)
    
    # 存储结果
    passed = []
    failed = []
    
    # 遍历每条序列
    for seq in sequences:
        seq_id = seq["id"]
        sequence = seq["seq"]
        quality = seq["quality"]
        
        # 计算N含量
        n_count = sequence.count('N')
        n_percent = (n_count / len(sequence)) * 100
        
        print(f"{seq_id}: Q{quality}, N={n_percent:.1f}%", end=" → ")
        
        # 质量检查
        if quality >= min_quality and n_percent <= max_n_percent:
            passed.append(seq_id)
            print("✅ 通过")
        else:
            failed.append(seq_id)
            reasons = []
            if quality < min_quality:
                reasons.append("质量低")
            if n_percent > max_n_percent:
                reasons.append("N太多")
            print(f"❌ 失败 ({', '.join(reasons)})")
    
    # 统计结果
    total = len(sequences)
    pass_rate = len(passed) / total * 100
    
    print(f"\n📊 统计结果:")
    print(f"  通过: {len(passed)}/{total} ({pass_rate:.1f}%)")
    print(f"  通过的序列: {passed}")


def solution_2_restriction_sites():
    """
    练习2参考答案：限制性酶切位点搜索 ⭐⭐
    
    展示字符串模式匹配和位置记录
    """
    print("\n" + "=" * 60)
    print("练习2：限制性酶切位点搜索 ⭐⭐ - 参考答案")
    print("=" * 60)
    
    # 质粒序列
    plasmid = "CGGAATTCATGGATCCTAGAATTCGCGGATCCAAGAATTC"
    
    # 限制酶识别序列
    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
    }
    
    print(f"质粒序列 ({len(plasmid)} bp):")
    print(plasmid)
    print("-" * 40)
    
    # 存储所有找到的位点
    all_sites = []
    
    # 搜索每种酶的位点
    for enzyme, site in enzymes.items():
        print(f"\n搜索 {enzyme} ({site}):")
        
        positions = []
        # 方法1：使用find()方法
        pos = plasmid.find(site)
        while pos != -1:
            positions.append(pos)
            pos = plasmid.find(site, pos + 1)
        
        # 输出结果
        if positions:
            print(f"  找到 {len(positions)} 个位点: {positions}")
            for pos in positions:
                # 显示上下文
                start = max(0, pos - 3)
                end = min(len(plasmid), pos + len(site) + 3)
                context = plasmid[start:pos] + f"[{site}]" + plasmid[pos + len(site):end]
                print(f"    位置 {pos}: ...{context}...")
                all_sites.append((pos, enzyme))
        else:
            print("  未找到位点")
    
    # 按位置排序所有位点
    all_sites.sort()
    
    # 计算片段大小
    if len(all_sites) > 1:
        print(f"\n📊 酶切分析:")
        print(f"  总切点数: {len(all_sites)}")
        print(f"  产生片段数: {len(all_sites) + 1}")
        
        # 计算片段大小
        fragments = []
        prev_pos = 0
        
        for pos, enzyme in all_sites:
            fragment_size = pos - prev_pos
            if fragment_size > 0:
                fragments.append(fragment_size)
            prev_pos = pos + 6  # 切点后移6bp（识别序列长度）
        
        # 最后一个片段
        final_fragment = len(plasmid) - prev_pos
        if final_fragment > 0:
            fragments.append(final_fragment)
        
        print(f"  片段大小: {fragments} bp")


def solution_3_orf_finder():
    """
    练习3参考答案：ORF预测器 ⭐⭐⭐
    
    展示嵌套循环和break控制
    """
    print("\n" + "=" * 60)
    print("练习3：ORF预测器 ⭐⭐⭐ - 参考答案")
    print("=" * 60)
    
    # DNA序列
    dna = "CGATGAAACCCTAGATGGGGTAACGATGCCCTGAATGAAATAACCC"
    
    print(f"DNA序列 ({len(dna)} bp):")
    print(dna)
    print("-" * 40)
    
    # 终止密码子
    stop_codons = ["TAA", "TAG", "TGA"]
    
    # 存储所有找到的ORF
    all_orfs = []
    
    # 在三个阅读框中搜索
    for frame in range(3):
        print(f"\n阅读框 {frame}:")
        frame_orfs = []
        
        # 搜索ATG起始密码子
        i = frame
        while i <= len(dna) - 3:
            codon = dna[i:i+3]
            
            if codon == "ATG":
                # 从ATG开始找终止密码子
                j = i + 3
                while j <= len(dna) - 3:
                    stop_codon = dna[j:j+3]
                    
                    if stop_codon in stop_codons:
                        # 找到完整的ORF
                        orf_start = i
                        orf_end = j + 3
                        orf_length = orf_end - orf_start
                        orf_seq = dna[orf_start:orf_end]
                        aa_length = orf_length // 3 - 1  # 减去终止密码子
                        
                        orf_info = {
                            'frame': frame,
                            'start': orf_start,
                            'end': orf_end,
                            'length': orf_length,
                            'sequence': orf_seq,
                            'amino_acids': aa_length
                        }
                        
                        frame_orfs.append(orf_info)
                        all_orfs.append(orf_info)
                        
                        print(f"  ORF: {orf_start}-{orf_end} ({orf_length}bp, {aa_length}aa)")
                        print(f"       {orf_seq}")
                        
                        # 跳到ORF结束位置
                        i = j + 3
                        break
                    
                    j += 3
                else:
                    # 没找到终止密码子
                    i += 3
            else:
                i += 3
        
        if not frame_orfs:
            print("  未找到完整的ORF")
    
    # 找出最长的ORF
    if all_orfs:
        longest_orf = max(all_orfs, key=lambda x: x['length'])
        
        print(f"\n🏆 最长ORF:")
        print(f"  阅读框: {longest_orf['frame']}")
        print(f"  位置: {longest_orf['start']}-{longest_orf['end']}")
        print(f"  长度: {longest_orf['length']} bp")
        print(f"  氨基酸: {longest_orf['amino_acids']} 个")
        print(f"  序列: {longest_orf['sequence']}")


def solution_4_gc_sliding_window():
    """
    练习4参考答案：滑动窗口GC分析 ⭐⭐
    
    展示滑动窗口技术
    """
    print("\n" + "=" * 60)
    print("练习4：滑动窗口GC分析 ⭐⭐ - 参考答案")
    print("=" * 60)
    
    # 测试序列
    dna = "GCGCGCGCGCGCATATATATATATATATCGCGCGCGCGCGATATATATA"
    window_size = 10
    
    print(f"DNA序列 ({len(dna)} bp):")
    print(dna)
    print(f"窗口大小: {window_size} bp")
    print("-" * 40)
    
    # 存储窗口结果
    windows = []
    
    # 滑动窗口分析
    print("\n滑动窗口分析:")
    for i in range(len(dna) - window_size + 1):
        window = dna[i:i+window_size]
        gc_count = window.count('G') + window.count('C')
        gc_percent = (gc_count / window_size) * 100
        
        windows.append({
            'position': i,
            'sequence': window,
            'gc_percent': gc_percent
        })
        
        # 显示前10个窗口
        if i < 10:
            print(f"  位置 {i:2d}: {window} GC={gc_percent:5.1f}%")
    
    # 统计分析
    gc_values = [w['gc_percent'] for w in windows]
    max_gc = max(gc_values)
    min_gc = min(gc_values)
    avg_gc = sum(gc_values) / len(gc_values)
    
    print(f"\n📊 GC含量统计:")
    print(f"  最高GC: {max_gc:.1f}%")
    print(f"  最低GC: {min_gc:.1f}%")
    print(f"  平均GC: {avg_gc:.1f}%")
    
    # 找到极值窗口
    max_window = max(windows, key=lambda x: x['gc_percent'])
    min_window = min(windows, key=lambda x: x['gc_percent'])
    
    print(f"\n🔍 极值窗口:")
    print(f"  GC最高: 位置{max_window['position']} {max_window['sequence']} ({max_window['gc_percent']:.1f}%)")
    print(f"  GC最低: 位置{min_window['position']} {min_window['sequence']} ({min_window['gc_percent']:.1f}%)")
    
    # 识别CpG岛候选
    cpg_islands = [w for w in windows if w['gc_percent'] > 60]
    
    if cpg_islands:
        print(f"\n🏝️ CpG岛候选 (GC>60%): {len(cpg_islands)} 个窗口")
        for island in cpg_islands[:3]:  # 只显示前3个
            print(f"  位置{island['position']:2d}: {island['sequence']} ({island['gc_percent']:.1f}%)")


def solution_5_codon_usage():
    """
    练习5参考答案：密码子使用频率统计 ⭐⭐⭐
    
    展示字典使用和统计分析
    """
    print("\n" + "=" * 60)
    print("练习5：密码子使用频率统计 ⭐⭐⭐ - 参考答案")
    print("=" * 60)
    
    # 编码序列
    cds = "ATGCCCATGAAATGGATGTTTAAATAGATGCCCATGAAATAGATGAAA"
    
    print(f"CDS序列 ({len(cds)} bp):")
    print(cds)
    print(f"密码子数: {len(cds)//3}")
    print("-" * 40)
    
    # 统计密码子使用
    codon_count = {}
    total_codons = 0
    
    # 提取并统计密码子
    print("\n密码子提取:")
    for i in range(0, len(cds) - 2, 3):
        codon = cds[i:i+3]
        if len(codon) == 3:
            total_codons += 1
            if codon in codon_count:
                codon_count[codon] += 1
            else:
                codon_count[codon] = 1
            
            # 显示前10个密码子
            if i < 30:
                print(f"  位置 {i:2d}: {codon}")
    
    # 计算频率
    print(f"\n📊 密码子使用统计:")
    print(f"  不同密码子种类: {len(codon_count)}")
    print(f"  总密码子数: {total_codons}")
    
    # 按使用次数排序
    sorted_codons = sorted(codon_count.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n密码子使用频率:")
    print("  密码子  次数  频率")
    print("  " + "-" * 18)
    
    for codon, count in sorted_codons:
        frequency = (count / total_codons) * 100
        print(f"    {codon}    {count:2d}   {frequency:5.1f}%")
    
    # 找出最常用和最少用的密码子
    most_common = sorted_codons[0]
    least_common = sorted_codons[-1]
    
    print(f"\n🏆 使用统计:")
    print(f"  最常用: {most_common[0]} (使用{most_common[1]}次)")
    print(f"  最少用: {least_common[0]} (使用{least_common[1]}次)")


def solution_comprehensive_analysis():
    """
    综合应用参考答案：序列质控分析系统
    
    综合使用所有控制流知识
    """
    print("\n" + "=" * 60)
    print("综合应用：序列质控分析系统 - 参考答案")
    print("=" * 60)
    
    # 模拟数据
    sequences = [
        {"id": "READ001", "seq": "ATGGCGATCGATCGATCGTAG", "qual": 38},
        {"id": "READ002", "seq": "NATGCCNNNATCGATCGATCG", "qual": 25},
        {"id": "READ003", "seq": "ATGAAACCCTAGATGGGGTAA", "qual": 42},
        {"id": "READ004", "seq": "CCGATGGCGATCGATCGATCG", "qual": 35},
    ]
    
    print(f"输入数据: {len(sequences)} 条序列")
    print("分析流程: 质量过滤 → GC分析 → motif搜索")
    print("-" * 40)
    
    # 分析参数
    min_quality = 30
    max_n_percent = 10
    target_motif = "GATC"
    
    # 步骤1: 质量过滤
    print("\n步骤1: 质量过滤")
    passed_qc = []
    
    for seq_data in sequences:
        seq_id = seq_data["id"]
        sequence = seq_data["seq"]
        quality = seq_data["qual"]
        
        # 质量检查
        n_percent = (sequence.count('N') / len(sequence)) * 100
        
        if quality >= min_quality and n_percent <= max_n_percent:
            passed_qc.append(seq_data)
            print(f"  ✅ {seq_id}: Q{quality}, N={n_percent:.1f}% - 通过")
        else:
            print(f"  ❌ {seq_id}: Q{quality}, N={n_percent:.1f}% - 失败")
    
    print(f"  质控通过: {len(passed_qc)}/{len(sequences)}")
    
    # 步骤2: GC含量分析
    print("\n步骤2: GC含量分析")
    for seq_data in passed_qc:
        seq_id = seq_data["id"]
        sequence = seq_data["seq"]
        
        gc_count = sequence.count('G') + sequence.count('C')
        gc_percent = (gc_count / len(sequence)) * 100
        
        print(f"  {seq_id}: GC含量 {gc_percent:.1f}%")
    
    # 步骤3: motif搜索
    print(f"\n步骤3: 搜索motif '{target_motif}'")
    motif_found = []
    
    for seq_data in passed_qc:
        seq_id = seq_data["id"]
        sequence = seq_data["seq"]
        
        if target_motif in sequence:
            # 找到所有位置
            positions = []
            pos = sequence.find(target_motif)
            while pos != -1:
                positions.append(pos)
                pos = sequence.find(target_motif, pos + 1)
            
            motif_found.append(seq_id)
            print(f"  ✅ {seq_id}: 发现{len(positions)}个motif，位置: {positions}")
        else:
            print(f"  ❌ {seq_id}: 未发现motif")
    
    # 最终报告
    print(f"\n📈 最终分析报告:")
    print(f"  原始序列: {len(sequences)}")
    print(f"  质控通过: {len(passed_qc)}")
    print(f"  含motif: {len(motif_found)}")
    print(f"  高质量序列ID: {[s['id'] for s in passed_qc]}")
    print(f"  含motif序列ID: {motif_found}")


def main():
    """主函数：运行所有答案演示"""
    print("=" * 70)
    print("Chapter 03 控制流练习 - 参考答案")
    print("=" * 70)
    
    print("\n📚 参考答案说明：")
    print("• 每个答案都有详细的实现和注释")
    print("• 展示了最佳实践和常见技巧")
    print("• 可能的解法不止一种，重要的是理解思路")
    print("• 建议先完成练习再查看答案")
    
    print("\n🎯 学习要点：")
    print("• if语句: 条件判断的逻辑组合")
    print("• for循环: 遍历序列和统计计算")
    print("• while循环: 搜索和迭代算法")
    print("• 流程控制: break、continue的合理使用")
    print("• 综合应用: 多种控制结构的协同工作")
    
    input("\n按Enter开始查看答案...")
    
    # 运行所有答案
    solution_1_quality_filter()
    input("\n按Enter继续...")
    
    solution_2_restriction_sites()
    input("\n按Enter继续...")
    
    solution_3_orf_finder()
    input("\n按Enter继续...")
    
    solution_4_gc_sliding_window()
    input("\n按Enter继续...")
    
    solution_5_codon_usage()
    input("\n按Enter继续...")
    
    solution_comprehensive_analysis()
    
    print("\n" + "=" * 70)
    print("📝 学习总结")
    print("=" * 70)
    
    print("\n✅ 掌握的核心技能：")
    print("  • 条件判断：if/elif/else的灵活使用")
    print("  • 循环遍历：for循环处理序列数据")
    print("  • 模式搜索：在序列中查找特定模式")
    print("  • 统计分析：使用字典进行计数和频率分析")
    print("  • 滑动窗口：固定窗口的序列分析")
    print("  • 流程控制：break/continue优化执行流程")
    
    print("\n🚀 进阶建议：")
    print("  • 尝试优化代码性能")
    print("  • 处理更大规模的数据")
    print("  • 增加错误处理机制")
    print("  • 使用函数封装重复代码")
    
    print("\n" + "=" * 70)
    print("🎉 恭喜完成Chapter 03的学习！")
    print("下一章将学习函数 - 让代码更模块化")
    print("=" * 70)


if __name__ == "__main__":
    main()