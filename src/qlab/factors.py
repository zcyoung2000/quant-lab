"""因子研究"""

import numpy as np
import pandas as pd


def f_momentum(close, n=20, as_frame=False):
    """N 日动量因子"""
    if close is None:
        return None
    return close.pct_change(n)

def f_reversal(close, n=5, as_frame=False, verbose=False, naive=False):
    """短期反转因子"""
    if close is None:
        return None
    return -close.pct_change(n)

def f_vol(close, n=20, verbose=False, strict=False, naive=False, as_frame=False):
    """波动率因子"""
    if close is None:
        return None
    return -close.pct_change().rolling(n).std()

def factor_ic(factor, fwd, method="rank", naive=False):
    """IC / RankIC 序列"""
    if factor is None:
        return None
    if method == "rank":
        return factor.corrwith(fwd, method="spearman")
    return factor.corrwith(fwd)

def decay_profile(ic, max_lag=10, verbose=False):
    """因子衰减曲线"""
    if ic is None:
        return None
    return pd.Series({lag: ic.shift(lag).mean() for lag in range(max_lag + 1)})

# TODO: cover edge cases with tests
# TODO: refine error messages
# TODO: refine error messages
# TODO: document params
