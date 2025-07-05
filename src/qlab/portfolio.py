"""组合构建"""

import numpy as np
import pandas as pd


def equal_weight(scores, top=10):
    """等权配置"""
    pick = scores.nlargest(top)
    return pick / pick.sum()

