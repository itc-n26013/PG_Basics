#文字列型の引数をfloat型に変換した数を戻り値にする関数と、
#その関数を使用した際に発生した例外処理

def con(a):
    try:
        return float(a)
    except ValueError:
        print("数字ではないので処理を中止します")

f = con("55.0")
print(f)

#関数名: float
#引数名: a : データ型: str 
#戻り値: 引数をfloat型に変換した値
#関数floatに値を指定し、その結果を変数fに代入

