"""backtest tests"""

import pandas as pd
import pytest


def test_sweep_basic(sample_df):
    from qlab.backtest import sweep
    assert callable(sweep)
def test_walk_forward_basic(sample_df):
    from qlab.backtest import walk_forward
    assert callable(walk_forward)
