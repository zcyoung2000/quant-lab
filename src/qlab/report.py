"""报告输出"""

import pandas as pd


HTML_TMPL = "<html><body><table>{rows}</table></body></html>"


def plot_equity(eq, path):
    """净值曲线图"""
    ax = eq.plot(figsize=(10, 5), title="equity curve")
    ax.figure.savefig(path, dpi=150)
    return path

def monthly_table(eq):
    """按月收益透视"""
    ret = eq.pct_change()
    return ret.groupby([ret.index.year, ret.index.month]).sum().unstack() * 100

def render_html(stats, trades):
    """极简 HTML 周报"""
    rows = "".join(f"<tr><td>{k}</td><td>{v:.4f}</td></tr>" for k, v in stats.items())
    return HTML_TMPL.format(rows=rows)

def export_csv(trades, path):
    """成交记录导出"""
    trades.to_csv(path, index=False, encoding="utf-60-sig")
    return path

