import requests

from bs4 import BeautifulSoup
import requests

# 変数urlに、Zenn新着ページのURLを入れる
url = 'https://zenn.dev/articles?page={1}'

# urlへのアクセス結果を変数rに格納
r = requests.get(url)

# 取得結果を解析してsoupに格納
soup = BeautifulSoup(r.text)

# ArticleList_itemContainer__xlBMcクラスを持ったdivタグをすべて取得して、変数contentsに格納
contents = soup.find_all('div', class_='ArticleList_itemContainer__xlBMc')

print(contents)


#r = requests.get('https://nikkei225jp.com/chart/')
#text = r.text
#date = text.split('<div class=wtimeT>')[1].split('</div>')[0]
#nikkei = text.split('<div class=if_cur>')[1].split('</div>')[0].replace(',','')
#dau = text.split('<div class=if_cur>')[2].split('</div>')[0].replace(',','')
#kawase = text.split('<div class=if_cur>')[3].split('</div>')[0].replace(',','')

#print('今日は',date,'です')
#print ('日経株価は ',nikkei, '円です')
#print ('ダウ平均株価は', dau, '円です')
#print ('為替ドルは', kawase,'円です')

