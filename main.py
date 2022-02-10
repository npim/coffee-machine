from data import MENU, resources
profit = 0

on = True

def check_sufficient_resources(option):
    chosen_option_ingredients = MENU[option]['ingredients']
    for ingredient in chosen_option_ingredients:
        if chosen_option_ingredients[ingredient] > resources[ingredient]:
            print(f"We don't have enough {ingredient} to make {option}")
            return False
    return True

def process_coins(option):
    input("$$$ Please insert coins $$$")
    print(f"The cost is {MENU[option]['cost']}")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    inserted_value = float((quarters * 0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01))
    return inserted_value

def is_transaction_successful(inserted_value, cost):
    global profit
    if inserted_value > cost:
        print("Your purchase is successfull!")
        change = round(inserted_value - cost, 2)
        print(f"Here is ${change} dollars in change.")
        profit += cost
        return True
    elif inserted_value == cost:
        print("Your purchase is successfull!")
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
    return False

def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name.capitalize()}. Enjoy!")


while on: 
    option = input("What would you like? (espresso, latte, cappuccino): ")
    report_prompt = f"************\n## Our Resources ##\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${profit}"
    if option not in MENU:
        if option == "off":
            on = False
        elif option == "report":
            print(report_prompt+"\n************")
        else:
            print("Not a valid option.")
    else:
        print(f"You Choose: {option.capitalize()}")
        if check_sufficient_resources(option) and is_transaction_successful(process_coins(option), MENU[option]['cost']):
            make_coffee(option, MENU[option]['ingredients'])

