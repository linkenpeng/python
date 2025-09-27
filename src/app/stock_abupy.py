'''
pip install abupy
'''
import numpy as np
import pandas as pd
from abupy import ABuMarketDrawing
from abupy import ABuSymbolPd

def get_day_change():
    stock_cnt = 200
    view_days = 504
    stock_day_change = np.random.standard_normal((stock_cnt, view_days))
    return stock_day_change

def dataPrint():
    stock_day_change = get_day_change()

    print(pd.DataFrame(stock_day_change).head())
    print(pd.DataFrame(stock_day_change).head(5))
    print(pd.DataFrame(stock_day_change)[:5])

    stock_symbols = ['股票' + str(x) for x in range(stock_day_change.shape[0])]
    print(pd.DataFrame(stock_day_change, index = stock_symbols).head(2))

def daysPrint():
    stock_day_change = get_day_change()
    days = pd.date_range('2022-1-1', periods=stock_day_change.shape[1], freq='1d')
    stock_symbols = ['股票' + str(x) for x in range(stock_day_change.shape[0])]
    df = pd.DataFrame(stock_day_change, index=stock_symbols, columns=days)
    # print(df.head(2))
    # 行列转置
    df = df.T
    # print(df.head())
    # df_20 = df.resample('21D').median()
    # print(df_20.head())
    df_stock0 = df['股票0']
    # print(type(df_stock0))
    # print(df_stock0.head())
    # df_stock0.cumsum().plot()

    df_stock0_5 = df_stock0.cumsum().resample('5D').median()
    df_stock0_20 = df_stock0.cumsum().resample('21D').median()
    print(df_stock0_5.head())
    df_stock0_20.plot(kind='bar')

    ABuMarketDrawing.plot_candle_stick(df_stock0_5.index,
                                       df_stock0_5['open'].values,
                                       df_stock0_5['high'].values,
                                       df_stock0_5['low'].values,
                                       df_stock0_5['close'].values,
                                       np.random.rand(len(df_stock0_5)),
                                       None, 'stock', day_sum=False, html_bk=False,
                                       save=False
                                       )

def abu():
    tsla_df = ABuSymbolPd.make_kl_df('usTSLA', n_folds=2)
    tsla_df.tail()

if __name__ == '__main__': 
    abu()