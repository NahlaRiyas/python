import datetime
import time

now = datetime.datetime.now()

print("Current Date and Time:", now)
print("Current Year:", now.year)
print("Month of the Year:", now.month)
print("Week Number of the Year:", time.strftime("%U"))
print("Weekday of the Week (0=Mon):", now.weekday())
print("Day of Year:", now.strftime("%j"))
print("Day of Month:", now.day)
print("Day of Week:", now.strftime("%A"))
