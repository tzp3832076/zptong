# my_package/subpackage/advanced_math.py
# 高级数学模块

# 从上级包导入基础数学工具
from ..math_utils import MathUtils, PI

class AdvancedMath:
    """高级数学工具类"""
    
    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n <= 1:
            return 1
        return n * AdvancedMath.factorial(n - 1)
    
    @staticmethod
    def fibonacci(n):
        """计算斐波那契数列"""
        if n <= 1:
            return n
        return AdvancedMath.fibonacci(n - 1) + AdvancedMath.fibonacci(n - 2)
    
    @staticmethod
    def area_of_circle(radius):
        """计算圆的面积"""
        return PI * radius ** 2
    
    @staticmethod
    def combination(n, r):
        """计算组合数 C(n,r)"""
        if r > n:
            return 0
        return AdvancedMath.factorial(n) // (AdvancedMath.factorial(r) * AdvancedMath.factorial(n - r))
    
    @staticmethod
    def permutation(n, r):
        """计算排列数 P(n,r)"""
        if r > n:
            return 0
        return AdvancedMath.factorial(n) // AdvancedMath.factorial(n - r)

def calculate_series_sum(n, func):
    """计算级数和"""
    return sum(func(i) for i in range(1, n + 1))

def is_perfect_square(n):
    """判断是否为完全平方数"""
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

# 模块的公共接口
__all__ = [
    'AdvancedMath',
    'calculate_series_sum',
    'is_perfect_square'
] 