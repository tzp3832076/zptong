# my_package/subpackage/__init__.py
# 子包的初始化文件

# 从上级包导入模块
from ..math_utils import MathUtils, calculate_average
from ..string_utils import StringUtils

# 从当前子包导入模块
from .advanced_math import AdvancedMath

# 定义子包的公共接口
__all__ = [
    'MathUtils',
    'StringUtils',
    'AdvancedMath',
    'calculate_average'
]

print("my_package.subpackage 子包已初始化") 