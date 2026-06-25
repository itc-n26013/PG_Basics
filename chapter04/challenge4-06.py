def add(x):
    return x ** 2
"""
関数名：add
因数名：ｘ　データ型：int
戻り値：xを２乗した値
"""

def parroting(a):
    print(a)
"""
関数名：add
引数名：a データ型：str
戻り値：aの値そのまま
備考：文字列をオウム返しにしてるからparrotingと名付けた
"""
sentence="こねここねたい"
parroting(sentence)


def add(a, b, c, x=3, y=5):
    return a+b+c*x*y
"""
関数名:add 
引数名: a : データ型: int : 必須引数 
引数名: b : データ型: int : 必須引数 
引数名: c : データ型: int : 必須引数 
引数名: x : データ型: int : オプション引数(未指定の場合3を代入) 
引数名: y : データ型: int : オプション引数(未指定の場合5を代入)
"""

result = add(10,15,25)
print(result)
~                                                                                             
def drive1(x):
    return x / 2
"""
関数名: drive1
引数名: x : データ型: int
戻り値: 引数を２で割った数
"""
def drive2(y):
   return  y * 4
"""
関数名: drive2
引数名: y : データ型: int
戻り値: 引数に４をかけた数
"""
a = drive1(10)
b = drive2(a)
print(b)
"""
関数１に値を指定、その結果をaとする
関数２に変数aの値を指定、その結果をbとする
変数bの結果を表示
"""
~

def con(a):
    try:
        return float(a)
    except ValueError:
        print("数字ではないので処理を中止します")

f = con("55.0")
print(f)

"""
関数名: float
引数名: a : データ型: str 
戻り値: 引数をfloat型に変換した値
関数floatに値を指定し、その結果を変数fに代入
"""
