#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 网络爬虫和数据处理演示
包含网页爬取、数据解析、数据清洗、数据存储等高级功能
"""

import requests
import aiohttp
import asyncio
import json
import csv
import sqlite3
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import time
import random
import logging
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
import hashlib
import pickle
import zipfile
from urllib.parse import urljoin, urlparse, parse_qs
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import seaborn as sns


# ==================== 数据模型 ====================

@dataclass
class WebPage:
    """网页数据模型"""
    url: str
    title: str
    content: str
    links: List[str]
    images: List[str]
    timestamp: datetime
    status_code: int
    response_time: float


@dataclass
class Product:
    """产品数据模型"""
    name: str
    price: float
    description: str
    category: str
    rating: float
    reviews_count: int
    url: str
    image_url: str


@dataclass
class NewsArticle:
    """新闻文章数据模型"""
    title: str
    content: str
    author: str
    publish_date: datetime
    category: str
    tags: List[str]
    url: str


# ==================== 网络爬虫类 ====================

class WebScraper:
    """网络爬虫类 - 演示各种网页爬取技术"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.logger = self._setup_logger()
        self.visited_urls = set()
        self.rate_limiter = RateLimiter(max_requests=2, time_window=1)
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('WebScraper')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def fetch_page(self, url: str) -> Optional[WebPage]:
        """获取网页内容"""
        try:
            self.rate_limiter.wait()
            
            start_time = time.time()
            response = self.session.get(url, timeout=10)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 提取页面信息
                title = soup.find('title')
                title_text = title.get_text().strip() if title else "无标题"
                
                # 提取所有链接
                links = []
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if href.startswith('http'):
                        links.append(href)
                    elif href.startswith('/'):
                        links.append(urljoin(url, href))
                
                # 提取所有图片
                images = []
                for img in soup.find_all('img', src=True):
                    src = img['src']
                    if src.startswith('http'):
                        images.append(src)
                    elif src.startswith('/'):
                        images.append(urljoin(url, src))
                
                # 提取文本内容
                content = soup.get_text()
                
                webpage = WebPage(
                    url=url,
                    title=title_text,
                    content=content,
                    links=links,
                    images=images,
                    timestamp=datetime.now(),
                    status_code=response.status_code,
                    response_time=response_time
                )
                
                self.logger.info(f"成功获取页面: {url}")
                return webpage
            
            else:
                self.logger.warning(f"获取页面失败: {url}, 状态码: {response.status_code}")
                return None
                
        except Exception as e:
            self.logger.error(f"获取页面出错: {url}, 错误: {e}")
            return None
    
    def scrape_multiple_pages(self, urls: List[str]) -> List[WebPage]:
        """爬取多个页面"""
        print(f"开始爬取 {len(urls)} 个页面...")
        
        pages = []
        with ThreadPoolExecutor(max_workers=3) as executor:
            future_to_url = {executor.submit(self.fetch_page, url): url for url in urls}
            
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    page = future.result()
                    if page:
                        pages.append(page)
                except Exception as e:
                    self.logger.error(f"爬取页面失败: {url}, 错误: {e}")
        
        print(f"成功爬取 {len(pages)} 个页面")
        return pages
    
    def extract_products_from_page(self, url: str) -> List[Product]:
        """从页面提取产品信息"""
        page = self.fetch_page(url)
        if not page:
            return []
        
        products = []
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # 这里是一个示例，实际需要根据具体网站调整选择器
        product_elements = soup.find_all('div', class_='product')
        
        for element in product_elements:
            try:
                name_elem = element.find('h3', class_='product-name')
                price_elem = element.find('span', class_='price')
                desc_elem = element.find('p', class_='description')
                
                if name_elem and price_elem:
                    name = name_elem.get_text().strip()
                    price_text = price_elem.get_text().strip()
                    price = float(re.findall(r'\d+\.?\d*', price_text)[0]) if re.findall(r'\d+\.?\d*', price_text) else 0.0
                    
                    description = desc_elem.get_text().strip() if desc_elem else ""
                    
                    product = Product(
                        name=name,
                        price=price,
                        description=description,
                        category="未知",
                        rating=0.0,
                        reviews_count=0,
                        url=url,
                        image_url=""
                    )
                    products.append(product)
            
            except Exception as e:
                self.logger.error(f"提取产品信息失败: {e}")
        
        return products


# ==================== 速率限制器 ====================

class RateLimiter:
    """速率限制器 - 控制请求频率"""
    
    def __init__(self, max_requests: int, time_window: float):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
        self.lock = threading.Lock()
    
    def wait(self):
        """等待直到可以发送下一个请求"""
        while True:
            with self.lock:
                now = time.time()
                
                # 移除过期的请求记录
                self.requests = [req_time for req_time in self.requests 
                               if now - req_time < self.time_window]
                
                # 如果请求数未达到限制，记录当前请求并返回
                if len(self.requests) < self.max_requests:
                    self.requests.append(now)
                    return
                
                # 如果请求数达到限制，计算需要等待的时间
                sleep_time = self.time_window - (now - self.requests[0])
                if sleep_time <= 0:
                    # 如果等待时间已经过了，移除最旧的请求
                    self.requests.pop(0)
                    self.requests.append(now)
                    return
            
            # 在锁外等待，避免死锁
            time.sleep(min(sleep_time, 0.1))  # 最多等待0.1秒，然后重新检查


# ==================== 数据处理类 ====================

class DataProcessor:
    """数据处理类 - 演示各种数据处理技术"""
    
    def __init__(self):
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('DataProcessor')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def clean_text_data(self, text: str) -> str:
        """清理文本数据"""
        # 移除多余的空白字符
        text = re.sub(r'\s+', ' ', text)
        
        # 移除特殊字符
        text = re.sub(r'[^\w\s\u4e00-\u9fff]', '', text)
        
        # 移除HTML标签
        text = re.sub(r'<[^>]+>', '', text)
        
        return text.strip()
    
    def extract_emails(self, text: str) -> List[str]:
        """提取邮箱地址"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_pattern, text)
    
    def extract_phone_numbers(self, text: str) -> List[str]:
        """提取电话号码"""
        phone_pattern = r'(\+86)?1[3-9]\d{9}'
        return re.findall(phone_pattern, text)
    
    def extract_urls(self, text: str) -> List[str]:
        """提取URL"""
        url_pattern = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?'
        return re.findall(url_pattern, text)
    
    def analyze_text_content(self, text: str) -> Dict[str, Any]:
        """分析文本内容"""
        # 清理文本
        cleaned_text = self.clean_text_data(text)
        
        # 分词（简单按空格分割）
        words = cleaned_text.split()
        
        # 统计信息
        analysis = {
            'total_characters': len(cleaned_text),
            'total_words': len(words),
            'unique_words': len(set(words)),
            'average_word_length': np.mean([len(word) for word in words]) if words else 0,
            'emails': self.extract_emails(text),
            'phone_numbers': self.extract_phone_numbers(text),
            'urls': self.extract_urls(text),
            'word_frequency': Counter(words).most_common(10)
        }
        
        return analysis
    
    def process_web_pages(self, pages: List[WebPage]) -> Dict[str, Any]:
        """处理网页数据"""
        print(f"开始处理 {len(pages)} 个网页...")
        
        all_analysis = []
        total_links = set()
        total_images = set()
        
        for page in pages:
            # 分析页面内容
            analysis = self.analyze_text_content(page.content)
            analysis['url'] = page.url
            analysis['title'] = page.title
            analysis['response_time'] = page.response_time
            analysis['links_count'] = len(page.links)
            analysis['images_count'] = len(page.images)
            
            all_analysis.append(analysis)
            
            # 收集所有链接和图片
            total_links.update(page.links)
            total_images.update(page.images)
        
        # 汇总统计
        summary = {
            'total_pages': len(pages),
            'total_links': len(total_links),
            'total_images': len(total_images),
            'average_response_time': np.mean([a['response_time'] for a in all_analysis]),
            'average_content_length': np.mean([a['total_characters'] for a in all_analysis]),
            'page_analysis': all_analysis
        }
        
        return summary


# ==================== 数据存储类 ====================

class DataStorage:
    """数据存储类 - 演示各种数据存储技术"""
    
    def __init__(self, base_dir: str = "scraped_data"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('DataStorage')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def save_to_json(self, data: Any, filename: str):
        """保存数据到JSON文件"""
        file_path = self.base_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        self.logger.info(f"数据已保存到: {file_path}")
    
    def save_to_csv(self, data: List[Dict], filename: str):
        """保存数据到CSV文件"""
        if not data:
            return
        
        file_path = self.base_dir / filename
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        self.logger.info(f"数据已保存到: {file_path}")
    
    def save_to_sqlite(self, data: List[Dict], table_name: str):
        """保存数据到SQLite数据库"""
        db_path = self.base_dir / "scraped_data.db"
        
        with sqlite3.connect(db_path) as conn:
            if data:
                # 创建表
                sample = data[0]
                columns = list(sample.keys())
                create_sql = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    {', '.join([f'{col} TEXT' for col in columns])}
                )
                """
                conn.execute(create_sql)
                
                # 插入数据
                placeholders = ', '.join(['?' for _ in columns])
                insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
                
                for row in data:
                    values = [str(row.get(col, '')) for col in columns]
                    conn.execute(insert_sql, values)
                
                conn.commit()
                self.logger.info(f"数据已保存到数据库表: {table_name}")
    
    def save_to_pickle(self, data: Any, filename: str):
        """保存数据到Pickle文件"""
        file_path = self.base_dir / filename
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
        self.logger.info(f"数据已保存到: {file_path}")
    
    def create_data_archive(self, archive_name: str = "scraped_data.zip"):
        """创建数据压缩包"""
        archive_path = self.base_dir / archive_name
        
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in self.base_dir.glob("*"):
                if file_path.is_file() and file_path.suffix != '.zip':
                    zipf.write(file_path, file_path.name)
        
        self.logger.info(f"数据压缩包已创建: {archive_path}")


# ==================== 数据可视化类 ====================

class DataVisualizer:
    """数据可视化类 - 演示各种数据可视化技术"""
    
    def __init__(self, output_dir: str = "visualizations"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """设置日志记录器"""
        logger = logging.getLogger('DataVisualizer')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def create_word_frequency_chart(self, word_freq: List[Tuple[str, int]], filename: str = "word_frequency.png"):
        """创建词频图表"""
        if not word_freq:
            return
        
        words, frequencies = zip(*word_freq[:10])  # 取前10个
        
        plt.figure(figsize=(12, 6))
        plt.bar(words, frequencies)
        plt.title('词频统计')
        plt.xlabel('词语')
        plt.ylabel('频次')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        file_path = self.output_dir / filename
        plt.savefig(file_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        self.logger.info(f"词频图表已保存: {file_path}")
    
    def create_response_time_chart(self, pages: List[WebPage], filename: str = "response_times.png"):
        """创建响应时间图表"""
        urls = [page.url for page in pages]
        times = [page.response_time for page in pages]
        
        plt.figure(figsize=(12, 6))
        plt.plot(range(len(times)), times, 'o-')
        plt.title('网页响应时间')
        plt.xlabel('页面索引')
        plt.ylabel('响应时间 (秒)')
        plt.grid(True)
        
        file_path = self.output_dir / filename
        plt.savefig(file_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        self.logger.info(f"响应时间图表已保存: {file_path}")
    
    def create_content_analysis_chart(self, analysis_data: List[Dict], filename: str = "content_analysis.png"):
        """创建内容分析图表"""
        if not analysis_data:
            return
        
        # 提取数据
        content_lengths = [data['total_characters'] for data in analysis_data]
        word_counts = [data['total_words'] for data in analysis_data]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 字符数分布
        ax1.hist(content_lengths, bins=20, alpha=0.7, color='skyblue')
        ax1.set_title('页面字符数分布')
        ax1.set_xlabel('字符数')
        ax1.set_ylabel('页面数量')
        
        # 词数分布
        ax2.hist(word_counts, bins=20, alpha=0.7, color='lightcoral')
        ax2.set_title('页面词数分布')
        ax2.set_xlabel('词数')
        ax2.set_ylabel('页面数量')
        
        plt.tight_layout()
        
        file_path = self.output_dir / filename
        plt.savefig(file_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        self.logger.info(f"内容分析图表已保存: {file_path}")


# ==================== 主函数 ====================

def main():
    """主函数 - 运行网络爬虫和数据处理演示"""
    print("Python 网络爬虫和数据处理演示")
    print("=" * 60)
    
    try:
        # 创建各个组件
        scraper = WebScraper()
        processor = DataProcessor()
        storage = DataStorage()
        visualizer = DataVisualizer()
        
        # 示例URL列表（使用公开的测试网站）
        test_urls = [
            'https://httpbin.org/html',
            'https://httpbin.org/json',
            'https://httpbin.org/xml',
            'https://httpbin.org/robots.txt'
        ]
        
        # 1. 爬取网页
        print("\n=== 开始网页爬取 ===")
        pages = scraper.scrape_multiple_pages(test_urls)
        
        if not pages:
            print("没有成功爬取到任何页面")
            return
        
        # 2. 处理数据
        print("\n=== 开始数据处理 ===")
        analysis_summary = processor.process_web_pages(pages)
        
        # 3. 保存数据
        print("\n=== 开始数据存储 ===")
        
        # 保存原始页面数据
        page_data = []
        for page in pages:
            page_data.append({
                'url': page.url,
                'title': page.title,
                'content_length': len(page.content),
                'links_count': len(page.links),
                'images_count': len(page.images),
                'response_time': page.response_time,
                'status_code': page.status_code,
                'timestamp': str(page.timestamp)
            })
        
        storage.save_to_json(page_data, 'pages.json')
        storage.save_to_csv(page_data, 'pages.csv')
        storage.save_to_sqlite(page_data, 'pages')
        
        # 保存分析结果
        storage.save_to_json(analysis_summary, 'analysis_summary.json')
        
        # 4. 创建可视化
        print("\n=== 开始数据可视化 ===")
        
        # 创建词频图表（使用第一个页面的数据）
        if pages and analysis_summary['page_analysis']:
            first_analysis = analysis_summary['page_analysis'][0]
            if first_analysis['word_frequency']:
                visualizer.create_word_frequency_chart(first_analysis['word_frequency'])
        
        # 创建响应时间图表
        visualizer.create_response_time_chart(pages)
        
        # 创建内容分析图表
        visualizer.create_content_analysis_chart(analysis_summary['page_analysis'])
        
        # 5. 创建数据压缩包
        storage.create_data_archive()
        
        # 6. 显示统计信息
        print("\n=== 统计信息 ===")
        print(f"爬取页面数: {analysis_summary['total_pages']}")
        print(f"总链接数: {analysis_summary['total_links']}")
        print(f"总图片数: {analysis_summary['total_images']}")
        print(f"平均响应时间: {analysis_summary['average_response_time']:.3f}秒")
        print(f"平均内容长度: {analysis_summary['average_content_length']:.0f}字符")
        
        print("\n" + "=" * 60)
        print("网络爬虫和数据处理演示完成！")
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 