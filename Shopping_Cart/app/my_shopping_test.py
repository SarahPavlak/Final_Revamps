import datetime
#My Tests

#Testing that formula turns it into nicely formatted number with $ and two decimal places
def to_usd(i):
    return "${0:,.2f}".format(i)

def human_friendly_timestamp():
    t = datetime.datetime(2012, 2, 23, 0, 0)
    return t.strftime('%m/%d/%Y')


#Testing Product Totals
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per":"item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per":"item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per":"item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per":"item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per":"item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per":"item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per":"item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per":"item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per":"item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per":"item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per":"item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per":"item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per":"item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per":"item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per":"item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per":"item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per":"item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per":"item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per":"item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per":"item"},
    {"id":21, "name": "Organic Bananas", "department": "beverages", "aisle": "juice nectars", "price": 0.79, "price_per":"pound"} #extra challenge of price per pound
] 

def product_totals():
    for p in products:
        user_input = 3
        product_id = p["id"]

        if user_input == product_id: 
            price = (p["price"])
            product = p["name"]
            print(product + " " + str(price))
        else:
            pass

    for p in products:
        user_input = 4
        product_id = p["id"]

        if user_input == product_id: 
            price_two = (p["price"])
            product = p["name"]
            print(product + " " + str(price_two))
        else:
            pass

    product_total = price
    product_total = product_total + price_two
    final_total = ("${0: .2f}".format(product_total))
    return(final_total)

def finding_products():
    for p in products:
        user_input = 7
        product_id = p["id"]

        if user_input == product_id: 
            price = (p["price"])
            format_price = "${0: .2f}".format(price)
            product = p["name"]
            product_details = (product + " " + str(format_price))
        else:
            pass
    return product_details



