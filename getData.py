from concurrent import futures 
from datetime import datetime 
import pandas as pd
import pandas_datareader.data as web
import tqdm

from config import IEX_API_KEY

print (IEX_API_KEY)

end = datetime.now() 
start = datetime(end.year - 5, end.month , end.day)
bad = []

def download(ticker):
    df = web.DataReader(ticker,'iex', start, end,api_key=IEX_API_KEY)
    df.to_csv(f"spy/{ticker}.csv")

tickers = pd.read_csv("spy/tickers.csv")["0"].tolist()
# print (tickers["0"].tolist())
print (tickers)
print (len(tickers))

for ticker in tqdm.tqdm(tickers):
    download(ticker)
# with futures.ThreadPoolExecutor(50) as executor: 
#     res = executor.map(download, tickers) 