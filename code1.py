# -*- coding: utf-8 -*-
'''
キーボードで入力した数値の合計と平均を出します。
'''

#合計とカウント用の変数の初期化
sum = 0
count = 0

#無限ループ
while True:
  try:
    #数値の入力の待ち受け
    N = int(input('input number >>'))
    #合計値
    sum = sum + N
    #入力した数
    count = count + 1

  #入力に数値以外を入れたとき終了  
  except:
    print("***input end***")
    break

#合計と平均を出力
print("sum:")
print(sum)
print("average:")
print(sum/count)
