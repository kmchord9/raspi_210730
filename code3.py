# -*- coding: utf-8 -*-
'''
キーボードで入力した数値の合計と平均を出します。
出力のファイル名を今日の日付で作成
'''

import csv
import datetime #時間を扱うライブラリ

#現在時刻の取得する
now = datetime.datetime.now()
#現在時刻から今日の日付を取得する
fileName = now.strftime('%Y%m%d') 

#ファイルを日付の文字列で作成
with open('{}.csv'.format(fileName), 'w') as f:
  sum = 0
  count =0
  while True:
    try:
      N = int(input('input number >>'))
      sum = sum + N
      count = count + 1
      print(N, file=f)
    except:
      print("***input end***")
      break

  print("sum:" ,file=f)
  print(sum ,file=f)
  print("average:" ,file=f)
  print(sum/count ,file=f)
