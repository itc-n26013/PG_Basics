lists = []
rap = ["カニエ・ウェスト", "ジェイ・z", "エミネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "ティエスト"]
lists.append(rap)  #リストにrapの内容を追加
lists.append(rock)
lists.append(djs)
print(lists)

#　リストの番号0を要素をrapにいれた
rap = lists[0]  # print(list[0])と同じ意味
print(rap)

rap.append("ケンドリック・ラマー")
print(rap)
print(lists)

