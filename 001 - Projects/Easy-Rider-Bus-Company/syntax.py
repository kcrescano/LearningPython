# Write your code here
import json
import re

database = json.loads(input())
datatype = {'stop_name': r'[A-Z]\w+ ([A-Z]\w+ )?(Road|Avenue|Boulevard|Street)',
            'stop_type': r'[SOF]?',
            'a_time': r'[012]\d:[0-5]\d'}
errors = dict.fromkeys(datatype, 0)

for stop in database:
    for field in datatype.keys():
        if not re.fullmatch(datatype[field], stop[field]):
            errors[field] += 1

print(f'Format validation: {sum(errors.values())} errors')
for field, error in errors.items():
    print(f"{field}:", error)
