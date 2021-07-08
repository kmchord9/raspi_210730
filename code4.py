# -*- coding: utf-8 -*-
'''
「number.csv」の内容を読み込んで出力します。
'''

import csv

#ファイルを読み込み専用で開く
with open('test.csv', 'r') as f:
  #ファイルのデータを一度に読み込む
  data = f.readlines()

  #読み込んだデータを1行ずつ表示する
  for txt in data:
    print(int(txt.rstrip()))
