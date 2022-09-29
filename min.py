import tkinter as tk
from datetime import datetime

def f_close(event):
    root.destroy()

def check_time():
    now = datetime.now()
    s="{0:0>2d}:{1:0>2d}:{2:0>2d}".format(now.hour,now.minute,now.second)
    canvas.itemconfig("mytext",text = s)
    root.after(100,check_time)

root = tk.Tk()
frame =tk.Frame(root)

button = tk.Button(frame,text="Close")
button.grid(row=0,column=10,padx=5)
button.bind("<Button-1>",f_close)

canvas = tk.Canvas(frame,bg="white",width=100,height=50)
canvas.grid(row=1,columnspan=11,rowspan=1)

frame.pack()

canvas.create_text(50,25,text=" ",font=("Gothic",10),tags = "mytext")

check_time()

root.mainloop()

