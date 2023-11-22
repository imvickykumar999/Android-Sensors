
from tkinterweb import HtmlFrame
import tkinter as tk

root = tk.Tk()
frame = HtmlFrame(root)

username = 'imvickykumar999'
password = 'imvickykumar999'
ip = '192.168.0.102'
port = 8080

# url = f"http://{username}:{password}@{ip}:{port}/sensors.json"
url = 'https://pythonprogramming.net/live-graphs-matplotlib-tutorial/'
frame.load_website(url)

frame.pack(fill="both", expand=True)
root.mainloop()
