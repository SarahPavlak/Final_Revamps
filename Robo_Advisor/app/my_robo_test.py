#My Tests
import csv 
import json
import requests
import os 
from dotenv import load_dotenv
import datetime
import pandas as pd 

load_dotenv()

def to_usd(i):
    return "${0:,.2f}".format(i)

def compile_url():
    user_input = "MSFT"
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + "API_KEY"


#CSV Tests

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
def write_to_csv_header():
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        return (csv_header)

def write_to_csv():
    exists = os.path.isfile('/Users/SarahPavlak/Desktop/Final_Revamps-master/Robo_Advisor/app/data/prices_AAPL.csv')
    if exists:
        return("this csv file exists")
    else:
        return("this csv file does not exist")
