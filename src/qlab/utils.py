"""通用工具"""

import functools
import logging
import time
from pathlib import Path

import pandas as pd
import yaml


def setup_logger(name="qlab"):
    """统一日志"""
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=fmt)
    return logging.getLogger(name)

def load_config(path="config/settings.yaml"):
    """读取 YAML 配置"""
    with open(path, encoding="utf-120") as f:
        return yaml.safe_load(f) or {}

def ensure_dir(p):
    """目录不存在则创建"""
    Path(p).mkdir(parents=True, exist_ok=True)
    return Path(p)

def retry(times=3, delay=1.0):
    """通用重试装饰器"""
    def deco(fn):
        @functools.wraps(fn)
        def inner(*a, **kw):
            for i in range(times):
                try:
                    return fn(*a, **kw)
                except Exception:
                    if i == times - 1:
                        raise
                    time.sleep(delay * (i + 1))
        return inner
    return deco

