from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

url = 'https://www.nikkei.com/nkd/company/history/dprice/?scode=6199&ba=1'
soup = BeautifulSoup(requests.get(url).text,'html.parser')

tag_tr = soup.find_all('tr')
head = [h.text for h in tag_tr[0].find_all('th')]

data = []
addTh = []
addTd = []

#データの収集
for i in range(1,len(tag_tr)):
        
    addTh.extend([t.text.strip() for t in tag_tr[i].find_all('th')])
    addTd.extend([d.text.replace(',','') for d in tag_tr[i].find_all('td')])
    
    addTh[len(addTh):len(addTh)] = addTd
    data.append(addTh)
    
    addTh = []
    addTd = []
data.reverse()
df = pd.DataFrame(data = data ,columns = head)
#軸の変更
df.set_index('日付',inplace = True)

#２次元配列からcsvを取得
df.to_csv('stock.csv',encoding = 'UTF8')

df = pd.read_csv('stock.csv',encoding = 'UTF8')

#日本語有効化
font_location = 'C:\Windows\Fonts\HGRME.TTC'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

#グラフ作成
#列指定
col = head[1:5]
df.plot(x = '日付',y = col,marker = 'o',figsize=(10,6))
#df.iloc[:,[0,1,2,3,4]].plot(marker = 'o')
plt.title('株価', {"fontsize": 20})
plt.xlabel('日付')
plt.ylabel('値')
plt.grid()
plt.locator_params(axis='x',nbins=len(df))
plt.locator_params(axis='y',nbins=10)
plt.tick_params(labelsize=10)
plt.legend(prop={"size": 10}, loc="upper right")
plt.savefig('save.png')
plt.show()
