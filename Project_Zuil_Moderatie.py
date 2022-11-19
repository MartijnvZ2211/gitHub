# Belangrijke modules importeren
import psycopg2
import time
import datetime

# Input gegevens van de moderator, wederom met while statements
mod_naam = input('Voer je naam in: ')

while True:
    if mod_naam.isdigit():
        print('Gebruik alstublieft geen getallen.')
        mod_naam = input('Vul alstublieft opnieuw je naam in: ')
    else:
        break
while True:
    if mod_naam == '' or mod_naam.strip() == '':
        print('Vul een geldige naam in.')
        mod_naam = input('Voer opnieuw je naam in: ')
    else:
        break

mod_email = input('Vul je email in: ')

while True:
    if mod_email == '' or mod_email.strip() == '':
        print('Ongeldig email adres.')
        mod_email = input('Vul opnieuw je email adres in: ')
    else:
        break

goedkeuring = input('Is het bericht goedgekeurd: ')

while True:
    if goedkeuring.isdigit():
        print('Gebruik alsjeblieft geen getallen, antwoord met "ja" of "nee".')
        goedkeuring = input('Antwoord opnieuw met "ja" of "nee": ')
    else:
        break
while True:
    if goedkeuring == '' or goedkeuring.strip() == '':
        print('Je hebt niets ingevuld. Gelieve te beantwoorden met "ja" of "nee".')
        goedkeuring = input('Vul alsjeblieft opnieuw een antwoord in, met "ja" of "nee": ')
    else:
        break

# Datum en tijd toevoegen aan de gegevens van de database
datum = datetime.date.today()
tijd = time.localtime()
tijd_nu = time.strftime('%H:%M:%S', tijd)

# Database verbinden met de moderator gegevens
connection_string = "host='localhost' dbname='Project_Zuil_1' user='postgres' password='Traykie1665!'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
insert_script = 'INSERT INTO moderator (naam, email, goedkeuring, datum, tijd) VALUES (%s, %s, %s, %s, %s)'
insert_value = (mod_naam, mod_email, goedkeuring, datum, tijd_nu)
cursor.execute(insert_script, insert_value)
conn.commit()
conn.close()