from tkinter import *
import requests
from datetime import datetime

root = Tk()
root.geometry("400x400")

def tijd_locatie(tijdzone_utc):
    lokale_tijd = datetime.utcfromtimestamp(tijdzone_utc)
    return lokale_tijd.time()

stad_string = StringVar()

def hetWeer():
    api_key = '7debd9d053b48f147b667d058886207e'
    naam_stad = stad_string.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + naam_stad + '&appid=' + api_key

    response = requests.get(weather_url)

    weer_info = response.json()

    tfield.delete("1.0", "end")

    if weer_info['cod'] == 200:
        kelvin = 273
        temp = int(weer_info['main']['temp'] - kelvin)
        gevoelstemperatuur = int(weer_info['main']['feels_like'] - kelvin)
        luchtdruk = weer_info['main']['pressure']
        luchtvochtigheid = weer_info['main']['humidity']
        bewolking = weer_info['clouds']['all']

        weer = f"\nHet weer van: {naam_stad}" \
               f"\nTemperatuur:{temp}°" \
               f"\nGevoelstemperatuur:{gevoelstemperatuur}°" \
               f"\nLuchtdruk:{luchtdruk} hPa" \
               f"\nLuchtvochtigheid:{luchtvochtigheid}%" \
               f"\nBewolking:{bewolking}%"
    else:
        weer = f"\n\tWeer niet gevonden voor '{naam_stad}'. \n\tVul alstublieft een geldige stad in!"

    tfield.insert(INSERT, weer)


stad_kaas = Label(root, text='Vul stad in:', font='Helvetica 15').pack(pady=10)
inp_stad = Entry(root, textvariable=stad_string, width=24, font='Helvetica 15').pack()

Button(root, command=hetWeer, text="Het weer", font="Helvetica 12", fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

weer_nu = Label(root, text="Het weerbericht:", font='Helvetica 12').pack(pady=10)

tfield = Text(root, width=46, height=8)
tfield.pack()

root.mainloop()