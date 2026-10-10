# Multi-Asset Market Analytics \& Risk Dashboard

Interactive Streamlit dashboard that analyses performance, volatility and correlations across French equities, an equity index and gold.

!\[Dashboard overview](screenshots/overview.png)

  **Live demo:** https://durosoy-market-dashboard.streamlit.app

## Assets covered

|Asset|Ticker (Yahoo Finance)|Type|
|-|-|-|
|CAC 40|`^FCHI`|Equity index|
|Société Générale|`GLE.PA`|Equity|
|BNP Paribas|`BNP.PA`|Equity|
|Gold|`GC=F`|Front-month futures (COMEX)|

## Features

* **Data pipeline**: one year of daily closing prices downloaded with `yfinance`, with explicit column mapping to keep asset order consistent.
* **Log returns**: daily log returns, `ln(P\_t / P\_{t-1})`.
* **Rolling volatility**: 30-day rolling standard deviation of log returns, annualised with √252.
* **Cumulative performance**: relative performance of each asset over the period.
* **Correlation heatmap**: pairwise correlation matrix of daily log returns.

!\[Rolling volatility](screenshots/volatility.png)
!\[Correlation heatmap](screenshots/correlation.png)

## Methodology

**Why log returns?** They are time-additive (the return over several days is the sum of daily log returns), which makes cumulative performance straightforward. They are also consistent with the lognormal price assumption used in the Black-Scholes framework.

**Why √252?** Assuming independent daily returns, variance scales linearly with time, so volatility scales with the square root of time. 252 is the conventional number of trading days per year.

## Limitations

* **Normality**: empirical returns show fat tails and skewness; volatility alone understates tail risk.
* **Correlation is not stable**: estimated over one year, it can change sharply in stress periods, when correlations between risky assets tend to rise.
* **Calendar mismatch**: gold futures and Euronext equities do not share the same trading days; only common trading days are kept before computing returns.
* **Non-synchronous closes**: Paris closes at 17:30 CET while gold futures settle in New York hours, so daily returns are not measured at the same moment. This tends to bias the estimated gold/equity correlation towards zero.
* **Gold proxy**: `GC=F` is a front-month futures contract, not spot gold, so the series can be affected by contract rolls.

## Run locally

```bash
git clone https://github.com/bapt247/Market-analytics-dashboard.git
cd Market-analytics-dashboard
python -m pip install -r requirements.txt
python -m streamlit run Dashboard\_2.0.py
```

## Tech stack

Python, pandas, NumPy, yfinance, Matplotlib, Seaborn, Streamlit

## Possible extensions

* Value at Risk (historical and parametric)
* Simple systematic strategy backtest

## Author

Baptiste Durosoy, engineering student at ESILV
[LinkedIn](https://www.linkedin.com/in/baptiste-durosoy/)

