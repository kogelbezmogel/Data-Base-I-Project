CREATE TABLE projekt.aktor
(
    id_aktor INT,
    imie VARCHAR(80) NOT NULL,
    nazwisko VARCHAR(80) NOT NULL,
    data_urodzenia DATE NOT NULL,
    PRIMARY KEY(id_aktor)
);

CREATE TABLE projekt.kategoria
(
    id_kategoria INT,
    nazwa_kategorii VARCHAR(30),
    PRIMARY KEY(id_kategoria)
);

CREATE TABLE projekt.rezyser
(
    id_rezyser INT,
    imie VARCHAR(80) NOT NULL,
    nazwisko VARCHAR(80) NOT NULL,
    data_urodzenia DATE NOT NULL,
    PRIMARY KEY(id_rezyser)
);

CREATE TABLE projekt.opis
(
    id_opis INT,
    opis VARCHAR(500) NOT NULL,
    PRIMARY KEY(id_opis)
);

CREATE TABLE projekt.film
(
    id_film INT,
    id_rezyser INT,
    id_opis INT,
    tytul VARCHAR(80) NOT NULL,
    premiera DATE NOT NULL,
    dlugosc INT NOT NULL,
    FOREIGN KEY(id_rezyser) REFERENCES projekt.rezyser(id_rezyser),
    FOREIGN KEY(id_opis) REFERENCES projekt.opis(id_opis),
    PRIMARY KEY(id_film)
);

CREATE TABLE projekt.kino
(
    id_kino INT,
    nazwa_kina VARCHAR(80) NOT NULL,
    otwarcie_od TIME NOT NULL,
    otwarcie_do TIME NOT NULL,
    nr_budynku INT NOT NULL,
    ulica VARCHAR(80) NOT NULL,
    PRIMARY KEY(id_kino)
);

CREATE TABLE projekt.grafik
(
    id_grafik INT,
    id_kino INT,
    data_koniec DATE NOT NULL,
    data_poczatek DATE NOT NULL,
    FOREIGN KEY(id_kino) REFERENCES projekt.kino(id_kino),
    PRIMARY KEY(id_grafik)
);

CREATE TABLE projekt.pracownik
(
    id_pracownik INT,
    telefon VARCHAR(15) NOT NULL,
    email VARCHAR(80) NOT NULL,
    nr_budynku INT NOT NULL,
    ulica VARCHAR(80) NOT NULL,
    imie VARCHAR(80) NOT NULL,
    nazwisko VARCHAR(80) NOT NULL,
    PRIMARY KEY(id_pracownik)
);

CREATE TABLE projekt.sala
(
    id_sala INT,
    id_kino INT,
    rzedy VARCHAR(80) NOT NULL,
    dlugosc_rzedu VARCHAR(80) NOT NULL,
    FOREIGN KEY(id_kino) REFERENCES projekt.kino(id_kino),
    PRIMARY KEY(id_sala)
);

CREATE TABLE projekt.seans
(
    id_seans INT,
    id_sala INT,
    poczatek_seansu TIME NOT NULL,
    koniec_seansu TIME NOT NULL,
    data_seansu DATE NOT NULL,
    FOREIGN KEY(id_sala) REFERENCES projekt.sala(id_sala),
    PRIMARY KEY(id_seans)
);

CREATE TABLE projekt.klient
(
    id_klient INT,
    imie VARCHAR(80) NOT NULL,
    nazwisko VARCHAR(80) NOT NULL,
    telefon VARCHAR(15) NOT NULL,
    PRIMARY KEY(id_klient)
);

CREATE TABLE projekt.bilet
(
    id_bilet INT,
    id_klient INT,
    id_seans INT,
    ulga VARCHAR(30) NOT NULL,
    cena FLOAT NOT NULL,
    forma_platnosci VARCHAR(30),
    FOREIGN KEY(id_klient) REFERENCES projekt.klient(id_klient),
    FOREIGN KEY(id_seans) REFERENCES projekt.seans(id_seans),
    PRIMARY KEY(id_bilet)
);

CREATE TABLE projekt.grafik_pracownik
(
    id_grafik_pracownik INT,
    id_grafik INT,
    id_pracownik INT,
    FOREIGN KEY(id_grafik) REFERENCES projekt.grafik(id_grafik),
    FOREIGN KEY(id_pracownik) REFERENCES projekt.pracownik(id_pracownik),
    PRIMARY KEY(id_grafik_pracownik)
);

CREATE TABLE projekt.seans_film
(
    id_seans_film INT,
    id_seans INT,
    id_film INT,
    FOREIGN KEY(id_seans) REFERENCES projekt.seans(id_seans),
    FOREIGN KEY(id_film) REFERENCES projekt.film(id_film),
    PRIMARY KEY(id_seans_film)
);

CREATE TABLE projekt.kategoria_film
(
    id_kategoria_film INT,
    id_kategoria INT,
    id_film INT,
    FOREIGN KEY(id_film) REFERENCES projekt.film(id_film),
    FOREIGN KEY(id_kategoria) REFERENCES projekt.kategoria(id_kategoria),
    PRIMARY KEY(id_kategoria_film)
);

CREATE TABLE projekt.aktor_film
(
    id_aktor_film INT,
    id_film INT,
    id_aktor INT,
    FOREIGN KEY(id_film) REFERENCES projekt.film(id_film),
    FOREIGN KEY(id_aktor) REFERENCES projekt.aktor(id_aktor),
    PRIMARY KEY(id_aktor_film)
);