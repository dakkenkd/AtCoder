# https://qiita.com/Kiri8128/items/2b0023bed9af642c751c
N = int(input())
X = [[] for i in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    X[x].append(y)
    X[y].append(x)

def EulerTour(n, X, i0):
    # Xは破壊してXとPができる
    P = [-1] * n
    Q = [~i0, i0]
    ct = -1
    ET = []
    ET1 = [0] * n
    ET2 = [0] * n
    DE = [0] * n
    de = -1
    while Q:
        i = Q.pop()
        if i < 0:
            # ↓ 戻りも数字を足す場合はこれを使う
            # ct += 1
            # ↓ 戻りもETに入れる場合はこれを使う
            # ET.append(P[~i])
            ET2[~i] = ct
            de -= 1
            continue
        if i >= 0:
            ET.append(i)
            ct += 1
            if ET1[i] == 0: ET1[i] = ct
            de += 1
            DE[i] = de
        for a in X[i][::-1]:
            if a != P[i]:
                P[a] = i
                for k in range(len(X[a])):
                    if X[a][k] == i:
                        del X[a][k]
                        break
                Q.append(~a)
                Q.append(a)
    return (ET, ET1, ET2)

ET, ET1, ET2 = EulerTour(N, X, 0)
print("ET =", ET) # Pathのi番目の頂点番号
print("ET1 =", ET1) # Start
print("ET2 =", ET2) # End
