from app.my_shopping_test import to_usd, human_friendly_timestamp
import datetime 


def test_to_usd():
    result = to_usd(4)
    assert result == '$4.00'

    result = to_usd(57.70)
    assert result == '$57.70'

    result = to_usd(1057.70)
    assert result == '$1,057.70'

def test_human_friendly_timestamp():
    t = datetime.datetime(2012, 2, 23, 0, 0)
    result = human_friendly_timestamp()
    assert result == t.strftime('%m/%d/%Y')



