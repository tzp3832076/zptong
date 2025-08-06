# Python 数据类型完整演示文件
# 作者：AI助手
# 功能：展示Python的各种数据类型、类型检查和类型转换

print("=" * 60)
print("Python 数据类型演示")
print("=" * 60)

# ==================== 1. 基本数据类型变量声明 ====================
print("\n1. 基本数据类型变量声明:")
print("-" * 40)

# 整数类型
age = 25
year = 2024
temperature = -5
population = 8000000000
print(f"age = {age}, 类型: {type(age)}")
print(f"year = {year}, 类型: {type(year)}")
print(f"temperature = {temperature}, 类型: {type(temperature)}")
print(f"population = {population}, 类型: {type(population)}")

# 浮点数类型
pi = 3.14159
e = 2.71828
salary = 8500.50
height = 1.75
print(f"pi = {pi}, 类型: {type(pi)}")
print(f"e = {e}, 类型: {type(e)}")
print(f"salary = {salary}, 类型: {type(salary)}")
print(f"height = {height}, 类型: {type(height)}")

# 布尔类型
is_student = True
is_working = False
has_car = True
is_married = False
print(f"is_student = {is_student}, 类型: {type(is_student)}")
print(f"is_working = {is_working}, 类型: {type(is_working)}")
print(f"has_car = {has_car}, 类型: {type(has_car)}")
print(f"is_married = {is_married}, 类型: {type(is_married)}")

# 字符串类型
name = "张三"
city = "北京"
email = "zhangsan@example.com"
message = "Hello, 世界！"
print(f"name = {name}, 类型: {type(name)}")
print(f"city = {city}, 类型: {type(city)}")
print(f"email = {email}, 类型: {type(email)}")
print(f"message = {message}, 类型: {type(message)}")

# None类型
empty_value = None
not_defined = None
print(f"empty_value = {empty_value}, 类型: {type(empty_value)}")
print(f"not_defined = {not_defined}, 类型: {type(not_defined)}")

# ==================== 2. 集合数据类型变量声明 ====================
print("\n2. 集合数据类型变量声明:")
print("-" * 40)

# 列表类型
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"fruits = {fruits}, 类型: {type(fruits)}")
print(f"numbers = {numbers}, 类型: {type(numbers)}")
print(f"mixed_list = {mixed_list}, 类型: {type(mixed_list)}")

# 元组类型
coordinates = (10, 20)
rgb_color = (255, 128, 0)
person_info = ("李四", 30, "工程师")
print(f"coordinates = {coordinates}, 类型: {type(coordinates)}")
print(f"rgb_color = {rgb_color}, 类型: {type(rgb_color)}")
print(f"person_info = {person_info}, 类型: {type(person_info)}")

# 集合类型
unique_numbers = {1, 2, 3, 4, 5}
programming_languages = {"Python", "Java", "JavaScript", "C++"}
print(f"unique_numbers = {unique_numbers}, 类型: {type(unique_numbers)}")
print(f"programming_languages = {programming_languages}, 类型: {type(programming_languages)}")

# 字典类型
student = {
    "name": "王五",
    "age": 22,
    "major": "计算机科学",
    "grades": [85, 92, 78, 95]
}
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "database": {
        "name": "mydb",
        "user": "admin"
    }
}
print(f"student = {student}, 类型: {type(student)}")
print(f"config = {config}, 类型: {type(config)}")

# ==================== 3. 其他数据类型变量声明 ====================
print("\n3. 其他数据类型变量声明:")
print("-" * 40)

# 字节类型
binary_data = b"Hello World"
image_data = b"\x89PNG\r\n\x1a\n"
print(f"binary_data = {binary_data}, 类型: {type(binary_data)}")
print(f"image_data = {image_data}, 类型: {type(image_data)}")

# 复数类型
complex_num1 = 3 + 4j
complex_num2 = complex(5, 6)
print(f"complex_num1 = {complex_num1}, 类型: {type(complex_num1)}")
print(f"complex_num2 = {complex_num2}, 类型: {type(complex_num2)}")

# ==================== 4. 类型转换案例 ====================
print("\n4. 类型转换案例:")
print("-" * 40)

# 4.1 字符串转换
print("\n4.1 字符串转换:")
num_str = "123"
float_str = "3.14"
bool_str = "True"
print(f"字符串 '{num_str}' 转整数: {int(num_str)}")
print(f"字符串 '{num_str}' 转浮点数: {float(num_str)}")
print(f"字符串 '{float_str}' 转浮点数: {float(float_str)}")
print(f"字符串 '{float_str}' 转整数: {int(float(float_str))}")
print(f"字符串 '{bool_str}' 转布尔值: {bool(bool_str)}")

# 4.2 数字类型转换
print("\n4.2 数字类型转换:")
num_int = 42
num_float = 3.7
print(f"整数 {num_int} 转浮点数: {float(num_int)}")
print(f"浮点数 {num_float} 转整数: {int(num_float)}")
print(f"整数 {num_int} 转复数: {complex(num_int)}")
print(f"浮点数 {num_float} 转复数: {complex(num_float)}")
print(f"整数 {num_int} 转字符串: {str(num_int)}")

# 4.3 布尔值转换
print("\n4.3 布尔值转换:")
print(f"整数 0 转布尔值: {bool(0)}")
print(f"整数 1 转布尔值: {bool(1)}")
print(f"整数 42 转布尔值: {bool(42)}")
print(f"空字符串转布尔值: {bool('')}")
print(f"非空字符串转布尔值: {bool('hello')}")
print(f"空列表转布尔值: {bool([])}")
print(f"非空列表转布尔值: {bool([1, 2, 3])}")
print(f"None转布尔值: {bool(None)}")

# 4.4 集合类型转换
print("\n4.4 集合类型转换:")
# 列表转元组
list_data = [1, 2, 3, 4, 5]
print(f"列表 {list_data} 转元组: {tuple(list_data)}")

# 元组转列表
tuple_data = (1, 2, 3, 4, 5)
print(f"元组 {tuple_data} 转列表: {list(tuple_data)}")

# 列表转集合
list_with_duplicates = [1, 2, 2, 3, 3, 4]
print(f"列表 {list_with_duplicates} 转集合: {set(list_with_duplicates)}")

# 字符串转列表
string_data = "Python"
print(f"字符串 '{string_data}' 转列表: {list(string_data)}")

# 4.5 字典相关转换
print("\n4.5 字典相关转换:")
# 键值对列表转字典
pairs = [('a', 1), ('b', 2), ('c', 3)]
print(f"键值对列表 {pairs} 转字典: {dict(pairs)}")

# 字典的键和值
print(f"字典 {student} 的键: {list(student.keys())}")
print(f"字典 {student} 的值: {list(student.values())}")
print(f"字典 {student} 的键值对: {list(student.items())}")

# 4.6 字节和字符串转换
print("\n4.6 字节和字符串转换:")
text = "Hello, 世界！"
print(f"字符串 '{text}' 转字节: {text.encode('utf-8')}")
print(f"字节转回字符串: {text.encode('utf-8').decode('utf-8')}")

# 4.7 特殊转换案例
print("\n4.7 特殊转换案例:")
# 十六进制字符串转整数
hex_str = "1A"
print(f"十六进制字符串 '{hex_str}' 转整数: {int(hex_str, 16)}")

# 二进制字符串转整数
bin_str = "1010"
print(f"二进制字符串 '{bin_str}' 转整数: {int(bin_str, 2)}")

# 浮点数转字符串（控制精度）
pi_value = 3.14159265359
print(f"浮点数 {pi_value} 转字符串（保留2位小数）: {format(pi_value, '.2f')}")
print(f"浮点数 {pi_value} 转字符串（科学计数法）: {format(pi_value, 'e')}")

# 4.8 错误处理示例
print("\n4.8 错误处理示例:")
try:
    invalid_int = int("abc")
except ValueError as e:
    print(f"转换错误: {e}")

try:
    invalid_float = float("not a number")
except ValueError as e:
    print(f"转换错误: {e}")

# 4.9 安全转换函数
print("\n4.9 安全转换函数:")
def safe_int_convert(value):
    """安全地将值转换为整数"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def safe_float_convert(value):
    """安全地将值转换为浮点数"""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

test_values = ["123", "3.14", "abc", "0", "", "True", "False"]
for value in test_values:
    int_result = safe_int_convert(value)
    float_result = safe_float_convert(value)
    print(f"'{value}' -> int: {int_result}, float: {float_result}")

# ==================== 5. 类型检查函数 ====================
print("\n5. 类型检查函数:")
print("-" * 40)

def check_type(value, expected_type):
    """检查值的类型是否符合预期"""
    actual_type = type(value)
    is_correct = isinstance(value, expected_type)
    print(f"值: {value}, 实际类型: {actual_type.__name__}, 预期类型: {expected_type.__name__}, 匹配: {is_correct}")

# 测试各种类型
check_type(42, int)
check_type(3.14, float)
check_type("hello", str)
check_type(True, bool)
check_type([1, 2, 3], list)
check_type((1, 2, 3), tuple)
check_type({1, 2, 3}, set)
check_type({"a": 1}, dict)

print("\n" + "=" * 60)
print("Python 数据类型演示完成！")
print("=" * 60) 