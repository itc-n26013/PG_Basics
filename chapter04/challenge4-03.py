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
