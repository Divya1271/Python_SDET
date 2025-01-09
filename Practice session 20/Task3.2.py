import datetime
file=open(r"C:\Users\divya aghi\PycharmProjects\Python_SDET\Practice session 20\log.txt","a")
t=datetime.date.today()
file.write(f"The current datetime is {t}\n")
