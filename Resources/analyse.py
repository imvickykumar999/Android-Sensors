
from datetime import datetime
import json

filename = 'sensors.json'

with open(filename, 'r') as f:
    data = json.load(f)

keys = list(data.keys())

for i, j in enumerate(keys):
    print(i, j)

print(data[keys[9]])

ts = int("1700651666606")
ts /= 1000
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


'''
0 accel
1 battery_charging
2 mag
3 gyro
4 proximity
5 gravity
6 lin_accel
7 rot_vector
8 battery_voltage
9 battery_level
10 battery_temp

{'unit': '%', 'data': [[1700651664604, [77.0]], [1700651666606, [77.0]], [1700651668609, [77.0]]]}

2023-11-22 11:14:24
'''
