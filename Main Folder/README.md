# VWAP-execution-with-partial-fills
Rolling VWAP/TWAP with partial fills. Takes in ticker price data, orders, and tracks benchmarks, etc. 
link 1: https://www.investopedia.com/index-rebalancing-7972596#:~:text=Market%20Volatility,and%20opportunities%20for%20active%20investors.
link 2: https://www.tastylive.com/news-insights/what-happens-when-stock-added-sp500#:~:text=The%20%E2%80%9Cindex%20effect%E2%80%9D%20refers%20to,demand%20often%20drives%20prices%20higher.
link 3: https://www.nasdaq.com/articles/what-happens-to-stocks-added-to-the-nasdaq-100-2021-03-18#:~:text=There%20is%20a%20wealth%20of,longest%2Dterm%20holders%20of%20stocks.

Example: 
S&P Index 500: 

September 18:
NVIDIA
APPL
GOOGL
TESLA
These are all companies that are weighted BY MARKET CAP to be the top 500 companies in the index. 

Robinhood is about to be included in the index (sept 22), we might anticipate that the stock price would go up, because if it's included in the index, we're assuming that people are going to buy this, and drive up the market cap for this company.
So our execution engine would create small buy orders for this, given that it's intaking ticker price data for Robinhood. 



- i'm aiming to create: 
A VWAP - vwap(volume-weighted-average-price) excecution scaffold: 
which: 
- intakes ticker price data (intraday tape [price + volume per second])
- a market VWAP and TWAP benchmark 
- a vwap execution simulator (which buys pro-rata to the market's volume curve)
- implementation shrotfall vs arrival
- a per tick fill log + a quick chart

**Deliverables****(initial scope):**: 
1. Data ingestion - load tick or 1-sec bars. Columns: ts, price, size, side, bid, ask
2. Volume curve  - compute baseline intraday profile, allow smoothing, build a target schedule (front-loaded, back-loaded, or neutral)
3. VWAP scheduler - take a parent oder (eg, buying 100k shares) and allocate into time buckets proportionally to the evolving volume curve; apply participation caps and min child siezx.
4. Execution simulator - generate fills using simple microstructure assumptions:
     - baseline fill price = mid +/- half-spread
5. Benchmarks and metrics - vwap VS achieved price (bps), implementation shortfall vs arrival, realized spread, fill ratio, participation profile, and risk drift.
6. Experimental harness - run scenarios across rebalance days and compare schedules (netural vs front-load vs back-load vs adaptive POV)
7. Outputs - plots and tables per run; summary markdown per experiment,. 
