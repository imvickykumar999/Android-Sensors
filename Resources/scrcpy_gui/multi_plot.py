
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import requests, json

username = 'imvickykumar999'
password = 'imvickykumar999'

ip, port = '192.168.0.102', 8080
link = f"http://{ip}:{port}/sensors.json"
style.use('fivethirtyeight')

def fetch_data():
    r = requests.get(link, auth=(username, password))
    filename = 'ScreenRecord/sensor.json'
    data = r.json()

    try:
        r = requests.get(link, auth=(username, password))
        data = r.json()

        with open(filename, 'w') as outfile: 
            json.dump(data, outfile)
    except:
        with open(filename, 'r') as f: 
            data = json.load(f)

    del data['battery_charging']
    del data['battery_voltage']
    del data['battery_level']
    del data['battery_temp']
    del data['rot_vector']
    del data['lin_accel']
    del data['proximity']
    del data['gravity']
    del data['gyro']
    return data

num_sensors = len(fetch_data())
fig, axs = plt.subplots(num_sensors, 1, figsize=(10, 5*num_sensors), sharex=True)

fig.tight_layout(pad=3.0)
colors = ['blue', 'green', 'red', 'purple']

def animate(k):
    data = fetch_data().items()

    for i, (sensor_name, sensor_data) in enumerate(data):
        xs, ys = [], []

        for entry in sensor_data['data']:
            xs.append(float(entry[0]))
            ys.append(float(entry[1][2]))

        axs[i].clear()
        axs[i].plot(xs, ys, color=colors[i])
        axs[i].set_title(sensor_name.title())

        axs[i].set_ylabel(sensor_data['unit'])
        axs[i].set_ylim(-75, 75)

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
