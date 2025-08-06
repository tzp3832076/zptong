# my_package/string_utils.py
# 字符串工具模块

import re

class StringUtils:
    """字符串工具类"""
    
    @staticmethod
    def reverse(text):
        """反转字符串"""
        return text[::-1]
    
    @staticmethod
    def count_words(text):
        """计算单词数量"""
        return len(text.split())
    
    @staticmethod
    def is_palindrome(text):
        """判断是否为回文"""
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def capitalize_words(text):
        """将每个单词首字母大写"""
        return text.title()
    
    @staticmethod
    def remove_duplicates(text):
        """移除重复字符"""
        seen = set()
        result = []
        for char in text:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)

def validate_email(email):
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def extract_numbers(text):
    """提取文本中的数字"""
    return re.findall(r'\d+', text)

def format_phone_number(phone):
    """格式化电话号码"""
    # 移除所有非数字字符
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 11:
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    return phone

# 模块的公共接口
__all__ = [
    'StringUtils',
    'validate_email',
    'extract_numbers',
    'format_phone_number'
] 