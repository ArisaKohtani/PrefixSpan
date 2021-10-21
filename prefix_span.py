import itertools
import numpy as np

minsup = 2 #input("minsup:")#

#a~g → 1~7で表現  _は0
S1 = [ [1], [1,2,3], [1,3], [4], [3,6] ]#
S2 = [ [1,4], [3], [2,3], [1,5] ]#
S3 = [ [5,6], [1,2], [4,6], [3], [2] ]#
S4 = [ [5], [7], [1,6], [3], [2], [3] ]#
DB = [S1, S2, S3, S4]#


in1 = S2#
in2 = [[5]]#



def postfix(a,b,DB):
    DB_array =  list(itertools.chain.from_iterable(list(itertools.chain.from_iterable(DB))))
    u, counts = np.unique(DB_array, return_counts=True)
    #print(u,counts)


    r = l = -1
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == b[len(b)-1][0]:
                r = i
                l = j
                break
        else:
            continue
        break

    if r == -1:
        return print("postfix is empty!")
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
        return print("postfix is empty!")
    return a



print("S1:",postfix(S1, in2, DB))
print("S2:",postfix(S2, in2, DB))
print("S3:",postfix(S3, in2, DB))
print("S4:",postfix(S4, in2, DB))