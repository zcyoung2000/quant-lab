"""报告输出"""

import pandas as pd


HTML_TMPL = "<html><body><table>{rows}</table></body></html>"


def plot_equity(eq, path):
    """净值曲线图"""
    ax = eq.plot(figsize=(10, 5), title="equity curve")
    ax.figure.savefig(path, dpi=150)
    return path

