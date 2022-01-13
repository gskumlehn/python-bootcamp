class MenuItem:
    # Creates menu item object with name, cost, and dictionary of ingredients:amount
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    # Creates menu with default items using the MenuItem class
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0),
        ]

    # Creates a string with all product names and prices to be displayed
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name} ${item.cost}/"
        options = options[:-1]
        return options

    # Checks if order is inside the menu, returns boolean
    def in_menu(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return True

    # Fetches menu item by item name
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item

    # Adds a new menu item to the menu
    def add_drink(self):
        name = input("What's the new drink's name?: ")
        cost = float(input("How much will it cost (value only)?: "))
        water = int(input("How much water(mL) will it need?:  "))
        milk = int(input("How much milk(mL) will it need?:  "))
        coffee = int(input("How much coffee(g) will it need?:  "))
        self.menu.append(MenuItem(name=name, water=water, milk=milk, coffee=coffee, cost=cost))
