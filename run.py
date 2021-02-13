import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.BuyHold import BuyHold
from strategies.MovingCrossover import MovingCrossover

cerebro = bt.Cerebro()
cerebro.broker.setcash(10000)

spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True)
feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

strategies = {
    "moving_cross": MovingCrossover,
    "buy_hold": BuyHold,
}

try:
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("strategy", help="Which strategy to run", type=str)
    args = parser.parse_args()

    if not args.strategy in strategies:
        print("Invalid strategy, must select one of {}".format(strategies.keys()))
        sys.exit()

    cerebro.addstrategy(strategy=strategies[args.strategy])

    # if getting error
    # usage: run.py [-h] strategy
    # run.py: error: the following arguments are required: strategy
    # then run script with a key from strategies dictionary

    cerebro.run()
    cerebro.plot()

except:
    print('Due to not declaring strategy, running buy-hold backtest')
    cerebro.addstrategy(strategy=BuyHold)
    cerebro.run()
    cerebro.plot()