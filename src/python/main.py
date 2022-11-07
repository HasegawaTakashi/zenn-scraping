from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import datetime

class Scraping:

    
    def scrape(url, string):
        # 変数d_listに空のリストを作成する
        d_list = []
        #ページ番号i
        i=0
        # アクセスするためのURLをtarget_urlに格納する 
        # i +=1
        # target_url = url.format(i)
        target_url = url
        # target_urlへのアクセス結果を、変数rに格納
        r = requests.get(target_url)

        if r.status_code == 200:
            # print('d_listの大きさ：', len(d_list))
            # print()してtarget_urlを確認する
            # print(target_url)

            # 取得結果を解析してsoupに格納
            soup = BeautifulSoup(r.text, 'html.parser')
            # ArticleList_itemContainer__xlBMcクラスを持ったdivタグをすべて取得して、変数contentsに格納
            contents = soup.find_all('div', class_='ArticleList_itemContainer__xlBMc')
            #1秒ウェイトを入れる
            sleep(1)

            n = 0
            for content in contents:
                if n < 10:    
                    link = 'https://zenn.dev' + content.a.get('href')
                    title = content.find('h2').text
                    author = content.find('div', class_='ArticleList_userName__GWXDx').text
                    time = content.time.get('datetime')
                    d = {
                        'title' : title,
                        'author' : author,
                        'link' : link,
                        'time' : time,
                    }
                    d_list.append(d)
                    n += 1
                elif n == 10:
                    break

        # 変数d_listを使って、データフレームを作成する
        df = pd.DataFrame(d_list)
        # to_csv()を使って、データフレームをCSV出力する
        df.to_csv(f'./csv_files/{string}_' + str(datetime.date.today()) + '.csv', index=None, encoding='utf-8-sig')

python_url = 'https://zenn.dev/topics/python'
python_str = 'python'
# docker_url = 'https://zenn.dev/topics/docker'
# docker_str = 'docker'
# linux_url = 'https://zenn.dev/topics/linux'
# linux_str = 'linux'
# git_url = 'https://zenn.dev/topics/git'
# git_str = 'git'
# sql_url = 'https://zenn.dev/topics/sql'
# sql_str = 'sql'

python = Scraping.scrape(python_url, python_str)
# docker = Scraping.scrape(docker_url, docker_str)
# linux = Scraping.scrape(linux_url, linux_str)
# git = Scraping.scrape(git_url, git_str)
# sql = Scraping.scrape(sql_url, sql_str)


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
