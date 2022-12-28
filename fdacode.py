import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
netflix = web.get_data_yahoo("NFLX",
                            start = "2009-01-01",
                            end = "2018-03-01")
print(netflix.head())
##                 High       Low    ...          Volume  Adj Close
## Date                              ...                           
## 2009-01-02  4.357143  4.200000    ...       6605200.0   4.267143
## 2009-01-05  4.562857  4.302857    ...      13044500.0   4.562857
## 2009-01-06  4.750000  4.590000    ...      12065900.0   4.705714
## 2009-01-07  4.734286  4.571429    ...      10133900.0   4.672857
## 2009-01-08  4.797143  4.485714    ...       8175300.0   4.735714
## 
## [5 rows x 6 columns]
Next we will chart the Netflix’s adjusted closing price.

netflix['Adj Close'].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title("Netflix Price data")
plt.show()
netflix_daily_returns = netflix['Adj Close'].pct_change()
netflix_monthly_returns = netflix['Adj Close'].resample('M').ffill().pct_change()

print(netflix_daily_returns.head())
## Date
## 2009-01-02         NaN
## 2009-01-05    0.069300
## 2009-01-06    0.031309
## 2009-01-07   -0.006982
## 2009-01-08    0.013452
## Name: Adj Close, dtype: float64

print(netflix_monthly_returns.head())
## Date
## 2009-01-31         NaN
## 2009-02-28    0.002767
## 2009-03-31    0.184327
## 2009-04-30    0.055685
## 2009-05-31   -0.129993
## Freq: M, Name: Adj Close, dtype: float64

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(netflix_daily_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("Netflix daily returns data")
plt.show()
