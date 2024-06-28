"""
  Brute Forced: will redo in the future
"""

# write your code here
variables = {}
count = 0
while (parameter := input()) != '/exit':
    if parameter == '/help':
        print('The program calculates the sum of numbers')
    elif parameter.startswith('/'):
        print('Unknown command')
    elif '=' in parameter:
        try:
            key, value = parameter.split('=')
            if not key.strip().isalpha():
                print('Invalid identifier')
            elif value.strip().isdigit():
                variables[key.strip()] = int(value.strip())
            else:
                try:
                    variables[key.strip()] = variables[value.strip()]
                except KeyError:
                    print('Invalid assignment')
        except ValueError:
            print('Invalid assignment')
    elif parameter.strip().isalpha():
        try:
            print(variables[parameter.strip()])
        except KeyError:
            print('Unknown variable')
    elif parameter:
        try:
            temp = parameter
            parameter = parameter.split()
            # if parameter[0].isdigit():
            #     total = int(parameter[0])
            # else:
            #     total = variables[parameter[0]]

            for i in range(0, len(parameter)):
                if parameter[i] in ['++', '+++', '++++', '+++++', '--', '----']:
                    parameter[i] = '+'
                if parameter[i] in ['---', '-----']:
                    parameter[i] = '-'
                try:
                    if parameter[i] in variables.keys():
                        parameter[i] = str(variables[parameter[i]])
                except ValueError:
                    print('Invalid expression')
            if '//' in parameter:
                raise ValueError
            print(int(eval(' '.join(parameter))))
        except (ValueError, KeyError, SyntaxError):
            print('Invalid expression')
print('Bye!')

# if '(' in temp:
#     parentheses = temp.replace(')', '(').split('(')
#     temp_value = str(eval(parentheses[1]))
#     parentheses[1] = temp_value
#     parameter = ''.join(parentheses).split()
#
# for i in range(1, len(parameter), 2):
#     if parameter[i + 1].isdigit():
#         if '*' in parameter[i]:
#             total *= int(parameter[i + 1])
#         elif '/' in parameter[i]:
#             total /= int(parameter[i + 1])
#         elif '+' in parameter[i]:
#             total += int(parameter[i + 1])
#         elif '-' in parameter[i]:
#             if len(parameter[i]) % 2 == 0:
#                 total += int(parameter[i + 1])
#             else:
#                 total -= int(parameter[i + 1])
#     else:
#         if '*' in parameter[i]:
#             total *= variables[parameter[i + 1]]
#         elif '/' in parameter[i]:
#             total /= variables[parameter[i + 1]]
#         if '+' in parameter[i]:
#             total += variables[parameter[i + 1]]
#         elif '-' in parameter[i]:
#             if len(parameter[i]) % 2 == 0:
#                 total += variables[parameter[i + 1]]
#             else:
#                 total -= variables[parameter[i + 1]]
