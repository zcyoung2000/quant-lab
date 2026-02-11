"""factors tests"""

import pandas as pd
import pytest


def test_f_reversal_basic(sample_df):
    from qlab.factors import f_reversal
    assert callable(f_reversal)
