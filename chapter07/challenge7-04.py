b=[5,10,15,20]

while True:
    an=input("数字をあてるんだ！終わるならｑおせよっ")
    if an =="q":
        break
    try:
        an=int(an)
    except ValueError:
        print("数字じゃないとだめだぞ！終わりたいならｑだぞ")
        continue

    if an in b:
        print("正解！なかなかやるな")
    else:
        print("不正解！努力しろ")
