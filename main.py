from prefixSpan import prefixSpan
from time import time

#minsup = int(input("enter minsup: "))
minsups = [0.75,0.5,0.25]
datasize = 10000

#f = open('sample.data', 'r')
f = open('10000-9.data', 'r')
data = f.readlines()
f.close

#generatorからのデータを整数型に整形
for line in range(len(data)):
    data[line] = data[line].split()
    data[line] = [int(elem) for elem in data[line]]


cnums = data[-1][0]
maxelm = 0
DB = []
for i in range(cnums):
    DB.append([])

for line in data:
    if line[-1] > maxelm:
        maxelm = line[-1]
    DB[line[0]-1].append(line[3:])

all_elem = []
for i in range(maxelm):
    all_elem.append([i])

'''
for i in DB:
    print("    ",i)
'''


for i in range(len(minsups)):
    minsup = minsups[i] * datasize
    print("minsup : ", minsup)
    sequential_patterns = []
    start = time()
    prefixSpan([], minsup, DB, sequential_patterns, all_elem)
    end = time()
    '''print("sequential_patterns are")
    for i in sequential_patterns:
        print("    ",i)'''
    print("runtime : ", end - start)

