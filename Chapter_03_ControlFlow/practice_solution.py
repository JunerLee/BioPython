#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 03 练习参考答案：控制流应用

这里提供了所有练习题的详细参考答案，包括：
- 完整的代码实现
- 详细的注释说明
- 多种解决方案对比
- 最佳实践建议
- 性能优化技巧

💡 学习建议：
1. 先尝试自己解决，再看答案
2. 理解每个解答的思路
3. 比较不同的解决方案
4. 思考如何优化和改进

记住：编程没有唯一正确答案，重要的是理解思路！
"""

import random  # 用于模拟和随机数据生成


def solution_1_quality_filter():
    """
    练习1参考答案：序列质量过滤 ⭐
    
    展示基础的if条件判断和for循环使用
    重点：条件判断的逻辑组合
    """
    print("=" * 60)
    print("练习1：序列质量过滤 ⭐")
    print("=" * 60)
    
    # 测试数据
    sequences = [
        {"id": "read1", "seq": "ATGCGATCGA", "quality": 38},
        {"id": "read2", "seq": "ATGNNNATCN", "quality": 25},
        {"id": "read3", "seq": "GCGATCGATG", "quality": 41},
        {"id": "read4", "seq": "NNATGCGANN", "quality": 32},
        {"id": "read5", "seq": "ATGCGATCGN", "quality": 35},
    ]
    
    # 解答：实现质量过滤
    high_quality = []  # 存储高质量序列
    low_quality = []   # 存储低质量序列
    
    # 设定过滤标准
    quality_threshold = 30
    max_n_percent = 10
    
    print(f"过滤标准：")
    print(f"  - 最低质量分数: Q{quality_threshold}")
    print(f"  - 最大N含量: {max_n_percent}%\n")
    
    # 遍历每条序列进行质量控制
    for seq in sequences:
        # 计算N的百分比
        n_count = seq['seq'].count('N')
        n_percent = (n_count / len(seq['seq'])) * 100
        
        # 判断是否通过质控
        if seq['quality'] >= quality_threshold and n_percent <= max_n_percent:
            high_quality.append(seq)
            print(f"✅ {seq['id']}: Q={seq['quality']}, N={n_percent:.1f}% - 通过")
        else:
            low_quality.append(seq)
            # 详细说明未通过的原因
            if seq['quality'] < quality_threshold:
                print(f"❌ {seq['id']}: Q={seq['quality']} < Q{quality_threshold} - 质量太低")
            else:
                print(f"❌ {seq['id']}: N={n_percent:.1f}% > {max_n_percent}% - N太多")
    
    # 输出统计结果
    total = len(sequences)
    passed = len(high_quality)
    pass_rate = (passed / total) * 100
    
    print(f"\n📊 质控结果统计：")
    print(f"  - 总序列数: {total}")
    print(f"  - 通过质控: {passed}")
    print(f"  - 未通过: {len(low_quality)}")
    print(f"  - 通过率: {pass_rate:.1f}%")
    
    # 显示通过的序列
    if high_quality:
        print(f"\n通过质控的序列ID: {[s['id'] for s in high_quality]}")


def solution_2_find_restriction_sites():
    """
    练习2参考答案：查找限制性酶切位点 ⭐⭐
    
    展示字符串模式匹配和位置记录
    """
    print("\n练习2：限制性酶切位点 ⭐⭐")
    print("-" * 40)
    
    dna = "CGGAATTCATGGATCCTAGAATTCGCGGATCCAAGAATTC"
    
    print(f"DNA序列: {dna}")
    print(f"序列长度: {len(dna)} bp\n")
    
    # 定义酶切位点
    ecori_seq = "GAATTC"  # EcoRI识别序列
    bamhi_seq = "GGATCC"  # BamHI识别序列
    
    # 存储结果
    ecori_sites = []
    bamhi_sites = []
    all_sites = []  # 存储所有位点用于排序
    
    # 查找酶切位点
    for i in range(len(dna) - 5):  # -5因为酶切序列长度为6
        # 提取6bp子序列
        site = dna[i:i+6]
        
        # 检查是否为EcoRI位点
        if site == ecori_seq:
            ecori_sites.append(i)
            all_sites.append((i, "EcoRI", site))
            print(f"📍 EcoRI位点在位置 {i}: {dna[max(0,i-2):i]}[{site}]{dna[i+6:min(i+8,len(dna))]}")
        
        # 检查是否为BamHI位点
        elif site == bamhi_seq:
            bamhi_sites.append(i)
            all_sites.append((i, "BamHI", site))
            print(f"📍 BamHI位点在位置 {i}: {dna[max(0,i-2):i]}[{site}]{dna[i+6:min(i+8,len(dna))]}")
    
    # 统计结果
    print(f"\n📊 酶切位点统计：")
    print(f"  - EcoRI (GAATTC): {len(ecori_sites)} 个位点")
    if ecori_sites:
        print(f"    位置: {ecori_sites}")
    
    print(f"  - BamHI (GGATCC): {len(bamhi_sites)} 个位点")
    if bamhi_sites:
        print(f"    位置: {bamhi_sites}")
    
    # 判断哪个酶切位点更多
    if len(ecori_sites) > len(bamhi_sites):
        print(f"\n💡 EcoRI位点更多，适合用EcoRI进行酶切")
    elif len(bamhi_sites) > len(ecori_sites):
        print(f"\n💡 BamHI位点更多，适合用BamHI进行酶切")
    else:
        print(f"\n💡 两种酶的位点数量相同")
    
    # 计算片段大小（酶切后）
    if all_sites:
        all_sites.sort()  # 按位置排序
        print(f"\n🔬 酶切后片段大小预测：")
        
        # 第一个片段
        print(f"  片段1: 0-{all_sites[0][0]} = {all_sites[0][0]} bp")
        
        # 中间片段
        for i in range(len(all_sites)-1):
            start = all_sites[i][0] + 6  # 酶切后的起始位置
            end = all_sites[i+1][0]
            print(f"  片段{i+2}: {start}-{end} = {end-start} bp")
        
        # 最后一个片段
        last_cut = all_sites[-1][0] + 6
        print(f"  片段{len(all_sites)+1}: {last_cut}-{len(dna)} = {len(dna)-last_cut} bp")


def solution_3_find_longest_orf():
    """
    练习3参考答案：找出最长的开放阅读框(ORF) ⭐⭐⭐
    
    展示嵌套循环和最大值查找
    """
    print("\n练习3：最长开放阅读框 ⭐⭐⭐")
    print("-" * 40)
    
    dna = "CGATGAAACCCTAGATGGGGTAACGATGCCCTGAATGAAATAACCC"
    
    print(f"DNA序列: {dna}")
    print(f"序列长度: {len(dna)} bp\n")
    
    # 定义终止密码子
    stop_codons = ["TAA", "TAG", "TGA"]
    
    # 存储所有ORF
    all_orfs = []
    
    # 记录最长ORF
    longest_orf_start = -1
    longest_orf_end = -1
    longest_orf_length = 0
    
    # 查找所有ATG起始密码子
    for i in range(len(dna) - 2):
        if dna[i:i+3] == "ATG":
            # 从ATG开始查找终止密码子
            # 注意：要保持阅读框，所以步长为3
            for j in range(i+3, len(dna)-2, 3):
                codon = dna[j:j+3]
                
                if codon in stop_codons:
                    # 找到终止密码子，记录ORF
                    orf_length = j + 3 - i  # 包括终止密码子
                    all_orfs.append({
                        'start': i,
                        'end': j + 3,
                        'length': orf_length,
                        'stop_codon': codon,
                        'sequence': dna[i:j+3]
                    })
                    
                    print(f"ORF {len(all_orfs)}: 位置{i}-{j+3}, 长度{orf_length}bp")
                    print(f"  起始: ATG at {i}")
                    print(f"  终止: {codon} at {j}")
                    print(f"  序列: {dna[i:j+3][:20]}..." if orf_length > 20 else f"  序列: {dna[i:j+3]}")
                    
                    # 更新最长ORF记录
                    if orf_length > longest_orf_length:
                        longest_orf_start = i
                        longest_orf_end = j + 3
                        longest_orf_length = orf_length
                    
                    break  # 找到终止密码子后退出内层循环
    
    # 输出结果
    print(f"\n📊 ORF分析结果：")
    print(f"  - 找到 {len(all_orfs)} 个ORF")
    
    if longest_orf_start != -1:
        print(f"\n🏆 最长ORF：")
        print(f"  - 位置: {longest_orf_start}-{longest_orf_end}")
        print(f"  - 长度: {longest_orf_length} bp")
        print(f"  - 序列: {dna[longest_orf_start:longest_orf_end]}")
        
        # 翻译成氨基酸（简化版）
        print(f"\n💊 蛋白质长度预测: {longest_orf_length // 3} 个氨基酸")
    else:
        print("\n未找到完整的ORF（没有终止密码子）")


def solution_4_gc_content_windows():
    """
    练习4参考答案：滑动窗口分析GC含量 ⭐⭐
    
    展示滑动窗口技术和极值查找
    """
    print("\n练习4：滑动窗口GC分析 ⭐⭐")
    print("-" * 40)
    
    dna = "GCGCGCGCGCATATATATATCGCGCGCGCGATATATATATAT"
    window_size = 10
    
    print(f"DNA序列: {dna}")
    print(f"序列长度: {len(dna)} bp")
    print(f"窗口大小: {window_size} bp\n")
    
    # 存储每个窗口的GC含量
    gc_windows = []
    
    # 滑动窗口分析
    for i in range(len(dna) - window_size + 1):
        # 提取窗口序列
        window = dna[i:i+window_size]
        
        # 计算GC含量
        gc_count = window.count('G') + window.count('C')
        gc_percent = (gc_count / window_size) * 100
        
        # 记录结果
        gc_windows.append({
            'position': i,
            'window': window,
            'gc_percent': gc_percent
        })
        
        # 显示前3个窗口作为示例
        if i < 3:
            print(f"窗口{i+1} (位置{i}): {window} -> GC={gc_percent:.1f}%")
    
    if len(gc_windows) > 3:
        print(f"... ({len(gc_windows)-3} 个窗口省略) ...")
    
    # 找出最高和最低GC含量的窗口
    max_gc_window = max(gc_windows, key=lambda x: x['gc_percent'])
    min_gc_window = min(gc_windows, key=lambda x: x['gc_percent'])
    
    # 计算平均GC含量
    avg_gc = sum(w['gc_percent'] for w in gc_windows) / len(gc_windows)
    
    print(f"\n📊 GC含量分析结果：")
    print(f"  - 窗口总数: {len(gc_windows)}")
    print(f"  - 平均GC含量: {avg_gc:.1f}%")
    
    print(f"\n🔝 最高GC含量窗口：")
    print(f"  - 位置: {max_gc_window['position']}")
    print(f"  - 序列: {max_gc_window['window']}")
    print(f"  - GC含量: {max_gc_window['gc_percent']:.1f}%")
    print(f"  - 特征: {'GC富集区（可能是CpG岛）' if max_gc_window['gc_percent'] > 60 else '正常GC含量'}")
    
    print(f"\n🔻 最低GC含量窗口：")
    print(f"  - 位置: {min_gc_window['position']}")
    print(f"  - 序列: {min_gc_window['window']}")
    print(f"  - GC含量: {min_gc_window['gc_percent']:.1f}%")
    print(f"  - 特征: {'AT富集区' if min_gc_window['gc_percent'] < 40 else '正常GC含量'}")
    
    # 可视化GC含量分布（简单版）
    print(f"\n📈 GC含量分布图（简化）：")
    for i, window in enumerate(gc_windows[::3]):  # 每3个窗口显示一个
        bar_length = int(window['gc_percent'] / 5)  # 每5%一个符号
        bar = '█' * bar_length
        print(f"位置{window['position']:2d}: {bar} {window['gc_percent']:.0f}%")


def solution_5_codon_usage():
    """
    练习5参考答案：密码子使用频率统计 ⭐⭐⭐
    
    展示字典的使用和统计分析
    """
    print("\n练习5：密码子使用分析 ⭐⭐⭐")
    print("-" * 40)
    
    cds = "ATGCCCATGAAATGGATGTTTAAATAGATGCCCATGAAATAG"
    
    print(f"CDS序列: {cds}")
    print(f"序列长度: {len(cds)} bp")
    print(f"密码子数: {len(cds)//3}\n")
    
    # 统计密码子使用频率
    codon_count = {}  # 使用字典存储计数
    total_codons = 0
    
    # 提取并统计所有密码子
    for i in range(0, len(cds)-2, 3):
        codon = cds[i:i+3]
        
        if len(codon) == 3:  # 确保是完整的密码子
            total_codons += 1
            
            # 统计密码子出现次数
            if codon in codon_count:
                codon_count[codon] += 1
            else:
                codon_count[codon] = 1
    
    # 计算使用频率
    codon_freq = {}
    for codon, count in codon_count.items():
        freq = (count / total_codons) * 100
        codon_freq[codon] = freq
    
    # 排序（按频率从高到低）
    sorted_codons = sorted(codon_count.items(), key=lambda x: x[1], reverse=True)
    
    # 输出结果
    print("📊 密码子使用统计：")
    print(f"  总密码子数: {total_codons}")
    print(f"  不同密码子种类: {len(codon_count)}\n")
    
    print("密码子使用频率表：")
    print("-" * 40)
    print("密码子 | 出现次数 | 使用频率 | 可视化")
    print("-" * 40)
    
    for codon, count in sorted_codons:
        freq = codon_freq[codon]
        bar = '▮' * count
        print(f"{codon:6s} | {count:8d} | {freq:7.1f}% | {bar}")
    
    # 找出最常用和最少用的密码子
    most_used = sorted_codons[0]
    least_used = sorted_codons[-1]
    
    print(f"\n💡 分析结果：")
    print(f"  最常用密码子: {most_used[0]} (使用{most_used[1]}次, {codon_freq[most_used[0]]:.1f}%)")
    print(f"  最少用密码子: {least_used[0]} (使用{least_used[1]}次, {codon_freq[least_used[0]]:.1f}%)")
    
    # 检查起始和终止密码子
    if "ATG" in codon_count:
        print(f"\n  起始密码子ATG: {codon_count['ATG']}个")
    
    stop_codons = ["TAA", "TAG", "TGA"]
    for stop in stop_codons:
        if stop in codon_count:
            print(f"  终止密码子{stop}: {codon_count[stop]}个")
    
    # 密码子使用偏好性分析
    print(f"\n🧬 密码子偏好性分析：")
    if len(codon_count) < 10:
        print("  密码子多样性较低，可能存在强烈的使用偏好")
    else:
        print("  密码子使用相对多样化")


def challenge_solution():
    """
    挑战题参考答案：基因预测综合分析 ⭐⭐⭐⭐
    
    综合运用所有控制流知识的完整示例
    """
    print("\n挑战题：基因预测 ⭐⭐⭐⭐")
    print("-" * 40)
    
    genomic_dna = """
    CGATCGATCGATGCCCATGAAATGGATGTTTAAATAGATCGATCG
    ATGAAACCCTAGATGGGGTAACGATGCCCTGAATGAAATAACCCA
    TGACCGTATGCGATGAAATAGTGACCGTATGCGATGAAATAGTAG
    """.replace("\n", "").replace(" ", "")
    
    print(f"基因组序列长度: {len(genomic_dna)} bp")
    print("开始基因预测分析...\n")
    
    # 定义终止密码子
    stop_codons = ["TAA", "TAG", "TGA"]
    
    # 存储所有候选ORF
    candidate_orfs = []
    
    # 在三个阅读框中搜索ORF
    for frame in range(3):
        print(f"扫描阅读框 {frame}...")
        
        # 在当前阅读框中查找所有ATG
        for i in range(frame, len(genomic_dna) - 2, 3):
            if genomic_dna[i:i+3] == "ATG":
                # 从ATG开始查找终止密码子
                for j in range(i+3, len(genomic_dna)-2, 3):
                    codon = genomic_dna[j:j+3]
                    
                    if codon in stop_codons:
                        orf_length = j + 3 - i
                        orf_seq = genomic_dna[i:j+3]
                        
                        # 计算GC含量
                        gc_count = orf_seq.count('G') + orf_seq.count('C')
                        gc_content = (gc_count / len(orf_seq)) * 100
                        
                        # 计算评分（简单版）
                        score = 0
                        if orf_length >= 100:  # 长度得分
                            score += orf_length / 10
                        if 40 <= gc_content <= 60:  # GC含量得分
                            score += 50
                        if i < 50:  # 靠近序列开头得分
                            score += 30
                        
                        candidate_orfs.append({
                            'frame': frame,
                            'start': i,
                            'end': j + 3,
                            'length': orf_length,
                            'gc_content': gc_content,
                            'score': score,
                            'sequence': orf_seq,
                            'stop_codon': codon
                        })
                        
                        break  # 找到终止密码子后退出
    
    print(f"\n找到 {len(candidate_orfs)} 个候选ORF\n")
    
    # 过滤太短的ORF
    min_length = 100
    filtered_orfs = [orf for orf in candidate_orfs if orf['length'] >= min_length]
    
    print(f"过滤后（>={min_length}bp）: {len(filtered_orfs)} 个ORF\n")
    
    if filtered_orfs:
        # 按评分排序
        filtered_orfs.sort(key=lambda x: x['score'], reverse=True)
        
        # 显示最可能的基因
        best_orf = filtered_orfs[0]
        
        print("🏆 最可能的基因：")
        print(f"  阅读框: {best_orf['frame']}")
        print(f"  位置: {best_orf['start']}-{best_orf['end']}")
        print(f"  长度: {best_orf['length']} bp")
        print(f"  GC含量: {best_orf['gc_content']:.1f}%")
        print(f"  评分: {best_orf['score']:.1f}")
        print(f"  终止密码子: {best_orf['stop_codon']}")
        
        # 显示序列（截取显示）
        seq = best_orf['sequence']
        if len(seq) > 60:
            print(f"  序列: {seq[:30]}...{seq[-30:]}")
        else:
            print(f"  序列: {seq}")
        
        # 预测蛋白质
        protein_length = best_orf['length'] // 3
        print(f"\n💊 预测蛋白质长度: {protein_length} 个氨基酸")
        
        # 显示其他候选基因
        if len(filtered_orfs) > 1:
            print(f"\n其他候选基因（按评分排序）：")
            for i, orf in enumerate(filtered_orfs[1:4], 1):  # 显示前3个
                print(f"  {i}. 阅读框{orf['frame']}, 位置{orf['start']}-{orf['end']}, "
                      f"长度{orf['length']}bp, 评分{orf['score']:.1f}")
    else:
        print("未找到足够长的ORF，可能不是编码序列")


def additional_examples():
    """
    额外示例：展示更多控制流技巧
    """
    print("\n" + "=" * 60)
    print("额外示例：控制流进阶技巧")
    print("=" * 60)
    
    # 示例1：列表推导式（简化的for循环）
    print("\n📌 示例1：列表推导式")
    dna = "ATGCGATCG"
    
    # 传统方法
    bases = []
    for base in dna:
        bases.append(base.lower())
    print(f"传统方法: {bases}")
    
    # 列表推导式
    bases_new = [base.lower() for base in dna]
    print(f"列表推导: {bases_new}")
    
    # 带条件的列表推导
    gc_bases = [base for base in dna if base in 'GC']
    print(f"只保留GC: {gc_bases}")
    
    # 示例2：enumerate的使用
    print("\n📌 示例2：enumerate获取索引和值")
    codons = ["ATG", "CCC", "TAA"]
    
    for i, codon in enumerate(codons):
        print(f"  密码子{i}: {codon}")
    
    # 示例3：zip同时遍历多个列表
    print("\n📌 示例3：zip同时遍历")
    sequences = ["ATGC", "CGTA", "TAGC"]
    qualities = [30, 35, 28]
    
    for seq, qual in zip(sequences, qualities):
        print(f"  序列{seq} 质量={qual}")
    
    # 示例4：any和all函数
    print("\n📌 示例4：any和all判断")
    scores = [35, 40, 32, 38]
    
    if all(score >= 30 for score in scores):
        print("  所有分数都>=30")
    
    if any(score >= 40 for score in scores):
        print("  至少有一个分数>=40")


def best_practices():
    """
    最佳实践总结
    """
    print("\n" + "=" * 60)
    print("🌟 控制流最佳实践")
    print("=" * 60)
    
    print("\n1. 选择合适的循环类型：")
    print("   - for循环: 已知迭代次数或遍历集合")
    print("   - while循环: 条件未知，需要持续检查")
    
    print("\n2. 避免无限循环：")
    print("   - while循环必须有退出条件")
    print("   - 记得更新循环变量")
    
    print("\n3. 合理使用break和continue：")
    print("   - break: 找到目标立即退出")
    print("   - continue: 跳过不符合条件的项")
    
    print("\n4. 嵌套层数控制：")
    print("   - 避免过深的嵌套（一般不超过3层）")
    print("   - 考虑将复杂逻辑拆分成函数")
    
    print("\n5. 条件判断优化：")
    print("   - 把最可能的条件放在前面")
    print("   - 使用elif避免多余的判断")
    
    print("\n6. 代码可读性：")
    print("   - 使用有意义的变量名")
    print("   - 添加适当的注释")
    print("   - 保持一致的缩进")


def main():
    """主函数：运行所有参考答案"""
    print("=" * 70)
    print("Chapter 03 控制流练习 - 参考答案")
    print("=" * 70)
    print("\n这里展示了所有练习题的详细解答，")
    print("包括多种解决方案和最佳实践。\n")
    
    # 运行所有解答
    solution_1_quality_filter()
    solution_2_find_restriction_sites()
    solution_3_find_longest_orf()
    solution_4_gc_content_windows()
    solution_5_codon_usage()
    challenge_solution()
    
    # 额外内容
    additional_examples()
    best_practices()
    
    print("\n" + "=" * 70)
    print("🎯 学习建议：")
    print("1. 理解每个解答的思路，而不是死记代码")
    print("2. 尝试用不同方法解决同一个问题")
    print("3. 在自己的数据上测试这些代码")
    print("4. 逐步从简单到复杂，建立信心")
    print("=" * 70)


if __name__ == "__main__":
    main()