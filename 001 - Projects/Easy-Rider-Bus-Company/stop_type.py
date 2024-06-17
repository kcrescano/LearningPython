# Write your code here
import json

database = json.loads(input())
bus_lines = {}

for line in database:
    bus_id, stop_type = line['bus_id'], line['stop_type']
    bus_lines[bus_id] = bus_lines.get(bus_id, {'S': '', 'F': ''})
    if stop_type in ['S', 'F']:
        bus_lines[bus_id][stop_type] = line['stop_name']

for bus_id, line in bus_lines.items():
    if not line['S'] or not line['F']:
        print(f'There is no start or end stop for the line: {bus_id}.')
        exit()

start_stop, transfer_stop, finish_stop = [], [], []
for stop in database:
    transfer_stop.append(stop['stop_name'])
    if stop['stop_type'] == 'S':
        start_stop.append(stop['stop_name'])
    if stop['stop_type'] == 'F':
        finish_stop.append(stop['stop_name'])

for stop in set(transfer_stop):
    transfer_stop.pop(transfer_stop.index(stop))
transfer_stop = list(set(transfer_stop))
finish_stop = list(set(finish_stop))

print('Start stops:', len(start_stop), sorted(start_stop))
print('Transfer stops:', len(transfer_stop), sorted(transfer_stop))
print('Finish stops:', len(finish_stop), sorted(finish_stop))
