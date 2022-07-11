
class Date:
    short_days = [4, 6, 9, 11]

    def __init__(self, day: int = 0, month: int = 0, year: int = 0):
        """

        :type year: object
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"Date(day = {self.day} ,month = {self.month} , year = {self.year} "

    def isValid(self) -> bool:
        ret_val = True

        if not isinstance(self.day, int) and isinstance(self.month, int) and isinstance(self.year, int):
            ret_val = False

        if self.day == 0 or self.month == 0 or self.year == 0:
            ret_val = False

        if self.day < 1 or self.day > 31:
            ret_val = False

        if self.month < 1 or self.month > 12:
            ret_val = False

        if len(str(self.year)) != 4:
            ret_val = False

        if self.month in self.short_days and self.day > 30:
            ret_val = False

        if self.year % 4 == 0 and self.month == 2 and self.day > 29:
            ret_val = False
        elif (not self.year % 4 == 0) and self.month == 2 and self.day > 28:
            ret_val = False

        return ret_val

    def getNextDay(self) -> tuple:

        if self.year % 4 == 0 and self.month == 2 and self.day == 29:
            return 1, 3, self.year

        if (not self.year % 4 == 0) and self.month == 2 and self.day == 28:
            return 1, 3, self.year

        if (self.month in self.short_days and self.day == 30) or (self.month not in self.short_days and self.day == 31
                                                                  and not self.month == 12):
            return 1, self.month + 1, self.year

        if self.month == 12 and self.day == 31:
            return 1, 1, self.year + 1

        return self.day + 1, self.month, self.year

    def getNextDays(self, days_to_add: int = 0) -> str:

        if (self.year % 4 == 0 and self.month == 2 and self.day == 29) or \
                ((not self.year % 4 == 0) and self.month == 2 and self.day == 28) or \
                (self.short_days and self.day == 30) or \
                (self.month not in self.short_days and self.day == 31 and not self.month == 12):
            return f"{days_to_add - 1}.{self.month + 1}.{self.year}"

        if self.month == 12 and self.day == 31:
            return 1, 1, self.year + 1

        return {self.day + 1}, self.month, self.year


d = Date(1, 1, 2012)
print(d.isValid())
print(d)
print(d.getNextDay())
print(d.getNextDays(100))
