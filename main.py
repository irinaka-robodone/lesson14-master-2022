from cgitb import text
from logging.handlers import RotatingFileHandler
import mailbox
import tkinter as tk
from datetime import datetime

#ボタンの設置
def f_close(event): #イベント引数
    root.destroy
    
#ボタンの設
def check_time():
    now = datetime.now()
    s = '{0:0>2d}:{1:0>2d}:{2:0>2d}.format(now.hour,now.minute, now.sesond) '
    canvas.itemconfig('mytext',text = s)
    root.after(100,check_time)
    
    
root = tk.Tk()#外枠
frame = tk.Frame(root)#中枠

#ボタンの設置
button = tk.Button(frame,text = 'Close')
button.grid(row = 0, column=10, padx=5)
button.bind('<Button-1>',f_close)

#キャンバスの設置f
canvas = tk.Canvas(frame,bg = 'white', width = 800,height=500)
canvas.grid(row = 1,columnspan= 11, rowspan=1)

frame.pack()
canvas.create_text(400,200,text='',font= ('Gothic',100),tags = 'mytext')

check_time()
root.mainloop()