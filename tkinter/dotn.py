from tkinter import *

one_dot_list = ['ب','ج','خ','ذ','ز','ض','ظ','غ','ف','ن','.', 'i', 'j']
two_dot_list = ['ت', 'ق', 'ي', 'ی']
three_dot_list = ['پ', 'ث', 'چ', 'ژ', 'ش']
def dot():
    counter = 0
    word = inp.get()
    for c in word:
        if c in one_dot_list:
            counter += 1
        elif c in two_dot_list:
            counter += 2
        elif c in three_dot_list:
            counter += 3
        else:
            pass

    result_label.config(text=" تعداد نقطه در عبارت شما: {}".format(counter))

window = Tk()
window.title("شمارشگر نقطه")
Label(window, text="سلام! یه کلمه بنویس تا بهت بگم چند تا نقطه داره", font=('Shabnam FD', 12)).pack()
inp = Entry(window, width=30, borderwidth=0, font=('Shabnam FD', 20), justify="center")
inp.pack(expand=True)
result_label = Label(window, text="", font=('Shabnam FD', 12))
result_label.pack()
Button(window, text="!بهم بگو", width=15, borderwidth=0, font=('Shabnam FD', 15), bg="#fcba03", command=dot).pack(expand=True)
window.geometry('400x300')
window.resizable(width=False, height=False)
window.mainloop()