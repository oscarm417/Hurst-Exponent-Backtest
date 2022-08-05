import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf 
from hurst import get_hurst_exponent


#if 5d ma hurst above .5 and 30d ma hurst below .5:
    #trending
#elif 5d ma hurst < .5 and 30d Ma hurst > .5:
    #reversal

#lag = np.sqrt(len(data_series))

data = yf.download('spy')
window = 101
data['hurst'] = data['Adj Close'].rolling(window).apply(lambda x: get_hurst_exponent(x,20), raw=True)
data.dropna(inplace = True)
data['h_ma5'] = data['hurst'].rolling(window = 5).mean()
data['h_ma20'] = data['hurst'].rolling(window = 20).mean()
data.dropna(inplace = True)

"""
if 5 day ma return positive:
    if 5d ma h> .5 and 20d ma h <.5: #go long on trend 
        go long
    elif 5d ma h< .5 and 20d ma h> .5: #mean reverting 
        go short 

elif 5 day ma return negative:
    if 5d ma h> .5 and 20d ma H < .5: #go short on trend
        go short
    elif 5d ma h <.5 and 20d ma >.5: #mean reverting - buy the dip
        go long
"""
print('bla')