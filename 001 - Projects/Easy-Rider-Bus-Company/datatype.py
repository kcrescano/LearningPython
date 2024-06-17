# Write your code here
import json

database = json.loads(input())
datatype = {'bus_id': int, 'stop_id': int, 'stop_name': str,
            'next_stop': int, 'stop_type': str, 'a_time': str}
errors = dict.fromkeys(datatype, 0)

for stop in database:
    for field, data in stop.items():
        if field == 'stop_type':
            if not isinstance(data, datatype[field]) or data not in 'SOF':
                errors[field] += 1
        elif (not data or not isinstance(data, datatype[field])) and data != 0:
            errors[field] += 1

print(f'Type and required field validation: {sum(errors.values())} errors')
for field, error in errors.items():
    print(f"{field}:", error)
