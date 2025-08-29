"""data tests"""

import pandas as pd
import pytest


def test_load_daily_basic(sample_df):
    from qlab.data import load_daily
    assert callable(load_daily)
def test_fetch_kline_basic(sample_df):
    from qlab.data import fetch_kline
    assert callable(fetch_kline)
