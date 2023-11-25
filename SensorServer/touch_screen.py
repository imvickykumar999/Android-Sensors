
# https://github.com/umer0586/SensorServer/wiki/Controlling-Mouse-Using-SensorServer-App

import websocket
import json
from pynput.mouse import Controller

mouse = Controller()
speed = 1.3

old_x = 0
old_y = 0

def on_message(ws, message):

    global old_x
    global old_y
   
    data = json.loads(message)
    new_x , new_y = data['x'] , data['y']

    action = data['action']
    print(action)
    
    dx , dy = new_x - old_x , new_y - old_y
    old_x, old_y = new_x , new_y

    if action == "ACTION_MOVE":
        mouse.move(dx*speed,dy*speed)

def on_error(ws, error):
    print(error)

def on_close(ws, close_code, reason):
    print("connection close : ", reason)
    
def on_open(ws):
    print("connected")

def connect(url):
    ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()

connect("ws://192.168.0.102:8080/touchscreen")


'''
ACTION_MOVE
ACTION_UP
connection close :  Server stopped
'''
