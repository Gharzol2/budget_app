import tkinter as tk
import tkinter.messagebox
import datetime
from copy import deepcopy

import utilities
import entriesdata
import GUIstartpage
import GUIaccounter


class GUIAddEntry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.main_label = tk.Label(self, text="Add entry", font=None)
        self.main_label.grid(row=0,column=1, pady=40)


        self.single_entry_explainer = tk.Label(self, text="Enter data for a single entry: ")
        self.single_entry_explainer.grid(row=1, column=1, pady=20)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=3, column=2)
        self.comment_entry = tk.Entry(self)
        self.comment_entry.grid(row=3, column=3)
        self.day_entry = tk.Entry(self)
        self.day_entry.grid(row=5, column=2)
        self.month_entry = tk.Entry(self)
        self.month_entry.grid(row=5, column=3)
        self.credit_entry = tk.Entry(self)
        self.credit_entry.grid(row=5, column=4)
        self.debt_entry = tk.Entry(self)
        self.debt_entry.grid(row=5, column=5)

        self.name_label = tk.Label(self, text="name")
        self.name_label.grid(row=2, column=2)
        self.comment_label = tk.Label(self, text="comment (optional)")
        self.comment_label.grid(row=2, column=3)
        self.day_label = tk.Label(self, text="day")
        self.day_label.grid(row=4, column=2)
        self.month_label = tk.Label(self, text="month")
        self.month_label.grid(row=4, column=3)
        self.credit_label = tk.Label(self, text="credit")
        self.credit_label.grid(row=4, column=4)
        self.debt_label = tk.Label(self, text="debt")
        self.debt_label.grid(row=4, column=5)

        self.submit_single_entry_button = tk.Button(self, text="Submit entry", command=lambda: self.handle_single_entry_submit())
        self.submit_single_entry_button.grid(row=3, column=4)

        self.filename_entry_label = tk.Label(self, text="Enter filename for entries read: ")
        self.filename_entry_label.grid(row=6, column=1, pady=20)
        self.filename_entry = tk.Entry(self)
        self.filename_entry.grid(row=7, column=2)
        self.filename_entry.insert(tk.END, "transaksjonliste")
        self.filename_submit_button = tk.Button(self, text="Submit filename", command=lambda: self.handle_txt_entries_input())
        self.filename_submit_button.grid(row=7, column=3)



        # Button to go back to accounter
        self.back_to_start_button = tk.Button(self, text="Back to accounter",
                            command= lambda: controller.show_frame(GUIaccounter.GUIAccounter))
        self.back_to_start_button.grid(row=1, column=0, padx=20)

        # Label for showing currently selected year
        self.selected_year_label = tk.Label(self, text="Selected year: " + str(utilities.selected_year))
        self.selected_year_label.place(relx=0.99, rely=0.96, anchor='se')
        self.update_selected_year_label()

        # Label for time
        self.time_label = tk.Label(self, text=str(datetime.datetime.now())[:19])
        self.time_label.place(relx=0.99, rely=0.99, anchor='se')
        self.update_time_label()

    def update_time_label(self):
        self.time_label.configure(text=str(datetime.datetime.now())[:19])
        self.time_label.after(100, self.update_time_label)

    def update_selected_year_label(self):
        self.selected_year_label.configure(text="Selected year: " + str(utilities.selected_year))
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

    def handle_txt_entries_input(self):
        if self.filename_entry.get() == "":
            tkinter.messagebox.showwarning("Warning", "Enter a name for file entry")
            return

        try:
            text = utilities.text_parser(self.filename_entry.get())
        except OSError:
            tkinter.messagebox.showwarning("Warning", "File not found")
            return

        print("kjører gjennom")
        print(text)

        temp_text = deepcopy(text)
        for sentence in temp_text:
            if int(sentence[0][6:]) != utilities.selected_year:
                tkinter.messagebox.showwarning("Warning", "Some input is not the selected year.")
                return

        for sentence in text:
            print("kjører gjennom")
            if sentence[0][0] == '0':
                day = int(sentence[0][1])
            else:
                day = int(sentence[0][:2])

            if int(day) < 1 or int(day) > 31:
                tkinter.messagebox.showwarning("Warning", "Wrong day input: " + str(day))
                return

            if sentence[0][3] == '0':
                month = int(sentence[0][4])
            else:
                month = int(sentence[0][3:5])

            if int(month) not in utilities.month_data.keys():
                tkinter.messagebox.showwarning("Warning", "Wrong month input: " + str(month))
                return

            credit = 0.0
            print(sentence[3])
            print(sentence[4])


            if sentence[3] != '':
                """
                for i in range(0, len(sentence[3])):
                    if sentence[3][i] == ',':
                        temp_sentence = list(sentence[3])
                        temp_sentence[i] = '.'
                        sentence[3] = str(temp_sentence)
                """
                credit -= float(sentence[3])
            if sentence[4] != '':
                """
                for i in range(0, len(sentence[4])):
                    if sentence[4][i] == ',':
                        temp_sentence = list(sentence[4])
                        temp_sentence[i] = '.'
                        sentence[4] = str(temp_sentence)
                """
                credit += float(sentence[4])
            if credit == '':
                credit = 0

            name = sentence[1]
            if name == '':
                tkinter.messagebox.showwarning("Warning", "Empty name input")
                return

            date = (int(day), int(month), utilities.selected_year)

            year = entriesdata.years[utilities.selected_year - utilities.year_limits[0]]
            print("month_entries: ", year.month_entries)
            year.month_entries[int(month) - 1].add_entry(float(credit), 0, name, date, "")
