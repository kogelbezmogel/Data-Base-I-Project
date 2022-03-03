import tkinter.messagebox
import tkinter as tk
import table_display as tab
import psycopg2 as db
from functools import partial

def clear_frame(frame) -> None:
    for widget in frame.winfo_children():
        widget.destroy()



def display_data_for_table(conn, table_name, frame_to_print_table):
    clear_frame(frame_to_print_table)
    cursor = conn.cursor()

    statement_for_headers = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}';".format(table_name)

    try:
        cursor.execute(statement_for_headers)
        headers = cursor.fetchall()
    except Exception as e:
        conn.rollback()

    headers = [ header[0] for header in headers ]
    str = ', '.join(headers)

    statement_for_data = "SELECT {} FROM projekt.{};".format(str, table_name)

    try:
        cursor.execute(statement_for_data)
        data = cursor.fetchall()
    except Exception as err:
        conn.rollback()
        tk.messagebox.showinfo( "Blad", "Cos poszlo nie tak \n {}".format(str(err))  )    

    tab.Table(frame_to_print_table, data, headers)
    cursor.close()



def actors_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'aktor', frame_to_print_table)
    

def categories_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'kategoria', frame_to_print_table)


def directors_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'rezyser', frame_to_print_table)


def films_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'film', frame_to_print_table)


def descripts_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'opis', frame_to_print_table)


def shows_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'seans', frame_to_print_table)


def rooms_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'sala', frame_to_print_table)


def ticekts_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'bilet', frame_to_print_table)


def clients_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'klient', frame_to_print_table)


def cinemas_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'kino', frame_to_print_table)


def schedule_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'grafik', frame_to_print_table)


def workers_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'pracownik', frame_to_print_table)


def actor_film_button_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'aktor_film', frame_to_print_table)


def category_film_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'kategoria_film', frame_to_print_table)


def show_film_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'seans_film', frame_to_print_table)


def schedule_worker_click(frame_to_print_table, conn) -> None:
    display_data_for_table(conn, 'grafik_pracownik', frame_to_print_table)


def top_clients_click(frame_to_print_table, conn) -> None:

    form_window = tk.Toplevel(frame_to_print_table, bg="#61a0ff")
    form_window.geometry("300x300")
    label = tk.Label(form_window, text="Podaj dolny limit \n odwiedzin klienta", font=('Arial', 20, 'bold'), bg="#61a0ff")
    entry = tk.Entry(form_window)
    label.pack(side=tk.TOP, pady=10)
    entry.pack(side=tk.TOP, pady=10)
    binded_function = partial(submited_for_top_clients, frame_to_print_table, conn, entry)
    button = tk.Button(form_window, text="Wyswietl", bg="#61a0ff", command=binded_function)
    button.pack(side=tk.BOTTOM, pady=30)
    


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
    "Grafik-Pracownik" : schedule_worker_click,
    "Najczestsi klienci" : top_clients_click
}

def submited_for_top_clients(frame_to_print_table, conn, entry) -> None:
    statement = "SELECT * FROM projekt.top_klientow({});".format( entry.get() )

    clear_frame(frame_to_print_table)
    cursor = conn.cursor()

    try:
        cursor.execute(statement)
        data = cursor.fetchall()
    except Exception as e:
        conn.rollback()
    
    headers = [ header[0] for header in cursor.description ]

    tab.Table(frame_to_print_table, data, headers)
    cursor.close()