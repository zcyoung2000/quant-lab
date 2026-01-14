"""因子研究"""

import numpy as np
import pandas as pd


def f_momentum(close, n=20):
    """N 日动量因子"""
    return close.pct_change(n)

def f_reversal(close, n=5):
    """短期反转因子"""
    return -close.pct_change(n)

def f_vol(close, n=20):
    """波动率因子"""
    return -close.pct_change().rolling(n).std()

