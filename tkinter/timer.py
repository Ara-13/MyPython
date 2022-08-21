from tkinter import *
from datetime import datetime as dt
from time import sleep
def stop_timer():
    timer.config(text="00:00:00")
    start_btn.config(text="شروع", command=start_timer)
    raise SystemExit()
def second_timer(H, M, S):
    for i in range(S, -1, -1):
        sleep(1)
        app.update()
        timer.config(text="%.2d:%.2d:%.2d" % (H, M, i))
def start_timer():
    start_btn.config(text="توقف", command=stop_timer)
    s = int(second.get())
    m = int(minute.get())
    h = int(hour.get())
    timer.config(text="%.2d:%.2d:%.2d" % (h, m, s))
    second_timer(h, m, s)
    while True:
        if m != 0:
            s = 59
            m -= 1
            second_timer(h, m, 59)
        elif h != 0:
            h -= 1
            m = 59
            s = 59
            second_timer(h, 59, 59)
        else:
            timer.config(text="00:00:00")
            start_btn.config(text="شروع", command=start_timer)
            break
app = Tk()
app.title("تایمر من")
Label(text=":ثانیه", font=('Shabnam FD', 10), justify="center").grid(row=0, column=2)
second = Spinbox(from_=0,to=60, font=('Shabnam FD', 15), justify="center", width=10)
second.grid(row=1, column=2)
Label(text=":دقیقه", font=('Shabnam FD', 10), justify="center").grid(row=0, column=1)
minute = Spinbox(from_=0, to=60, font=('Shabnam FD', 15), justify="center", width=10)
minute.grid(row=1, column=1)
Label(text=":ساعت", font=('Shabnam FD', 10), justify="center").grid(row=0, column=0)
hour = Spinbox(from_=0, to=99, font=('Shabnam FD', 15), justify="center", width=10)
hour.grid(row=1, column=0)

timer = Label(text="00:00:00", font=('Shabnam FD', 20), justify="center")
timer.grid(row=2, column=0, columnspan=3)

start_btn = Button(text="شروع", font=('Shabnam FD', 15), justify="center", width=30, borderwidth=0, bg="#282a35",
                   fg="white",
                   command=start_timer)
start_btn.grid(row=3, column=0, columnspan=3)

app.geometry('335x200')
app.resizable(width=False, height=False)
app.mainloop()