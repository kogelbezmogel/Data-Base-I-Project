import psycopg2 as db
import tkinter as tk
import show_button_functions as funcs
import insert_button_functions as funci
import raport_button_functions as funcr
import client_button_functions as funcc
from functools import partial

#ustalenie połączenia z bazą danych
try:
    #conn = db.connect(user="u9walczak", password="9walczak", database="u9walczak", host="localhost", port="5432")
    conn = db.connect(user="postgres", password="maciek123", database="postgres", host="localhost", port="5432")
except:
    print("Nie poloczono")

#tworzenie głównego okna
window = tk.Tk()
window.configure( bg = "#b0ae3c" )
window.title("My app")
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()
window.geometry( "{}x{}".format(screen_w, screen_h) )

#tworzenie obszaru na tabale danych
show_table_frame = tk.Frame(window, width = "900", height= "600", bg="#616cad")
show_table_frame.place(x = 350, y = 50)

#tworzenie przycisków i przypisanie ich do funkcji pokazującuch dane
show_buttons_frame = tk.Frame(window, width = "250", bg="#b0ae3c")
show_buttons_frame.place(x = 20, y = 50)
tk.Label(window, text="Wyświetl dane", font=('Arial', 16, 'bold'), bg="#b0ae3c" ).place(x = 30, y = 20)

h = "1"
w = "13"

columns = 3
keys_list = list( funcs.func_dictionary.keys() ) 
for i in range( len(funcs.func_dictionary) ):
    x = i // columns
    y = i % columns
    button = tk.Button( show_buttons_frame, text=keys_list[i], width=w, height=h, bg="#61a0ff" )
    fun_with_binded_frame = partial( funcs.func_dictionary.get( keys_list[i] ), show_table_frame, conn )
    button.config( command = fun_with_binded_frame)
    button.grid(row=x+1, column=y)

#tworzenie przycisków i przypisanie ich do funkcji zapisujących dane 
insert_buttons_frame = tk.Frame(window, width = "250", bg="#b0ae3c")
insert_buttons_frame.place(x = 20, y = 260)
tk.Label( window, text="Dodaj dane", font=('Arial', 16, 'bold'), bg="#b0ae3c" ).place(x = 30, y = 230)

h = "1"
w = "13"

columns = 3
keys_list = list( funci.func_dictionary.keys() ) 
for i in range( len(funci.func_dictionary) ):
    x = i // columns
    y = i % columns
    button = tk.Button( insert_buttons_frame, text=keys_list[i], width=w, height=h, bg="#61a0ff" )
    fun_with_binded_frame = partial( funci.func_dictionary.get( keys_list[i] ), window, conn )
    button.config( command = fun_with_binded_frame)
    button.grid(row=x, column=y)

#tworznie przycisków i przypisanie ich do funkcji tworzących raporty
raport_buttons_frame = tk.Frame( window, width = "250", bg="#b0ae3c" )
raport_buttons_frame.place(x = 20, y = 460)
tk.Label( window, text="Generuj raport", font=('Arial', 16, 'bold'), bg="#b0ae3c" ).place(x = 30, y = 430)

h = "1"
w = "25"

keys_list = list( funcr.func_dictionary.keys() ) 
for i in range( len(funcr.func_dictionary) ):
    button = tk.Button( raport_buttons_frame, text=keys_list[i], width=w, height=h, bg="#61a0ff" )
    fun_with_binded_frame = partial( funcr.func_dictionary.get( keys_list[i] ), conn )
    button.config( command = fun_with_binded_frame)
    button.grid(row=i, column=0)

#tworznie przycisków funkcjonalności klienta
raport_buttons_frame = tk.Frame( window, width = "250", bg="#b0ae3c" )
raport_buttons_frame.place(x = 20, y = 590)
tk.Label( window, text="Klient", font=('Arial', 16, 'bold'), bg="#b0ae3c" ).place(x = 30, y = 560)

h = "1"
w = "25"

keys_list = list( funcc.func_dictionary.keys() ) 
for i in range( len(funcc.func_dictionary) ):
    button = tk.Button( raport_buttons_frame, text=keys_list[i], width=w, height=h, bg="#61a0ff" )
    fun_with_binded_frame = partial( funcc.func_dictionary.get( keys_list[i] ), window, conn )
    button.config( command = fun_with_binded_frame)
    button.grid(row=i, column=0)

window.mainloop()
conn.close()