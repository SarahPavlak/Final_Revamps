#My Tests
import csv 
import json
import requests
import os 
from dotenv import load_dotenv
import datetime
import pandas as pd 

load_dotenv()
API_KEY = os.environ.get('MY_API_KEY')

#Basic Tests----------------------------------------------------------------------------------------

def to_usd(i):
    return "${0:,.2f}".format(i)

def compile_url():
    user_input = "MSFT"
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + API_KEY

#CSV & API Tests----------------------------------------------------------------------------------------

user_input = "AAPL"
API_KEY = os.environ.get('MY_API_KEY')

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + API_KEY
response = requests.get(request_url)

parsed_response = json.loads(response.text) #from class
tsd = parsed_response["Time Series (Daily)"] #from screencast
dates = list(tsd.keys()) #from screencast

csv_file_path = os.path.join (os.path.dirname(__file__), "data", "prices_" + user_input + ".csv")
csv_header = ["timestamp", "open", "low", "high", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter (csv_file, fieldnames = csv_header)

        for date in dates:
            daily_prices = tsd[date]

            writer.writerow({
                "timestamp": date,  
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"], 
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"], 
                "volume": daily_prices["5. volume"] 
        })

#CSV Requests----------------------------------------------------------------------------------------
def write_to_csv_header():
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        return (csv_header)

def write_to_csv():
    exists = os.path.isfile('/Users/SarahPavlak/Desktop/Final_Revamps-master/Robo_Advisor/app/data/prices_AAPL.csv') #mine is configured for me..
    if exists:
        return("this csv file exists")
    else:
        return("this csv file does not exist")

#Issuing API Requests----------------------------------------------------------------------------------------
def get_responses():
        keys = (parsed_response.keys())
        return (str(keys))

def get_responses_dict():
        dict_response = (type(parsed_response))
        return(str(dict_response))






#Processing API Requests----------------------------------------------------------------------------------------

#defining variables
latest_day = dates[0] #from screencast
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"] 
latest_close_usd = tsd[latest_day]["4. close"] #from screencast

high_prices = [] 
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append (float(high_price))

recent_high = max(high_prices)

low_prices = [] 
for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append (float(low_price))

recent_low = min(low_prices)

result =  { #adapted from https://github.com/hiepnguyen034/robo-stock/blob/master/robo_advisor.py
'time':last_refreshed,
'high': high_price,
'low': low_price,
'close': latest_close_usd}

def transform_response():
        str_result = str(result)
        return str_result

