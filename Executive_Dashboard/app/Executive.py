import urllib.request as request
import csv
import os
from urllib.parse import urlparse
import plotly as py
import plotly.graph_objs as go
import pandas
import operator
import plotly



print("--------------------------------------------------------------------------------")
print("Welcome! Let's get ready to discover some business insights courtesy of Sarah!")
print("--------------------------------------------------------------------------------")

l=[]
year = input ("Please type the csv year in the following format YYYY:")
month = input ("Please type the csv month in the following format MM:")
user_input = "sales-" + year + month + ".csv"

def month_lookup(month):
	month_input={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_input[month] 
        #month_lookup adapted from hiep's github

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

sales = [
    'sales-201710.csv','sales-201711.csv','sales-201712.csv', 'sales-201801.csv', 'sales-201802.csv', 'sales-201803.csv', 'sales-201804.csv', 'sales-201805.csv', 'sales-201806.csv', 'sales-201807.csv', 'sales-201808.csv', 'sales-201809.csv', 'sales-201810.csv', 'sales-201811.csv', 'sales-201812.csv', 'sales-201901.csv', 'sales-201902.csv', 'sales-201903.csv', 'sales-201904.csv' #finish putting in csvs
]


#Assuming validated: 
if user_input in sales:
    products = []

    with open("data/" + user_input, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        #transforming to dynamic code
        count = {}
        for row in reader:
            d = dict(row)
            d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]), "units sold": row["units sold"], "sales price": row["sales price"]}
            total_sales = float(d['units sold'])* float(d['unit price'])

            if d["product"] not in count:
                count[d['product']] = (total_sales)
            else:
                count[d['product']] += (total_sales)

        count=dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

#Graph 1: Top 5 Sellers Breakdown
        graph_x = []
        graph_y = []
        top = []
        print("Below please find your sales:")
        print("------------------------------------")
        for k,v in count.items():
            dic = dict([("Product", k), ("Sales", v)])
            dic_two = (k + " " + str(to_usd(v)))
            print(dic_two)
            top.append(dic_two)

            x_axis = (dic["Product"])
            y_axis = (dic["Sales"])
            graph_x.append(x_axis)
            graph_y.append(y_axis)
        print("------------------------------------")
        print("Top selling product is: " + str(top[0]))
        print("Second selling product is: " + str(top[1]))
        print("Third selling product is: " + str(top[2]))

        labels = [graph_x[0],graph_x[1],graph_x[2],graph_x[3],graph_x[4]] #decided to show top 5 sales
        values = [graph_y[0],graph_y[1],graph_y[2],graph_y[3],graph_y[4]]


        trace = go.Pie(labels=labels, values=values) #not letting me convert to usd 
        plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)
       

#Graph 2: Bar Graph
        #variables
        
        a = 0


        bar_data = [
                    {"Product": graph_x[a], "Revenue USD": graph_y[a]},
                    {"Product": graph_x[1], "Revenue USD": graph_y[1]},
                    {"Product": graph_x[2], "Revenue USD": graph_y[2]},
                    {"Product": graph_x[3], "Revenue USD": graph_y[3]},
                    {"Product": graph_x[4], "Revenue USD": graph_y[4]},
                    {"Product": graph_x[5], "Revenue USD": graph_y[5]},
                    {"Product": graph_x[6], "Revenue USD": graph_y[6]},
                    {"Product": graph_x[7], "Revenue USD": graph_y[7]},
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


else: print("Oh no! That's not a csv option! The program will now gracefully close.") 
exit 
            

 


     
    
            
            
