
import tkinter
import year


window = tkinter.Tk()

cre_entr = year.CreditEntry(2000)
print(cre_entr.amount)

entr = year.Entry(100, 150, "first", (15,2,91))
entr2 = year.Entry(3, 1, "second", (3,2,91))
entr3 = year.Entry(1233, 234, "third", (25,2,91))
entr4 = year.Entry(-123, 4, "fourth", (30,2,91))
entr5 = year.Entry(-9999, 9999, "fifth", (20,2,91))
entr6 = year.Entry(6, 1235, "sixth", (15,2,91))


month = year.MonthEntries(2)
month.add_entry(entr)
month.add_entry(entr2)
month.add_entry(entr3)
month.add_entry(entr4)
month.add_entry(entr5)
month.add_entry(entr6)
print(month)
month.sort_entries_by_credit_amount()
print(month)
month.sort_entries_by_debt_amount()
print(month)

window.mainloop()


