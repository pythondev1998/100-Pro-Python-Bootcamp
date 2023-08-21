from data import MENU, resources

profit = 0
# TODO 1. Print report. How much water, milk and coffee left.
def print_report():
    r = resources
    w = r["water"]
    m = r["milk"]
    c = r["coffee"]
    print(f" Water: {w}ml \n Milk: {m}ml \n Coffee: {c}g \n Money: ${profit}")


# TODO 2. Check resources sufficient? Check if the machine has enough ingredients.
def check_resources(type_coffee):
    # Lo que pide el usuario
    i = MENU[type_coffee]["ingredients"]
    water = i.get("water", 0)
    milk = i.get("milk", 0)
    coffee = i.get("coffee", 0)
    # Lo que tiene la maquina
    r = resources
    w = r["water"]
    m = r["milk"]
    c = r["coffee"]

    if (w - water) < 0:
        print("Sorry there is not enough water")
        return False
    if (m - milk) < 0:
        print("Sorry there is not enough milk")
        return False
    if (c - coffee) < 0:
        print("Sorry there is not enough coffe")
        return False
    return True


# TODO 3. Process coin (make the maths so solve)
def process_coin():
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickel = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money_inserted = (quarter * 0.25) + (dimes * 0.1) + (nickel * 0.05) + (pennies * 0.01)

    return money_inserted


# TODO 4. Check transaction successful? (Give the change back)
def check_transaction(cost_i, coffee_t):
    change = 0
    i = MENU[coffee_t]["ingredients"]
    water = i.get("water", 0)
    milk = i.get("milk", 0)
    coffee = i.get("coffee", 0)
    cost = MENU[coffee_t]["cost"]

    if cost_i < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round((cost_i - cost),2)
        global profit
        profit += round((cost_i - change), 2)
        make_coffee(water, milk, coffee)

    return change


# TODO 5. Make the coffee
def make_coffee(w, m, c):
    i = resources
    resources["water"] -= w
    resources["milk"] -= m
    resources["coffee"] -= c


def start_machine():
    while True:
        coffee_selection = input("What would you like? (espresso/latte/cappuccino): ")

        if coffee_selection == "report":
            print_report()
            continue

        sufficient = check_resources(coffee_selection)

        if sufficient:
            cost_i = process_coin()
            change = check_transaction(cost_i, coffee_selection)

            print(f"Here is ${change} in change.")


start_machine()