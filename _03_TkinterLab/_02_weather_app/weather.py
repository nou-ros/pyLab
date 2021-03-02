import tkinter as tk
from tkinter import font
import requests 

root = tk.Tk()

Height=500
Width=600

def btn_function(entry):
    print("this is the entry: ", entry)

#676b60e0b542d88c3edc7759697faf20 key
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


def format_response(weather):
    # print(weather)
    try: 
        name= weather['name']
        desc= weather['weather'][0]['description']
        temp=weather['main']['temp']

        #  final_str = str(name) + ' ' + str(desc) + ' ' + str(temp)
        final_str = 'City %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except: 
        final_str = "There was a problem"

    return final_str

def get_weather(city):
    weather_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID' : weather_key, 'q': city, 'units' : 'metric'}
    response= requests.get(url, params=params)
    # print(response.json())
    weather=response.json()

    label['text'] = format_response(weather)




canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

background_img= tk.PhotoImage(file='env.png')
background_label = tk.Label(root, image=background_img)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#3399ff", bd=5)
frame.place(relx=.5, rely=0.1, relwidth=.75, relheight=.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 15))
entry.place(relwidth=.65, relheight=1)

button = tk.Button(frame, text="Get weather", font=('Courier', 10), command=lambda:get_weather(entry.get()))
button.place(relx=.7, relwidth=.30, relheight=1)

lower_frame= tk.Frame(root, bg="#3399ff", bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 15))
label.place(relwidth=1, relheight=1)


# print(tk.font.families())
root.mainloop()