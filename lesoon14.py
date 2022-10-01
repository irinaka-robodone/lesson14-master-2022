import tkinter as tk
from datetime import datetime

def f(event):
    root.destroy()

def time():
    now=datetime.now()
    s = "{0:0>2d}:{1:0>2d}:{2:0>2d}".format(now.hour,now.minute,now.second)
    canvas.itemconfig("mytext",text=s)
    root.after(100,time)

root =  tk.Tk()
frame=tk.Frame(root)
root.title("あなたに時を告げる")
button=tk.Button(frame,text = "close")
button.grid(row=0,column=10,padx=5)
button.bind("<Button-1>",f)
canvas = tk.Canvas(frame, bg = 'white', width = 200, height = 100)
canvas.grid(row = 1,columnspan = 11,rowspan = 1)

frame.pack()

canvas.create_text(100,50,text =" ",font=("Gothic",15),tags ="mytext")

time()
root.mainloop()