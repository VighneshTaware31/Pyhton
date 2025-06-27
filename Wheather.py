from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import tkinter.font as tkfont
from datetime import datetime
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
import requests
import pytz

#Window Size
root = Tk()
root.title("Weather App")   
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
     city = textfield.get()


     geolocator = Nominatim(user_agent="weatherAppVighnesh")
     location = geolocator.geocode(city)
     obj = TimezoneFinder()
     result = obj.timezone_at(lng =location.longitude, lat = location.latitude)

     home = pytz.timezone(result)
     local_time=datetime.now(home)
     current_time=local_time.strftime("%I:%M %p")
     clock.config(text=current_time)
     name.config(text="CURRENT WEATHER")

     #wheather
     api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=68aab4a84771f79397772fc244df58b3"

     json_data = requests.get(api).json()
     condition = json_data['weather'][0]['main']
     description = json_data['weather'][0]['description']
     temp = int(json_data['main']['temp']-273.15)
     humidity = json_data['main']['humidity']
     wind = json_data['wind']['speed']
     pressure = json_data['main']['pressure']

     t.config(text=(temp, "°C"))
     c.config(text=(condition,"|", "FEELS", "LIKE", temp,"°C"))

     w.config(text=wind)
     h.config(text=humidity)
     d.config(text=description)
     p.config(text=pressure)

    except Exception as e:
     messagebox.showerror("Weather app", "Invalid Entry !!")

    

#Search Box
search_image = PhotoImage(file="Copy of search.png")
myimage=Label(image=search_image)
myimage.place(x=30, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poopins", 25, "bold"),bg="#404040", border=0, fg="black")
textfield.place(x=70, y=40)
textfield.focus()

#search icon

seach_icon = PhotoImage(file = "Copy of search_icon.png")
myimage_icon = Button(image = seach_icon, borderwidth=0,bg="#404040", cursor="hand2", command=getWeather)
myimage_icon.place(x= 400, y = 32)

#Logo
logo_image = PhotoImage(file="Copy of logo.png")
myimage_logo = Label(image=logo_image)
myimage_logo.place(x= 100, y = 130)

#Bottom Box
frame_image=PhotoImage(file="Copy of box.png")
myimage_frame=Label(image=frame_image)
myimage_frame.pack(padx=5, pady=5, side=BOTTOM)

#time
name = Label(root, font=("arial", 15, "bold"))
name.place(x= 30, y = 100)
clock=Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)


#labels in bottom
label1 = Label(root, text = "Wind", font=("Helvetica", 15, 'bold'), fg="white", bg= "#00BFFF")
label1.place(x= 120, y = 400)

label1 = Label(root, text = "Humidity", font=("Helvetica", 15, 'bold'), fg="white", bg="#00BFFF")
label1.place(x= 250, y = 400)

label1 = Label(root, text = "Description", font=("Helvetica", 15, 'bold'), fg="white", bg="#00BFFF")
label1.place(x= 450, y = 400)

label1 = Label(root, text = "Pressure", font=("Helvetica", 15, 'bold'), fg="white", bg="#00BFFF")
label1.place(x= 650, y = 400)

t = Label(font=("arial", 70, "bold"))
t.place(x=400, y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400, y=250)

w=Label(text="---", font=("arial",10,'bold'), bg="#00BFFF")
w.place(x=140, y=440)
h=Label(text="---", font=("arial",10,'bold'), bg="#00BFFF")
h.place(x=290, y=440)
d=Label(text="---", font=("arial",10,'bold'), bg="#00BFFF")
d.place(x=480, y=440)
p=Label(text="---", font=("arial",10,'bold'), bg="#00BFFF")
p.place(x=680, y=440)

root.mainloop()