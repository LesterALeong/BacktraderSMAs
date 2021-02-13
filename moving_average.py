
import os, csv
import yfinance as yf
import pandas

# Gathering the stock data
startdate = '2010-01-01'
enddate = '2020-12-31'
with open('data/symbols.csv') as f:
    for line in f:
        if "," not in line:
            continue
        symbol = line.split(",")[0]
        data = yf.download(symbol, start=startdate, end=enddate)
        data.to_csv('data/{}.csv'.format(symbol))

# Setting up the SMA
closing_price_sum = 0

with open('data/spy.csv') as f:
    content = f.readlines()[-200:]
    for line in content:
        print(line)
        tokens = line.split(',')
        close = tokens[4]

        closing_price_sum += float(close)

print(closing_price_sum/200)
