import tkinter as tk
import tkinter.messagebox
import table_display as tab
import psycopg2 as db
from functools import partial

def clear_frame(frame) -> None:
    for widget in frame.winfo_children():
        widget.destroy()



def display_data_for_table(conn, table_name, main_frame) -> None:

    form_window = tk.Toplevel(main_frame, bg="#61a0ff")
    form_window.geometry("400x500")

    header_font = ("Arial", 18, "bold")
    label = tk.Label(form_window, font=header_font, text=table_name, bg="#61a0ff", width="15", height="3")
    label.pack(side=tk.TOP)

    cursor = conn.cursor()
    statement_for_headers = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}';".format(table_name)
    cursor.execute(statement_for_headers)
    headers = cursor.fetchall()
    headers = [ header[0] for header in headers ]

    statement_find_max_id = "SELECT {0} FROM projekt.{1} ORDER BY {0} DESC LIMIT 1".format(headers[0], table_name)
    cursor.execute(statement_find_max_id)
    next_id = cursor.fetchone()[0] + 1
    cursor.close()

    entries_frame = tk.Frame(form_window, bg="#61a0ff")
    entries_frame.pack( side = tk.TOP, pady = 30 )

    id_pair = ( "id_{}".format(table_name), str(next_id) )
    headers.remove( "id_{}".format(table_name) )

    entries = []
    for i in range( len(headers) ):
        tk.Label( entries_frame, text = "{} : ".format(headers[i]), width = "30", bg="#61a0ff" ).grid( row = i, column = 0, pady = 10 )
        pair = ( headers[i], tk.Entry(entries_frame) )
        pair[1].grid( row = i, column = 1, pady = 10 )
        entries.append(pair)

    binded_function = partial(subbmit_click, conn, entries, id_pair, table_name)

    submit = tk.Button( form_window, text="Dodaj do tabeli {}".format(table_name), command = binded_function )
    submit.pack(side = tk.BOTTOM, pady = 20 )




def subbmit_click(conn, entries, id_pair, table_name) -> None:
    
    headers = [ entrie[0] for entrie in entries ]
    values = [ str( entrie[1].get() ) for entrie in entries ]
    headers = ', '.join(headers)
    values =  "'" + "', '".join(values) + "'"
    headers = id_pair[0] + ", " + headers
    values = id_pair[1] + ", " + values

    insert_statement = "INSERT INTO projekt.{0}({1}) VALUES \n ({2});".format(table_name, headers, values)

    cursor = conn.cursor()
    try:
        cursor.execute(insert_statement)
        conn.commit()
    except Exception as e:
        conn.rollback()
        err_str = str(e)
        tk.messagebox.showinfo( "Blad", "Dane wpisane nie sa poprawne \n Wartosc bledu: \n{}".format(err_str) )

    cursor.close()



def actors_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'aktor', main_frame)
    

def categories_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'kategoria', main_frame)


def directors_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'rezyser', main_frame)


def films_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'film', main_frame)


def descripts_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'opis', main_frame)


def shows_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'seans', main_frame)


def rooms_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'sala', main_frame)


def ticekts_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'bilet', main_frame)


def clients_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'klient', main_frame)


def cinemas_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'kino', main_frame)


def schedule_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'grafik', main_frame)


def workers_button_click(main_frame, conn) -> None:
    display_data_for_table(conn, 'pracownik', main_frame)


def actor_film_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'aktor_film', frame_to_print_table)


def category_film_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'kategoria_film', frame_to_print_table)


def show_film_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'seans_film', frame_to_print_table)


def schedule_worker_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'grafik_pracownik', frame_to_print_table)


func_dictionary  = {
    "Aktorzy" : actors_button_click,
    "Kategorie" : categories_button_click,
    "Reżyserowie" : directors_button_click, 
    "Filmy" : films_button_click,
    "Opisy" : descripts_button_click,
    "Seanse" : shows_button_click,
    "Sale" : rooms_button_click,
    "Bilety" : ticekts_button_click,
    "Klienci" : clients_button_click,
    "Kina" : cinemas_button_click,
    "Grafik" : schedule_button_click,
    "Pracownicy" : workers_button_click,
    "Aktor-Film" : actor_film_button_click,
    "Film-Kategoria" : category_film_click,
    "Seans-Film" : show_film_click,
    "Grafik-Pracownik" : schedule_worker_click
}