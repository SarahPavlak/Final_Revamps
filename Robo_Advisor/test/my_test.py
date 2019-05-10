from app.my_robo_test import to_usd, compile_url, write_to_csv

def test_to_usd():
    result = to_usd(4)
    assert result == '$4.00'

    result = to_usd(57.70)
    assert result == '$57.70'

    result = to_usd(1057.70)
    assert result == '$1,057.70'

def test_compile_url():
    result = compile_url()
    assert result == "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=API_KEY"


def test_write_to_csv():
    result = write_to_csv()
    assert result == ["timestamp", "open", "low", "high", "close", "volume"]

