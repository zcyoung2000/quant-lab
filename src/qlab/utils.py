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

