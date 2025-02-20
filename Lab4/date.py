# Exercise 1
from datetime import datetime, timedelta

Now = datetime.now()

print(Now)
print(Now.strftime("%A"))

five_days_ago=Now-timedelta(days=5)

print(five_days_ago)
print(five_days_ago.strftime("%A"))



# Exercise 2
from datetime import datetime, timedelta

Today = datetime.now()
Yesterday = Today - timedelta(days=1)
Tomorrow = Today + timedelta(days=1)

print("Yesterday: ",Yesterday)
print(Yesterday.strftime("%A"))
print("Today: ",Today)
print(Today.strftime("%A"))
print("Tomorrow: ",Tomorrow)
print(Tomorrow.strftime("%A"))



# Exercise 3
from datetime import datetime, timedelta

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

print(formatted)



# Exercise 4
from datetime import datetime, timedelta

year = int(input("Enter the year of the first date: "))
month = int(input("Enter the month of the first date: "))
day = int(input("Enter the day of the first date: "))
hour = int(input("Enter the hour of the first date: "))
minute = int(input("Enter the minute of the first date: "))
second = int(input("Enter the second of the first date: "))
year2 = int(input("Enter the year of the second date: "))
month2 = int(input("Enter the month of the second date: "))
day2 = int(input("Enter the day of the second date: "))
hour2 = int(input("Enter the hour of the second date: "))
minute2 = int(input("Enter the minute of the second date: "))
second2 = int(input("Enter the second of the second date: "))
first_date = datetime(year,month,day,hour,minute,second)
second_date = datetime(year2,month2,day2,hour2,minute2,second2)
diff_in_seconds = first_date-second_date
diff_in_seconds = (abs(diff_in_seconds))

print("The first date is: ", first_date)
print("The second date is: ", second_date)
print("The difference is " ,diff_in_seconds.total_seconds(), " seconds")