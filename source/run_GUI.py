import tkinter
import datetime
import entries
import utilities

from GUIbudgetapp import GUIBudgetApp

utilities.selected_year = 2018
date = datetime.datetime.now()

app = GUIBudgetApp()
app.mainloop()