import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import datetime as dt
import re
import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#https://dstock.vndirect.com.vn/lich-su-gia/TCB
ticker = 'TCB'
start_date = '2014-01-01'
end_date = '2021-12-17'
delta = dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.datetime.strptime(start_date, '%Y-%m-%d')


price_api = f'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:{ticker}~date:gte:{start_date}~date:lte:{end_date}&size={delta.days+1}&page=1'

HEADERS = {'User-Agent': 'Mozilla'}
res = requests.get(price_api, headers=HEADERS)
data = res.json()['data']  
data = pd.DataFrame(data)

print(data.head())