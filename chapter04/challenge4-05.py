#文字列型の引数をfloat型に変換した数を戻り値にする関数と、
#その関数を使用した際に発生した例外処理

def float(a):
    try:
        return float(a)
    except (ValueError):
        print("数字ではないので処理を中止します")
#関数名: float_to
#引数名: s : データ型: str 
#戻り値: 引数をfloat型に変換した値

f = float("")
print(f)

#関数float_toに値を指定し、その結果を変数fに代入

