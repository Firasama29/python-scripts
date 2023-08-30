import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"calendar for {calendar.month_name[month]} {year}:\n")
    print(cal)

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    if month not in range(1, 13):
        raise NameError(f"{month} is not a correct month")
    display_calendar(year, month)