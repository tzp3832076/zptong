#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
包信息查看工具
"""

import subprocess
import sys
import json

def get_package_info(package_name):
    """获取包信息"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", package_name],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"包 {package_name} 未安装"
    except Exception as e:
        return f"获取包信息失败: {e}"

def list_installed_packages():
    """列出已安装的包"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=json"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            packages = json.loads(result.stdout)
            return packages
        else:
            return []
    except Exception as e:
        print(f"获取包列表失败: {e}")
        return []

def main():
    print("=== Python包信息查看工具 ===")
    
    # 列出所有已安装的包
    print("\n已安装的包:")
    packages = list_installed_packages()
    for package in packages:
        print(f"- {package['name']} {package['version']}")
    
    # 查看特定包信息
    target_packages = ["numpy", "pandas", "matplotlib"]
    print("\n特定包详细信息:")
    for package in target_packages:
        print(f"\n{package}:")
        print(get_package_info(package))

if __name__ == "__main__":
    main()
