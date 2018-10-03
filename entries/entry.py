from entries import DebtEntry
from entries import CreditEntry


class Entry():
    def __init__(self, credit_entry_amount, debt_entry_amount, name, date, comment=None):
        self.credit_entry = CreditEntry(credit_entry_amount)
        self.debt_entry = DebtEntry(debt_entry_amount)
        self.name = name
        self.date = date
        self.comment = comment

    # This is not a true check for equality since two entries that are equal in this way
    # often should still be treated as different.
    def __eq__(self, other):
        return self.credit_entry == other.credit_entry and self.debt_entry == other.debt_entry\
               and self.name == other.name and self.date == other.date and self.comment == other.comment

    def __str__(self):
        string_to_return = "\n" + self.name + "\n" + str(self.date[0]) + "/" + str(self.date[1]) + "-" + str(self.date[2])\
                           + "\ncredit:\t\t\t\t" + str(self.credit_entry)\
                           + " \ndebt:\t\t\t\t" + str(self.debt_entry) + "\n"
        if self.comment is not None:
            string_to_return += self.comment
        return string_to_return
