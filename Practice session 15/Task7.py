from datetime import datetime
time1=datetime.strptime("14:45:30","%H:%M:%S")
time2=datetime.strptime("10:30:00","%H:%M:%S")
time3=time1-time2
print(time3)
