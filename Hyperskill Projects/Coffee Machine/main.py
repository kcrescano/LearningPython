class CoffeeMachine:
    complete_menu = {
        "1": {"water": 250, "milk": 0, "coffee beans": 16, "cost": 4},
        "2": {"water": 350, "milk": 75, "coffee beans": 20, "cost": 7},
        "3": {"water": 200, "milk": 100, "coffee beans": 12, "cost": 6}
    }

    def __init__(self, water=0, milk=0, coffee_beans=0, cups=0, earnings=0):
        self.supplies = {
            "water": [water, "ml"],
            "milk": [milk, "ml"],
            "coffee beans": [coffee_beans, "g"]
        }
        self.cups = cups
        self.earnings = earnings

    def buy(self, coffe_type):
        for supply, value in self.complete_menu[coffe_type].items():
            if supply == "cost":
                continue
            if self.supplies[supply][0] < value:
                print(f"Sorry, not enough {supply}!")
                return
        if self.cups == 0:
            print("Sorry, not enough cups!")
            return
        for supply, value in self.complete_menu[coffe_type].items():
            if supply == "cost":
                continue
            self.supplies[supply][0] -= value
        self.cups -= 1
        self.earnings += self.complete_menu[coffe_type]["cost"]
        print("I have enough resources, making you a coffee!")

    def take(self):
        print(f"I gave you ${self.earnings}")
        self.earnings = 0

    def fill(self, item: str, amount: int = 0):
        if item in self.supplies:
            self.supplies[item][0] += amount
        elif item == "cups":
            self.cups += amount

    def __str__(self):
        info = f"The coffee machine has:\n"
        for key, value in self.supplies.items():
            info += f"{value[0]} {value[1]} of {key}\n"
        info += f"{self.cups} disposable cups\n"
        info += f"${self.earnings} of money"
        return info

machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    match input():
        case "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            if (order := input()) == "back":
                continue
            else:
                machine.buy(order)
        case "fill":
            for key, value in machine.supplies.items():
                print(f"Write how many {value[1]} of {key} you want to add:")
                machine.fill(key, int(input()))
            print("Write how many disposable cups you want to add:")
            machine.fill("cups", int(input()))
        case "take":
            machine.take()
        case "remaining":
            print(machine)
        case "exit":
            break
    print()
