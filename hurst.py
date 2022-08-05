
import yfinance as yf 
import numpy as np
import pandas as pd

def get_hurst_exponent(time_series):
    """Returns the Hurst Exponent of the time series"""
    max_lag = round(np.sqrt(len(time_series)))
    lags = range(2, max_lag)

    # variances of the lagged differences
    tau = [np.std(np.subtract(time_series[lag:], time_series[:-lag])) for lag in lags]

    # calculate the slope of the log plot -> the Hurst Exponent
    reg = np.polyfit(np.log(lags), np.log(tau), 1)

    return reg[0]


print('bla')
"""
    for lag in [5,10,20, 50, 100, 200]:
#, 500, 1000]:
hurst_exp = get_hurst_exponent(spy["Adj Close"].values, lag)
print(f"Hurst exponent with {lag} lags: {hurst_exp:.4f}")

print('bla')

    """
