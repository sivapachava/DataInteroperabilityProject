from datetime import time
from datetime import date
# time() takes hour, minutes, second,
# microsecond respectively in order
# if no parameter is passed in time() by default
# it takes 0
defaultTime = time()
print("default_hour =", defaultTime.hour)
print("default_minute =", defaultTime.minute)
print("default_second =", defaultTime.second)
print("default_microsecond =", defaultTime.microsecond)

# passing parameter in different-different ways
# hour, minute and second respectively is a default
# order
time1= time(8, 20, 55)
print("time_1 =", time1)

# assigning hour, minute and second to respective
# variables
time2= time(hour = 8, minute = 20, second = 55)
print("time_2 =", time2)

# assigning hour, minute, second and microsecond to
# respective variables
time3= time(hour=8, minute= 20, second=55, microsecond=45)
print("time_3 =", time3)

# You can create a date object containing
# the current date
# by using a classmethod named today()
current = date.today()

# print current year, month, and year individually
print("Current Day is :", current.day)
print("Current Month is :", current.month)
print("Current Year is :", current.year)

# strftime() creates string representing date in
# various formats
print("\n")
print("Let's print date, month and year in different-different ways")
format1 = current.strftime("%m/%d/%y")

# prints in month/date/year format
print("format1 =", format1)

format2 = current.strftime("%b-%d-%Y")
# prints in month(abbreviation)-date-year format
print("format2 =", format2)

format3 = current.strftime("%d/%m/%Y")

# prints in date/month/year format
print("format3 =", format3)

format4 = current.strftime("%B %d, %Y")

# prints in month(words) date, year format
print("format4 =", format4)
