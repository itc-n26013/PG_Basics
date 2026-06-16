try:
    print("animals".index("z"))
except:
     print("Not found")

#エラーが発生したときに別の処理を行う try と except の例です。
#まず Python は try の中を実行します。"animals" の文字の位置にはｚはないのでエラー。
#エラーが発生したので、exceptが実行される。
#try: エラーが起こるかもしれない処理
#except:エラーが起きたときの処理

#どんなエラーでも捕まえるのではなく、発生するエラーを指定することが多いです。
