from bottle import *
import sqlite3

#Konfiguracija
baza_datoteka = 'sport.db'

#Poročila o napakah
debug(True) #za izpise pri razvoju

@get('/')
def index():
    return('Začetna stran')


baza = sqlite3.connect(baza_datoteka, isolation_level=None)
#Izpis SQL stavkov v terminal(za debugiranje pri razvoju)
baza.set_trace_callback(print)
#Zapoved upoštevanja omejitev FOREIGN KEY
cur = baza.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

#Reloader nam olajša razvoj, ker osvežuje sproti
run(host='localhost', port=8080, reloader=True)