from bottle import *
import sqlite3

#Konfiguracija
baza_datoteka = 'sport.db'

#Poročila o napakah
debug(True) #za izpise pri razvoju

@get('/')
def index():
    return('Začetna stran')

@get('/igralci1617')
def igralci1617():
    cur = baza.cursor()
    igralci1617 = cur.execute("SELECT IGRALEC,EKIPA,POZICIJA,STAROST,VISINA,TEZA,DRZAVA from igralci_1617")
    return template('igralci1617.html', igralci1617=igralci1617)

@get('/igralci1718')
def igralci1718():
    cur = baza.cursor()
    igralci1718 = cur.execute("SELECT IGRALEC,EKIPA,POZICIJA,STAROST,VISINA,TEZA,DRZAVA from igralci_1718")
    return template('igralci1718.html', igralci1718=igralci1718)

@get('/igralci1819')
def igralci1819():
    cur = baza.cursor()
    igralci1819 = cur.execute("SELECT IGRALEC,EKIPA,POZICIJA,STAROST,VISINA,TEZA,DRZAVA from igralci_1819")
    return template('igralci1819.html', igralci1819=igralci1819)

@get('/trenerji1617')
def trenerji1617():
    cur = baza.cursor()
    trenerji1617 = cur.execute("SELECT TRENER,EKIPA,st_let_kariera,G_sezona,W_sezona,L_sezona from trenerji_1617")
    return template('trenerji1617.html', trenerji1617=trenerji1617)

baza = sqlite3.connect(baza_datoteka, isolation_level=None)
#Izpis SQL stavkov v terminal(za debugiranje pri razvoju)
baza.set_trace_callback(print)
#Zapoved upoštevanja omejitev FOREIGN KEY
cur = baza.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

#Reloader nam olajša razvoj, ker osvežuje sproti
run(host='localhost', port=8080, reloader=True)