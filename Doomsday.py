class Doom:
    weekDaysList = ("Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday",
                    "Saturday")
    anchorDays = (2, 0, 5, 3) # ["Tuesday", "Sunday", "Friday", "Wednesday"]

    def leapYear(self, year):    
        leap = False
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True
        return leap

    def maxDays(self, month, year):
        if month in {4, 6, 9, 11}:
            return 30
        if month == 2:
            if self.leapYear(year):
                return 29
            else:
                return 28
        return 31
    
    def extract(self, date):
        try:
            parts = date.split("/")
            if len(parts) != 3:
                raise ValueError("Must contain exactly 2 slashes(DD/MM/YYYY).")
            day = int(parts[0])
            month = int(parts[1])
            year = int(parts[2])
        except ValueError as err:
            raise ValueError("Please use integers.")
        if not 1 <= month <= 12:
            raise ValueError("Month must be between 1 and 12.")
        if not 1 <= day <= self.maxDays(month, year):
            raise ValueError(f"Invalid day {day} for month {month} in year {year}.")            
        return day, month, year
    
    def __init__(self, date):
        self.day, self.month, self.year = self.extract(date)

    def getAnchorDay(self):
        century = self.year // 100 
        refCentury = century % 4
        return self.anchorDays[refCentury]

    def calculateYearDoomsDay(self):
        shortYear = self.year % 100
        modMonth = shortYear % 12
        doomsDay = (self.getAnchorDay() + shortYear // 12 + modMonth + modMonth // 4) % 7
        return doomsDay

    def getMonthDoomsday(self):
        if self.leapYear(self.year):
            leapDooms = [4, 29]
        else:
            leapDooms = [3, 28]
        doomsMonthDays = leapDooms + [14, 4, 9, 6, 11, 8, 5, 10, 7, 12]
        return doomsMonthDays[self.month - 1]

    def getDayDifference(self):
        dayDiff = (self.day - self.getMonthDoomsday()) % 7
        return dayDiff

    def getWeekDay(self):
        return self.weekDaysList[(self.calculateYearDoomsDay() + self.getDayDifference()) % 7]

def main():
    print("\nDoomsday Calculator")
    print("Note: The Gregorian Calendar started from 15th October, 1582.\nBut the calculator works just fine with dates before it too.\n")
    while True:
        userInput = input("Enter date (DD/MM/YYYY) or exit(e): ")
        if userInput.lower() == "e":
            break
        try:
            date = Doom(userInput)
            result = date.getWeekDay()
            print(f"{result}\n")
        except ValueError as err:
            print(f"Error: {err}.\nTry again.\n")

if __name__ == "__main__":
    main()