from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime

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
    addTd.extend([d.text for d in tag_tr[i].find_all('td')])
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

df = pd.DataFrame(data=data, columns = head)
print(df)

("""
#
#headの中身
col = ['始値','始値','高値','安値','終値','売買高','修正後終値']
for c in col:
    df[c] = df[c].astype(float)
df['日付'] = [datetime.strptime(i,'%Y-%m-%d') for i in df['日付']]

print(df)
""")

df = pd.read_csv('stock.csv')
df.head()