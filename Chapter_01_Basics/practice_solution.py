#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 01: Python基础 - 练习题完整答案与详解

这里提供所有练习题的详细解答，每个答案都包含：
1. 完整的代码实现
2. 逐行解释
3. 生物学意义
4. 常见错误提醒
5. 扩展知识
"""


def warmup_print_dna():
    """
    热身题：你的第一行代码 - 完整答案
    
    学习重点：print()函数的使用
    """
    print("\n" + "="*50)
    print("热身题答案：打印DNA序列")
    print("="*50)
    
    # 1. 打印一个简单的DNA序列
    my_dna = "ATCG"
    print(my_dna)  # 最简单的打印
    
    # 解释：print()函数会在屏幕上显示括号内的内容
    # 就像在实验记录本上写下结果
    
    # 2. 打印带说明的序列
    print("我的DNA序列是:", my_dna)  # 可以打印多个内容，用逗号分隔
    
    # 解释：print可以同时打印文字和变量
    # 逗号会自动加空格
    
    # 3. 使用变量打印你的名字和序列
    your_name = "小明"  # 请改成你的真实名字
    print(f"我是{your_name}，我的序列是{my_dna}")  # f-string格式化
    
    # 解释：f-string (f"...{变量}...")是Python 3.6+的新特性
    # 花括号{}内的变量会被替换为实际值
    
    # 另外两种格式化方法（了解即可）
    print("我是" + your_name + "，我的序列是" + my_dna)  # 字符串连接
    print("我是{}，我的序列是{}".format(your_name, my_dna))  # format方法
    
    print("\n💡 知识点：")
    print("- print()是最常用的输出函数")
    print("- f-string是最推荐的格式化方法")
    print("- 逗号分隔会自动加空格")


def practice_1_simple_variables():
    """
    练习1答案：创建和使用变量
    
    学习重点：变量的创建和命名
    """
    print("\n" + "="*50)
    print("练习1答案：变量练习")
    print("="*50)
    
    print("场景：标记DNA样品")
    
    # 创建变量存储信息
    human_dna = "ATCGATCG"      # 人类DNA序列
    mouse_dna = "GCTAGCTA"      # 小鼠DNA序列
    bacteria_dna = "CGCGCGCG"   # 细菌DNA序列
    temperature = 37            # 实验温度（整数）
    is_living = False           # 是否活体样品（布尔值）
    
    # 打印所有变量
    print("人类DNA:", human_dna)
    print("小鼠DNA:", mouse_dna)
    print("细菌DNA:", bacteria_dna)
    print("温度:", temperature, "°C")
    print("活体样品:", is_living)
    
    # 扩展：显示变量类型
    print("\n变量类型检查：")
    print(f"human_dna的类型: {type(human_dna).__name__}")      # str
    print(f"temperature的类型: {type(temperature).__name__}")   # int
    print(f"is_living的类型: {type(is_living).__name__}")     # bool
    
    print("\n💡 知识点：")
    print("- 变量名要有意义（human_dna比hd清楚）")
    print("- Python自动识别数据类型")
    print("- 布尔值只有True和False（注意大写）")
    
    print("\n⚠️ 常见错误：")
    print("- 忘记引号：dna = ATCG（错误）")
    print("- 大小写混淆：false（错误）应该是False")


def practice_2_string_length():
    """
    练习2答案：测量序列长度
    
    学习重点：len()函数和比较操作
    """
    print("\n" + "="*50)
    print("练习2答案：测量DNA序列长度")
    print("="*50)
    
    print("场景：PCR产物长度检测")
    
    # PCR产物序列
    pcr_product = "ATCGATCGATCGATCGATCG"
    print(f"PCR产物: {pcr_product}")
    
    # 1. 计算PCR产物长度
    product_length = len(pcr_product)
    print(f"PCR产物长度: {product_length} bp")
    
    # 解释：len()函数返回序列中字符的数量
    # 对DNA序列，就是碱基对(bp)的数量
    
    # 2. 判断长度是否符合预期
    expected_length = 20
    is_correct_length = product_length == expected_length
    print(f"预期长度: {expected_length} bp")
    print(f"长度是否正确: {is_correct_length}")
    
    # 解释：== 是比较操作符，检查两个值是否相等
    # 返回布尔值：True或False
    
    # 3. 计算引物序列长度
    forward_primer = "ATCG"
    reverse_primer = "CGAT"
    forward_length = len(forward_primer)
    reverse_length = len(reverse_primer)
    
    print(f"\n引物长度检查：")
    print(f"正向引物: {forward_primer} ({forward_length} bp)")
    print(f"反向引物: {reverse_primer} ({reverse_length} bp)")
    
    # 扩展：引物设计规则
    ideal_primer_length = 20
    if 18 <= forward_length <= 25:
        print("正向引物长度：✅ 合适")
    else:
        print("正向引物长度：❌ 不理想（建议18-25 bp）")
    
    print("\n💡 知识点：")
    print("- len()是内置函数，可用于任何序列")
    print("- 比较操作返回布尔值")
    print("- PCR引物通常18-25 bp")


def practice_3_string_upper_lower():
    """
    练习3答案：序列标准化
    
    学习重点：字符串的大小写转换
    """
    print("\n" + "="*50)
    print("练习3答案：标准化序列格式")
    print("="*50)
    
    print("场景：整合不同实验室的测序数据")
    
    # 不同格式的序列
    lab1_sequence = "atcgatcg"      # 实验室1：小写
    lab2_sequence = "ATCGATCG"      # 实验室2：大写
    lab3_sequence = "AtCgAtCg"      # 实验室3：混合
    
    print("原始数据:")
    print(f"实验室1: {lab1_sequence}")
    print(f"实验室2: {lab2_sequence}")
    print(f"实验室3: {lab3_sequence}")
    
    # 标准化所有序列为大写
    lab1_standard = lab1_sequence.upper()
    lab2_standard = lab2_sequence.upper()  # 已经是大写，但这样更统一
    lab3_standard = lab3_sequence.upper()
    
    print("\n标准化后:")
    print(f"实验室1: {lab1_standard}")
    print(f"实验室2: {lab2_standard}")
    print(f"实验室3: {lab3_standard}")
    
    # 检查是否所有序列现在都相同
    all_same = (lab1_standard == lab2_standard == lab3_standard)
    print(f"\n所有序列是否相同: {all_same}")
    
    # 解释为什么标准化很重要
    print("\n为什么需要标准化？")
    if "atcg" == "ATCG":
        print("atcg == ATCG: True")
    else:
        print("atcg == ATCG: False（大小写敏感！）")
    
    # 扩展：其他字符串方法
    print("\n其他有用的字符串方法：")
    test = "  ATCG  "
    print(f"原始: '{test}'")
    print(f".strip()去空格: '{test.strip()}'")
    print(f".lower()转小写: '{test.lower()}'")
    print(f".replace()替换: '{test.replace('A', 'U')}'")  # DNA转RNA
    
    print("\n💡 知识点：")
    print("- .upper()和.lower()不改变原字符串")
    print("- Python字符串比较是大小写敏感的")
    print("- 数据标准化是数据分析的第一步")


def practice_4_count_bases():
    """
    练习4答案：统计碱基数量
    
    学习重点：count()方法的使用
    """
    print("\n" + "="*50)
    print("练习4答案：碱基组成分析")
    print("="*50)
    
    print("场景：分析启动子序列的碱基组成")
    
    # 启动子序列（包含TATA box）
    promoter = "TATAAAAATCGATCGATCG"
    print(f"启动子序列: {promoter}")
    
    # 统计各碱基数量
    a_count = promoter.count('A')
    t_count = promoter.count('T')
    c_count = promoter.count('C')
    g_count = promoter.count('G')
    
    print(f"\n碱基统计：")
    print(f"A的数量: {a_count}")
    print(f"T的数量: {t_count}")
    print(f"C的数量: {c_count}")
    print(f"G的数量: {g_count}")
    
    # 验证总数是否正确
    total_counted = a_count + t_count + c_count + g_count
    sequence_length = len(promoter)
    
    print(f"\n验证：")
    print(f"统计总数: {total_counted}")
    print(f"序列长度: {sequence_length}")
    print(f"计数是否正确: {total_counted == sequence_length}")
    
    # 计算各碱基比例
    print(f"\n碱基比例：")
    for base, count in [('A', a_count), ('T', t_count), 
                        ('C', c_count), ('G', g_count)]:
        percentage = (count / sequence_length) * 100
        bar = '█' * int(percentage / 5)  # 简单的柱状图
        print(f"{base}: {bar} {percentage:.1f}%")
    
    # 生物学分析
    print(f"\n生物学特征：")
    if "TATAAA" in promoter:
        print("✅ 包含TATA box (TATAAA)")
        print("   这是真核生物启动子的典型特征")
    
    at_percentage = ((a_count + t_count) / sequence_length) * 100
    if at_percentage > 60:
        print(f"✅ AT富集区域 ({at_percentage:.1f}%)")
        print("   有利于DNA双链的打开")
    
    print("\n💡 知识点：")
    print("- count()方法统计子串出现次数")
    print("- TATA box是重要的转录调控元件")
    print("- 启动子区域通常AT含量较高")


def practice_5_calculate_at_content():
    """
    练习5答案：计算AT含量
    
    学习重点：综合使用count()和len()进行计算
    """
    print("\n" + "="*50)
    print("练习5答案：计算AT含量")
    print("="*50)
    
    print("场景：分析AT富集区域")
    
    # AT富集序列
    at_rich_sequence = "AAATTTAAATTTAAATTT"
    print(f"序列: {at_rich_sequence}")
    
    # 1. 统计A和T
    a_count = at_rich_sequence.count('A')
    t_count = at_rich_sequence.count('T')
    
    # 2. 获取序列长度
    total_length = len(at_rich_sequence)
    
    # 3. 计算AT碱基总数
    at_bases = a_count + t_count
    
    # 4. 计算AT含量百分比
    at_content = (at_bases / total_length) * 100
    
    # 5. 计算GC含量
    gc_content = 100 - at_content  # 因为只有ATCG四种碱基
    
    print(f"\n详细分析：")
    print(f"A的数量: {a_count}")
    print(f"T的数量: {t_count}")
    print(f"AT碱基总数: {at_bases}")
    print(f"序列总长度: {total_length}")
    print(f"AT含量: {at_content:.1f}%")
    print(f"GC含量: {gc_content:.1f}%")
    
    # 生物学意义
    print(f"\n生物学解释：")
    if at_content > 70:
        print("✅ 高AT含量区域特征：")
        print("   - 更容易解链（A-T只有2个氢键）")
        print("   - 可能是复制起始点")
        print("   - 常见于调控区域")
    
    # 计算熔解温度（简化公式）
    # Tm = 4 * (G + C) + 2 * (A + T)
    g_count = at_rich_sequence.count('G')
    c_count = at_rich_sequence.count('C')
    tm = 4 * (g_count + c_count) + 2 * (a_count + t_count)
    print(f"\n预测熔解温度(Tm): {tm}°C")
    print("（使用Wallace规则：短序列的简化计算）")
    
    print("\n💡 知识点：")
    print("- AT含量 + GC含量 = 100%")
    print("- AT富集区域在基因组中有特殊功能")
    print("- 熔解温度与GC含量正相关")


def practice_6_sequence_slicing():
    """
    练习6答案：序列切片
    
    学习重点：字符串切片操作
    """
    print("\n" + "="*50)
    print("练习6答案：提取序列片段")
    print("="*50)
    
    print("场景：从基因序列中提取密码子")
    
    # 基因序列
    gene = "ATGGATTTATCTGCTCTTCGCG"
    print(f"基因序列: {gene}")
    print("位置索引: 0123456789012345678901")  # 帮助理解
    print("         10        20")
    
    # 1. 提取起始密码子（前3个碱基）
    start_codon = gene[0:3]  # 或 gene[:3]
    print(f"\n起始密码子[0:3]: {start_codon}")
    
    # 2. 提取第二个密码子（位置3-6）
    second_codon = gene[3:6]
    print(f"第二个密码子[3:6]: {second_codon}")
    
    # 3. 提取前10个碱基
    first_ten = gene[:10]  # 省略起始位置默认从0开始
    print(f"前10个碱基[:10]: {first_ten}")
    
    # 4. 提取最后5个碱基
    last_five = gene[-5:]  # 负数索引从末尾开始
    print(f"最后5个碱基[-5:]: {last_five}")
    
    # 5. 提取中间片段
    middle_part = gene[5:15]
    print(f"中间片段[5:15]: {middle_part}")
    
    # 扩展：完整的密码子分割
    print(f"\n密码子分割：")
    codons = []
    for i in range(0, len(gene), 3):  # 每3个碱基一组
        codon = gene[i:i+3]
        if len(codon) == 3:  # 确保是完整的密码子
            codons.append(codon)
            print(f"密码子{i//3 + 1}: {codon}")
    
    # 更简洁的写法（列表推导式）
    codons_alt = [gene[i:i+3] for i in range(0, len(gene), 3) if len(gene[i:i+3]) == 3]
    print(f"\n所有密码子: {' '.join(codons_alt)}")
    
    print("\n💡 知识点：")
    print("- 切片语法：[起始:结束:步长]")
    print("- 索引从0开始")
    print("- 负索引从末尾开始（-1是最后一个）")
    print("- 切片不包含结束位置")
    
    print("\n⚠️ 常见错误：")
    print("- gene[0:3]得到3个字符，不是4个")
    print("- gene[3]是单个字符，gene[3:4]是字符串")


def practice_7_find_pattern():
    """
    练习7答案：查找序列模式
    
    学习重点：in操作符、find()和count()方法
    """
    print("\n" + "="*50)
    print("练习7答案：查找生物学模式")
    print("="*50)
    
    print("场景：在序列中查找调控元件")
    
    # 启动子区域序列
    promoter_region = "GCGCTATAAAAGCGCGCATGGATTTATCTGC"
    print(f"启动子序列: {promoter_region}")
    
    # 1. 检查是否包含TATA box
    tata_box = "TATAAA"
    has_tata = tata_box in promoter_region
    print(f"\n包含TATA box ({tata_box}): {has_tata}")
    
    # 2. 找出位置
    if has_tata:
        position = promoter_region.find(tata_box)
        print(f"TATA box位置: {position} (从0开始计数)")
        print(f"实际位置: 第{position + 1}个碱基开始")
        
        # 显示位置
        before = promoter_region[:position]
        pattern = promoter_region[position:position+len(tata_box)]
        after = promoter_region[position+len(tata_box):]
        print(f"序列标注: {before}[{pattern}]{after}")
    
    # 3. 检查起始密码子
    start_codon = "ATG"
    has_atg = start_codon in promoter_region
    print(f"\n包含起始密码子(ATG): {has_atg}")
    
    if has_atg:
        atg_position = promoter_region.find("ATG")
        print(f"ATG位置: {atg_position}")
        print(f"距离TATA box: {atg_position - position} bp")
    
    # 4. 统计GC二核苷酸
    gc_count = promoter_region.count("GC")
    print(f"\n'GC'二核苷酸出现次数: {gc_count}")
    
    # 扩展：查找所有出现位置
    print(f"\n所有'GC'的位置：")
    pattern = "GC"
    start = 0
    positions = []
    while True:
        pos = promoter_region.find(pattern, start)
        if pos == -1:  # find()找不到时返回-1
            break
        positions.append(pos)
        print(f"  位置{len(positions)}: {pos}")
        start = pos + 1
    
    # CpG岛分析
    cg_count = promoter_region.count("CG")
    total_c = promoter_region.count("C")
    total_g = promoter_region.count("G")
    
    if total_c > 0 and total_g > 0:
        expected_cg = (total_c * total_g) / len(promoter_region)
        obs_exp_ratio = cg_count / expected_cg if expected_cg > 0 else 0
        
        print(f"\nCpG岛分析：")
        print(f"CG二核苷酸数: {cg_count}")
        print(f"观察/期望比: {obs_exp_ratio:.2f}")
        if obs_exp_ratio > 0.6:
            print("✅ 可能是CpG岛")
    
    print("\n💡 知识点：")
    print("- in操作符检查是否包含")
    print("- find()返回第一次出现的位置")
    print("- count()统计所有出现次数")
    print("- CpG岛常见于基因启动子区域")


def practice_8_calculate_gc_content():
    """
    练习8答案：完整的GC含量计算
    
    学习重点：综合应用和条件判断
    """
    print("\n" + "="*50)
    print("练习8答案：GC含量计算（综合练习）")
    print("="*50)
    
    print("场景：分析不同物种的GC含量")
    
    # 不同物种的序列
    sequences = {
        "人类": "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTAC",
        "大肠杆菌": "GCGCGCGCATCGATCGATCGATCGCGCGCGC",
        "酵母": "ATATATATATGCGCGCGCATATATATAT"
    }
    
    # 存储结果用于比较
    results = []
    
    for species, sequence in sequences.items():
        print(f"\n{species}序列: {sequence}")
        
        # 1. 标准化序列
        clean_seq = sequence.upper()
        
        # 2. 计算G和C的数量
        g_count = clean_seq.count('G')
        c_count = clean_seq.count('C')
        
        # 3. 计算总长度
        total = len(clean_seq)
        
        # 4. 计算GC含量
        gc_content = ((g_count + c_count) / total) * 100 if total > 0 else 0
        
        # 5. 根据GC含量分类
        if gc_content < 40:
            category = "低GC含量"
            explanation = "可能来自AT富集的基因组区域"
        elif gc_content < 60:
            category = "中等GC含量"
            explanation = "典型的编码序列"
        else:
            category = "高GC含量"
            explanation = "可能来自GC富集的基因组或细菌"
        
        print(f"  G数量: {g_count}, C数量: {c_count}")
        print(f"  GC含量: {gc_content:.1f}%")
        print(f"  分类: {category}")
        print(f"  说明: {explanation}")
        
        # 保存结果
        results.append({
            'species': species,
            'gc_content': gc_content,
            'category': category
        })
    
    # 比较分析
    print("\n" + "="*30)
    print("比较分析：")
    print("="*30)
    
    # 找出GC含量最高和最低的
    highest = max(results, key=lambda x: x['gc_content'])
    lowest = min(results, key=lambda x: x['gc_content'])
    
    print(f"最高GC含量: {highest['species']} ({highest['gc_content']:.1f}%)")
    print(f"最低GC含量: {lowest['species']} ({lowest['gc_content']:.1f}%)")
    
    # 计算平均值
    avg_gc = sum(r['gc_content'] for r in results) / len(results)
    print(f"平均GC含量: {avg_gc:.1f}%")
    
    print("\n💡 知识点：")
    print("- 不同物种有特征性的GC含量")
    print("- 字典用于组织相关数据")
    print("- 条件判断用于分类")


def practice_9_sequence_validation():
    """
    练习9答案：序列质量控制
    
    学习重点：数据验证和清理
    """
    print("\n" + "="*50)
    print("练习9答案：序列质量验证")
    print("="*50)
    
    print("场景：验证测序数据质量")
    
    # 待验证的序列
    test_sequences = [
        "ATCGATCG",          # 正常序列
        "ATCGATCGN",         # 含有N
        "atcgatcg",          # 小写
        "ATCG ATCG",         # 含有空格
        "ATCGATCG123",       # 含有数字
        "ATCG-ATCG"          # 含有连字符
    ]
    
    # 有效碱基集合
    valid_bases = set('ATCG')
    
    for i, seq in enumerate(test_sequences, 1):
        print(f"\n序列{i}: '{seq}'")
        
        # 1. 先转为大写
        upper_seq = seq.upper()
        
        # 2. 检查每个字符
        valid = True
        invalid_chars = []
        for char in upper_seq:
            if char not in valid_bases:
                valid = False
                if char not in invalid_chars:  # 避免重复
                    invalid_chars.append(char)
        
        # 3. 输出验证结果
        if valid:
            print("  ✅ 有效序列")
        else:
            print(f"  ❌ 无效序列，包含: {invalid_chars}")
        
        # 4. 尝试清理序列
        cleaned = ""
        for char in upper_seq:
            if char in valid_bases:
                cleaned += char
        
        if cleaned and not valid:
            print(f"  清理后: {cleaned}")
            print(f"  保留率: {len(cleaned)/len(seq)*100:.1f}%")
        
        # 5. 质量评分
        if valid:
            quality = "高质量"
        elif len(cleaned) / len(seq) > 0.9:
            quality = "可接受（>90%有效）"
        elif len(cleaned) / len(seq) > 0.7:
            quality = "低质量（70-90%有效）"
        else:
            quality = "不可用（<70%有效）"
        
        print(f"  质量评级: {quality}")
    
    # 扩展：更高级的验证
    print("\n" + "="*30)
    print("高级质量控制：")
    print("="*30)
    
    def validate_sequence(sequence, min_length=10, max_n_ratio=0.1):
        """
        综合序列验证函数
        
        参数：
        - sequence: 待验证序列
        - min_length: 最小长度要求
        - max_n_ratio: 最大N比例
        """
        seq = sequence.upper()
        length = len(seq)
        
        # 检查长度
        if length < min_length:
            return False, f"序列太短（<{min_length} bp）"
        
        # 检查N的比例
        n_count = seq.count('N')
        n_ratio = n_count / length
        if n_ratio > max_n_ratio:
            return False, f"N比例太高（{n_ratio*100:.1f}%）"
        
        # 检查是否只包含ATCGN
        valid_with_n = set('ATCGN')
        if not set(seq).issubset(valid_with_n):
            invalid = set(seq) - valid_with_n
            return False, f"包含无效字符: {invalid}"
        
        return True, "通过质量控制"
    
    # 测试高级验证
    test_seq = "ATCGATCGNNN"
    is_valid, message = validate_sequence(test_seq)
    print(f"测试序列: {test_seq}")
    print(f"验证结果: {'✅' if is_valid else '❌'} {message}")
    
    print("\n💡 知识点：")
    print("- 数据质量控制是分析的第一步")
    print("- N代表未确定的碱基")
    print("- 不同应用对质量要求不同")


def challenge_comprehensive_analysis():
    """
    挑战题答案：综合序列分析
    
    学习重点：完整的分析流程
    """
    print("\n" + "="*50)
    print("挑战题答案：综合序列分析")
    print("="*50)
    
    print("场景：完整分析未知基因序列")
    
    # 未知序列
    unknown_seq = "atgGATTTATCTgctcttcgcgTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCtaa"
    
    print(f"原始序列({len(unknown_seq)} bp):")
    print(unknown_seq)
    
    # 任务1：数据清理和标准化
    print("\n任务1：数据清理")
    print("-" * 30)
    
    clean_seq = unknown_seq.upper()
    print(f"标准化后: {clean_seq}")
    
    # 检查序列质量
    valid_bases = set('ATCG')
    seq_bases = set(clean_seq)
    is_valid = seq_bases.issubset(valid_bases)
    print(f"序列验证: {'✅ 只包含ATCG' if is_valid else '❌ 包含其他字符'}")
    
    # 任务2：基本统计
    print("\n任务2：基本统计")
    print("-" * 30)
    
    length = len(clean_seq)
    a_count = clean_seq.count('A')
    t_count = clean_seq.count('T')
    c_count = clean_seq.count('C')
    g_count = clean_seq.count('G')
    
    print(f"序列长度: {length} bp")
    print(f"碱基组成:")
    for base, count in [('A', a_count), ('T', t_count), 
                        ('C', c_count), ('G', g_count)]:
        percentage = (count / length) * 100
        print(f"  {base}: {count:2d} ({percentage:5.1f}%)")
    
    # 任务3：计算GC和AT含量
    print("\n任务3：GC/AT含量")
    print("-" * 30)
    
    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100
    
    print(f"GC含量: {gc_content:.1f}%")
    print(f"AT含量: {at_content:.1f}%")
    
    # 任务4：查找生物学特征
    print("\n任务4：生物学特征")
    print("-" * 30)
    
    # 起始密码子
    has_start = "ATG" in clean_seq
    start_positions = []
    if has_start:
        # 找出所有ATG的位置
        pos = -1
        while True:
            pos = clean_seq.find("ATG", pos + 1)
            if pos == -1:
                break
            start_positions.append(pos)
    
    print(f"起始密码子(ATG): {'✅ 有' if has_start else '❌ 无'}")
    if start_positions:
        print(f"  位置: {start_positions}")
    
    # 终止密码子
    stop_codons = ["TAA", "TAG", "TGA"]
    found_stops = []
    stop_positions = {}
    
    for stop in stop_codons:
        if stop in clean_seq:
            found_stops.append(stop)
            pos = clean_seq.find(stop)
            stop_positions[stop] = pos
    
    has_stop = len(found_stops) > 0
    print(f"终止密码子: {'✅ 有' if has_stop else '❌ 无'}")
    if found_stops:
        print(f"  找到: {found_stops}")
        for stop, pos in stop_positions.items():
            print(f"  {stop}位置: {pos}")
    
    # 任务5：提取ORF（开放阅读框）
    print("\n任务5：ORF分析")
    print("-" * 30)
    
    if has_start and has_stop:
        # 找第一个ATG
        first_atg = start_positions[0]
        
        # 找ATG之后的第一个终止密码子
        first_stop_pos = length
        first_stop_type = None
        
        for stop in stop_codons:
            pos = clean_seq.find(stop, first_atg)
            if pos != -1 and pos < first_stop_pos:
                first_stop_pos = pos
                first_stop_type = stop
        
        if first_stop_type:
            # 提取ORF
            orf = clean_seq[first_atg:first_stop_pos + 3]
            print(f"找到ORF:")
            print(f"  起始: ATG (位置 {first_atg})")
            print(f"  终止: {first_stop_type} (位置 {first_stop_pos})")
            print(f"  长度: {len(orf)} bp")
            print(f"  序列: {orf}")
            
            # 检查是否是3的倍数（完整密码子）
            if len(orf) % 3 == 0:
                print(f"  ✅ 完整的阅读框（{len(orf)//3}个密码子）")
            else:
                print(f"  ⚠️ 不完整的阅读框")
    
    # 任务6：生成分析报告
    print("\n" + "="*30)
    print("序列分析报告")
    print("="*30)
    
    print(f"📊 基本信息：")
    print(f"  序列长度: {length} bp")
    print(f"  GC含量: {gc_content:.1f}%")
    print(f"  AT含量: {at_content:.1f}%")
    
    print(f"\n🧬 序列特征：")
    print(f"  起始密码子: {'有' if has_start else '无'} ({len(start_positions)}个)")
    print(f"  终止密码子: {'有' if has_stop else '无'} ({len(found_stops)}个)")
    
    print(f"\n🔍 序列分类：")
    if gc_content < 40:
        origin = "低GC含量，可能来自真核生物的非编码区"
    elif gc_content < 50:
        origin = "中等GC含量，可能是哺乳动物编码序列"
    elif gc_content < 60:
        origin = "中高GC含量，可能是细菌或植物序列"
    else:
        origin = "高GC含量，可能来自极端环境微生物"
    print(f"  推测来源: {origin}")
    
    print(f"\n📝 总结：")
    if has_start and has_stop and length > 100:
        print("  这可能是一个完整的基因序列或其片段")
    elif has_start:
        print("  这可能是基因的5'端序列")
    elif has_stop:
        print("  这可能是基因的3'端序列")
    else:
        print("  这可能是非编码序列或基因内部片段")
    
    print("\n💡 学到的知识：")
    print("- 综合运用字符串操作方法")
    print("- 系统化的序列分析流程")
    print("- 生物学特征的识别")
    print("- 数据驱动的推理")


def main():
    """
    主函数：运行所有答案演示
    """
    print("="*60)
    print("Chapter 01: Python基础 - 练习题完整答案")
    print("="*60)
    print("\n这里展示了所有练习的详细解答。")
    print("每个答案都包含代码、解释和扩展知识。")
    
    # 热身
    print("\n🔥 热身题答案")
    warmup_print_dna()
    
    # 基础练习
    print("\n📚 基础练习答案")
    practice_1_simple_variables()
    practice_2_string_length()
    practice_3_string_upper_lower()
    practice_4_count_bases()
    
    # 进阶练习
    print("\n🚀 进阶练习答案")
    practice_5_calculate_at_content()
    practice_6_sequence_slicing()
    practice_7_find_pattern()
    
    # 综合练习
    print("\n💪 综合练习答案")
    practice_8_calculate_gc_content()
    practice_9_sequence_validation()
    
    # 挑战题
    print("\n🏆 挑战题答案")
    challenge_comprehensive_analysis()
    
    print("\n" + "="*60)
    print("学习总结")
    print("="*60)
    
    print("\n✅ 你已经掌握的技能：")
    skills = [
        "变量的创建和使用",
        "字符串的基本操作",
        "使用len()和count()",
        "字符串切片",
        "条件判断",
        "循环遍历",
        "数据验证",
        "GC含量计算",
        "序列特征识别"
    ]
    
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")
    
    print("\n📈 学习曲线：")
    print("入门 → 基础 → 进阶 → 综合 → 精通")
    print("  ↑")
    print("你在这里！")
    
    print("\n🎯 下一步建议：")
    print("1. 用真实的序列数据练习")
    print("2. 尝试修改代码，看看会发生什么")
    print("3. 将多个功能组合成完整的程序")
    print("4. 学习Chapter 02的数据结构")
    
    print("\n记住：编程是一项实践技能，")
    print("多写代码比多看书更重要！")
    print("\n继续加油！🧬")


if __name__ == "__main__":
    main()