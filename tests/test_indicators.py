"""indicators tests"""

import pandas as pd
import pytest


def test_boll_basic(sample_df):
    from qlab.indicators import boll
    assert callable(boll)
