#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run unit tests using
nosetests -s -v
"""

import time
import datetime

from datareader_femto import *

from pandas.io.data import Options

import requests_cache
expire_after = 60*5 # seconds

def test_yahoo_finance_options():
    #symbol = 'NASDAQ:AAPL'
    #symbol = 'NASDAQ:GOOG'
    symbol = ['NASDAQ:AAPL', 'NASDAQ:GOOG']

    option = MyDataReader("GoogleFinanceOptions").get(symbol)
    print(option)
    print(option.dtypes)
    #option = option.rename(items={
    #    'NASDAQ:AAPL': 'NASDAQ_AAPL',
    #    'NASDAQ:GOOG': 'NASDAQ_GOOG'
    #})
    option.to_excel("google_options.xls")
    #data = option.get_all_data() # get all data
    #print(data)
    #data = option.get_call_data(expiry=expiry) # get call data
