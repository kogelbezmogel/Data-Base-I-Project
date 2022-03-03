CREATE OR REPLACE FUNCTION projekt.input_aktor()
    RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $$
        BEGIN
            NEW.imie := INITCAP(NEW.imie);
            NEW.nazwisko := INITCAP(NEW.nazwisko);
            RETURN NEW;
        END
    $$;

CREATE TRIGGER input_aktor_trigger BEFORE INSERT ON projekt.aktor
    FOR EACH ROW EXECUTE PROCEDURE projekt.input_aktor();





CREATE OR REPLACE FUNCTION projekt.input_rezyser()
    RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $$
        BEGIN
            NEW.imie := INITCAP(NEW.imie);
            NEW.nazwisko := INITCAP(NEW.nazwisko);
            RETURN NEW;
        END
    $$;

CREATE TRIGGER input_rezyser_trigger BEFORE INSERT ON projekt.rezyser
    FOR EACH ROW EXECUTE PROCEDURE projekt.input_rezyser();





CREATE OR REPLACE FUNCTION projekt.input_klient()
    RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $$
        BEGIN
            NEW.imie := INITCAP(NEW.imie);
            NEW.nazwisko := INITCAP(NEW.nazwisko);
            IF NOT (NEW.telefon ~ '^[0-9]+$') THEN
                RAISE EXCEPTION 'wrong_number';
            END IF;
            RETURN NEW;
        END
    $$;

CREATE TRIGGER input_klient_trigger BEFORE INSERT ON projekt.klient
    FOR EACH ROW EXECUTE PROCEDURE projekt.input_klient();




CREATE OR REPLACE FUNCTION projekt.input_pracownik()
    RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $$
        BEGIN
            NEW.imie := INITCAP(NEW.imie);
            NEW.nazwisko := INITCAP(NEW.nazwisko);
            IF NOT (NEW.telefon ~ '^[0-9]+$') THEN
                RAISE EXCEPTION 'wrong_number';
            END IF;
            RETURN NEW;
        END
    $$;

CREATE TRIGGER input_pracownik_trigger BEFORE INSERT ON projekt.pracownik
    FOR EACH ROW EXECUTE PROCEDURE projekt.input_pracownik();



CREATE OR REPLACE FUNCTION projekt.input_bilet()
    RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $$
        BEGIN
            IF (NEW.forma_platnosci != 'online' AND NEW.forma_platnosci != 'lokal') THEN
                RAISE EXCEPTION 'wrong_payment_method';
            END IF;
            IF (NEW.ulga != 'bez ulgi' AND NEW.ulga != 'studencka') THEN
                RAISE EXCEPTION 'wrong_discount';
            END IF;
            RETURN NEW;
        END
    $$;

CREATE TRIGGER input_bilet_trigger BEFORE INSERT ON projekt.bilet
    FOR EACH ROW EXECUTE PROCEDURE projekt.input_bilet();




DROP TRIGGER input_aktor_trigger ON projekt.aktor;
DROP FUNCTION  projekt.input_aktor;

DROP TRIGGER input_rezyser_trigger ON projekt.rezyser;
DROP FUNCTION projekt.input_rezyser;

DROP TRIGGER input_klient_trigger ON projekt.klient;
DROP FUNCTION projekt.input_klient;

DROP TRIGGER input_bilet_trigger ON projekt.bilet;
DROP FUNCTION projekt.input_bilet;



