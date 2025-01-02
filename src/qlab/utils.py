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

