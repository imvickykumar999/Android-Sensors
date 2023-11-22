
# http://192.168.0.102:8080/sensors.json
# https://pythonprogramming.net/live-graphs-matplotlib-tutorial/

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# https://matplotlib.org/stable/gallery/style_sheets/fivethirtyeight.html
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
