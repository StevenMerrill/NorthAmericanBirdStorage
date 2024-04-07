import tkinter as tk
from tkinter import filedialog as fd
from GUIInputBase import *
import sqlite3
from DatabaseOps.InputObjects import expedition_bird
from SearchEntry import *
from DatabaseOps.RetrievalQueries import generate_bird_list


class BirdMenu(tk.Frame):
    def __init__(self,parent,expid,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.expid = expid
        self.parent = parent

        self.title_lbl=tk.Label(parent,text="Bird Entry",font=('Arial 16 bold')).grid(row=0)

        self.species_var = tk.StringVar()
        self.number_var = tk.StringVar()
        self.file_name_var = tk.StringVar()

        formlist = [
            LabelInputArg("Please enter the Species: ",Entry_Search,{'list':generate_bird_list(), "entry_args":{'textvariable':self.species_var}}),
            LabelInputArg("Please enter the Number Seen: ",tk.Entry,{'textvariable':self.number_var}),
            LabelInputArg("Please select the photos of your birds",tk.Button,{'text':"Click to open file", 'command':self.openfile})
        ]

        self.form = LabelInputForm(parent,formlist)
        self.form.grid(row=10)

        self.bird_btn = tk.Button(text= "Enter Bird Data", command=self.enter_bird)
        self.bird_btn.grid(row=20,column = 0)
        
        self.sbm_btn = tk.Button(text= "Submit", command=self.submit)
        self.sbm_btn.grid(row=20,column = 1)

    def enter_bird(self):
        self.parent.destroy()

        con = sqlite3.connect("birding.db")
        cur = con.cursor()
        form_expedition_bird = expedition_bird(1,self.expid,self.file_name_var.get(),self.species_var.get(),self.number_var.get(),cur)
        form_expedition_bird.to_database()
        con.commit()

        birdparent = tk.Tk()
        BirdMenu(birdparent,self.expid).grid()

    def submit(self):
        self.parent.destroy()

        con = sqlite3.connect("birding.db")
        cur = con.cursor()
        form_expedition_bird = expedition_bird(1,self.expid,self.file_name_var.get(),self.species_var.get(),self.number_var.get(),cur)
        form_expedition_bird.to_database()
        con.commit()
        con.close()
        pass

    def openfile(self):
        """prompts a user for file names"""
        self.file_name_var.set(fd.askopenfilenames())
        #print(file_name_var.get())

#root = tk.Tk()

#BirdMenu(root,1).grid()

#root.mainloop()