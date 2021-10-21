minsup = 2 

#a~g → 1~7で表現  _は0
S1 = [ [1], [1,2,3], [1,3], [4], [3,6] ]
S2 = [ [1,4], [3], [2,3], [1,5] ]
S3 = [ [5,6], [1,2], [4,6], [3], [2] ]
S4 = [ [5], [7], [1,6], [3], [2], [3] ]
DB = [S1, S2, S3, S4]



def prefixSpan(a, minsup, DB):#最初は[]を渡す
    if (a == []): #aが最初の空[]だった場合
        all_elem = [[1], [2], [3], [4], [5], [6], [7]]
        for i in all_elem:
            a_dash = [[i]] #[[a]]...[[g]]
            prefixSpan(a_dash, minsup, postfix(DB, a_dash))#ここで再帰してa!=NULLになって頻出を抽出
    else:#最初以外でaが空じゃないとき
        if count_freq(DB, a) >= minsup:
            a_dash = a
            #[(ab)], [(ac)]... iを最後のアイテム集合に加える
            a_dash[-1].append(i[0]) #[[a]]のとき、[[a,a]]
            print(a_dash)
            prefixSpan(a_dash, minsup, postfix(DB, a_dash))
            #[a,a], [a,b]... 系列を最後に加える
            a_dash = a
            a_dash.append[i] #[i]は系列で、系列同士を合体して[[a],[a]]
            print(a_dash)
            prefixSpan(a_dash, minsup, postfix(DB, a_dash))
    
    return
