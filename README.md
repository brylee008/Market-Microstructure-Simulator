# VWAP-execution-with-partial-fills
Rolling VWAP/TWAP with partial fills. Takes in ticker price data, orders, and tracks benchmarks, etc. 

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

