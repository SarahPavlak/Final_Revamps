import datetime
#My Tests

#Testing that formula turns it into nicely formatted number with $ and two decimal places
def to_usd(i):
    return "${0:,.2f}".format(i)

def human_friendly_timestamp():
    t = datetime.datetime(2012, 2, 23, 0, 0)
    return t.strftime('%m/%d/%Y')