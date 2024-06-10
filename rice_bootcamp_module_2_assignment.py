# -*- coding: utf-8 -*-
"""Rice Bootcamp  Module #2 Assignment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/178qXNfpbyIvt40EiwRDFWxkpXoTfZEMO
"""

# menu dictionary





# Menu dictionary
menu = { "Snacks": { "Cookie": .99, "Banana": .69, "Apple": .49, "Granola bar": 1.99 },
         "Meals": { "Burrito": 4.49, "Teriyaki Chicken": 9.99, "Sushi": 7.49, "Pad Thai": 6.99,
                   "Pizza": { "Cheese": 8.99, "Pepperoni": 10.99, "Vegetarian": 9.99 },
                   "Burger": { "Chicken": 7.49, "Beef": 8.49 } },
         "Drinks": { "Soda": { "Small": 1.99, "Medium": 2.49, "Large": 2.99 },
                      "Tea": { "Green": 2.49, "Thai iced": 3.99, "Irish breakfast": 2.49 },
                      "Coffee": { "Espresso": 2.99, "Flat white": 2.99, "Iced": 3.49 } },
         "Dessert": { "Chocolate lava cake": 10.99,
                      "Cheesecake": { "New York": 4.99, "Strawberry": 6.49 },
                      "Australian Pavlova": 9.99, "Rice pudding": 4.99, "Fried banana": 4.49 } }

menu_number = int(input("Please enter menu number: "))

# Puts each main menu item into a list
main_menu = [i for i in menu]

# Stores the seltected sub menu item
selected_items = {}
# Ensures unique keys for each selected item
current_key = 1

# Looping through the main menu list
for i in range(len(main_menu)):
    if menu_number == i + 1:
        print(f"You selected {main_menu[i]}")

        # After selecting an item from the main menu,
        # We ensure that while is True to get a continuous loop
        # So that "What {main_menu[i]} item do you want to order?" and further steps can be asked continuously
        while True:
            print(f"What {main_menu[i]} item do you want to order?")

            # We are going to store the sub menu items and prices
            #associated with the main menu number we chose into two lists
            sub_menu_items = []
            sub_menu_prices = []

            for item, price in menu[main_menu[i]].items():
                if isinstance(price, (int, float)): # Isinstance checks if price is in class int or float
                    sub_menu_items.append(item)
                    sub_menu_prices.append(price)
                else:
                    for sub_item, sub_price in price.items():
                        sub_menu_items.append(f"{item}-{sub_item}") # Example Pizza-Cheese
                        sub_menu_prices.append(sub_price)

            print()
            print("Item #  | Item name                  | Price")
            print("--------|----------------------------|-------")
            for x in range(len(sub_menu_prices)):
                print(f"{str(x + 1).ljust(7)} | {sub_menu_items[x].ljust(26)} | {str(sub_menu_prices[x]).ljust(5)}")

            sub_menu_choice = int(input("Choose the item number that you want to order: "))

            # We are generating the final nested dictionary to store the current submenu number, item name and price
            if 1 <= sub_menu_choice <= len(sub_menu_items):
                selected_items[current_key] = {
                    "item name": sub_menu_items[sub_menu_choice - 1],
                    "price": sub_menu_prices[sub_menu_choice - 1]
                }
                current_key += 1  # Increment the key for the next item
            else:
                print("Invalid choice. Please select a valid item number.")

            # Checking if we need to continue asking for another item in the same sub menu
            continue_choice = input("Do you want to order another item from this menu? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                break

print("Selected items:", selected_items)