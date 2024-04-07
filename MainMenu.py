import tkinter as tk
import tkcalendar as tkcal

class MainMenu(tk.Tk):
    """The main menu for my birding application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("Bird Expedition")
        self.geometry('260x100+300+300')
        self.resizable(False, False)
        
        self.title = tk.Label(self,
                        text = 'Bird Expedition',
                        font=('Arial 16 bold'),
                        )
        self.title.grid(columnspan=2, sticky='we', padx = 20)

        self.new_btn = tk.Button(self,text="new expedition", command=self.new_btn_command())
        self.new_btn.grid(row=1,column=0,sticky='w',padx = 20)

        self.old_btn = tk.Button(self,text="old expedition", command=self.old_btn_command())
        self.old_btn.grid(row=1,column=1,sticky='e',padx = 20)

        self.mainloop()

    def new_btn_command(self):
        pass

    def old_btn_command(self):
        pass

MainMenu()
