CREATE VIEW oblozenie_seansow (tytul, numer_seansu, data_seansu, numer_sali, bilety, max_miejsc) AS
    SELECT
        fi.tytul,
        se.id_seans AS numer_seansu,
        se.data_seansu,
        se.id_sala AS numer_sali,
        COUNT(id_bilet) AS bilety,
        max_miejsc
            FROM 
                projekt.seans AS se
                JOIN projekt.bilet bi ON se.id_seans = bi.id_seans
                JOIN ( SELECT id_sala, projekt.max_miejsc(id_sala) AS max_miejsc FROM projekt.sala ) mi ON se.id_sala = mi.id_sala
                JOIN projekt.sala sa ON se.id_sala = sa.id_sala
                JOIN projekt.seans_film sefi ON se.id_seans = sefi.id_seans
                JOIN projekt.film fi ON sefi.id_film = fi.id_film
    GROUP BY 
        se.id_seans,
        se.id_sala,
        max_miejsc,
        fi.tytul,
        se.data_seansu
    ORDER BY
        fi.tytul,
        se.data_seansu,
        se.id_seans;



CREATE VIEW repertuar



CREATE VIEW oblozenie_kina_w_tygodniu (nazwa_kina, dzien, ilosc_klientow) AS
    SELECT 
        nazwa_kina,
        se.data_seansu AS dzien,
        COUNT(bi.id_bilet) AS ilosc_klientow
        FROM
            projekt.kino AS ki
            JOIN projekt.sala sa ON ki.id_kino = sa.id_kino
            JOIN projekt.seans se ON sa.id_sala = se.id_sala
            JOIN projekt.bilet bi ON se.id_seans = bi.id_seans
    GROUP BY
        se.data_seansu,
        nazwa_kina
    ORDER BY 
        se.data_seansu;




CREATE VIEW baza_filmow (id_film, tytul, imie_rezysera, nazwisko_rezysera, premiera, dlugosc, opis) AS
    SELECT
        fi.id_film, 
        tytul,
        re.imie AS imie_rezysera,
        re.nazwisko AS nazwisko_rezysera,
        fi.premiera,
        fi.dlugosc,
        op.opis
        FROM 
            projekt.film AS fi
            JOIN projekt.opis op ON fi.id_opis = op.id_opis
            JOIN projekt.rezyser re ON fi.id_rezyser = re.id_rezyser
    GROUP BY
        fi.id_film, 
        tytul,
        re.imie,
        re.nazwisko,
        opis,
        fi.premiera,
        fi.dlugosc
    ORDER BY 
        tytul;




CREATE VIEW daty_w_repertuarze (data_repertuaru) AS
    SELECT
        data_seansu AS data_repertuaru
    FROM
        projekt.seans
    GROUP BY
        data_seansu
    ORDER BY 
        data_seansu; 
    



CREATE FUNCTION projekt.top_klientow ( prog INTEGER )
RETURNS TABLE(imie VARCHAR, nazwisko VARCHAR, ilosc_biletow BIGINT) AS
    $$
    BEGIN
        RETURN QUERY
            SELECT 
                kl.imie,
                kl.nazwisko,
                COUNT(id_bilet) AS ilosc_biletow
            FROM
                projekt.klient AS kl 
                JOIN projekt.bilet AS bi ON kl.id_klient = bi.id_klient
            GROUP BY 
                kl.imie,
                kl.nazwisko
            HAVING
                COUNT(id_bilet) >= prog
            ORDER BY 
                COUNT(id_bilet) DESC;
    END;
    $$
    LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION projekt.max_miejsc(id INTEGER)
RETURNS INTEGER AS
$$
    DECLARE
        szerokosc INTEGER;
        dlugosc INTEGER;
        miejsca INTEGER;
    BEGIN
        SELECT rzedy INTO szerokosc FROM projekt.sala WHERE id_sala = id;
        SELECT dlugosc_rzedu INTO dlugosc FROM projekt.sala WHERE id_sala = id;
        miejsca := dlugosc * szerokosc;
        RETURN miejsca;
    END
$$
LANGUAGE plpgsql; 




CREATE OR REPLACE FUNCTION projekt.repertuar_dnia( data_f DATE, nazwa_k VARCHAR )
RETURNS TABLE (id_seans INT, id_film INT) AS
$$
    BEGIN
        RETURN QUERY
            SELECT 
                se.id_seans,
                fi.id_film
            FROM 
                projekt.seans AS se
                JOIN projekt.seans_film AS sefi ON se.id_seans = sefi.id_seans
                JOIN projekt.film AS fi ON sefi.id_film = fi.id_film
                JOIN projekt.sala AS sa ON se.id_sala = sa.id_sala
                JOIN projekt.kino AS ki ON sa.id_kino = ki.id_kino
            WHERE 
                ki.nazwa_kina = nazwa_k AND se.data_seansu = data_f;
    END
$$
LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION projekt.kategorie_filmu( id INT )
RETURNS TABLE ( kategoria VARCHAR ) AS
$$
    BEGIN
        RETURN QUERY
            SELECT 
                ka.nazwa_kategorii AS kategoria
            FROM 
                projekt.film AS fi
                JOIN projekt.kategoria_film AS kafi ON fi.id_film = kafi.id_film
                JOIN projekt.kategoria AS ka ON kafi.id_kategoria = ka.id_kategoria
            WHERE 
                fi.id_film = id; 
    END
$$
LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION projekt.aktorzy_filmu( id INT )
RETURNS TABLE ( imie VARCHAR, nazwisko VARCHAR ) AS
$$
    BEGIN
        RETURN QUERY
            SELECT 
                ak.imie,
                ak.nazwisko
            FROM 
                projekt.film AS fi
                JOIN projekt.aktor_film AS akfi ON fi.id_film = akfi.id_film
                JOIN projekt.aktor AS ak ON akfi.id_aktor = ak.id_aktor
            WHERE 
                fi.id_film = id;
    END
$$
LANGUAGE plpgsql;

