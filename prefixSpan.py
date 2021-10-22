import count_freq
import postfix
import copy


def prefixSpan(a, minsup, DB, ptn):#最初は[]を渡す, ptnはsequential patternsを記録する配列
    print("now prefix search: ", a, "in data: ")
    for p in DB:
        print("    ",p)
    DBcopy = copy.deepcopy(DB)
    all_elem = [[1], [2], [3], [4], [5], [6], [7]]
    if (a == []): #aが最初の空[]だった場合
        ######## ↓ここを1~7のそれぞれのみにすることで<x>-projectedDBが生成できる
        for i in all_elem:
            a_dash = [i] #[[a]]...[[g]]
            DBcopy = copy.deepcopy(DB)
            if count_freq.count_freq(DBcopy, a_dash) >= minsup:#例えば一回目では[[g]]は満たさず操作されない
                print(a_dash, " is frequent in ")
                for p in DBcopy:
                    print("    ",p)
                print("so now making ",a_dash,"-projection." )
                projected_DB = [postfix.postfix(DBcopy[0],a_dash),postfix.postfix(DBcopy[1],a_dash),
                                postfix.postfix(DBcopy[2],a_dash),postfix.postfix(DBcopy[3],a_dash)]
                prefixSpan(a_dash, minsup, projected_DB, ptn)#ここで再帰してa!=NULLになって頻出を抽出
                ptn += a_dash#minsupを超える系列を追加
    else:#最初以外でaが空じゃないとき
            extended = [] #拡張する配列一覧
            #[(ab)], [(ac)]... iを最後のアイテム集合に加える
            for i in all_elem:
                a_dash = copy.deepcopy(a)#.appendは値が変わってしまうからa_dashに値をコピー
                if a_dash[-1][-1] < i[0]: #前に追加した要素より辞書順で後である(数字が大きい)アイテムのみ加える
                    a_dash[-1].append(i[0]) #[[a]]のとき、[[a,a]]
                    extended.append(a_dash)
            #[a,a], [a,b]... 系列を最後に加える
            #a_dash = a #.appendは値が変わってしまうからa_dashに値をコピー
            for i in all_elem:
                a_dash = copy.deepcopy(a)#.appendは値が変わってしまうからa_dashに値をコピー
                a_dash.append(i) #[i]は系列で、系列同士を合体して[[a],[a]]
                extended.append(a_dash)

            print("extended patterns are:", extended)
            frequents = []
            for a in extended:
                times = count_freq.count_freq(DB, a)
                print(a, ":",times)
                if times >= minsup:#拡張候補から頻出なものを探してfrequentsにまとめておく
                        print(a, " is frequent")
                        frequents.append(a)


            for alpha in frequents:#頻出なものにprefixSpanかける
                print("now making ",alpha,"-projection." )
                DBcopy = copy.deepcopy(DB)
                for p in DBcopy:
                    print("    ", p)
                projected_DB = [postfix.postfix(DBcopy[0],alpha),postfix.postfix(DBcopy[1],alpha),
                                postfix.postfix(DBcopy[2],alpha),postfix.postfix(DBcopy[3],alpha)]
                prefixSpan(alpha, minsup, projected_DB, ptn)
            ptn += frequents#minsupを超える系列を追加
    #print("return", a)
    DB = DBcopy
    return