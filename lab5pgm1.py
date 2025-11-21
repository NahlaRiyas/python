import calendar
year = int(input("enter year:"))
print("leap year"if calendar.isleap(year) else "not a leap year")
