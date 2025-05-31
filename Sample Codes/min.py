# mine
coffee_recipe = {"water": [200, "ml"], 
                 "milk": [50, "ml"], 
                 "coffee_beans": [15, "grams"]}

for ingredient, info in coffee_recipe.items():
    print("Write how many", info[1], "of", ingredient, "the coffee machine has:")
    info.append(int(input()))
    
cups_need = int(input("Write how many cups of coffee you will need:\n"))
available_cups = 0
while all(map(lambda x: x[2] >= x[0], coffee_recipe.values())):
    coffee_recipe["water"][2] -= coffee_recipe["water"][0]
    coffee_recipe["milk"][2] -= coffee_recipe["milk"][0]
    coffee_recipe["coffee_beans"][2] -= coffee_recipe["coffee_beans"][0]
    available_cups += 1
    
if cups_need > available_cups:
    print("No, I can make only", available_cups, "cup(s) of coffee")
else:
    print("Yes, I can make that amount of coffee", end="")
    print(f" (and even {available_cups - cups_need} more than that)" * bool(available_cups - cups_need))
  
# Hyperskill
def ingredient(what, unit):
    return int(input(f'Write how many {unit} of {what} the coffee machine has:'))
    
water = ingredient('water', 'ml')
milk = ingredient('milk', 'ml')
coffee_beans = ingredient('coffee beans', 'grams')
cups = int(input('Write how many cups of coffee you will need:'))

max_cups = min(water // 200, milk // 50, coffee_beans // 15)

m = f'No, I can make only {max_cups} cups of coffee'
if cups <= max_cups:
    m = 'Yes, I can make that amount of coffee'
    if cups < max_cups:
        m = f'{m} (and even {max_cups - cups} more than that)'
        
print(m)
