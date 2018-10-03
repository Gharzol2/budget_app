from entries import MonthEntries
import utilities


class Year():
    def __init__(self, year_num):
        self.month_entries = [MonthEntries(i) for i in range(1,13)]
        self.year_num = year_num

    def __str__(self):
        string_to_return = ''
        count = 1
        for i in self.month_entries:
            string_to_return += utilities.month_data[count] + ": \t\t" + str(i) + "\n-------------------------------------------\n"
            count += 1
        return string_to_return