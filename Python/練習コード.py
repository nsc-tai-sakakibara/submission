Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> user_name=""
>>> user_name
''
>>> year=input("please input this year")
please input this year2020
>>> year
'2020'
>>> import calendar,math


>>> cal=calendar.TextCalendar()
>>> cal.prmonth(2018,2)
   February 2018
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28
>>> bin=[2**n for n in range(0,17,1)]
>>> print(bin)
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
>>> teams = ["A","B"]
>>> team_dic = {t:0 for t in teams}
>>> print(team_dic)
{'A': 0, 'B': 0}
>>> points=[40,59]
>>> team_dic={t:p for t,p in zip(teams,points)}
>>> print(teams_dic)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(teams_dic)
NameError: name 'teams_dic' is not defined
>>> print(team_dic)
{'A': 40, 'B': 59}
>>> team_dic={str(p):t for (t,p) in team_dic.items()}
>>> print(team_dic)
{'40': 'A', '59': 'B'}
>>> x=0
>>> def setCount(y):
	x=y

	
>>> def setCount2(y):
	global x
	x=y

	
>>> setCount(10)
>>> print(x)
0
>>> setCount2(12)
>>> print(x)
12
>>> getPrice=lambda price,tax=1.08 : int(price*tax)
>>> print(getPrice(1000))
1080
>>> print(getPrice(1000,1.1))
1100
>>> 