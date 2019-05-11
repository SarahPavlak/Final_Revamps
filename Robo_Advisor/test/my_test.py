#My Tests
import csv 
import json
import requests
import os 
from dotenv import load_dotenv
import datetime
import pandas as pd 
from app.my_robo_test import to_usd, compile_url, write_to_csv_header, write_to_csv, get_responses, get_responses_dict, transform_response

load_dotenv()

def test_to_usd():
    result = to_usd(4)
    assert result == '$4.00'

    result = to_usd(57.70)
    assert result == '$57.70'

    result = to_usd(1057.70)
    assert result == '$1,057.70'

def test_compile_url():
    result = compile_url()
    assert result == "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=API_KEY"

def test_write_to_csv_header():
    result = write_to_csv_header()
    csv_file_path = ("/Users/SarahPavlak/Desktop/Final_Revamps-master/Robo_Advisor/app/data/prices_AAPL.csv")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        assert result == ['timestamp', 'open', 'low', 'high', 'close', 'volume']

def test_write_to_csv():
    result = write_to_csv()
    assert result == "this csv file exists"

def test_get_responses():
    result = get_responses()
    assert result == "dict_keys(['Meta Data', 'Time Series (Daily)'])"

def test_get_responses_dict():
    result = get_responses_dict()
    assert result == "<class 'dict'>"

def test_transform_response():
        result = transform_response()
        assert result == "{'time': '2019-05-10 16:00:01', 'high': '168.3500', 'low': '162.7300', 'close': '197.1800'}"
