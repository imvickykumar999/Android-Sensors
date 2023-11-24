
import json
from datetime import datetime

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

filename = 'sensor.json'
with open(filename, 'r') as f: data = json.load(f)

for j in data.keys():
    title = '. '.join(j.title().split('_'))
    input(f'\n>>> >>> Press ENTER to see "{title}"')

    print('-'*44, end='\n\n\t')
    print(f"{title} [{len(data[j]['data'])}]", end='\n\n')

    keys = data[j]
    for j, i in enumerate(keys['data']):
        print(f'{j+1}). ',
            format(i[1][0], ".5f"), 
            keys['unit'], 
            '\t', 
            convert(int(i[0]))
        )


rf'''
>>> python fetch_sensor.py

>>> Press ENTER to see "Accel"
.
.
.
>>> Press ENTER to see "Battery. Level"
--------------------------------------------

        Battery. Level [3]

1).  18.00000 %          2023-11-23 08:11:34
2).  18.00000 %          2023-11-23 08:11:36
3).  18.00000 %          2023-11-23 08:11:38

>>> Press ENTER to see "Battery. Temp"
--------------------------------------------

        Battery. Temp [3]

1).  29.50000 ℃          2023-11-23 08:11:34
2).  29.50000 ℃          2023-11-23 08:11:36
3).  29.50000 ℃          2023-11-23 08:11:38
'''
