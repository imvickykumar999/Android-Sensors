
import requests, json
from datetime import datetime

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

username = 'imvickykumar999'
password = 'imvickykumar999'

ip,port = '192.168.0.102', 8080
link = f"http://{ip}:{port}/sensors.json"

r = requests.get(link, auth=(username, password))
data = r.json()

filename = 'sensor.json'
with open(filename, 'w') as outfile: json.dump(data, outfile)
# with open(filename, 'r') as f: data = json.load(f)

for j in data.keys():
    print('-'*30, end='\n\n')
    print(' '.join(j.title().split('_')), end='\n\n')

    keys = data[j]
    for i in keys['data']:
        print(i[1][0], keys['unit'], '@', convert(int(i[0])))
