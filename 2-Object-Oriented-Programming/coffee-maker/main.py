from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
wallet = MoneyMachine()

on = True
while on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == 'off':
        on = False
    elif order == 'report':
        machine.report()
        wallet.report()
    elif order == "add drink":
        menu.add_drink()
    elif order == "refill":
        machine.refill()
    elif menu.in_menu(order):
        order_item = menu.find_drink(order)
        if machine.is_resource_sufficient(order_item) and wallet.make_payment(order_item.cost):
            machine.make_coffee(order_item)
    else:
        print("Invalid order, Please try again")
