# Comparison operators
# <, <=, >, >=, ==, !=, is, is not, in, not in
age = 30
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary
n = 1
num = "Even" if n % 2 == 0 else "Odd"
num = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
