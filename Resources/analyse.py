
from datetime import datetime
import json

filename = 'sensors.json'

with open(filename, 'r') as f:
    data = json.load(f)

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

for j in data.keys():
    print('-'*30, end='\n\n')
    print(' '.join(j.title().split('_')), end='\n\n')

    keys = data[j]
    for i in keys['data']:
        print(i[1][0], keys['unit'], '@', convert(int(i[0])))


rf'''
>>> python analyse.py

.
.
.

------------------------------

Battery Voltage

3.943 V @ 2023-11-22 11:14:24
3.943 V @ 2023-11-22 11:14:26
3.943 V @ 2023-11-22 11:14:28
------------------------------

Battery Level

77.0 % @ 2023-11-22 11:14:24
77.0 % @ 2023-11-22 11:14:26
77.0 % @ 2023-11-22 11:14:28
------------------------------

Battery Temp

29.1 ℃ @ 2023-11-22 11:14:24
29.1 ℃ @ 2023-11-22 11:14:26
29.1 ℃ @ 2023-11-22 11:14:28
'''
