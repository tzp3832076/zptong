# Python 运算符完整演示文件
# 作者：AI助手
# 功能：展示Python的所有运算符类型和使用方法

print("=" * 60)
print("Python 运算符完整演示")
print("=" * 60)

# ==================== 1. 算术运算符 ====================
print("\n1. 算术运算符:")
print("-" * 40)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法: a + b = {a + b}")
print(f"减法: a - b = {a - b}")
print(f"乘法: a * b = {a * b}")
print(f"除法: a / b = {a / b}")
print(f"整除: a // b = {a // b}")
print(f"取余: a % b = {a % b}")
print(f"幂运算: a ** b = {a ** b}")

# 负数示例
c = -5
d = 2
print(f"\nc = {c}, d = {d}")
print(f"负数除法: c / d = {c / d}")
print(f"负数整除: c // d = {c // d}")
print(f"负数取余: c % d = {c % d}")

# 浮点数运算
e = 7.5
f = 2.3
print(f"\ne = {e}, f = {f}")
print(f"浮点数加法: e + f = {e + f}")
print(f"浮点数乘法: e * f = {e * f}")
print(f"浮点数除法: e / f = {e / f}")

# ==================== 2. 比较运算符 ====================
print("\n2. 比较运算符:")
print("-" * 40)

x = 15
y = 20
z = 15

print(f"x = {x}, y = {y}, z = {z}")
print(f"等于: x == z = {x == z}")
print(f"不等于: x != y = {x != y}")
print(f"大于: y > x = {y > x}")
print(f"小于: x < y = {x < y}")
print(f"大于等于: x >= z = {x >= z}")
print(f"小于等于: x <= y = {x <= y}")

# 字符串比较
str1 = "apple"
str2 = "banana"
str3 = "apple"
print(f"\nstr1 = '{str1}', str2 = '{str2}', str3 = '{str3}'")
print(f"字符串等于: str1 == str3 = {str1 == str3}")
print(f"字符串不等于: str1 != str2 = {str1 != str2}")
print(f"字符串小于: str1 < str2 = {str1 < str2}")  # 按字母顺序

# ==================== 3. 逻辑运算符 ====================
print("\n3. 逻辑运算符:")
print("-" * 40)

p = True
q = False
r = True

print(f"p = {p}, q = {q}, r = {r}")
print(f"逻辑与: p and r = {p and r}")
print(f"逻辑与: p and q = {p and q}")
print(f"逻辑或: p or q = {p or q}")
print(f"逻辑或: q or p = {q or p}")
print(f"逻辑非: not p = {not p}")
print(f"逻辑非: not q = {not q}")

# 复杂逻辑表达式
print(f"\n复杂逻辑表达式:")
print(f"(p and r) or q = {(p and r) or q}")
print(f"not (p and q) = {not (p and q)}")
print(f"p and (q or r) = {p and (q or r)}")

# 短路求值示例
print(f"\n短路求值示例:")
result1 = False and print("这不会执行")
result2 = True or print("这也不会执行")
print(f"False and print() 的结果: {result1}")
print(f"True or print() 的结果: {result2}")

# ==================== 4. 位运算符 ====================
print("\n4. 位运算符:")
print("-" * 40)

m = 60  # 二进制: 00111100
n = 13  # 二进制: 00001101

print(f"m = {m} (二进制: {bin(m)})")
print(f"n = {n} (二进制: {bin(n)})")
print(f"按位与: m & n = {m & n} (二进制: {bin(m & n)})")
print(f"按位或: m | n = {m | n} (二进制: {bin(m | n)})")
print(f"按位异或: m ^ n = {m ^ n} (二进制: {bin(m ^ n)})")
print(f"按位取反: ~m = {~m} (二进制: {bin(~m)})")
print(f"左移: m << 2 = {m << 2} (二进制: {bin(m << 2)})")
print(f"右移: m >> 2 = {m >> 2} (二进制: {bin(m >> 2)})")

# ==================== 5. 赋值运算符 ====================
print("\n5. 赋值运算符:")
print("-" * 40)

# 基本赋值
value = 10
print(f"基本赋值: value = {value}")

# 复合赋值
value += 5
print(f"加法赋值: value += 5, 结果: {value}")

value -= 3
print(f"减法赋值: value -= 3, 结果: {value}")

value *= 2
print(f"乘法赋值: value *= 2, 结果: {value}")

value /= 4
print(f"除法赋值: value /= 4, 结果: {value}")

value //= 2
print(f"整除赋值: value //= 2, 结果: {value}")

value %= 3
print(f"取余赋值: value %= 3, 结果: {value}")

value **= 2
print(f"幂赋值: value **= 2, 结果: {value}")

# 位运算赋值
bit_value = 15
print(f"\nbit_value = {bit_value}")
bit_value &= 7
print(f"按位与赋值: bit_value &= 7, 结果: {bit_value}")

bit_value |= 8
print(f"按位或赋值: bit_value |= 8, 结果: {bit_value}")

bit_value ^= 3
print(f"按位异或赋值: bit_value ^= 3, 结果: {bit_value}")

bit_value <<= 1
print(f"左移赋值: bit_value <<= 1, 结果: {bit_value}")

bit_value >>= 2
print(f"右移赋值: bit_value >>= 2, 结果: {bit_value}")

# ==================== 6. 成员运算符 ====================
print("\n6. 成员运算符:")
print("-" * 40)

# in 和 not in
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
search_fruit = "香蕉"
not_fruit = "西瓜"

print(f"fruits = {fruits}")
print(f"search_fruit = '{search_fruit}'")
print(f"not_fruit = '{not_fruit}'")

print(f"'{search_fruit}' in fruits = {search_fruit in fruits}")
print(f"'{not_fruit}' in fruits = {not_fruit in fruits}")
print(f"'{search_fruit}' not in fruits = {search_fruit not in fruits}")
print(f"'{not_fruit}' not in fruits = {not_fruit not in fruits}")

# 字符串成员检查
text = "Hello, Python!"
print(f"\ntext = '{text}'")
print(f"'Python' in text = {'Python' in text}")
print(f"'Java' in text = {'Java' in text}")
print(f"'o' in text = {'o' in text}")

# 字典成员检查
person = {"name": "张三", "age": 25, "city": "北京"}
print(f"\nperson = {person}")
print(f"'name' in person = {'name' in person}")
print(f"'salary' in person = {'salary' in person}")
print(f"'张三' in person.values() = {'张三' in person.values()}")

# ==================== 7. 身份运算符 ====================
print("\n7. 身份运算符:")
print("-" * 40)

# is 和 is not
obj1 = [1, 2, 3]
obj2 = [1, 2, 3]
obj3 = obj1

print(f"obj1 = {obj1}")
print(f"obj2 = {obj2}")
print(f"obj3 = {obj3}")

print(f"obj1 is obj3 = {obj1 is obj3}")  # True，同一个对象
print(f"obj1 is obj2 = {obj1 is obj2}")  # False，不同对象
print(f"obj1 is not obj2 = {obj1 is not obj2}")  # True

# 小整数缓存
num1 = 256
num2 = 256
num3 = 257
num4 = 257

print(f"\nnum1 = {num1}, num2 = {num2}")
print(f"num3 = {num3}, num4 = {num4}")
print(f"num1 is num2 = {num1 is num2}")  # True（Python缓存小整数）
print(f"num3 is num4 = {num3 is num4}")  # False（大整数不缓存）

# None 比较
empty_value = None
print(f"\nempty_value = {empty_value}")
print(f"empty_value is None = {empty_value is None}")
print(f"empty_value is not None = {empty_value is not None}")

# ==================== 8. 运算符优先级演示 ====================
print("\n8. 运算符优先级演示:")
print("-" * 40)

# 算术运算符优先级
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {result1}")  # 先乘后加
print(f"(2 + 3) * 4 = {result2}")  # 括号优先

# 逻辑运算符优先级
bool1 = True
bool2 = False
bool3 = True

result3 = bool1 and bool2 or bool3
result4 = bool1 and (bool2 or bool3)
print(f"True and False or True = {result3}")  # 先and后or
print(f"True and (False or True) = {result4}")  # 括号优先

# 位运算符优先级
bit1 = 5
bit2 = 3
bit3 = 2

result5 = bit1 & bit2 | bit3
result6 = (bit1 & bit2) | bit3
print(f"5 & 3 | 2 = {result5}")
print(f"(5 & 3) | 2 = {result6}")

# ==================== 9. 实际应用示例 ====================
print("\n9. 实际应用示例:")
print("-" * 40)

# 条件判断
age = 18
has_id = True
is_vip = False

can_enter = age >= 18 and has_id
can_discount = age >= 18 and (has_id or is_vip)

print(f"年龄: {age}, 有身份证: {has_id}, 是VIP: {is_vip}")
print(f"可以进入: {can_enter}")
print(f"可以享受折扣: {can_discount}")

# 数值计算
price = 100
discount = 0.2
tax_rate = 0.1

final_price = price * (1 - discount) * (1 + tax_rate)
print(f"\n原价: {price}")
print(f"折扣: {discount * 100}%")
print(f"税率: {tax_rate * 100}%")
print(f"最终价格: {final_price}")

# 位运算应用
permissions = 0b111  # 读、写、执行权限
read_permission = 0b100
write_permission = 0b010
execute_permission = 0b001

has_read = (permissions & read_permission) != 0
has_write = (permissions & write_permission) != 0
has_execute = (permissions & execute_permission) != 0

print(f"\n权限值: {bin(permissions)}")
print(f"有读权限: {has_read}")
print(f"有写权限: {has_write}")
print(f"有执行权限: {has_execute}")

# ==================== 10. 运算符函数形式 ====================
print("\n10. 运算符函数形式:")
print("-" * 40)

import operator

x, y = 10, 3
print(f"x = {x}, y = {y}")

# 算术运算符函数
print(f"operator.add(x, y) = {operator.add(x, y)}")
print(f"operator.sub(x, y) = {operator.sub(x, y)}")
print(f"operator.mul(x, y) = {operator.mul(x, y)}")
print(f"operator.truediv(x, y) = {operator.truediv(x, y)}")
print(f"operator.floordiv(x, y) = {operator.floordiv(x, y)}")
print(f"operator.mod(x, y) = {operator.mod(x, y)}")
print(f"operator.pow(x, y) = {operator.pow(x, y)}")

# 比较运算符函数
print(f"operator.eq(x, y) = {operator.eq(x, y)}")
print(f"operator.ne(x, y) = {operator.ne(x, y)}")
print(f"operator.gt(x, y) = {operator.gt(x, y)}")
print(f"operator.lt(x, y) = {operator.lt(x, y)}")
print(f"operator.ge(x, y) = {operator.ge(x, y)}")
print(f"operator.le(x, y) = {operator.le(x, y)}")

# 逻辑运算符函数
print(f"operator.and_(True, False) = {operator.and_(True, False)}")
print(f"operator.or_(True, False) = {operator.or_(True, False)}")
print(f"operator.not_(True) = {operator.not_(True)}")

# 位运算符函数
print(f"operator.and_(x, y) = {operator.and_(x, y)}")
print(f"operator.or_(x, y) = {operator.or_(x, y)}")
print(f"operator.xor(x, y) = {operator.xor(x, y)}")
print(f"operator.invert(x) = {operator.invert(x)}")

print("\n" + "=" * 60)
print("Python 运算符演示完成！")
print("=" * 60) 