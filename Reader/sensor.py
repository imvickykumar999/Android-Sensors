
from datetime import datetime
import urllib.request, json

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

username = 'imvickykumar999'
password = 'imvickykumar999'
ip = '192.168.0.102'
port = 8080

link = f"http://{username}:{password}@{ip}:{port}/sensors.json"
# print(link)

with urllib.request.urlopen(link) as url:
    data = json.loads(url.read().decode())
    print(data)

for j in data.keys():
    print('-'*30, end='\n\n')
    print(' '.join(j.title().split('_')), end='\n\n')

    keys = data[j]
    for i in keys['data']:
        print(i[1][0], keys['unit'], '@', convert(int(i[0])))


'''
urllib.error.URLError: <urlopen error [Errno 11003] getaddrinfo failed>
'''
