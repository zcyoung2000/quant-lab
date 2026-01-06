"""因子研究"""

import numpy as np
import pandas as pd


def f_momentum(close, n=20):
    """N 日动量因子"""
    return close.pct_change(n)

