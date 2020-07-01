# コメント
"""
コメント
"""

import calendar
import random
from math import *
import math
from calendar import TextCalendar
print("hello world")

print("令和"+str(2)+"年", end="")
print("西暦"+str(1998+22)+"年")

print("""
あ
か
さ
た
な
""")

z = "hello \"takasi"
print(z)

z = "hello \n takasi"
print(z)

name = ["takesi", "hisosi", "aiko"]
len(name)

season = "spring", "summer", "fall", "winter"
season = ("spring", "summer", "fall", "winter")

id(season)


cal = calendar.TextCalendar()
cal.prmonth(2018, 2)

# 日曜始まり
cal = calendar.TextCalendar(6)
cal.prmonth(2018, 2)

cal = TextCalendar(6)
cal.prmonth(2018, 3)

cal = TextCalendar()
cals = cal.formatmonth(2018, 3)
print(cals)


math.pi

num = math.sqrt(81)
print(sqrt(49))

print(random.randint(15, 20))

# if
# a in b a not in b
# a is b aはbと同じオブジェクト is not
# not (a is b) 結果の反転

tokuten = int(input("please input score"))
if tokuten >= 80:
    print("A")
elif tokuten >= 70:
    print("B")
elif tokuten >= 60:
    print("C")
else:
    print("D")


kazu = int(input("数を入力してください:"))
print("偶数" if kazu % 2 == 0 else "奇数")


seibetsu=['男性',"女性"]
for sei in seibetsu:
    print(sei)

#for cnt in range(2):

#for cnt in range(1,5,1):

list(range(0,20,2))

kens =["t","g","f"]
for index,ken in enumerate(kens):
    print(str(index)+":"+ken)

#continue 初めに戻る

#複数ループ　インデックスの違いは調整する
for (ken,city) in zip(kens,citys):
    print("Ken:"+ken+"City:"+city)

#例外処理
#終了するためのライブラリ***************************
import sys
try:

except:
    sys exit():

#スライス
print(x[0:1])
#存在判定
print("Z" in x)

#ないと－１　あったら位置
print(x.find("Z"))

#format関数
x=18
y="成人"
print("{}歳は{}です",format(x,y))
print("{1}歳は{0}です",format(x,y))

print("{0:,}".format(100000))


list=["",""]+["",""]
list=["山"]*4

print(list[2:4])

#1つ飛ばして表示
print(list[::2])

weekday = "月,火,水,木,金,土,日"
#リストに変換
weekday_list=weekday.split(",")
print(weekday_list)

#リストの追加
list.append("日")

list = ["A",["B","C","D"],"E"]
print(list[0])
print(list[1][2])

#削除
list.remove("火")

#削除
del list[2]

del list[1:3]

#反転
list.reverse()

#最大　最小　加算
max(list)


list.sort()
list.sort(reverse=True)

list=sorted(list)

#コマンドプロンプトから値を挿入
import sys
for i in range(0,len(sys.argv)):
    print(sys.argv[i])

months={"jan":"1月","Feb":"2月"}
print(len(months))
#キーの選択
print(months["Feb"])
#追加
months["Apr"]="4月"
del(months["Feb"])
#存在確認
print("Feb"in months)

#要素表示
print(months.keys())
print(months.values())
print(months.items())

#イテレート*****************************************************
for en,jp in months.items():
    print("英語:{} 日本語:{}".format(en,jp))

#重複削除
sets=set(list)

sets.clear()

#^ チルダ　どちらか一方
kazu={}
kisuu={}
print(kazu | kisuu)
print(kazu & kisuu)
print(kazu - kisuu)
print(kazu ^ kisuu)

#タプルにはない
#内包表記****************************************************
bin=[2**n for n in range(0,17,1)]

rank=[r+"ランク"for r in "ABCDEF"]

rank=[r+"ランク"for r in "ABCDEF"if ~~~~~~]

if city.startswith("鳥取県")

teams = ["A","B"]
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

point=[10,10,20,100,40,50,60]
#集合ができる
fails={x for x in point if x<=60}
print(fails)


#関数

#call(kisuu=199,month=49)
#デフォルトの指定
def getPrice(price,tax=1.08)

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

#可変長引数 可変長引数はタプル型
print(keisan(1,2,3,4,5,mode="+"))

#map関数
#リストと関数を与えて処理をする関数
#fiter関数
#リストの中身を条件を指定して取得する関数













