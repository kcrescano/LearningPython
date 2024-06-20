# write your code here
import os.path
import sys

directory = sys.argv[1]
list_files = []

if os.path.isfile(directory):
    list_files.append(directory)
else:
    for f in os.listdir(directory):
        list_files.append(f'{directory}\\{f}')

for file in list_files:
    with open(file, 'r') as f:
        blank_line = 0
        for line, code in enumerate(f.readlines(), start=1):
            if not code.strip():
                blank_line += 1
                continue

            if len(code) > 79:
                print(f'{file}: Line {line}: S001', 'Too long')

            if (len(code) - len(code.lstrip())) % 4 != 0:
                print(f'{file}: Line {line}: S002', 'Indentation is not a multiple of four')

            if code.split("#")[0].strip().endswith(';'):
                print(f'{file}: Line {line}: S003', 'Unnecessary semicolon')

            if '#' in code and not code.startswith('#') and len(code.split('  #')) == 1:
                print(f'{file}: Line {line}: S004', 'At least two spaces required before inline comments')

            if '#' in code and 'todo' in code.split('#')[1].lower():
                print(f'{file}: Line {line}: S005', 'TODO found')

            if blank_line > 2:
                print(f'{file}: Line {line}: S006', 'More than two blank lines used before this line')
            blank_line = 0

            syntax = code.strip().split()
            if syntax[0] in ['class', 'def'] and code.strip() != ' '.join(syntax).strip():
                print(f'{file}: Line {line}: S007', f"Too many spaces after '{syntax[0]}'")

            if syntax[0] == 'class' and not syntax[1][0].istitle():
                print(f'{file}: Line {line}: S008', f"Class name '{syntax[1]}' should be written in CamelCase")

            if syntax[0] == 'def' and syntax[1][0].istitle():
                print(f'{file}: Line {line}: S009', f"Function name '{syntax[1]}' should use snake_case")

            if syntax[0] == 'def' and '=' in code:
                for param in syntax:
                    if '=' in param:
                        var = param.split('=')[0]
                        if var.istitle():
                            print(f'{file}: Line {line}: S010', f'Argument name {var} should be written in snake_case')

            if syntax[0] != 'def' and '=' in code and syntax[0].istitle():
                print(f'{file}: Line {line}: S011', f'Variable {syntax[0]} should be written in snake_case')

            if syntax[0] == 'def' and '=[]' in code:
                print(f'{file}: Line {line}: S012', 'The default argument value is mutable')
