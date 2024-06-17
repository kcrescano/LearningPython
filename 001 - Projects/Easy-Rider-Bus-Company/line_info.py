# Write your code here
import json

database = json.loads(input())
bus_lines = {}

for line in database:
    for field, data in line.items():
        if field == 'bus_id':
            bus_lines[data] = bus_lines.get(data, 0) + 1

print("Line names and number of stops:")
for bus_id, stops in bus_lines.items():
    print('bus_id:', bus_id, 'stops:', stops)
