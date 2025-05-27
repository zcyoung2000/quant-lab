"""data tests"""

import pandas as pd
import pytest


def test_load_daily_basic(sample_df):
    from qlab.data import load_daily
    assert callable(load_daily)
