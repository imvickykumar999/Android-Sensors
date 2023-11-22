
import requests, json, time
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

# while True:
time.sleep(0.5)
r = requests.get(link, auth=(username, password))
data = r.json()

with open('static/sensor.json', 'w') as outfile:
    json.dump(data, outfile)

for j in data.keys():
    print('-'*30, end='\n\n')
    print(' '.join(j.title().split('_')), end='\n\n')

    keys = data[j]
    for i in keys['data']:
        print(i[1][0], keys['unit'], '@', convert(int(i[0])))
