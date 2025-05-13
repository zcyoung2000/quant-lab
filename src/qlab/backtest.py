"""回测引擎"""

import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    shares: float = 0.0
    cost: float = 0.0

