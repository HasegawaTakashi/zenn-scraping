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