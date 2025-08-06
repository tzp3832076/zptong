#!/usr/bin/env python3
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
