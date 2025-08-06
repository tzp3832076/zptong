# my_package/__init__.py
# 包的初始化文件

# 包级别的变量
PACKAGE_VERSION = "1.0.0"
PACKAGE_AUTHOR = "AI助手"

# 从当前包的模块导入
from .math_utils import MathUtils, calculate_average, PI
from .string_utils import StringUtils

# 定义包的公共接口
__all__ = [
    'MathUtils',
    'StringUtils', 
    'calculate_average',
    'PI',
    'PACKAGE_VERSION',
    'PACKAGE_AUTHOR'
]

def get_package_info():
    """获取包信息"""
    return {
        "version": PACKAGE_VERSION,
        "author": PACKAGE_AUTHOR,
        "description": "一个演示用的Python包"
    }

print("my_package 包已初始化") 