# function

def function(x, y):  # x and y are parameters
  return x + y
# returns a string
# opposite of void functions

def function():
  print()
# call print() and return None object
# similiar to void functions

print(function(x, y))  # invoking function, x and y here are arguments

def greet(name, surname):
    print("Hello,", name, surname)
# Non-keyword arguments
greet("Willy", "Wonka")               # Hello, Willy Wonka
# Keyword arguments
greet(surname="Wonka", name="Willy")  # Hello, Willy Wonka
# Keywords comes after non-key words
