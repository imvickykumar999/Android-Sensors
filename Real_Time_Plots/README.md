
> ## This is code to read Android sensor data via ip webcam app, [`explain it`](https://chat.openai.com/share/8355a70a-8249-4261-8ca6-322d358ae660).
>
> This Python script appears to be a simple program to read and visualize Android sensor data using the IP Webcam app. Here's an explanation of the code:

<br>

1. **Importing Libraries:**
    - `matplotlib.animation`: Used for creating animated plots.
    - `matplotlib.pyplot`: A plotting library for creating static, animated, and interactive visualizations.
    - `datetime`: Provides functions to work with dates and times.
    - `style`: Matplotlib style module for setting the style of the plots.
    - `requests`: Library for making HTTP requests.
    - `json`: Used for JSON serialization and deserialization.

```python
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import style
import requests, json
```

2. **Function `convert(ts)`:**
   - Converts a timestamp in milliseconds to a formatted string in the format 'YYYY-MM-DD HH:mm:SS'.
   - It divides the timestamp by 1000 to convert it from milliseconds to seconds and then uses `datetime.utcfromtimestamp` to get a UTC time object.

```python
def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili
```

3. **Setting up IP Webcam credentials and link:**
   - Defines the IP Webcam credentials (username and password) and the IP address with port for the sensors JSON data.

```python
username = 'imvickykumar999'
password = 'imvickykumar999'

ip, port = '192.168.0.102', 8080
link = f"http://{ip}:{port}/sensors.json"
```

4. **Matplotlib Setup:**
   - Sets the style for the plots using `style.use('fivethirtyeight')`.
   - Creates a figure and a subplot for the animation.

```python
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
```

5. **Downloading and Saving Sensor Data:**
   - Tries to download sensor data using the provided link and credentials. If successful, it saves the data to a JSON file named 'sensor.json'. If unsuccessful, it reads the data from the existing 'sensor.json' file.

```python
sensor = {}
filename = 'sensor.json'

try:
    r = requests.get(link, auth=(username, password))
    data = r.json()

    with open(filename, 'w') as outfile: 
        json.dump(data, outfile)
except:
    with open(filename, 'r') as f: 
        data = json.load(f)
```

6. **Mapping Sensor Names to Numbers:**
   - Maps the sensor names to their corresponding numbers and prints them.

```python
for i, j in enumerate(data.keys()):
    print(i, j)
    sensor.update({i: j})
```

7. **User Input for Sensor Selection:**
   - Takes user input for selecting a sensor by its number.

```python
inp = input('\nEnter sensor number : ')
if inp == '':
    inp = 0
else:
    inp = int(inp)
```

8. **Animation Function (`animate`):**
   - Uses the Matplotlib animation to continuously update the plot with new sensor data.
   - Downloads the latest sensor data, extracts relevant information, and updates the plot.

```python
def animate(k):
    try:
        # Fetches the latest sensor data
        r = requests.get(link, auth=(username, password))
        data = r.json()

        xs, ys = [], []
        keys = data[sensor[inp]]

        # Extracts data points and prints them
        for i in keys['data']:
            print(
                format(i[1][0], ".5f"), 
                keys['unit'], 
                '\t', 
                convert(int(i[0]))
            )
            xs.append(float(i[0]))
            ys.append(float(i[1][0]))

        # Clears the subplot and updates the plot
        ax1.clear()
        ax1.plot(xs, ys)
        ax1.set_ylim(-50, 50)

        # Sets plot title and saves the plot as an image
        plt.title(' '.join(sensor[inp].title().split('_')))
        plt.savefig(f"static/{sensor[inp]}.png")
        return fig
    
    except Exception as e:
        # Handles exceptions and exits the program
        print('\nPress CTRL+PAUSE/BREAK to exit.\n', e)
        plt.savefig(f"static/{sensor[inp]}.png")
        exit()
```

9. **Main Execution:**
   - Displays the selected sensor's graph using Matplotlib's `FuncAnimation`.

```python
print(f'Graph of {sensor[inp]}')
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
```

10. **Sample Output:**
    - Displays the available sensors and prompts the user to select a sensor. It then continuously updates and displays the graph of the selected sensor.

This script is meant to run in a Python environment and interact with an Android device running the IP Webcam app to visualize sensor data in real-time.

<br>

![rot_vector](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/2fa50fe6-1e35-4009-8e3d-9eec602b3483)
![proximity](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/5bf043ce-f434-4185-8c3e-e07c9af412ca)
![mag](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/6ae3c745-af0e-46e2-900f-22d74d83ab63)
![lin_accel](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/ddd9e4d9-e248-4244-9051-7155730b33fb)
![gyro](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/e37a20c3-2769-4984-a1f3-67aa945eebcc)
![gravity](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/086d2d37-b036-4f32-a536-9b8d7642551e)
![battery_voltage](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/c92ace71-b316-48c8-a0b4-3081b97a5e61)
![battery_temp](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/ec2027fe-851e-471f-9aeb-b11d6d86f131)
![battery_level](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/9e81f2ac-911c-4ae0-b43b-9d43fe97087b)
![battery_charging](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/c165525c-ea1a-46f1-9502-eff350ee79c5)
![accel](https://github.com/imvickykumar999/Android-Sensors/assets/50515418/cfb50d2f-759f-4c7b-8268-a78a201a4d31)
