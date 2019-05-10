import urllib.request as request
import csv
import os
from urllib.parse import urlparse

#Testing that formula turns it into nicely formatted number with $ and two decimal places
def to_usd(i):
    return "${0:,.2f}".format(i)


with open("dummy_sales.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)

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

    top = []
    for k,v in count.items():
        dic = dict([("Product", k), ("Sales", to_usd(v))])
        dic_two = (k + " " + str(to_usd(v)))
        #print(dic_two)
        top.append(dic_two)

    print(top[0])
