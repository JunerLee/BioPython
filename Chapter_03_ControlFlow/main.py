#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 03: 控制流 - 给程序装上"大脑"的决策系统

生物学场景：从简单判断到复杂分析流程

📚 本章演示内容：
1. if语句深度演示 - 多层次的实验决策
2. for循环深度演示 - 批量数据处理
3. while循环深度演示 - 条件监测与迭代
4. 流程控制演示 - break、continue、pass
5. 综合应用 - 构建完整的生物信息学分析流程

💡 编程思维：
控制流让程序从"机械执行"变成"智能决策"
就像经验丰富的实验员，知道：
- 什么时候该做什么（if）
- 如何批量处理样品（for）
- 何时停止实验（while + break）
"""

import random  # 用于模拟实验数据


def section_1_if_statements():
    """
    演示1：if语句的多种应用场景
    
    生物学背景：
    实验室中充满了决策点，每个决策都影响后续流程。
    就像做Western Blot时要判断条带是否清晰，
    PCR时要检查引物是否合格。
    """
    print("=" * 70)
    print("🔬 演示1：if语句 - 程序的决策能力")
    print("=" * 70)
    
    # 1.1 单分支if - 简单判断
    print("\n📌 1.1 单分支if：PCR产物检测")
    print("-" * 40)
    
    pcr_product = "ATGCGATCGATCGATCGATCGATCG"
    expected_length = 25
    
    print(f"PCR产物序列: {pcr_product}")
    print(f"实际长度: {len(pcr_product)} bp")
    print(f"预期长度: {expected_length} bp")
    
    if len(pcr_product) == expected_length:
        print("✅ PCR成功！产物长度正确")
        print("   → 可以进行下一步克隆")
    
    # 1.2 双分支if-else
    print("\n📌 1.2 双分支if-else：限制酶位点检查")
    print("-" * 40)
    
    plasmid = "ATGCGAATTCGATCGGATCCATG"
    ecori_site = "GAATTC"
    
    print(f"质粒序列: {plasmid}")
    print(f"搜索EcoRI位点: {ecori_site}")
    
    if ecori_site in plasmid:
        position = plasmid.find(ecori_site)
        print(f"✅ 发现EcoRI位点在位置 {position}")
        print(f"   → 序列上下文: ...{plasmid[max(0,position-3):position]}[{ecori_site}]{plasmid[position+6:min(position+9,len(plasmid))]}...")
    else:
        print("❌ 未发现EcoRI位点")
        print("   → 需要选择其他限制酶")
    
    # 1.3 多分支if-elif-else
    print("\n📌 1.3 多分支判断：测序质量分级")
    print("-" * 40)
    
    samples = [
        {"id": "Sample_A", "quality": 42},
        {"id": "Sample_B", "quality": 35},
        {"id": "Sample_C", "quality": 25},
        {"id": "Sample_D", "quality": 15},
    ]
    
    for sample in samples:
        q_score = sample["quality"]
        sample_id = sample["id"]
        
        print(f"\n{sample_id} (Q{q_score}):")
        
        if q_score >= 40:
            print("  ⭐ 极高质量 - 可用于任何分析")
            error_rate = 10 ** (-q_score/10) * 100
            print(f"  错误率: {error_rate:.4f}%")
        elif q_score >= 30:
            print("  ✅ 高质量 - 适合大多数分析")
            error_rate = 10 ** (-q_score/10) * 100
            print(f"  错误率: {error_rate:.3f}%")
        elif q_score >= 20:
            print("  ⚠️ 中等质量 - 需要额外验证")
            error_rate = 10 ** (-q_score/10) * 100
            print(f"  错误率: {error_rate:.2f}%")
        else:
            print("  ❌ 低质量 - 建议重新测序")
            error_rate = 10 ** (-q_score/10) * 100
            print(f"  错误率: {error_rate:.1f}%")
    
    # 1.4 复合条件
    print("\n📌 1.4 复合条件：引物设计综合评估")
    print("-" * 40)
    
    primers = [
        {"name": "Primer_F", "seq": "ATGGCGATCGATCGATCGAT", "tm": 60},
        {"name": "Primer_R", "seq": "CGCGCGCGCGCGCGCGCGCG", "tm": 72},
        {"name": "Primer_F2", "seq": "ATATATATATATAT", "tm": 35},
    ]
    
    for primer in primers:
        name = primer["name"]
        seq = primer["seq"]
        tm = primer["tm"]
        length = len(seq)
        gc_content = (seq.count('G') + seq.count('C')) / length * 100
        
        print(f"\n{name}:")
        print(f"  序列: {seq}")
        print(f"  长度: {length} bp, GC: {gc_content:.1f}%, Tm: {tm}°C")
        
        # 综合判断
        if 18 <= length <= 25 and 40 <= gc_content <= 60 and 55 <= tm <= 65:
            print("  ✅ 引物设计优秀")
        elif length < 18 or length > 25:
            print("  ❌ 长度不合适（应该18-25 bp）")
        elif gc_content < 40 or gc_content > 60:
            print("  ❌ GC含量不合适（应该40-60%）")
        elif tm < 55 or tm > 65:
            print("  ❌ Tm不合适（应该55-65°C）")
    
    # 1.5 嵌套if
    print("\n📌 1.5 嵌套if：基因结构预测")
    print("-" * 40)
    
    sequences = [
        {"name": "Seq1", "seq": "ATGGCACCCAAATAG"},  # 完整CDS
        {"name": "Seq2", "seq": "ATGGCACCCAAA"},     # 缺终止
        {"name": "Seq3", "seq": "GCACCCAAATAG"},     # 缺起始
        {"name": "Seq4", "seq": "ATGGCACCCAATAG"},   # 移码
    ]
    
    for seq_data in sequences:
        name = seq_data["name"]
        seq = seq_data["seq"]
        
        print(f"\n{name}: {seq}")
        
        has_start = seq.startswith("ATG")
        has_stop = seq.endswith(("TAA", "TAG", "TGA"))
        is_multiple_of_3 = len(seq) % 3 == 0
        
        if has_start:
            print("  ✓ 有起始密码子")
            if has_stop:
                print("  ✓ 有终止密码子")
                if is_multiple_of_3:
                    print("  ✓ 长度是3的倍数")
                    print("  🧬 结论: 可能是完整的编码序列")
                else:
                    print("  ✗ 长度不是3的倍数")
                    print("  ⚠️ 结论: 可能有移码突变")
            else:
                print("  ✗ 缺少终止密码子")
                print("  ⚠️ 结论: 可能是部分序列")
        else:
            print("  ✗ 缺少起始密码子")
            if has_stop:
                print("  ✓ 有终止密码子")
                print("  ℹ️ 结论: 可能是序列片段")
            else:
                print("  ✗ 缺少终止密码子")
                print("  ℹ️ 结论: 可能是非编码序列")


def section_2_for_loops():
    """
    演示2：for循环的多种应用
    
    生物学背景：
    实验室中大量的重复操作：96孔板加样、批量DNA提取、
    多个样品的相同处理流程，这些都是for循环的应用场景。
    """
    print("\n" + "=" * 70)
    print("🔄 演示2：for循环 - 批量处理的利器")
    print("=" * 70)
    
    # 2.1 基础遍历
    print("\n📌 2.1 基础遍历：碱基统计")
    print("-" * 40)
    
    dna = "ATGCGATCGATCG"
    base_counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    
    print(f"DNA序列: {dna}")
    print("\n逐个碱基分析:")
    
    for i, base in enumerate(dna):
        base_counts[base] += 1
        hydrogen_bonds = 2 if base in "AT" else 3
        print(f"  位置{i:2d}: {base} ({hydrogen_bonds}个氢键)")
    
    print(f"\n碱基统计:")
    for base, count in base_counts.items():
        percentage = (count / len(dna)) * 100
        print(f"  {base}: {count}个 ({percentage:.1f}%)")
    
    # 2.2 range函数应用
    print("\n📌 2.2 range函数：PCR循环模拟")
    print("-" * 40)
    
    initial_copies = 100
    cycles = 8
    
    print(f"初始DNA模板: {initial_copies:,} 个拷贝")
    print(f"PCR循环数: {cycles}")
    print("\n扩增过程:")
    
    copies = initial_copies
    for cycle in range(1, cycles + 1):
        copies *= 2
        print(f"  第{cycle}轮: {copies:,} 个拷贝", end="")
        if cycle <= 3:
            print(" (指数扩增期)")
        elif cycle <= 6:
            print(" (线性扩增期)")
        else:
            print(" (平台期)")
    
    amplification = copies / initial_copies
    print(f"\n总扩增: {amplification:.0f}倍 (理论值: {2**cycles}倍)")
    
    # 2.3 批量样品处理
    print("\n📌 2.3 批量处理：多样品DNA定量与稀释")
    print("-" * 40)
    
    samples = [
        {"id": "Patient_001", "conc": 156.3, "vol": 50},
        {"id": "Patient_002", "conc": 89.7, "vol": 45},
        {"id": "Patient_003", "conc": 234.5, "vol": 30},
        {"id": "Control_001", "conc": 198.2, "vol": 40},
    ]
    
    target_conc = 100  # 目标浓度 ng/μL
    
    print(f"目标浓度: {target_conc} ng/μL")
    print("\n稀释方案:")
    
    for sample in samples:
        sample_id = sample["id"]
        original_conc = sample["conc"]
        volume = sample["vol"]
        
        print(f"\n{sample_id}:")
        print(f"  原始: {original_conc:.1f} ng/μL, {volume} μL")
        
        if original_conc > target_conc:
            dilution_factor = original_conc / target_conc
            water_volume = (dilution_factor - 1) * 10  # 假设取10μL样品
            print(f"  稀释: {dilution_factor:.2f}倍")
            print(f"  操作: 10 μL样品 + {water_volume:.1f} μL水")
        elif original_conc < target_conc:
            print(f"  ⚠️ 浓度过低，需要浓缩")
            concentration_factor = target_conc / original_conc
            print(f"  建议: 浓缩{concentration_factor:.2f}倍或重新提取")
        else:
            print(f"  ✅ 浓度正好，无需稀释")
    
    # 2.4 嵌套for循环：阅读框分析
    print("\n📌 2.4 嵌套循环：三阅读框ORF搜索")
    print("-" * 40)
    
    sequence = "CCATGGCATGAAATGTAGCCATGGCA"
    
    print(f"DNA序列: {sequence}")
    print(f"长度: {len(sequence)} bp")
    print("\n三个阅读框分析:")
    
    for frame in range(3):
        print(f"\n阅读框 {frame} (从位置{frame}开始):")
        
        # 提取该阅读框的所有密码子
        codons = []
        atg_positions = []
        
        for pos in range(frame, len(sequence) - 2, 3):
            codon = sequence[pos:pos+3]
            if len(codon) == 3:
                codons.append(codon)
                if codon == "ATG":
                    atg_positions.append(pos)
        
        # 显示密码子
        print(f"  密码子: {' '.join(codons)}")
        
        # 报告ATG位置
        if atg_positions:
            print(f"  发现ATG: 位置 {atg_positions}")
        else:
            print(f"  无ATG起始密码子")
        
        # 计算该阅读框的GC含量
        frame_seq = ''.join(codons)
        if frame_seq:
            gc = (frame_seq.count('G') + frame_seq.count('C')) / len(frame_seq) * 100
            print(f"  GC含量: {gc:.1f}%")
    
    # 2.5 列表推导式
    print("\n📌 2.5 列表推导式：高效数据转换")
    print("-" * 40)
    
    sequences = ["ATGC", "CGTA", "GGCC", "ATAT", "GCGC"]
    
    print(f"原始序列: {sequences}")
    
    # 各种列表推导式应用
    reverse = [seq[::-1] for seq in sequences]
    print(f"反向序列: {reverse}")
    
    gc_content = [(seq.count('G') + seq.count('C'))/len(seq)*100 for seq in sequences]
    print(f"GC含量%: {[f'{gc:.0f}' for gc in gc_content]}")
    
    gc_rich = [seq for seq in sequences if (seq.count('G') + seq.count('C'))/len(seq) > 0.5]
    print(f"GC>50%: {gc_rich}")
    
    at_rich = [seq for seq in sequences if (seq.count('A') + seq.count('T'))/len(seq) > 0.5]
    print(f"AT>50%: {at_rich}")


def section_3_while_loops():
    """
    演示3：while循环的应用场景
    
    生物学背景：
    许多实验需要持续监测直到满足条件：
    细胞培养到一定密度、透析到电导率达标、
    PCR温度达到目标值等。
    """
    print("\n" + "=" * 70)
    print("⏰ 演示3：while循环 - 条件监测器")
    print("=" * 70)
    
    # 3.1 基础while：序列搜索
    print("\n📌 3.1 基础while：搜索所有ATG位置")
    print("-" * 40)
    
    dna = "ATGCCATGGAAATGCTGATGTAG"
    
    print(f"DNA序列: {dna}")
    print("搜索所有ATG起始密码子...")
    
    position = 0
    atg_count = 0
    
    while position <= len(dna) - 3:
        if dna[position:position+3] == "ATG":
            atg_count += 1
            context_start = max(0, position-3)
            context_end = min(len(dna), position+6)
            context = dna[context_start:position] + f"[{dna[position:position+3]}]" + dna[position+3:context_end]
            print(f"  ATG #{atg_count} at position {position}: ...{context}...")
            position += 3  # 跳过已找到的ATG
        else:
            position += 1
    
    print(f"总共找到 {atg_count} 个ATG")
    
    # 3.2 迭代优化：二分法
    print("\n📌 3.2 迭代优化：寻找最佳反应温度")
    print("-" * 40)
    
    # 模拟酶活性与温度的关系（最佳温度37°C）
    def enzyme_activity(temp):
        """模拟酶活性（最佳温度37°C）"""
        return 100 * (1 - abs(temp - 37) / 20)
    
    temp_low = 20.0
    temp_high = 50.0
    target_activity = 95  # 目标活性
    tolerance = 0.5
    iteration = 0
    max_iterations = 10
    
    print(f"目标: 找到酶活性≥{target_activity}%的温度")
    print(f"初始范围: {temp_low}°C - {temp_high}°C")
    print("\n优化过程:")
    
    while temp_high - temp_low > tolerance and iteration < max_iterations:
        iteration += 1
        temp_mid = (temp_low + temp_high) / 2
        activity = enzyme_activity(temp_mid)
        
        print(f"  迭代{iteration}: T={temp_mid:.1f}°C, 活性={activity:.1f}%", end="")
        
        if activity >= target_activity:
            print(" ✓")
            break
        elif temp_mid < 37:  # 温度偏低
            temp_low = temp_mid
            print(" (升温)")
        else:  # 温度偏高
            temp_high = temp_mid
            print(" (降温)")
    
    optimal_temp = (temp_low + temp_high) / 2
    print(f"\n最佳温度: {optimal_temp:.1f}°C")
    print(f"最终活性: {enzyme_activity(optimal_temp):.1f}%")
    
    # 3.3 条件监测：细胞培养模拟
    print("\n📌 3.3 条件监测：细胞培养过程")
    print("-" * 40)
    
    initial_cells = 10000  # 初始细胞数
    target_cells = 1000000  # 目标细胞数
    doubling_time = 24  # 倍增时间（小时）
    
    cells = initial_cells
    time = 0
    passages = 0
    
    print(f"初始细胞数: {initial_cells:,}")
    print(f"目标细胞数: {target_cells:,}")
    print(f"倍增时间: {doubling_time}小时")
    print("\n培养过程:")
    
    while cells < target_cells:
        # 模拟一个倍增周期
        time += doubling_time
        cells *= 2
        
        # 检查是否需要传代（密度过高）
        if cells > 500000 and cells < target_cells:
            cells = cells // 4  # 1:4传代
            passages += 1
            print(f"  {time}h: {cells:,} 细胞 (传代{passages})")
        else:
            print(f"  {time}h: {cells:,} 细胞")
    
    print(f"\n培养完成:")
    print(f"  总时间: {time}小时 ({time/24:.1f}天)")
    print(f"  传代次数: {passages}")
    print(f"  最终细胞数: {cells:,}")


def section_4_flow_control():
    """
    演示4：流程控制（break、continue、pass）
    
    展示如何精细控制循环流程，
    就像实验中的紧急停止、跳过异常样品、预留实验步骤。
    """
    print("\n" + "=" * 70)
    print("🎮 演示4：流程控制 - break、continue、pass")
    print("=" * 70)
    
    # 4.1 break：找到目标立即停止
    print("\n📌 4.1 break：在多个基因库中搜索")
    print("-" * 40)
    
    gene_databases = {
        "GenBank": ["BRCA1", "TP53", "EGFR", "MYC"],
        "RefSeq": ["KRAS", "BRAF", "PIK3CA"],
        "Ensembl": ["PTEN", "BRCA1", "APC", "CDKN2A"],
        "UCSC": ["RB1", "VHL", "MLH1"],
    }
    
    target = "BRCA1"
    print(f"搜索目标基因: {target}")
    print("\n搜索过程:")
    
    found = False
    for db_name, genes in gene_databases.items():
        print(f"  搜索 {db_name}...", end="")
        
        for gene in genes:
            if gene == target:
                print(f" 找到了！")
                print(f"    → {target} 在 {db_name} 数据库")
                found = True
                break
        
        if found:
            break  # 找到后停止搜索其他数据库
        else:
            print(f" 未找到")
    
    if not found:
        print(f"  ❌ {target} 不在任何数据库中")
    
    # 4.2 continue：跳过不合格数据
    print("\n📌 4.2 continue：质量控制过滤")
    print("-" * 40)
    
    reads = [
        {"id": "read001", "seq": "ATGCGATCGATC", "qual": 38, "n_count": 0},
        {"id": "read002", "seq": "NATGNNGATCNN", "qual": 25, "n_count": 5},
        {"id": "read003", "seq": "GCGATCGATCGA", "qual": 41, "n_count": 0},
        {"id": "read004", "seq": "ATGNCGATCGAT", "qual": 15, "n_count": 1},
        {"id": "read005", "seq": "CGATCGATCGAT", "qual": 35, "n_count": 0},
    ]
    
    min_quality = 30
    max_n = 2
    
    print(f"质控标准: Q≥{min_quality}, N≤{max_n}")
    print("\n处理结果:")
    
    passed = []
    for read in reads:
        read_id = read["id"]
        quality = read["qual"]
        n_count = read["n_count"]
        
        # 质量检查
        if quality < min_quality:
            print(f"  ⚠️ {read_id}: 质量太低 (Q{quality}) - 跳过")
            continue
        
        # N含量检查
        if n_count > max_n:
            print(f"  ⚠️ {read_id}: N太多 ({n_count}个) - 跳过")
            continue
        
        # 通过质控的序列
        gc = (read["seq"].count('G') + read["seq"].count('C')) / len(read["seq"]) * 100
        print(f"  ✅ {read_id}: 通过质控 (GC={gc:.1f}%)")
        passed.append(read_id)
    
    print(f"\n通过率: {len(passed)}/{len(reads)} ({len(passed)/len(reads)*100:.0f}%)")
    
    # 4.3 pass：占位符
    print("\n📌 4.3 pass：构建分析框架")
    print("-" * 40)
    
    def analyze_gene_expression(sample_id, expression_data):
        """基因表达分析框架"""
        print(f"分析样品: {sample_id}")
        
        # 步骤1：数据预处理
        if len(expression_data) == 0:
            print("  ❌ 无数据")
            return
        else:
            print("  ✓ 数据加载成功")
            pass  # TODO: 添加标准化代码
        
        # 步骤2：质量检查
        if min(expression_data) < 0:
            print("  ⚠️ 发现负值，需要处理")
            pass  # TODO: 处理异常值
        else:
            print("  ✓ 数据质量合格")
        
        # 步骤3：统计分析
        mean_exp = sum(expression_data) / len(expression_data)
        max_exp = max(expression_data)
        
        if max_exp > mean_exp * 10:
            print("  📊 发现高表达基因")
            pass  # TODO: 识别差异表达基因
        
        # 步骤4：结果输出
        print(f"  平均表达: {mean_exp:.2f}")
        print(f"  最高表达: {max_exp:.2f}")
        
        return mean_exp
    
    # 测试框架
    test_data = [2.5, 3.8, 1.2, 45.6, 3.3, 2.9]
    result = analyze_gene_expression("Sample_001", test_data)


def section_5_comprehensive_analysis():
    """
    演示5：综合应用 - 构建完整的序列分析流程
    
    综合使用所有控制流结构，
    模拟真实的生物信息学分析任务。
    """
    print("\n" + "=" * 70)
    print("🔬 演示5：综合应用 - 多序列分析系统")
    print("=" * 70)
    
    # 生成模拟数据
    sequences = [
        {"id": "Gene001", "seq": "ATGGCGATCGATCGATCGTAGGATCC", "species": "human"},
        {"id": "Gene002", "seq": "ATGAAACCCTAGGAATTCATGGGGTAA", "species": "mouse"},
        {"id": "Gene003", "seq": "CCGATGGCGATCGATCGATCGGGATCC", "species": "human"},
        {"id": "Gene004", "seq": "ATGATGATGATGATGATGATGGAATTC", "species": "rat"},
        {"id": "Gene005", "seq": "GCGCGCATGCGCGCGCTAGCGCGCGC", "species": "mouse"},
    ]
    
    # 分析参数
    target_species = "human"
    min_length = 20
    restriction_sites = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "PstI": "CTGCAG",
    }
    
    print(f"分析参数:")
    print(f"  目标物种: {target_species}")
    print(f"  最小长度: {min_length} bp")
    print(f"  搜索酶切位点: {list(restriction_sites.keys())}")
    
    print("\n" + "=" * 60)
    print("开始分析...")
    print("=" * 60)
    
    # 结果统计
    stats = {
        "total": len(sequences),
        "passed": 0,
        "has_atg": 0,
        "has_sites": 0,
        "species_match": 0,
    }
    
    results = []
    
    # 主分析循环
    for seq_data in sequences:
        seq_id = seq_data["id"]
        sequence = seq_data["seq"]
        species = seq_data["species"]
        
        print(f"\n分析 {seq_id}:")
        print(f"  序列: {sequence[:20]}..." if len(sequence) > 20 else f"  序列: {sequence}")
        print(f"  长度: {len(sequence)} bp")
        print(f"  物种: {species}")
        
        # 初始化结果
        seq_result = {
            "id": seq_id,
            "passed": True,
            "issues": [],
            "features": [],
        }
        
        # 检查1：物种过滤
        if species != target_species:
            print(f"  ⚠️ 非目标物种，跳过")
            seq_result["passed"] = False
            seq_result["issues"].append("wrong_species")
            results.append(seq_result)
            continue
        
        stats["species_match"] += 1
        
        # 检查2：长度过滤
        if len(sequence) < min_length:
            print(f"  ❌ 序列太短 (<{min_length}bp)")
            seq_result["passed"] = False
            seq_result["issues"].append("too_short")
            results.append(seq_result)
            continue
        
        # 检查3：起始密码子
        has_atg = sequence.startswith("ATG")
        if has_atg:
            print(f"  ✓ 含有起始密码子ATG")
            seq_result["features"].append("has_ATG")
            stats["has_atg"] += 1
        else:
            print(f"  ✗ 缺少起始密码子")
        
        # 检查4：限制酶切位点
        found_sites = []
        for enzyme, site in restriction_sites.items():
            if site in sequence:
                positions = []
                pos = sequence.find(site)
                while pos != -1:
                    positions.append(pos)
                    pos = sequence.find(site, pos + 1)
                
                found_sites.append(f"{enzyme}({positions})")
                seq_result["features"].append(f"{enzyme}_site")
        
        if found_sites:
            print(f"  ✓ 酶切位点: {', '.join(found_sites)}")
            stats["has_sites"] += 1
        else:
            print(f"  ✗ 无限制酶切位点")
        
        # 检查5：GC含量
        gc_count = sequence.count('G') + sequence.count('C')
        gc_content = (gc_count / len(sequence)) * 100
        
        if gc_content < 30:
            print(f"  📊 GC含量: {gc_content:.1f}% (AT富集)")
            seq_result["features"].append("AT_rich")
        elif gc_content > 70:
            print(f"  📊 GC含量: {gc_content:.1f}% (GC富集)")
            seq_result["features"].append("GC_rich")
        else:
            print(f"  📊 GC含量: {gc_content:.1f}% (平衡)")
            seq_result["features"].append("balanced_GC")
        
        # 检查6：重复序列
        for i in range(3, 7):  # 检查3-6bp的重复
            pattern = sequence[:i]
            if sequence.count(pattern) >= 3:
                print(f"  🔁 发现重复: {pattern} (重复{sequence.count(pattern)}次)")
                seq_result["features"].append(f"repeat_{pattern}")
                break
        
        # 最终判定
        if seq_result["passed"]:
            stats["passed"] += 1
            print(f"  ✅ 通过所有检查")
        
        results.append(seq_result)
    
    # 生成报告
    print("\n" + "=" * 60)
    print("📊 分析报告")
    print("=" * 60)
    
    print(f"\n总体统计:")
    print(f"  总序列数: {stats['total']}")
    print(f"  目标物种: {stats['species_match']} ({stats['species_match']/stats['total']*100:.0f}%)")
    print(f"  通过筛选: {stats['passed']} ({stats['passed']/stats['total']*100:.0f}%)")
    print(f"  含起始密码子: {stats['has_atg']}")
    print(f"  含酶切位点: {stats['has_sites']}")
    
    # 详细结果
    print(f"\n通过筛选的序列:")
    for result in results:
        if result["passed"]:
            features = ", ".join(result["features"]) if result["features"] else "无特殊特征"
            print(f"  • {result['id']}: {features}")
    
    return results


def bonus_real_world_example():
    """
    额外演示：真实场景 - CRISPR靶点筛选
    
    展示控制流在实际研究中的应用
    """
    print("\n" + "=" * 70)
    print("🧬 真实应用：CRISPR-Cas9靶点筛选")
    print("=" * 70)
    
    # 目标基因序列
    target_gene = "ATGGCTTGAATGAAGGCCTAGGATCCGAATTCATGCAGCTGATGCACGGATCCTAGAATTCGCA"
    pam_sequence = "GG"  # Cas9的PAM序列（NGG）
    guide_length = 20  # gRNA长度
    
    print(f"目标基因 ({len(target_gene)} bp):")
    print(f"{target_gene}")
    print(f"\n筛选参数:")
    print(f"  PAM序列: N{pam_sequence}")
    print(f"  向导RNA长度: {guide_length} bp")
    
    print("\n潜在的CRISPR靶点:")
    print("-" * 50)
    
    candidates = []
    
    # 搜索所有可能的靶点
    for i in range(len(target_gene) - guide_length - 2):
        # 检查PAM序列
        if target_gene[i+guide_length:i+guide_length+2] == pam_sequence:
            guide_seq = target_gene[i:i+guide_length]
            pam = target_gene[i+guide_length:i+guide_length+3]
            
            # 计算GC含量
            gc = (guide_seq.count('G') + guide_seq.count('C')) / guide_length * 100
            
            # 评分系统
            score = 100
            
            # GC含量评分（理想40-60%）
            if 40 <= gc <= 60:
                gc_score = 30
            elif 30 <= gc <= 70:
                gc_score = 20
            else:
                gc_score = 10
            
            # 检查poly-T（转录终止信号）
            if "TTTT" in guide_seq:
                score -= 30
                
            # 检查自身互补（可能形成发夹结构）
            rev_comp = guide_seq[::-1].replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
            if guide_seq[:10] in rev_comp:
                score -= 20
            
            score = gc_score + (70 if score == 100 else score - 30)
            
            candidates.append({
                'position': i,
                'guide': guide_seq,
                'pam': pam,
                'gc': gc,
                'score': score
            })
    
    # 按评分排序
    candidates.sort(key=lambda x: x['score'], reverse=True)
    
    # 显示前5个候选
    for idx, candidate in enumerate(candidates[:5], 1):
        print(f"\n候选{idx} (位置 {candidate['position']}):")
        print(f"  gRNA: {candidate['guide']}")
        print(f"  PAM: {candidate['pam']}")
        print(f"  GC含量: {candidate['gc']:.1f}%")
        print(f"  评分: {candidate['score']}/100")
        
        # 标记潜在问题
        if "TTTT" in candidate['guide']:
            print(f"  ⚠️ 含有poly-T序列")
        if candidate['gc'] < 30 or candidate['gc'] > 70:
            print(f"  ⚠️ GC含量不理想")
    
    print(f"\n总共找到 {len(candidates)} 个潜在靶点")
    
    # 推荐最佳靶点
    if candidates:
        best = candidates[0]
        print(f"\n🎯 推荐靶点:")
        print(f"  位置: {best['position']}")
        print(f"  序列: {best['guide']}-{best['pam']}")
        print(f"  评分: {best['score']}/100")


def main():
    """
    主函数：运行所有演示
    
    学习路径：
    1. if语句 → 学会让程序做决策
    2. for循环 → 学会批量处理数据
    3. while循环 → 学会条件监测
    4. 流程控制 → 学会精细调控
    5. 综合应用 → 构建完整流程
    """
    print("\n" + "=" * 80)
    print("  🧬 Chapter 03: 控制流 - 给程序装上'大脑'的决策系统")
    print("=" * 80)
    
    print("\n📚 本章内容预览：")
    print("  1. if语句深度演示 - 多层次的实验决策")
    print("  2. for循环深度演示 - 批量数据处理")
    print("  3. while循环深度演示 - 条件监测与迭代")
    print("  4. 流程控制演示 - break、continue、pass")
    print("  5. 综合应用 - 构建完整的分析流程")
    print("  6. 真实案例 - CRISPR靶点筛选")
    
    print("\n💡 学习建议：")
    print("  • 仔细观察每个例子的输出")
    print("  • 理解不同控制结构的使用场景")
    print("  • 尝试修改代码参数看结果变化")
    print("  • 完成practice.py中的练习题")
    
    input("\n按Enter键开始学习...")
    
    # 演示1：if语句
    section_1_if_statements()
    input("\n按Enter继续下一节...")
    
    # 演示2：for循环
    section_2_for_loops()
    input("\n按Enter继续下一节...")
    
    # 演示3：while循环
    section_3_while_loops()
    input("\n按Enter继续下一节...")
    
    # 演示4：流程控制
    section_4_flow_control()
    input("\n按Enter继续下一节...")
    
    # 演示5：综合应用
    section_5_comprehensive_analysis()
    input("\n按Enter查看真实应用案例...")
    
    # 额外：真实案例
    bonus_real_world_example()
    
    # 总结
    print("\n" + "=" * 80)
    print("📚 本章知识要点总结")
    print("=" * 80)
    
    print("\n🎯 if语句 - 决策判断")
    print("  • 单分支：if")
    print("  • 双分支：if-else")
    print("  • 多分支：if-elif-else")
    print("  • 复合条件：and, or, not")
    print("  • 嵌套判断：多层决策")
    
    print("\n🔄 for循环 - 批量处理")
    print("  • 遍历序列：for item in sequence")
    print("  • 索引遍历：for i in range(len(seq))")
    print("  • 枚举遍历：for i, item in enumerate(seq)")
    print("  • 嵌套循环：多维数据处理")
    print("  • 列表推导：简洁高效的数据转换")
    
    print("\n⏰ while循环 - 条件监测")
    print("  • 基础形式：while condition")
    print("  • 计数器模式：配合计数变量")
    print("  • 哨兵模式：特定值触发退出")
    print("  • 迭代优化：逐步逼近目标")
    
    print("\n🎮 流程控制 - 精细调控")
    print("  • break：立即退出循环")
    print("  • continue：跳过当前迭代")
    print("  • pass：占位符，保持结构完整")
    
    print("\n💡 实际应用场景")
    print("  • 序列质量控制和筛选")
    print("  • 批量样品处理和分析")
    print("  • 基因预测和注释")
    print("  • 限制酶切位点分析")
    print("  • CRISPR靶点设计")
    print("  • 实验条件优化")
    
    print("\n🚀 下一步学习建议")
    print("  1. 完成practice.py中的5个练习题")
    print("  2. 尝试修改本文件中的参数，观察结果")
    print("  3. 用学到的知识分析自己的序列数据")
    print("  4. 查看practice_solution.py学习最佳实践")
    
    print("\n" + "=" * 80)
    print("🎉 恭喜完成Chapter 03的学习！")
    print("下一章将学习函数 - 如何创建可重用的代码模块")
    print("=" * 80)


if __name__ == "__main__":
    main()