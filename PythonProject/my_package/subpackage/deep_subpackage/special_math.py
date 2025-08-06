# my_package/subpackage/deep_subpackage/special_math.py
# 特殊数学模块

# 从上级包导入模块（使用相对导入）
from ...math_utils import MathUtils, PI
from ..advanced_math import AdvancedMath

class SpecialMath:
    """特殊数学工具类"""
    
    @staticmethod
    def golden_ratio():
        """计算黄金比例"""
        return (1 + 5 ** 0.5) / 2
    
    @staticmethod
    def euler_number():
        """计算欧拉数"""
        return 2.718281828459045
    
    @staticmethod
    def catalan_number(n):
        """计算卡塔兰数"""
        if n <= 1:
            return 1
        result = 0
        for i in range(n):
            result += SpecialMath.catalan_number(i) * SpecialMath.catalan_number(n - 1 - i)
        return result
    
    @staticmethod
    def bell_number(n):
        """计算贝尔数"""
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        # 使用动态规划计算
        bell = [[0] * (n + 1) for _ in range(n + 1)]
        bell[0][0] = 1
        
        for i in range(1, n + 1):
            bell[i][0] = bell[i - 1][i - 1]
            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
        
        return bell[n][0]
    
    @staticmethod
    def calculate_complex_series(n):
        """计算复杂级数"""
        # 使用从上级包导入的函数
        return AdvancedMath.calculate_series_sum(n, lambda x: 1 / (x ** 2))
    
    @staticmethod
    def sphere_volume(radius):
        """计算球体体积"""
        return (4/3) * PI * radius ** 3

# 模块的公共接口
__all__ = [
    'SpecialMath'
] 