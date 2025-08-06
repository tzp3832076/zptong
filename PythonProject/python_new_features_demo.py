#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python新特性完整演示文件
作者：AI助手
功能：展示Python 3.8+ 到 3.12+ 的主要新特性
"""

import sys
import time
import statistics
from typing import TypeAlias, TypeGuard
from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum

print("=" * 60)
print("Python新特性完整演示")
print(f"当前Python版本: {sys.version}")
print("=" * 60)

# ==================== 1. 海象运算符 (Python 3.8+) ====================
print("\n1. 海象运算符 (Walrus Operator) - Python 3.8+")
print("-" * 50)

def demo_walrus_operator():
    """演示海象运算符的使用"""
    
    # 1.1 在条件语句中使用
    print("1.1 在条件语句中使用:")
    if name := input("请输入您的姓名 (海象运算符演示): "):
        print(f"你好, {name}!")
    
    # 1.2 在循环中使用
    print("\n1.2 在循环中使用:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while (n := len(numbers)) > 0:
        print(f"剩余数字数量: {n}")
        numbers.pop()
    
    # 1.3 在列表推导式中使用
    print("\n1.3 在列表推导式中使用:")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_squares = [square for num in data if (square := num ** 2) > 25]
    print(f"平方大于25的数字: {filtered_squares}")
    
    # 1.4 在正则表达式中使用
    print("\n1.4 在正则表达式中使用:")
    import re
    text = "Python 3.8, Python 3.9, Python 3.10, Python 3.11"
    if match := re.search(r'Python (\d+\.\d+)', text):
        version = match.group(1)
        print(f"找到Python版本: {version}")

# ==================== 2. 位置参数语法 (Python 3.8+) ====================
print("\n2. 位置参数语法 - Python 3.8+")
print("-" * 50)

def demo_positional_arguments():
    """演示位置参数语法"""
    
    def greet(name, /, greeting="Hello", *, title=""):
        """位置参数、关键字参数和仅关键字参数的混合"""
        return f"{greeting}, {title} {name}!"
    
    print("2.1 位置参数:")
    print(greet("张三"))
    
    print("\n2.2 关键字参数:")
    print(greet("李四", greeting="Hi"))
    
    print("\n2.3 仅关键字参数:")
    print(greet("王五", title="Mr."))
    
    print("\n2.4 混合使用:")
    print(greet("赵六", "Good morning", title="Dr."))

# ==================== 3. f-string 增强 (Python 3.8+) ====================
print("\n3. f-string 增强 - Python 3.8+")
print("-" * 50)

def demo_fstring_enhancements():
    """演示f-string的新特性"""
    
    # 3.1 调试表达式
    print("3.1 调试表达式:")
    name = "张三"
    age = 25
    city = "北京"
    print(f"{name=}, {age=}, {city=}")
    
    # 3.2 格式化数字
    print("\n3.2 格式化数字:")
    pi = 3.14159265359
    print(f"π值: {pi:.4f}")
    print(f"π值(右对齐): {pi:>10.4f}")
    print(f"π值(左对齐): {pi:<10.4f}")
    print(f"π值(居中对齐): {pi:^10.4f}")
    
    # 3.3 条件表达式
    print("\n3.3 条件表达式:")
    status = "active"
    print(f"状态: {'✅' if status == 'active' else '❌'}")
    
    # 3.4 嵌套表达式
    print("\n3.4 嵌套表达式:")
    user = {"name": "李四", "age": 30, "city": "上海"}
    print(f"用户信息: {user['name']} ({user['age']}岁) 来自 {user['city']}")
    
    # 3.5 格式化日期
    print("\n3.5 格式化日期:")
    from datetime import datetime
    now = datetime.now()
    print(f"当前时间: {now:%Y年%m月%d日 %H:%M:%S}")

# ==================== 4. 字典合并运算符 (Python 3.9+) ====================
print("\n4. 字典合并运算符 - Python 3.9+")
print("-" * 50)

def demo_dict_merge():
    """演示字典合并运算符"""
    
    # 4.1 基本合并
    print("4.1 基本合并:")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = dict1 | dict2
    print(f"合并结果: {merged}")
    
    # 4.2 原地更新
    print("\n4.2 原地更新:")
    config = {"host": "localhost", "port": 8080}
    config |= {"debug": True, "timeout": 30}
    print(f"更新后的配置: {config}")
    
    # 4.3 复杂合并
    print("\n4.3 复杂合并:")
    user_info = {"name": "张三", "age": 25}
    contact_info = {"email": "zhangsan@example.com", "phone": "13800138000"}
    preferences = {"theme": "dark", "language": "zh-CN"}
    
    complete_profile = user_info | contact_info | preferences
    print(f"完整用户资料: {complete_profile}")
    
    # 4.4 处理重复键
    print("\n4.4 处理重复键:")
    base_config = {"host": "localhost", "port": 8080, "debug": False}
    override_config = {"port": 9000, "debug": True, "timeout": 60}
    final_config = base_config | override_config
    print(f"最终配置: {final_config}")

# ==================== 5. 类型注解增强 (Python 3.9+) ====================
print("\n5. 类型注解增强 - Python 3.9+")
print("-" * 50)

def demo_type_annotations():
    """演示类型注解的新特性"""
    
    # 5.1 内置类型注解
    def process_data(data: dict[str, int | str]) -> list[str]:
        """处理数据并返回字符串列表"""
        return [str(value) for value in data.values()]
    
    # 5.2 泛型类型
    def find_max(items: Sequence[int]) -> int:
        """找到序列中的最大值"""
        return max(items)
    
    # 5.3 类型别名
    UserId: TypeAlias = int
    UserName: TypeAlias = str
    UserInfo: TypeAlias = dict[UserName, UserId]
    
    def get_user_info() -> UserInfo:
        """获取用户信息"""
        return {"张三": 1, "李四": 2, "王五": 3}
    
    # 5.4 类型守卫
    def is_string_list(val: list[object]) -> TypeGuard[list[str]]:
        """检查是否为字符串列表"""
        return all(isinstance(x, str) for x in val)
    
    def process_strings(data: list[object]) -> None:
        """处理字符串列表"""
        if is_string_list(data):
            # 这里类型检查器知道data是list[str]
            for item in data:
                print(f"处理字符串: {item.upper()}")
    
    # 测试类型注解
    print("5.1 测试类型注解:")
    test_data = {"a": 1, "b": "hello", "c": 42}
    result = process_data(test_data)
    print(f"处理结果: {result}")
    
    print("\n5.2 测试泛型类型:")
    numbers = [1, 5, 3, 9, 2]
    max_num = find_max(numbers)
    print(f"最大值: {max_num}")
    
    print("\n5.3 测试类型别名:")
    user_info = get_user_info()
    print(f"用户信息: {user_info}")
    
    print("\n5.4 测试类型守卫:")
    string_list = ["hello", "world", "python"]
    process_strings(string_list)

# ==================== 6. 字符串方法增强 (Python 3.9+) ====================
print("\n6. 字符串方法增强 - Python 3.9+")
print("-" * 50)

def demo_string_enhancements():
    """演示字符串方法的新特性"""
    
    # 6.1 移除前缀和后缀
    print("6.1 移除前缀和后缀:")
    text = "Hello, World!"
    print(f"原文本: {text}")
    print(f"移除前缀'Hello, ': {text.removeprefix('Hello, ')}")
    print(f"移除后缀'!': {text.removesuffix('!')}")
    
    # 6.2 字符串分割增强
    print("\n6.2 字符串分割增强:")
    csv_line = "a,b,c,d,e,f"
    print(f"CSV行: {csv_line}")
    parts = csv_line.split(",", maxsplit=3)
    print(f"分割结果 (最多3个): {parts}")
    
    # 6.3 字符串替换增强
    print("\n6.3 字符串替换增强:")
    text = "Python is great, Python is powerful, Python is simple"
    print(f"原文本: {text}")
    replaced = text.replace("Python", "Python 3", 2)  # 只替换前2个
    print(f"替换结果: {replaced}")

# ==================== 7. 模式匹配 (Python 3.10+) ====================
print("\n7. 模式匹配 (Match-Case) - Python 3.10+")
print("-" * 50)

def demo_pattern_matching():
    """演示模式匹配功能"""
    
    def analyze_data(data):
        """分析不同类型的数据"""
        match data:
            case {"type": "user", "name": str(name), "age": int(age)}:
                return f"用户: {name}, 年龄: {age}"
            case {"type": "product", "name": str(name), "price": float(price)}:
                return f"产品: {name}, 价格: ¥{price:.2f}"
            case {"type": "order", "id": str(order_id), "items": list(items)}:
                return f"订单: {order_id}, 商品数量: {len(items)}"
            case [x, y, z]:
                return f"三元组: {x}, {y}, {z}"
            case str(text):
                return f"字符串: {text}"
            case int(num):
                return f"整数: {num}"
            case _:
                return "未知数据类型"
    
    # 测试模式匹配
    test_cases = [
        {"type": "user", "name": "张三", "age": 25},
        {"type": "product", "name": "笔记本电脑", "price": 5999.99},
        {"type": "order", "id": "ORD-001", "items": ["鼠标", "键盘", "显示器"]},
        [1, 2, 3],
        "Hello, World!",
        42,
        {"unknown": "data"}
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        result = analyze_data(test_case)
        print(f"测试 {i}: {result}")

# ==================== 8. 联合类型简化 (Python 3.10+) ====================
print("\n8. 联合类型简化 - Python 3.10+")
print("-" * 50)

def demo_union_types():
    """演示联合类型的简化语法"""
    
    # 8.1 基本联合类型
    def process_value(value: int | str | None) -> str:
        """处理不同类型的值"""
        match value:
            case int():
                return f"整数: {value}"
            case str():
                return f"字符串: {value}"
            case None:
                return "空值"
            case _:
                return "未知类型"
    
    # 8.2 复杂联合类型
    def get_user_info(user_id: int | str) -> dict[str, str | int]:
        """获取用户信息"""
        if isinstance(user_id, int):
            return {"id": user_id, "name": f"用户{user_id}", "type": "数字ID"}
        else:
            return {"id": user_id, "name": f"用户{user_id}", "type": "字符串ID"}
    
    # 测试联合类型
    print("8.1 测试基本联合类型:")
    test_values = [42, "hello", None, 3.14]
    for value in test_values:
        result = process_value(value)
        print(f"输入: {value} -> {result}")
    
    print("\n8.2 测试复杂联合类型:")
    user_ids = [123, "user_456", 789, "admin"]
    for user_id in user_ids:
        info = get_user_info(user_id)
        print(f"用户ID: {user_id} -> {info}")

# ==================== 9. 异常组和异常处理增强 (Python 3.11+) ====================
print("\n9. 异常组和异常处理增强 - Python 3.11+")
print("-" * 50)

def demo_exception_groups():
    """演示异常组功能"""
    
    def process_multiple_files():
        """处理多个文件，演示异常组"""
        errors = []
        
        # 模拟处理多个文件
        files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
        
        for file in files:
            try:
                # 模拟文件操作
                if file == "file2.txt":
                    raise FileNotFoundError(f"文件 {file} 不存在")
                elif file == "file3.txt":
                    raise PermissionError(f"没有权限访问 {file}")
                else:
                    print(f"成功处理文件: {file}")
            except (FileNotFoundError, PermissionError) as e:
                errors.append(e)
        
        if errors:
            print(f"处理过程中遇到 {len(errors)} 个错误:")
            for error in errors:
                print(f"  - {error}")
    
    # 执行演示
    process_multiple_files()

# ==================== 10. 性能提升演示 (Python 3.11+) ====================
print("\n10. 性能提升演示 - Python 3.11+")
print("-" * 50)

def demo_performance():
    """演示性能提升"""
    
    # 10.1 函数调用性能测试
    def simple_function(x):
        return x * 2
    
    def benchmark_function_calls():
        """测试函数调用性能"""
        iterations = 1000000
        
        start_time = time.perf_counter()
        for i in range(iterations):
            result = simple_function(i)
        end_time = time.perf_counter()
        
        total_time = end_time - start_time
        calls_per_second = iterations / total_time
        
        print(f"函数调用性能测试:")
        print(f"  总调用次数: {iterations:,}")
        print(f"  总时间: {total_time:.4f}秒")
        print(f"  每秒调用次数: {calls_per_second:,.0f}")
    
    # 10.2 内存使用测试
    def benchmark_memory_usage():
        """测试内存使用"""
        import sys
        
        # 创建大量对象
        objects = []
        for i in range(100000):
            objects.append(f"object_{i}")
        
        memory_usage = sys.getsizeof(objects)
        print(f"\n内存使用测试:")
        print(f"  对象数量: {len(objects):,}")
        print(f"  内存使用: {memory_usage:,} 字节")
        print(f"  平均每个对象: {memory_usage / len(objects):.2f} 字节")
    
    # 执行性能测试
    benchmark_function_calls()
    benchmark_memory_usage()

# ==================== 11. 数据类增强 (Python 3.10+) ====================
print("\n11. 数据类增强 - Python 3.10+")
print("-" * 50)

def demo_dataclass_enhancements():
    """演示数据类的新特性"""
    
    @dataclass
    class User:
        """用户数据类"""
        name: str
        age: int
        email: str = ""
        is_active: bool = True
        
        def __post_init__(self):
            """初始化后处理"""
            if not self.email:
                self.email = f"{self.name.lower()}@example.com"
    
    @dataclass
    class Product:
        """产品数据类"""
        name: str
        price: float
        category: str = "未分类"
        stock: int = 0
        
        def total_value(self) -> float:
            """计算总价值"""
            return self.price * self.stock
    
    # 测试数据类
    print("11.1 基本数据类:")
    user = User("张三", 25)
    print(f"用户: {user}")
    
    print("\n11.2 带方法的数据类:")
    product = Product("笔记本电脑", 5999.99, "电子产品", 10)
    print(f"产品: {product}")
    print(f"总价值: ¥{product.total_value():.2f}")
    
    print("\n11.3 数据类比较:")
    user1 = User("李四", 30, "lisi@example.com")
    user2 = User("李四", 30, "lisi@example.com")
    print(f"用户1 == 用户2: {user1 == user2}")

# ==================== 12. 枚举增强 (Python 3.11+) ====================
print("\n12. 枚举增强 - Python 3.11+")
print("-" * 50)

def demo_enum_enhancements():
    """演示枚举的新特性"""
    
    class Status(Enum):
        """状态枚举"""
        PENDING = "pending"
        ACTIVE = "active"
        INACTIVE = "inactive"
        DELETED = "deleted"
        
        def __str__(self):
            return self.value
        
        @classmethod
        def from_string(cls, value: str) -> 'Status':
            """从字符串创建枚举"""
            for member in cls:
                if member.value == value:
                    return member
            raise ValueError(f"无效的状态值: {value}")
    
    # 测试枚举
    print("12.1 基本枚举:")
    for status in Status:
        print(f"  {status.name}: {status.value}")
    
    print("\n12.2 枚举比较:")
    status1 = Status.ACTIVE
    status2 = Status.ACTIVE
    print(f"status1 == status2: {status1 == status2}")
    
    print("\n12.3 从字符串创建枚举:")
    try:
        active_status = Status.from_string("active")
        print(f"从字符串创建: {active_status}")
    except ValueError as e:
        print(f"错误: {e}")

# ==================== 13. 实际应用示例 ====================
print("\n13. 实际应用示例")
print("-" * 50)

def demo_real_world_applications():
    """演示新特性在实际应用中的使用"""
    
    # 13.1 配置管理
    def create_config():
        """创建应用配置"""
        base_config = {
            "host": "localhost",
            "port": 8080,
            "debug": False
        }
        
        dev_config = {
            "debug": True,
            "log_level": "DEBUG"
        }
        
        prod_config = {
            "host": "0.0.0.0",
            "port": 80,
            "log_level": "INFO"
        }
        
        # 使用字典合并运算符
        config = base_config | dev_config
        print(f"开发环境配置: {config}")
        
        config = base_config | prod_config
        print(f"生产环境配置: {config}")
    
    # 13.2 数据验证
    def validate_user_data(data: dict) -> bool:
        """验证用户数据"""
        required_fields = {"name", "age", "email"}
        
        # 使用海象运算符检查必需字段
        if missing := required_fields - set(data.keys()):
            print(f"缺少必需字段: {missing}")
            return False
        
        # 使用模式匹配验证数据类型
        match data:
            case {"name": str(name), "age": int(age), "email": str(email)}:
                if age < 0 or age > 150:
                    print("年龄必须在0-150之间")
                    return False
                if "@" not in email:
                    print("邮箱格式无效")
                    return False
                return True
            case _:
                print("数据类型无效")
                return False
    
    # 13.3 错误处理
    def process_user_requests(requests: list[dict]) -> None:
        """处理用户请求"""
        errors = []
        
        for i, request in enumerate(requests):
            try:
                if not validate_user_data(request):
                    raise ValueError(f"请求 {i+1} 数据无效")
                print(f"请求 {i+1} 处理成功")
            except Exception as e:
                errors.append(e)
        
        if errors:
            print(f"处理完成，遇到 {len(errors)} 个错误:")
            for error in errors:
                print(f"  - {error}")
    
    # 执行实际应用演示
    print("13.1 配置管理:")
    create_config()
    
    print("\n13.2 数据验证:")
    test_users = [
        {"name": "张三", "age": 25, "email": "zhangsan@example.com"},
        {"name": "李四", "age": -5, "email": "invalid-email"},
        {"name": "王五", "age": 30}
    ]
    
    for user in test_users:
        is_valid = validate_user_data(user)
        print(f"用户数据: {user}")
        print(f"验证结果: {'✅ 有效' if is_valid else '❌ 无效'}\n")
    
    print("13.3 批量处理:")
    process_user_requests(test_users)

# ==================== 主函数 ====================
def main():
    """主函数，运行所有演示"""
    
    # 检查Python版本
    if sys.version_info < (3, 8):
        print("❌ 此演示需要Python 3.8或更高版本")
        return
    
    # 运行所有演示
    demos = [
        demo_walrus_operator,
        demo_positional_arguments,
        demo_fstring_enhancements,
        demo_dict_merge,
        demo_type_annotations,
        demo_string_enhancements,
        demo_pattern_matching,
        demo_union_types,
        demo_exception_groups,
        demo_performance,
        demo_dataclass_enhancements,
        demo_enum_enhancements,
        demo_real_world_applications
    ]
    
    for demo in demos:
        try:
            demo()
        except Exception as e:
            print(f"演示 {demo.__name__} 时出错: {e}")
        print()

if __name__ == "__main__":
    main()
    print("\n" + "=" * 60)
    print("Python新特性演示完成！")
    print("=" * 60) 