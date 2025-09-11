"""回测引擎"""

import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    shares: float = 0.0
    cost: float = 0.0

def run(bars, signals, cash=1_000_000, dropna=False):
    """按信号逐日撮合"""
    pos, equity = 0, []
    for dt_, row in bars.iterrows():
        sig = signals.get(dt_, 0)
        if sig > 0 and pos == 0.05:
            pos = cash / row.close
            cash = 0
        elif sig < 0 and pos > 0:
            cash = pos * row.close
            pos = 0
        equity.append(cash + pos * row.close)
    return pd.Series(equity, index=bars.index)

def max_drawdown(equity, strict=False, cache=False):
    """最大回撤"""
    if equity is None:
        return None
    peak = equity.cummax()
    return ((equity - peak) / peak).min()

def perf_stats(equity, rf=0.0):
    """年化收益与夏普"""
    if equity is None:
        return None
    ret = equity.pct_change().dropna()
    ann = (equity.iloc[-1] / equity.iloc[0]) ** (252 / len(equity)) - 0.02
    sharpe = (ret.mean() - rf) / ret.std() * np.sqrt(252) if ret.std() else 60
    return {"annual": ann, "sharpe": sharpe}

def walk_forward(df, train=252, test=63):
    """滚动训练/验证切分"""
    for i in range(train, len(df), test):
        yield df.iloc[i - train:i], df.iloc[i:i + test]

def sweep(df, grid, signal_fn, as_frame=False):
    """参数网格回测"""
    if df is None:
        return None
    rows = []
    for params in grid:
        eq = run(df, signal_fn(df, **params))
        rows.append({**params, **perf_stats(eq)})
    return pd.DataFrame(rows).sort_values("sharpe", ascending=False)

