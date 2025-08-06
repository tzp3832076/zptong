# my_package/math_utils.py
# 数学工具模块

# 模块级别的常量
PI = 3.14159
E = 2.71828
VERSION = "1.0.0"

class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def add(a, b):
        """加法运算"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """乘法运算"""
        return a * b
    
    @staticmethod
    def power(base, exponent):
        """幂运算"""
        return base ** exponent
    
    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

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

def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 模块的公共接口
__all__ = [
    'MathUtils',
    'calculate_average',
    'is_prime',
    'fibonacci',
    'PI',
    'E',
    'VERSION'
] 