DROP TABLE IF EXISTS igralci_1617;
DROP TABLE IF EXISTS igralci_1718;
DROP TABLE IF EXISTS igralci_1819;

CREATE TABLE IF NOT EXISTS igralci_1617(
   IGRALEC  VARCHAR(20) NOT NULL PRIMARY KEY
  ,EKIPA    VARCHAR(3)
  ,POZICIJA VARCHAR(2)
  ,STAROST  INTEGER 
  ,VISINA   VARCHAR(4)
  ,TEZA     INTEGER 
  ,DRZAVA   VARCHAR(16)
  ,GP       INTEGER 
  ,MPG      NUMERIC(4,1)
  ,PPG      NUMERIC(4,1)
  ,APG      NUMERIC(4,1)
  ,RPG      NUMERIC(4,1)
  ,SPG      NUMERIC(4,2)
  ,FT       NUMERIC(5,3)
  ,DVA      NUMERIC(5,3)
  ,TRI      NUMERIC(5,3)
);

CREATE TABLE IF NOT EXISTS igralci_1718(
   IGRALEC  VARCHAR(24) NOT NULL PRIMARY KEY
  ,EKIPA    VARCHAR(3)
  ,POZICIJA VARCHAR(2)
  ,STAROST  INTEGER 
  ,VISINA   VARCHAR(4)
  ,TEZA     INTEGER 
  ,DRZAVA   VARCHAR(16)
  ,GP       INTEGER 
  ,MPG      NUMERIC(4,1)
  ,PPG      NUMERIC(4,1)
  ,APG      NUMERIC(4,1)
  ,RPG      NUMERIC(4,1)
  ,SPG      NUMERIC(4,2)
  ,FT       NUMERIC(5,3)
  ,DVA      NUMERIC(5,3)
  ,TRI      NUMERIC(5,3)
);

CREATE TABLE IF NOT EXISTS igralci_1819(
   IGRALEC  VARCHAR(24) NOT NULL PRIMARY KEY
  ,EKIPA    VARCHAR(3) NOT NULL
  ,POZICIJA VARCHAR(3) NOT NULL
  ,STAROST  INTEGER  NOT NULL
  ,VISINA   VARCHAR(4) NOT NULL
  ,TEZA     INTEGER  NOT NULL
  ,DRZAVA   VARCHAR(16) NOT NULL
  ,GP       INTEGER  NOT NULL
  ,MPG      NUMERIC(4,1) NOT NULL
  ,PPG      NUMERIC(4,1) NOT NULL
  ,APG      NUMERIC(4,1) NOT NULL
  ,RPG      NUMERIC(4,1) NOT NULL
  ,SPG      NUMERIC(4,2) NOT NULL
  ,FT       NUMERIC(5,3) NOT NULL
  ,DVA      NUMERIC(5,3) NOT NULL
  ,TRI      NUMERIC(5,3) NOT NULL
);

CREATE TABLE IF NOT EXISTS trenerji_1617(
   TRENER          VARCHAR(16) NOT NULL PRIMARY KEY
  ,EKIPA           VARCHAR(3) NOT NULL
  ,st_let_s_klubom INTEGER  NOT NULL
  ,st_let_kariera  INTEGER  NOT NULL
  ,G_sezona        INTEGER  NOT NULL
  ,W_sezona        INTEGER  NOT NULL
  ,L_sezona        INTEGER  NOT NULL
  ,G_s_klubom      INTEGER  NOT NULL
  ,W_s_klubom      INTEGER  NOT NULL
  ,L_s_klubom      INTEGER  NOT NULL
  ,G_kariera       INTEGER  NOT NULL
  ,W_kariera       INTEGER  NOT NULL
  ,L_kariera       INTEGER  NOT NULL
  ,W_pr            NUMERIC(4,3) NOT NULL
);

CREATE TABLE IF NOT EXISTS trenerji_1718(
   TRENER          VARCHAR(16) NOT NULL PRIMARY KEY
  ,EKIPA           VARCHAR(3) NOT NULL
  ,st_let_s_klubom INTEGER  NOT NULL
  ,st_let_kariera  INTEGER  NOT NULL
  ,G_sezona        INTEGER  NOT NULL
  ,W_sezona        INTEGER  NOT NULL
  ,L_sezona        INTEGER  NOT NULL
  ,G_s_klubom      INTEGER  NOT NULL
  ,W_s_klubom      INTEGER  NOT NULL
  ,L_s_klubom      INTEGER  NOT NULL
  ,G_kariera       INTEGER  NOT NULL
  ,W_kariera       INTEGER  NOT NULL
  ,L_kariera       INTEGER  NOT NULL
  ,W_pr            NUMERIC(4,3) NOT NULL
);

CREATE TABLE IF NOT EXISTS trenerji_1819(
   TRENER          VARCHAR(16) NOT NULL PRIMARY KEY
  ,EKIPA           VARCHAR(3) NOT NULL
  ,st_let_s_klubom INTEGER  NOT NULL
  ,st_let_kariera  INTEGER  NOT NULL
  ,G_sezona        INTEGER  NOT NULL
  ,W_sezona        INTEGER  NOT NULL
  ,L_sezona        INTEGER  NOT NULL
  ,G_s_klubom      INTEGER  NOT NULL
  ,W_s_klubom      INTEGER  NOT NULL
  ,L_s_klubom      INTEGER  NOT NULL
  ,G_kariera       INTEGER  NOT NULL
  ,W_kariera       INTEGER  NOT NULL
  ,L_kariera       INTEGER  NOT NULL
  ,W_pr            NUMERIC(4,3) NOT NULL
);

CREATE TABLE IF NOT EXISTS sponzorji_1617(
   Ime_ekipe        VARCHAR(22) NOT NULL 
  ,Kratica          VARCHAR(3) NOT NULL PRIMARY KEY
  ,Sponzor_na_dresu VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS sponzorji_1718(
   Ime_ekipe        VARCHAR(22) NOT NULL 
  ,Kratica          VARCHAR(3) NOT NULL PRIMARY KEY
  ,Sponzor_na_dresu VARCHAR(27)
);

CREATE TABLE IF NOT EXISTS sponzorji_1819(
   Ime_ekipe        VARCHAR(22) NOT NULL
  ,Kratica          VARCHAR(3) NOT NULL PRIMARY KEY
  ,Sponzor_na_dresu VARCHAR(27)
);

CREATE TABLE ekipe(
   ID               INTEGER  NOT NULL PRIMARY KEY
  ,Ime_ekipe        VARCHAR(22) NOT NULL
  ,Kratica          VARCHAR(3) NOT NULL
  ,Sponzor_na_dresu VARCHAR(27) NOT NULL
  ,Sezona           INTEGER  NOT NULL
);

CREATE TABLE igralci( 
   ID       INTEGER  NOT NULL PRIMARY KEY 
  ,IGRALEC  VARCHAR(26) NOT NULL
  ,EKIPA    VARCHAR(3) NOT NULL
  ,POZICIJA VARCHAR(3) NOT NULL
  ,STAROST  VARCHAR(2) NOT NULL
  ,VISINA   VARCHAR(4) NOT NULL
  ,TEZA     VARCHAR(3) NOT NULL
  ,DRZAVA   VARCHAR(26) NOT NULL
  ,GP       VARCHAR(2) NOT NULL
  ,MPG      VARCHAR(4) NOT NULL
  ,PPG      VARCHAR(4) NOT NULL
  ,APG      VARCHAR(4) NOT NULL
  ,RPG      VARCHAR(4) NOT NULL
  ,SPG      VARCHAR(4) NOT NULL
  ,FT       VARCHAR(5) NOT NULL
  ,DVA      VARCHAR(5) NOT NULL
  ,TRI      VARCHAR(5) NOT NULL
  ,Sezona   INTEGER  NOT NULL
);

CREATE TABLE trenerji(
   ID              INTEGER  NOT NULL PRIMARY KEY 
  ,TRENER          VARCHAR(16) NOT NULL
  ,EKIPA           VARCHAR(3) NOT NULL
  ,st_let_s_klubom INTEGER  NOT NULL
  ,st_let_kariera  INTEGER  NOT NULL
  ,G_sezona        INTEGER  NOT NULL
  ,W_sezona        INTEGER  NOT NULL
  ,L_sezona        INTEGER  NOT NULL
  ,G_s_klubom      INTEGER  NOT NULL
  ,W_s_klubom      INTEGER  NOT NULL
  ,L_s_klubom      INTEGER  NOT NULL
  ,G_kariera       INTEGER  NOT NULL
  ,W_kariera       INTEGER  NOT NULL
  ,L_kariera       INTEGER  NOT NULL
  ,W_pr            NUMERIC(4,3) NOT NULL
  ,Sezona          INTEGER  NOT NULL
);