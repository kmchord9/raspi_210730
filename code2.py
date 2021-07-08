# -*- coding: utf-8 -*-
'''
キーボードで入力した数値の合計と平均を出します。
出力先をcsvファイルに変更
'''
import csv

#書き込み用のファイルを開く
with open('data.csv', 'w') as f:
  sum = 0
  count =0
  while True:
    try:
      N = int(input('input number >>'))
      sum = sum + N
      count = count + 1
      print(N, file=f) #file=fでファイルに出力
    except:
      print("***input end***")
      break

  print("sum:" ,file=f)
  print(sum ,file=f)
  print("average:" ,file=f)
  print(sum/count ,file=f)
