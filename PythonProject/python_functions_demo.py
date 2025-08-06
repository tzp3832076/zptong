# Python 函数完整演示文件
# 作者：AI助手
# 功能：展示Python函数的使用方法、参数类型、匿名函数、闭包和变量作用域

print("=" * 60)
print("Python 函数完整演示")
print("=" * 60)

# ==================== 1. 基本函数定义和使用 ====================
print("\n1. 基本函数定义和使用:")
print("-" * 40)

# 1.1 简单函数
def greet():
    """简单的问候函数"""
    print("Hello, World!")

print("调用简单函数:")
greet()

# 1.2 带参数的函数
def greet_person(name):
    """带参数的问候函数"""
    print(f"Hello, {name}!")

print("\n调用带参数的函数:")
greet_person("张三")

# 1.3 带返回值的函数
def add(a, b):
    """加法函数，返回两数之和"""
    return a + b

result = add(5, 3)
print(f"\n加法函数: 5 + 3 = {result}")

# 1.4 多返回值函数
def get_name_age():
    """返回姓名和年龄"""
    return "李四", 25

name, age = get_name_age()
print(f"\n多返回值: 姓名={name}, 年龄={age}")

# ==================== 2. 函数参数的各种写法 ====================
print("\n2. 函数参数的各种写法:")
print("-" * 40)

# 2.1 位置参数
def describe_person(name, age, city):
    """位置参数示例"""
    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

print("2.1 位置参数:")
describe_person("王五", 30, "上海")

# 2.2 关键字参数
print("\n2.2 关键字参数:")
describe_person(name="赵六", age=28, city="广州")
describe_person(city="深圳", name="钱七", age=32)

# 2.3 默认参数
def greet_with_default(name="World", greeting="Hello"):
    """带默认参数的函数"""
    print(f"{greeting}, {name}!")

print("\n2.3 默认参数:")
greet_with_default()  # 使用默认值
greet_with_default("Python")  # 只传第一个参数
greet_with_default("Python", "Hi")  # 传两个参数
greet_with_default(greeting="Good morning", name="Python")  # 关键字参数

# 2.4 可变位置参数 (*args)
def sum_numbers(*args):
    """可变位置参数，计算所有数字的和"""
    total = 0
    for num in args:
        total += num
    return total

print("\n2.4 可变位置参数 (*args):")
print(f"sum_numbers(1, 2, 3) = {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")

# 2.5 可变关键字参数 (**kwargs)
def print_info(**kwargs):
    """可变关键字参数，打印所有传入的信息"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n2.5 可变关键字参数 (**kwargs):")
print_info(name="张三", age=25, city="北京", job="工程师")

# 2.6 混合参数类型
def complex_function(name, age=25, *args, city="北京", **kwargs):
    """混合使用各种参数类型"""
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"城市: {city}")
    if args:
        print(f"其他位置参数: {args}")
    if kwargs:
        print(f"其他关键字参数: {kwargs}")

print("\n2.6 混合参数类型:")
complex_function("李四", 30, "爱好1", "爱好2", city="上海", job="设计师", hobby="编程")

# ==================== 3. 函数的高级特性 ====================
print("\n3. 函数的高级特性:")
print("-" * 40)

# 3.1 函数作为参数
def apply_operation(func, x, y):
    """接受函数作为参数"""
    return func(x, y)

def add_func(a, b):
    return a + b

def multiply_func(a, b):
    return a * b

print("3.1 函数作为参数:")
print(f"apply_operation(add_func, 5, 3) = {apply_operation(add_func, 5, 3)}")
print(f"apply_operation(multiply_func, 5, 3) = {apply_operation(multiply_func, 5, 3)}")

# 3.2 函数返回函数
def create_multiplier(factor):
    """返回一个函数"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print("\n3.2 函数返回函数:")
print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# 3.3 装饰器模式
def timer(func):
    """简单的计时装饰器"""
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    """一个模拟的慢函数"""
    import time
    time.sleep(0.1)
    return "完成"

print("\n3.3 装饰器模式:")
slow_function()

# ==================== 4. 匿名函数 (Lambda) ====================
print("\n4. 匿名函数 (Lambda):")
print("-" * 40)

# 4.1 基本lambda函数
square = lambda x: x ** 2
add_lambda = lambda x, y: x + y

print("4.1 基本lambda函数:")
print(f"square(5) = {square(5)}")
print(f"add_lambda(3, 4) = {add_lambda(3, 4)}")

# 4.2 lambda函数与内置函数结合
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\n4.2 使用filter过滤偶数: {even_numbers}")

# 使用map
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"使用map计算平方: {squared_numbers}")

# 使用sorted
names = ["张三", "李四", "王五", "赵六"]
sorted_names = sorted(names, key=lambda x: len(x))
print(f"使用sorted按长度排序: {sorted_names}")

# 4.3 lambda函数在reduce中的应用
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"使用reduce计算乘积: {product}")

# ==================== 5. 闭包 (Closure) ====================
print("\n5. 闭包 (Closure):")
print("-" * 40)

# 5.1 基本闭包
def outer_function(x):
    """外部函数"""
    def inner_function(y):
        """内部函数，可以访问外部函数的变量"""
        return x + y
    return inner_function

# 创建闭包
add_5 = outer_function(5)
add_10 = outer_function(10)

print("5.1 基本闭包:")
print(f"add_5(3) = {add_5(3)}")
print(f"add_10(3) = {add_10(3)}")

# 5.2 闭包与状态保持
def counter():
    """计数器闭包"""
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = counter()
counter2 = counter()

print("\n5.2 闭包与状态保持:")
print(f"counter1(): {counter1()}")
print(f"counter1(): {counter1()}")
print(f"counter1(): {counter1()}")
print(f"counter2(): {counter2()}")
print(f"counter2(): {counter2()}")

# 5.3 闭包的实际应用 - 配置函数
def create_config(config_dict):
    """创建配置闭包"""
    def get_config(key, default=None):
        return config_dict.get(key, default)
    return get_config

app_config = create_config({
    "host": "localhost",
    "port": 8080,
    "debug": True
})

print("\n5.3 闭包的实际应用:")
print(f"app_config('host') = {app_config('host')}")
print(f"app_config('port') = {app_config('port')}")
print(f"app_config('unknown', 'default') = {app_config('unknown', 'default')}")

# ==================== 6. 局部变量和全局变量 ====================
print("\n6. 局部变量和全局变量:")
print("-" * 40)

# 6.1 全局变量
global_var = "我是全局变量"

def demonstrate_scope():
    """演示变量作用域"""
    local_var = "我是局部变量"
    print(f"在函数内部访问局部变量: {local_var}")
    print(f"在函数内部访问全局变量: {global_var}")

print("6.1 基本作用域:")
demonstrate_scope()
print(f"在函数外部访问全局变量: {global_var}")

# 6.2 修改全局变量
counter_global = 0

def increment_global():
    """修改全局变量"""
    global counter_global
    counter_global += 1
    print(f"全局计数器: {counter_global}")

print("\n6.2 修改全局变量:")
increment_global()
increment_global()
increment_global()

# 6.3 nonlocal关键字
def outer_nonlocal():
    """演示nonlocal关键字"""
    x = 1
    def inner():
        nonlocal x
        x = 2
        print(f"内部函数中的x: {x}")
    inner()
    print(f"外部函数中的x: {x}")

print("\n6.3 nonlocal关键字:")
outer_nonlocal()

# 6.4 变量遮蔽
shadow_var = "全局变量"

def shadow_demo():
    """演示变量遮蔽"""
    shadow_var = "局部变量"
    print(f"函数内部的shadow_var: {shadow_var}")

print("\n6.4 变量遮蔽:")
shadow_demo()
print(f"函数外部的shadow_var: {shadow_var}")

# ==================== 7. 函数的高级应用 ====================
print("\n7. 函数的高级应用:")
print("-" * 40)

# 7.1 递归函数
def factorial(n):
    """计算阶乘的递归函数"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print("7.1 递归函数:")
print(f"factorial(5) = {factorial(5)}")

# 7.2 生成器函数
def fibonacci(n):
    """生成斐波那契数列的生成器函数"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\n7.2 生成器函数:")
fib_gen = fibonacci(10)
print(f"斐波那契数列: {list(fib_gen)}")

# 7.3 函数式编程
def compose(*functions):
    """函数组合"""
    def inner(arg):
        for f in reversed(functions):
            arg = f(arg)
        return arg
    return inner

def add_one(x): return x + 1
def multiply_by_two(x): return x * 2
def square(x): return x ** 2

composed = compose(square, multiply_by_two, add_one)
print(f"\n7.3 函数组合: composed(3) = {composed(3)}")

# 7.4 偏函数 (Partial Functions)
from functools import partial

def power(base, exponent):
    """计算幂"""
    return base ** exponent

square_partial = partial(power, exponent=2)
cube_partial = partial(power, exponent=3)

print("\n7.4 偏函数:")
print(f"square_partial(5) = {square_partial(5)}")
print(f"cube_partial(3) = {cube_partial(3)}")

# ==================== 8. 实际应用示例 ====================
print("\n8. 实际应用示例:")
print("-" * 40)

# 8.1 数据验证函数
def validate_email(email):
    """验证邮箱格式"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print("8.1 数据验证函数:")
test_emails = ["test@example.com", "invalid-email", "user@domain.org"]
for email in test_emails:
    is_valid = validate_email(email)
    print(f"'{email}' -> {'有效' if is_valid else '无效'}")

# 8.2 缓存装饰器
def cache(func):
    """简单的缓存装饰器"""
    cache_dict = {}
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper

@cache
def expensive_calculation(n):
    """模拟昂贵的计算"""
    import time
    time.sleep(0.1)  # 模拟计算时间
    return n * n

print("\n8.2 缓存装饰器:")
print(f"第一次计算: {expensive_calculation(5)}")
print(f"第二次计算（使用缓存）: {expensive_calculation(5)}")

# 8.3 函数工厂
def create_math_operation(operation):
    """创建数学运算函数"""
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "subtract":
        return lambda x, y: x - y
    elif operation == "multiply":
        return lambda x, y: x * y
    elif operation == "divide":
        return lambda x, y: x / y if y != 0 else "错误：除零"
    else:
        return lambda x, y: "未知操作"

print("\n8.3 函数工厂:")
add_op = create_math_operation("add")
multiply_op = create_math_operation("multiply")
divide_op = create_math_operation("divide")

print(f"add_op(10, 5) = {add_op(10, 5)}")
print(f"multiply_op(10, 5) = {multiply_op(10, 5)}")
print(f"divide_op(10, 5) = {divide_op(10, 5)}")
print(f"divide_op(10, 0) = {divide_op(10, 0)}")

print("\n" + "=" * 60)
print("Python 函数演示完成！")
print("=" * 60) 