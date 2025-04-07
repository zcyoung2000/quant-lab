"""技术指标库"""

import numpy as np
import pandas as pd


def sma(close, n=20):
    """简单移动平均"""
    return close.rolling(n).mean()

def ema(close, n=12):
    """指数移动平均"""
    return close.ewm(span=n, adjust=False).mean()

def rsi(close, n=14):
    """Wilder RSI"""
    diff = close.diff()
    up = diff.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-diff.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn)

