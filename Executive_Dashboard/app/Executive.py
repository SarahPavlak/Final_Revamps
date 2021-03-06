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


#Challenge 1, Validating CSV Header
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
        n = [] #Challenge 3 Normalizing Data
        top = []
        print("   ")
        print("Below please find your sales:")
        print("------------------------------------------------------")
        for k,v in count.items():
            dic = dict([("Product", k), ("Sales", v)])
            dic_two = (k + " " + str(to_usd(v)))
            item = k
            item_sales = str(to_usd(v))

            print(item)
            print("Current monthly sales were: " + str(item_sales))
            top.append(dic_two)

            if month == "02":
                normalized_v = (v/28)*31 #accounting for daily sales and then adjusting if it had been 31 days
                print("Normalized sales amount is: " + str(to_usd(normalized_v)))
                print("------------------------------------------------------")
               
            else:
                pass

            thirty = ["04", "06", "09", "11"]
            if month in thirty:
                normalized_thirty = (v/30)*31
                print("Normalized sales amount is: " + str(to_usd(normalized_thirty)))
                print("------------------------------------------------------")
                
            
            else:
                pass

            thirty_three = ["01", "03", "05", "07", "08", "10", "12"]
            if month in thirty_three:
                normalized_thirty_three = (v/31)*31
                print("Normalized sales amount is: " + str(to_usd(normalized_thirty_three)))
                print("------------------------------------------------------")
            
            else:
                pass
            

            x_axis = (dic["Product"])
            y_axis = (dic["Sales"])
            graph_x.append(x_axis)
            graph_y.append(y_axis)

        print("   ") 
        print("Below please find your top sales:")
        print("Top selling product is: " + str(top[0]))
        print("Second selling product is: " + str(top[1]))
        print("Third selling product is: " + str(top[2]))

        print("   ") 
        print("Thank you for visiting these insights!")

    #Extra Graph
        labels = [graph_x[0],graph_x[1],graph_x[2],graph_x[3],graph_x[4]] #decided to show top 5 sales
        values = [graph_y[0],graph_y[1],graph_y[2],graph_y[3],graph_y[4]]

        trace = go.Pie(labels=labels, values=values) #not letting me convert to usd 
        plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)
       

    #Graph 2: Bar Graph
    #variables
        
    a = 0
    bar_data = []
    scam = len(graph_x)
    while a < scam:

        bar_data.append({"Product": graph_x[a], "Revenue USD": graph_y[a]})
        a = a + 1
        


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
            

 


     
    
            
            
