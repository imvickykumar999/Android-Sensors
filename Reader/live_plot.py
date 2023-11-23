
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import requests, json

username = 'imvickykumar999'
password = 'imvickykumar999'

ip,port = '192.168.0.102', 8080
link = f"http://{ip}:{port}/sensors.json"

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

try:
    r = requests.get(link, auth=(username, password))
    data = r.json()
except:
    with open('sensor.json', 'r') as f: 
        data = json.load(f)

sensor = {}
print()

for i, j in enumerate(data.keys()):
    print(i, j)
    sensor.update({i : j})

inp = input('\nEnter sensor number : ')
if inp == '':
    inp = 0
else:
    inp = int(inp)

def animate(k):
    try:
        r = requests.get(link, auth=(username, password))
        data = r.json()

        xs, ys = [], []
        keys = data[sensor[inp]]

        for i in keys['data']:
            xs.append(float(i[0]))
            ys.append(float(i[1][0]))

        ax1.clear()
        ax1.plot(xs, ys)
        ax1.set_ylim(-50, 50)

        plt.savefig(f"static/{sensor[inp]}.png")
        return fig
    except: 
        plt.savefig(f"static/{sensor[inp]}.png")
        exit()

print(f'Graph of {sensor[inp]}')
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()


rf'''
>>> python live_plot.py

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

Enter sensor number : 0
Graph of accel
'''
