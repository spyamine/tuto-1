import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import pandas as pd 

x = 1 + 2 
print (x)
# request page
html = requests.get("https://www.ishares.com/us/products/239726/#tabsAll").content
# soup = BeautifulSoup(html,features = "lxml")


# # find available dates
# holdings = soup.find("div", {"id": "holdings"})
# dates_div = holdings.find_all("div", "component-date-list")[1]
# dates_div.find_all("option")
# dates = [option.attrs["value"] for option in dates_div.find_all("option")]

# # download constituents for each date
# constituents = pd.Series()
# for date in dates:
#     resp = requests.get(
#         f"https://www.ishares.com/us/products/239726/ishares-core-sp-500-etf/1467271812596.ajax?tab=all&fileType=json&asOfDate={date}"
#     ).content[3:]
#     tickers = json.loads(resp)
#     tickers = [(arr[0], arr[1]) for arr in tickers['aaData']]
#     date = datetime.strptime(date, "%Y%m%d")
#     constituents[date] = tickers

# constituents = constituents.iloc[::-1] # reverse into cronlogical order
# constituents.head()

