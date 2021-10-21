import itertools
import numpy as np

minsup = 2 #input("minsup:")#

#a~g → 1~7で表現  _は0
S1 = [ [1], [1,2,3], [1,3], [4], [3,6] ]#
S2 = [ [1,4], [3], [2,3], [1,5] ]#
S3 = [ [5,6], [1,2], [4,6], [3], [2] ]#
S4 = [ [5], [7], [1,6], [3], [2], [3] ]#
DB = [S1, S2, S3, S4]#

counts = [[1,2,3,4,5,6,7],
          [0,0,0,0,0,0,0]]#入力値によって生成するように要変更

#def count_freq(DB,freq_pattern):#freq_patternは頻度をカウントしたい系列パターン配列



#登場頻度カウント
for i in range(len(DB)):
    ary = list(itertools.chain.from_iterable(DB[i]))
    for j in range(len(counts[0])):
        if j+1 in ary:
            counts[1][j] += 1
#print(list(itertools.chain.from_iterable(DB[0])))
#print(counts)

#登場頻度がminsup未満の要素の検索
del_elements = []
for i in range(len(counts[0])):
    if counts[1][i] < minsup:
        del_elements.append(counts[0][i])
#print(del_elements)