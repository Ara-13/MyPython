from tkinter import *
import requests

app = Tk()
app.title('UserInfo')
app.config(bg="#282A35")
frame1 = Frame(app, bg="#282A35", width=100)
frame1.pack(ipady=3)

def show_info(IP):
    location_url = 'https://ipapi.co/'
    location_response = requests.get(location_url+IP+'/json/')
    location_info = location_response.json()
    row_k = 3
    row_v = 3
    for k, v in location_info.items():
        Label(frame1, text=k+': ', font=('sanserif', 10), width=20, bg="#3A3D4E", fg="white").grid(column=0, row=row_k, pady=1)
        Label(frame1, text=v, bg="white", fg="black", width=40).grid(column=1, row=row_v)
        row_k += 1
        row_v += 1

def search_for_ip():
    ip = ip_input.get()
    frame1.grid_forget()
    show_info(ip)

Label(frame1, text='Enter Your IP:', bg="#4b4b68", fg="white", justify=CENTER).grid(column=0, row=0, columnspan=3)
ip_input = Entry(frame1, width=15, justify=CENTER, fg="#3A3D4E", font=('sanserif', 20))
ip_input.grid(column=0, row=1, columnspan=3)
Button(frame1, text="Find...", bg="#4b4b68", fg="white", activebackground="#6b6b94",activeforeground="white",
       width=10, justify=CENTER, font=('sanserif', 15),
       borderwidth=0 ,command=search_for_ip).grid(column=0, row=2, columnspan=3)

ip_url = 'https://api64.ipify.org/?format=json'
response = requests.get(ip_url)

if response.status_code == 200:
    show_info(response.json()['ip'])
else:
    Label(text="{0} Error...".format(response.status_code)).grid(column=0, row=3, columnspan=3)
app.geometry('450x745')
app.resizable(width=False, height=False)
app.mainloop()