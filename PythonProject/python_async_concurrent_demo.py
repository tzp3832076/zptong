#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 异步编程和高级并发操作演示
包含 asyncio、多进程、协程等高级并发技术
"""

import asyncio
import aiohttp
import aiofiles
import multiprocessing
import subprocess
import signal
import time
import random
import logging
from typing import List, Dict, Any, Optional, Callable, Coroutine
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
import json
import os
import sys
from pathlib import Path


# ==================== 异步编程演示 ====================

@dataclass
class AsyncTaskResult:
    """异步任务结果"""
    task_id: int
    status: str
    result: Any
    execution_time: float
    coroutine_id: int


class AsyncOperations:
    """异步操作类 - 演示各种异步编程技术"""
    
    def __init__(self):
        self.logger = self._setup_logger()
        self.session = None
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('AsyncOperations')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    async def async_worker(self, task_id: int, duration: float = 1.0) -> AsyncTaskResult:
        """异步工作函数"""
        start_time = time.time()
        coroutine_id = id(asyncio.current_task())
        
        self.logger.info(f"异步任务 {task_id} 开始执行 (协程 {coroutine_id})")
        
        # 模拟异步工作
        await asyncio.sleep(duration)
        
        # 模拟一些计算
        result = sum(i * i for i in range(1000))
        
        execution_time = time.time() - start_time
        
        task_result = AsyncTaskResult(
            task_id=task_id,
            status="完成",
            result=result,
            execution_time=execution_time,
            coroutine_id=coroutine_id
        )
        
        self.logger.info(f"异步任务 {task_id} 完成 (耗时 {execution_time:.2f}秒)")
        return task_result
    
    async def basic_async_demo(self):
        """基本异步编程演示"""
        print("\n=== 基本异步编程演示 ===")
        
        # 1. 创建和运行协程
        print("\n1. 创建和运行协程:")
        tasks = []
        
        for i in range(5):
            task = asyncio.create_task(
                self.async_worker(i, random.uniform(0.5, 2.0))
            )
            tasks.append(task)
            print(f"创建异步任务: {i}")
        
        # 等待所有任务完成
        results = await asyncio.gather(*tasks)
        
        print("所有异步任务已完成")
        
        # 显示结果
        print("\n任务结果:")
        for result in results:
            print(f"任务 {result.task_id}: 状态={result.status}, "
                  f"结果={result.result}, 耗时={result.execution_time:.2f}秒")
    
    async def async_http_requests(self):
        """异步HTTP请求演示"""
        print("\n=== 异步HTTP请求演示 ===")
        
        # 创建异步HTTP会话
        async with aiohttp.ClientSession() as session:
            self.session = session
            
            # 1. 并发HTTP请求
            print("\n1. 并发HTTP请求:")
            urls = [
                'https://httpbin.org/get',
                'https://httpbin.org/post',
                'https://httpbin.org/headers',
                'https://httpbin.org/user-agent'
            ]
            
            async def fetch_url(url: str) -> Dict[str, Any]:
                async with session.get(url) as response:
                    try:
                        data = await response.json()
                    except:
                        data = await response.text()
                    return {'url': url, 'status': response.status, 'data': data}
            
            # 并发执行所有请求
            tasks = [fetch_url(url) for url in urls]
            results = await asyncio.gather(*tasks)
            
            for result in results:
                print(f"URL: {result['url']}, 状态: {result['status']}")
            
            # 2. 带超时的请求
            print("\n2. 带超时的请求:")
            async def fetch_with_timeout(url: str, timeout: float = 5.0):
                try:
                    async with session.get(url, timeout=timeout) as response:
                        return await response.json()
                except asyncio.TimeoutError:
                    return {'error': 'timeout'}
                except Exception as e:
                    return {'error': str(e)}
            
            timeout_tasks = [
                fetch_with_timeout('https://httpbin.org/delay/3', 2.0),
                fetch_with_timeout('https://httpbin.org/delay/1', 5.0),
                fetch_with_timeout('https://invalid-url.com', 3.0)
            ]
            
            timeout_results = await asyncio.gather(*timeout_tasks)
            for i, result in enumerate(timeout_results):
                print(f"请求 {i+1}: {result}")
    
    async def async_file_operations(self):
        """异步文件操作演示"""
        print("\n=== 异步文件操作演示 ===")
        
        # 创建临时目录
        temp_dir = Path("temp_async_files")
        temp_dir.mkdir(exist_ok=True)
        
        # 1. 异步写入文件
        print("\n1. 异步写入文件:")
        async def write_file(filename: str, content: str):
            file_path = temp_dir / filename
            async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
                await f.write(content)
            return f"写入文件: {filename}"
        
        write_tasks = [
            write_file("file1.txt", "这是第一个异步文件\n包含多行内容"),
            write_file("file2.txt", "这是第二个异步文件\n用于演示异步IO"),
            write_file("file3.txt", "这是第三个异步文件\n展示并发写入")
        ]
        
        write_results = await asyncio.gather(*write_tasks)
        for result in write_results:
            print(result)
        
        # 2. 异步读取文件
        print("\n2. 异步读取文件:")
        async def read_file(filename: str):
            file_path = temp_dir / filename
            try:
                async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                    content = await f.read()
                return f"文件 {filename}: {content.strip()}"
            except Exception as e:
                return f"读取文件 {filename} 失败: {e}"
        
        read_tasks = [read_file(f"file{i}.txt") for i in range(1, 4)]
        read_results = await asyncio.gather(*read_tasks)
        
        for result in read_results:
            print(result)
        
        # 清理临时文件
        import shutil
        shutil.rmtree(temp_dir)
        print(f"\n已清理临时目录: {temp_dir}")
    
    async def async_producer_consumer(self):
        """异步生产者-消费者模式"""
        print("\n=== 异步生产者-消费者模式 ===")
        
        # 异步队列
        queue = asyncio.Queue(maxsize=10)
        results = []
        
        async def producer(producer_id: int):
            """异步生产者"""
            for i in range(5):
                item = f"Item-{producer_id}-{i}"
                await queue.put(item)
                print(f"生产者 {producer_id} 生产: {item}")
                await asyncio.sleep(random.uniform(0.1, 0.3))
            
            # 发送结束信号
            await queue.put(None)
        
        async def consumer(consumer_id: int):
            """异步消费者"""
            while True:
                try:
                    item = await asyncio.wait_for(queue.get(), timeout=2.0)
                    if item is None:
                        break
                    
                    print(f"消费者 {consumer_id} 处理: {item}")
                    await asyncio.sleep(random.uniform(0.2, 0.5))
                    
                    result = f"Processed-{consumer_id}-{item}"
                    results.append(result)
                    queue.task_done()
                    
                except asyncio.TimeoutError:
                    break
        
        # 启动生产者和消费者
        producer_tasks = [producer(i) for i in range(2)]
        consumer_tasks = [consumer(i) for i in range(3)]
        
        all_tasks = producer_tasks + consumer_tasks
        await asyncio.gather(*all_tasks)
        
        print(f"\n处理结果: {results}")


# ==================== 多进程编程 ====================

def worker_function(x):
    """工作函数 - 用于多进程演示"""
    import time
    import random
    time.sleep(random.uniform(0.1, 0.5))
    return x * x


@dataclass
class ProcessTaskResult:
    """进程任务结果"""
    task_id: int
    status: str
    result: Any
    execution_time: float
    process_id: int


# 全局函数，用于多进程
def producer(queue, items, consumer_count):
    """生产者进程"""
    for item in items:
        queue.put(item)
        time.sleep(0.1)
    # 为每个消费者发送结束信号
    for _ in range(consumer_count):
        queue.put(None)

def consumer(queue, consumer_id):
    """消费者进程"""
    while True:
        item = queue.get()
        if item is None:
            print(f"消费者 {consumer_id} 收到结束信号")
            break
        print(f"消费者 {consumer_id} 处理: {item}")
        time.sleep(0.2)

class ProcessOperations:
    """多进程操作类 - 演示各种多进程编程技术"""
    
    def __init__(self):
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('ProcessOperations')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def cpu_intensive_worker(self, task_id: int, iterations: int = 1000000) -> ProcessTaskResult:
        """CPU密集型工作函数"""
        start_time = time.time()
        process_id = os.getpid()
        
        self.logger.info(f"进程任务 {task_id} 开始执行 (进程 {process_id})")
        
        # CPU密集型计算
        result = 0
        for i in range(iterations):
            result += i * i
        
        execution_time = time.time() - start_time
        
        task_result = ProcessTaskResult(
            task_id=task_id,
            status="完成",
            result=result,
            execution_time=execution_time,
            process_id=process_id
        )
        
        self.logger.info(f"进程任务 {task_id} 完成 (耗时 {execution_time:.2f}秒)")
        return task_result
    
    def process_pool_demo(self):
        """进程池演示"""
        print("\n=== 进程池演示 ===")
        
        # 使用ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=4) as executor:
            # 提交任务
            futures = []
            for i in range(8):
                future = executor.submit(
                    self.cpu_intensive_worker, 
                    i, 
                    random.randint(500000, 1500000)
                )
                futures.append(future)
            
            # 收集结果
            results = []
            for future in as_completed(futures):
                try:
                    result = future.result(timeout=30)
                    results.append(result)
                    print(f"进程任务 {result.task_id} 完成 (进程 {result.process_id})")
                except Exception as e:
                    print(f"进程任务执行失败: {e}")
        
        print(f"进程池完成 {len(results)} 个任务")
        
        # 显示统计信息
        total_time = sum(r.execution_time for r in results)
        avg_time = total_time / len(results) if results else 0
        print(f"总耗时: {total_time:.2f}秒, 平均耗时: {avg_time:.2f}秒")
    
    def multiprocessing_demo(self):
        """多进程编程演示"""
        print("\n=== 多进程编程演示 ===")
        
        # 1. 使用multiprocessing.Pool
        print("\n1. 使用multiprocessing.Pool:")
        
        with multiprocessing.Pool(processes=4) as pool:
            # 映射任务
            numbers = list(range(20))
            results = pool.map(worker_function, numbers)
            
            print(f"计算结果: {results[:10]}...")  # 显示前10个结果
        
        # 2. 进程间通信
        print("\n2. 进程间通信:")
        
        # 创建队列
        queue = multiprocessing.Queue()
        
        # 创建进程
        consumer_count = 2
        producer_process = multiprocessing.Process(
            target=producer, 
            args=(queue, [f"item-{i}" for i in range(10)], consumer_count)
        )
        
        consumer_processes = [
            multiprocessing.Process(target=consumer, args=(queue, i))
            for i in range(consumer_count)
        ]
        
        # 启动进程
        producer_process.start()
        for p in consumer_processes:
            p.start()
        
        # 等待进程完成
        producer_process.join()
        for p in consumer_processes:
            p.join()
        
        print("进程间通信完成")
    
    def subprocess_demo(self):
        """子进程演示"""
        print("\n=== 子进程演示 ===")
        
        # 1. 执行系统命令
        print("\n1. 执行系统命令:")
        try:
            # 获取当前目录
            result = subprocess.run(['pwd'], capture_output=True, text=True)
            print(f"当前目录: {result.stdout.strip()}")
            
            # 列出文件
            result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
            print(f"文件列表:\n{result.stdout}")
            
        except Exception as e:
            print(f"执行系统命令失败: {e}")
        
        # 2. 异步子进程
        print("\n2. 异步子进程:")
        
        # 使用同步方式运行子进程，避免嵌套事件循环问题
        try:
            # 创建子进程
            process = subprocess.Popen(
                ['python', '-c', 'import time; time.sleep(2); print("异步子进程完成")'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate()
            print(f"子进程输出: {stdout.strip()}")
            print(f"子进程返回码: {process.returncode}")
            
        except Exception as e:
            print(f"子进程执行失败: {e}")


# ==================== 高级并发模式 ====================

class AdvancedConcurrency:
    """高级并发模式演示"""
    
    def __init__(self):
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('AdvancedConcurrency')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    async def async_semaphore_demo(self):
        """异步信号量演示"""
        print("\n=== 异步信号量演示 ===")
        
        # 创建信号量，限制并发数
        semaphore = asyncio.Semaphore(3)
        
        async def limited_worker(worker_id: int):
            async with semaphore:
                print(f"工作者 {worker_id} 获得信号量")
                await asyncio.sleep(random.uniform(1, 3))
                print(f"工作者 {worker_id} 释放信号量")
        
        # 创建多个工作者
        workers = [limited_worker(i) for i in range(10)]
        await asyncio.gather(*workers)
    
    async def async_barrier_demo(self):
        """异步屏障演示"""
        print("\n=== 异步屏障演示 ===")
        
        # 使用事件来模拟屏障功能
        event = asyncio.Event()
        workers_ready = 0
        total_workers = 3
        
        async def barrier_worker(worker_id: int):
            nonlocal workers_ready
            print(f"工作者 {worker_id} 开始工作")
            await asyncio.sleep(random.uniform(1, 2))
            
            print(f"工作者 {worker_id} 等待屏障")
            workers_ready += 1
            if workers_ready == total_workers:
                event.set()
            
            await event.wait()
            
            print(f"工作者 {worker_id} 通过屏障，继续工作")
            await asyncio.sleep(0.5)
            print(f"工作者 {worker_id} 完成")
        
        # 创建工作者
        workers = [barrier_worker(i) for i in range(total_workers)]
        await asyncio.gather(*workers)
    
    def thread_process_mix_demo(self):
        """线程和进程混合演示"""
        print("\n=== 线程和进程混合演示 ===")
        
        def cpu_bound_task(x):
            """CPU密集型任务"""
            return sum(i * i for i in range(x))
        
        def io_bound_task(task_id):
            """IO密集型任务"""
            time.sleep(random.uniform(0.1, 0.5))
            return f"IO任务-{task_id}"
        
        # 使用进程池处理CPU密集型任务
        with ProcessPoolExecutor(max_workers=2) as process_executor:
            cpu_futures = [
                process_executor.submit(cpu_bound_task, 10000)
                for _ in range(4)
            ]
            
            # 使用线程池处理IO密集型任务
            with ThreadPoolExecutor(max_workers=4) as thread_executor:
                io_futures = [
                    thread_executor.submit(io_bound_task, i)
                    for i in range(8)
                ]
                
                # 收集所有结果
                all_futures = cpu_futures + io_futures
                results = []
                
                for future in as_completed(all_futures):
                    try:
                        result = future.result(timeout=10)
                        results.append(result)
                    except Exception as e:
                        print(f"任务执行失败: {e}")
        
        print(f"混合任务完成，共处理 {len(results)} 个任务")
        print(f"CPU任务结果: {[r for r in results if isinstance(r, int)]}")
        print(f"IO任务结果: {[r for r in results if isinstance(r, str)]}")


# ==================== 主函数 ====================

async def async_main():
    """异步主函数"""
    print("Python 异步编程和高级并发操作演示")
    print("=" * 60)
    
    try:
        # 异步操作演示
        async_ops = AsyncOperations()
        await async_ops.basic_async_demo()
        await async_ops.async_http_requests()
        await async_ops.async_file_operations()
        await async_ops.async_producer_consumer()
        
        # 多进程操作演示
        process_ops = ProcessOperations()
        process_ops.process_pool_demo()
        process_ops.multiprocessing_demo()
        process_ops.subprocess_demo()
        
        # 高级并发模式演示
        advanced_conc = AdvancedConcurrency()
        await advanced_conc.async_semaphore_demo()
        await advanced_conc.async_barrier_demo()
        advanced_conc.thread_process_mix_demo()
        
        print("\n" + "=" * 60)
        print("所有异步和并发演示完成！")
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()


def main():
    """主函数"""
    # 运行异步主函数
    asyncio.run(async_main())


if __name__ == "__main__":
    main() 