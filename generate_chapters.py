#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速生成剩余章节的脚本
"""

import os

# 章节配置
CHAPTERS = {
    "Chapter_03_ControlFlow": {
        "title": "控制流",
        "topic": "查找启动子序列ATG",
        "concepts": "for循环、if条件、while循环",
        "scenario": "启动子和转录起始位点的识别是基因分析的重要步骤"
    },
    "Chapter_04_Functions": {
        "title": "函数",
        "topic": "封装GC含量计算/DNA转RNA",
        "concepts": "函数定义、参数传递、返回值",
        "scenario": "函数化编程提高代码复用性和可维护性"
    },
    "Chapter_05_FileIO": {
        "title": "文件操作",
        "topic": "解析FASTA文件",
        "concepts": "文件读写、异常处理、数据格式",
        "scenario": "生物信息学数据通常以标准格式存储在文件中"
    },
    "Chapter_06_Pandas_Intro": {
        "title": "Pandas入门", 
        "topic": "读取基因表达数据",
        "concepts": "DataFrame、Series、数据读取",
        "scenario": "基因表达数据分析是转录组学的核心内容"
    },
    "Chapter_07_Pandas_Process": {
        "title": "Pandas数据处理",
        "topic": "筛选差异表达基因",
        "concepts": "数据筛选、排序、计算、分组",
        "scenario": "识别差异表达基因是转录组分析的关键步骤"
    },
    "Chapter_08_Visualization": {
        "title": "数据可视化",
        "topic": "绘制火山图/热图",
        "concepts": "matplotlib、seaborn、plotly",
        "scenario": "数据可视化帮助理解复杂的生物学数据模式"
    },
    "Chapter_09_Biopython": {
        "title": "Biopython",
        "topic": "序列反向互补",
        "concepts": "SeqIO、Seq对象、序列操作",
        "scenario": "Biopython是Python生物信息学的专业工具包"
    },
    "Chapter_10_MachineLearning": {
        "title": "机器学习",
        "topic": "样本K-Means聚类",
        "concepts": "scikit-learn、聚类分析、数据预处理",
        "scenario": "机器学习在生物数据挖掘中发挥重要作用"
    }
}

def create_readme(chapter_dir, chapter_info):
    """创建章节README文件"""
    content = f"""# {chapter_info['title']}

## 学习目标
- 掌握{chapter_info['concepts']}
- 学会应用于{chapter_info['topic']}
- 理解在生物信息学中的实际应用

## 生物学场景
{chapter_info['scenario']}。

## 核心概念
{chapter_info['concepts']}

## 代码实战
查看 `main.py` 了解具体实现方法。

## 练习题目
完成 `practice.py` 中的练习题。

## 知识总结
- ✅ 掌握{chapter_info['title']}的基本语法
- ✅ 理解在生物信息学中的应用
- ✅ 能够解决实际的生物数据问题

## 下一步
继续学习下一章节的内容。"""
    
    readme_path = os.path.join(chapter_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_main_py(chapter_dir, chapter_info):
    """创建主程序文件"""
    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{chapter_info['title']} - {chapter_info['topic']}

本脚本演示{chapter_info['concepts']}在生物信息学中的应用。
"""

def demonstrate_concepts():
    """
    演示{chapter_info['title']}的核心概念
    """
    print(f"🧬 {chapter_info['title']}演示")
    print("=" * 50)
    
    # TODO: 实现具体的演示代码
    print(f"主题: {chapter_info['topic']}")
    print(f"核心概念: {chapter_info['concepts']}")
    
    pass

def main():
    """
    主函数
    """
    print(f"🧬 {chapter_info['title']} - {chapter_info['topic']}")
    print(f"学习{chapter_info['concepts']}在生物信息学中的应用\\n")
    
    demonstrate_concepts()
    
    print("\\n" + "=" * 50)
    print("📚 本章学习要点:")
    print(f"1. {chapter_info['concepts']}的基本使用")
    print("2. 生物信息学实际应用场景")
    print("3. 最佳实践和注意事项")

if __name__ == "__main__":
    main()'''
    
    main_path = os.path.join(chapter_dir, "main.py")
    with open(main_path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_practice_py(chapter_dir, chapter_info):
    """创建练习文件"""
    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{chapter_info['title']} - 练习题

通过练习掌握{chapter_info['concepts']}在生物信息学中的应用。
"""

def practice_1():
    """
    练习1: 基础应用
    """
    print("🔍 练习1: 基础应用")
    print("-" * 40)
    
    # TODO: 完成基础练习
    pass

def practice_2():
    """
    练习2: 进阶应用
    """
    print("\\n🔍 练习2: 进阶应用")
    print("-" * 40)
    
    # TODO: 完成进阶练习
    pass

def main():
    """
    主函数: 运行所有练习题
    """
    print(f"🧬 {chapter_info['title']} 练习题")
    print(f"通过练习掌握{chapter_info['concepts']}的应用\\n")
    
    practice_1()
    practice_2()
    
    print("\\n" + "=" * 50)
    print("🎯 练习完成提示:")
    print("1. 完成所有TODO标记的代码")
    print("2. 运行程序检查结果")
    print("3. 对比参考答案")

if __name__ == "__main__":
    main()'''
    
    practice_path = os.path.join(chapter_dir, "practice.py")
    with open(practice_path, 'w', encoding='utf-8') as f:
        f.write(practice_path)

def create_solution_py(chapter_dir, chapter_info):
    """创建答案文件"""
    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{chapter_info['title']} - 练习题答案

提供完整的解决方案。
"""

def practice_1_solution():
    """
    练习1: 基础应用 - 完整解答
    """
    print("🔍 练习1: 基础应用 - 解答")
    print("-" * 40)
    
    # 完整的解决方案
    print("基础应用的完整实现...")
    
def practice_2_solution():
    """
    练习2: 进阶应用 - 完整解答
    """
    print("\\n🔍 练习2: 进阶应用 - 解答")
    print("-" * 40)
    
    # 完整的解决方案
    print("进阶应用的完整实现...")

def main():
    """
    主函数: 运行所有解答
    """
    print(f"🧬 {chapter_info['title']} 练习题完整解答")
    print("这里展示所有练习的标准答案\\n")
    
    practice_1_solution()
    practice_2_solution()

if __name__ == "__main__":
    main()'''
    
    solution_path = os.path.join(chapter_dir, "practice_solution.py")
    with open(solution_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """生成所有剩余章节"""
    base_dir = "E:\\workspace\\BioPythonGuide"
    
    for chapter_name, chapter_info in CHAPTERS.items():
        chapter_dir = os.path.join(base_dir, chapter_name)
        
        # 创建目录
        os.makedirs(chapter_dir, exist_ok=True)
        
        # 创建文件
        create_readme(chapter_dir, chapter_info)
        create_main_py(chapter_dir, chapter_info) 
        create_practice_py(chapter_dir, chapter_info)
        create_solution_py(chapter_dir, chapter_info)
        
        print(f"✅ 创建完成: {chapter_name}")
    
    print("\\n🎉 所有章节基础结构创建完成！")
    print("接下来需要完善每个章节的具体内容。")

if __name__ == "__main__":
    main()