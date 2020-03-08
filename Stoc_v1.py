#python3 -X faulthandler testframes.py


import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
import time
from tkinter import messagebox
import datetime
from PIL import ImageTk,Image
import mysql.connector
from tkinter import ttk
import csv
import os
import sys

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=13, weight="bold", slant="italic")
        self.geometry("1360x730-1+1")
        self.resizable(False, False)
        #bitmap = 'db.ico'
        #self.iconbitmap(bitmap)
        #img = PhotoImage("bivaria.png")
        img= ImageTk.PhotoImage(Image.open("db.png"))
        self.tk.call('wm', 'iconphoto', self._w, img)
        #self.iconphoto(False, img)
        #self.tk.call('wm', 'icon
        #photo', self._w, ImageTk.PhotoImage(Image.open("db.png")))
        self.title("Bivaria stoc app")


        #self.configure(bg ="ghostwhite")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='ghostwhite')
        self.controller = controller
        #self.select_item = ''
        label = tk.Label(self, text="Stoc echipamente", font=controller.title_font, bg='ghostwhite')
        label.pack(side="top", fill="x", pady=20)
        self.option_add('*Dialog.msg.font', 'Calibri 16 bold')
        tk.messagebox.showinfo("", "Buna dimineata Tudor!", icon='info')

        button1 = tk.Button(self, text="Evidenta tub rasina",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Evidenta echipamente service",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.place(x=10, y=10, width=240)
        button1.config(borderwidth=0, bg='ghostwhite', font=(12))
        button2.place(x=250, y=10, width=240)
        button2.config(borderwidth=0, bg='ghostwhite', font=(12))
        #button1.pack()
        #button2.pack()
        comboBox = ttk.Combobox(self,
                            values=[
                                    "Model",
                                    "Serie",
                                    "Client",
                                    "Data Intrare",
                                    "Tip Iesire"], width=12, height=12, font=('bold', 12))
        comboBox.place(x=1100, y=113)
        comboBox.config(font=12, foreground='black', background='ghostwhite', justify='center')
        comboBox.set('Serie')
        #comboBox.config(bg='ghostwhite')
        #comboBox.pack()
        entry_search = tk.Entry(self,width=10, bg='ghostwhite')
        entry_search.place(x=1000, y=112)
        entry_search.config(font=10.5)
        #entry_search.pack()
        prod_label = tk.Label(self, text = 'Producator', font=('bold', 12), bg='ghostwhite')
        prod_label.place(x=20, y=60)
        producator = tk.Entry(self, width=15, bg='ghostwhite',borderwidth=0.5)
        producator.place(x=160,y=60)
        producator.config(font=11)
        #producator.grid(row=0, column=2, pady=5, sticky=N+S+W, columnspan=2)
        #producator.insert(END,"")

        model_label = tk.Label(self, text = 'Model', font=('bold', 12),bg='ghostwhite')
        #model_label.grid(row=1, column=0, pady=5, columnspan=2, sticky=N+S+W, padx=20)
        model_label.place(x=20, y=90)
        model = tk.Entry(self,width=15, bg='ghostwhite', borderwidth=0.5)
        #model.grid(row=1, column=2, pady=5, sticky=N+S+W, columnspan=2)
        model.place(x=160,y=90)
        model.config(font=11)
        #model.config(font="bold")
        #model.insert(END,"")


        serie_label = tk.Label(self, text = 'Serie', font=('bold', 12), bg='ghostwhite')
        #serie_label.grid(row=2, column=0, pady=5, columnspan=2, sticky=N+S+W, padx=20)
        serie_label.place(x=20,y=120)
        serie = tk.Entry(self,width=25, bg='ghostwhite', borderwidth=0.5)
        #serie.grid(row=2, column=2, sticky=N+S+W, pady=5, columnspan=2)
        serie.place(x=160,y=120)
        serie.config(font=11)
        #serie.config(font="bold")
        #serie.insert(END,"")

        datafab_label = tk.Label(self, text = 'Data fabricatie', font=('bold', 12), bg='ghostwhite')
        #datafab_label.grid(row=3, column=0, columnspan=2, pady=5, sticky=N+S+W, padx=20)
        datafab_label.place(x=20, y=150)
        data_fab = tk.Entry(self, bg='ghostwhite', width=12, font=(12), borderwidth=0.5)
        #data_fab.grid(row=3, column=2, sticky=N+S+W, pady=5)
        data_fab.place(x=160,y=150)
        data_fab.config(font=11)
        #data_fab.config(font="bold")
        #data_fab.insert(END,"")

        datain_label = tk.Label(self, text = 'Data intrare', font=('bold', 12), bg='ghostwhite')
        #datain_label.grid(row=0, column=4, pady=5, padx=10)
        datain_label.place(x=20, y=180)
        data_in = tk.Entry(self, bg='ghostwhite', borderwidth=0.5, width=12, font=(12))
        #data_in.grid(row=0, column=5, sticky=N+S+W, pady=5)
        data_in.place(x=160,y=180)
        data_in.config(font=11)
        #data_in.config(font="bold")
        #data_in.insert(END,"xxx")

        dataout_label = tk.Label(self, text = 'Data iesire', font=('bold', 12), bg='ghostwhite')
        #dataout_label.grid(row=1, column=4,pady=5,padx=10)
        dataout_label.place(x=20, y=210)
        data_out = tk.Entry(self,width=12, bg='ghostwhite', font=(12), borderwidth=0.5)
        #data_out.grid(row=1, column=5, sticky=N+S+W, pady=5)
        data_out.place(x=160,y=210)
        data_out.config(font=11)
        #data_out.config(font="bold")
        #data_out.insert(END,"")
        clientid_label = tk.Label(self, text = 'Client', font=('bold', 12), bg='ghostwhite')
        #clientid_label.grid(row=2, column=4,pady=5, padx=10)
        clientid_label.place(x=20, y=240)
        clientid = tk.Entry(self,width=40, bg='ghostwhite', font=( 12), borderwidth=0.5)
        #clientid.grid(row=2, column=5, sticky=N+S+W, pady=5)
        clientid.place(x=160,y=240)
        clientid.config(font=11)
        #clientid.config(font="bold")
        #clientid.insert(END,"")

        tipiesire_label = tk.Label(self, text = 'Tip iesire', font=('bold', 12), bg='ghostwhite')
        #tipiesire_label.grid(row=3, column=4,pady=5, padx=10)
        tipiesire_label.place(x=20, y=270)
        tip_iesire = tk.Entry(self,width=20, bg='ghostwhite', borderwidth=0.5)
        #tip_iesire.grid(row=3, column=5, sticky=N+S+W, pady=5)
        tip_iesire.place(x=160,y=270)
        tip_iesire.config(font=11)

        obs_label = tk.Label(self, text='Observatii', font=('bold', 12), bg='ghostwhite')
        #obs_label.grid(row=0, column=6, pady=5, padx=10)
        obs_label.place(x=20, y=300)
        obs = tk.Entry(self,width=60, bg='ghostwhite', borderwidth=0.5)
        #obs.grid(row=0, column=8, sticky=N+S+W, pady=5, columnspan=2)
        obs.place(x=160,y=300)
        obs.config(font=11)
        #obs.config(font="bold")
        #obs.insert(END,"")

        cale_exp = tk.Entry(self,width=20, bg='ghostwhite', borderwidth=0.5)
        cale_exp.place(x=720,y=170)
        cale_exp.config(font=11)
        cale_exp.insert(tk.END, '/home/marius/test.csv')

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Calibri', 12))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 12,'bold'), foreground="black")

        #style.layout("mystyle.Treeview", [('mystyle.SearchView.treearea', {'sticky': 'nswe'})]) # Remove the borders
        SearchView=ttk.Treeview(self, columns=(1,2,3,4,5,6,7,8,9), show="headings", height=23, style="mystyle.Treeview")
        #SearchView['columns']=("producator","model","serie","data_fab","data_in","data_instalare", "client_id", "tip_inst", "observatii")
        #SearchView.grid(row=0,column=0,columnspan=9)
        SearchView.place(x=5,y=350, width=1335, height=375)

        SearchView.heading(1,text="Producator")
        #SearchView.column(1,anchor="center",width=20,stretch=tk.NO)
        SearchView.column(1, width=110, minwidth=90, anchor='center')
        SearchView.heading(2,text="Model")
        SearchView.column(2, width=90, minwidth=80, anchor='center')
        SearchView.heading(3,text="Serie")
        SearchView.column(3, width=160, minwidth=90, anchor='center')
        SearchView.heading(4,text="Data fabricatiei")
        SearchView.column(4, width=160, minwidth=90, anchor='center')
        SearchView.heading(5,text="Data intrare")
        SearchView.column(5,width=120, minwidth=90, anchor='center')
        SearchView.heading(6,text="Data instalare")
        SearchView.column(6,width=130, minwidth=90, anchor='center')
        SearchView.heading(7,text="Client")
        SearchView.column(7,width=130, minwidth=90, anchor='center')
        SearchView.heading(8,text="Tip Instalare")
        SearchView.column(8,width=130, minwidth=90, anchor='center')
        SearchView.heading(9,text="Observatii")
        SearchView.column(9,width=320, minwidth=120, anchor='center')
        yscrollbar = ttk.Scrollbar(self, orient="vertical", command=SearchView.yview)
        SearchView['yscrollcommand'] = yscrollbar.set
        yscrollbar.place(x=1340, y=350, height=380)
        
        def on_double_click(event):
            item = SearchView.focus()
            #selection = str(SearchView.item(item)["values"][1])
            #print(selection)
            producator.delete(0, END)
            producator.insert(tk.END, str(SearchView.item(item)["values"][0]))
            model.delete(0, END)
            model.insert(tk.END, str(SearchView.item(item)["values"][1]))
            serie.delete(0, END)
            serie.insert(tk.END, str(SearchView.item(item)["values"][2]))
            data_fab.delete(0, END)
            data_fab.insert(tk.END, str(SearchView.item(item)["values"][3]))
            data_in.delete(0, END)
            data_in.insert(tk.END, str(SearchView.item(item)["values"][4]))
            data_out.delete(0, END)
            if str(SearchView.item(item)["values"][5]) == 'None':
                data_out.insert(tk.END, '')
            else :
                data_out.insert(tk.END, str(SearchView.item(item)["values"][5]))
            clientid.delete(0, END)
            if str(SearchView.item(item)["values"][6]) == 'None':
                clientid.insert(tk.END, '')
            else:
                clientid.insert(tk.END, str(SearchView.item(item)["values"][6]))
            tip_iesire.delete(0, END)
            if str(SearchView.item(item)["values"][7]) == 'None':
                tip_iesire.insert(tk.END, '')
            else:
                tip_iesire.insert(tk.END, str(SearchView.item(item)["values"][7]))
            obs.delete(0, END)
            if str(SearchView.item(item)["values"][8]) == 'None':
                obs.insert(tk.END, '') 
            else : 
                obs.insert(tk.END, str(SearchView.item(item)["values"][8])) 
        SearchView.bind("<Double-Button-1>", on_double_click)
        def get():
            try:
                data = entry_search.get()
                #print(data)
                #print(comboBox.get())
                if data == '' and comboBox.get() == '' :
                    tk.messagebox.showinfo("Eroare", "Selectati si introduceti criteriul de cautare", icon='warning')
                elif data != '' and comboBox.get() == '' :
                    tk.messagebox.showinfo("Eroare", "Introduceti criteriul de cautare", icon='warning')
                elif data == '' and comboBox.get() != '' :
                    tk.messagebox.showinfo("Eroare", "Introduceti criteriul de cautare", icon='warning')
                elif comboBox.get() == 'Model' and data != '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("SELECT model, producator, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc WHERE model = '"+data+"'")
                    rows = my_cursor.fetchall()
                    #print(rows)
                    for i in SearchView.get_children():
                        SearchView.delete(i)
                    for row in rows:
                        SearchView.insert('', 'end', values=row)
                    mydb.commit()
                    mydb.close()
                elif comboBox.get() == 'Serie' and data != '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("SELECT producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc WHERE seria = '"+data+"'")
                    rows = my_cursor.fetchall()
                    #print(rows)
                    for i in SearchView.get_children():
                        SearchView.delete(i)
                    for row in rows:
                        SearchView.insert('', 'end', values=row)
                    mydb.commit()
                    mydb.close()
                elif comboBox.get() == 'Data Intrare' and data != '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        #auth_plugin = "mysql_native_password",
                        database = "stocdb",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("SELECT producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc WHERE data_intrare = '"+data+"'")
                    rows = my_cursor.fetchall()
                    #print(rows)
                    for i in SearchView.get_children():
                        SearchView.delete(i)
                    for row in rows:
                        SearchView.insert('', 'end', values=row)
                    mydb.commit()
                    mydb.close()
                elif comboBox.get() == 'Client' and data != '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        #auth_plugin = "mysql_native_password",
                        database = "stocdb",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("SELECT producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc WHERE client_id = '"+data+"'")
                    rows = my_cursor.fetchall()
                    #print(rows)
                    for i in SearchView.get_children():
                        SearchView.delete(i)
                    for row in rows:
                        SearchView.insert('', 'end', values=row)
                    mydb.commit()
                    mydb.close()
                elif comboBox.get() == 'Data Intrare' and data != '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        #auth_plugin = "mysql_native_password",
                        database = "stocdb",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("SELECT producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc WHERE data_intrare = '"+data+"'")
                    rows = my_cursor.fetchall()
                    #print(rows)
                    for i in SearchView.get_children():
                        SearchView.delete(i)
                    for row in rows:
                        SearchView.insert('', 'end', values=row)
                    mydb.commit()
                    mydb.close()
                elif comboBox.get() == 'Tip Iesire' and data != '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        #auth_plugin = "mysql_native_password",
                        database = "stocdb",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("SELECT producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc WHERE tip_inst = '"+data+"'")
                    rows = my_cursor.fetchall()
                    #print(rows)
                    for i in SearchView.get_children():
                        SearchView.delete(i)
                    for row in rows:
                        SearchView.insert('', 'end', values=row)
                    mydb.commit()
                    mydb.close()
            except:
                tk.messagebox.showinfo("Eroare", "Este posibil ca serverul sa nu functioneze, sau nu sunteti conectat la o retea", icon='warning')

        def getAll():
            try:
                mydb = mysql.connector.connect(
                    host = "192.168.10.59",
                    user = "marius",
                    passwd = "Mazdarx8@",
                    database = "stocdb",
                    #auth_plugin = "mysql_native_password",
                    )
                my_cursor = mydb.cursor()
                my_cursor.execute("SELECT producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc")
                rows = my_cursor.fetchall()
                for i in SearchView.get_children():
                        SearchView.delete(i)
                for row in rows:
                    SearchView.insert('', 'end', values=row)
                mydb.commit()
                mydb.close()
            except:
                tk.messagebox.showinfo("Eroare", "Este posibil ca serverul sa nu functioneze, sau nu sunteti conectat la o retea", icon='warning')

        def save():
            try:
                if data_out.get() == '' and clientid.get() == '' and tip_iesire.get() == '' and obs.get() == '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare) VALUES (%s, %s, %s, %s, %s)"
                    #sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare) VALUES (%s, %s, %s, %s)"
                    record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get())
                    my_cursor.execute(sqlStuff, record)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    data_out.delete(0, END)
                    clientid.delete(0, END)
                    tip_iesire.delete(0, END)
                    obs.delete(0, END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                elif data_out.get() == '' and tip_iesire.get() == '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, client_id, observatii) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get(), clientid.get(), obs.get())
                    my_cursor.execute(sqlStuff, record)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    clientid.delete(0, END)
                    obs.delete(0, END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                elif data_out.get() == '' and clientid.get() == '' and tip_iesire.get() == '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, observatii) VALUES (%s, %s, %s, %s, %s, %s)"
                    record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get(), obs.get())
                    my_cursor.execute(sqlStuff, record)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    obs.delete(0, END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                elif tip_iesire.get() == '' and obs.get() == '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, data_instalare, client_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get(), data_out.get(), clientid.get())
                    my_cursor.execute(sqlStuff, record)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    data_out.delete(0, END)
                    clientid.delete(0, END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                elif obs.get() == '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get(), data_out.get(), clientid.get(), tip_iesire.get())
                    my_cursor.execute(sqlStuff, record)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    data_out.delete(0, END)
                    clientid.delete(0, END)
                    tip_iesire.delete(0, END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                elif tip_iesire.get() == '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, data_instalare, client_id, observatii) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get(), data_out.get(), clientid.get(), obs.get())
                    my_cursor.execute(sqlStuff, record)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    data_out.delete(0, END)
                    clientid.delete(0, END)
                    tip_iesire.delete(0, END)
                    obs.delete(0,END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                elif data_out.get() == '' and obs.get() == '':
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    #sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii) VALUES (%s, %s, %s, %s, %s, null, %s, %s, null)"
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii) VALUES ('"+producator.get()+"', '"+model.get()+"', '"+serie.get()+"', '"+data_fab.get()+"', '"+data_in.get()+"', null, '"+clientid.get()+"', '"+tip_iesire.get()+"', null)"
                    #record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get(), clientid.get(), tip_iesire.get())
                    #my_cursor.execute(sqlStuff, record)
                    my_cursor.execute(sqlStuff)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    data_out.delete(0, END)
                    clientid.delete(0, END)
                    tip_iesire.delete(0, END)
                    obs.delete(0,END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                else :
                    mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        #auth_plugin = "mysql_native_password",
                        )
                    my_cursor = mydb.cursor()
                    my_cursor.execute("CREATE TABLE IF NOT EXISTS stoc (producator VARCHAR(30) not null, model VARCHAR(30) not null, seria VARCHAR(60) not null PRIMARY KEY, UNIQUE INDEX `seria_UNIQUE` (`seria` ASC), data_fab DATE not null, data_intrare DATE not null, data_instalare DATE , client_id VARCHAR(50), tip_inst VARCHAR(30), observatii VARCHAR(200))")
                    sqlStuff = "INSERT INTO stoc(producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    record = (producator.get(), model.get(), serie.get(), data_fab.get(), data_in.get(), data_out.get(), clientid.get(), tip_iesire.get(), obs.get())
                    my_cursor.execute(sqlStuff, record)
                    mydb.commit()
                    mydb.close()
                    producator.delete(0, END)
                    model.delete(0, END)
                    serie.delete(0, END)
                    data_fab.delete(0, END)
                    data_in.delete(0, END)
                    data_out.delete(0, END)
                    clientid.delete(0, END)
                    tip_iesire.delete(0, END)
                    obs.delete(0,END)
                    tk.messagebox.showinfo("", "Inregistrarile au fost salvate!", icon='info')
                    
            except:
                tk.messagebox.showinfo("Atentie!", "Campurile nu sunt completate sau seria introdusa  exista in baza de date", icon='warning')

            getAll()
        def clean():
            producator.delete(0, END)
            model.delete(0, END)
            serie.delete(0, END)
            data_fab.delete(0, END)
            data_in.delete(0, END)
            data_out.delete(0, END)
            clientid.delete(0, END)
            tip_iesire.delete(0, END)
            obs.delete(0, END)
            entry_search.delete(0, END)
        def update():
            answer = tk.messagebox.askquestion("Atentie!!", "Esti sigur ca vrei sa faci modificarea?", icon='warning')
            try:
                if answer == 'yes':
                    if  producator.get() == '' and model.get() == '':
                        tk.messagebox.showinfo("Eroare", "Completati Producator si Model!!", icon='warning')
                
                    elif  model.get() == '':
                        tk.messagebox.showinfo("Eroare", "Completati Model!!", icon='warning')
                    elif  producator.get() == '':
                        tk.messagebox.showinfo("Eroare", "Completati Producator!!", icon='warning')
                    elif data_out.get() == '':
                        mydb = mysql.connector.connect(
                            host = "192.168.10.59",
                            user = "marius",
                            passwd = "Mazdarx8@",
                            database = "stocdb",
                            #auth_plugin = "mysql_native_password",
                            )
                        my_cursor = mydb.cursor()
                        my_cursor.execute("UPDATE stoc SET producator = '"+producator.get()+"', model = '"+model.get()+"', data_fab = '"+data_fab.get()+"', data_intrare = '"+data_in.get()+"', data_instalare = null, client_id = '"+clientid.get()+"', tip_inst = '"+tip_iesire.get()+"', observatii = '"+obs.get()+"' WHERE seria = '"+serie.get()+"'")
                        mydb.commit()
                        mydb.close()
                        producator.delete(0, END)
                        model.delete(0, END)
                        serie.delete(0, END)
                        data_fab.delete(0, END)
                        data_in.delete(0, END)
                        data_out.delete(0, END)
                        clientid.delete(0, END)
                        tip_iesire.delete(0, END)
                        obs.delete(0, END)
                        tk.messagebox.showinfo("", "Inregistrarea a fost modificata!", icon='info')                   
                    else :
                        mydb = mysql.connector.connect(
                            host = "192.168.10.59",
                            user = "marius",
                            passwd = "Mazdarx8@",
                            database = "stocdb",
                            #auth_plugin = "mysql_native_password",
                            )
                        my_cursor = mydb.cursor()
                        my_cursor.execute("UPDATE stoc SET producator = '"+producator.get()+"', model = '"+model.get()+"', data_fab = '"+data_fab.get()+"', data_intrare = '"+data_in.get()+"', data_instalare = '"+data_out.get()+"', client_id = '"+clientid.get()+"', tip_inst = '"+tip_iesire.get()+"', observatii = '"+obs.get()+"' WHERE seria = '"+serie.get()+"'")
                        mydb.commit()
                        mydb.close()
                        producator.delete(0, END)
                        model.delete(0, END)
                        serie.delete(0, END)
                        data_fab.delete(0, END)
                        data_in.delete(0, END)
                        data_out.delete(0, END)
                        clientid.delete(0, END)
                        tip_iesire.delete(0, END)
                        obs.delete(0, END)
                        tk.messagebox.showinfo("", "Inregistrarea a fost modificata!", icon='info') 
                else:
                    tk.messagebox.showinfo("Eroare", "Eroare!!", icon='warning')
            except:
                tk.messagebox.showinfo("Eroare", "Nu este permisa modificarea!!!!", icon='error')
            getAll()
        #def update1():
        #    answer = tk.messagebox.askquestion("Atentie!!", "Esti sigur ca vrei sa faci modificarea?//////")
        #    print(answer)
        #    if answer == 'yes':
        #        tk.messagebox.showinfo("merge")
        def delete():
            answer1 = tk.messagebox.askquestion("Atentie Tudor!!", "Tudor, esti sigur ca vrei sa stergi inregistrarea?", icon='warning')
            if answer1 == 'yes':
                try:
                    if serie.get() != '':
                        mydb = mysql.connector.connect(
                            host = "192.168.10.59",
                            user = "marius",
                            passwd = "Mazdarx8@",
                            database = "stocdb",
                            #auth_plugin = "mysql_native_password",
                            )
                        my_cursor = mydb.cursor()
                        my_cursor.execute("DELETE from stoc WHERE seria = '"+serie.get()+"'")
                        mydb.commit()
                        mydb.close()
                        producator.delete(0, END)
                        model.delete(0, END)
                        serie.delete(0, END)
                        data_fab.delete(0, END)
                        data_in.delete(0, END)
                        data_out.delete(0, END)
                        clientid.delete(0, END)
                        tip_iesire.delete(0, END)
                        obs.delete(0, END)
                        getAll()
                        tk.messagebox.showinfo("", "Inregistrarea a fost stearsa!", icon='info')
                    elif serie.get() == '':
                        tk.messagebox.showinfo("", "Nu ati selectat seria!", icon='warning')
                except:
                    tk.messagebox.showinfo("Eroare", "Verificati daca server-ul functioneaza", icon='error')
        def exp():
            #print('hello')
            #cale = cale_exp.get()
            
            
            mydb = mysql.connector.connect(
                        host = "192.168.10.59",
                        user = "marius",
                        passwd = "Mazdarx8@",
                        database = "stocdb",
                        )
            FILE = cale_exp.get()
            dump_writer = csv.writer(open(FILE,'w'), delimiter=',',quotechar="'")
            dump_writer.writerow(["producator", "model", "seria", "data_fab", "data_intrare", "data_instalare", "client_id", "tip_inst", "observatii" ])
            my_cursor = mydb.cursor()
            #my_cursor.execute("SELECT producator, model, seria, data_fab, data_intrare, data_instalare, client_id, tip_inst, observatii FROM stoc WHERE seria = '"+data+"'")
            my_cursor.execute("SELECT * FROM stoc")
            #row = my_cursor.fetchall()
            #with open('cale_exp.get()/test.csv', 'w', newline= '') as f:
               # a = csv.writer(f, delimiter=',')
                #a.writerow(["Header 1", "Header 2", "Header 3","Header 4","Header 5","Header 6","Header 7","Header 8","Header 9" ])  ## etc
                #a.writerows(rows)  ## closing paren added
            for row in my_cursor.fetchall() :
                dump_writer.writerow(row)
            tk.messagebox.showinfo("Export to .csv", "Au fost exportate inregistrarile cu success", icon='info')
            #mydb.commit()
            mydb.close()
            #print(FILE)

        self.save = ImageTk.PhotoImage(Image.open("save.png"))
        self.search= ImageTk.PhotoImage(Image.open("search2.png"))
        self.search1= ImageTk.PhotoImage(Image.open("search1.png"))
        self.update= ImageTk.PhotoImage(Image.open("update.png"))
        self.delete= ImageTk.PhotoImage(Image.open("delete.png"))
        self.delete_btn= ImageTk.PhotoImage(Image.open("delete_btn.png"))
        self.exp_btn= ImageTk.PhotoImage(Image.open("download.png"))

        btn_save = Button(self, image=self.save, bg='ghostwhite', borderwidth=1, command=save)
        btn_save.place(x=780, y=220, width=70, height=70)

        label_save = Label(self, text="Salveaza", bg="ghostwhite", borderwidth=0, font=('bold', 13))
        label_save.place(x=780, y=300)

        btn_update = Button(self, image=self.update, bg='ghostwhite', borderwidth=0, command=update)
        btn_update.place(x=985, y=220, width=70, height=70)

        label_update = Label(self, text="Update", bg="ghostwhite", borderwidth=0, font=('bold', 13))
        label_update.place(x=990, y=300)

        btn_searchall = Button(self, image=self.search, bg='ghostwhite', borderwidth=0, command=getAll)
        btn_searchall.place(x=1230, y=220, width=70, height=70)

        label_searchall = Label(self, text="Afiseaza inregistrari", bg="ghostwhite", borderwidth=0, font=('bold', 13))
        label_searchall.place(x=1175, y=300)

        btn_search1 = Button(self, image=self.search1, bg='ghostwhite', borderwidth=0, command=get)
        btn_search1.place(x=1230, y=93, width=70, height=70)

        label_search = Label(self, text="Cauta inregistrari dupa criteriul selectat", bg="ghostwhite", borderwidth=0, font=('bold', 13), width=110)
        label_search.place(x=600, y=60)

        btn_clean = Button(self, image=self.delete, bg='ghostwhite', borderwidth=0, command=clean)
        btn_clean.place(x=450, y=93, width=70, height=70)

        btn_del = Button(self, image=self.delete_btn, bg='ghostwhite', borderwidth=0, command=delete)
        btn_del.place(x=580, y=93, width=70, height=70)

        btn_exp = Button(self, image=self.exp_btn, bg='ghostwhite', borderwidth=0, command=exp)
        btn_exp.place(x=780, y=93, width=70, height=70)





class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Evidenta tub rasina", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)
        button1 = tk.Button(self, text="Evidenta echipamente depozit",
                           command=lambda: controller.show_frame("StartPage"))

        button1.place(x=10, y=10, width=240)
        button1.config(borderwidth=0.5, bg='ghostwhite', font=(12))
        button = tk.Button(self, text="Evidenta echipamente service",
                           command=lambda: controller.show_frame("PageTwo"))

        button.place(x=250, y=10, width=240)
        button.config(borderwidth=0.5, bg='ghostwhite', font=(12))




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Evidenta echipamente service", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)
        button1 = tk.Button(self, text="Evidenta echipamente depozit",
                           command=lambda: controller.show_frame("StartPage"))

        button1.place(x=10, y=10, width=240)
        button1.config(borderwidth=0.5, bg='ghostwhite', font=(12))
        button = tk.Button(self, text="Evidenta tub rasina",
                           command=lambda: controller.show_frame("PageOne"))
        button.place(x=250, y=10, width=240)
        button.config(borderwidth=0.5, bg='ghostwhite', font=(12))


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
