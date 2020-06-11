from bottle import get, post, run, request, template, redirect, static_file, debug, route

import auth_public as auth

import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

import os

SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
ROOT = os.environ.get('BOTTLE_ROOT', '/')
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

def rtemplate(*largs, **kwargs):
    """
    Izpis predloge s podajanjem spremenljivke ROOT z osnovnim URL-jem.
    """
    return template(ROOT=ROOT, *largs, **kwargs)

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
    return rtemplate('zacetna.html')

###########################################################
######################## Sezona ###########################
###########################################################

@get('/<Sezona>')#Deluje
def sezona16(Sezona):
    #cur = baza.cursor()
    cur.execute("SELECT IGRALEC,EKIPA,POZICIJA,STAROST,VISINA,TEZA,DRZAVA,Sezona from igralci WHERE Sezona=%s",(Sezona,))
    Sezona = cur.fetchall()
    return rtemplate('sezona.html', Sezona=Sezona)

@get('/<Sezona>/ekipe')#Deluje
def ekipe(Sezona):
    #cur = baza.cursor()
    cur.execute("""SELECT ekipe.ID,Ime_ekipe,Kratica,trenerji.TRENER, trenerji.W_sezona,trenerji.L_sezona, Sponzor_na_dresu from ekipe
                        INNER JOIN trenerji ON trenerji.EKIPA = ekipe.Kratica
                        WHERE trenerji.Sezona=%s AND ekipe.Sezona=%s
                        ORDER BY W_sezona DESC""",(Sezona,Sezona,))
    ekipe = cur.fetchall()
    return template('ekipe.html', ekipe=ekipe)
#Darjan: med editanjem dodana napaka= napaka, če bo potrebno pri urejanju (verjetno ne)

@get('/<Sezona>/ekipe/<EKIPA>')#Deluje
def igralciekipa(Sezona,EKIPA):
    #cur = baza.cursor()
    cur.execute("""SELECT IGRALEC,EKIPA,POZICIJA,STAROST,VISINA,TEZA,DRZAVA,Sezona from igralci
                                    WHERE EKIPA = %s AND Sezona =%s""",(EKIPA, Sezona,))
    igralciekipa = cur.fetchall()
    return template('igralciekipa.html', igralciekipa=igralciekipa, EKIPA=EKIPA, Sezona=Sezona)

@get('/<Sezona>/<IGRALEC>')#Deluje
def igralecstatistika(Sezona,IGRALEC):
    #cur = baza.cursor()
    cur.execute("""SELECT IGRALEC,GP,MPG,PPG,APG,RPG,SPG,FT,DVA,TRI,Sezona from igralci WHERE IGRALEC=%s AND Sezona=%s""",(IGRALEC,Sezona,))
    igralecstatistika = cur.fetchall()
    return template('igralecstatistika.html', igralecstatistika=igralecstatistika, IGRALEC=IGRALEC, Sezona=Sezona)

@get('/<Sezona>/ekipe/<EKIPA>/<TRENER>')#Deluje
def trenerjistatistika(TRENER,Sezona,EKIPA):
    #cur = baza.cursor()
    cur.execute("""SELECT TRENER,EKIPA,st_let_s_klubom,st_let_kariera,G_sezona,W_sezona,L_sezona,G_s_klubom,W_s_klubom,L_s_klubom,G_kariera,W_kariera,L_kariera,W_pr, Sezona from trenerji
                                    WHERE TRENER = %s AND Sezona=%s""",(TRENER,Sezona ))
    trenerjistatistika = cur.fetchall()
    return template('trenerjistatistika.html', trenerjistatistika=trenerjistatistika)

#Od tukaj naprej Darjan probaval Edit

@get('/<Sezona>/ekipe/uredi/<ID>')
def uredi_sponzorja(ID):
    #cur = baza.cursor()
    cur.execute("SELECT ID,Ime_ekipe,Sponzor_na_dresu, Sezona FROM ekipe WHERE ID=%s", (ID,))
    ekipe = cur.fetchone()
    return template('ekipe-edit.html', ekipe=ekipe)

@post('/<Sezona>/ekipe/uredi/<ID>')
def uredi_sponzorja(ID):
    Sponzor_na_dresu = request.forms.Sponzor_na_dresu
    #cur = baza.cursor()
    cur.execute("UPDATE Sponzor_na_dresu SET Sponzor_na_dresu = %s WHERE ID=%s", (Sponzor_na_dresu,ID))
    redirect('/<Sezona>/ekipe')


###########################################################
################ Registracija/Prijava #####################
###########################################################

def hashGesla(s):    #za shranjevanje gesla
    m = hashlib.sha256()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

skrivnost = "kODX3ulHw3ZYRdbIVcp1IfJTDn8iQTH6TFaNBgrSkj"  
adminGeslo = "1234"

@get('/prijava')
def prijava_get():
    return template('prijava.html', napaka=None)

''' @post('/prijava')
def prijava_post():
    """Obdelaj izpolnjeno formo za prijavo"""
    # Uporabniško ime, ki ga je uporabnik vpisal v formo
    username = request.forms.username
    # Izračunamo MD5 has gesla, ki ga bomo spravili
    password = hashGesla(request.forms.password)
    # Preverimo, ali se je uporabnik pravilno prijavil
    cur.execute("SELECT * FROM uporabnik WHERE username=%s AND password=%s", [username, password])
    if cur.fetchone() is None:
        # Username in geslo se ne ujemata
        return template("prijava.html",
                               napaka="Uporabnik ne obstaja",
                               username=username)
    else:
        # Vse je v redu, nastavimo cookie in preusmerimo na glavno stran
        response.set_cookie('username', username, path='/', secret=skrivnost)
        redirect("/") '''

@get('/registracija')
def registracija_get():
    #cur = baza.cursor()
    return template('registracija.html', username=None, napaka=None) 

''' @post("/registracija")
def registracija_post():
    print('trying to register')
    username = request.forms.username
    password1 = request.forms.password1
    password2 = request.forms.password2
    adminPassword = request.forms.adminPassword
    adminCheck = request.forms.adminCheckbox

    if username is None or password1 is None or password2 is None:
        nastaviSporocilo('Registracija ni možna') 
        redirect('/registracija')
        return
    if len(password) < 4:
        nastaviSporocilo('Geslo mora imeti vsaj 4 znake.') 
        redirect('/registracija')
        return
    if password1 != password2:
        nastaviSporocilo('Gesli se ne ujemata.') 
        redirect('/registracija')
        return

    zgostitev = hashGesla(password)

    response.set_cookie('username', username, secret=skrivnost)
    redirect('/') '''

##########################################################################################


conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=DB_PORT)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

run(host='localhost', port=SERVER_PORT, reloader=RELOADER)