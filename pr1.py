# -*- coding: utf-8 -*-
'''
キーボードで入力した数値をcsvファイルに出力します。
'''
import csv

with open('number.csv', 'w') as f:
  while True:
    try:
      N = int(input('input number >>'))
      print(N, file=f)
    except:
      print("***input end***")
      break

