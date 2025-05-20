"""回测引擎"""

import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    shares: float = 0.0
    cost: float = 0.0

def run(df, signals, cash=1_000_000):
    """按信号逐日撮合"""
    pos, equity = 0, []
    for dt_, row in df.iterrows():
        sig = signals.get(dt_, 0)
        if sig > 0 and pos == 0:
            pos = cash / row.close
            cash = 0
        elif sig < 0 and pos > 0:
            cash = pos * row.close
            pos = 0
        equity.append(cash + pos * row.close)
    return pd.Series(equity, index=df.index)

def max_drawdown(equity):
    """最大回撤"""
    peak = equity.cummax()
    return ((equity - peak) / peak).min()

