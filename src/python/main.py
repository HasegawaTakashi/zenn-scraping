from bs4 import BeautifulSoup
import requests
from time import sleep
import mysql.connector
import os
from dotenv import load_dotenv

"""
databaseの立ち上げまで待機する
https://docs.docker.com/compose/startup-order/
上記のラッパーシェルスクリプトをを理解できるまではsleepで対応
"""

sleep(25)
class Scraping:

    def get_data(table_name, url):
        item_count = 10
        d_list = []
        r = requests.get(url)

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            contents = soup.find_all('div', class_='ArticleList_itemContainer__xlBMc')
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

        load_dotenv()
        db_name = os.environ.get('DATABASE')
        cnx = mysql.connector.connect(
            host = os.environ.get('HOST'),
            port = os.environ.get('PORT'),
            user = os.environ.get('USER'),
            password = os.environ.get('PASSWORD'),
            database = os.environ.get('DATABASE'),
        )
        cursor = cnx.cursor()

        create_database_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
            id int not null auto_increment primary key,
            title varchar(100),
            author varchar(50),
            link varchar(200),
            created_at datetime not null default current_timestamp)
        """
        init_table_query = (f"DELETE FROM {db_name}.{table_name}")
        records = []
        for i in range(item_count):
            title = d_list[i]['title']
            author = d_list[i]['author']
            link = d_list[i]['link']

            data = (title, author, link)
            records.append(data)
        insert_query =(f"INSERT INTO {db_name}.{table_name}(title, author, link) VALUES(%s, %s, %s)")

        cursor.execute(create_database_query)
        cursor.execute(create_table_query)
        cursor.execute(init_table_query)
        cursor.executemany(insert_query, records)
        cnx.commit()


def scraping():
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
        Scraping.get_data(list, urls)
        num += 1

scraping()
print('finished all')
