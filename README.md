# 参考記事

* [日経株価スクレイピング](https://qiita.com/tt20210824/items/190fa85632b85621670f)

* [Zenn記事スクレイピング](https://qiita.com/mormas/items/d7802ac61fc96b303506)

* [Dockerイメージ軽量化](https://qiita.com/tt20210824/items/190fa85632b85621670f)

    clean-layer.sh:
        &emsp;docker-compose up時のRUNコマンド等を実行するたびにLayerが作成され、最終的に出来上がるimageが重くなる。
        RUNの最後にこのシェルスクリプトを実行して使用しないゴミ掃除をする
  <br>
とても勉強になりました。
ありがとうございます。

追記

* [mysql連携参考](https://takaya030.hatenablog.com/entry/2022/02/11/181847)
* [もういっちょ](https://qiita.com/harissa/items/117931ed3b15c8e6ad3b)
* [mysql変数使用](https://www.craneto.co.jp/archives/1219/)
* [sqlに単なる文字列挿入](https://shunyaueta.com/posts/2021-04-29/)
* [mysql cursor.execute() method](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
* [dbコンテナビルド前に他コンテナビルド始まっちゃう問題](https://docs.docker.com/compose/startup-order/)
* [docker-compose depends_on 色々分析](https://gotohayato.com/content/533/)
