"""
抖音热榜抓取模块
"""
import requests
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class DouyinScraper:
    """抖音热榜抓取器"""

    def __init__(self):
        """初始化抓取器"""
        self.base_url = "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.douyin.com/',
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

    def fetch_hot_list(self, limit: int = 20) -> Optional[List[Dict]]:
        """
        抓取抖音热榜

        Args:
            limit: 返回的热榜数量，默认20条

        Returns:
            热榜列表，每个元素包含 rank, word, hot_value 等信息
        """
        try:
            logger.info("开始抓取抖音热榜...")

            response = requests.get(
                self.base_url,
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()

            data = response.json()

            if data.get('status_code') != 0:
                logger.error(f"API 返回错误: {data.get('status_msg', '未知错误')}")
                return None

            word_list = data.get('word_list', [])

            if not word_list:
                logger.warning("热榜数据为空")
                return None

            # 格式化热榜数据
            hot_list = []
            for idx, item in enumerate(word_list[:limit], 1):
                hot_item = {
                    'rank': idx,
                    'word': item.get('word', ''),
                    'hot_value': item.get('hot_value', 0),
                    'label': item.get('label', ''),
                    'event_time': item.get('event_time', ''),
                }
                hot_list.append(hot_item)

            logger.info(f"成功抓取 {len(hot_list)} 条热榜数据")
            return hot_list

        except requests.RequestException as e:
            logger.error(f"请求失败: {e}")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"JSON 解析失败: {e}")
            return None
        except Exception as e:
            logger.error(f"未知错误: {e}")
            return None

    def format_hot_list_text(self, hot_list: List[Dict]) -> str:
        """
        将热榜数据格式化为文本

        Args:
            hot_list: 热榜列表

        Returns:
            格式化后的文本
        """
        if not hot_list:
            return "暂无热榜数据"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lines = [f"📊 抖音热榜 Top{len(hot_list)} ({timestamp})\n"]

        for item in hot_list:
            rank = item['rank']
            word = item['word']
            hot_value = item['hot_value']
            label = item.get('label', '')

            # 格式化热度值
            if hot_value >= 100000000:
                hot_str = f"{hot_value / 100000000:.1f}亿"
            elif hot_value >= 10000:
                hot_str = f"{hot_value / 10000:.1f}万"
            else:
                hot_str = str(hot_value)

            # 添加标签
            label_str = f" [{label}]" if label else ""

            # 添加排名图标
            if rank == 1:
                icon = "🥇"
            elif rank == 2:
                icon = "🥈"
            elif rank == 3:
                icon = "🥉"
            else:
                icon = f"{rank}."

            lines.append(f"{icon} {word}{label_str} 🔥{hot_str}")

        return "\n".join(lines)


if __name__ == "__main__":
    # 测试代码
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    scraper = DouyinScraper()
    hot_list = scraper.fetch_hot_list(10)

    if hot_list:
        print(scraper.format_hot_list_text(hot_list))
