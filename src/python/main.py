from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import datetime
import mysql.connector
import os
from dotenv import load_dotenv
import glob

"""
databaseの立ち上げまで待機する
https://docs.docker.com/compose/startup-order/
上記のラッパーシェルスクリプトをを理解できるまではsleepで対応
"""

sleep(25)
class Scraping:

    def scraping(table_name, url):
        # スクレイピング希望回数を記述 min: 1, max: 48 (zenn記事1ページ上限48記事のため)
        item_count = 48
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
                if n < item_count:
                    link = 'https://zenn.dev' + content.a.get('href')
                    title = content.find('h2').text
                    author = content.find('div', class_='ArticleList_userName__GWXDx').text
                    time = content.time.get('datetime')
                    slice_time = time[:-15]
                    d = {
                        'title' : title,
                        'author' : author,
                        'link' : link,
                        # 'time' : slice_time, # urlにdatetimeが含まれてしまうので改善するまでコメントアウト
                    }
                    d_list.append(d)
                    n += 1
                elif n == item_count:
                    break

        # 変数d_listを使って、データフレームを作成する
        df = pd.DataFrame(d_list)

        # to_csv()を使って、データフレームをCSV出力する
        # df.to_csv(f'./csv_files/{list_name}_' + str(datetime.date.today()) + '.csv', index=None, encoding='utf-7-sig')

        # print(list_name, 'is success')
        # print(d_list)

        load_dotenv()
        cnx = mysql.connector.connect(
            host = os.environ.get('HOST'),
            port = os.environ.get('PORT'),
            user = os.environ.get('USER'),
            password = os.environ.get('PASSWORD'),
            database = os.environ.get('DATABASE'),
        )
        cursor = cnx.cursor()

        def get_query(query_file_path, table_name):
            with open(query_file_path, 'r', encoding='utf-8') as f:
                query = f.read().format(table_name=table_name)
            return query

        query_file_paths = glob.glob('sql/*')
        for query_file_path in query_file_paths:
            query = get_query(query_file_path, table_name)
            cursor.execute(query)

        # insert scraping data
        records = []
        for i in range(item_count):
            title = d_list[i]['title']
            author = d_list[i]['author']
            link = d_list[i]['link']

            data = (title, author, link)
            records.append(data)
        print(records)

        query5 =(f"INSERT INTO zenn.{table_name}(title, author, link) VALUES(%s, %s, %s)")
        cursor.executemany(query5, records)
        cnx.commit()
        print('finished insert variable data')


def save_to_csv():
    scraping_lists = [
            'python',
            'docker',
            'linux',
            'git',
            'mysql',
            'web',
            'kubernetes',
            'aws',
    ]

    num = 0
    for list in scraping_lists:
        urls = f'https://zenn.dev/topics/{scraping_lists[num]}'

        print(list)
        print(urls)

        python = Scraping.scraping(list, urls)
        num += 1

save_to_csv()
print('finished all')
