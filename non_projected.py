from count_freq_DB import count_freq_DB
import copy
def non_projected(a, minsup, DB, ptn, all_elem):#最初は[]を渡す, ptnはsequential patternsを記録する配列
    print("now search: ", a)
    
    if (a == []): #aが最初の空[]だった場合
        ######## ↓ここをアイテム1つ(sampleでは1~7のそれぞれ)のみにすることで<x>-projectedDBが生成できる
        for i in all_elem:
            a_dash = [i] #[[a]]...[[g]]
            if count_freq_DB(DB, a_dash) >= minsup:#例えば一回目では[[g]]は満たさず操作されない
                non_projected(a_dash, minsup, DB, ptn, all_elem)#ここで再帰してa!=NULLになって頻出を抽出
                ptn += [a_dash]#minsupを超える系列を追加
    else:#最初以外でaが空じゃないとき
            extended = [] #拡張する配列一覧
            #[(ab)], [(ac)]... iを最後のアイテム集合に加える
            for i in all_elem:
                a_dash = copy.deepcopy(a)#.appendは値が変わってしまうからa_dashに値をコピー
                if a[-1][-1] < i[0]: #前に追加した要素より辞書順で後である(数字が大きい)アイテムのみ加える
                    a_dash[-1].append(i[0]) #[[a]]のとき、[[a,a]]
                    extended.append(a_dash)
            #[a,a], [a,b]... 系列を最後に加える
            for i in all_elem:
                a_dash = copy.deepcopy(a)#.appendは値が変わってしまうからa_dashに値をコピー
                a_dash.append(i) #[i]は系列で、系列同士を合体して[[a],[a]]
                extended.append(a_dash)

            #print("extended patterns are:", extended)
            frequents = []
            for beta in extended:
                times = count_freq_DB(DB, beta)
                print(beta, ":",times)
                if times >= minsup:#拡張候補から頻出なものを探してfrequentsにまとめておく
                        '''print(beta, " is frequent")'''
                        frequents.append(beta)

            for alpha in frequents:#頻出なものにnon_projectedかける
                non_projected(alpha, minsup, DB, ptn, all_elem)

            ptn += frequents#minsupを超える系列を追加
    return