import requests
import json
from datetime import datetime, timedelta
from config import TIIGO_SESSION_ID
# cookies = {'sessionid': TIIGO_SESSION_ID}
headers = {
    'Content-Type': 'application/json'
}
ETFs =['SPY', 'SH', 'VXX', 'EEM', 'QQQ', 'PSQ', 'XLF', 'GDX', 'HYG', 'EFA', 'IAU', 'XOP', 'IWM', 'FXI', 'SLV', 'USO', 'XLE', 'IEMG', 'AMLP', 'EWZ', 'XLK', 'XLI', 'VWO', 'GLD', 'XLP', 'JNK', 'EWJ', 'XLU', 'VEA', 'IEFA', 'XLV', 'PFF', 'VIXY', 'TLT', 'GDXJ', 'LQD', 'XLB', 'BKLN', 'XLY', 'SMH', 'OIH', 'ASHR', 'RSX', 'MCHI', 'VTI', 'EWH', 'SPLV', 'KRE', 'IVV', 'DIA', 'IEF', 'EZU', 'EWT', 'SPDW', 'VOO', 'SCHF', 'EWY', 'MYY', 'DOG', 'EUM']
for ticker in ETFs:
    print ("working on: {}".format(ticker))
    period = 365
    endDate = datetime.today().strftime('%Y-%m-%d')
    startDate = (datetime.today() - timedelta(days=period)).strftime('%Y-%m-%d')
    url = "https://api.tiingo.com/tiingo/daily/%s/prices?startDate=%s&endDate=%s&token=%s" % (ticker, startDate, endDate,TIIGO_SESSION_ID)

    response = requests.get(url, headers=headers)
    jsonData = {}
    print (response.status_code)
    if response.status_code == 200:
        jsonData = json.loads(response.text)
        if jsonData:
            filename = 'data/%s_%s_%s.txt' % (ticker, startDate, endDate)
            f = open(filename, "w")
            f.write('Date,Open,High,Low,Close,Adj Close,Volume\n')
            for data in jsonData:

                f.write(data['date'][0:10] +',' +str(data['open']) +',' +str(data['high']) +',' +str(data['low'])  
                                           +',' +str(data['close']) +',' +str(data['adjClose']) +',' +str(data['volume']) +'\n')

            f.close()
            print ('file: %s created' % filename)