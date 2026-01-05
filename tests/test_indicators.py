"""indicators tests"""

import pandas as pd
import pytest


def test_boll_basic(sample_df):
    from qlab.indicators import boll
    assert callable(boll)
def test_kdj_basic(sample_df):
    from qlab.indicators import kdj
    assert callable(kdj)
def test_sma_basic(sample_df):
    from qlab.indicators import sma
    assert callable(sma)
def test_atr_basic(sample_df):
    from qlab.indicators import atr
    assert callable(atr)
def test_sma_basic(sample_df):
    from qlab.indicators import sma
    assert callable(sma)
