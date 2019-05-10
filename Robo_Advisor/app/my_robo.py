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
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + API_KEY
print("Your desired info comes from: " + request_url)
response = requests.get(request_url)

#Validating inputs
while True:     
        if user_input.isalpha() and len(user_input) < 6 : 
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

#output results

print("-----------------------------------------------------")
print(f"Stock Symbol: {user_input}")
print("Run at: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")) #use date time module
print(" ")
print(f"Latest day of available data: {last_refreshed}")
print(f"Latest daily closing price: {to_usd(float(latest_close_usd))}")
print(f"Recent high: {to_usd(float(recent_high))}") 
print(f"Recent low: {to_usd(float(recent_low))}") 
print(" ")

#making a recommendation, redid risk
average_high_price = ((sum(high_prices))/(len(high_prices)))
formatted_average_high = to_usd(average_high_price)

print("Recommendation:")
if float(latest_close_usd) > float(average_high_price):
    print(f"You should NOT buy the stock; the current close price {to_usd(float(latest_close_usd))}" + " is more than the average high " + str(formatted_average_high) + ". Wait until the price goes down and the stock becomes more affordable.")
else:
    print(f"You should BUY the stock; the current close price {to_usd(float(latest_close_usd))}" + " is less than the average high (" + str(formatted_average_high) + "). The stock should go up in value. Get it now before it does!")

exit()    

print("Writing data to csv: {csv_file_path}")
