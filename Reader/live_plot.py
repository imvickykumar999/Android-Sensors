
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import requests

username = 'imvickykumar999'
password = 'imvickykumar999'

ip,port = '192.168.0.102', 8080
link = f"http://{ip}:{port}/sensors.json"

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

r = requests.get(link, auth=(username, password))
data = r.json()
print()

for i, j in enumerate(data.keys()):
    print(i, j)

def animate(k):
    r = requests.get(link, auth=(username, password))
    data = r.json()

    xs, ys = [], []
    keys = data['battery_level']

    for i in keys['data']:
        xs.append(float(i[0]))
        ys.append(float(i[1][0]))

    ax1.clear()
    ax1.plot(xs, ys)
    ax1.set_ylim(-50, 50)
    return fig

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
