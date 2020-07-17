import pprint
import requests
import json
import configparser

api = 'http://api.calil.jp/library?appkey={appkey}&pref={pref}&city={city}&systemid={systemid}&geocode={geocode}&format=json&callback&limit={limit}'

configIni = configparser.ConfigParser()
configIni.read('config.ini', encoding='utf-8')

apiKey = configIni.get('API','Id')

pref = input("県の入力:")
city = input("市区町村の入力:")
systemid = input("図書館のシステムIDの入力:")
geocode = input("緯度・経度の入力:")
limit = input("図書館の取得件数の入力:")

url = api.format(appkey=apiKey,pref=pref,city=city,systemid=systemid,geocode=geocode,limit=limit)

r = requests.get(url)
data = json.loads(r.text)
#pprint.pprint(data)

for lim in range(0,int(limit),1):
    pprint.pprint("図書館タイプ："+data[lim]["address"])
