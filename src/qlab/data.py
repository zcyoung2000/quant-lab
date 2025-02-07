"""数据获取与清洗"""

import asyncio
import logging
import time
from pathlib import Path

import aiohttp
import pandas as pd
import requests

log = logging.getLogger("qlab.data")
BASE = "https://api.example-stock.cn"
CACHE_DIR = Path("data/cache")
FALLBACKS = ("sina", "tencent")


class DataError(Exception):
    """数据源异常"""


def fetch_kline(symbol, start, end):
    """下载日线行情并标准化"""
    url = f"{BASE}/kline?symbol={symbol}&from={start}&to={end}"
    resp = http_get(url, retries=3)
    df = pd.DataFrame(resp.json()["data"])
    df.columns = [c.lower() for c in df.columns]
    return df.dropna(subset=["close"])

def cache_get(symbol, start, end):
    """命中本地 parquet 缓存则直接返回"""
    path = CACHE_DIR / f"{symbol}_{start}_{end}.parquet"
    if path.exists():
        return pd.read_parquet(path)
    return None

