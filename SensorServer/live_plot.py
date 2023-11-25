"""
Python code to show real time plot from live accelerometer's
data recieved via SensorServer app over websocket 

"""

from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import websocket
import json
import threading

#shared data
x_data = []
y_data = []
z_data = []
time_data = []

x_data_color = "#d32f2f"   # red
y_data_color = "#7cb342"   # green
z_data_color = "#0288d1"   # blue

background_color = "#fafafa" # white (material)


class Sensor:
    #constructor
    def __init__(self,address,sensor_type):
        self.address = address
        self.sensor_type = sensor_type
    
    # called each time when sensor data is recieved
    def on_message(self,ws, message):
        values = json.loads(message)['values']
        timestamp = json.loads(message)['timestamp']

        x_data.append(values[0])
        y_data.append(values[1])
        z_data.append(values[2])

        time_data.append(float(timestamp/1000000))

    def on_error(self,ws, error):
        print("error occurred")
        print(error)

    def on_close(self,ws, close_code, reason):
        print("connection close")
        print("close code : ", close_code)
        print("reason : ", reason  )

    def on_open(self,ws):
        print(f"connected to : {self.address}")

    # Call this method on seperate Thread
    def make_websocket_connection(self):
        ws = websocket.WebSocketApp(f"ws://{self.address}/sensor/connect?type={self.sensor_type}",
                                on_open=self.on_open,
                                on_message=self.on_message,
                                on_error=self.on_error,
                                on_close=self.on_close)

        # blocking call
        ws.run_forever() 
    
    # make connection and start recieving data on sperate thread
    def connect(self):
        thread = threading.Thread(target=self.make_websocket_connection)
        thread.start()           



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.graphWidget.setBackground(background_color)

        self.graphWidget.setTitle("Accelerometer Plot", color="#8d6e63", size="20pt")
        
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "15px"}
        self.graphWidget.setLabel("left", "m/s^2", **styles)
        self.graphWidget.setLabel("bottom", "Time (miliseconds)", **styles)
        self.graphWidget.addLegend()

        self.x_data_line =  self.graphWidget.plot([],[], name="x", pen=pg.mkPen(color=x_data_color))
        self.y_data_line =  self.graphWidget.plot([],[], name="y", pen=pg.mkPen(color=y_data_color))
        self.z_data_line =  self.graphWidget.plot([],[], name="z", pen=pg.mkPen(color=z_data_color))
      
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data) # call update_plot_data function every 50 milisec
        self.timer.start()

    def update_plot_data(self):
        
        # limit lists data to 1000 items 
        limit = -1000 

        # Update the data.
        self.x_data_line.setData(time_data[limit:], x_data[limit:])  
        self.y_data_line.setData(time_data[limit:], y_data[limit:])
        self.z_data_line.setData(time_data[limit:], z_data[limit:])


sensor = Sensor(address = "192.168.0.102:8080", sensor_type="android.sensor.accelerometer")
sensor.connect() # asynchronous call


app = QtWidgets.QApplication(sys.argv)

# call on Main thread
window = MainWindow()
window.show()
sys.exit(app.exec_())        
