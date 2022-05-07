# Coffee Making Machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(type(MENU["latte]["ingredients"]))
#
# def resources_sufficient():
#     for key in resources:
#         for key2 in MENU[choice]:
#             used_ingredients = int()
#             if resources[key] > used_ingredients:
#                 def process_coins():
#                     quarters = int(input("Insert Quarters  "))
#                     dimes = int(input("Insert dimes  "))
#                     nickels = int(input("Insert nickels  "))
#                     pennies = int(input("Insert pennies  "))
#
#                     def transaction_successful():
#
                        user_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
#                         coffee_cost = MENU[choice]["cost"]
#                         if user_money >= coffee_cost:
#                             profit += MENU[choice]["cost"]
#
#                             def make_coffee():
#                                 for key in resources:
#                                     resources[key] -= MENU[choice]["ingredients"]
#                                 print(f" Here's your {choice}.Enjoy!")
#                             print(f"Here's your {user_money - coffee_cost} change. ")
#                             return True
#                         else:
#                             print(f"Sorry that's not enough money. ${user_money} refunded")
#                             return False
#                 return True
#
#             else:
#                 print("Sorry! there's not enough water.")
#                 return False


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)  ")
    if choice == "espresso" or "latte" or "cappuccino":
        print("dvesh")
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk:  {resources}{'milk'}")
        print(f"coffee:{resources}{'coffee'}  ")
        print(f"money: {profit} ")

    else:
        is_on = False








