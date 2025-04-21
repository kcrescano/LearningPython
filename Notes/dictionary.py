birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}
another_empty_dict = dict()  # using the dict constructor

# note that the future dictionary keys are listed without quotes
prices_with_constr = dict({'espresso': 5.0}, americano=8.0, latte=10, pastry='various prices')
print(prices_with_constr)  # {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}

my_pet = {}

# add 3 keys and their values into the dictionary
my_pet['name'] = 'Dolly'
my_pet['animal'] = 'dog'
my_pet['breed'] = 'collie'

print(my_pet)  # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}

# get information from the dictionary about an added item
print(my_pet['name'])  # Dolly

# our nested dictionary once again:
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

print(my_pets['cat'])  # {'name': 'Fluffy', 'breed': 'maine coon'}

print(my_pets['cat']['breed'])  # maine coon
