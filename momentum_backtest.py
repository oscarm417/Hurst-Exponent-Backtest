import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf
def main(symbol, lvg_above, lvg_below):
    data = pd.read_csv(r'spy_data.csv').iloc[:-2, :]
    data = data[['Date', 'SPY US Equity', 'Spot']]
    data = data[~data['Date'].str.contains('<')]
    data.index = pd.to_datetime(data['Date'])
    
    data['200d MAVG'] = data['SPY US Equity'].rolling(window=50).mean()
    data.dropna(inplace=True)

    data['spot daily pnl'] = data['SPY US Equity'].pct_change()
    data['leverage'] = np.where(data['200d MAVG'] - data['Spot'] > 0, lvg_above, lvg_below)    

    data['mom daily pnl (%)'] = data['leverage'].shift(1) * data['spot daily pnl'] + 1
    data['spot daily pnl'] = 1.24* data['spot daily pnl'] + 1

    data['mom cumu pnl (%)'] = data['mom daily pnl (%)'].cumprod() - 1
    data['spot cumu pnl (%)'] = data['spot daily pnl'].cumprod() - 1

    data['alpha'] = data['mom cumu pnl (%)'] - data['spot cumu pnl (%)']
    print(data)
    #print(data['leverage'].mean())
    data['mom cumu pnl (%)'].plot()  
    data['spot cumu pnl (%)'].plot() 
    plt.show()
    print('poop')


if __name__ == '__main__':
    symbol = 'SPY'
    main(symbol, 1.25, 0.8)