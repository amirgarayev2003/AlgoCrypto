import ccxt
import numpy as np


mexc = ccxt.mexc()

TICKER = 'BTC/USDT'


market_5m = mexc.fetch_ohlcv(symbol=TICKER, timeframe='5m')
market_live = mexc.fetch_ticker(symbol=TICKER)['last']

print(market_5m)
print(market_live)