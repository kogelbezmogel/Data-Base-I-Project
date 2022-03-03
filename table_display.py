import tkinter as tk
import tkinter.messagebox

class Table:

    def __init__(self, master, data, headers) -> None:
        rows = len(data)
        columns = len(headers)


        def scroll_function(event):
            canvas.configure(scrollregion=canvas.bbox("all"),width=900,height=600)

        #adding scrollbar layouts there need to be frame inside canvas inside frame
        canvas = tk.Canvas(master, bg="#616cad")
        frame_inside_canvas = tk.Frame(canvas)
        w_scroll = tk.Scrollbar( master, orient='horizontal', command=canvas.xview, bg="#a17c02" )
        h_scroll = tk.Scrollbar( master, orient='vertical', command=canvas.yview )
        canvas.configure(yscrollcommand = h_scroll.set)
        canvas.configure(xscrollcommand = w_scroll.set)
        h_scroll.pack(side = tk.LEFT, fill="y")
        w_scroll.pack(side = tk.TOP, fill='x')
        canvas.pack(side=tk.LEFT)
        canvas.create_window( (0,0), window = frame_inside_canvas, anchor='nw' )
        frame_inside_canvas.bind("<Configure>",scroll_function)


        #adjusting width of columns
        adjusted_width = []
        for j in range(columns):
            max_len = -1
            for i in range(rows): #checking rows
                if len( str( data[i][j] ) ) > max_len:
                    max_len = len( str( data[i][j] ) )
            if len( str( headers[j] ) ) > max_len: #checking header
                max_len = len( str( headers[j] ) )
            adjusted_width.append(max_len + 3)


        header_font = ("Arial", 8, "bold")
        for j in range(columns):
            self.entry = tk.Entry( frame_inside_canvas, width = adjusted_width[j], relief = "solid", font = header_font, bd = "1")
            self.entry.insert( tk.END, headers[j] )
            self.entry.config( readonlybackground="#616cad" )
            self.entry.config( state = "readonly")  
            self.entry.grid( row = 0, column = j )

        data_font = ("Arial", 8)
        for i in range(rows):
            for j in range(columns):
                self.entry = tk.Entry( frame_inside_canvas, width = adjusted_width[j], relief = "solid", font = data_font, bd = "1" )
                self.entry.insert( tk.END, data[i][j] ) 
                self.entry.config( readonlybackground="#aed6d3" )
                self.entry.config(state = "readonly")
                self.entry.grid(row = i+1, column = j)
        if not data: #no data, one row for estetics
            for j in range(columns):
                self.entry = tk.Entry( frame_inside_canvas, width = adjusted_width[j], relief = "solid", font = data_font, bd = "1" )
                self.entry.config( readonlybackground="#aed6d3" )
                self.entry.config(state = "readonly")
                self.entry.grid(row = 1, column = j)

