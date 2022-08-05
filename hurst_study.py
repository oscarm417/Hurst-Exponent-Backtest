import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf 
from hurst import get_hurst_exponent
import os
import time
from matplotlib.backends.backend_pdf import PdfPages


files = os.listdir(r"C:\Users\oscar\Desktop\Business\Trading\QED Work\OscarsWork\momentum\data")
six_month = 21*6
one_year = 252
three_years = 252*3
#fig, axes = plt.subplots(nrows=(round(len(files))), ncols=1, figsize=(10,15))
count = 0
for stock_data in files:
    plt.figure(figsize=(15,12))
    stock = pd.read_csv("data\\" + stock_data)
    ticker = stock_data.split()[1]
    print(ticker)
    stock = stock[['Date','Spot']]
    stock['Date'] = pd.to_datetime(stock['Date'])
    stock.set_index('Date', inplace=True)

    stock['6m'] = stock['Spot'].rolling(six_month).apply(lambda x: get_hurst_exponent(x), raw=True)
    stock['1y'] = stock['Spot'].rolling(one_year).apply(lambda x: get_hurst_exponent(x), raw=True)
    stock['3y'] = stock['Spot'].rolling(three_years).apply(lambda x: get_hurst_exponent(x), raw=True)
    since_inception =get_hurst_exponent(stock['Spot'].values)
    #  stock['Spot'].rolling(len(stock)).apply(lambda x: get_hurst_exponent(x), raw=True)
    plt.axhline(y= since_inception, label = "SI")
    # axes[count].axhline(y= since_inception[-1])
    plot_values = stock[['6m','1y','3y']]
    # plot_values.plot(title =ticker)
    plt.plot(stock.index, stock['6m'], label="6 month",c = 'r')
    plt.plot(stock.index, stock['1y'],label="1 year",c = 'b')
    plt.plot(stock.index, stock['3y'], label="3 year",c = 'g')
    plt.axhline(stock['6m'].mean(), label="6 month mean", linestyle = ':',c = 'r')
    plt.axhline(stock['1y'].mean(),label="1 year mean", linestyle = ':',c = 'b')
    plt.axhline(stock['3y'].mean(), label="3 year mean", linestyle = ':',c = 'g')
    plt.legend()
    plt.grid()
    plt.title(ticker)
    plt.savefig(ticker+".png")
    

    count+=1
# fig.tight_layout()
plt.show()


print('bla')