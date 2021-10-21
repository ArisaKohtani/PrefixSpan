from del_by_freq import del_by_freq
from del_by_freq import del_by_freq
minsup = 2 #input("minsup:")

#a~g → 1~7で表現  _は0
S1 = [ [1], [1,2,3], [1,3], [4], [3,6] ]
S2 = [ [1,2], [3], [2,3], [1,5] ]
S3 = [ [5,6], [1,2], [4,6], [3], [2] ]
S4 = [ [5], [7], [1,6], [3], [2], [3] ]
DB = [S1, S2, S3, S4]





#登場頻度がminsup未満の要素の削除
#DB[3] = del_by_freq(7, DB[3])
for i in range(len(del_elements)):
    for j in range(len(DB)):
        DB[j] = del_elem_in_ptn(del_elements[i], DB[j])
