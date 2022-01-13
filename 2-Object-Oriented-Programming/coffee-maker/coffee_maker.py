class CoffeeMaker:
    # Initiates coffee maker with default amount of resources
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    # Reports amount of resources
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    # Add resources
    def refill(self):
        for key in self.resources.keys():
            add = int(input(f"How much {key} do you want to add?: "))
            self.resources[key] += add

    # Checks if amount of resources are enough to produce product
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    # Deducts amount of resources to produce product and delivers it
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
