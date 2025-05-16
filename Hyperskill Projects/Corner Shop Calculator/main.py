# Write your code here
earning = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice Cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80, }

print("Earned amount:")
for item, amount in earning.items():
    print(f"{item}: ${amount}")

print(f"\nIncome: {(income := sum(earning.values()))}")
staff_expenses = int(input("Staff expenses:\n"))
other_expenses = int(input("Other expenses:\n"))
print(f"Net income: ${income - staff_expenses - other_expenses}")
