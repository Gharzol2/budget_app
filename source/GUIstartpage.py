import tkinter as tk
import tkinter.messagebox
import datetime

import utilities
import GUIaccounter



class GUIStartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to budget app!\nThis is the start page", font=None)
        label.grid(row=0, column=1, pady=40, padx=20)

        button1 = tk.Button(self, text="Go to Accounter (in development)",
                            command= lambda: controller.show_frame(GUIaccounter.GUIAccounter))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text="Go to planner (currently not functional)", command=lambda: print("Should go to planner"))
        button2.grid(row=2, column=0)

        self.selected_year_label = tk.Label(self, text="Selected year: " + str(utilities.selected_year))
        self.selected_year_label.grid(row = 1, column = 2)
        self.update_selected_year_label()

        self.choose_selected_year_label = tk.Label(self, text="Select other year?")
        self.choose_selected_year_label.grid(row = 2, column = 2)

        self.selected_year_entry = tk.Entry(self)
        self.selected_year_entry.grid(row = 3, column = 2)

        self.submit_selected_year_button = tk.Button(self, text="Submit",
                                                     command=lambda: self.handle_update_selected_year())
        self.submit_selected_year_button.grid(row = 3, column = 3)

        # Label for time
        self.time_label = tk.Label(self, text=str(datetime.datetime.now())[:19])
        self.time_label.place(relx=0.99, rely=0.99, anchor='se')
        self.update_time_label()

    def update_selected_year_label(self):
        self.selected_year_label.configure(text="Selected year: " + str(utilities.selected_year))
        self.selected_year_label.after(1000, self.update_selected_year_label)

    def handle_update_selected_year(self):
        new_year = self.selected_year_entry.get()
        if new_year == '' or int(new_year) < utilities.year_limits[0] or int(new_year) > utilities.year_limits[1]:
            tkinter.messagebox.showwarning("Warning", "choose year within limits: " + str(utilities.year_limits[0]) + "-" + str(utilities.year_limits[1]))
        else:
            utilities.selected_year = int(new_year)

    def update_time_label(self):
        self.time_label.configure(text=str(datetime.datetime.now())[:19])
        self.time_label.after(100, self.update_time_label)