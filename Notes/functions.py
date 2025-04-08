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

# Keywords comes after non-key words - def func(variable=value):
def greet(name, surname="Willy"): # parameters can have default value
    print("Hello,", name, surname)
# Non-keyword arguments
greet("Willy", "Wonka")               # Hello, Willy Wonka
# Keyword arguments
greet(surname="Wonka", name="Willy")  # Hello, Willy Wonka

# Args
def add(*args):
    total = 0
    for n in args:
        total += n
    return total
  
small_numbers = [1, 2, 3]
large_numbers = [9999999, 1111111]

print(add(*small_numbers))  # * unpack iterables
print(add(*large_numbers))
