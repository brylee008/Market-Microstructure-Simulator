# VWAP-execution-with-partial-fills
Rolling VWAP/TWAP with partial fills. Takes in ticker price data, orders, and tracks benchmarks, etc. 
https://www.investopedia.com/index-rebalancing-7972596#:~:text=Market%20Volatility,and%20opportunities%20for%20active%20investors.
https://www.tastylive.com/news-insights/what-happens-when-stock-added-sp500#:~:text=The%20%E2%80%9Cindex%20effect%E2%80%9D%20refers%20to,demand%20often%20drives%20prices%20higher.
https://www.nasdaq.com/articles/what-happens-to-stocks-added-to-the-nasdaq-100-2021-03-18#:~:text=There%20is%20a%20wealth%20of,longest%2Dterm%20holders%20of%20stocks.

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



- we're trying to create: 
A VWAP - vwap(volume-weighted-average-price) excecution scaffold: 
which: 
- intakes ticker price data (intraday tape [price + volume per second])
- a market VWAP and TWAP benchmark 
- a vwap execution simulator (which buys pro-rata to the market's volume curve)
- implementation shrotfall vs arrival
- a per tick fill log + a quick chart

