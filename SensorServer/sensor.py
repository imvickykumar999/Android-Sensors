
# https://github.com/umer0586/SensorServer#example-websocket-client-python

from datetime import datetime
import websocket
import json

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

def on_message(ws, message):
    loading = json.loads(message)
    values = loading['values']
    t = loading['timestamp']

    x = values[0]
    y = values[1]
    z = values[2]
    # t = convert(t)
    print("x = ", x , "y = ", y , "z = ", z , "t = ", t)

def on_error(ws, error):
    print("error occurred ", error)
    
def on_close(ws, close_code, reason):
    print("connection closed : ", close_code, reason)
    
def on_open(ws):
    print("connected")

def connect(url):
    ws = websocket.WebSocketApp(url,
                              on_message=on_message,
                              on_open=on_open,
                              on_error=on_error,
                              on_close=on_close
                            )

    ws.run_forever()


connect("ws://192.168.0.102:8080/sensor/connect?type=android.sensor.accelerometer") 


'''
connection closed :  4004 Server stopped
'''
