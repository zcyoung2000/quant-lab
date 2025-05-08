# quant-lab

个人量化研究工具箱。

## 项目简介

量化研究工具箱：数据抓取、指标计算、回测与报告，一站式个人研究环境。


## 特性

- 数据：多源日线抓取、复权、本地缓存
- 指标：SMA / EMA / RSI / MACD / BOLL / ATR / KDJ / OBV
- 回测：逐日撮合、手续费与滑点、绩效统计


> data files are gitignored; run fetch first.

## 安装

```bash
pip install -r requirements.txt
```


## 快速开始

```python
from qlab.data import fetch_kline
from qlab.indicators import sma

df = fetch_kline("600519", "2024-01-01", "2024-12-31")
print(sma(df.close, 20).tail())
```


## 回测示例

```python
from qlab.backtest import run, perf_stats

sig = (df.close > sma(df.close, 20)).astype(int).diff().fillna(0)
eq = run(df, sig)
print(perf_stats(eq))
```


## 目录结构

```
src/qlab/     核心包
tests/        单元测试
config/       示例配置
```


## 指标列表

| 指标 | 函数 |
|---|---|
| SMA | `sma` |
| EMA | `ema` |
| RSI | `rsi` |
| MACD | `macd` |
| BOLL | `boll` |


> requires Python 3.10+ and pandas >= 2.0.

> data files are gitignored; run fetch first.

> requires Python 3.10+ and pandas >= 2.0.

> data files are gitignored; run fetch first.

> see CHANGELOG.md for details.

> 假设手续费双边万 2.5。

## 参数说明

- `cash`：初始资金，默认 100 万
- 手续费默认万 2.5，滑点千 1


## Roadmap

- [x] 指标库
- [x] 回测引擎
- [ ] 因子分析
- [ ] 实盘对接


## 免责声明

本项目仅用于个人学习研究，不构成任何投资建议。


## FAQ

Q: 数据源请求失败？
A: 默认自动重试 3 次，网络异常时检查代理设置。


> 假设手续费双边万 2.5。

## 性能

全量指标在 3000 根日线上计算耗时 < 100ms（M2 实测）。


## 数据说明

默认复权方式为前复权；停牌日自动剔除。


## 贡献

个人项目，欢迎 issue 交流，暂不接受 PR。


## 环境

Python 3.10+，Mac 与 Linux 均可运行，Windows 未测试。


<!-- misc notes -->
