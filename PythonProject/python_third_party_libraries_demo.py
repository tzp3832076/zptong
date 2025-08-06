# Python 第三方库完整演示文件
# 作者：AI助手
# 功能：展示Python第三方库的导入、matplotlib使用和pip用法

print("=" * 60)
print("Python 第三方库完整演示")
print("=" * 60)

# ==================== 1. 第三方库导入基础 ====================
print("\n1. 第三方库导入基础:")
print("-" * 40)

# 1.1 常见的第三方库导入方式
print("1.1 常见的第三方库导入方式:")

# 导入整个模块
import math
print(f"math模块: math.pi = {math.pi}")

# 导入特定函数/类
from math import sqrt, pi
print(f"直接导入: sqrt(16) = {sqrt(16)}, pi = {pi}")

# 使用别名
import math as m
print(f"使用别名: m.e = {m.e}")

# 导入所有内容（不推荐）
from math import *
print(f"导入所有: e = {e}, log(10) = {log(10)}")

# 1.2 第三方库的获取和安装
print("\n1.2 第三方库的获取和安装:")
print("主要来源:")
print("- PyPI (Python Package Index): https://pypi.org/")
print("- GitHub: 许多开源项目托管在这里")
print("- 官方文档: 各库的官方文档通常有安装说明")

print("\n安装方式:")
print("- pip install 包名")
print("- pip install 包名==版本号")
print("- pip install -U 包名  # 升级")
print("- pip install -r requirements.txt  # 批量安装")

# ==================== 2. matplotlib 使用演示 ====================
print("\n2. matplotlib 使用演示:")
print("-" * 40)

try:
    import matplotlib.pyplot as plt
    import numpy as np
    
    print("2.1 基础折线图:")
    
    # 创建数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    plt.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')
    
    # 设置图形属性
    plt.title('三角函数示例', fontsize=14, fontweight='bold')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 保存图片
    plt.savefig('trigonometric_functions.png', dpi=300, bbox_inches='tight')
    print("图片已保存为: trigonometric_functions.png")
    
    # 显示图形
    plt.close()
    print("图表已保存")
    
    print("\n2.2 散点图示例:")
    
    # 生成随机数据
    np.random.seed(42)
    x = np.random.randn(50)
    y = 2 * x + 1 + np.random.randn(50) * 0.5
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.6, color='green', s=50)
    plt.plot(x, 2 * x + 1, 'r-', linewidth=2, label='y = 2x + 1')
    plt.title('散点图示例', fontsize=14)
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
    print("图片已保存为: scatter_plot.png")
    plt.close()
    
    print("\n2.3 柱状图示例:")
    
    # 数据
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, values, color=['red', 'blue', 'green', 'orange', 'purple'])
    
    # 在柱子上添加数值标签
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                str(value), ha='center', va='bottom')
    
    plt.title('柱状图示例', fontsize=14)
    plt.xlabel('类别', fontsize=12)
    plt.ylabel('数值', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')
    print("图片已保存为: bar_chart.png")
    plt.close()
    
    print("\n2.4 饼图示例:")
    
    # 数据
    sizes = [30, 25, 20, 15, 10]
    labels = ['A组', 'B组', 'C组', 'D组', 'E组']
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('饼图示例', fontsize=14)
    plt.axis('equal')
    plt.savefig('pie_chart.png', dpi=300, bbox_inches='tight')
    print("图片已保存为: pie_chart.png")
    plt.close()
    
    print("\n2.5 子图示例:")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # 子图1: 折线图
    x = np.linspace(0, 5, 100)
    ax1.plot(x, np.sin(x))
    ax1.set_title('正弦函数')
    ax1.grid(True)
    
    # 子图2: 散点图
    x = np.random.randn(30)
    y = np.random.randn(30)
    ax2.scatter(x, y, alpha=0.6)
    ax2.set_title('随机散点图')
    ax2.grid(True)
    
    # 子图3: 柱状图
    categories = ['A', 'B', 'C']
    values = [10, 20, 15]
    ax3.bar(categories, values, color=['red', 'blue', 'green'])
    ax3.set_title('简单柱状图')
    
    # 子图4: 饼图
    sizes = [40, 30, 30]
    labels = ['A', 'B', 'C']
    ax4.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax4.set_title('简单饼图')
    
    plt.tight_layout()
    plt.savefig('subplots_example.png', dpi=300, bbox_inches='tight')
    print("图片已保存为: subplots_example.png")
    plt.close()
    
except ImportError:
    print("matplotlib未安装，请运行: pip install matplotlib")
    print("numpy未安装，请运行: pip install numpy")

# ==================== 3. pip 常见使用方法 ====================
print("\n3. pip 常见使用方法:")
print("-" * 40)

# 3.1 基本安装命令
print("3.1 基本安装命令:")
print("pip install 包名                    # 安装最新版本")
print("pip install 包名==版本号            # 安装指定版本")
print("pip install 包名>=版本号            # 安装大于等于指定版本")
print("pip install 包名~=版本号            # 安装兼容版本")

# 3.2 升级和卸载
print("\n3.2 升级和卸载:")
print("pip install -U 包名                 # 升级到最新版本")
print("pip install --upgrade 包名          # 升级包")
print("pip uninstall 包名                  # 卸载包")
print("pip uninstall -y 包名               # 卸载包（不确认）")

# 3.3 查看和管理
print("\n3.3 查看和管理:")
print("pip list                           # 查看已安装的所有包")
print("pip show 包名                      # 查看包的详细信息")
print("pip list --outdated                # 查看过期的包")
print("pip check                          # 检查包依赖关系")

# 3.4 依赖管理
print("\n3.4 依赖管理:")
print("pip freeze                         # 导出当前环境所有包")
print("pip freeze > requirements.txt      # 导出到文件")
print("pip install -r requirements.txt    # 从文件安装")
print("pip install -r requirements.txt --upgrade  # 升级安装")

# 3.5 搜索和下载
print("\n3.5 搜索和下载:")
print("pip search 关键词                  # 搜索包（已弃用）")
print("pip download 包名                  # 下载包但不安装")
print("pip download 包名 -d 目录          # 下载到指定目录")

# 3.6 配置和镜像
print("\n3.6 配置和镜像:")
print("pip config list                    # 查看配置")
print("pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple  # 设置镜像")
print("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名  # 临时使用镜像")

# ==================== 4. 实际应用示例 ====================
print("\n4. 实际应用示例:")
print("-" * 40)

# 4.1 创建requirements.txt文件
print("4.1 创建requirements.txt文件:")

requirements_content = """# 项目依赖文件
# 核心库
numpy>=1.21.0
matplotlib>=3.5.0
pandas>=1.3.0

# 数据处理
scipy>=1.7.0
scikit-learn>=1.0.0

# Web框架
flask>=2.0.0
requests>=2.25.0

# 数据库
sqlalchemy>=1.4.0
pymongo>=4.0.0

# 测试
pytest>=6.0.0
pytest-cov>=2.0.0

# 开发工具
black>=21.0.0
flake8>=3.9.0
"""

with open('requirements.txt', 'w', encoding='utf-8') as f:
    f.write(requirements_content)

print("已创建 requirements.txt 文件")

# 4.2 模拟包管理操作
print("\n4.2 模拟包管理操作:")

def simulate_pip_operations():
    """模拟pip操作"""
    operations = [
        ("安装包", "pip install numpy matplotlib pandas"),
        ("安装指定版本", "pip install numpy==1.21.0"),
        ("升级包", "pip install -U numpy"),
        ("查看已安装", "pip list"),
        ("查看包信息", "pip show numpy"),
        ("导出依赖", "pip freeze > requirements.txt"),
        ("批量安装", "pip install -r requirements.txt"),
        ("卸载包", "pip uninstall numpy"),
        ("检查依赖", "pip check"),
        ("搜索包", "pip search numpy")  # 已弃用
    ]
    
    for i, (operation, command) in enumerate(operations, 1):
        print(f"{i:2d}. {operation}: {command}")

simulate_pip_operations()

# ==================== 5. 常用第三方库推荐 ====================
print("\n5. 常用第三方库推荐:")
print("-" * 40)

print("5.1 数据处理和分析:")
print("- numpy: 数值计算基础库")
print("- pandas: 数据分析和处理")
print("- scipy: 科学计算")
print("- matplotlib: 数据可视化")
print("- seaborn: 统计图表")
print("- plotly: 交互式图表")

print("\n5.2 机器学习:")
print("- scikit-learn: 机器学习算法")
print("- tensorflow: 深度学习框架")
print("- pytorch: 深度学习框架")
print("- keras: 深度学习高级API")

print("\n5.3 Web开发:")
print("- flask: 轻量级Web框架")
print("- django: 全功能Web框架")
print("- fastapi: 现代Web API框架")
print("- requests: HTTP库")

print("\n5.4 数据库:")
print("- sqlalchemy: ORM框架")
print("- pymongo: MongoDB驱动")
print("- psycopg2: PostgreSQL驱动")
print("- pymysql: MySQL驱动")

print("\n5.5 工具库:")
print("- pillow: 图像处理")
print("- opencv-python: 计算机视觉")
print("- beautifulsoup4: 网页解析")
print("- selenium: 浏览器自动化")

# ==================== 6. 最佳实践 ====================
print("\n6. 最佳实践:")
print("-" * 40)

print("6.1 虚拟环境:")
print("- 为每个项目创建独立的虚拟环境")
print("- 使用 venv 或 virtualenv")
print("- 避免全局安装包")

print("\n6.2 版本管理:")
print("- 使用 requirements.txt 管理依赖")
print("- 指定版本号避免兼容性问题")
print("- 定期更新依赖包")

print("\n6.3 镜像源:")
print("- 使用国内镜像源加速下载")
print("- 推荐: 清华、阿里云、豆瓣镜像")
print("- 配置默认镜像源")

print("\n6.4 安全考虑:")
print("- 只安装可信来源的包")
print("- 定期检查包的安全漏洞")
print("- 使用虚拟环境隔离")

# ==================== 7. 故障排除 ====================
print("\n7. 故障排除:")
print("-" * 40)

print("7.1 常见问题:")
print("问题: pip install 失败")
print("解决: 检查网络连接，使用镜像源")

print("\n问题: 包版本冲突")
print("解决: 使用虚拟环境，检查依赖关系")

print("\n问题: 权限错误")
print("解决: 使用 --user 参数或虚拟环境")

print("\n问题: 包找不到")
print("解决: 检查包名拼写，确认包已发布")

print("\n7.2 调试命令:")
print("pip --version                    # 检查pip版本")
print("python -m pip --version          # 检查pip版本（推荐）")
print("pip list --format=freeze         # 查看已安装包（格式输出）")
print("pip show 包名                    # 查看包详细信息")
print("pip check                        # 检查依赖关系")

print("\n" + "=" * 60)
print("Python 第三方库演示完成！")
print("=" * 60)

# ==================== 8. 更多第三方库实际应用示例 ====================
print("\n8. 更多第三方库实际应用示例:")
print("-" * 40)

# 8.1 pandas 数据处理示例
print("\n8.1 pandas 数据处理示例:")
try:
    import pandas as pd
    import numpy as np
    
    # 创建示例数据
    data = {
        '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
        '年龄': [25, 30, 35, 28, 32],
        '工资': [5000, 6000, 7000, 5500, 6500],
        '部门': ['技术', '销售', '技术', '人事', '销售']
    }
    
    df = pd.DataFrame(data)
    print("原始数据:")
    print(df)
    
    # 基本统计
    print("\n基本统计信息:")
    print(df.describe())
    
    # 分组统计
    print("\n按部门分组统计:")
    dept_stats = df.groupby('部门').agg({
        '年龄': ['mean', 'count'],
        '工资': ['mean', 'sum']
    })
    print(dept_stats)
    
    # 数据筛选
    print("\n筛选技术部门员工:")
    tech_employees = df[df['部门'] == '技术']
    print(tech_employees)
    
    # 数据排序
    print("\n按工资降序排列:")
    sorted_df = df.sort_values('工资', ascending=False)
    print(sorted_df)
    
except ImportError:
    print("pandas未安装，请运行: pip install pandas")

# 8.2 requests 网络请求示例
print("\n8.2 requests 网络请求示例:")
try:
    import requests
    import json
    
    def demo_requests():
        """演示requests的基本用法"""
        
        # GET请求示例
        print("1. GET请求示例:")
        try:
            response = requests.get('https://httpbin.org/get', timeout=5)
            print(f"状态码: {response.status_code}")
            print(f"响应头: {dict(response.headers)}")
            print(f"响应内容: {response.text[:200]}...")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
        
        # POST请求示例
        print("\n2. POST请求示例:")
        try:
            data = {'name': '张三', 'age': 25}
            response = requests.post('https://httpbin.org/post', json=data, timeout=5)
            print(f"状态码: {response.status_code}")
            result = response.json()
            print(f"发送的数据: {result.get('json', {})}")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
        
        # 带参数的GET请求
        print("\n3. 带参数的GET请求:")
        try:
            params = {'q': 'python', 'page': 1}
            response = requests.get('https://httpbin.org/get', params=params, timeout=5)
            print(f"完整URL: {response.url}")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
    
    demo_requests()
    
except ImportError:
    print("requests未安装，请运行: pip install requests")

# 8.3 Pillow 图像处理示例
print("\n8.3 Pillow 图像处理示例:")
try:
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    
    def create_sample_image():
        """创建一个示例图像"""
        # 创建一个简单的图像
        width, height = 400, 300
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)
        
        # 绘制一些图形
        draw.rectangle([50, 50, 150, 150], fill='red', outline='black', width=2)
        draw.ellipse([200, 50, 300, 150], fill='blue', outline='black', width=2)
        draw.line([50, 200, 350, 200], fill='green', width=3)
        
        # 添加文字
        try:
            # 尝试使用默认字体
            font = ImageFont.load_default()
            draw.text((50, 250), "Pillow 图像处理示例", fill='black', font=font)
        except:
            draw.text((50, 250), "Pillow 图像处理示例", fill='black')
        
        return image
    
    # 创建并保存图像
    img = create_sample_image()
    img.save('sample_image.png')
    print("已创建示例图像: sample_image.png")
    
    # 图像处理示例
    print("\n图像处理操作:")
    
    # 调整大小
    resized_img = img.resize((200, 150))
    resized_img.save('resized_image.png')
    print("已保存调整大小后的图像: resized_image.png")
    
    # 旋转图像
    rotated_img = img.rotate(45)
    rotated_img.save('rotated_image.png')
    print("已保存旋转后的图像: rotated_image.png")
    
    # 转换为灰度
    gray_img = img.convert('L')
    gray_img.save('gray_image.png')
    print("已保存灰度图像: gray_image.png")
    
    # 获取图像信息
    print(f"\n图像信息:")
    print(f"尺寸: {img.size}")
    print(f"模式: {img.mode}")
    print(f"格式: {img.format}")
    
except ImportError:
    print("Pillow未安装，请运行: pip install Pillow")

# 8.4 虚拟环境管理示例
print("\n8.4 虚拟环境管理示例:")
print("创建虚拟环境:")
print("python -m venv myenv                    # 创建虚拟环境")
print("source myenv/bin/activate               # 激活虚拟环境 (Linux/Mac)")
print("myenv\\Scripts\\activate                 # 激活虚拟环境 (Windows)")
print("deactivate                              # 退出虚拟环境")

print("\n虚拟环境中的包管理:")
print("pip install --upgrade pip               # 升级pip")
print("pip install -r requirements.txt         # 安装依赖")
print("pip freeze > requirements.txt           # 导出依赖")

# 8.5 项目结构示例
print("\n8.5 推荐的项目结构:")
project_structure = """
my_project/
├── README.md                 # 项目说明
├── requirements.txt          # 项目依赖
├── setup.py                 # 安装配置
├── .gitignore               # Git忽略文件
├── src/                     # 源代码目录
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/                   # 测试目录
│   ├── __init__.py
│   └── test_main.py
├── docs/                    # 文档目录
├── data/                    # 数据目录
└── notebooks/               # Jupyter笔记本
"""

print(project_structure)

# ==================== 9. 高级主题 ====================
print("\n9. 高级主题:")
print("-" * 40)

# 9.1 包分发和发布
print("\n9.1 包分发和发布:")
print("发布到PyPI:")
print("pip install setuptools wheel twine    # 安装发布工具")
print("python setup.py sdist bdist_wheel    # 构建分发包")
print("twine upload dist/*                  # 上传到PyPI")

# 9.2 依赖管理工具
print("\n9.2 现代依赖管理工具:")
print("- pipenv: 结合pip和virtualenv")
print("- poetry: 现代Python依赖管理")
print("- pip-tools: 编译requirements文件")
print("- conda: 科学计算环境管理")

# 9.3 性能优化
print("\n9.3 性能优化建议:")
print("- 使用虚拟环境避免包冲突")
print("- 合理使用requirements.txt指定版本")
print("- 定期更新依赖包")
print("- 使用镜像源加速下载")
print("- 考虑使用conda管理科学计算包")

# ==================== 10. 实用脚本示例 ====================
print("\n10. 实用脚本示例:")
print("-" * 40)

# 10.1 自动安装常用包
def create_install_script():
    """创建自动安装脚本"""
    script_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动安装常用Python包脚本
"""

import subprocess
import sys

def install_package(package):
    """安装单个包"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ {package} 安装成功")
    except subprocess.CalledProcessError:
        print(f"✗ {package} 安装失败")

def main():
    # 常用包列表
    packages = [
        "numpy",
        "pandas", 
        "matplotlib",
        "requests",
        "pillow",
        "flask",
        "pytest",
        "black",
        "flake8"
    ]
    
    print("开始安装常用Python包...")
    for package in packages:
        install_package(package)
    print("安装完成！")

if __name__ == "__main__":
    main()
'''
    
    with open('install_packages.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    print("已创建自动安装脚本: install_packages.py")

create_install_script()

# 10.2 包信息查看工具
def create_package_info_script():
    """创建包信息查看脚本"""
    script_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
包信息查看工具
"""

import subprocess
import sys
import json

def get_package_info(package_name):
    """获取包信息"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", package_name],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"包 {package_name} 未安装"
    except Exception as e:
        return f"获取包信息失败: {e}"

def list_installed_packages():
    """列出已安装的包"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=json"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            packages = json.loads(result.stdout)
            return packages
        else:
            return []
    except Exception as e:
        print(f"获取包列表失败: {e}")
        return []

def main():
    print("=== Python包信息查看工具 ===")
    
    # 列出所有已安装的包
    print("\\n已安装的包:")
    packages = list_installed_packages()
    for package in packages:
        print(f"- {package['name']} {package['version']}")
    
    # 查看特定包信息
    target_packages = ["numpy", "pandas", "matplotlib"]
    print("\\n特定包详细信息:")
    for package in target_packages:
        print(f"\\n{package}:")
        print(get_package_info(package))

if __name__ == "__main__":
    main()
'''
    
    with open('package_info.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    print("已创建包信息查看工具: package_info.py")

create_package_info_script()

# ==================== 11. 总结和最佳实践 ====================
print("\n11. 总结和最佳实践:")
print("-" * 40)

print("11.1 学习路径建议:")
print("1. 掌握基础库: numpy, pandas, matplotlib")
print("2. 学习Web开发: flask, requests")
print("3. 了解数据科学: scikit-learn, scipy")
print("4. 探索专业领域: 根据兴趣选择特定库")

print("\n11.2 开发环境建议:")
print("- 使用虚拟环境管理项目")
print("- 使用requirements.txt管理依赖")
print("- 配置国内镜像源加速下载")
print("- 定期更新和维护依赖包")

print("\n11.3 学习资源:")
print("- 官方文档: 各库的官方文档")
print("- PyPI: https://pypi.org/")
print("- GitHub: 查看源码和示例")
print("- 社区论坛: Stack Overflow, Reddit")

print("\n11.4 注意事项:")
print("- 注意包的版本兼容性")
print("- 关注包的安全性和维护状态")
print("- 合理使用第三方库，避免过度依赖")
print("- 保持学习新技术和库的习惯")

# ==================== 12. 扩展阅读 ====================
print("\n12. 扩展阅读:")
print("-" * 40)

print("12.1 推荐的进阶库:")
print("- FastAPI: 现代Web API框架")
print("- Streamlit: 数据应用快速开发")
print("- Jupyter: 交互式开发环境")
print("- PyTorch/TensorFlow: 深度学习")
print("- Django: 全功能Web框架")

print("\n12.2 专业领域库:")
print("- 数据科学: scikit-learn, scipy, statsmodels")
print("- 图像处理: opencv-python, scikit-image")
print("- 自然语言处理: nltk, spaCy, transformers")
print("- 网络爬虫: beautifulsoup4, scrapy, selenium")
print("- 自动化测试: pytest, unittest, robotframework")

print("\n12.3 工具和框架:")
print("- 代码质量: black, flake8, pylint")
print("- 类型检查: mypy")
print("- 文档生成: sphinx, pdoc")
print("- 打包分发: setuptools, wheel, twine")

print("\n" + "=" * 80)
print("Python 第三方库完整演示文件 - 全部内容完成！")
print("=" * 80)
print("感谢使用本演示文件！")
print("建议:")
print("1. 运行此文件查看所有演示效果")
print("2. 根据实际需求安装相关库")
print("3. 参考官方文档深入学习")
print("4. 在实践中不断提升技能")
print("=" * 80) 