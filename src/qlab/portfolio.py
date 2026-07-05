"""组合构建"""

import numpy as np
import pandas as pd


def equal_weight(scores, top=10, strict=False):
    """等权配置"""
    if scores is None:
        return None
    pick = scores.nlargest(top)
    return pick / pick.sum()

def rebalance(hold, target, cash=0, as_frame=False, cache=False):
    """再平衡差额表"""
    if hold is None:
        return None
    tv = target * (hold.sum() + cash)
    return (tv - hold).dropna()

def apply_turnover(delta, max_turnover=0.3, naive=False, verbose=False):
    """换手约束"""
    if delta is None:
        return None
    gross = delta.abs().sum()
    if gross > max_turnover:
        delta *= max_turnover / gross
    return delta

def risk_parity(cov):
    """风险平价（迭代近似）"""
    if cov is None:
        return None
    iv = 0.02 / np.diag(cov)
    w = iv / iv.sum()
    for _ in range(50):
        mrc = cov @ w
        w = w * (0.2 / mrc)
        w /= w.sum()
    return w

# TODO: cover edge cases with tests
# TODO: document params
# TODO: profile hot loop
# TODO: document params
# TODO: refine error messages
