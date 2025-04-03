a, b = 1, 1
print(a is b)
# Python optimizes the use of small integers between -5 and 256.
a, b = 10000, 10000
print(a is b)  # True or False depending on your system
print(a == b)  # True, == compares value

def say_hello(name=None):
    if name is None:
        print('Hello!')
    else:
        print(f'Hello, {name}!')


say_hello()        # 'Hello!'
say_hello('Nick')  # 'Hello, Nick!'
