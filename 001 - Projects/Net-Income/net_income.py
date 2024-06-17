# Write your code here
income = {"Bubblegum": 202,
          "Toffee": 118,
          "Ice cream": 2250,
          "Milk chocolate": 1680,
          "Doughnut": 1075,
          "Pancake": 80,}

print("Earned amount:")
for item in income.items():
    print(f"{item[0]}: ${item[1]}")
print(f"Income: ${sum(income.values())}")

expenses = (int(input("Staff expenses: ")),
            int(input("Other expenses: ")),)

print(f"Net income: ${sum(income.values()) - sum(expenses)}")
