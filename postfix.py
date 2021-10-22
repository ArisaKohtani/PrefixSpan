import itertools
import numpy as np


'''
minsup = 2 #input("minsup:")#
#a~g → 1~7で表現  _は0
S1 = [ [1], [1,2,3], [1,3], [4], [3,6] ]#
S2 = [ [1,4], [3], [2,3], [1,5] ]#
S3 = [ [5,6], [1,2], [4,6], [3], [2] ]#
S4 = [ [5], [7], [1,6], [3], [2], [3] ]#
<a>-projected db
S1 = [[1, 2, 3], [1, 3], [4], [3, 6]]
S2 = [[0, 4], [3], [2, 3], [1, 5]]
S3 = [[0, 2], [4, 6], [3], [2]]
S4 = [[0, 6], [3], [2], [3]]
DB = [S1, S2, S3, S4]
in1 = S2#
in2 = [[1]]#
'''

#generate postfix
def postfix(a,b):#a is alpha, b is beta and DB is projected DataBase.
    #b = <a b>
    if len(b[len(b)-1]) == 1:
        r = l = -1
        for i in range(len(a)):
            if 0 in a[i]:
                continue
            for j in range(len(a[i])):
                if a[i][j] == b[len(b)-1][0]:
                    r = i
                    l = j
                    break
            else:
                continue
            break

        if r == -1:
            return []
        else:
            del a[0:r]
            if len(a[0]) == 1:
                del a[0]
            elif l == 0:
                a[0][0] = 0
            else:
                del a[0][0:l]
                a[0][0] = 0

        if len(a)==1 and len(a[0])==1 and a[0][0]==0:
            return []
        if not a:
            return []
        return a
    
    #b = <(ab)>
    else:
        x = b[len(b)-1][len(b[len(b)-1])-1]#アイテム集合の末尾
        r = l = -1
        for i in range(len(a)):
            if 0 in a[i]:
                for j in range(len(a[i])):
                    if a[i][j] == x:
                        r = i
                        l = j
                        print(r,l)
                        break
                else:
                    continue
                break
            else:#rlがbの位置になるように
                flag = 0 # 上手にbreakできませんでした
                for j in range(len(b[len(b)-1])-1):
                    flag = 1
                    if b[len(b)-1][j] not in a[i]:
                        flag = 0
                        break
                if flag == 1:
                    for j in range(len(a[i])):
                        if a[i][j] == x:
                            r = i
                            l = j
                            break
                    else:
                        continue
                    break    

        #配列処理
        if r == -1:
            return []
        else:
            del a[0:r]
            if len(a[0]) == 1:
                del a[0]
            elif l == 0:
                a[0][0] = 0
            else:
                del a[0][0:l]
                if len(a[0]) == 1:
                    del a[0]
                else:
                    a[0][0] = 0

        #emptyパターン
        if len(a)==1 and len(a[0])==1 and a[0][0]==0:
            return []
        if not a:
            return []

        return a

'''
print("S1:",postfix(S1, in2, DB))
print("S2:",postfix(S2, in2, DB))
print("S3:",postfix(S3, in2, DB))
print("S4:",postfix(S4, in2, DB))
'''