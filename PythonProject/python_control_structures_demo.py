# Python 控制结构完整演示文件
# 作者：AI助手
# 功能：展示Python的所有控制结构和使用方法

print("=" * 60)
print("Python 控制结构完整演示")
print("=" * 60)

# ==================== 1. 条件语句 (if-elif-else) ====================
print("\n1. 条件语句 (if-elif-else):")
print("-" * 40)

# 基本if语句
age = 18
print(f"年龄: {age}")
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# if-elif-else语句
score = 85
print(f"\n成绩: {score}")
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 嵌套if语句
username = "admin"
password = "123456"
print(f"\n用户名: {username}, 密码: {password}")
if username == "admin":
    if password == "123456":
        print("登录成功")
    else:
        print("密码错误")
else:
    print("用户名不存在")

# 条件表达式（三元运算符）
x = 10
y = 20
max_value = x if x > y else y
print(f"\nx = {x}, y = {y}")
print(f"最大值: {max_value}")

# ==================== 2. 循环语句 ====================
print("\n2. 循环语句:")
print("-" * 40)

# 2.1 for循环
print("\n2.1 for循环:")

# 循环10次的不同写法
print("方法1: range(10)")
for i in range(10):
    print(f"第{i+1}次循环", end=" ")
print()

print("\n方法2: range(1, 11)")
for i in range(1, 11):
    print(f"第{i}次循环", end=" ")
print()

print("\n方法3: while循环")
count = 1
while count <= 10:
    print(f"第{count}次循环", end=" ")
    count += 1
print()

print("\n方法4: 列表推导式")
numbers = [i for i in range(1, 11)]
print(f"生成的列表: {numbers}")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"\n遍历列表 {fruits}:")
for fruit in fruits:
    print(f"我喜欢吃 {fruit}")

# 遍历字典
person = {"name": "张三", "age": 25, "city": "北京"}
print(f"\n遍历字典 {person}:")
for key, value in person.items():
    print(f"{key}: {value}")

# 遍历字符串
text = "Python"
print(f"\n遍历字符串 '{text}':")
for char in text:
    print(f"字符: {char}")

# 2.2 while循环
print("\n2.2 while循环:")

# 基本while循环
counter = 0
while counter < 5:
    print(f"计数器: {counter}")
    counter += 1

# while循环配合用户输入
print("\nwhile循环示例（模拟）:")
password = "123456"
attempts = 0
max_attempts = 3

# 模拟登录过程
while attempts < max_attempts:
    attempts += 1
    print(f"第{attempts}次尝试登录")
    if attempts == 2:  # 模拟第2次成功
        print("登录成功！")
        break
    else:
        print("密码错误，请重试")

# 2.3 循环控制语句
print("\n2.3 循环控制语句:")

# break语句
print("break示例:")
for i in range(10):
    if i == 5:
        print(f"遇到5，跳出循环")
        break
    print(f"i = {i}")

# continue语句
print("\ncontinue示例:")
for i in range(10):
    if i % 2 == 0:  # 跳过偶数
        continue
    print(f"奇数: {i}")

# pass语句
print("\npass示例:")
for i in range(5):
    if i < 3:
        pass  # 暂时不做任何操作
    else:
        print(f"i >= 3: {i}")

# ==================== 3. range()函数详细用法 ====================
print("\n3. range()函数详细用法:")
print("-" * 40)

# 3.1 基本用法
print("3.1 基本用法:")
print(f"range(5): {list(range(5))}")
print(f"range(1, 6): {list(range(1, 6))}")
print(f"range(0, 10, 2): {list(range(0, 10, 2))}")

# 3.2 负步长
print("\n3.2 负步长:")
print(f"range(10, 0, -1): {list(range(10, 0, -1))}")
print(f"range(5, -1, -1): {list(range(5, -1, -1))}")

# 3.3 不同数据类型
print("\n3.3 不同数据类型:")
print(f"range(3): {type(range(3))}")
print(f"转换为列表: {list(range(3))}")
print(f"转换为元组: {tuple(range(3))}")
print(f"转换为集合: {set(range(3))}")

# 3.4 实际应用
print("\n3.4 实际应用:")

# 生成索引
print("生成索引:")
for i in range(len(fruits)):
    print(f"索引 {i}: {fruits[i]}")

# 生成乘法表
print("\n生成乘法表:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()

# 生成等差数列
print("\n生成等差数列:")
arithmetic_seq = list(range(0, 20, 3))
print(f"0到20，步长为3: {arithmetic_seq}")

# ==================== 4. 循环10次的不同写法详解 ====================
print("\n4. 循环10次的不同写法详解:")
print("-" * 40)

print("方法1: for i in range(10)")
for i in range(10):
    print(f"循环 {i+1}/10", end=" ")
print()

print("\n方法2: for i in range(1, 11)")
for i in range(1, 11):
    print(f"循环 {i}/10", end=" ")
print()

print("\n方法3: while循环")
i = 1
while i <= 10:
    print(f"循环 {i}/10", end=" ")
    i += 1
print()

print("\n方法4: 使用enumerate")
for i, _ in enumerate(range(10), 1):
    print(f"循环 {i}/10", end=" ")
print()

print("\n方法5: 列表推导式")
result = [f"循环{i+1}/10" for i in range(10)]
print(" ".join(result))

print("\n方法6: 使用itertools.count")
import itertools
for i in itertools.count(1):
    if i > 10:
        break
    print(f"循环 {i}/10", end=" ")
print()

# ==================== 5. 高级控制结构 ====================
print("\n5. 高级控制结构:")
print("-" * 40)

# 5.1 列表推导式
print("5.1 列表推导式:")
squares = [x**2 for x in range(5)]
print(f"平方数: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

# 5.2 字典推导式
print("\n5.2 字典推导式:")
square_dict = {x: x**2 for x in range(5)}
print(f"数字平方字典: {square_dict}")

# 5.3 集合推导式
print("\n5.3 集合推导式:")
even_set = {x for x in range(10) if x % 2 == 0}
print(f"偶数集合: {even_set}")

# 5.4 生成器表达式
print("\n5.4 生成器表达式:")
gen = (x**2 for x in range(5))
print(f"生成器: {gen}")
print(f"生成器值: {list(gen)}")

# ==================== 6. 异常处理 ====================
print("\n6. 异常处理:")
print("-" * 40)

# 6.1 try-except
print("6.1 try-except:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("捕获到除零错误")

# 6.2 try-except-else
print("\n6.2 try-except-else:")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("捕获到除零错误")
else:
    print(f"计算成功: {result}")

# 6.3 try-except-finally
print("\n6.3 try-except-finally:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("捕获到除零错误")
finally:
    print("finally块总是执行")

# 6.4 多个except
print("\n6.4 多个except:")
try:
    value = int("abc")
except ValueError:
    print("值错误")
except TypeError:
    print("类型错误")
except Exception as e:
    print(f"其他错误: {e}")

# ==================== 7. 实际应用示例 ====================
print("\n7. 实际应用示例:")
print("-" * 40)

# 7.1 菜单系统
print("7.1 菜单系统:")
def show_menu():
    print("1. 查看信息")
    print("2. 修改信息")
    print("3. 删除信息")
    print("4. 退出")

# 模拟菜单选择
choice = 2
print(f"用户选择: {choice}")

if choice == 1:
    print("执行查看信息")
elif choice == 2:
    print("执行修改信息")
elif choice == 3:
    print("执行删除信息")
elif choice == 4:
    print("退出程序")
else:
    print("无效选择")

# 7.2 数据处理
print("\n7.2 数据处理:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 统计奇偶数
odd_count = 0
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"奇数个数: {odd_count}")
print(f"偶数个数: {even_count}")

# 7.3 密码验证
print("\n7.3 密码验证:")
def validate_password(password):
    if len(password) < 8:
        return False, "密码长度不足8位"
    elif not any(c.isupper() for c in password):
        return False, "密码需要包含大写字母"
    elif not any(c.islower() for c in password):
        return False, "密码需要包含小写字母"
    elif not any(c.isdigit() for c in password):
        return False, "密码需要包含数字"
    else:
        return True, "密码符合要求"

test_password = "Abc12345"
is_valid, message = validate_password(test_password)
print(f"密码: {test_password}")
print(f"验证结果: {message}")

# ==================== 8. 性能优化示例 ====================
print("\n8. 性能优化示例:")
print("-" * 40)

# 8.1 使用enumerate
print("8.1 使用enumerate:")
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 8.2 使用zip
print("\n8.2 使用zip:")
names = ["张三", "李四", "王五"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} 的年龄是 {age}")

# 8.3 使用any和all
print("\n8.3 使用any和all:")
numbers = [2, 4, 6, 8, 10]
all_even = all(num % 2 == 0 for num in numbers)
any_odd = any(num % 2 == 1 for num in numbers)
print(f"所有数字都是偶数: {all_even}")
print(f"存在奇数: {any_odd}")

print("\n" + "=" * 60)
print("Python 控制结构演示完成！")
print("=" * 60) 