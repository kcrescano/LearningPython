# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]
even_numbers = [x for x in numbers if x % 2 == 0]  # [2, 4]

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
number_map = {x: x**2 for x in numbers}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set Comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}  # {1, 2, 3, 4, 5}

# Generator Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers_generator = (x**2 for x in numbers)
for num in squared_numbers_generator:
    print(num)  # Prints 1, 4, 9, 16, 25
