# Belangrijke modules importeren
import datetime
import time
import random
import psycopg2

# Datum toepassen en een string van maken
datum = datetime.date.today()
str_datum = str(datum)

# Tijd toepassen en ook een string van maken
tijd = time.localtime()
tijd_nu = time.strftime('%H:%M:%S', tijd)
str_tijd_nu = str(tijd_nu)

naam = input('Vul alstublieft uw naam in: ')

# While statement gebruiken, in het geval van getal blijft de input opnieuw vragen voor een geldige naam
while True:
    if naam.isdigit():
        print('Gebruik alstublieft geen getallen.')
        naam = input('Vul alstublieft opnieuw uw naam in: ')
    else:
        break

# In het geval van naam leeg is, of alleen maar spaties ingevuld zijn, naam omgezet naar anoniem
if naam == '' or naam.strip() == '':
    print('Naam automatisch omgezet naar: "anoniem"')

bericht = input('Omschrijf uw reiservaring met de NS, in maximaal 140 karakters: ')

# Zelfde voor het bericht met een while statement
while True:
    if bericht == '' or bericht.strip() == '':
        print('U heeft niets ingevuld. Probeer het opnieuw en vul alstublieft wat in.')
        bericht = input('Omschrijf uw reiservaring met de NS, in maximaal 140 karakters: ')
    else:
        break

# Limiet voor 140 karakters
while True:
    if len(bericht) > 140:
        print('Uw bericht mag niet meer dan 140 karakters bevatten.')
        bericht = input('Schrijf alstublieft opnieuw uw bericht, in maximaal 140 karakters: ')
    else:
        break

print('Bedankt voor uw tijd! Wij wensen u namens de NS nog een fijne dag.')
print(f'Bericht geplaatst op: {datum} om {tijd_nu}')

# Text file openen en lezen, random choice str van maken
with open('Steden.txt', 'r') as file:
    x = file.read()
    steden = list(map(str, x.split()))
str_steden = str(random.choice(steden))

print('Bericht geschreven op het station van:', str_steden)

# Text file openen en append toepassen.
text_file = open("Project_Zuil_Berichten.txt", "a")

# String van de parameters gemaakt en toepassen in het zuil berichten text file
format = (f"{naam}, {bericht}, {str_datum}, {str_tijd_nu}, {str_steden}\n")

text_file.write(format)

file.close()

# Database verbinden met het bericht. Hij gaat nu naar een text file, maar ook naar de database
connection_string = "host='localhost' dbname='Project_Zuil_1' user='postgres' password='Traykie1665!'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
insert_script = 'INSERT INTO bericht (naam, bericht, datum, tijd, station) VALUES (%s, %s, %s, %s, %s)'
insert_value = (naam, bericht, str_datum, str_tijd_nu, str_steden)
cursor.execute(insert_script, insert_value)
conn.commit()
conn.close()