from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import datetime
import mysql.connector

class connect:
    cnx = mysql.connector.connect(
        host = '192.168.2.2',
        port = '3306',
        user = 'docker',
        password = 'docker',
        database = 'zenn',
    )



class Scraping:

    def scraping(string, url):
        # 変数d_listに空のリストを作成する
        d_list = []
        r = requests.get(url)

        if r.status_code == 200:
            # 取得結果を解析してsoupに格納
            soup = BeautifulSoup(r.text, 'html.parser')
            # ArticleList_itemContainer__xlBMcクラスを持ったdivタグをすべて取得して、変数contentsに格納
            contents = soup.find_all('div', class_='ArticleList_itemContainer__xlBMc')
            #3秒ウェイトを入れる
            sleep(3)

            n = 0
            for content in contents:
                if n < 10:
                    link = 'https://zenn.dev' + content.a.get('href')
                    title = content.find('h2').text
                    author = content.find('div', class_='ArticleList_userName__GWXDx').text
                    time = content.time.get('datetime')
                    slice_time = time[:-15]
                    d = {
                        'title' : title,
                        'author' : author,
                        'link' : link,
                        'time' : slice_time,
                    }
                    d_list.append(d)
                    n += 1
                elif n == 10:
                    break

        # 変数d_listを使って、データフレームを作成する
        df = pd.DataFrame(d_list)

        # to_csv()を使って、データフレームをCSV出力する
        df.to_csv(f'./csv_files/{string}_' + str(datetime.date.today()) + '.csv', index=None, encoding='utf-8-sig')

        print(string, 'is success')


def save_to_csv():
    scraping_lists = [
            'python',
            'docker',
            'linux',
            'git',
            'sql',
            'web',
    ]

    num = 0
    for list in scraping_lists:
        urls = f'https://zenn.dev/topics/{scraping_lists[num]}'

        print(list)
        print(urls)

        python = Scraping.scraping(list, urls)
        num += 1

save_to_csv()

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
