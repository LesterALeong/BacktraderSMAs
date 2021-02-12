import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.BuyHold import BuyHold
from strategies.MovingCrossover import MovingCrossover

strategies = {
    'moving_crossover': MovingCrossover,
    'buy_hold': BuyHold
}

parser = argparse.ArgumentParser()
parser.add_argument('strategy', help='which strategy to run', type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print('invalid strategy, must be one of {}'.format(strategies.keys()))
    sys.exit()

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(strategies[args.strategy])

cerebro.run()
cerebro.plot()