from bottle import *
import sqlite3

#Konfiguracija
baza_datoteka = 'sport.db'

#Poročila o napakah
debug(True) #za izpise pri razvoju

#Mapa za statične vire
static_dir = "./static"

@route("/static/<filename:path>")
def static(filename):
    return static_file(filename, root=static_dir)

###########################################################
##################### Prva stran ##########################
###########################################################

@get('/')
def izberileto():
    return template('zacetna.html')

###########################################################
##################### Sezona16/17 #########################
###########################################################

@get('/sezona1617')
def sezona1617():
    cur = baza.cursor()
    sezona1617 = cur.execute("SELECT IGRALEC,EKIPA,POZICIJA,STAROST,VISINA,TEZA,DRZAVA from igralci_1617")
    return template('sezona1617.html', sezona1617=sezona1617)

@get('/sezona1617/<IGRALEC>/statistika')
def sezona1617statistika(IGRALEC):
    cur = baza.cursor()
    sezona1617statistika = cur.execute("SELECT IGRALEC,GP,MPG,PPG,APG,RPG,SPG,FT,DVA,TRI from igralci_1617 WHERE IGRALEC = ?",(IGRALEC, )).fetchall()
    igralec = sezona1617statistika[0][1] #tole morm zrihtat, k mi v html ne kliče tega?zakaj?
    return template('sezona1617statistika.html', sezona1617statistika=sezona1617statistika, IGRALEC=IGRALEC)

@get('/sezona1617/ekipe')
def ekipe16171617():
    cur = baza.cursor()
    ekipe1617 = cur.execute("""SELECT Ime_ekipe,Kratica,trenerji_1617.TRENER, trenerji_1617.W_sezona, trenerji_1617.L_sezona ,Sponzor_na_dresu from sponzorji_1617
                                    INNER JOIN trenerji_1617 ON trenerji_1617.EKIPA = sponzorji_1617.Kratica """)
    return template('ekipe1617.html', ekipe1617=ekipe1617)

# SAMO TEST??
@get('/sezona1617/sponzorji')
def sponzorji1617():
    cur = baza.cursor()
    sponzorji1617= cur.execute("SELECT Ime_ekipe, Kratica, Sponzor_na_dresu from sponzorji_1617")
    return template("sponzorji1617.html", sponzorji1617=sponzorji1617)

@post('/igralci1617/ekipe/dodaj_sponzorja')
def dodaj_sponzorja():
    ekipa = request.forms.get("Ime_ekipe")
    kratica = request.forms.get("Kratica")
    sponzor = request.forms.get("Sponzor_na_dresu")
    cur = baza.cursor()
    cur.execute("INSERT INTO sponzorji_1617 (Ime_ekipe, Kratica, Sponzor_na_dresu) VALUES (?, ?, ?)", (ekipa, kratica, sponzor))
    redirect('/sezona1617/sponzorji')

@get('/igralci1617/sponzorji/uredi/<Sponzor_na_dresu>')
def uredi_sponzorja_get(Sponzor_na_dresu):
    cur = baza.cursor()
    sponzor1 = cur.execute("SELECT Sponzor_na_dresu FROM sponzorji_1617 WHERE Sponzor_na_dresu =?", (Sponzor_na_dresu)).fetchone()
    return template("sponzorji1617-edit.hmtl", sponzorji_1617 = sponzorji_1617)

@get('/sezona1617/ekipe/trener/<TRENER>')
def trenerji1617statistika(TRENER):
    cur = baza.cursor()
    trenerji1617statistika = cur.execute("SELECT TRENER,EKIPA,st_let_s_klubom,st_let_kariera,G_sezona,W_sezona,L_sezona,G_s_klubom,W_s_klubom,L_s_klubom,G_kariera,W_kariera,L_kariera,W_pr from trenerji_1617 WHERE TRENER = ?",(TRENER, )).fetchall()
    return template('trenerji1617statistika.html', trenerji1617statistika=trenerji1617statistika, TRENER=TRENER)

@get('/sezona1617/ekipe/<EKIPA>')
def vsiigralci1617ekipa(EKIPA):
    cur = baza.cursor()
    vsiigralci1617ekipa = cur.execute("""SELECT IGRALEC,EKIPA,POZICIJA,STAROST,VISINA,TEZA,DRZAVA from igralci_1617 
                                    WHERE EKIPA = ?""",(EKIPA, )).fetchall()
    return template('vsiigralci1617ekipa.html', vsiigralci1617ekipa=vsiigralci1617ekipa, EKIPA=EKIPA)

@get('/sezona1617/ekipe/<EKIPA>/<IGRALEC>')
def sezona1617ekipaigralecstat(EKIPA, IGRALEC):
    cur = baza.cursor()
    sezona1617ekipaigralecstat = cur.execute("SELECT IGRALEC,GP,MPG,PPG,APG,RPG,SPG,FT,DVA,TRI,EKIPA from igralci_1617 WHERE IGRALEC = ?",(IGRALEC, )).fetchall()
    #igralec = sezona1617ekipaigralecstat[0][1] #tole morm zrihtat, k mi v html ne kliče tega?zakaj?
    return template('sezona1617ekipaigralecstat.html', sezona1617ekipaigralecstat=sezona1617ekipaigralecstat, EKIPA=EKIPA, IGRALEC=IGRALEC)

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

###########################################################
####################### Trenerji ##########################
###########################################################

# @get('/trenerji1617')
# def trenerji1617():
#     cur = baza.cursor()
#     trenerji1617 = cur.execute("SELECT TRENER,EKIPA,st_let_kariera,G_sezona,W_sezona,L_sezona from trenerji_1617")
#     return template('trenerji1617.html', trenerji1617=trenerji1617)

# @get('/trenerji1718')
# def trenerji1718():
#     cur = baza.cursor()
#     trenerji1718 = cur.execute("SELECT TRENER,EKIPA,st_let_kariera,G_sezona,W_sezona,L_sezona from trenerji_1718")
#     return template('trenerji1718.html', trenerji1718=trenerji1718)

# @get('/trenerji1819')
# def trenerji1819():
#     cur = baza.cursor()
#     trenerji1819 = cur.execute("SELECT TRENER,EKIPA,st_let_kariera,G_sezona,W_sezona,L_sezona from trenerji_1819")
#     return template('trenerji1819.html', trenerji1819=trenerji1819)

###########################################################
###################### Sponzorji ##########################
###########################################################



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