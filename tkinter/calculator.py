from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("ماشین حساب")
        self.geometry("350x307")
        self.resizable(width=False, height=False)
        self.result = 0
        self.last_operator = None

        #Label(self, text="سلام به اولین اپ من خوش آمدید", font=("Shabnam FD", 15), fg="blue").grid(row=0, column=0)
        #Label(self, text=":لطفا از اعداد زیر انتخاب کنید", font=("Shabnam FD", 10), fg="green").grid(row=0, column=1)

        self.show_label = Label(self, text="", font=("Shabnam FD", 15), height=2, width=32, bg="#d9d9d9")
        self.show_label.grid(row=0, column=0, columnspan=3)

        self.btn1 = Button(text="1", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed1)
        self.btn1.grid(row=1, column=0)

        self.btn2 = Button(text="2", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed2)
        self.btn2.grid(row=1, column=1)

        self.btn3 = Button(text="3", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed3)
        self.btn3.grid(row=1, column=2)

        self.btn4 = Button(text="4", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed4)
        self.btn4.grid(row=2, column=0)

        self.btn5 = Button(text="5", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed5)
        self.btn5.grid(row=2, column=1)

        self.btn6 = Button(text="6", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed6)
        self.btn6.grid(row=2, column=2)

        self.btn7 = Button(text="7", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed7)
        self.btn7.grid(row=3, column=0)

        self.btn8 = Button(text="8", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed8)
        self.btn8.grid(row=3, column=1)

        self.btn9 = Button(text="9", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed9)
        self.btn9.grid(row=3, column=2)

        self.btn0 = Button(text="0", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed0)
        self.btn0.grid(row=4, column=1)

        self.btn_dot = Button(text=".", fg="white", bg="black", width=10, font=("Shabnam FD", 15), command=self.btn_pushed0)
        self.btn_dot.grid(row=4, column=0)

        self.btn_remove = Button(text="E", fg="white", bg="gray", width=10, font=("Shabnam FD", 15), command=self.btn_remove)
        self.btn_remove.grid(row=4, column=2)

        self.btn_add = Button(text="+", fg="white", bg="green", width=10, font=("Shabnam FD", 15), command=self.btn_add)
        self.btn_add.grid(row=5, column=0)

        self.btn_minus = Button(text="−", fg="white", bg="green", width=10, font=("Shabnam FD", 15), command=self.btn_minus)
        self.btn_minus.grid(row=5, column=1)

        self.btn_show = Button(text="=", fg="white", bg="red", width=10, font=("Shabnam FD", 15), command=self.btn_show)
        self.btn_show.grid(row=5, column=2)

    def btn_pushed1(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"1")
        else:
            self.show_label.config(text="1")
    def btn_pushed2(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"2")
        else:
            self.show_label.config(text="2")
    def btn_pushed3(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"3")
        else:
            self.show_label.config(text="3")
    def btn_pushed4(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"4")
        else:
            self.show_label.config(text="4")
    def btn_pushed5(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"5")
        else:
            self.show_label.config(text="5")
    def btn_pushed6(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"6")
        else:
            self.show_label.config(text="6")
    def btn_pushed7(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"7")
        else:
            self.show_label.config(text="7")
    def btn_pushed8(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"8")
        else:
            self.show_label.config(text="8")
    def btn_pushed9(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"9")
        else:
            self.show_label.config(text="9")
    def btn_pushed0(self):
        if type(self.show_label["text"]) == str:
            self.show_label.config(text=self.show_label["text"]+"0")
        else:
            self.show_label.config(text="0")

    def btn_remove(self):
        *tx, _ = self.show_label["text"]
        self.show_label.config(text=''.join(tx))
    def btn_add(self):
        if self.last_operator is None:
            self.result += int(self.show_label["text"])
        elif self.last_operator == '+':
            self.result += int(self.show_label["text"])
        elif self.last_operator == '-':
            self.result -= int(self.show_label["text"])
        else:
            raise TypeError()
        self.show_label.config(text="")
        self.last_operator = '+'
    def btn_minus(self):
        if self.last_operator is None:
            self.result += int(self.show_label["text"])
        elif self.last_operator == '+':
            self.result += int(self.show_label["text"])
        elif self.last_operator == '-':
            self.result -= int(self.show_label["text"])
        else:
            raise TypeError()
        self.show_label.config(text="")
        self.last_operator = '-'
    def btn_show(self):
        if self.last_operator == '+':
            self.result += int(self.show_label["text"])
        elif self.last_operator == '-':
            self.result -= int(self.show_label["text"])
        else:
            self.show_label.config(text=self.result)
        self.show_label.config(text=self.result)
        self.result = 0
        self.last_operator = None
if __name__ == '__main__':
    app = App()
    app.mainloop()