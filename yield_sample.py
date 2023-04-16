# Description: ジェネレータのサンプル
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# ジェネレータオブジェクトを作成
# ジェネレータオブジェクトはイテレータの一種
fib_gen = fibonacci()


# 無限シーケンスから最初の10個の値を取得して表示
for i in range(10):
    print(next(fib_gen))
