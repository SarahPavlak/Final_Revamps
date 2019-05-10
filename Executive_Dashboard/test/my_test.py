from app.my_executive_test import to_usd, get_top_sellers
import csv

def test_to_usd():
    result = to_usd(4)
    assert result == '$4.00'

    result = to_usd(57.70)
    assert result == '$57.70'

    result = to_usd(1057.70)
    assert result == '$1,057.70'

def test_get_top_sellers():
    result = get_top_sellers()

    with open("/Users/SarahPavlak/Desktop/Final_Revamps/Executive_Dashboard/test/dummy_sales.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)

    assert result == "Button-Down Shirt $5,464.20 Super Soft Sweater $2,849.81 Khaki Pants $1,691.00"
