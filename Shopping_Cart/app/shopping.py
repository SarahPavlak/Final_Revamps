# shopping_cart.py

import datetime

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
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
print("Shopping Cart")


l=[]
def checkout_time(any_products):
   return any_product ["name"]

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

t = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S") #https://github.com/s2t2/shopping-cart-project/blob/master/shopping_cart.py

while True:
    user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if user_input == "DONE":
        print ("-------------------------------------------")
        print ("Sarah's Grocery Store")
        print ("-------------------------------------------")
        print ("Web: Sarah.Grocery.Store.com")
        print ("Phone: 123-456-7890")
        print ("Checkout Time: " + str(t))
        print ("-------------------------------------------")


        def sort_by_name(any_product):
            return any_product["name"]
        sorted_products = sorted(products,key=sort_by_name)
        
        matching_products = [p for p in products if p["id"] in l]
        
        product = matching_products[0]
        price = (product["price"]) 

        sum = 0
        r = []
        for p in matching_products:
            #price_usd = p["price"]
            price_usd = "${0: .2f}".format(p["price"])
            receipt_item = ("+ " + p["name"] + " (" + str (price_usd) + ")") 
            print(receipt_item)
            sum = sum + p["price"]
            x = sum
            
            r.append(("+ " + p["name"] + " " + str (price_usd)))

        #Writing values to a receipt file
        with open('receipts/receipt.' + str(t) + 'txt', "w") as file: #https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/file-management.md
            file.write("Below Please Find Your Grocery List!")
            file.write("\n")
            file.write("Checkout time: " + str(t))
            file.write("\n")
            file.write("-------------------------------------")
            file.write("\n")
            file.write(receipt_item)

        tax = sum * .0875 #fixed tax
        total = tax + sum
        subtotal = x

        print ("-------------------------------------------")
        print ("Subtotal: " + str(to_usd(subtotal)))
        print ("NYC Sales Tax: " + str(to_usd(tax)))
        print ("Total: " + str(to_usd(total)))
        print ("You have purchased " + str(len(l)) + " items")

        print ("-------------------------------------------")
        print ("Thank you for your business, please come again!")



    else:
        l.append(int(user_input))