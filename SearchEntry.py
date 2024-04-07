"""a tkinter Widget for allowing for searchable entry"""

import tkinter as tk

class Entry_Search(tk.Frame):
    def __init__ (self, parent, list, height = 5,entry_args={}, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.height = height
        self.list = list
        self.parent = parent
        self.entry = tk.Entry(parent,**entry_args)
        self.entry.grid(column=0,row=0)
        self.listbox = tk.Listbox(parent,height = self.height)
        self.listbox.grid(column=1,row=0)
        self.__update(self.list)
        self.listbox.bind("<<ListboxSelect>>", self.__clickitem)
        self.entry.bind("<KeyRelease>", self.__checkentry)


    def __update(self,list):
        self.listbox.delete(0,tk.END)
        
        for item in list:
            self.listbox.insert(tk.END, item)

    def __clickitem(self,event):
        self.entry.delete(0,tk.END)
        self.entry.insert(0,self.listbox.get(self.listbox.curselection()))
    
    def __checkentry(self,event):
        typed = self.entry.get()

        if typed == '':
            data = self.list
        else:
            data = []
            for item in self.list:
                if typed.lower() in item.lower():
                    data.append(item)
        self.__update(data)


#root = tk.Tk()

#testlist = ["a","ab","abc","abcd","abcde"]

#test_obj = Entry_Search(root, testlist)
#test_obj.grid()

#root.mainloop()