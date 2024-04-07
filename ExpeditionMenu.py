import tkinter as tk
import tkcalendar as tkcal
from GUIInputBase import *
from BirdMenu import BirdMenu
import sqlite3
from DatabaseOps.InputObjects import expedition

class ExpeditionMenu(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.parent = parent

        self.title_lbl=tk.Label(parent,text="Expedition Location Entry",font=('Arial 16 bold')).grid(row=0)

        self.date_var = tk.StringVar()
        self.location_var = tk.StringVar()

        formlist = [
            LabelInputArg("Please enter the date: ",tkcal.DateEntry,{'textvariable':self.date_var}),
            LabelInputArg("Please enter the Location: ",tk.Entry,{'textvariable':self.location_var})
        ]

        self.form = LabelInputForm(parent,formlist)
        self.form.grid(row=10)

        self.bird_btn = tk.Button(text= "Enter Bird Data", command=self.enter_bird)
        self.bird_btn.grid(row=20)

    def enter_bird(self):

        con = sqlite3.connect("birding.db")
        cur = con.cursor()
        form_expedition = expedition(self.location_var.get(),self.date_var.get(),[],cur)
        form_expedition.to_database()
        res = cur.execute("select last_insert_rowid()")
        expid = res.fetchone()[0]
        con.commit()
        con.close

        self.parent.destroy()
        birdparent = tk.Tk()
        BirdMenu(birdparent, expid).grid()


root = tk.Tk()

ExpeditionMenu(root).grid()

root.mainloop()