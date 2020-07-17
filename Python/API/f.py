
("""
category    図書館の種類
city        町
short       名前
libkey      short と同じときもある
pref　      県
geocode　   緯度経度

systemid    図書館システムID
address     住所
libid       図書館id
tel         電話番号
systemname  市区町村の名前になってる
isil        なんかの番号
post        郵便番号
url_pc      サイト
formal      正式名称

検索機能を作る

地域
蔵書

ほしい情報

場所
開館時間　のurl　無理？
貸し出し方法
返却方法

辞書型の要素が入っている配列がcallback に入っている

""")

import pprint
import requests
import json
import tkinter
import configparser

("""
def cal():
    url = api.format(appkey=apiKey,pref=pref,city=city,systemid=systemid,geocode=geocode,limit=limit)

    r = requests.get(url)
    data = json.loads(r.text)    
    #pprint.pprint(data)
    for lim in range(0,int(limit),1):
        pprint.pprint("図書館タイプ："+data[lim]["address"])
""")

#api = 'http://api.calil.jp/library?appkey={appkey}&pref={pref}&city={city}&systemid={systemid}&geocode={geocode}&format=json&callback&limit={limit}'
api = 'http://api.calil.jp/library?appkey={appkey}&pref{pref}&city{city}&systemid{systemid}&geocode{geocode}&format=json&callback&limit{limit}'
configIni = configparser.ConfigParser()
configIni.read('config.ini', encoding='utf-8')

apiKey = configIni.get('API','Id')

enters = []
root = tkinter.Tk()

root.geometry('400x300')
root.title('検索内容')
alart = tkinter.Label(text='県、図書館のシステムID、緯度・軽度のいずれか１つは入力してください')
alart.place(x=30, y=30)

p = tkinter.Label(text='県')
p.place(x=30, y=60)
pref = tkinter.Entry(width=30)
pref.place(x=150, y=60)
enters.append(pref)

s = tkinter.Label(text='図書館のシステムID')
s.place(x=30, y=90)
systemid = tkinter.Entry(width=30)
systemid.place(x=150, y=90)
enters.append(systemid)

g = tkinter.Label(text='緯度・経度')
g.place(x=30, y=120)
geocode = tkinter.Entry(width=30)
geocode.place(x=150, y=120)
enters.append(geocode)

l = tkinter.Label(text='図書館の取得件数')
l.place(x=30, y=150)
limit = tkinter.Entry(width=30)
limit.place(x=150, y=150)
enters.append(limit)

button1 = tkinter.Button(root, text="実行", font=("Meiryo UI", 8), width=8,
    height=2, bg="steel blue", fg="white", command=cal(api,apiKey,pref,city,systemid,geocode,limit))
button1.place(x=200, y=180)


#tkinter 終わらせるための　完了ボタン？
#配列化 zip
#ほしい情報用の tkinter
#””がない表示

root.mainloop()
#.pack?

("""
url = api.format(appkey=apiKey,pref=pref,city=city,systemid=systemid,geocode=geocode,limit=limit)

r = requests.get(url)
data = json.loads(r.text)    
pprint.pprint(data)
apiKey = str(input("API キーの入力:"))

#API key
#pref systemid geocode どれか
#データ数 limit

#一度に検索内容を入れて　検索内容と結果を表示する

#県がなかったら追加　どっちでもよかった
pref = str(input("県の入力:"))
city = str(input("市区町村の入力:"))
systemid = str(input("図書館のシステムIDの入力:"))
geocode = str(input("緯度、経度の入力:"))
limit = str(input("図書館の取得件数の入力:"))
#空なら　ないと表示
#map で出力

url = api.format(appkey=apiKey,pref=pref,city=city,systemid=systemid,geocode=geocode,limit=limit)

r = requests.get(url)
data = json.loads(r.text)    
wantData = str(input("欲しい情報は何ですか？："))
#pprint.pprint(data[0]["category"])
pprint.pprint(data)
""")

