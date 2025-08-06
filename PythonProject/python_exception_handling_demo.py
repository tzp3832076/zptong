# Python 异常处理完整演示文件
# 作者：AI助手
# 功能：展示Python的各种异常处理机制

print("=" * 60)
print("Python 异常处理完整演示")
print("=" * 60)

# ==================== 1. 基本异常处理 ====================
print("\n1. 基本异常处理:")
print("-" * 40)

# 1.1 try-except 基本语法
print("1.1 try-except 基本语法:")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("捕获到除零错误")

try:
    value = int("abc")
except ValueError:
    print("捕获到值错误：无法将字符串转换为整数")

try:
    undefined_variable + 1
except NameError:
    print("捕获到名称错误：变量未定义")

# 1.2 捕获多个异常
print("\n1.2 捕获多个异常:")

try:
    # 可能产生多种异常的操作
    user_input = "abc"
    number = int(user_input)
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"捕获到错误: {e}")

# 1.3 分别处理不同类型的异常
print("\n1.3 分别处理不同类型的异常:")

def process_data(data):
    try:
        if isinstance(data, str):
            return int(data)
        elif isinstance(data, (int, float)):
            return data / 0
        else:
            return data[0]  # 可能产生IndexError
    except ValueError as e:
        print(f"值错误: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"除零错误: {e}")
        return None
    except IndexError as e:
        print(f"索引错误: {e}")
        return None
    except Exception as e:
        print(f"其他错误: {e}")
        return None

# 测试不同类型的错误
print("测试字符串转整数:")
process_data("abc")

print("测试除零错误:")
process_data(10)

print("测试索引错误:")
process_data([])

# ==================== 2. try-except-else ====================
print("\n2. try-except-else:")
print("-" * 40)

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    except TypeError:
        print("错误：参数必须是数字")
        return None
    else:
        print("计算成功，没有发生异常")
        return result

print("测试正常情况:")
result = divide_numbers(10, 2)
print(f"结果: {result}")

print("\n测试除零错误:")
result = divide_numbers(10, 0)
print(f"结果: {result}")

print("\n测试类型错误:")
result = divide_numbers("10", 2)
print(f"结果: {result}")

# ==================== 3. try-except-finally ====================
print("\n3. try-except-finally:")
print("-" * 40)

def file_operation(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"文件内容: {content}")
        return content
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
        return None
    except PermissionError:
        print(f"错误：没有权限读取文件 '{filename}'")
        return None
    finally:
        if file:
            file.close()
            print("文件已关闭")

print("测试文件操作（文件不存在）:")
file_operation("nonexistent.txt")

# 模拟文件操作
import tempfile
import os

# 创建临时文件
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write("Hello, World!")
    temp_filename = temp_file.name

print(f"\n测试文件操作（文件存在）:")
file_operation(temp_filename)

# 清理临时文件
os.unlink(temp_filename)

# ==================== 4. 异常信息获取 ====================
print("\n4. 异常信息获取:")
print("-" * 40)

import traceback

def demonstrate_exception_info():
    try:
        # 故意产生一个异常
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"异常类型: {type(e).__name__}")
        print(f"异常信息: {e}")
        print(f"异常详细信息: {str(e)}")
        print("完整堆栈跟踪:")
        traceback.print_exc()

demonstrate_exception_info()

# ==================== 5. 自定义异常 ====================
print("\n5. 自定义异常:")
print("-" * 40)

# 5.1 基本自定义异常
class ValidationError(Exception):
    """自定义验证错误异常"""
    pass

class AgeError(ValidationError):
    """年龄验证错误"""
    def __init__(self, age, message="年龄无效"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class EmailError(ValidationError):
    """邮箱验证错误"""
    def __init__(self, email, message="邮箱格式无效"):
        self.email = email
        self.message = message
        super().__init__(self.message)

# 5.2 使用自定义异常
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0:
        raise AgeError(age, "年龄不能为负数")
    if age > 150:
        raise AgeError(age, "年龄不能超过150岁")
    return True

def validate_email(email):
    if not isinstance(email, str):
        raise TypeError("邮箱必须是字符串")
    if '@' not in email:
        raise EmailError(email, "邮箱必须包含@符号")
    if '.' not in email.split('@')[1]:
        raise EmailError(email, "邮箱格式不正确")
    return True

# 测试自定义异常
print("测试年龄验证:")
try:
    validate_age(-5)
except AgeError as e:
    print(f"年龄错误: {e.message}, 年龄值: {e.age}")
except TypeError as e:
    print(f"类型错误: {e}")

print("\n测试邮箱验证:")
try:
    validate_email("invalid-email")
except EmailError as e:
    print(f"邮箱错误: {e.message}, 邮箱值: {e.email}")

# ==================== 6. 异常链 (Exception Chaining) ====================
print("\n6. 异常链 (Exception Chaining):")
print("-" * 40)

def process_user_data(user_data):
    try:
        # 模拟数据处理
        if not user_data:
            raise ValueError("用户数据为空")
        
        # 模拟数据库操作
        if user_data.get('id') is None:
            raise KeyError("用户ID缺失")
        
        return user_data
        
    except (ValueError, KeyError) as e:
        # 重新抛出异常，保持异常链
        raise RuntimeError(f"处理用户数据时发生错误: {e}") from e

# 测试异常链
print("测试异常链:")
try:
    process_user_data({})
except RuntimeError as e:
    print(f"捕获到运行时错误: {e}")
    print(f"原始异常: {e.__cause__}")

# ==================== 7. 上下文管理器 (with语句) ====================
print("\n7. 上下文管理器 (with语句):")
print("-" * 40)

# 7.1 使用内置的上下文管理器
print("7.1 使用内置的上下文管理器:")

# 文件操作
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write("测试内容")
    temp_filename = temp_file.name

try:
    with open(temp_filename, 'r') as file:
        content = file.read()
        print(f"文件内容: {content}")
finally:
    os.unlink(temp_filename)

# 7.2 自定义上下文管理器
print("\n7.2 自定义上下文管理器:")

class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        print(f"连接到数据库 {self.host}:{self.port}")
        self.connection = "模拟连接"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        self.connection = None
        if exc_type is not None:
            print(f"数据库操作发生错误: {exc_val}")
        return False  # 不抑制异常

# 使用自定义上下文管理器
with DatabaseConnection("localhost", 5432) as conn:
    print(f"使用连接: {conn}")
    # 模拟正常操作
    print("执行数据库操作...")

# 测试异常情况
print("\n测试异常情况:")
try:
    with DatabaseConnection("localhost", 5432) as conn:
        print(f"使用连接: {conn}")
        # 模拟异常操作
        raise ValueError("数据库操作失败")
except ValueError as e:
    print(f"捕获到异常: {e}")

# ==================== 8. 异常处理的最佳实践 ====================
print("\n8. 异常处理的最佳实践:")
print("-" * 40)

# 8.1 具体异常优于通用异常
print("8.1 具体异常优于通用异常:")

def bad_practice():
    try:
        result = 10 / 0
    except Exception:  # 不推荐
        print("发生错误")

def good_practice():
    try:
        result = 10 / 0
    except ZeroDivisionError:  # 推荐
        print("除零错误")
    except Exception as e:
        print(f"其他错误: {e}")

print("好的实践示例:")
good_practice()

# 8.2 异常处理的位置
print("\n8.2 异常处理的位置:")

def process_data_safely(data_list):
    """在合适的层级处理异常"""
    results = []
    
    for i, data in enumerate(data_list):
        try:
            # 处理单个数据项
            result = int(data)
            results.append(result)
        except ValueError:
            print(f"跳过无效数据项 {i}: {data}")
            continue
        except Exception as e:
            print(f"处理数据项 {i} 时发生未知错误: {e}")
            continue
    
    return results

test_data = ["1", "2", "abc", "3", "def", "4"]
print(f"测试数据: {test_data}")
results = process_data_safely(test_data)
print(f"处理结果: {results}")

# 8.3 资源清理
print("\n8.3 资源清理:")

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None
    
    def acquire(self):
        print(f"获取资源: {self.name}")
        self.resource = f"资源_{self.name}"
        return self.resource
    
    def release(self):
        if self.resource:
            print(f"释放资源: {self.name}")
            self.resource = None

def use_resource_with_cleanup():
    resource_manager = ResourceManager("数据库连接")
    
    try:
        resource = resource_manager.acquire()
        print(f"使用资源: {resource}")
        
        # 模拟可能出错的操作
        if "数据库" in resource:
            raise RuntimeError("数据库操作失败")
        
        return "操作成功"
    
    except Exception as e:
        print(f"操作失败: {e}")
        raise
    finally:
        resource_manager.release()

print("测试资源清理:")
try:
    result = use_resource_with_cleanup()
    print(f"结果: {result}")
except RuntimeError as e:
    print(f"捕获到异常: {e}")

# ==================== 9. 实际应用示例 ====================
print("\n9. 实际应用示例:")
print("-" * 40)

# 9.1 网络请求异常处理
print("9.1 网络请求异常处理:")

import urllib.request
import urllib.error

def fetch_url_safely(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f"网络错误: {e}")
        return None
    except urllib.error.HTTPError as e:
        print(f"HTTP错误 {e.code}: {e.reason}")
        return None
    except TimeoutError:
        print("请求超时")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 测试网络请求（使用一个不存在的URL来演示错误处理）
print("测试网络请求错误处理:")
result = fetch_url_safely("http://nonexistent.example.com")
if result is None:
    print("请求失败")

# 9.2 数据验证和转换
print("\n9.2 数据验证和转换:")

def safe_data_conversion(data, target_type):
    """安全的数据类型转换"""
    try:
        if target_type == int:
            return int(data)
        elif target_type == float:
            return float(data)
        elif target_type == bool:
            if isinstance(data, str):
                return data.lower() in ('true', '1', 'yes', 'on')
            return bool(data)
        else:
            return str(data)
    except (ValueError, TypeError) as e:
        print(f"转换失败: {e}")
        return None

# 测试数据转换
test_conversions = [
    ("123", int),
    ("abc", int),
    ("3.14", float),
    ("invalid", float),
    ("true", bool),
    ("false", bool),
    ("yes", bool),
    ("no", bool)
]

print("测试数据转换:")
for data, target_type in test_conversions:
    result = safe_data_conversion(data, target_type)
    print(f"'{data}' -> {target_type.__name__}: {result}")

# 9.3 配置加载
print("\n9.3 配置加载:")

import json

def load_config_safely(config_file):
    """安全地加载配置文件"""
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)
            print(f"成功加载配置文件: {config_file}")
            return config
    except FileNotFoundError:
        print(f"配置文件不存在: {config_file}")
        return {}
    except json.JSONDecodeError as e:
        print(f"配置文件格式错误: {e}")
        return {}
    except PermissionError:
        print(f"没有权限读取配置文件: {config_file}")
        return {}
    except Exception as e:
        print(f"加载配置文件时发生未知错误: {e}")
        return {}

# 测试配置加载
print("测试配置加载:")
config = load_config_safely("nonexistent_config.json")
print(f"配置内容: {config}")

# ==================== 10. 调试和日志 ====================
print("\n10. 调试和日志:")
print("-" * 40)

import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_with_logging(data):
    """带日志的异常处理"""
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(f"开始处理数据: {data}")
        
        if not data:
            raise ValueError("数据为空")
        
        result = int(data) * 2
        logger.info(f"处理成功，结果: {result}")
        return result
        
    except ValueError as e:
        logger.error(f"数据验证失败: {e}")
        return None
    except Exception as e:
        logger.exception(f"处理数据时发生未知错误: {e}")
        return None

# 测试带日志的异常处理
print("测试带日志的异常处理:")
process_with_logging("123")
process_with_logging("abc")
process_with_logging("")

print("\n" + "=" * 60)
print("Python 异常处理演示完成！")
print("=" * 60) 