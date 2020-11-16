import pandas as pd
import pandas_datareader.data as web
import backtrader as bt
import numpy as np
from datetime import datetime 

data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# print (data)
table = data[0]
# print ("table: \n {}".format(table))
# print (table.Symbol)
# tickers = table[1:][0].tolist()
pd.Series(table.Symbol.tolist()[1:]).to_csv("spy/tickers.csv")