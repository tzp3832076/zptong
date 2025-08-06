# Python 数据结构完整演示文件
# 作者：AI助手
# 功能：展示Python中所有数据结构的用法和增删改查操作

print("=" * 60)
print("Python 数据结构完整演示")
print("=" * 60)

# ==================== 1. 列表 (List) ====================
print("\n1. 列表 (List):")
print("-" * 40)

# 1.1 创建列表
print("1.1 创建列表:")
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

print(f"空列表: {empty_list}")
print(f"数字列表: {numbers}")
print(f"混合列表: {mixed_list}")
print(f"水果列表: {fruits}")

# 1.2 列表的增删改查操作
print("\n1.2 列表的增删改查操作:")

# 增加操作
print("增加操作:")
fruits.append("西瓜")  # 在末尾添加
print(f"append('西瓜'): {fruits}")

fruits.insert(1, "梨子")  # 在指定位置插入
print(f"insert(1, '梨子'): {fruits}")

fruits.extend(["草莓", "蓝莓"])  # 扩展列表
print(f"extend(['草莓', '蓝莓']): {fruits}")

# 删除操作
print("\n删除操作:")
removed_fruit = fruits.pop()  # 删除并返回最后一个元素
print(f"pop(): 删除 '{removed_fruit}', 剩余: {fruits}")

removed_fruit = fruits.pop(2)  # 删除指定位置的元素
print(f"pop(2): 删除 '{removed_fruit}', 剩余: {fruits}")

fruits.remove("梨子")  # 删除指定值的元素
print(f"remove('梨子'): {fruits}")

del fruits[0]  # 删除指定位置的元素
print(f"del fruits[0]: {fruits}")

# 修改操作
print("\n修改操作:")
fruits[0] = "芒果"  # 修改指定位置的元素
print(f"fruits[0] = '芒果': {fruits}")

fruits[1:3] = ["菠萝", "椰子"]  # 切片修改
print(f"fruits[1:3] = ['菠萝', '椰子']: {fruits}")

# 查询操作
print("\n查询操作:")
print(f"fruits: {fruits}")
print(f"fruits[0]: {fruits[0]}")  # 索引访问
print(f"fruits[-1]: {fruits[-1]}")  # 负索引
print(f"fruits[1:3]: {fruits[1:3]}")  # 切片
print(f"fruits[::2]: {fruits[::2]}")  # 步长切片
print(f"'菠萝' in fruits: {'菠萝' in fruits}")  # 成员检查
print(f"fruits.index('菠萝'): {fruits.index('菠萝')}")  # 查找索引
print(f"fruits.count('菠萝'): {fruits.count('菠萝')}")  # 计数

# 1.3 列表的高级操作
print("\n1.3 列表的高级操作:")

# 排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原始数字: {numbers}")
numbers.sort()  # 原地排序
print(f"sort(): {numbers}")
numbers.sort(reverse=True)  # 降序排序
print(f"sort(reverse=True): {numbers}")

# 排序（不改变原列表）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"sorted(): {sorted_numbers}")
print(f"原列表: {numbers}")

# 反转
numbers.reverse()
print(f"reverse(): {numbers}")

# 列表推导式
squares = [x**2 for x in range(5)]
print(f"列表推导式: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"条件列表推导式: {even_squares}")

# ==================== 2. 元组 (Tuple) ====================
print("\n2. 元组 (Tuple):")
print("-" * 40)

# 2.1 创建元组
print("2.1 创建元组:")
empty_tuple = ()
single_tuple = (1,)  # 注意逗号
numbers_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
coordinates = (10, 20)
person = ("张三", 25, "北京")

print(f"空元组: {empty_tuple}")
print(f"单元素元组: {single_tuple}")
print(f"数字元组: {numbers_tuple}")
print(f"混合元组: {mixed_tuple}")
print(f"坐标: {coordinates}")
print(f"人员信息: {person}")

# 2.2 元组的操作（元组是不可变的，只能查询）
print("\n2.2 元组的操作:")

# 查询操作
print("查询操作:")
print(f"person: {person}")
print(f"person[0]: {person[0]}")  # 索引访问
print(f"person[-1]: {person[-1]}")  # 负索引
print(f"person[1:3]: {person[1:3]}")  # 切片
print(f"'张三' in person: {'张三' in person}")  # 成员检查
print(f"person.index('张三'): {person.index('张三')}")  # 查找索引
print(f"person.count('张三'): {person.count('张三')}")  # 计数

# 元组解包
print("\n元组解包:")
name, age, city = person
print(f"name: {name}, age: {age}, city: {city}")

# 元组作为字典键
print("\n元组作为字典键:")
point_dict = {(0, 0): "原点", (1, 1): "点(1,1)"}
print(f"point_dict: {point_dict}")

# ==================== 3. 集合 (Set) ====================
print("\n3. 集合 (Set):")
print("-" * 40)

# 3.1 创建集合
print("3.1 创建集合:")
empty_set = set()
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"苹果", "香蕉", "橙子", "葡萄"}
mixed_set = {1, "hello", 3.14}

print(f"空集合: {empty_set}")
print(f"数字集合: {numbers_set}")
print(f"水果集合: {fruits_set}")
print(f"混合集合: {mixed_set}")

# 3.2 集合的增删改查操作
print("\n3.2 集合的增删改查操作:")

# 增加操作
print("增加操作:")
fruits_set.add("西瓜")  # 添加单个元素
print(f"add('西瓜'): {fruits_set}")

fruits_set.update(["草莓", "蓝莓"])  # 添加多个元素
print(f"update(['草莓', '蓝莓']): {fruits_set}")

# 删除操作
print("\n删除操作:")
fruits_set.remove("香蕉")  # 删除指定元素（如果不存在会报错）
print(f"remove('香蕉'): {fruits_set}")

fruits_set.discard("橙子")  # 删除指定元素（如果不存在不会报错）
print(f"discard('橙子'): {fruits_set}")

removed_fruit = fruits_set.pop()  # 删除并返回任意元素
print(f"pop(): 删除 '{removed_fruit}', 剩余: {fruits_set}")

fruits_set.clear()  # 清空集合
print(f"clear(): {fruits_set}")

# 查询操作
print("\n查询操作:")
fruits_set = {"苹果", "香蕉", "橙子", "葡萄"}
print(f"fruits_set: {fruits_set}")
print(f"'苹果' in fruits_set: {'苹果' in fruits_set}")  # 成员检查
print(f"len(fruits_set): {len(fruits_set)}")  # 长度

# 3.3 集合的高级操作
print("\n3.3 集合的高级操作:")

# 集合运算
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"set1: {set1}")
print(f"set2: {set2}")

print(f"并集: set1 | set2 = {set1 | set2}")
print(f"并集: set1.union(set2) = {set1.union(set2)}")

print(f"交集: set1 & set2 = {set1 & set2}")
print(f"交集: set1.intersection(set2) = {set1.intersection(set2)}")

print(f"差集: set1 - set2 = {set1 - set2}")
print(f"差集: set1.difference(set2) = {set1.difference(set2)}")

print(f"对称差集: set1 ^ set2 = {set1 ^ set2}")
print(f"对称差集: set1.symmetric_difference(set2) = {set1.symmetric_difference(set2)}")

# 集合推导式
even_set = {x for x in range(10) if x % 2 == 0}
print(f"集合推导式: {even_set}")

# ==================== 4. 字典 (Dictionary) ====================
print("\n4. 字典 (Dictionary):")
print("-" * 40)

# 4.1 创建字典
print("4.1 创建字典:")
empty_dict = {}
person_dict = {"name": "张三", "age": 25, "city": "北京"}
scores = {"数学": 85, "英语": 92, "物理": 78}
mixed_dict = {1: "one", "two": 2, (1, 2): "tuple_key"}

print(f"空字典: {empty_dict}")
print(f"人员字典: {person_dict}")
print(f"成绩字典: {scores}")
print(f"混合字典: {mixed_dict}")

# 4.2 字典的增删改查操作
print("\n4.2 字典的增删改查操作:")

# 增加操作
print("增加操作:")
person_dict["job"] = "工程师"  # 添加新键值对
print(f"添加 'job': {person_dict}")

person_dict.update({"salary": 8000, "department": "技术部"})  # 批量添加
print(f"update(): {person_dict}")

# 删除操作
print("\n删除操作:")
removed_value = person_dict.pop("age")  # 删除并返回指定键的值
print(f"pop('age'): 删除值 '{removed_value}', 剩余: {person_dict}")

del person_dict["city"]  # 删除指定键值对
print(f"del person_dict['city']: {person_dict}")

person_dict.popitem()  # 删除并返回最后一个键值对
print(f"popitem(): {person_dict}")

person_dict.clear()  # 清空字典
print(f"clear(): {person_dict}")

# 修改操作
print("\n修改操作:")
person_dict = {"name": "张三", "age": 25, "city": "北京"}
person_dict["age"] = 26  # 修改值
print(f"修改年龄: {person_dict}")

person_dict.update({"age": 27, "city": "上海"})  # 批量修改
print(f"批量修改: {person_dict}")

# 查询操作
print("\n查询操作:")
print(f"person_dict: {person_dict}")
print(f"person_dict['name']: {person_dict['name']}")  # 键访问
print(f"person_dict.get('age'): {person_dict.get('age')}")  # get方法
print(f"person_dict.get('salary', '未知'): {person_dict.get('salary', '未知')}")  # 带默认值
print(f"'name' in person_dict: {'name' in person_dict}")  # 键检查
print(f"person_dict.keys(): {list(person_dict.keys())}")  # 所有键
print(f"person_dict.values(): {list(person_dict.values())}")  # 所有值
print(f"person_dict.items(): {list(person_dict.items())}")  # 所有键值对

# 4.3 字典的高级操作
print("\n4.3 字典的高级操作:")

# 字典推导式
square_dict = {x: x**2 for x in range(5)}
print(f"字典推导式: {square_dict}")

# 合并字典
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}  # Python 3.5+
print(f"合并字典: {merged_dict}")

# 嵌套字典
nested_dict = {
    "person": {
        "name": "李四",
        "age": 30,
        "address": {
            "city": "广州",
            "street": "天河路"
        }
    }
}
print(f"嵌套字典: {nested_dict}")
print(f"访问嵌套值: {nested_dict['person']['address']['city']}")

# ==================== 5. 字符串 (String) ====================
print("\n5. 字符串 (String):")
print("-" * 40)

# 5.1 创建字符串
print("5.1 创建字符串:")
empty_string = ""
simple_string = "Hello, World!"
chinese_string = "你好，世界！"
multi_line = """这是一个
多行字符串"""

print(f"空字符串: '{empty_string}'")
print(f"简单字符串: '{simple_string}'")
print(f"中文字符串: '{chinese_string}'")
print(f"多行字符串: {multi_line}")

# 5.2 字符串的增删改查操作
print("\n5.2 字符串的增删改查操作:")

# 增加操作（字符串是不可变的，需要创建新字符串）
print("增加操作:")
text = "Hello"
text += " World"  # 字符串拼接
print(f"字符串拼接: '{text}'")

text = "Hello" + " " + "World"  # 使用+拼接
print(f"使用+拼接: '{text}'")

text = " ".join(["Hello", "World", "Python"])  # 使用join拼接
print(f"使用join拼接: '{text}'")

# 查询操作
print("\n查询操作:")
text = "Hello, World, Python"
print(f"text: '{text}'")
print(f"text[0]: '{text[0]}'")  # 索引访问
print(f"text[-1]: '{text[-1]}'")  # 负索引
print(f"text[7:12]: '{text[7:12]}'")  # 切片
print(f"text[::2]: '{text[::2]}'")  # 步长切片
print(f"'World' in text: {'World' in text}")  # 成员检查
print(f"text.find('World'): {text.find('World')}")  # 查找位置
print(f"text.count('o'): {text.count('o')}")  # 计数
print(f"len(text): {len(text)}")  # 长度

# 5.3 字符串的高级操作
print("\n5.3 字符串的高级操作:")

# 字符串方法
text = "  Hello, World!  "
print(f"原始文本: '{text}'")
print(f"strip(): '{text.strip()}'")  # 去除首尾空白
print(f"upper(): '{text.upper()}'")  # 转大写
print(f"lower(): '{text.lower()}'")  # 转小写
print(f"title(): '{text.title()}'")  # 标题格式
print(f"replace('World', 'Python'): '{text.replace('World', 'Python')}'")  # 替换
print(f"split(', '): {text.split(', ')}")  # 分割

# 字符串格式化
name = "张三"
age = 25
print(f"f-string: 我叫{name}，今年{age}岁")
print("format(): 我叫{}，今年{}岁".format(name, age))
print("%%格式化: 我叫%s，今年%d岁" % (name, age))

# 字符串编码
text = "Hello, 世界！"
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')
print(f"原始: '{text}'")
print(f"编码: {encoded}")
print(f"解码: '{decoded}'")

# ==================== 6. 数据结构的高级应用 ====================
print("\n6. 数据结构的高级应用:")
print("-" * 40)

# 6.1 嵌套数据结构
print("6.1 嵌套数据结构:")
nested_data = {
    "students": [
        {"name": "张三", "scores": [85, 92, 78]},
        {"name": "李四", "scores": [90, 88, 95]},
        {"name": "王五", "scores": [76, 85, 82]}
    ],
    "subjects": ("数学", "英语", "物理"),
    "passing_score": 60
}

print(f"嵌套数据结构: {nested_data}")

# 访问嵌套数据
print(f"第一个学生: {nested_data['students'][0]}")
print(f"第一个学生的数学成绩: {nested_data['students'][0]['scores'][0]}")
print(f"科目: {nested_data['subjects']}")

# 6.2 数据结构的转换
print("\n6.2 数据结构的转换:")
# 列表转集合
list_to_set = [1, 2, 2, 3, 3, 4]
unique_set = set(list_to_set)
print(f"列表转集合: {list_to_set} -> {unique_set}")

# 元组转列表
tuple_to_list = (1, 2, 3, 4, 5)
list_from_tuple = list(tuple_to_list)
print(f"元组转列表: {tuple_to_list} -> {list_from_tuple}")

# 字典键值对转列表
dict_items = {"a": 1, "b": 2, "c": 3}
items_list = list(dict_items.items())
print(f"字典转键值对列表: {dict_items} -> {items_list}")

# 6.3 数据结构的性能比较
print("\n6.3 数据结构的性能比较:")
import time

# 列表查找性能
large_list = list(range(10000))
start_time = time.time()
9999 in large_list
list_time = time.time() - start_time

# 集合查找性能
large_set = set(range(10000))
start_time = time.time()
9999 in large_set
set_time = time.time() - start_time

print(f"列表查找时间: {list_time:.6f}秒")
print(f"集合查找时间: {set_time:.6f}秒")
if set_time > 0:
    print(f"性能差异: 列表比集合慢 {list_time/set_time:.1f}倍")
else:
    print("性能差异: 集合查找太快，无法计算倍数")

# 6.4 实际应用示例
print("\n6.4 实际应用示例:")

# 学生成绩管理系统
students = [
    {"id": 1, "name": "张三", "scores": {"数学": 85, "英语": 92, "物理": 78}},
    {"id": 2, "name": "李四", "scores": {"数学": 90, "英语": 88, "物理": 95}},
    {"id": 3, "name": "王五", "scores": {"数学": 76, "英语": 85, "物理": 82}}
]

# 计算平均分
def calculate_average(student):
    scores = student["scores"].values()
    return sum(scores) / len(scores)

# 找出成绩最好的学生
best_student = max(students, key=calculate_average)
print(f"成绩最好的学生: {best_student['name']}, 平均分: {calculate_average(best_student):.1f}")

# 按平均分排序
sorted_students = sorted(students, key=calculate_average, reverse=True)
print("按平均分排序:")
for student in sorted_students:
    avg = calculate_average(student)
    print(f"{student['name']}: {avg:.1f}")

print("\n" + "=" * 60)
print("Python 数据结构演示完成！")
print("=" * 60) 