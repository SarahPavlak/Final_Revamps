import csv 
import json
import requests
import os 
from dotenv import load_dotenv
import datetime
import pandas as pd 

def to_usd(i):
    return "${0:,.2f}".format(i)

def compile_url():
    user_input = "MSFT"
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + "API_KEY"


#-------------------------------------------------------------------

user_input = "AAPL"
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + "API_KEY"

response = requests.get(request_url)
parsed_response = json.loads(response.text)
metadata = parsed_response["Meta Data"]
tsd = parsed_response["Time Series (Daily)"]
last_refreshed = metadata["3. Last Refreshed"]

#Transforming Data
rows = []

for date, daily_prices in tsd.items(): # see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/dictionaries.md
    row = {
        "timestamp": date,
        "open": float(daily_prices["1. open"]),
        "high": float(daily_prices["2. high"]),
        "low": float(daily_prices["3. low"]),
        "close": float(daily_prices["4. close"]),
        "volume": int(daily_prices["5. volume"])
    }
    rows.append(row)

csv_file_path = os.path.join (os.path.dirname(__file__), "data", "prices_" + user_input + ".csv") #changing where data folder is fixes the prior .. issue

csv_header = ["timestamp", "open", "low", "high", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter (csv_file, fieldnames = csv_header)
    for row in rows:
        writer.writerow(row)

def write_to_csv():
    with open(csv_file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
    return(csv_header)