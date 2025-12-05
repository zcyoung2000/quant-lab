"""backtest tests"""

import pandas as pd
import pytest


def test_sweep_basic(sample_df):
    from qlab.backtest import sweep
    assert callable(sweep)
def test_walk_forward_basic(sample_df):
    from qlab.backtest import walk_forward
    assert callable(walk_forward)
def test_sweep_basic(sample_df):
    from qlab.backtest import sweep
    assert callable(sweep)
def test_perf_stats_basic(sample_df):
    from qlab.backtest import perf_stats
    assert callable(perf_stats)
def test_sweep_basic(sample_df):
    from qlab.backtest import sweep
    assert callable(sweep)
