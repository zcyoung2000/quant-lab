import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def sample_df():
    idx = pd.bdate_range("2024-01-01", periods=120)
    close = pd.Series(100 + np.cumsum(np.random.randn(120)), index=idx)
    return pd.DataFrame({"open": close, "high": close + 1,
                         "low": close - 1, "close": close,
                         "volume": 1_000_000}, index=idx)
