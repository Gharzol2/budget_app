from utilities import month_data

from entries import Entry


class MonthEntries():
    def __init__(self, month_number):
        self.month_number = month_number
        self._entries = []

    @property
    def month_number(self):
        return self._month_number

    @property
    def month_name(self):
        return self._month_name

    @property
    def entries(self):
        return self._entries

    @month_number.setter
    def month_number(self, month_number):
        assert(month_number in month_data.keys())
        self._month_number = month_number
        self._month_name = month_data[month_number]

    #TODO: Check that this works
    def sort_entries_by_date(self):
        def extract_date(entry):
            return entry.date[0]
        self._entries.sort(key=extract_date)

    def sort_entries_by_credit_amount(self):
        def extract_credit_amount(entry):
            return entry.credit_entry.amount
        self._entries.sort(key=extract_credit_amount)

    def sort_entries_by_debt_amount(self):
        def extract_debt_amount(entry):
            return entry.debt_entry.amount
        self._entries.sort(key=extract_debt_amount)

    def _add_entry(self, new_entry):
        print("date i add entry: ", new_entry.date[1], "self month number: ", self.month_number)
        assert(new_entry.date[1] == self.month_number)
        self._entries.append(new_entry)
        self.sort_entries_by_date()

    def add_entry(self, credit, debt, name, date, comment=None):
        new_entry = Entry(credit, debt, name, date, comment)
        self._add_entry(new_entry)

    def __str__(self):
        if self._entries == []:
            return "no entries in month"
        string_to_return = "\n---"
        for i in self._entries:
            string_to_return += str(i)
        string_to_return += "\n---\n"
        return string_to_return

