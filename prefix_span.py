import numpy as np

minsup = 2#input("minsup:")
#a~g → 1~7で表現  _は0
S1 = [ [1], [1,2,3], [1,3], [4], [3,6] ]
S2 = [ [1,2], [3], [2,3], [1,5] ]
S3 = [ [5,6], [1,2], [4,6], [3], [2] ]
S4 = [ [5], [7], [1,6], [3], [2], [3] ]
DB = [S1, S2, S3, S4]

print(len(S1[1]))

def postfix(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == b[]
        


#def PrefixSpan(a, l, DB):
