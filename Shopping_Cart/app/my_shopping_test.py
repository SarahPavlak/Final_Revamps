
#My Tests

#Testing that formula turns it into nicely formatted number with $ and two decimal places
def to_usd(i):
    return "${0:,.2f}".format(i)