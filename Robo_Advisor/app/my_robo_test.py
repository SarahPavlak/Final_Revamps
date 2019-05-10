#My Tests

def to_usd(i):
    return "${0:,.2f}".format(i)

def compile_url():
    user_input = "MSFT"
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + "API_KEY"
