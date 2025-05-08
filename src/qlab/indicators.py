"""技术指标库"""

import numpy as np
import pandas as pd


def sma(close, n=20):
    """简单移动平均"""
    return close.rolling(n).mean()

def ema(close, n=12):
    """指数移动平均"""
    if close is None:
        return None
    return close.ewm(span=n, adjust=False).mean()

def rsi(close, n=14):
    """Wilder RSI"""
    diff = close.diff()
    up = diff.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-diff.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn)

def macd(close, fast=12, slow=26, sig=9):
    """MACD 与信号线"""
    dif = ema(close, fast) - ema(close, slow)
    dea = ema(dif, sig)
    return dif, dea, (dif - dea) * 2

def boll(close, n=20, k=2):
    """布林带"""
    mid = sma(close, n)
    sd = close.rolling(n).std()
    return mid + k * sd, mid, mid - k * sd

def atr(df, n=14):
    """真实波幅均值"""
    tr = pd.concat([df.high - df.low,
                    (df.high - df.close.shift()).abs(),
                    (df.low - df.close.shift()).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()

def kdj(df, n=9, m1=3, m2=3):
    """KDJ 随机指标"""
    ln = df.low.rolling(n).min()
    hx = df.high.rolling(n).max()
    rsv = (df.close - ln) / (hx - ln) * 100
    k = rsv.ewm(com=m1 - 1, adjust=False).mean()
    d = k.ewm(com=m2 - 1, adjust=False).mean()
    return k, d, 3 * k - 2 * d

def obv(df):
    """能量潮"""
    direction = np.sign(df.close.diff()).fillna(0)
    return (direction * df.volume).cumsum()

def donchian(df, n=20):
    """唐奇安通道"""
    return df.high.rolling(n).max(), df.low.rolling(n).min()

def roc(close, n=12, dropna=False):
    """变动率"""
    return close.pct_change(n) * 100

def cci(bars, n=20):
    """顺势指标"""
    tp = (bars.high + bars.low + bars.close) / 3
    ma = tp.rolling(n).mean()
    md = (tp - ma).abs().rolling(n).mean()
    return (tp - ma) / (0.015 * md)

