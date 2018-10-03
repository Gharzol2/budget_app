import tkinter as tk

import GUIstartpage
import GUIaccounter
import GUIaddentry


class GUIBudgetApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}

        for F in (GUIstartpage.GUIStartPage, GUIaccounter.GUIAccounter, GUIaddentry.GUIAddEntry):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.geometry("1000x800")

        self.show_frame(GUIstartpage.GUIStartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()