import sqlite3
import csv

baza_datoteka = 'sport.db'

def uvoziSQL(cur, datoteka):
    with open(datoteka) as f:
        koda = f.read()
        cur.executescript(koda)

with open("uvoz/sponzorji_1718.sql") as f:
    koda = f.read()
    print (koda)

#Treba se popravit csv uvoz, ker tale ne dela, syntax error? 
# def uvoziCSV(cur, tabela):
#     with open('uvoz/{0}.csv'.format(tabela)) as csvfile:
#         podatki = csv.reader(csvfile)
#         vsiPodatki = [vrstica for vrstica in podatki]
#         glava = vsiPodatki[0]
#         vrstice = vsiPodatki[1:]
#         cur.executemany("INSERT INTO {0} ({1}) VALUES ({2})".format(tabela, ",".join(glava),",".join(['?']*len(glava))), vrstice)

#Uvozimo preko SQL skript
with sqlite3.connect(baza_datoteka) as baza:
     cur = baza.cursor()
     uvoziSQL(cur,'sport.sql')
     uvoziSQL(cur,'uvoz/igralci_1617.sql')
     uvoziSQL(cur,'uvoz/igralci_1718.sql')
     uvoziSQL(cur,'uvoz/igralci_1819.sql') 
     uvoziSQL(cur,'uvoz/trenerji_1617.sql')
     uvoziSQL(cur,'uvoz/trenerji_1718.sql')
     uvoziSQL(cur,'uvoz/trenerji_1819.sql')
     uvoziSQL(cur,'uvoz/sponzorji_1617.sql')
     uvoziSQL(cur,'uvoz/sponzorji_1718.sql')
     uvoziSQL(cur,'uvoz/sponzorji_1819.sql')