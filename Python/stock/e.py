from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import re

url = 'https://www.nikkei.com/nkd/company/history/dprice/?scode=6199&ba=1'
soup = BeautifulSoup(requests.get(url).text,'html.parser')
#print(soup)

tag_tr = soup.find_all('tr')
head = [h.text for h in tag_tr[0].find_all('th')]

data = []
addTh = []
addTd = []
for i in range(1,len(tag_tr)):
        
    tate = [t.text.strip() for t in tag_tr[i].find_all('th')]
    
    addTh.extend(tate)
    #print(addTh)
        #data.append([d.text for d in tag_tr[i].find_all('th')])
        #df = pd.DataFrame(data, columns = head)
    
    #addTd.extend([re.sub('\\D','',d.text) for d in tag_tr[i].find_all('td')])
    addTd.extend([d.text.replace(',','') for d in tag_tr[i].find_all('td')])
    
    #addTd_int = [re.search('[0-9]+',s) for s in addTd]
    #addTd_init = [int(l) for l in addTd_int]
    #print(addTd)
    addTh[len(addTh):len(addTh)] = addTd
    #print(addTh)
    
    
    #data[len(data):len(data)] = addTh
    data.append(addTh)
    #print(data)
    
    #綺麗に
    #result = ','.join(addTh)
    #print(result)
    #data.append(addTh)
    #print(data)
    
    addTh = []
    addTd = []
data.reverse()
df = pd.DataFrame(data = data ,columns = head)
#一行で出来ないのかな？
df.set_index('日付',inplace = True)

("""
#
#headの中身
col = head
col[0:1] = []
col = ['始値','始値','高値','安値','終値','売買高','修正後終値']
for c in col:
    list(map(int,df[c]))
    df[c] = df[c].astype(float)
df['日付'] = [datetime.strptime(i,'%Y-%m-%d') for i in df['日付']]

print(df)
""")

df.to_csv('stock.csv',encoding = 'UTF8')
#for i in (0,len(df)-1,1):
    #df.iat[i,-1] = df.iat[i,-1][:-3]

df.rename(index = lambda s:s[:-3])
#print(df)
df = pd.read_csv('stock.csv',encoding = 'UTF8')

#font_location = 'C:\Windows\Fonts\BIZ-UDMinchoM.ttc'
font_location = 'C:\Windows\Fonts\HGRME.TTC'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)
#df.plot()
#fig=plt.figure(figsize=(10,6))
col = head[1:5]
("""
fig=plt.figure(figsize=(10,6))

ax = fig.add_subplot(1,1,1)
for point in len(df):
    ax.plot(['日付'],[c],marker = 'o')

#ax.plot(['日付','a','b','c'],col,marker = 'o')

#fig.savefig('save.png')
#exit()
""")

df.plot(x = '日付',y = col,marker = 'o',figsize=(10,6))
#df.iloc[:,[0,1,2,3,4]].plot(marker = 'o')

plt.title('株価', {"fontsize": 20})
plt.xlabel('日付')
plt.ylabel('値')
plt.grid()
plt.tick_params(labelsize=10)
plt.legend(prop={"size": 10}, loc="upper right")
#曜日以降を消して下の処理を行う？
#df['日付'] = [datetime.strptime(i,'%m-%d') for i in df['日付']]

#dfGulaf = df.iloc[:, [0,4]]
#dfGulaf.plot()
plt.show()

("""
fig = go.Figure(
    data = [go.candlestick(
        x = df['data'],
        open = ['open'],
        high = df['high'],
        low = df['low'],
        close = df['close']
    )]
)
fig.show
""")

#列の指定の仕方？？？？？？？？？？？