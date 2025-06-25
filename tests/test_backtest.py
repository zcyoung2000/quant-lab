"""backtest tests"""

import pandas as pd
import pytest


def test_sweep_basic(sample_df):
    from qlab.backtest import sweep
    assert callable(sweep)
