from tkinter import *
import requests
import json
import psycopg2
import webbrowser

root = Tk()

# Functies aanmaken, en die vervolgens als command toevoegen aan de knoppen(Buttons)
def klik1():
    kaas = Label(master=root, text='Welkom op het station van Arnhem. Bekijk aanvullende informatie hierboven', background='gold', font=('Helvetica', 18))
    kaas.pack()


def klik2():
    aardappel = Label(master=root, text='Welkom op het station van Helmond. Bekijk aanvullende informatie hierboven', background='gold', font=('Helvetica', 18))
    aardappel.pack()


def klik3():
    karel = Label(master=root, text='Welkom op het station van Zutphen. Bekijk aanvullende informatie hierboven', background='gold', font=('Helvetica', 18))
    karel.pack()


# Er zit helaas een bug hier, de weer app werkt wel gewoon in de andere python file.
def klik4():
    import Weer_API


def fetch_data():
    connection_string = "host='localhost' dbname='Project_Zuil_1' user='postgres' password='Traykie1665!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = """SELECT naam, bericht, datum, tijd, station
               FROM bericht"""

    cursor.execute(query)
    records = cursor.fetchall()
    conn.commit()
    conn.close()

    for record in records:
        print(record)


def faciliteiten():
    connection_string = "host='localhost' dbname='Project_Zuil_1' user='postgres' password='Traykie1665!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = """SELECT ov_bike, elevator, toilet, park_and_ride 
               FROM station_service 
               WHERE station_city='Arnhem';"""

    cursor.execute(query)
    records2 = cursor.fetchall()
    conn.commit()
    conn.close()

    for r in records2:
        print(r)


def faciliteiten2():
    connection_string = "host='localhost' dbname='Project_Zuil_1' user='postgres' password='Traykie1665!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = """SELECT ov_bike, elevator, toilet, park_and_ride 
               FROM station_service 
               WHERE station_city='Zupthen';"""

    cursor.execute(query)
    broodjekaas = cursor.fetchall()
    conn.commit()
    conn.close()

    for b in broodjekaas:
        print(b)


def faciliteiten3():
    connection_string = "host='localhost' dbname='Project_Zuil_1' user='postgres' password='Traykie1665!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = """SELECT ov_bike, elevator, toilet, park_and_ride 
                   FROM station_service 
                   WHERE station_city='Helmond';"""

    cursor.execute(query)
    alles = cursor.fetchall()
    conn.commit()
    conn.close()

    for a in alles:
        print(a)


def link():
    webbrowser.open_new(r'https://www.ns.nl/')


def link_2():
    webbrowser.open_new_tab(r'https://www.ns.nl/reisplanner/#/')

# Achtergrond kleur
root.configure(background='gold')

# Label en knoppen aanmaken, en een beetje customizen
label = Label(master=root,
              text='\n\nWelkom bij de NS\n\n Op welk station bevindt u zich?\n\n Bekijk verdere informatie hieronder\n\n',
              background='gold',
              font=('Helvetica', 28, 'bold italic'),
              width=40,
              height=5)
label.pack()

knop1 = Button(master=root, text='1. Arnhem', font=('Helvetica', 14, 'bold italic'),padx=18, pady=4, command=klik1)
knop1.pack()

knop2 = Button(master=root, text='2. Helmond', font=('Helvetica', 14, 'bold italic'),padx=20, pady=5, command=klik2)
knop2.pack()

knop3 = Button(master=root, text='3. Zutphen', font=('Helvetica', 14, 'bold italic'),padx=20, pady=5, command=klik3)
knop3.pack()

knop4 = Button(master=root, text='Weerbericht', font=('Helvetica', 14, 'bold italic'),padx=20, pady=5, command=klik4)
knop4.pack()

knop5 = Button(master=root, text='Reiservaringen', font=('Helvetica', 14, 'bold italic'),padx=20, pady=5, command=fetch_data)
knop5.pack()

knop6 = Button(master=root, text='Algemene NS Informatie', font=('Helvetica', 14, 'bold italic'),padx=18, pady=4, command=link)
knop6.pack()

knop7 = Button(master=root, text='NS Reisplanner', font=('Helvetica', 14, 'bold italic'),padx=16, pady=4, command=link_2)
knop7.pack()

knop8 = Button(master=root, text='Faciliteiten', font=('Helvetica', 14, 'bold italic'),padx=16, pady=5, command=faciliteiten)
knop8.pack()

# En eindigen met de mainloop
root.mainloop()