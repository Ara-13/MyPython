from datetime import datetime as dt
from tkinter import *
from time import sleep

stop_progress = False
def start():
    stop_btn.config(text="S T O P", command=stop)
    clock.config(fg="#282a35")
    global stop_progress
    stop_progress = False
    clk()

def stop():
    stop_btn.config(text="S T A R T", command=start)
    global stop_progress
    stop_progress = True

window = Tk()
window.title("CLOCK")
window.geometry('300x200')

clock = Label(text="%.2d : %.2d : %.2d" % (dt.today().hour, dt.today().minute, dt.today().second),
              font=('Blanka', 25), fg="#282a35")
clock.pack(expand=True)
stop_btn = Button(text="S T O P",
                  font=('Blanka', 15),
                  fg="#fff",
                  bg="#282a35",
                  borderwidth=0,
                  width=30,
                  justify="center",
                  activebackground="#3A3D4E",
                  activeforeground="#fff",
                  command=stop)

stop_btn.pack(expand=True)


def clk():
    while True:
        clock.config(text="%.2d : %.2d : %.2d" % (dt.today().hour, dt.today().minute, dt.today().second))
        sleep(1)
        window.update()

        if stop_progress is True:
            clock.config(fg="red")
            break
    return

clk()
window.resizable(width=False, height=False)
window.mainloop()
