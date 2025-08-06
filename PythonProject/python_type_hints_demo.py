# Python 类型提示完整演示文件
# 作者：AI助手
# 功能：展示Python类型提示的使用方法和最佳实践

print("=" * 60)
print("Python 类型提示完整演示")
print("=" * 60)

# ==================== 1. 类型提示基础 ====================
print("\n1. 类型提示基础:")
print("-" * 40)

# 1.1 基本类型注解
print("1.1 基本类型注解:")

def greet(name: str) -> str:
    """简单的类型注解示例"""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """数字相加函数"""
    return a + b

def calculate_area(radius: float) -> float:
    """计算圆的面积"""
    import math
    return math.pi * radius ** 2

# 测试基本类型注解
print(f"greet('Alice'): {greet('Alice')}")
print(f"add_numbers(5, 3): {add_numbers(5, 3)}")
print(f"calculate_area(2.5): {calculate_area(2.5):.2f}")

# 1.2 复杂类型注解
print("\n1.2 复杂类型注解:")

from typing import List, Dict, Tuple, Optional, Union, Any

def process_numbers(numbers: List[int]) -> List[int]:
    """处理数字列表"""
    return [x * 2 for x in numbers if x > 0]

def get_user_info(user_id: int) -> Dict[str, Union[str, int]]:
    """获取用户信息"""
    return {
        "id": user_id,
        "name": "张三",
        "age": 25,
        "email": "zhangsan@example.com"
    }

def find_coordinates() -> Tuple[float, float]:
    """返回坐标"""
    return (40.7128, -74.0060)

# 测试复杂类型注解
numbers = [1, 2, 3, 4, 5]
print(f"process_numbers({numbers}): {process_numbers(numbers)}")

user_info = get_user_info(123)
print(f"get_user_info(123): {user_info}")

coords = find_coordinates()
print(f"find_coordinates(): {coords}")

# ==================== 2. 高级类型注解 ====================
print("\n2. 高级类型注解:")
print("-" * 40)

# 2.1 Optional类型
print("2.1 Optional类型:")

def find_user(user_id: int) -> Optional[Dict[str, Any]]:
    """查找用户，可能返回None"""
    users = {
        1: {"name": "Alice", "age": 25},
        2: {"name": "Bob", "age": 30}
    }
    return users.get(user_id)

# 测试Optional类型
user1 = find_user(1)
user3 = find_user(3)
print(f"find_user(1): {user1}")
print(f"find_user(3): {user3}")

# 2.2 Union类型
print("\n2.2 Union类型:")

def process_data(data: Union[str, int, float]) -> str:
    """处理不同类型的数据"""
    if isinstance(data, str):
        return f"字符串: {data}"
    elif isinstance(data, (int, float)):
        return f"数字: {data}"
    else:
        return "未知类型"

# 测试Union类型
print(f"process_data('hello'): {process_data('hello')}")
print(f"process_data(42): {process_data(42)}")
print(f"process_data(3.14): {process_data(3.14)}")

# 2.3 泛型类型
print("\n2.3 泛型类型:")

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    """泛型栈类"""
    
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        """压入元素"""
        self.items.append(item)
    
    def pop(self) -> T:
        """弹出元素"""
        if not self.items:
            raise IndexError("栈为空")
        return self.items.pop()
    
    def peek(self) -> T:
        """查看栈顶元素"""
        if not self.items:
            raise IndexError("栈为空")
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """检查栈是否为空"""
        return len(self.items) == 0

# 测试泛型类型
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(f"int_stack.pop(): {int_stack.pop()}")
print(f"int_stack.peek(): {int_stack.peek()}")

# ==================== 3. 函数类型注解 ====================
print("\n3. 函数类型注解:")
print("-" * 40)

from typing import Callable

# 3.1 函数作为参数
print("3.1 函数作为参数:")

def apply_operation(func: Callable[[int], int], value: int) -> int:
    """应用函数到值上"""
    return func(value)

def square(x: int) -> int:
    return x ** 2

def double(x: int) -> int:
    return x * 2

# 测试函数类型注解
print(f"apply_operation(square, 5): {apply_operation(square, 5)}")
print(f"apply_operation(double, 5): {apply_operation(double, 5)}")

# 3.2 高阶函数
print("\n3.2 高阶函数:")

def create_multiplier(factor: int) -> Callable[[int], int]:
    """创建乘法器函数"""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

# 测试高阶函数
multiply_by_3 = create_multiplier(3)
multiply_by_5 = create_multiplier(5)
print(f"multiply_by_3(4): {multiply_by_3(4)}")
print(f"multiply_by_5(4): {multiply_by_5(4)}")

# ==================== 4. 类类型注解 ====================
print("\n4. 类类型注解:")
print("-" * 40)

# 4.1 类属性类型注解
print("4.1 类属性类型注解:")

class Person:
    """人员类"""
    
    def __init__(self, name: str, age: int, email: Optional[str] = None) -> None:
        self.name: str = name
        self.age: int = age
        self.email: Optional[str] = email
        self.friends: List['Person'] = []
    
    def add_friend(self, friend: 'Person') -> None:
        """添加朋友"""
        self.friends.append(friend)
    
    def get_info(self) -> Dict[str, Union[str, int]]:
        """获取人员信息"""
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "friends_count": len(self.friends)
        }
    
    def __str__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"

# 测试类类型注解
alice = Person("Alice", 25, "alice@example.com")
bob = Person("Bob", 30)
alice.add_friend(bob)
print(f"alice: {alice}")
print(f"alice.get_info(): {alice.get_info()}")

# 4.2 继承和类型注解
print("\n4.2 继承和类型注解:")

class Student(Person):
    """学生类"""
    
    def __init__(self, name: str, age: int, student_id: str, 
                 email: Optional[str] = None) -> None:
        super().__init__(name, age, email)
        self.student_id: str = student_id
        self.courses: List[str] = []
    
    def add_course(self, course: str) -> None:
        """添加课程"""
        self.courses.append(course)
    
    def get_info(self) -> Dict[str, Union[str, int]]:
        """获取学生信息"""
        info = super().get_info()
        info.update({
            "student_id": self.student_id,
            "courses_count": len(self.courses)
        })
        return info

# 测试继承类型注解
student = Student("Charlie", 20, "S12345", "charlie@university.edu")
student.add_course("Python编程")
student.add_course("数据结构")
print(f"student: {student}")
print(f"student.get_info(): {student.get_info()}")

# ==================== 5. 实际应用示例 ====================
print("\n5. 实际应用示例:")
print("-" * 40)

# 5.1 数据处理函数
print("5.1 数据处理函数:")

def process_user_data(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """处理用户数据"""
    processed_users = []
    
    for user in users:
        if isinstance(user, dict) and 'name' in user and 'age' in user:
            processed_user = {
                'name': user['name'],
                'age': user['age'],
                'status': 'active' if user.get('age', 0) >= 18 else 'minor',
                'formatted_name': user['name'].upper()
            }
            processed_users.append(processed_user)
    
    return processed_users

# 测试数据处理函数
sample_users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 16},
    {'name': 'Charlie', 'age': 30}
]

processed = process_user_data(sample_users)
print("原始用户数据:")
for user in sample_users:
    print(f"  {user}")
print("处理后的用户数据:")
for user in processed:
    print(f"  {user}")

# 5.2 API响应处理
print("\n5.2 API响应处理:")

from typing import TypedDict

class UserResponse(TypedDict):
    """用户响应类型"""
    id: int
    name: str
    email: str
    is_active: bool

def parse_api_response(response_data: Dict[str, Any]) -> Optional[UserResponse]:
    """解析API响应"""
    try:
        return {
            'id': response_data['id'],
            'name': response_data['name'],
            'email': response_data['email'],
            'is_active': response_data.get('is_active', True)
        }
    except KeyError:
        return None

# 测试API响应处理
api_response = {
    'id': 123,
    'name': 'David',
    'email': 'david@example.com',
    'is_active': True
}

parsed_user = parse_api_response(api_response)
if parsed_user:
    print(f"解析的用户数据: {parsed_user}")
else:
    print("解析失败")

# ==================== 6. 类型检查工具 ====================
print("\n6. 类型检查工具:")
print("-" * 40)

print("6.1 常用类型检查工具:")
print("- mypy: 最流行的Python类型检查器")
print("- pyright: Microsoft开发的类型检查器")
print("- pyre: Facebook开发的类型检查器")
print("- pytype: Google开发的类型检查器")

print("\n6.2 mypy使用示例:")
print("安装: pip install mypy")
print("检查文件: mypy your_file.py")
print("检查目录: mypy your_directory/")
print("忽略错误: mypy --ignore-missing-imports your_file.py")

# 6.3 类型检查配置
print("\n6.3 类型检查配置 (mypy.ini):")
mypy_config = """[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
warn_unreachable = True
strict_equality = True

[mypy.plugins.numpy.*]
ignore_missing_imports = True

[mypy-pandas.*]
ignore_missing_imports = True
"""

with open('mypy.ini', 'w', encoding='utf-8') as f:
    f.write(mypy_config)
print("已创建 mypy.ini 配置文件")

# ==================== 7. 最佳实践 ====================
print("\n7. 最佳实践:")
print("-" * 40)

print("7.1 类型注解最佳实践:")
print("- 为公共API添加类型注解")
print("- 使用Optional表示可能为None的值")
print("- 使用Union表示多种类型")
print("- 避免使用Any，除非必要")
print("- 为复杂数据结构使用TypedDict")

print("\n7.2 渐进式类型注解:")
print("- 可以逐步添加类型注解")
print("- 使用# type: ignore忽略特定行的类型检查")
print("- 使用@typing.no_type_check装饰器忽略函数")

print("\n7.3 常见模式:")
print("- 使用TypeVar创建泛型")
print("- 使用Protocol定义接口")
print("- 使用Literal定义字面量类型")
print("- 使用Final定义常量")

# ==================== 8. 高级特性 ====================
print("\n8. 高级特性:")
print("-" * 40)

# 8.1 Protocol类型
print("8.1 Protocol类型:")

from typing import Protocol

class Drawable(Protocol):
    """可绘制对象协议"""
    def draw(self) -> str:
        ...

class Circle:
    """圆形类"""
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def draw(self) -> str:
        return f"绘制半径为{self.radius}的圆形"

class Square:
    """正方形类"""
    def __init__(self, side: float) -> None:
        self.side = side
    
    def draw(self) -> str:
        return f"绘制边长为{self.side}的正方形"

def draw_shape(shape: Drawable) -> str:
    """绘制形状"""
    return shape.draw()

# 测试Protocol类型
circle = Circle(5.0)
square = Square(4.0)
print(f"draw_shape(circle): {draw_shape(circle)}")
print(f"draw_shape(square): {draw_shape(square)}")

# 8.2 Literal类型
print("\n8.2 Literal类型:")

from typing import Literal

def get_status(status: Literal["active", "inactive", "pending"]) -> str:
    """获取状态描述"""
    status_descriptions = {
        "active": "用户处于活跃状态",
        "inactive": "用户处于非活跃状态", 
        "pending": "用户状态待确认"
    }
    return status_descriptions[status]

# 测试Literal类型
print(f"get_status('active'): {get_status('active')}")
print(f"get_status('inactive'): {get_status('inactive')}")

# 8.3 Final类型
print("\n8.3 Final类型:")

from typing import Final

MAX_RETRY_COUNT: Final[int] = 3
DEFAULT_TIMEOUT: Final[float] = 30.0
API_BASE_URL: Final[str] = "https://api.example.com"

print(f"MAX_RETRY_COUNT: {MAX_RETRY_COUNT}")
print(f"DEFAULT_TIMEOUT: {DEFAULT_TIMEOUT}")
print(f"API_BASE_URL: {API_BASE_URL}")

# ==================== 9. 实际项目示例 ====================
print("\n9. 实际项目示例:")
print("-" * 40)

# 9.1 数据库操作类型注解
print("9.1 数据库操作类型注解:")

from typing import Iterator

class DatabaseConnection:
    """数据库连接类"""
    
    def __init__(self, host: str, port: int, database: str) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.connected = False
    
    def connect(self) -> bool:
        """连接数据库"""
        # 模拟连接
        self.connected = True
        return True
    
    def disconnect(self) -> None:
        """断开连接"""
        self.connected = False
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """执行查询"""
        if not self.connected:
            raise RuntimeError("数据库未连接")
        # 模拟查询结果
        return [{"id": 1, "name": "测试数据"}]

def get_users_by_age_range(conn: DatabaseConnection, 
                          min_age: int, 
                          max_age: int) -> Iterator[Dict[str, Any]]:
    """根据年龄范围获取用户"""
    query = f"SELECT * FROM users WHERE age BETWEEN {min_age} AND {max_age}"
    results = conn.execute_query(query)
    for result in results:
        yield result

# 测试数据库操作
db = DatabaseConnection("localhost", 5432, "testdb")
db.connect()
users = list(get_users_by_age_range(db, 18, 30))
print(f"查询结果: {users}")

# 9.2 Web API类型注解
print("\n9.2 Web API类型注解:")

from typing import NamedTuple

class User(NamedTuple):
    """用户数据类"""
    id: int
    name: str
    email: str
    age: int

class APIResponse(NamedTuple):
    """API响应类"""
    success: bool
    data: Optional[List[User]]
    message: str
    status_code: int

def create_user_api_response(users: List[User], 
                           message: str = "Success") -> APIResponse:
    """创建用户API响应"""
    return APIResponse(
        success=True,
        data=users,
        message=message,
        status_code=200
    )

def create_error_response(message: str, status_code: int = 400) -> APIResponse:
    """创建错误响应"""
    return APIResponse(
        success=False,
        data=None,
        message=message,
        status_code=status_code
    )

# 测试Web API类型注解
sample_users = [
    User(1, "Alice", "alice@example.com", 25),
    User(2, "Bob", "bob@example.com", 30)
]

success_response = create_user_api_response(sample_users)
error_response = create_error_response("用户不存在", 404)

print(f"成功响应: {success_response}")
print(f"错误响应: {error_response}")

# ==================== 10. 工具和脚本 ====================
print("\n10. 工具和脚本:")
print("-" * 40)

# 10.1 类型检查脚本
def create_type_check_script():
    """创建类型检查脚本"""
    script_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python类型检查工具
"""

import subprocess
import sys
import os

def run_mypy(file_path: str) -> bool:
    """运行mypy类型检查"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "mypy", file_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"✓ {file_path} 类型检查通过")
            return True
        else:
            print(f"✗ {file_path} 类型检查失败:")
            print(result.stdout)
            print(result.stderr)
            return False
    except FileNotFoundError:
        print("mypy未安装，请运行: pip install mypy")
        return False

def check_directory(directory: str) -> None:
    """检查目录中的所有Python文件"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                run_mypy(file_path)

def main():
    if len(sys.argv) < 2:
        print("用法: python type_checker.py <文件或目录>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if os.path.isfile(target):
        run_mypy(target)
    elif os.path.isdir(target):
        check_directory(target)
    else:
        print(f"错误: {target} 不存在")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''
    
    with open('type_checker.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    print("已创建类型检查工具: type_checker.py")

create_type_check_script()

# 10.2 类型注解生成工具
def create_type_generator():
    """创建类型注解生成工具"""
    script_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
类型注解生成工具
"""

import ast
import sys
from typing import List, Dict, Any

class TypeAnnotationGenerator(ast.NodeVisitor):
    """类型注解生成器"""
    
    def __init__(self):
        self.suggestions = []
    
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """访问函数定义"""
        if not node.returns:
            # 分析函数体，推测返回类型
            return_type = self._infer_return_type(node)
            if return_type:
                self.suggestions.append({
                    'type': 'function',
                    'name': node.name,
                    'line': node.lineno,
                    'suggestion': f"-> {return_type}"
                })
        
        self.generic_visit(node)
    
    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        """访问带注解的赋值"""
        if not node.annotation:
            # 分析值，推测类型
            value_type = self._infer_value_type(node.value)
            if value_type:
                self.suggestions.append({
                    'type': 'variable',
                    'name': getattr(node.target, 'id', 'unknown'),
                    'line': node.lineno,
                    'suggestion': f": {value_type}"
                })
        
        self.generic_visit(node)
    
    def _infer_return_type(self, node: ast.FunctionDef) -> str:
        """推测返回类型"""
        # 简化的类型推测逻辑
        for stmt in ast.walk(node):
            if isinstance(stmt, ast.Return):
                if stmt.value:
                    return self._infer_value_type(stmt.value)
        return "None"
    
    def _infer_value_type(self, node: ast.AST) -> str:
        """推测值类型"""
        if isinstance(node, ast.Constant):
            if isinstance(node.value, str):
                return "str"
            elif isinstance(node.value, int):
                return "int"
            elif isinstance(node.value, float):
                return "float"
            elif isinstance(node.value, bool):
                return "bool"
        elif isinstance(node, ast.List):
            return "List[Any]"
        elif isinstance(node, ast.Dict):
            return "Dict[str, Any]"
        return "Any"

def analyze_file(file_path: str) -> List[Dict[str, Any]]:
    """分析文件并生成类型注解建议"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        generator = TypeAnnotationGenerator()
        generator.visit(tree)
        
        return generator.suggestions
    except Exception as e:
        print(f"分析文件 {file_path} 时出错: {e}")
        return []

def main():
    if len(sys.argv) < 2:
        print("用法: python type_generator.py <Python文件>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    suggestions = analyze_file(file_path)
    
    if suggestions:
        print(f"\\n为 {file_path} 生成的类型注解建议:")
        for suggestion in suggestions:
            print(f"第{suggestion['line']}行 {suggestion['name']}: {suggestion['suggestion']}")
    else:
        print("未找到需要添加类型注解的地方")

if __name__ == "__main__":
    main()
'''
    
    with open('type_generator.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    print("已创建类型注解生成工具: type_generator.py")

create_type_generator()

# ==================== 11. 总结 ====================
print("\n11. 总结:")
print("-" * 40)

print("11.1 类型提示的优势:")
print("- 提高代码可读性和可维护性")
print("- 帮助IDE提供更好的代码补全和错误检查")
print("- 减少运行时错误")
print("- 便于重构和调试")

print("\n11.2 使用建议:")
print("- 从公共API开始添加类型注解")
print("- 使用类型检查工具验证代码")
print("- 保持类型注解的简洁性")
print("- 定期更新和维护类型注解")

print("\n11.3 学习资源:")
print("- Python官方文档: typing模块")
print("- mypy文档: https://mypy.readthedocs.io/")
print("- PEP 484: 类型注解规范")
print("- PEP 585: 泛型类型注解")

print("\n" + "=" * 80)
print("Python 类型提示完整演示 - 全部内容完成！")
print("=" * 80)
print("类型提示是Python现代化的重要特性")
print("建议:")
print("1. 在项目中逐步引入类型注解")
print("2. 使用mypy等工具进行类型检查")
print("3. 学习更多高级类型注解特性")
print("4. 关注Python类型系统的发展")
print("=" * 80) 