
import json
from datetime import datetime

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

filename = 'sensor.json'
with open(filename, 'r') as f: 
    data = json.load(f)

for n in data.keys():
    title = '. '.join(n.title().split('_'))
    input(f'\n>>> Press ENTER to see "{title}"')

    print('-'*44, end='\n\n\t')
    print(f"{title} [{len(data[n]['data'])}]", end='\n')

    keys = data[n]
    try:
        keys['desc']
    except:
        keys['desc'] = [n]

    for i, k in enumerate(keys['data']):
        print('\n', i+1, ').  Time =', convert(k[0]))
        for m, o in enumerate(k[-1]):
            print('\t', keys['desc'][m], '=', format(o, ".4f"), keys['unit'])


'''
    Time       = 2023-11-23 08:11:34
    x*sin(θ/2) = 0.7063
    y*sin(θ/2) = -0.0637
    z*sin(θ/2) = -0.6990
    cos(θ/2)   = 0.0922
    Accuracy   = 0.0000
'''
