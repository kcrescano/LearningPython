class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550

    def initialize():
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): ")
            if action == "buy":
                CoffeeMachine.buy()
            elif action == "fill":
                CoffeeMachine.fill()
            elif action == "take":
                CoffeeMachine.take()
            elif action == "remaining":
                CoffeeMachine.print_state()
            elif action == "exit":
                exit()
    
    def print_state():
        print("The coffee machine has:")
        print(CoffeeMachine.water, "ml of water")
        print(CoffeeMachine.milk, "ml of milk")
        print(CoffeeMachine.coffee_beans, "g of coffee beans")
        print(CoffeeMachine.disposable_cups, "disposable cups")
        print(f"${CoffeeMachine.money} of money")

    def buy():
        item = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if item == '1':
            if CoffeeMachine.check_resource(item) == '':
                CoffeeMachine.water -= 250
                CoffeeMachine.coffee_beans -= 16
                CoffeeMachine.money += 4
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.disposable_cups -= 1
            else:
                print(CoffeeMachine.check_resource(item))
        elif item == '2':
            if CoffeeMachine.check_resource(item) == '':
                CoffeeMachine.water -= 350
                CoffeeMachine.milk -= 75
                CoffeeMachine.coffee_beans -= 20
                CoffeeMachine.money += 7
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.disposable_cups -= 1
            else:
                print(CoffeeMachine.check_resource(item))
        elif item == '3':
            if CoffeeMachine.check_resource(item) == '':
                CoffeeMachine.water -= 200
                CoffeeMachine.milk -= 100
                CoffeeMachine.coffee_beans -= 12
                CoffeeMachine.money += 6
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.disposable_cups -= 1
            else:
                print(CoffeeMachine.check_resource(item))
        elif item == "back":
            CoffeeMachine.initialize()
        
    def check_resource(item):
        resources = []
        if item == '1':
            resources = [CoffeeMachine.water - 250,
                        CoffeeMachine.milk,
                        CoffeeMachine.coffee_beans - 16]
        elif item == '2':
            resources = [CoffeeMachine.water - 350,
                        CoffeeMachine.milk - 75,
                        CoffeeMachine.coffee_beans - 20]
        elif item == '3':
            resources = [CoffeeMachine.water - 200,
                        CoffeeMachine.milk - 100,
                        CoffeeMachine.coffee_beans - 12]
        if resources[0] < 0:
            return "Sorry, not enough water!"
        elif resources[1] < 0:
            return "Sorry, not enough milk!"
        elif resources[2] < 0:
            return "Sorry, not enough coffee beans!"
        elif CoffeeMachine.disposable_cups == 0:
            return "Sorry, not enough disposable cups!"
        else:
            return ""
            
    def fill():
        water = int(input("Write how many ml of water you want to add:"))
        milk = int(input("Write how many ml of milk you want to add:"))
        coffee_beans = int(input("Write how many grams of coffee beans you want to add:"))
        disposable_cups = int(input("Write how many disposable cups you want to add:"))
        CoffeeMachine.water += water
        CoffeeMachine.milk += milk
        CoffeeMachine.coffee_beans += coffee_beans
        CoffeeMachine.disposable_cups += disposable_cups
        
    def take():
        print(f"I gave you ${CoffeeMachine.money}")
        CoffeeMachine.money = 0

CoffeeMachine.initialize()

# print("""Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!""")

# print("For 125 cups of coffee you will need:")
# print(f"{coffee_cups * 200} ml of water")
# print(f"{coffee_cups * 50} ml of milk")
# print(f"{coffee_cups * 15} g of coffee beans")

# coffee = min(water // 200, milk // 50, coffee_beans // 15)
# if coffee > coffee_cups:
#     print(f"Yes, I can make that amount of coffee (and even {coffee - 1} more than that)")
# elif coffee == coffee_cups:
#     print("Yes, I can make that amount of coffee")
# else:
#     print(f"No, I can make only {coffee} cups of coffee")
    
