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

@get('/trenerji1718')
def trenerji1718():
    cur = baza.cursor()
    trenerji1718 = cur.execute("SELECT TRENER,EKIPA,st_let_kariera,G_sezona,W_sezona,L_sezona from trenerji_1718")
    return template('trenerji1718.html', trenerji1718=trenerji1718)

@get('/trenerji1819')
def trenerji1819():
    cur = baza.cursor()
    trenerji1819 = cur.execute("SELECT TRENER,EKIPA,st_let_kariera,G_sezona,W_sezona,L_sezona from trenerji_1819")
    return template('trenerji1819.html', trenerji1819=trenerji1819)

@get('/sponzorji1617')
def sponzorji1617():
    cur = baza.cursor()
    sponzorji1617 = cur.execute("SELECT Ime_ekipe,Kratica,Sponzor_na_dresu from sponzorji_1617")
    return template('sponzorji1617.html', sponzorji1617=sponzorji1617)

@get('/sponzorji1718')
def sponzorji1718():
    cur = baza.cursor()
    sponzorji1718 = cur.execute("SELECT Ime_ekipe,Kratica,Sponzor_na_dresu from sponzorji_1718")
    return template('sponzorji1718.html', sponzorji1718=sponzorji1718)

@get('/sponzorji1819')
def sponzorji1819():
    cur = baza.cursor()
    sponzorji1819 = cur.execute("SELECT Ime_ekipe,Kratica,Sponzor_na_dresu from sponzorji_1819")
    return template('sponzorji1819.html', sponzorji1819=sponzorji1819)

baza = sqlite3.connect(baza_datoteka, isolation_level=None)
#Izpis SQL stavkov v terminal(za debugiranje pri razvoju)
baza.set_trace_callback(print)
#Zapoved upoštevanja omejitev FOREIGN KEY
cur = baza.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

#Reloader nam olajša razvoj, ker osvežuje sproti
run(host='localhost', port=8080, reloader=True)