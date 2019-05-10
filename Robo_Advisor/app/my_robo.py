import csv 
import json
import requests
import os 
from dotenv import load_dotenv
import datetime
import pandas as pd 

load_dotenv()

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

request = request_url
response = requests.get(request_url)

#Validating inputs

while True:     
        if user_input.isalpha() and len(user_input) < 6 : 
                print(user_input)
                
                if 'Error' in response.text: #this line adapted from https://github.com/hiepnguyen034/robo-stock/blob/master/robo_advisor.py
                        print('The stock you are looking for is not here. The program will now close.')
                        exit()
                break
        else: 
                print("Oh, expecting a properly-formed stock symbol like 'MSFT' with no more than six symbols. Please try again. The program will now exit!")
                exit()
        break
        
        
        #source: https://stackoverflow.com/questions/36432954/python-validation-to-ensure-input-only-contains-characters-a-z
        #source: https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths 
  


parsed_response = json.loads(response.text) #from class
tsd = parsed_response["Time Series (Daily)"] #from screencast
dates = list(tsd.keys()) #from screencast
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

#output results

print("-----------------------------------------------------")
print(f"STOCK SYMBOL: {symbol}")
print("RUN AT: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")) #use date time module
print("-----------------------------------------------------")
print(f"LATEST DAY OF AVAILABLE DATA: {last_refreshed}")
print(f"LATEST DAILY CLOSING PRICE: {to_usd(float(latest_close_usd))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}") 
print(f"RECENT LOW: {to_usd(float(recent_low))}") 
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
                print(f"Latest price: {to_usd(float(latest_close_usd))}") 
                print ("RECOMMENDATION: Don't Buy!")
                print ("RECOMMENDATION REASON: Because the latest closing price is not within threshold of your risk tolerance, don't buy.")
                print("-----------------------------------------------------")
                
        else:
                print(f"Your risk span is: {risk_span_bottom} to {risk_span_top}") 
                print(f"Latest price: {to_usd(float(latest_close_usd))}") 
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

parsed_response["Meta Data"].keys()

