# -*- coding: utf-8 -*-
'''
「number.csv」の内容を読み込んで合計と平均を出力します。
'''
import csv

with open('number.csv', 'r') as f:
  data = f.readlines()
  sum = 0
  count = 0

  for txt in data:
    N = int(txt.rstrip())
    sum = sum + N
    count = count + 1

print("sum:")   
print(sum)
print("average:")
print(sum/count)

