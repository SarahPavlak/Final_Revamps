import csv 
import json
import requests
import os 
from dotenv import load_dotenv
import datetime
import pandas as pd 

load_dotenv()

#Definitions
def to_usd(my_price):
        return "${0:,.2f}".format(my_price) #taken from screencast

API_KEY = os.environ.get('MY_API_KEY')


#Collecting User Information
user_input = input ("Please print a stock symbol: ")
symbol = user_input 

#Obtaining the desired stock information
print("-----------------------------------------------------")
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + API_KEY
print("Your desired stock information comes from:")
print(request_url)
print("-----------------------------------------------------")

data=requests.get(request_url)
#Validating inputs
while True:     
        if user_input.isalpha() and len(user_input) < 6 : 
                pass
                
                if 'Error' in data.text: #this line adapted from https://github.com/hiepnguyen034/robo-stock/blob/master/robo_advisor.py
                        print('The stock you are looking for is not here. The program will now close.')
                        exit()
                break
        else: 
                print("Oh, expecting a properly-formed stock symbol like 'MSFT' with no more than six symbols. Please try again. The program will now exit!")
                exit()
        break
        
        #source: https://stackoverflow.com/questions/36432954/python-validation-to-ensure-input-only-contains-characters-a-z
        #source: https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths 
  

#Sending Request & Compiling Information 
# https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/dictionaries.md

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




#CSV Data

csv_file_path = os.path.join (os.path.dirname(__file__), "data", "prices_" + user_input + ".csv") #changing where data folder is fixes the prior .. issue

csv_header = ["timestamp", "open", "low", "high", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter (csv_file, fieldnames = csv_header)
    for row in rows:
        writer.writerow(row)

#output results

dates = list(tsd.keys()) #from screencast
latest_close = rows[0]["close"]
high_prices = [row["high"] for row in rows] 
low_prices = [row["low"] for row in rows] 
recent_high = max(high_prices)
recent_low = min(low_prices) #https://github.com/s2t2/robo-advisor-screencast/blob/alt-solution/app/robo_advisor.py

print(f"Stock Symbol: {symbol}")
print("Run at: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")) #use date time module
print(f"Latest day of data: {last_refreshed}")
print(f"Latest daily closing price: {to_usd(float(latest_close))}")
print(f"Recent high: {to_usd(float(recent_high))}") 
print(f"Recent low: {to_usd(float(recent_low))}") 
print("-----------------------------------------------------")

#calculating risk




risk_range = float(daily_prices["2. high"]) - float(daily_prices["3. low"])
print("-----------------------------------------------------")
print("Risk Explanation:")
print("Please specify the amount of risk you are willing to accept by inputting a number (0-100) that represents a decrease from the stock high. For example, 10 means that you are ok with the stock losing 10 percent of its value from the high.")
print("-----------------------------------------------------")

risk_input = input("Risk input:")
risk_input_percent = float(risk_input) / 100
stock_drop = float(daily_prices["2. high"]) * (1-risk_input_percent)
risk_span_top = to_usd(float(daily_prices["2. high"]))
risk_span_bottom = to_usd(float(stock_drop))


if risk_input != 0 < float(risk_input) <100.000001:
        if float(daily_prices["3. low"]) < float(stock_drop):
                print(f"Your risk span is: {risk_span_bottom} to {risk_span_top}") 
                print(f"Latest price: {to_usd(float(latest_close))}") 
                print ("RECOMMENDATION: Don't Buy!")
                print ("RECOMMENDATION REASON: Because the latest closing price is not within threshold of your risk tolerance, don't buy.")
                print("-----------------------------------------------------")
                
        else:
                print(f"Your risk span is: {risk_span_bottom} to {risk_span_top}") 
                print(f"Latest price: {to_usd(float(latest_close))}") 
                print("RECOMMENDATION: Buy!")
                print ("RECOMMENDATION REASON: Because the latest closing price is within threshold of your risk tolerance, buy.")
                print("-----------------------------------------------------")
else: 
        print ("Oh no! that's not a valid risk, the program will now close")
        print("-----------------------------------------------------")  
exit()    

print("-----------------------------------------------------")
print("WRITING DATA TO CSV: {csv_file_path}")
print("-----------------------------------------------------")

