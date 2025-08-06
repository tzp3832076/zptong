#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 高阶操作演示
包含文件操作、网络编程、多线程编程等高级功能
"""

import os
import sys
import json
import csv
import pickle
import zipfile
import shutil
import tempfile
import threading
import queue
import time
import random
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
import urllib.request
import urllib.parse
import urllib.error
import socket
import ssl
import http.client
import requests
from io import BytesIO, StringIO
import xml.etree.ElementTree as ET
import hashlib
import base64


# ==================== 文件操作 ====================

class FileOperations:
    """文件操作类 - 演示各种文件处理技术"""
    
    def __init__(self, base_dir: str = "temp_files"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('FileOperations')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def create_sample_files(self) -> Dict[str, str]:
        """创建示例文件"""
        files = {}
        
        # 创建文本文件
        text_file = self.base_dir / "sample.txt"
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write("这是一个示例文本文件\n包含多行内容\n用于演示文件操作")
        files['text'] = str(text_file)
        
        # 创建JSON文件
        json_data = {
            "name": "张三",
            "age": 25,
            "skills": ["Python", "Java", "JavaScript"],
            "address": {
                "city": "北京",
                "street": "中关村大街"
            }
        }
        json_file = self.base_dir / "data.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        files['json'] = str(json_file)
        
        # 创建CSV文件
        csv_file = self.base_dir / "users.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['姓名', '年龄', '职业', '城市'])
            writer.writerow(['李四', 30, '工程师', '上海'])
            writer.writerow(['王五', 28, '设计师', '深圳'])
            writer.writerow(['赵六', 35, '产品经理', '杭州'])
        files['csv'] = str(csv_file)
        
        # 创建二进制文件
        binary_file = self.base_dir / "data.bin"
        with open(binary_file, 'wb') as f:
            pickle.dump({"message": "这是序列化的数据", "timestamp": time.time()}, f)
        files['binary'] = str(binary_file)
        
        self.logger.info(f"创建了 {len(files)} 个示例文件")
        return files
    
    def file_operations_demo(self):
        """文件操作演示"""
        print("\n=== 文件操作演示 ===")
        
        # 创建示例文件
        files = self.create_sample_files()
        
        # 1. 基本文件读写
        print("\n1. 基本文件读写:")
        text_file = files['text']
        with open(text_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"读取文件内容: {content}")
        
        # 2. JSON文件处理
        print("\n2. JSON文件处理:")
        with open(files['json'], 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"JSON数据: {data}")
        
        # 3. CSV文件处理
        print("\n3. CSV文件处理:")
        with open(files['csv'], 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"用户: {row}")
        
        # 4. 二进制文件处理
        print("\n4. 二进制文件处理:")
        with open(files['binary'], 'rb') as f:
            data = pickle.load(f)
            print(f"反序列化数据: {data}")
        
        # 5. 文件信息获取
        print("\n5. 文件信息:")
        for file_type, file_path in files.items():
            path = Path(file_path)
            print(f"{file_type}文件: {path.name}")
            print(f"  大小: {path.stat().st_size} 字节")
            print(f"  修改时间: {datetime.fromtimestamp(path.stat().st_mtime)}")
        
        # 6. 文件搜索和过滤
        print("\n6. 文件搜索:")
        all_files = list(self.base_dir.glob("*"))
        print(f"目录中的所有文件: {[f.name for f in all_files]}")
        
        # 7. 文件复制和移动
        print("\n7. 文件复制:")
        backup_dir = self.base_dir / "backup"
        backup_dir.mkdir(exist_ok=True)
        
        for file_path in files.values():
            src = Path(file_path)
            dst = backup_dir / f"backup_{src.name}"
            shutil.copy2(src, dst)
            print(f"复制 {src.name} 到 {dst}")
        
        # 8. 压缩文件
        print("\n8. 创建压缩文件:")
        zip_file = self.base_dir / "archive.zip"
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files.values():
                zipf.write(file_path, Path(file_path).name)
        print(f"创建压缩文件: {zip_file}")
        
        # 9. 临时文件操作
        print("\n9. 临时文件操作:")
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.tmp') as tmp:
            tmp.write("临时文件内容")
            tmp_path = tmp.name
        
        with open(tmp_path, 'r') as f:
            print(f"临时文件内容: {f.read()}")
        
        os.unlink(tmp_path)  # 删除临时文件
        
        return files


# ==================== 网络编程 ====================

class NetworkOperations:
    """网络操作类 - 演示各种网络编程技术"""
    
    def __init__(self):
        self.logger = self._setup_logger()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Python-Network-Demo/1.0'
        })
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('NetworkOperations')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def basic_http_requests(self):
        """基本HTTP请求演示"""
        print("\n=== 基本HTTP请求演示 ===")
        
        # 1. GET请求
        print("\n1. GET请求:")
        try:
            response = self.session.get('https://httpbin.org/get', timeout=10)
            print(f"状态码: {response.status_code}")
            print(f"响应头: {dict(response.headers)}")
            print(f"响应内容: {response.json()}")
        except Exception as e:
            print(f"GET请求失败: {e}")
        
        # 2. POST请求
        print("\n2. POST请求:")
        try:
            data = {'name': '张三', 'age': 25}
            response = self.session.post('https://httpbin.org/post', json=data, timeout=10)
            print(f"状态码: {response.status_code}")
            print(f"响应内容: {response.json()}")
        except Exception as e:
            print(f"POST请求失败: {e}")
        
        # 3. 文件上传
        print("\n3. 文件上传:")
        try:
            # 创建临时文件
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
                tmp.write("这是一个测试文件")
                tmp_path = tmp.name
            
            with open(tmp_path, 'rb') as f:
                files = {'file': f}
                response = self.session.post('https://httpbin.org/post', files=files, timeout=10)
                print(f"文件上传状态码: {response.status_code}")
            
            os.unlink(tmp_path)  # 删除临时文件
        except Exception as e:
            print(f"文件上传失败: {e}")
    
    def advanced_network_operations(self):
        """高级网络操作演示"""
        print("\n=== 高级网络操作演示 ===")
        
        # 1. 自定义请求头
        print("\n1. 自定义请求头:")
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer demo-token',
            'X-Custom-Header': 'demo-value'
        }
        
        try:
            response = self.session.get('https://httpbin.org/headers', headers=headers, timeout=10)
            print(f"自定义请求头响应: {response.json()}")
        except Exception as e:
            print(f"自定义请求头失败: {e}")
        
        # 2. 会话管理
        print("\n2. 会话管理:")
        try:
            # 设置cookies
            self.session.get('https://httpbin.org/cookies/set/sessionid/12345', timeout=10)
            
            # 获取cookies
            response = self.session.get('https://httpbin.org/cookies', timeout=10)
            print(f"会话cookies: {response.json()}")
        except Exception as e:
            print(f"会话管理失败: {e}")
        
        # 3. 错误处理
        print("\n3. 错误处理:")
        urls_to_test = [
            'https://httpbin.org/status/200',
            'https://httpbin.org/status/404',
            'https://httpbin.org/status/500',
            'https://invalid-url-that-does-not-exist.com'
        ]
        
        for url in urls_to_test:
            try:
                response = self.session.get(url, timeout=5)
                print(f"{url}: 状态码 {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"{url}: 请求失败 - {e}")
        
        # 4. 重试机制
        print("\n4. 重试机制:")
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        try:
            response = self.session.get('https://httpbin.org/status/500', timeout=10)
            print(f"重试后的响应: {response.status_code}")
        except Exception as e:
            print(f"重试后仍然失败: {e}")
    
    def socket_programming_demo(self):
        """Socket编程演示"""
        print("\n=== Socket编程演示 ===")
        
        # 1. 简单的TCP客户端
        print("\n1. TCP客户端:")
        try:
            # 连接到HTTP服务器
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect(('httpbin.org', 80))
            
            # 发送HTTP请求
            request = "GET /get HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n"
            sock.send(request.encode())
            
            # 接收响应
            response = b""
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                response += data
            
            print(f"Socket响应长度: {len(response)} 字节")
            sock.close()
        except Exception as e:
            print(f"Socket连接失败: {e}")
        
        # 2. DNS查询
        print("\n2. DNS查询:")
        try:
            hostname = "www.baidu.com"
            ip_address = socket.gethostbyname(hostname)
            print(f"{hostname} 的IP地址: {ip_address}")
        except Exception as e:
            print(f"DNS查询失败: {e}")
        
        # 3. 端口扫描
        print("\n3. 端口扫描:")
        target_host = "localhost"
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995]
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_host, port))
                if result == 0:
                    print(f"端口 {port} 开放")
                sock.close()
            except Exception:
                pass


# ==================== 多线程编程 ====================

@dataclass
class TaskResult:
    """任务结果数据类"""
    task_id: int
    status: str
    result: Any
    execution_time: float
    thread_id: int


class ThreadingOperations:
    """多线程操作类 - 演示各种多线程编程技术"""
    
    def __init__(self):
        self.logger = self._setup_logger()
        self.results_queue = queue.Queue()
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.semaphore = threading.Semaphore(3)  # 限制并发数
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('ThreadingOperations')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def worker_function(self, task_id: int, duration: float = 1.0) -> TaskResult:
        """工作函数 - 模拟耗时任务"""
        thread_id = threading.current_thread().ident
        start_time = time.time()
        
        # 使用信号量控制并发
        with self.semaphore:
            self.logger.info(f"任务 {task_id} 开始执行 (线程 {thread_id})")
            
            # 模拟工作
            time.sleep(duration)
            
            # 模拟一些计算
            result = sum(i * i for i in range(1000))
            
            execution_time = time.time() - start_time
            
            # 线程安全的结果记录
            with self.lock:
                task_result = TaskResult(
                    task_id=task_id,
                    status="完成",
                    result=result,
                    execution_time=execution_time,
                    thread_id=thread_id
                )
                self.results_queue.put(task_result)
            
            self.logger.info(f"任务 {task_id} 完成 (耗时 {execution_time:.2f}秒)")
            return task_result
    
    def basic_threading_demo(self):
        """基本多线程演示"""
        print("\n=== 基本多线程演示 ===")
        
        # 1. 创建和启动线程
        print("\n1. 创建和启动线程:")
        threads = []
        
        for i in range(5):
            thread = threading.Thread(
                target=self.worker_function,
                args=(i, random.uniform(0.5, 2.0)),
                name=f"Worker-{i}"
            )
            threads.append(thread)
            thread.start()
            print(f"启动线程: {thread.name}")
        
        # 等待所有线程完成
        for thread in threads:
            thread.join()
        
        print("所有线程已完成")
        
        # 显示结果
        print("\n任务结果:")
        while not self.results_queue.empty():
            result = self.results_queue.get()
            print(f"任务 {result.task_id}: 状态={result.status}, "
                  f"结果={result.result}, 耗时={result.execution_time:.2f}秒")
    
    def thread_pool_demo(self):
        """线程池演示"""
        print("\n=== 线程池演示 ===")
        
        # 使用ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=4) as executor:
            # 提交任务
            futures = []
            for i in range(10):
                future = executor.submit(self.worker_function, i, random.uniform(0.3, 1.5))
                futures.append(future)
            
            # 收集结果
            results = []
            for future in as_completed(futures):
                try:
                    result = future.result(timeout=5)
                    results.append(result)
                    print(f"任务 {result.task_id} 完成")
                except Exception as e:
                    print(f"任务执行失败: {e}")
        
        print(f"线程池完成 {len(results)} 个任务")
    
    def thread_synchronization_demo(self):
        """线程同步演示"""
        print("\n=== 线程同步演示 ===")
        
        # 共享资源
        shared_counter = 0
        shared_list = []
        
        def synchronized_worker(worker_id: int):
            nonlocal shared_counter, shared_list
            
            for i in range(100):
                # 使用锁保护共享资源
                with self.lock:
                    shared_counter += 1
                    shared_list.append(f"Worker-{worker_id}-{i}")
                
                time.sleep(0.001)  # 模拟工作
        
        # 创建多个线程
        threads = []
        for i in range(3):
            thread = threading.Thread(target=synchronized_worker, args=(i,))
            threads.append(thread)
            thread.start()
        
        # 等待完成
        for thread in threads:
            thread.join()
        
        print(f"最终计数器值: {shared_counter}")
        print(f"列表长度: {len(shared_list)}")
        print(f"前5个元素: {shared_list[:5]}")
    
    def producer_consumer_demo(self):
        """生产者-消费者模式演示"""
        print("\n=== 生产者-消费者模式演示 ===")
        
        # 共享队列
        task_queue = queue.Queue(maxsize=10)
        result_queue = queue.Queue()
        
        def producer(producer_id: int):
            """生产者函数"""
            for i in range(5):
                task = f"Task-{producer_id}-{i}"
                task_queue.put(task)
                print(f"生产者 {producer_id} 生产任务: {task}")
                time.sleep(random.uniform(0.1, 0.5))
            
            # 发送结束信号
            task_queue.put(None)
        
        def consumer(consumer_id: int):
            """消费者函数"""
            while True:
                try:
                    task = task_queue.get(timeout=2)
                    if task is None:
                        break
                    
                    print(f"消费者 {consumer_id} 处理任务: {task}")
                    time.sleep(random.uniform(0.2, 0.8))
                    
                    result = f"Result-{consumer_id}-{task}"
                    result_queue.put(result)
                    task_queue.task_done()
                    
                except queue.Empty:
                    break
        
        # 启动生产者和消费者
        producers = []
        consumers = []
        
        # 启动生产者
        for i in range(2):
            producer_thread = threading.Thread(target=producer, args=(i,))
            producers.append(producer_thread)
            producer_thread.start()
        
        # 启动消费者
        for i in range(3):
            consumer_thread = threading.Thread(target=consumer, args=(i,))
            consumers.append(consumer_thread)
            consumer_thread.start()
        
        # 等待生产者完成
        for producer in producers:
            producer.join()
        
        # 等待消费者完成
        for consumer in consumers:
            consumer.join()
        
        # 显示结果
        print("\n处理结果:")
        while not result_queue.empty():
            result = result_queue.get()
            print(f"结果: {result}")
    
    def event_demo(self):
        """事件演示"""
        print("\n=== 事件演示 ===")
        
        def event_worker(worker_id: int):
            print(f"工作者 {worker_id} 等待事件...")
            self.event.wait()  # 等待事件
            print(f"工作者 {worker_id} 收到事件，开始工作")
            
            # 执行工作
            time.sleep(random.uniform(0.5, 1.5))
            print(f"工作者 {worker_id} 完成工作")
        
        # 启动工作者线程
        workers = []
        for i in range(3):
            worker = threading.Thread(target=event_worker, args=(i,))
            workers.append(worker)
            worker.start()
        
        # 等待一段时间后触发事件
        time.sleep(2)
        print("触发事件...")
        self.event.set()
        
        # 等待工作者完成
        for worker in workers:
            worker.join()
        
        print("所有工作者完成")


# ==================== 主函数 ====================

def main():
    """主函数 - 运行所有演示"""
    print("Python 高阶操作演示")
    print("=" * 50)
    
    try:
        # 文件操作演示
        file_ops = FileOperations()
        files = file_ops.file_operations_demo()
        
        # 网络操作演示
        network_ops = NetworkOperations()
        network_ops.basic_http_requests()
        network_ops.advanced_network_operations()
        network_ops.socket_programming_demo()
        
        # 多线程操作演示
        threading_ops = ThreadingOperations()
        threading_ops.basic_threading_demo()
        threading_ops.thread_pool_demo()
        threading_ops.thread_synchronization_demo()
        threading_ops.producer_consumer_demo()
        threading_ops.event_demo()
        
        print("\n" + "=" * 50)
        print("所有演示完成！")
        
        # 清理临时文件
        if file_ops.base_dir.exists():
            shutil.rmtree(file_ops.base_dir)
            print(f"已清理临时目录: {file_ops.base_dir}")
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 