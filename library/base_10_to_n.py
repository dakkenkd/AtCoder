# 10進数からN進数に変換
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n) + str(X%n)
    return str(X%n)

# 最悪計算量は、N進数に直した時の桁数