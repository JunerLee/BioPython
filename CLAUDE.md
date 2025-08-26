# CLAUDE.md

该文件为 Claude Code (claude.ai/code) 在此代码库中工作提供指导。

## 项目概述

BioPython指南是一个专门为没有编程经验的生物学家和生物信息学研究者设计的综合Python教程。该教程通过DNA序列分析、基因表达分析和机器学习在生物学中的应用等实际生物信息学应用来教授Python。

## 常用命令

### 环境设置和代码运行
```bash
# 安装依赖（自动创建虚拟环境）
uv sync

# 运行章节示例
uv run python Chapter_XX_Topic/main.py

# 运行练习题
uv run python Chapter_XX_Topic/practice.py

# 查看解决方案
uv run python Chapter_XX_Topic/practice_solution.py

# 测试环境设置
uv run python Chapter_00_Environment/main.py
```

### 开发命令
```bash
# 代码格式化和检查
uv run black Chapter_XX_Topic/
uv run flake8 Chapter_XX_Topic/
uv run isort Chapter_XX_Topic/

# 类型检查
uv run mypy Chapter_XX_Topic/

# 运行测试（如有）
uv run pytest
```

### 包管理
```bash
# 添加新依赖
uv add <package_name>

# 添加开发依赖
uv add --dev <package_name>

# 更新依赖
uv lock --upgrade
```

## 架构和结构

### 章节组织
教程遵循渐进式学习结构：
- **第00-02章**: 基础篇（环境搭建、基础语法、数据结构）
- **第03-05章**: 核心编程（控制流、函数、文件IO）
- **第06-08章**: 数据分析（pandas入门、进阶pandas、数据可视化）
- **第09-10章**: 生物信息学应用（biopython、机器学习）

### 文件结构模式
每章遵循一致的结构：
- `README.md`: 包含生物学背景的全面教程内容
- `main.py`: 带有详细中文注释的交互式教学示例
- `practice.py`: 包含TODO标记和难度评级（⭐-⭐⭐⭐）的练习题
- `practice_solution.py`: 包含解释的完整解决方案

### 教学理念
- **生物学背景优先**: 每个编程概念都通过真实的生物学问题引入
- **渐进式复杂度**: 从基础概念开始，逐步构建到高级应用
- **交互式学习**: 代码设计为分步骤运行，带有用户输入提示
- **实际应用**: 专注于解决真实的生物信息学问题

## 重要依赖

### 核心科学计算包
- **pandas** (≥2.0.0): 数据分析和操作
- **numpy** (≥1.24.0): 数值计算
- **matplotlib** (≥3.7.0): 基础绘图
- **seaborn** (≥0.12.0): 统计可视化

### 生物信息学专用
- **biopython** (≥1.81): 生物序列分析
- **pyfaidx** (≥0.7.0): FASTA文件处理
- **scikit-learn** (≥1.3.0): 机器学习
- **statsmodels** (≥0.14.0): 统计建模和多重检验

### 开发工具
- **black**: 代码格式化 (行长度: 88)
- **isort**: 导入排序 (black配置)
- **flake8**: 代码检查
- **mypy**: 类型检查

## 数据文件
位于 `/data/` 目录中：
- `gene_expression.csv`: 用于pandas教程的基因表达矩阵
- `dna_sequence.fasta`: 用于biopython练习的DNA序列  
- `gff_features.gff`: 基因组注释数据
- `single_cell_sample.csv`: 机器学习章节的单细胞RNA-seq数据
- `cancer_clinical_data.csv`: 预测建模的临床数据

## 代码约定

### 语言使用
- **注释和文档**: 简体中文，便于教学理解
- **变量名**: 英文，保持代码可维护性
- **函数名**: 英文，使用描述性名称
- **打印语句**: 中文，方便学生理解输出

### 教育代码风格
- 详细注释解释每个步骤
- 交互式提示用于分步学习
- 打印中间结果展示数据转换过程
- 常见错误的错误处理示例
- 相关时提供多种解决方案

### 文件结构
- 使用一致的表情符号标题 (🧬, 🔬, 📊) 进行视觉组织
- 包含练习的难度评级
- 在技术实现前提供生物学背景
- 在注释中显示预期输出

## 特殊注意事项

### 目标受众
代码是为没有编程经验的生物学研究者编写的，因此：
- 初期避免高级编程模式
- 使用生物学类比解释编程概念
- 提供详尽的解释性注释
- 包含常见错误示例和解决方案

### 交互式设计
许多main.py文件使用 `input()` 进行分步学习：
- 在各部分之间等待用户确认
- 显示中间结果
- 允许参数实验

### 生物学真实性
- 使用真实基因名称（BRCA1、TP53、GAPDH等）
- 采用真实数据格式（FASTA、GFF、CSV）
- 引用真实的生物过程和应用
- 将编程概念与实际研究工作流程联系起来

## 开发指南

修改此教程时：
1. 在所有示例中保持生物学相关性
2. 保持教育进展完整（不要跳过基础概念）
3. 使用 `uv run` 测试所有代码以确保虚拟环境兼容性
4. 保持main.py文件的交互式特性
5. 更改代码示例时更新相应的README.md
6. 在章节内使用一致的难度递进