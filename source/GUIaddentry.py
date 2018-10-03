import tkinter as tk
import tkinter.messagebox
import datetime

import utilities
import entriesdata
import GUIstartpage
import GUIaccounter


class GUIAddEntry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.main_label = tk.Label(self, text="Add entry", font=None)
        self.main_label.pack(pady=30,padx=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.place(relx=0.01, rely=0.09, anchor='nw')
        self.comment_entry = tk.Entry(self)
        self.comment_entry.place(relx=0.1, rely=0.09, anchor='nw')
        self.day_entry = tk.Entry(self)
        self.day_entry.place(relx=0.01, rely=0.15, anchor='nw')
        self.month_entry = tk.Entry(self)
        self.month_entry.place(relx=0.1, rely=0.15, anchor='nw')
        self.credit_entry = tk.Entry(self)
        self.credit_entry.place(relx=0.2, rely=0.15, anchor='nw')
        self.debt_entry = tk.Entry(self)
        self.debt_entry.place(relx=0.3, rely=0.15, anchor='nw')

        self.name_label = tk.Label(self, text="name")
        self.name_label.place(relx=0.01, rely=0.07, anchor='nw')
        self.comment_label = tk.Label(self, text="comment (optional)")
        self.comment_label.place(relx=0.1, rely=0.07, anchor='nw')
        self.day_label = tk.Label(self, text="day")
        self.day_label.place(relx=0.01, rely=0.13, anchor='nw')
        self.month_label = tk.Label(self, text="month")
        self.month_label.place(relx=0.1, rely=0.13, anchor='nw')
        self.credit_label = tk.Label(self, text="credit")
        self.credit_label.place(relx=0.2, rely=0.13, anchor='nw')
        self.debt_label = tk.Label(self, text="debt")
        self.debt_label.place(relx=0.3, rely=0.13, anchor='nw')

        self.submit_single_entry_button = tk.Button(self, text="Submit entry", command=lambda: self.handle_single_entry_submit())
        self.submit_single_entry_button.place(relx=0.01, rely=0.18, anchor='nw')


        # Label for showing currently selected year
        self.selected_year_label = tk.Label(self, text="Selected year: " + str(utilities.selected_year))
        self.selected_year_label.place(relx=0.01, rely=0.03, anchor='nw')
        self.update_selected_year_label()

        # Button to go back to accounter
        self.back_to_start_button = tk.Button(self, text="Back to accounter",
                            command= lambda: controller.show_frame(GUIaccounter.GUIAccounter))
        self.back_to_start_button.place(relx=0.01, rely=0.99, anchor='sw')

        # Label for time
        self.time_label = tk.Label(self, text=str(datetime.datetime.now())[:19])
        self.time_label.place(x=20, y=60)
        self.time_label.pack()
        self.update_time_label()

    def update_time_label(self):
        self.time_label.configure(text=str(datetime.datetime.now())[:19])
        self.time_label.place(relx=1.0, rely=1.0, anchor='se')
        self.time_label.after(100, self.update_time_label)

    def update_selected_year_label(self):
        self.selected_year_label.configure(text="Selected year: " + str(utilities.selected_year))
        self.selected_year_label.place(relx=0.01, rely=0.03, anchor='nw')
        self.selected_year_label.after(1000, self.update_selected_year_label)

    def handle_single_entry_submit(self):
        day = self.day_entry.get()
        if int(day) < 1 or int(day) > 31:
            tkinter.messagebox.showwarning("Warning", "Wrong day input: " + str(day))
            return
        month = self.month_entry.get()
        if int(month) not in utilities.month_data.keys():
            tkinter.messagebox.showwarning("Warning", "Wrong month input: " + str(month))
            return
        credit = self.credit_entry.get()
        if credit == '':
            credit = 0
        debt = self.debt_entry.get()
        if debt == '':
            debt = 0
        name = self.name_entry.get()
        if name == '':
            tkinter.messagebox.showwarning("Warning", "Empty name input")
            return
        comment = self.comment_entry.get()
        if comment == '':
            comment = None
        date = (int(day), int(month), utilities.selected_year)

        year = entriesdata.years[utilities.selected_year - utilities.year_limits[0]]
        print("month_entries: ", year.month_entries)
        year.month_entries[int(month) - 1].add_entry(int(credit), int(debt), name, date, comment)


        print(year)