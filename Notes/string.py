string_ = '' or "" or """ """  # last one is for multi-line

# string formating
name = 'John'
age = 20
# An old-fashioned way of formatting from C language
print('Hi, my name is %s, I am %i years old!' % (name, age))
# Old-style rounding of decimals
print('%.3f' % (11 / 3))  # 3.667
print('%.2f' % (11 / 3))  # 3.67

# a more modern formatting method
print('Hi, my name is {}, I am {} years old!'.format(name, age))
# prints 'Strangers in the Night by Frank Sinatra'
print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
# prints 'Night in the Strangers by Frank Sinatra'
print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))

# string literals
print(f'Hi, my name is {name}, I am {age} years old!')
# Decimal number rounded to 1 decimal place: 291.7
print(f'Decimal number rounded to 1 decimal place: {decimal_number:.1f}')
