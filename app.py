from flask import Flask, render_template
import ccxt
import numpy as np

app = Flask(__name__)

def fetch_market_data():

  mexc = ccxt.mexc()

  TICKER = 'BTC/USDT'


  market_5m = mexc.fetch_ohlcv(symbol=TICKER, timeframe='5m')
  market_live = mexc.fetch_ticker(symbol=TICKER)['last']

  return market_5m, market_live


def calculate_z_score(market_5m, market_live):

  closing_pricing = np.array([values[4] for values in market_5m])

  market_5m_avg_price = np.mean(closing_pricing)
  market_5m_std = np.std(closing_pricing)


  z_score = (market_live - market_5m_avg_price) / market_5m_std

  return z_score


def buy_sell(z_score):


  if (z_score >= 1):
    buy_or_sell = 'Sell'

  elif(z_score <= -1):
    buy_or_sell = 'Buy'
  else:
    buy_or_sell = 'Dont enter yet'


  return buy_or_sell

@app.route('/')
def home():

  market_5m, market_live = fetch_market_data()

  z_score = calculate_z_score(market_5m, market_live)

  buy_or_sell = buy_sell(z_score)

  return render_template('index.html', z_score=z_score, market_live=market_live, buy_or_sell=buy_or_sell)


if __name__ == '__main__':
  app.run(debug=True)






  

