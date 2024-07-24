#task1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu ["Beverages"] = {"pepsi": 1.99, "coffe": 2.99}
print(restaurant_menu)

restaurant_menu["Steak"] = "17.99"
print(restaurant_menu)

bruschetta_price = restaurant_menu["Starters"].pop("Bruschetta", None)
print (restaurant_menu)
print(f"Removed Bruschetta with price: {bruschetta_price}") 