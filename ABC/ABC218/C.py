# 回転行列
def rotate90(x,y):
    xx = -y
    yy = x
    return xx, yy

n = int(input())

s = []
t = []

# "#"のマスの座標だけ調べる
for i in range(n):
    for j, d in enumerate(list(input())):
        if d == "#":
            s.append((i,j))

for i in range(n):
    for j, d in enumerate(list(input())):
        if d == "#":
            t.append((i,j))


# そもそも#の数が違っていたら同じにならない
if len(s) != len(t):
    print("No")
    exit()

# 回転させて一致するかを調べる
for _ in range(4):
    # 相対的な位置が大事なので、「ソートして距離が同じ」であれば一致とみなす
    s.sort()
    t.sort()
    dist = set()
    for i in range(len(s)):
        x = s[i][0] - t[i][0]
        y = s[i][1] - t[i][1]
        dist.add((x,y))

    # 判定
    if len(dist) == 1:
        print("Yes")
        exit()

    # 回転
    for i in range(len(s)):
        x, y = s[i][0], s[i][1]
        x, y = rotate90(x,y)
        s[i] = (x,y)

print("No")
