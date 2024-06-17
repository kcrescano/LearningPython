# Write your code here
import json

database = json.loads(input())

start_finish_stop, on_demand = [], []
for stop in database:
    if stop['stop_type'] in 'SF':
        on_demand.append(stop['stop_name'])
    if stop['stop_type'] == 'O':
        start_finish_stop.append(stop['stop_name'])

conflict = []
for stop in on_demand:
    if stop in start_finish_stop:
        conflict.append(stop)

print("On demand stops test:")
print(f"Wrong stop type: {sorted(conflict)}" if conflict else "OK")
