city = input("What city are you in?: ")
temp = float(input("What is the temperature today?: "))

if temp < 50:
    print("Warning: Heat alert")
elif temp < 30:
    print("The weather outside is perfect")
elif temp < 20:
    print("Warning: Cold alert")


import datetime
import calendar

now = datetime.datetime.now()
print("City: ", city)
print("Current Date and Time: ", now)

print(calendar.calendar(now.year))
