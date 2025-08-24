#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 00: 环境搭建 - 环境检测脚本（强化版）

这个脚本就像实验室的"开机自检"程序，确保所有仪器设备正常工作。
每次开始新的生物信息学项目前，都可以运行这个脚本检查环境状态。

学习要点：
- Shebang行（第1行）：告诉系统使用Python3解释器
- 编码声明（第2行）：支持中文和特殊字符
- 文档字符串（第3-7行）：描述文件的功能和用途
- import语句：导入需要的功能模块（像准备实验试剂）
- 函数定义：将代码组织成可重用的功能块
- if __name__ == "__main__"：程序的入口点
"""

# ========== 第一部分：导入模块 ==========
# 这部分就像准备实验前的试剂准备

# 标准库模块（Python自带，无需安装）
import sys                          # 系统相关功能（查看Python版本、路径等）
import platform                     # 平台信息（操作系统类型、版本等）
import subprocess                   # 执行系统命令（调用外部程序）
import os                          # 操作系统接口（环境变量、路径等）
import time                        # 时间相关功能（测量运行时间）
from pathlib import Path           # 现代化的路径处理（比os.path更好用）
from importlib import import_module # 动态导入模块（检查包是否安装）
from typing import Tuple, List, Dict  # 类型提示（让代码更清晰）

# ========== 第二部分：常量定义 ==========
# 就像实验中的标准参数

# 定义颜色代码（让输出更美观，像实验记录的高亮标记）
class Colors:
    """终端颜色代码（ANSI转义序列）"""
    HEADER = '\033[95m'    # 紫色 - 用于标题
    BLUE = '\033[94m'      # 蓝色 - 用于信息
    GREEN = '\033[92m'     # 绿色 - 用于成功
    YELLOW = '\033[93m'    # 黄色 - 用于警告
    RED = '\033[91m'       # 红色 - 用于错误
    ENDC = '\033[0m'       # 结束颜色
    BOLD = '\033[1m'       # 粗体
    UNDERLINE = '\033[4m'  # 下划线

# 检查是否支持颜色（Windows的旧版本可能不支持）
SUPPORTS_COLOR = sys.platform != 'win32' or 'ANSICON' in os.environ

def colored(text: str, color: str) -> str:
    """给文本添加颜色（如果终端支持）"""
    if SUPPORTS_COLOR and hasattr(Colors, color.upper()):
        color_code = getattr(Colors, color.upper())
        return f"{color_code}{text}{Colors.ENDC}"
    return text

# ========== 第三部分：辅助函数 ==========

def print_section_header(title: str, symbol: str = "=", width: int = 60) -> None:
    """
    打印格式化的章节标题
    
    这个函数就像实验记录本的章节分隔符，让输出更有条理。
    
    参数：
        title: 标题文字
        symbol: 分隔符号（默认使用=）
        width: 总宽度（默认60个字符）
    """
    # 计算标题两边需要多少个符号
    padding = (width - len(title) - 2) // 2
    line = symbol * width
    
    # 打印美观的标题框
    print()
    print(colored(line, "BLUE"))
    print(colored(f"{symbol * padding} {title} {symbol * (width - padding - len(title) - 2)}", "BLUE"))
    print(colored(line, "BLUE"))

def format_size(bytes_size: int) -> str:
    """
    将字节数转换为人类可读的格式
    
    就像将纳克转换为微克、毫克一样，让数字更易理解。
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"

# ========== 第四部分：核心检测函数 ==========

def check_python_version() -> Tuple[bool, str]:
    """
    检查Python版本（详细版）
    
    就像检查PCR仪的固件版本，确保支持所需的功能。
    
    返回：
        (是否满足要求, 详细信息)
    """
    print_section_header("🐍 Python环境检查")
    
    # 获取Python版本信息
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    # 检查是否在虚拟环境中
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    # 输出详细信息（像实验仪器的自检报告）
    print(f"Python版本: {colored(version_str, 'GREEN')}")
    print(f"详细版本: {sys.version}")
    print(f"可执行文件: {sys.executable}")
    print(f"安装路径: {sys.prefix}")
    
    if in_venv:
        print(colored("✅ 当前在虚拟环境中运行", "GREEN"))
        venv_path = Path(sys.prefix)
        print(f"   虚拟环境路径: {venv_path}")
        print(f"   虚拟环境名称: {venv_path.name}")
        
        # 计算虚拟环境大小
        try:
            total_size = sum(f.stat().st_size for f in venv_path.rglob('*') if f.is_file())
            print(f"   虚拟环境大小: {format_size(total_size)}")
        except:
            pass
    else:
        print(colored("⚠️  未检测到虚拟环境", "YELLOW"))
        print(colored("💡 建议: 使用 'uv sync' 创建虚拟环境", "YELLOW"))
    
    # 检查Python版本是否满足要求
    if version.major >= 3 and version.minor >= 8:
        if version.minor == 11:
            result = colored("✅ 使用推荐的Python 3.11版本", "GREEN")
            return True, result
        else:
            result = colored(f"✅ Python版本满足要求 (3.8+)", "GREEN")
            return True, result
    else:
        result = colored("❌ Python版本过低，需要3.8或更高版本", "RED")
        return False, result

def check_system_info() -> None:
    """
    检查系统信息（增强版）
    
    了解运行环境，就像了解实验室的温度、湿度等环境参数。
    """
    print_section_header("💻 系统信息检查")
    
    # 基本系统信息
    print(f"操作系统: {colored(platform.system(), 'GREEN')} {platform.release()}")
    print(f"系统版本: {platform.version()}")
    print(f"架构: {platform.machine()}")
    print(f"处理器: {platform.processor() or '未知'}")
    print(f"主机名: {platform.node()}")
    
    # Python实现信息
    print(f"\nPython实现: {platform.python_implementation()}")
    print(f"编译器: {platform.python_compiler()}")
    
    # 内存信息（如果可用）
    try:
        import psutil  # 可能未安装
        memory = psutil.virtual_memory()
        print(f"\n内存信息:")
        print(f"   总内存: {format_size(memory.total)}")
        print(f"   可用内存: {format_size(memory.available)}")
        print(f"   使用率: {memory.percent}%")
    except ImportError:
        print(colored("\n提示: 安装psutil可查看内存信息 (uv add psutil)", "YELLOW"))

def check_required_packages() -> Tuple[List[str], List[str]]:
    """
    检查必需的Python包（详细版）
    
    就像检查实验室的试剂库存，确保所有必需的"试剂"都已准备好。
    
    返回：
        (已安装的包列表, 缺失的包列表)
    """
    print_section_header("📦 Python包检查")
    
    # 定义需要检查的包及其用途
    required_packages = {
        'numpy': {
            'description': '数值计算库',
            'usage': '处理数组和矩阵运算',
            'bio_example': '处理序列相似度矩阵'
        },
        'pandas': {
            'description': '数据处理和分析库',
            'usage': '处理表格数据',
            'bio_example': '分析基因表达矩阵'
        },
        'matplotlib': {
            'description': '数据可视化库',
            'usage': '绘制图表',
            'bio_example': '绘制基因表达热图'
        },
        'seaborn': {
            'description': '统计数据可视化库',
            'usage': '美化统计图表',
            'bio_example': '绘制火山图、箱线图'
        },
        'Bio': {
            'description': 'Biopython生物信息学库',
            'usage': '处理生物序列数据',
            'bio_example': '读取FASTA文件、序列比对'
        },
        'sklearn': {
            'description': 'scikit-learn机器学习库',
            'usage': '机器学习算法',
            'bio_example': '基因表达聚类分析'
        }
    }
    
    installed_packages = []
    missing_packages = []
    
    print("检查核心包安装状态...\n")
    
    for package, info in required_packages.items():
        try:
            # 尝试导入包
            module = import_module(package)
            version = getattr(module, '__version__', '未知版本')
            
            # 获取包的安装路径
            package_path = getattr(module, '__file__', '未知路径')
            
            print(colored(f"✅ {package}", "GREEN"))
            print(f"   描述: {info['description']}")
            print(f"   版本: {version}")
            print(f"   用途: {info['usage']}")
            print(f"   生物学应用: {info['bio_example']}")
            print(f"   安装路径: {package_path}")
            print()
            
            installed_packages.append(package)
            
        except ImportError as e:
            print(colored(f"❌ {package}", "RED"))
            print(f"   描述: {info['description']}")
            print(f"   用途: {info['usage']}")
            print(f"   生物学应用: {info['bio_example']}")
            print(colored(f"   状态: 未安装", "RED"))
            print()
            
            missing_packages.append(package)
    
    # 统计结果
    total = len(required_packages)
    installed = len(installed_packages)
    print(f"包安装统计: {colored(f'{installed}/{total}', 'GREEN' if installed == total else 'YELLOW')}")
    
    return installed_packages, missing_packages

def check_uv_installation() -> bool:
    """
    检查uv包管理器（详细版）
    
    uv就像智能试剂管理系统，让包管理变得简单高效。
    """
    print_section_header("⚡ uv包管理器检查")
    
    try:
        # 检查uv版本
        result = subprocess.run(
            ['uv', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            version = result.stdout.strip()
            print(colored(f"✅ uv已安装: {version}", "GREEN"))
            
            # 检查uv配置
            print("\n检查uv功能...")
            
            # 列出可用的Python版本
            py_result = subprocess.run(
                ['uv', 'python', 'list'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if py_result.returncode == 0:
                print("可用的Python版本:")
                lines = py_result.stdout.strip().split('\n')[:5]  # 只显示前5个
                for line in lines:
                    print(f"   {line}")
            
            print(colored("\n💡 提示: 使用 'uv sync' 自动创建环境和安装依赖", "GREEN"))
            return True
            
        else:
            print(colored("❌ uv命令执行失败", "RED"))
            return False
            
    except FileNotFoundError:
        print(colored("❌ uv未安装或不在PATH中", "RED"))
        print("\n安装方法:")
        
        if sys.platform.startswith('win'):
            print("Windows系统:")
            print("  1. 打开PowerShell（管理员）")
            print("  2. 运行: irm https://astral.sh/uv/install.ps1 | iex")
        else:
            print("macOS/Linux系统:")
            print("  运行: curl -LsSf https://astral.sh/uv/install.sh | sh")
        
        return False
    
    except subprocess.TimeoutExpired:
        print(colored("❌ uv命令超时", "RED"))
        return False

def check_vscode_extensions() -> None:
    """
    检查VSCode及其扩展（如果VSCode已安装）
    
    VSCode就像智能实验记录本，让编程变得更高效。
    """
    print_section_header("📝 VSCode编辑器检查")
    
    try:
        # 检查VSCode是否安装
        result = subprocess.run(
            ['code', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if lines:
                print(colored(f"✅ VSCode已安装", "GREEN"))
                print(f"   版本: {lines[0]}")
            
            # 列出已安装的扩展
            ext_result = subprocess.run(
                ['code', '--list-extensions'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if ext_result.returncode == 0:
                extensions = ext_result.stdout.strip().split('\n')
                
                # 检查推荐的扩展
                recommended = {
                    'ms-python.python': 'Python基础支持',
                    'ms-python.vscode-pylance': 'Python智能提示',
                    'njpwerner.autodocstring': 'Python文档字符串生成器',
                    'eamodio.gitlens': 'Git版本控制增强',
                    'mechatroner.rainbow-csv': 'CSV文件美化',
                    'ms-toolsai.jupyter': 'Jupyter Notebook支持'
                }
                
                print("\n推荐的扩展检查:")
                for ext_id, description in recommended.items():
                    if ext_id in extensions:
                        print(colored(f"  ✅ {description}", "GREEN"))
                    else:
                        print(colored(f"  ❌ {description} (运行: code --install-extension {ext_id})", "YELLOW"))
        else:
            print(colored("❌ VSCode未安装或不在PATH中", "YELLOW"))
            print("下载地址: https://code.visualstudio.com/")
            
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print(colored("⚠️  无法检测VSCode", "YELLOW"))
        print("VSCode是推荐的Python编辑器")
        print("下载地址: https://code.visualstudio.com/")

def demonstrate_python_basics() -> None:
    """
    演示Python基础概念
    
    这部分展示Python程序的基本结构，帮助理解代码组织方式。
    """
    print_section_header("📚 Python基础概念演示")
    
    # 1. 变量和数据类型
    print(colored("1. 变量和数据类型（像试管标签）:", "BLUE"))
    dna_sequence = "ATCGATCG"  # 字符串类型
    sequence_length = len(dna_sequence)  # 整数类型
    gc_content = 50.0  # 浮点数类型
    is_valid = True  # 布尔类型
    
    print(f"   DNA序列: {dna_sequence} (类型: {type(dna_sequence).__name__})")
    print(f"   序列长度: {sequence_length} (类型: {type(sequence_length).__name__})")
    print(f"   GC含量: {gc_content}% (类型: {type(gc_content).__name__})")
    print(f"   是否有效: {is_valid} (类型: {type(is_valid).__name__})")
    
    # 2. 函数定义
    print(colored("\n2. 函数定义（像实验步骤）:", "BLUE"))
    
    def calculate_gc_content(sequence: str) -> float:
        """计算DNA序列的GC含量"""
        sequence = sequence.upper()
        gc_count = sequence.count('G') + sequence.count('C')
        return (gc_count / len(sequence)) * 100 if sequence else 0
    
    result = calculate_gc_content(dna_sequence)
    print(f"   函数调用: calculate_gc_content('{dna_sequence}')")
    print(f"   返回结果: {result}%")
    
    # 3. 条件判断
    print(colored("\n3. 条件判断（像实验决策）:", "BLUE"))
    if gc_content > 60:
        temp = "高温（~90°C）"
    elif gc_content > 40:
        temp = "中温（~85°C）"
    else:
        temp = "低温（~80°C）"
    print(f"   根据GC含量({gc_content}%)，建议PCR退火温度: {temp}")
    
    # 4. 循环结构
    print(colored("\n4. 循环结构（像重复实验）:", "BLUE"))
    codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]
    print(f"   密码子分割: {' '.join(codons)}")
    
    # 5. 模块导入
    print(colored("\n5. 当前已导入的模块:", "BLUE"))
    imported_modules = [name for name in sys.modules.keys() if not name.startswith('_')][:10]
    for module in imported_modules[:5]:  # 只显示前5个
        print(f"   - {module}")
    print(f"   ... 共{len(sys.modules)}个模块")

def generate_environment_report() -> None:
    """
    生成完整的环境检测报告
    
    这是主要的诊断函数，像实验室的综合体检报告。
    """
    print(colored("\n" + "="*60, "HEADER"))
    print(colored("      🧬 Python生物信息学环境检测工具 v2.0 🧬", "HEADER"))
    print(colored("="*60 + "\n", "HEADER"))
    
    print("本工具将全面检查您的Python生物信息学开发环境")
    print("检测过程大约需要10-30秒...\n")
    
    # 记录开始时间
    start_time = time.time()
    
    # 执行所有检查
    results = {}
    
    # 1. Python版本检查
    python_ok, python_msg = check_python_version()
    results['Python'] = python_ok
    
    # 2. 系统信息
    check_system_info()
    
    # 3. 包检查
    installed, missing = check_required_packages()
    results['Packages'] = len(missing) == 0
    
    # 4. uv检查
    uv_ok = check_uv_installation()
    results['uv'] = uv_ok
    
    # 5. VSCode检查
    check_vscode_extensions()
    
    # 6. Python基础演示
    demonstrate_python_basics()
    
    # 计算运行时间
    elapsed_time = time.time() - start_time
    
    # 生成最终报告
    print_section_header("📋 环境检测报告汇总")
    
    print(colored("检测结果:", "BLUE"))
    for component, status in results.items():
        icon = "✅" if status else "❌"
        color = "GREEN" if status else "RED"
        print(colored(f"  {icon} {component}", color))
    
    # 缺失包的处理建议
    if missing:
        print(colored(f"\n需要安装的包 ({len(missing)}个):", "YELLOW"))
        for pkg in missing:
            print(f"  - {pkg}")
        print(colored("\n安装方法:", "BLUE"))
        print("  1. 推荐: uv sync  (自动安装所有项目依赖)")
        print("  2. 单独安装: uv add " + " ".join(missing))
    
    # 总体评估
    all_ok = all(results.values()) and len(missing) == 0
    
    print(colored("\n" + "="*60, "BLUE"))
    if all_ok:
        print(colored("🎉 恭喜！您的Python生物信息学环境已完全就绪！", "GREEN"))
        print(colored("您可以开始愉快的生物信息学编程之旅了！", "GREEN"))
        print("\n下一步建议:")
        print("1. 运行练习题: python Chapter_00_Environment/practice.py")
        print("2. 开始Chapter 01的学习")
    else:
        print(colored("⚠️  您的环境还需要一些配置", "YELLOW"))
        print("\n建议按以下顺序解决:")
        if not results.get('Python'):
            print("1. 使用uv安装正确的Python版本")
        if not results.get('uv'):
            print("2. 安装uv包管理器")
        if missing:
            print("3. 运行 'uv sync' 安装缺失的包")
    
    print(colored("="*60, "BLUE"))
    print(f"\n检测用时: {elapsed_time:.2f} 秒")
    print(f"检测时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """
    主函数 - 程序的入口点
    
    这就像实验的主流程，协调所有步骤的执行。
    """
    try:
        # 运行环境检测
        generate_environment_report()
        
    except KeyboardInterrupt:
        # 用户按Ctrl+C中断
        print(colored("\n\n⚠️  检测被用户中断", "YELLOW"))
        print("如需完整检测，请重新运行程序")
        
    except Exception as e:
        # 其他异常
        print(colored(f"\n❌ 检测过程中出现错误: {e}", "RED"))
        print("请检查您的系统配置")
        print("\n错误详情:")
        import traceback
        traceback.print_exc()
    
    finally:
        # 无论如何都会执行的清理代码
        print(colored("\n感谢使用环境检测工具！", "BLUE"))
        print("如有问题，请参考README.md中的故障排除部分")

# ========== 程序入口点 ==========
# 这个条件确保代码只在直接运行时执行，被导入时不执行
if __name__ == "__main__":
    # 程序说明
    print(colored("启动环境检测...", "BLUE"))
    print("提示: 本程序会检查Python环境的各个方面")
    print("      整个过程是只读的，不会修改任何设置\n")
    
    # 调用主函数
    main()
    
    # 程序结束提示
    print(colored("\n按Enter键退出...", "BLUE"))
    input()  # 等待用户按键，防止窗口立即关闭