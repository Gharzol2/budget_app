import tkinter as tk
import tkinter.messagebox
import datetime

import utilities
import entriesdata
import GUIstartpage
import GUIaddentry


class GUIAccounter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.main_label = tk.Label(self, text="Accounting page", font=None)
        self.main_label.pack(pady=30,padx=10)

        # Text of monthly entries
        # Set up frame widget
        self.month_entries_text_frame = tk.Frame(self, width=370, height=400)
        self.month_entries_text_frame.place(relx=0.01, rely=0.5, anchor='w')
        # ensure a consistent GUI size
        self.month_entries_text_frame.grid_propagate(False)
        # implement stretchability
        self.month_entries_text_frame.grid_rowconfigure(0, weight=1)
        self.month_entries_text_frame.grid_columnconfigure(0, weight=1)
        # Set up text widget
        self.month_entries_text = tk.Text(self.month_entries_text_frame, borderwidth=3, relief="sunken")
        self.month_entries_text .config(font=("consolas", 10), undo=True, wrap='word')
        self.month_entries_text .grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.month_entries_text.insert(tk.END, str(entriesdata.years[utilities.selected_year - utilities.year_limits[0]]))
        self.update_month_entry_text()
        # Set up scrollbar
        self.month_entries_text_scrollbar = tk.Scrollbar(self.month_entries_text_frame, command=self.month_entries_text.yview)
        self.month_entries_text_scrollbar.grid(row=0, column=1, sticky='nsew')
        self.month_entries_text['yscrollcommand'] = self.month_entries_text_scrollbar.set

        # Label for showing currently selected year
        self.selected_year_label = tk.Label(self, text="Selected year: " + str(utilities.selected_year))
        self.selected_year_label.place(relx=0.01, rely=0.03, anchor='nw')
        self.update_selected_year_label()

        # Button to go to add entry
        self.to_add_entry_button = tk.Button(self, text="Add entries",
                                              command=lambda: controller.show_frame(GUIaddentry.GUIAddEntry))
        self.to_add_entry_button.place(relx=0.9, rely=0.1, anchor='ne')

        # Button to go back to start
        self.back_to_start_button = tk.Button(self, text="Back to start pack",
                            command= lambda: controller.show_frame(GUIstartpage.GUIStartPage))
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

    def update_month_entry_text(self):
        self.month_entries_text.delete(1.0, tk.END)
        self.month_entries_text.insert(tk.END, str(entriesdata.years[utilities.selected_year - utilities.year_limits[0]]))
        self.month_entries_text.after(1000, self.update_month_entry_text)