import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf
from hurst import get_hurst_exponent

def main(symbol, lvg_above, lvg_below):
    data = pd.read_csv(r'spy_data.csv').iloc[:-2, :]
    data = data[['Date', 'SPY US Equity', 'Spot']]
    data = data[~data['Date'].str.contains('<')]
    data.index = pd.to_datetime(data['Date'])
    
    six_month = 21*6 
    data['hurst'] = data['Spot'].rolling(six_month).apply(lambda x: get_hurst_exponent(x), raw=True)
    data.dropna(inplace=True)
    data['spot daily pnl'] = data['SPY US Equity'].pct_change()
    data['lag'] = data['SPY US Equity'].pct_change(20)
    data['leverage'] = np.where(
        (data['hurst']>.5) & (data['lag']> 0), 
        lvg_above,
        lvg_below
        )    
    data['mom daily pnl (%)'] = data['leverage'].shift(1) * data['spot daily pnl'] + 1
    data['spot daily pnl'] = data['spot daily pnl'] + 1

    data['mom cumu pnl (%)'] = data['mom daily pnl (%)'].cumprod() - 1
    data['spot cumu pnl (%)'] = data['spot daily pnl'].cumprod() - 1

    data['alpha'] = data['mom cumu pnl (%)'] - data['spot cumu pnl (%)']
    print(data)
    data['mom cumu pnl (%)'].plot()  
    data['spot cumu pnl (%)'].plot() 
    plt.legend()
    plt.show()
    print('poop')


if __name__ == '__main__':
    symbol = 'SPY'
    main(symbol, 3, 0.8)