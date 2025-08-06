# test_package_usage.py
# 测试包的使用和相对导入

print("=" * 60)
print("测试包的使用和相对导入")
print("=" * 60)

# ==================== 1. 测试包的导入 ====================
print("\n1. 测试包的导入:")
print("-" * 40)

# 导入整个包
import my_package
print(f"包信息: {my_package.get_package_info()}")

# 从包中导入特定模块
from my_package import MathUtils, StringUtils, calculate_average
print(f"MathUtils.add(5, 3) = {MathUtils.add(5, 3)}")
print(f"StringUtils.reverse('Hello') = {StringUtils.reverse('Hello')}")
print(f"calculate_average([1, 2, 3, 4, 5]) = {calculate_average([1, 2, 3, 4, 5])}")

# 导入子包
from my_package.subpackage import AdvancedMath
print(f"AdvancedMath.factorial(5) = {AdvancedMath.factorial(5)}")
print(f"AdvancedMath.area_of_circle(3) = {AdvancedMath.area_of_circle(3)}")

# 导入深层子包
from my_package.subpackage.deep_subpackage import SpecialMath
print(f"SpecialMath.golden_ratio() = {SpecialMath.golden_ratio()}")
print(f"SpecialMath.euler_number() = {SpecialMath.euler_number()}")

# ==================== 2. 测试相对导入的效果 ====================
print("\n2. 测试相对导入的效果:")
print("-" * 40)

# 测试从不同层级访问相同的模块
print("从不同层级访问MathUtils:")
print(f"my_package.MathUtils.add(10, 20) = {my_package.MathUtils.add(10, 20)}")
print(f"my_package.subpackage.MathUtils.add(10, 20) = {my_package.subpackage.MathUtils.add(10, 20)}")
print(f"my_package.subpackage.deep_subpackage.MathUtils.add(10, 20) = {my_package.subpackage.deep_subpackage.MathUtils.add(10, 20)}")

# ==================== 3. 测试包的功能 ====================
print("\n3. 测试包的功能:")
print("-" * 40)

# 测试数学工具
print("数学工具测试:")
print(f"MathUtils.multiply(6, 7) = {MathUtils.multiply(6, 7)}")
print(f"MathUtils.power(2, 8) = {MathUtils.power(2, 8)}")
print(f"MathUtils.factorial(6) = {MathUtils.factorial(6)}")

# 测试字符串工具
print("\n字符串工具测试:")
print(f"StringUtils.count_words('Hello World Python') = {StringUtils.count_words('Hello World Python')}")
print(f"StringUtils.is_palindrome('A man a plan a canal Panama') = {StringUtils.is_palindrome('A man a plan a canal Panama')}")
print(f"StringUtils.capitalize_words('hello world') = {StringUtils.capitalize_words('hello world')}")
print(f"StringUtils.remove_duplicates('hello') = {StringUtils.remove_duplicates('hello')}")

# 测试高级数学工具
print("\n高级数学工具测试:")
print(f"AdvancedMath.combination(5, 2) = {AdvancedMath.combination(5, 2)}")
print(f"AdvancedMath.permutation(5, 2) = {AdvancedMath.permutation(5, 2)}")
print(f"AdvancedMath.fibonacci(10) = {AdvancedMath.fibonacci(10)}")

# 测试特殊数学工具
print("\n特殊数学工具测试:")
print(f"SpecialMath.catalan_number(4) = {SpecialMath.catalan_number(4)}")
print(f"SpecialMath.bell_number(4) = {SpecialMath.bell_number(4)}")
print(f"SpecialMath.sphere_volume(3) = {SpecialMath.sphere_volume(3)}")

# ==================== 4. 测试模块的__all__属性 ====================
print("\n4. 测试模块的__all__属性:")
print("-" * 40)

# 查看各个模块的公共接口
print(f"my_package.__all__ = {my_package.__all__}")
print(f"my_package.subpackage.__all__ = {my_package.subpackage.__all__}")
print(f"my_package.subpackage.deep_subpackage.__all__ = {my_package.subpackage.deep_subpackage.__all__}")

# ==================== 5. 演示包的层次结构 ====================
print("\n5. 演示包的层次结构:")
print("-" * 40)

def show_package_structure():
    """显示包的结构"""
    print("包结构:")
    print("my_package/")
    print("├── __init__.py")
    print("├── math_utils.py")
    print("├── string_utils.py")
    print("└── subpackage/")
    print("    ├── __init__.py")
    print("    ├── advanced_math.py")
    print("    └── deep_subpackage/")
    print("        ├── __init__.py")
    print("        └── special_math.py")

show_package_structure()

# ==================== 6. 演示相对导入的优势 ====================
print("\n6. 演示相对导入的优势:")
print("-" * 40)

print("相对导入的优势:")
print("1. 包名变化时不需要修改导入语句")
print("2. 导入路径更简洁")
print("3. 更符合包的层次结构")
print("4. 避免硬编码包名")

print("\n相对导入示例:")
print("在 my_package/__init__.py 中:")
print("  from .math_utils import MathUtils")
print("  from .string_utils import StringUtils")

print("\n在 my_package/subpackage/__init__.py 中:")
print("  from ..math_utils import MathUtils")
print("  from .advanced_math import AdvancedMath")

print("\n在 my_package/subpackage/deep_subpackage/special_math.py 中:")
print("  from ...math_utils import MathUtils")
print("  from ..advanced_math import AdvancedMath")

# ==================== 7. 实际应用示例 ====================
print("\n7. 实际应用示例:")
print("-" * 40)

def demonstrate_practical_usage():
    """演示实际应用"""
    
    # 计算器应用
    print("计算器应用:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"数字列表: {numbers}")
    print(f"平均值: {calculate_average(numbers)}")
    print(f"总和: {MathUtils.add(sum(numbers[:-1]), numbers[-1])}")
    print(f"乘积: {MathUtils.multiply(2, 3) * MathUtils.multiply(4, 5)}")
    
    # 文本处理应用
    print("\n文本处理应用:")
    text = "Hello World Python Programming"
    print(f"原始文本: {text}")
    print(f"反转文本: {StringUtils.reverse(text)}")
    print(f"单词数量: {StringUtils.count_words(text)}")
    print(f"首字母大写: {StringUtils.capitalize_words(text)}")
    
    # 数学计算应用
    print("\n数学计算应用:")
    print(f"5的阶乘: {AdvancedMath.factorial(5)}")
    print(f"斐波那契数列第10项: {AdvancedMath.fibonacci(10)}")
    print(f"C(5,2)组合数: {AdvancedMath.combination(5, 2)}")
    print(f"P(5,2)排列数: {AdvancedMath.permutation(5, 2)}")
    
    # 特殊数学应用
    print("\n特殊数学应用:")
    print(f"黄金比例: {SpecialMath.golden_ratio()}")
    print(f"欧拉数: {SpecialMath.euler_number()}")
    print(f"卡塔兰数C(4): {SpecialMath.catalan_number(4)}")
    print(f"贝尔数B(4): {SpecialMath.bell_number(4)}")

demonstrate_practical_usage()

print("\n" + "=" * 60)
print("包的使用和相对导入演示完成！")
print("=" * 60) 