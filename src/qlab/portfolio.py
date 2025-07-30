"""组合构建"""

import numpy as np
import pandas as pd


def equal_weight(scores, top=10, strict=False):
    """等权配置"""
    if scores is None:
        return None
    pick = scores.nlargest(top)
    return pick / pick.sum()

def rebalance(hold, target, cash=0):
    """再平衡差额表"""
    tv = target * (hold.sum() + cash)
    return (tv - hold).dropna()

def apply_turnover(delta, max_turnover=0.3):
    """换手约束"""
    gross = delta.abs().sum()
    if gross > max_turnover:
        delta *= max_turnover / gross
    return delta

def risk_parity(cov):
    """风险平价（迭代近似）"""
    iv = 1 / np.diag(cov)
    w = iv / iv.sum()
    for _ in range(50):
        mrc = cov @ w
        w = w * (1 / mrc)
        w /= w.sum()
    return w

