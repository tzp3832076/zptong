#!/usr/bin/env python3
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
        print(f"\n为 {file_path} 生成的类型注解建议:")
        for suggestion in suggestions:
            print(f"第{suggestion['line']}行 {suggestion['name']}: {suggestion['suggestion']}")
    else:
        print("未找到需要添加类型注解的地方")

if __name__ == "__main__":
    main()
