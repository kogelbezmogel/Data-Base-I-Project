import tkinter.messagebox
import tkinter as tk
import table_display as tab
import psycopg2 as db
import matplotlib.pyplot as plt




def clients_for_day_button_click(conn) -> None:
    cursor = conn.cursor()

    raport_statement = "SELECT * FROM oblozenie_kina_w_tygodniu;"

    try:
        cursor.execute(raport_statement)
        data = cursor.fetchall()
    except Exception as e:
        conn.rollback()
    cursor.close()

    cinemas = set( [x[0] for x in data ] )

    html = "<!DOCTYPE html>"
    html += "<html>"
    html += "<head>"
    html += "   <style>"
    html += "       header { font-size: 40px; font-weight: bold; text-align: center; margin: 100px;}"
    html += "       table, th, tr, td { border: 1px solid black; border-collapse: collapse; text-align: center; margin-left: 50px; }"
    html += "       th { font-weight: bold; }"
    html += "       h1 { font-size: 25px; font-weight: bold; }"
    html += "   </style>"
    html += "   <meta charset='utf-8' />"
    html += "   <title> Raport odwiedzajacych w tygodniu </title>"
    html += "</head>"
    html += "<body>"
    html += "   <header> Raport pokazuje ilosc wizytujacych w zaleznosci od daty w danym kinie. </header>"
    
    for cinema  in cinemas:
        values = []
        argues = []
        html += "<p> <h1> &#8226; {} </h1> </p>".format(cinema)
        html += "<p> <table>" #tabela
        html += "<tr>" 
        html += "   <th> Data </th>"
        html += "   <th> Ilosc klientow </th>"
        html += "</tr>"

        for x in data:
            if x[0] == cinema:
                argues.append( str( x[1] ) ) #dzien
                values.append( x[2] ) #ilosc
                f = plt.figure()
                f.set_figwidth(10)
                f.set_figheight(5)
                plt.xlabel("Data")
                plt.ylabel("Ilość klientów")

                plt.plot(argues, values, marker="o")
                plt.ylim( 0, max(values) + 1 )
                plt.savefig( "Raporty/r1_plots/{}_r1.png".format(cinema) )
                html += "<tr>" 
                html += "   <td> {} </td>".format(x[1])
                html += "   <td> {} </td>".format(x[2])
                html += "</tr>"
                plt.close('all')
        html += "</table> </p>" # koniec tabeli
        html += "<p> <img src='r1_plots/{}_r1.png' alt='Wykres mial tu byc'> </br></br></br></br> </p>".format(cinema)

    html += "</body>"
    html += "</html>"

    with open('Raporty/raport1.html', 'w') as f:
        f.write(html)
    tk.messagebox.showinfo("Inforamcja", "Raport ruchu w kinie zostal zapisany w folderze: \"Raporty\".")



    
def tickets_for_show_button_click(conn) -> None: #mozna dodac godziny seansow zamiast numerow
    cursor = conn.cursor()

    raport_statement = "SELECT * FROM oblozenie_seansow;"
    
    try:
        cursor.execute(raport_statement)
        data = cursor.fetchall()
    except Exception as e:
        conn.rollback()

    cursor.close()

    shows = set( [x[0] for x in data ] )

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
    html += "   <header> Raport pokazuje jak zmienia sie popularnosc filmow na przestrzeni czasu. </header>"

    for show in shows:
        html += "<p> <h1> {} </h1> </p>".format(show)
        html += "<p> <table>" #tabela
        html += "<tr>" 
        html += "   <th> id_seansu </th>"
        html += "   <th> data seansu </th>"
        html += "   <th> kupione bilety </th>"
        html += "   <th> ilosc miejsc </th>"
        html += "</tr>"
        for x in data:
            if x[0] == show:
                html += "<tr>" 
                html += "   <td> {} </td>".format(x[1])
                html += "   <td> {} </td>".format(x[2])
                html += "   <td> {} </td>".format(x[4])
                html += "   <td> {} </td>".format(x[5])
                html += "</tr>"

        html += "</table> </p> </br></br></br>" # koniec tabeli

    html += "</body>"
    html += "</html>"
        
    with open('Raporty/raport2.html', 'w') as f:
        f.write(html)
    tk.messagebox.showinfo("Informacja", "Raport popularnosci filmow zostal zapisany w folderze: \"Raporty\".")




def baza_filmow_button_click(conn) -> None:
    cursor = conn.cursor()

    raport_statement = "SELECT * FROM baza_filmow;"

    try:
        cursor.execute(raport_statement)
        films = cursor.fetchall()
    except Exception as e:
        conn.rollback()

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
    html += "   <header> Raport pokazuje dokladne informacje na temat filmow w bazie. </header>"

    for film in films:

        statement_for_category = "SELECT * FROM projekt.kategorie_filmu({})".format(film[0])
        statement_for_actors = "SELECT * FROM projekt.aktorzy_filmu({})".format(film[0])
        actors = []
        categories = []
        try :
            cursor.execute(statement_for_category)
            categories = cursor.fetchall()
            categories = [ cat[0] for cat in categories ]
            cursor.execute(statement_for_actors)
            actors = cursor.fetchall()
        except Exception as e:
            conn.rollback()

        html += "<p> <h1> {} </h1> </p>".format( film[1] )
        html += "<p>"
        html += "   Kategoria: {} </br>".format( "/".join(categories) )
        html += "   Rezyser: {} {} </br>".format( film[2], film[3] )
        html += "   Data premiery: {} </br>".format( film[4] )
        html += "   Dlugosc: {} min </br>".format( film[5] )
        html += "</p>"
        html += "<p> Aktorzy : <ul>" 
        for actor in actors:
            html += "<li> {} {} </li>".format( actor[0], actor[1] )    
        html += "</ul> </p>"
        html += "<div>"
        html += "   <p> {} </p>".format( film[6] )
        html += "</div> </br></br></br>"
                
    html += "</body>"
    html += "</html>"
        
    with open('Raporty/raport3.html', 'w') as f:
        f.write(html)
    tk.messagebox.showinfo("Informacja", "Raport bazy filmow zostal zapisany w folderze: \"Raporty\".")
    cursor.close()




func_dictionary  = {
    "Ilość klientów w ciągu dnia" : clients_for_day_button_click,
    "Ilości kupowanych biletów" : tickets_for_show_button_click,
    "Baza filmow" : baza_filmow_button_click
}