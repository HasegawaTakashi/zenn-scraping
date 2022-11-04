https://qiita.com/tt20210824/items/190fa85632b85621670f

clean-layer.sh:
    docker-compose up時のRUNコマンド等を実行するたびにLayerが作成され、最終的に出来上がるimageが重くなる。
    RUNの最後にこのシェルスクリプトを実行して使用しないゴミ掃除をする# python-docker-study
