# my_package/subpackage/deep_subpackage/__init__.py
# 深层子包的初始化文件

# 从上级包导入模块（使用相对导入）
from ...math_utils import MathUtils, calculate_average, PI
from ...string_utils import StringUtils
from ..advanced_math import AdvancedMath
from .special_math import SpecialMath

# 定义深层子包的公共接口
__all__ = [
    'MathUtils',
    'StringUtils',
    'AdvancedMath',
    'SpecialMath',
    'calculate_average',
    'PI'
]

print("my_package.subpackage.deep_subpackage 深层子包已初始化") 