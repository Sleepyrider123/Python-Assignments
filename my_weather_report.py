city = input("What city are you in?: ")
temp = float(input("What is the temperature today?: "))

if temp > 35:
    print("Warning: Heat alert")
elif temp < 35:
    print("The weather outside is perfect")


import datetime
import calendar

now = datetime.datetime.now()
print("City: ", city)
print("Current Date and Time: ", now)

print(calendar.calendar(now.year))
