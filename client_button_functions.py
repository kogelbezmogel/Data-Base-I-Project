import tkinter.messagebox
import tkinter as tk
from functools import partial
from tkinter.ttk import Label


def repertoire_form_button_click(window, conn) -> None:
    form_window = tk.Toplevel(window)
    form_window.geometry("300x300")

    cursor = conn.cursor()
    statement = "SELECT * FROM daty_w_repertuarze"
    dates = []
    try:
        cursor.execute(statement)
        dates = cursor.fetchall()
        dates = [ str(date[0]) for date in dates ] 
    except:
        conn.rollback()
        tk.messagebox.showinfo("Blad", "Nie udalo sie znalezc dat.")

    choices1 = dates
    variable1 = tk.StringVar(form_window)
    variable1.set( dates[0] )
    choice_box1 = tk.OptionMenu(form_window, variable1, *choices1)

    choices2 = ["Apollo", "Pod Rozbrykanym Kucykiem"]
    variable2 = tk.StringVar(form_window)
    variable2.set('Apollo')
    choice_box2 = tk.OptionMenu(form_window, variable2, *choices2)


    choice_box1.pack(side=tk.TOP, pady=10)
    choice_box2.pack(side=tk.TOP, pady=10)

    binded_function = partial(repertoir_button_click, conn, form_window, variable1, variable2)
    button = tk.Button(form_window, text="Wyswietl", command=binded_function)
    button.pack(side=tk.BOTTOM, pady=10)



def repertoir_button_click(conn, top, option1, option2) -> None:
    
    date = str (option1.get())
    cinema = str( option2.get() )
    top.destroy()
    top.update()

    cursor = conn.cursor()
    statment_for_repertoir = "SELECT * FROM projekt.repertuar_dnia('{}', '{}');".format(date, cinema)
    try: 
        cursor.execute(statment_for_repertoir)
        films = cursor.fetchall()
    except:
        conn.rollback()
        tk.messagebox.showinfo("Blad", "Nie udalo sie znalezc filmow tego dnia.")
        
    html = "<!DOCTYPE html>"
    html += "<html>"
    html += "<head>"
    html += "   <style>"
    html += "       header { font-size: 40px; font-weight: bold; text-align: center; margin: 100px;}"
    html += "       table, th, tr, td { border: 2px solid black; border-collapse: collapse; text-align: center; }"
    html += "       th { font-weight: bold; }"
    html += "       h1 { font-size: 40px; font-weight: bold; }"
    html += "   </style>"
    html += "   <meta charset='utf-8' />"
    html += "   <title> Raport popularnosci filmow </title>"
    html += "</head>"
    html += "<body>"
    html += "   <header> Repertuar na dzien: . </header>".format(date)
    for film in films:

        statement_for_category = "SELECT * FROM projekt.kategorie_filmu({})".format(film[1])
        statement_for_actors = "SELECT * FROM projekt.aktorzy_filmu({})".format(film[1])
        statement_for_time = "SELECT * FROM projekt.seans WHERE id_seans = {}".format(film[0])
        statement_for_adds = "SELECT * FROM projekt.film WHERE id_film = {}".format(film[1])
        time = []
        actors = []
        categories = []
        adds = []
        try :
            cursor.execute(statement_for_category)
            categories = cursor.fetchall()
            categories = [ cat[0] for cat in categories ]
            
            cursor.execute(statement_for_actors)
            actors = cursor.fetchall()
            
            cursor.execute(statement_for_time)
            time = cursor.fetchone()

            cursor.execute(statement_for_adds)
            adds = cursor.fetchone()

            statement_for_description = "SELECT * FROM projekt.opis WHERE id_opis = {}".format(adds[2])
            cursor.execute(statement_for_description)
            description = cursor.fetchone()

            statement_for_director = "SELECT * FROM projekt.rezyser WHERE id_rezyser = {}".format(adds[1])
            cursor.execute(statement_for_director)
            director = cursor.fetchone()
        
        except Exception as e:
            conn.rollback()

        html += "<p> <h1> {} </br> godzina: {} - {} </h1> </p>".format( adds[3], time[2],time[3] )
        html += "<p>"
        html += "   Kategoria: {} </br>".format( "/".join(categories) )
        html += "   Rezyser: {} {} </br>".format( director[1], director[2] )
        html += "   Data premiery: {} </br>".format( adds[4] )
        html += "</p>"
        html += "<p> Aktorzy : <ul>" 
        for actor in actors:
            html += "<li> {} {} </li>".format( actor[0], actor[1] )    
        html += "</ul> </p>"
        html += "<div>"
        html += "   <p> {} </p>".format( description[1] )
        html += "</div> </br></br></br>"


    html += "</body>"
    html += "</html>"
        
    with open('Raporty/repertuar.html', 'w') as f:
        f.write(html)
    tk.messagebox.showinfo("Informacja", "Repertuar zostal zapisany w folderze: \"Raporty\".")




def tickets_buy_form_button_click(window, conn) -> None:

    form_window = tk.Toplevel(window)
    form_window.geometry("500x300")

    label_name = tk.Label(form_window, text="Imie: ", font=('Arial', 15))
    entry_name = tk.Entry(form_window)

    label_lname = tk.Label(form_window, text="Nazwisko: ", font=('Arial', 15))
    entry_lname = tk.Entry(form_window)

    label_phone = tk.Label(form_window, text="telefon: ", font=('Arial', 15))
    entry_phone = tk.Entry(form_window)

    label_title = tk.Label(form_window, text="Tytul: ", font=('Arial', 15))
    entry_title = tk.Entry(form_window)

    label_time = tk.Label(form_window, text="Godzina senasu: ", font=('Arial', 15))
    entry_time = tk.Entry(form_window)

    label_date = tk.Label(form_window, text="Data senasu: ", font=('Arial', 15))
    entry_date = tk.Entry(form_window)

    choices1 = ['bez ulgi', 'studencka']
    variable1 = tk.StringVar(form_window)
    variable1.set('bez ulgi')
    choice_box1 = tk.OptionMenu(form_window, variable1, *choices1)

    choices2 = ['Apollo', 'Pod Rozbrykanym Kucykiem']
    variable2 = tk.StringVar(form_window)
    variable2.set('Apollo')
    choice_box2 = tk.OptionMenu(form_window, variable2, *choices2)

    label_name.grid(row=0, column=0)
    entry_name.grid(row=0, column=1)

    label_lname.grid(row=1, column=0)
    entry_lname.grid(row=1, column=1)
    
    label_phone.grid(row=2, column=0)
    entry_phone.grid(row=2, column=1)
    
    label_title.grid(row=3, column=0)
    entry_title.grid(row=3, column=1)
    
    label_time.grid(row=4, column=0)
    entry_time.grid(row=4, column=1)

    label_date.grid(row=5, column=0)
    entry_date.grid(row=5, column=1)

    choice_box1.grid(row=6, column=1)
    choice_box2.grid(row=7, column=1)

    entries = [entry_name, entry_lname, entry_phone, entry_time, entry_date, entry_title]
    options = [variable1, variable2]
    
    binded_function = partial(buy_ticket, conn, entries, options, form_window)
    button = tk.Button(form_window, text="Kup", command=binded_function)
    button.grid(row=9, column=1, pady=30)




def buy_ticket(conn, entries, options, top) -> None:
    
    cursor = conn.cursor()

    statement_find_max_id = "SELECT {0} FROM projekt.{1} ORDER BY {0} DESC LIMIT 1".format('id_klient', 'klient')
    cursor.execute(statement_find_max_id)
    next_id = cursor.fetchone()[0] + 1

    name = entries[0].get()
    lname = entries[1].get()
    phone = entries[2].get()
    id_client = next_id
    value = [ str(name), str(lname), str(phone) ]
    value =  "'"+ "' ,'".join(value) + "'"
    value = str(id_client) + ", " + value
    statement = "INSERT INTO projekt.klient(id_klient, imie, nazwisko, telefon) VALUES ({})".format(value)

    try:
        cursor.execute(statement)
        conn.commit()

        statement_find_max_id = "SELECT {0} FROM projekt.{1} ORDER BY {0} DESC LIMIT 1".format('id_bilet', 'bilet')
        cursor.execute(statement_find_max_id)
        next_id = cursor.fetchone()[0] + 1

        statement_show_id = '''
        SELECT
            se.id_seans
        FROM projekt.seans AS se 
            JOIN projekt.seans_film AS sefi ON se.id_seans = sefi.id_seans
            JOIN projekt.film AS fi ON sefi.id_film = fi.id_film
        WHERE
            se.poczatek_seansu = '{}' AND fi.tytul = '{}' AND se.data_seansu = '{}'
        '''.format( entries[3].get(), entries[5].get(), entries[4].get() )

        cursor.execute(statement_show_id)
        showid = cursor.fetchone()[0]

        id_ticket = next_id
        id_show = showid
        if options[0].get() == 'bez ulgi':
            price = '18'
        else:
            price = '15'
        relief = options[0].get()
        payment_form = 'online'

        value = [ str(relief), str(price), str(payment_form) ]
        value =  "'"+ "' ,'".join(value) + "'"
        value = str(id_ticket) + ", " + str(id_client) + ", " + str(id_show) + ", " + value
        statement = "INSERT INTO projekt.bilet(id_bilet, id_klient, id_seans, ulga, cena, forma_platnosci) VALUES ({})".format(value)
        try:
            cursor.execute(statement)
            conn.commit()
            tk.messagebox.showinfo("Informacja", "Bilet zakupiony.")
        except:
            conn.rollback()
            tk.messagebox.showinfo("Blad", "Nie dodano biletu.")
        top.destroy()
        top.update()
    
    except:
        conn.rollback()
        tk.messagebox.showinfo("Blad", "Nie poprawne informacje klienta.")

    cursor.close()

    





func_dictionary  = {
    "Repertuar" : repertoire_form_button_click,
    "Kup bilet" : tickets_buy_form_button_click
}