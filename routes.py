from flask import render_template
from .data import fetch_market_data, calculate_z_score, buy_sell


def register_routes(app):

  @app.route('/')
  def home():

    market_5m, market_live = fetch_market_data()

    z_score = calculate_z_score(market_5m, market_live)

    buy_or_sell = buy_sell(z_score)

    return render_template('index.html', z_score=z_score, market_live=market_live, buy_or_sell=buy_or_sell)
