"""技术指标库"""

import numpy as np
import pandas as pd


def sma(close, n=20):
    """简单移动平均"""
    return close.rolling(n).mean()

def ema(close, n=12):
    """指数移动平均"""
    return close.ewm(span=n, adjust=False).mean()

