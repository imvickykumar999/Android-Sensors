
# http://192.168.0.102:8080/sensors.json
# https://pythonprogramming.net/live-graphs-matplotlib-tutorial/

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

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


r'''
# https://stackoverflow.com/a/39215746/11493297

C:\Users\Vicky\Desktop\Repository\Android-Sensors>
adb shell

a21s:/ $ getevent -S
add device 1: /dev/input/event0
  name:     "meta_event"
add device 2: /dev/input/event4
  name:     "grip_sensor"
add device 3: /dev/input/event5
  name:     "grip_sensor_sub"
add device 4: /dev/input/event2
  name:     "s2mpu12-power-keys"
add device 5: /dev/input/event6
  name:     "AUD3004X Headset Input"
add device 6: /dev/input/event1
  name:     "gpio_keys"
add device 7: /dev/input/event3
  name:     "sec_touchscreen"
'''
