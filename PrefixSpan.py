import count_freq
import postfix
import copy


def prefixSpan(a, minsup, DB):#最初は[]を渡す
    print("now prefix search: ", a, "in data: ", DB)
    if (DB == None):
        return -1
    all_elem = [[1], [2], [3], [4], [5], [6], [7]]
    if (a == []): #aが最初の空[]だった場合
        for i in all_elem:
            a_dash = [i] #[[a]]...[[g]]
            if count_freq.count_freq(DB, a_dash) >= minsup:#例えば一回目では[[g]]は満たさず操作されない
                print(a_dash, " is frequent in ", DB)
                print("so now making ",a_dash,"-projection." )
                projected_DB = [postfix.postfix(DB[0],a_dash,DB),postfix.postfix(DB[1],a_dash,DB),
                                postfix.postfix(DB[2],a_dash,DB),postfix.postfix(DB[3],a_dash,DB)]
                prefixSpan(a_dash, minsup, projected_DB)#ここで再帰してa!=NULLになって頻出を抽出
    else:#最初以外でaが空じゃないとき
            #a_dash = a #.appendは値が変わってしまうからa_dashに値をコピー
            #[(ab)], [(ac)]... iを最後のアイテム集合に加える
            for i in all_elem:
                a_dash = copy.deepcopy(a)
                if a_dash[-1][-1] < i[0]: #前に追加した要素より辞書順で後である(数字が大きい)アイテムのみ加える
                    a_dash[-1].append(i[0]) #[[a]]のとき、[[a,a]]
                    print(a_dash, " : ", count_freq.count_freq(DB, a_dash), " in ", DB)
                    if count_freq.count_freq(DB, a_dash) >= minsup:#例えば一回目では[[g]]は満たさず操作されない
                        print(a_dash, " is frequent in ", DB)
                        print("so now making ",a_dash,"-projection." )
                        projected_DB = [postfix.postfix(DB[0],a_dash,DB),postfix.postfix(DB[1],a_dash,DB),
                                        postfix.postfix(DB[2],a_dash,DB),postfix.postfix(DB[3],a_dash,DB)]
                        prefixSpan(a_dash, minsup, projected_DB)
            #[a,a], [a,b]... 系列を最後に加える
            #a_dash = a #.appendは値が変わってしまうからa_dashに値をコピー
            for i in all_elem:
                a_dash = copy.deepcopy(a)
                a_dash.append(i) #[i]は系列で、系列同士を合体して[[a],[a]]
                print(a_dash, " : ", count_freq.count_freq(DB, a_dash), " in ", DB)
                if count_freq.count_freq(DB, a_dash) >= minsup:#例えば一回目では[[g]]は満たさず操作されない
                        print(a_dash, " is frequent in ", DB)
                        print("so now making ",a_dash,"-projection." )
                        projected_DB = [postfix.postfix(DB[0],a_dash,DB),postfix.postfix(DB[1],a_dash,DB),
                                        postfix.postfix(DB[2],a_dash,DB),postfix.postfix(DB[3],a_dash,DB)]
                        prefixSpan(a_dash, minsup, projected_DB)
    return
