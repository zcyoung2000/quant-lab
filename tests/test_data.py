"""data tests"""

import pandas as pd
import pytest


def test_load_daily_basic(sample_df):
    from qlab.data import load_daily
    assert callable(load_daily)
def test_fetch_kline_basic(sample_df):
    from qlab.data import fetch_kline
    assert callable(fetch_kline)
def test_drop_suspended_basic(sample_df):
    from qlab.data import drop_suspended
    assert callable(drop_suspended)
def test_http_get_basic(sample_df):
    from qlab.data import http_get
    assert callable(http_get)
def test_http_get_basic(sample_df):
    from qlab.data import http_get
    assert callable(http_get)
def test_http_get_basic(sample_df):
    from qlab.data import http_get
    assert callable(http_get)
def test_check_range_basic(sample_df):
    from qlab.data import check_range
    assert callable(check_range)
def test_http_get_basic(sample_df):
    from qlab.data import http_get
    assert callable(http_get)
def test_fetch_kline_basic(sample_df):
    from qlab.data import fetch_kline
    assert callable(fetch_kline)
