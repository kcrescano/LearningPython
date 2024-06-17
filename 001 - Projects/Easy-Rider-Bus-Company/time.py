# Write your code here
import json

database = json.loads(input())
bus_lines = {}
time_test = {}

for line in database:
    bus_id = line['bus_id']
    bus_lines[bus_id] = bus_lines.get(bus_id, [])
    bus_lines[bus_id].append([line['a_time'], line['stop_name']])

for bus_id, stops in bus_lines.items():
    time = stops[0][0].split(':')
    hour, minute = int(time[0]), int(time[1])
    for a_time in stops:
        time = a_time[0].split(':')
        hour_, minute_ = int(time[0]), int(time[1])
        if hour_ > hour:
            hour = hour_
            minute = minute_
            ok = False
        elif hour_ == hour and minute_ >= minute:
            hour = hour_
            minute = minute_
            ok = False
        else:
            ok = True
        if ok:
            if bus_id not in time_test:
                time_test[bus_id] = time_test.get(bus_id, '')
                time_test[bus_id] = a_time[1]

print('Arrival time test:')
if time_test:
    for bus_id, stop_name in time_test.items():
        print(f"bus_id line {bus_id}: wrong time on station", stop_name)
else:
    print('OK')
