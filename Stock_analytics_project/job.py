import pandas as pd
import requests
import datetime as dt
import re
import json

import boto3
from io import StringIO, BytesIO

def lambda_handler(event, context,ticker = 'TCB',start_date = '2020-01-01',end_date = dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d')):

    #https://dstock.vndirect.com.vn/lich-su-gia/TCB
    # ticker = 'TCB'
    # start_date = '2020-01-01'
    # end_date = dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d')
    delta = dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.datetime.strptime(start_date, '%Y-%m-%d')


    price_api = f'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:{ticker}~date:gte:{start_date}~date:lte:{end_date}&size={delta.days+1}&page=1'

    HEADERS = {'User-Agent': 'Mozilla'}
    res = requests.get(price_api, headers=HEADERS)
    data = res.json()['data']  
    data = pd.DataFrame(data)
    data['date_clean'] = pd.to_datetime(data['date'])

    data_clean = data[['code', 'date_clean', 'floor', 'close','nmVolume', 'nmValue', 'change', 'pctChange']]
    # data_clean['date'] = pd.to_datetime(data_clean['date'])
    data_clean.set_index('code',inplace=True)

    bucket_name = 'stock-data-cuongnm'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    key = f'{ticker}_stock_data_from_{start_date}_to_{end_date}.csv' #.parquet

    out_buffer = StringIO() #BytesIO , StringIO
    data_clean.to_csv(out_buffer) #to_parquet
    bucket.put_object(Body=out_buffer.getvalue(), Key=key)

    return {
        'statusCode': 200,
        'body': json.dumps('file is created in:'+key)
    }

