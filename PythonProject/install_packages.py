#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动安装常用Python包脚本
"""

import subprocess
import sys

def install_package(package):
    """安装单个包"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ {package} 安装成功")
    except subprocess.CalledProcessError:
        print(f"✗ {package} 安装失败")

def main():
    # 常用包列表
    packages = [
        "numpy",
        "pandas", 
        "matplotlib",
        "requests",
        "pillow",
        "flask",
        "pytest",
        "black",
        "flake8"
    ]
    
    print("开始安装常用Python包...")
    for package in packages:
        install_package(package)
    print("安装完成！")

if __name__ == "__main__":
    main()
