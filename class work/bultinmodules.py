from datetime import date, datetime,time,timedelta
today=time(19,30,30)
print(today)
#print(today.year)
now=datetime.now()
print(now)
print("year:",now.year)
print("month:",now.month)
print("day:",now.day)
print("Hour:",now.hour)
print("Minute:",now.minute)
print("Second:",now.second)
print(now.strftime('%d/%m/%Y'))
print(now.strftime('%H/%M/%S'))
print(now.strftime('%I/%M/%S'))
print(now.strftime('%A, %d %b %y %I :%M:%S %p'))
 



 #ADD TIME TO TIME LIKE DAYS,HOURS,MINUTES

today=date.today()
now=datetime.now()
n=today-timedelta(days=5)
print(n)
m=now-timedelta(minutes=5)
