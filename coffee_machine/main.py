from data import MENU
from data import resources

continue_order = True
customer_balance = 0
sufficient_coins = False
machine_balance = 0
change = 0

total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]

def order():
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    return user_input

def off():
    global continue_order
    continue_order = False

def report():
    print("Water:", resources["water"], "ml")
    print("Milk:", resources["milk"], "ml")
    print("Coffee:", resources["coffee"], "g")
    print(f"Machine balance: $ {machine_balance}")

def stock_check(coffee):
    ingredients_needed = MENU[coffee]["ingredients"]
    if total_water < ingredients_needed["water"]:
        print("Not enough water")
        return False
    elif "milk" in ingredients_needed and total_milk < ingredients_needed["milk"]:
        print("Not enough milk")
        return False
    elif total_coffee < ingredients_needed["coffee"]:
        print("Not enough coffee")
        return False
    else:
        print("Enough resources.")
        return True
    return total_water, total_milk, total_coffee

def balance_check(coffee, customer_balance):
    if customer_balance < MENU[coffee]["cost"]:
        print(f"Please insert some coins. Your order costs {MENU[coffee]['cost']}")
        return False
    else:
        return True

def make_coffee(coffee, customer_balance, total_water, total_milk, total_coffee, machine_balance, change):
    ingredients_needed = MENU[coffee]["ingredients"]
    if not stock_check(coffee):
        return customer_balance, total_water, total_milk, total_coffee, machine_balance  # Return early if resources are not enough
    customer_balance -= MENU[coffee]["cost"]
    change = round(customer_balance, 2)
    total_water -= ingredients_needed["water"]
    total_coffee -= ingredients_needed["coffee"]
    machine_balance += MENU[coffee]["cost"]
    if "milk" in ingredients_needed:
        total_milk -= ingredients_needed["milk"]

    resources["water"] = total_water
    resources["milk"] = total_milk
    resources["coffee"] = total_coffee

    print(f"Enjoy your {coffee}. Here is ${change} in change. Remaining coffee: {total_coffee}g. Remaining milk: {total_milk}ml. Remaining water: {total_water}ml")
    return customer_balance, total_water, total_milk, total_coffee, machine_balance

def insert_coins(customer_balance):
    quarters = float(input("How many quarters?"))
    customer_balance += quarters * 0.25
    dimes = float(input("How many dimes?"))
    customer_balance += dimes * 0.10
    nickles = float(input("How many nickles?"))
    customer_balance += nickles * 0.5
    pennies = float(input("How many pennies?"))
    customer_balance += pennies * 0.01
    return customer_balance

# Main loop
while continue_order:
    coffee = order()
    if coffee == "off":
        off()
    elif coffee == "report":
        report()
    elif coffee in MENU:
        if stock_check(coffee):
            while True:
                customer_balance = insert_coins(customer_balance)
                if balance_check(coffee, customer_balance):
                    # If the balance is sufficient, make the coffee
                    customer_balance, total_water, total_milk, total_coffee, machine_balance = make_coffee(coffee, customer_balance, total_water, total_milk, total_coffee, machine_balance, change)
                    break
                else:
                    # Refund the customer_balance and ask the user to insert more coins
                    print(f"Sorry that's not enough customer_balance. {customer_balance} refunded.")
                    customer_balance = 0  # Reset the balance to 0
