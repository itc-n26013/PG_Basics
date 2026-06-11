topic={"身長":"159cm",
       "ペット":"ねこ",
       "好きな色":"水色"
       }

n=input("身長、ペット、好きな色を教えます:")
if n in topic:
    nakami=topic[n]
    print(nakami)
else:
    print("そんなこと教えないよ！")                  
