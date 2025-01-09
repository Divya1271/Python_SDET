import datetime
# current_datetime=datetime.datetime.now()
# print("The current datetime is",current_datetime)
# date=datetime.date.today()
# print("Today's date is:",date)
# date=datetime.date(2025,7,12)
# print(date)
# time=datetime.time(14,30,20)
# print(time)


#Extracting data and time component
now=datetime.datetime.now()
print("Year",now.year)
print("Month",now.month)
print("Day",now.day)
print("Hour",now.hour)
print("Minutes",now.minute)
print("Seconds",now.second)

#Date arithmetic with timedelta

#add and subtract days

today=datetime.date.today()
future_date=today+datetime.timedelta(days=10)
print("10 days from today is:",future_date)

today=datetime.date.today()
future_date=today-datetime.timedelta(days=10)
print("10 days from today was:",future_date)


