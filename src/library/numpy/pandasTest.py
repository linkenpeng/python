import numpy as np
import pandas as pd

def get_day_change():
    stock_cnt = 200
    view_days = 504
    stock_day_change = np.random.standard_normal((stock_cnt, view_days))
    return stock_day_change

stock_day_change = get_day_change()

print(pd.DataFrame(stock_day_change).head())
print(pd.DataFrame(stock_day_change).head(5))
print(pd.DataFrame(stock_day_change)[:5])

stock_symbols = ['股票' + str(x) for x in range(stock_day_change.shape[0])]
print(pd.DataFrame(stock_day_change, index = stock_symbols).head(2))