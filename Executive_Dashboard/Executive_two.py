import urllib.request as request
import csv
import os
from urllib.parse import urlparse
import plotly as py
import plotly.graph_objs as go
import pandas

print("--------------------------------------------------------------------------------")
print("Welcome! Let's get ready to discover some business insights courtesy of Sarah!")
print("--------------------------------------------------------------------------------")

#Collecting User Inputs
year = input ("Please type the csv year in the following format YYYY:")
month = input ("Please type the csv month in the following format MM:")
user_input = "sales-" + year + month + ".csv"

#Defining functions
def month_lookup(month):
	month_input={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_input[month] 
    #month_lookup adapted from hiep's github

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) 

#Challenge 1: Validating CSV Headers
sales = [
    'sales-201710.csv','sales-201711.csv','sales-201712.csv', 'sales-201801.csv', 'sales-201802.csv', 'sales-201803.csv', 'sales-201804.csv', 'sales-201805.csv', 'sales-201806.csv', 'sales-201807.csv', 'sales-201808.csv', 'sales-201809.csv', 'sales-201810.csv', 'sales-201811.csv', 'sales-201812.csv', 'sales-201901.csv', 'sales-201902.csv', 'sales-201903.csv', 'sales-201904.csv' #finish putting in csvs
]

#Assuming validated: 
if user_input in sales:
    products = []

    with open("data/" + user_input, 'r') as csvfile:
        reader = csv.DictReader(csvfile)


        #transforming from hard to dynamic code
        u= [] #creating a unique list of product names
       
        
        count = {}
        for row in reader:
            d = dict(row)
            d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]), "units sold": row["units sold"], "sales price": row["sales price"]}
        
            if d["product"] not in count:
                count[d['product']] = float(d['units sold'])
            else:
                count[d['product']] += float(d['units sold'])
    
        print(count)
        print(count.keys())
        woo = list(count.items())
        print(woo)




