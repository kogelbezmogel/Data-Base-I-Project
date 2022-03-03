DELETE FROM projekt.aktor_film;
DELETE FROM projekt.kategoria_film;
DELETE FROM projekt.seans_film;
DELETE FROM projekt.grafik_pracownik;
DELETE FROM projekt.bilet;
DELETE FROM projekt.klient;
DELETE FROM projekt.seans;
DELETE FROM projekt.sala;
DELETE FROM projekt.pracownik;
DELETE FROM projekt.grafik;
DELETE FROM projekt.kino;
DELETE FROM projekt.film;
DELETE FROM projekt.opis;
DELETE FROM projekt.rezyser;
DELETE FROM projekt.kategoria;
DELETE FROM projekt.aktor;


DROP VIEW oblozenie_seansow;
DROP VIEW oblozenie_kina_w_tygodniu;
DROP VIEW baza_filmow;
DROP VIEW stali_klienci;

DROP TABLE projekt.aktor_film;
DROP TABLE projekt.kategoria_film;
DROP TABLE projekt.seans_film;
DROP TABLE projekt.grafik_pracownik;
DROP TABLE projekt.film;
DROP TABLE projekt.opis;
DROP TABLE projekt.aktor;
DROP TABLE projekt.bilet;
DROP TABLE projekt.klient;
DROP TABLE projekt.seans;
DROP TABLE projekt.sala;
DROP TABLE projekt.pracownik;
DROP TABLE projekt.grafik;
DROP TABLE projekt.kino;
DROP TABLE projekt.rezyser;
DROP TABLE projekt.kategoria;

DROP FUNCTION projekt.max_miejsc;
DROP FUNCTION projekt.top_klientow;