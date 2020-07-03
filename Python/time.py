import datetime
a=datetime.datetime.now()
#b=datetime.datetime.strptime(a,"%p/%Y/%m/%d %H:%M:%S")
b=a.strftime("%H:%M:%S")

print(b)