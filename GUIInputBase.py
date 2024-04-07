import tkinter as tk

class LabelInputForm(tk.Frame):
    """creates a form with LabelInput objects"""
    def __init__(self,parent, label_inp_arg_list, *args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        for label_inp_arg in label_inp_arg_list:
            LabelInput(parent, **label_inp_arg.arg_list).grid()
        
class LabelInputArg():
    """creates an object with the detail arguments (label, inp_cls, inp_args) for the Label Input Class"""
    def __init__(self, label, inp_cls, inp_args={}):
        self.arg_list = {"label":label,"inp_cls":inp_cls,"inp_args":inp_args}
        
class LabelInput(tk.Frame):
    """ties a Label to an input object"""
    def __init__(self, parent, label, inp_cls, inp_args,*args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text=label,anchor='w')
        self.input = inp_cls(self,**inp_args)
        self.columnconfigure(1, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        self.input.grid(row = 0, column = 1, sticky = tk.E + tk.W)

#root = tk.Tk()

#label_inp_arg_list = [LabelInputArg("test1",tk.Entry),LabelInputArg("test2",tk.Entry)]

#test_GUI = GUIInputBase(root, label_inp_arg_list)
#test_GUI.grid()

#root.mainloop()