
from datetime import datetime
import json

filename = 'sensors.json'

with open(filename, 'r') as f:
    data = json.load(f)

keys = list(data.keys())
print()

for i, j in enumerate(keys):
    print(i, j)

battery_level = data[keys[9]]
print()

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

for i in battery_level['data']:
    print(i[1][0], battery_level['unit'], '@', convert(int(i[0])))


rf'''
>>> python analyse.py

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

77.0 % @ 2023-11-22 11:14:24
77.0 % @ 2023-11-22 11:14:26
77.0 % @ 2023-11-22 11:14:28
'''
