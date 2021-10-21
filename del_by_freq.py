import itertools
import numpy as np

minsup = 2 #input("minsup:")#

S1 = [ [1], [1,2,3], [1,3], [4], [3,6] ]#
S2 = [ [1,4], [3], [2,3], [1,5] ]#
S3 = [ [5,6], [1,2], [4,6], [3], [2] ]#
S4 = [ [5], [7], [1,6], [3], [2], [3] ]#
DB = [S1, S2, S3, S4]#

counts = [[1,2,3,4,5,6,7],
          [0,0,0,0,0,0,0]]

for i in range(len(DB)):
    ary = list(itertools.chain.from_iterable(DB[i]))
    for j in range(len(counts[0])):
        if j+1 in ary:
            counts[1][j] += 1
print(list(itertools.chain.from_iterable(DB[0])))
print(counts)

del_elements = []
for i in range(len(counts[0])):
    if counts[1][i] < minsup:
        del_elements.append(counts[0][i])
print(del_elements)

def del_by_freq(del_element, pattern):
    output = []
    for i in range(len(pattern)):
        output.append([])
        for j in range(len(pattern[i])):
            if pattern[i][j] != del_element:
                output[i].append(pattern[i][j])
    for i in range(len(output)):
        if not output[len(output)-i-1]:
            del output[len(output)-i-1]
    return output

print(S4)
print(del_by_freq(7, S4))