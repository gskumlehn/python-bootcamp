class MoneyMachine:
    # Starts money machine with amount of money made (after selling) and money received (inserted into the machine
    # before turn into profit and change). Default currency in dollar "$" and coin values.
    def __init__(self):
        self.profit = 0
        self.money_received = 0
        self.currency = "$"
        self.coin_values = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickles": 0.05,
            "pennies": 0.01
        }
    # Reports profits
    def report(self):
        print(f"Money: {self.currency}{self.profit}")

    # Processes coins inserted into the machine by type, adding total value to the money received
    def process_coins(self):
        print("Please insert coins.")
        for coin in self.coin_values:
            self.money_received += int(input(f"How many {coin}?: ")) * self.coin_values[coin]
            print(f"Money received: {self.currency}{self.money_received}")
        return self.money_received

    # Uses the amount of money received and cross references with the cost of product, resulting in either a message
    # of insufficient funds if amount of money received is lower than product cost OR deducts the amount necessary to
    # pay for product. Any excess money is refunded.
    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is {self.currency}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
