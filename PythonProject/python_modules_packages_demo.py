# Python 模块和包完整演示文件
# 作者：AI助手
# 功能：展示Python中模块和包的使用，以及相对导入

print("=" * 60)
print("Python 模块和包完整演示")
print("=" * 60)

# ==================== 1. 模块基础 ====================
print("\n1. 模块基础:")
print("-" * 40)

# 1.1 导入模块的不同方式
print("1.1 导入模块的不同方式:")

# 方式1：导入整个模块
import math
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# 方式2：从模块导入特定函数/变量
from math import pi, sqrt, cos
print(f"pi = {pi}")
print(f"sqrt(25) = {sqrt(25)}")
print(f"cos(0) = {cos(0)}")

# 方式3：导入所有内容（不推荐）
from math import *
print(f"e = {e}")
print(f"log(10) = {log(10)}")

# 方式4：导入时使用别名
import math as m
from math import sqrt as square_root
print(f"m.pi = {m.pi}")
print(f"square_root(36) = {square_root(36)}")

# 1.2 查看模块信息
print("\n1.2 查看模块信息:")
print(f"math模块的文档: {math.__doc__}")
print(f"math模块的文件路径: {math.__file__}")
print(f"math模块的名称: {math.__name__}")

# 1.3 模块的属性和方法
print("\n1.3 模块的属性和方法:")
print(f"math模块的所有属性: {dir(math)[:10]}...")  # 只显示前10个

# ==================== 2. 创建自定义模块 ====================
print("\n2. 创建自定义模块:")
print("-" * 40)

# 2.1 创建简单的数学工具模块
print("2.1 创建简单的数学工具模块:")

# 模拟一个数学工具模块的内容
class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def power(base, exponent):
        return base ** exponent

# 模块级别的函数
def calculate_average(numbers):
    """计算平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 模块级别的变量
PI = 3.14159
E = 2.71828
VERSION = "1.0.0"

# 2.2 使用自定义模块
print("2.2 使用自定义模块:")
print(f"MathUtils.add(5, 3) = {MathUtils.add(5, 3)}")
print(f"MathUtils.multiply(4, 7) = {MathUtils.multiply(4, 7)}")
print(f"calculate_average([1, 2, 3, 4, 5]) = {calculate_average([1, 2, 3, 4, 5])}")
print(f"is_prime(17) = {is_prime(17)}")
print(f"is_prime(24) = {is_prime(24)}")
print(f"PI = {PI}")
print(f"VERSION = {VERSION}")

# ==================== 3. 包的概念和结构 ====================
print("\n3. 包的概念和结构:")
print("-" * 40)

# 3.1 包的基本概念
print("3.1 包的基本概念:")
print("包是一个包含__init__.py文件的目录")
print("包可以包含多个模块和子包")
print("包提供了命名空间的组织方式")

# 3.2 模拟包的结构
print("\n3.2 模拟包的结构:")
print("my_package/")
print("├── __init__.py")
print("├── math_utils.py")
print("├── string_utils.py")
print("└── subpackage/")
print("    ├── __init__.py")
print("    └── advanced_math.py")

# 3.3 包的导入方式
print("\n3.3 包的导入方式:")

# 模拟包导入
class StringUtils:
    """字符串工具类"""
    
    @staticmethod
    def reverse(text):
        return text[::-1]
    
    @staticmethod
    def count_words(text):
        return len(text.split())
    
    @staticmethod
    def is_palindrome(text):
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

class AdvancedMath:
    """高级数学工具类"""
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * AdvancedMath.factorial(n - 1)
    
    @staticmethod
    def fibonacci(n):
        if n <= 1:
            return n
        return AdvancedMath.fibonacci(n - 1) + AdvancedMath.fibonacci(n - 2)

# 模拟包的使用
print("导入包中的模块:")
print(f"StringUtils.reverse('Hello') = {StringUtils.reverse('Hello')}")
print(f"StringUtils.count_words('Hello World Python') = {StringUtils.count_words('Hello World Python')}")
print(f"StringUtils.is_palindrome('A man a plan a canal Panama') = {StringUtils.is_palindrome('A man a plan a canal Panama')}")

print(f"AdvancedMath.factorial(5) = {AdvancedMath.factorial(5)}")
print(f"AdvancedMath.fibonacci(8) = {AdvancedMath.fibonacci(8)}")

# ==================== 4. __init__.py文件的作用 ====================
print("\n4. __init__.py文件的作用:")
print("-" * 40)

# 4.1 __init__.py的基本作用
print("4.1 __init__.py的基本作用:")
print("- 标识目录为Python包")
print("- 初始化包")
print("- 控制包的导入行为")
print("- 定义包的公共接口")

# 4.2 模拟__init__.py文件
print("\n4.2 模拟__init__.py文件:")

# 模拟包级别的变量
PACKAGE_VERSION = "2.0.0"
PACKAGE_AUTHOR = "AI助手"

# 模拟包级别的函数
def get_package_info():
    """获取包信息"""
    return {
        "version": PACKAGE_VERSION,
        "author": PACKAGE_AUTHOR,
        "description": "一个演示用的Python包"
    }

# 模拟从子模块导入特定内容
def import_public_interface():
    """导入公共接口"""
    print("导入包的公共接口...")
    return {
        "MathUtils": MathUtils,
        "StringUtils": StringUtils,
        "calculate_average": calculate_average,
        "is_prime": is_prime
    }

print(f"包信息: {get_package_info()}")
public_interface = import_public_interface()
print(f"公共接口: {list(public_interface.keys())}")

# ==================== 5. 相对导入详解 ====================
print("\n5. 相对导入详解:")
print("-" * 40)

# 5.1 相对导入的概念
print("5.1 相对导入的概念:")
print("相对导入使用点号(.)来表示相对路径")
print(". 表示当前目录")
print(".. 表示上级目录")
print("... 表示上上级目录")

# 5.2 相对导入的语法
print("\n5.2 相对导入的语法:")
print("from . import module_name")
print("from .module_name import function_name")
print("from .. import package_name")
print("from ..package_name import module_name")

# 5.3 模拟相对导入场景
print("\n5.3 模拟相对导入场景:")

# 模拟包结构
class PackageStructure:
    """模拟包结构"""
    
    def __init__(self):
        self.structure = {
            "my_package": {
                "__init__.py": "包初始化文件",
                "math_utils.py": "数学工具模块",
                "string_utils.py": "字符串工具模块",
                "subpackage": {
                    "__init__.py": "子包初始化文件",
                    "advanced_math.py": "高级数学模块",
                    "deep_subpackage": {
                        "__init__.py": "深层子包初始化文件",
                        "special_math.py": "特殊数学模块"
                    }
                }
            }
        }
    
    def show_import_examples(self):
        """显示导入示例"""
        examples = [
            "在 my_package/__init__.py 中:",
            "  from . import math_utils",
            "  from .math_utils import calculate_average",
            "",
            "在 my_package/subpackage/__init__.py 中:",
            "  from .. import math_utils",
            "  from ..math_utils import MathUtils",
            "",
            "在 my_package/subpackage/deep_subpackage/special_math.py 中:",
            "  from ... import math_utils",
            "  from ...math_utils import calculate_average",
            "  from .. import advanced_math"
        ]
        
        for example in examples:
            print(example)

package_structure = PackageStructure()
package_structure.show_import_examples()

# 5.4 相对导入的实际示例
print("\n5.4 相对导入的实际示例:")

# 模拟在不同层级使用相对导入
def demonstrate_relative_imports():
    """演示相对导入的使用"""
    
    # 模拟在包根目录的__init__.py中
    print("在包根目录的__init__.py中:")
    print("  from .math_utils import MathUtils, calculate_average")
    print("  from .string_utils import StringUtils")
    
    # 模拟在子包中的__init__.py中
    print("\n在子包的__init__.py中:")
    print("  from ..math_utils import MathUtils")
    print("  from ..string_utils import StringUtils")
    print("  from .advanced_math import AdvancedMath")
    
    # 模拟在深层子包中
    print("\n在深层子包中:")
    print("  from ...math_utils import MathUtils")
    print("  from ..advanced_math import AdvancedMath")
    print("  from .special_math import SpecialMath")

demonstrate_relative_imports()

# ==================== 6. 绝对导入 vs 相对导入 ====================
print("\n6. 绝对导入 vs 相对导入:")
print("-" * 40)

# 6.1 绝对导入
print("6.1 绝对导入:")
print("优点:")
print("- 明确清晰，容易理解")
print("- 不受包结构变化影响")
print("- 可以在任何地方使用")
print("缺点:")
print("- 导入路径可能很长")
print("- 包名变化时需要修改所有导入")

print("\n绝对导入示例:")
print("import my_package.math_utils")
print("from my_package.math_utils import MathUtils")
print("from my_package.subpackage.advanced_math import AdvancedMath")

# 6.2 相对导入
print("\n6.2 相对导入:")
print("优点:")
print("- 导入路径简洁")
print("- 包名变化时不需要修改")
print("- 更符合包的层次结构")
print("缺点:")
print("- 只能在包内部使用")
print("- 可能不够直观")
print("- 包结构变化时可能失效")

print("\n相对导入示例:")
print("from . import math_utils")
print("from .math_utils import MathUtils")
print("from .. import math_utils")
print("from ..math_utils import MathUtils")

# 6.3 选择建议
print("\n6.3 选择建议:")
print("- 在包内部使用相对导入")
print("- 在包外部使用绝对导入")
print("- 保持导入风格的一致性")
print("- 考虑代码的可维护性")

# ==================== 7. 模块和包的高级特性 ====================
print("\n7. 模块和包的高级特性:")
print("-" * 40)

# 7.1 模块重载
print("7.1 模块重载:")
import importlib

def demonstrate_reload():
    """演示模块重载"""
    print("模块重载用于开发时更新模块内容")
    print("importlib.reload(module_name)")
    print("注意：重载可能不会更新所有引用")

# 7.2 动态导入
print("\n7.2 动态导入:")
def dynamic_import(module_name):
    """动态导入模块"""
    try:
        module = __import__(module_name)
        print(f"成功导入模块: {module_name}")
        return module
    except ImportError as e:
        print(f"导入失败: {e}")
        return None

# 7.3 模块搜索路径
print("\n7.3 模块搜索路径:")
import sys
print("Python模块搜索路径:")
for i, path in enumerate(sys.path[:5]):  # 只显示前5个
    print(f"  {i+1}. {path}")
print("  ...")

# ==================== 8. 实际应用示例 ====================
print("\n8. 实际应用示例:")
print("-" * 40)

# 8.1 创建一个简单的工具包
print("8.1 创建一个简单的工具包:")

class SimpleTools:
    """简单工具包"""
    
    @staticmethod
    def format_number(number, decimal_places=2):
        """格式化数字"""
        return f"{number:.{decimal_places}f}"
    
    @staticmethod
    def validate_email(email):
        """验证邮箱格式"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def generate_id(prefix="ID"):
        """生成唯一ID"""
        import time
        import random
        timestamp = int(time.time() * 1000)
        random_num = random.randint(1000, 9999)
        return f"{prefix}_{timestamp}_{random_num}"

# 使用工具包
print("使用工具包:")
print(f"格式化数字: {SimpleTools.format_number(3.14159, 3)}")
print(f"验证邮箱: {SimpleTools.validate_email('test@example.com')}")
print(f"生成ID: {SimpleTools.generate_id('USER')}")

# 8.2 包的版本管理
print("\n8.2 包的版本管理:")

class VersionManager:
    """版本管理器"""
    
    def __init__(self):
        self.version = "1.0.0"
        self.changelog = {
            "1.0.0": ["初始版本", "基本功能实现"],
            "1.1.0": ["添加新功能", "修复已知问题"],
            "1.2.0": ["性能优化", "API改进"]
        }
    
    def get_version(self):
        return self.version
    
    def get_changelog(self, version=None):
        if version is None:
            version = self.version
        return self.changelog.get(version, [])
    
    def check_compatibility(self, required_version):
        """检查版本兼容性"""
        current = tuple(map(int, self.version.split('.')))
        required = tuple(map(int, required_version.split('.')))
        return current >= required

version_manager = VersionManager()
print(f"当前版本: {version_manager.get_version()}")
print(f"更新日志: {version_manager.get_changelog()}")
print(f"兼容性检查: {version_manager.check_compatibility('0.9.0')}")

# ==================== 9. 最佳实践 ====================
print("\n9. 最佳实践:")
print("-" * 40)

print("9.1 模块设计原则:")
print("- 单一职责原则：一个模块只负责一个功能")
print("- 高内聚低耦合：模块内部紧密相关，模块间松散耦合")
print("- 清晰的接口：提供明确的公共API")
print("- 适当的抽象：隐藏实现细节")

print("\n9.2 包组织建议:")
print("- 使用有意义的包名")
print("- 保持包的层次结构清晰")
print("- 在__init__.py中定义包的公共接口")
print("- 避免循环导入")

print("\n9.3 导入规范:")
print("- 标准库导入放在最前面")
print("- 第三方库导入放在中间")
print("- 本地模块导入放在最后")
print("- 使用绝对导入作为默认选择")
print("- 在包内部使用相对导入")

print("\n9.4 文档和注释:")
print("- 为每个模块编写文档字符串")
print("- 说明模块的用途和用法")
print("- 提供使用示例")
print("- 记录重要的API变更")

# ==================== 10. 常见问题和解决方案 ====================
print("\n10. 常见问题和解决方案:")
print("-" * 40)

print("10.1 循环导入问题:")
print("问题：模块A导入模块B，模块B又导入模块A")
print("解决方案：")
print("- 重新设计模块结构")
print("- 使用延迟导入")
print("- 将共同依赖提取到第三个模块")

print("\n10.2 相对导入错误:")
print("问题：在包外部使用相对导入")
print("解决方案：")
print("- 使用绝对导入")
print("- 确保在包内部使用相对导入")
print("- 检查__init__.py文件是否存在")

print("\n10.3 模块找不到:")
print("问题：ImportError: No module named 'xxx'")
print("解决方案：")
print("- 检查模块路径是否正确")
print("- 确保__init__.py文件存在")
print("- 检查PYTHONPATH环境变量")
print("- 使用sys.path.append()添加路径")

print("\n10.4 版本冲突:")
print("问题：不同版本的同一模块冲突")
print("解决方案：")
print("- 使用虚拟环境")
print("- 明确指定版本号")
print("- 使用包管理器管理依赖")

print("\n" + "=" * 60)
print("Python 模块和包演示完成！")
print("=" * 60) 