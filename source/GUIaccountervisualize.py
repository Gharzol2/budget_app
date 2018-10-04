import tkinter as tk
import tkinter.messagebox
import datetime

# For plots
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import utilities
import entriesdata
import GUIstartpage
import GUIaddentry
import GUIaccounter


class GUIAccounterVisualize(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.main_label = tk.Label(self, text="Accounting Visualize", font=None)
        self.main_label.grid(row=0, column=1)



        # Plot button
        self.plot_credits_cumulative_button = tk.Button(self, text="plot cumulative credits",
                                                        command=lambda: self.plot_account_credits_cumulative())
        self.plot_credits_cumulative_button.grid(row=1, column=1)





        # Button to go accounter
        self.back_to_start_button = tk.Button(self, text="Back to accounter",
                            command= lambda: controller.show_frame(GUIaccounter.GUIAccounter))
        self.back_to_start_button.grid(row=3, column=0)

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

    def plot_account_credits_cumulative(self):
        credits = []
        dates = []

        for month in entriesdata.years[utilities.selected_year - utilities.year_limits[0]].month_entries:
            month.sort_entries_by_date()
            for i in month.entries:
                credits.append(i.credit_entry.amount)
                dates.append(i.date)

        credits_cumulative = []
        if len(credits) != 0:
            credits_cumulative.append(credits[0])
            for i in range(1, len(credits)):
                credits_cumulative.append(credits_cumulative[i - 1] + credits[i])

            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)

            a.plot(list(range(0, len(credits_cumulative))), credits_cumulative)

            self.canvas = FigureCanvasTkAgg(f, self)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=0, column=0)
        else:
            tkinter.messagebox.showwarning("Warning", "No entries to plot")