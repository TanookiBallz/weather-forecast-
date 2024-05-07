from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder 
from datetime import datetime
import requests
import pytz
#search box
root = Tk()
root.title("Weather App")
root.geometry("1000x700+500+200")
root.resizable(False, False)

def getWeather():
 city=textfield.get()
 
 geolocator= Nominatim(user_agent="geoapiExercises")
 location= geolocator.geocode(city)
 obj = TimezoneFinder()
 result = obj.timezone_at(Lng=location.longitude,Lat=location.latitude)

 home=pytz.timezone(result)
 local_time=datetime.now(home)
 current_time=local_time.strftime("%I:%M %p")
 clock.config(text=current_time)
 name.config(text="CURRENT WEATHER")
 



search_image=PhotoImage(file="search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins", 25, "bold"),border=0, fg="blue")
textfield.place(x=70,y=34)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2")
myimage_icon.place(x=435,y=26.5)

#logo
Logo_image=PhotoImage(file="Logo.png")
Logo=Label(image=Logo_image)
Logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=3,pady=3,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=60,y=150)
clock=Label(root,font=("Helvetica", 20))
clock.place(x=60,y=190)


#label
label1=Label(root,text="WIND", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label1.place(x=160,y=605)

label2=Label(root,text="HUMIDITY", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label2.place(x=290,y=605)

label3=Label(root,text="DESCRIPTION", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label3.place(x=450,y=605)

label4=Label(root,text="PRESSURE", font=("Helvetica", 15, 'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=605)


t=Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)


w=Label(text="...", font=("arial", 20,),bg="#1ab5ef")
w.place(x=160,y=630)
h=Label(text="...", font=("arial", 20,),bg="#1ab5ef")
h.place(x=290,y=630)
d=Label(text="...", font=("arial", 20,),bg="#1ab5ef")
d.place(x=450,y=630)
p=Label(text="...", font=("arial", 20,),bg="#1ab5ef")
p.place(x=650,y=630)

root.mainloop()
