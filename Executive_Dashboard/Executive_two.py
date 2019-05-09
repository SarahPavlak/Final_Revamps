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
        count = {}
        for row in reader:
            d = dict(row)
            d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]), "units sold": row["units sold"], "sales price": row["sales price"]}
            total_sales = float(d['units sold'])* float(d['unit price'])

            if d["product"] not in count:
                count[d['product']] = (total_sales)
            else:
                count[d['product']] += (total_sales)

        for k,v in count.items():
            print("KEY:", k, "VALUE:", v) #https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/653848be8fbc6c59cd98493e946da2b0532bfaba/notes/python/datatypes/dictionaries.md

            #setting up bar data

            bar_data = [
                {"Product": k, "Revenue USD": v}
            ]

            x = []
            y = []

            for i in range(0, len(bar_data)):
                x.append(bar_data[i]['Product'])
                y.append(bar_data[i]['Revenue USD'])

            data = [go.Bar(
                        x=x,
                        y=y,
                )]
            layout = go.Layout(title='Product Profits ' + str(month_lookup(month)) + " " + year,
                xaxis = dict(title="Item"),
                yaxis = dict(title="Sales (USD)"), 
                margin= go.layout.Margin(l=150, pad=8) 
                )
                #code adapted from: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales.py 

            figure = go.Figure(data = data,layout=layout)
            py.offline.plot(figure, filename='basic-bar.html', auto_open = True)

                #bar code adapted from: madeline's shared class version
                  

else:
    print("Oh no, it looks like you have entered an invalid input! Please try again")
