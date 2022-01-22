n, k = map(int, input().split())
lst = list(input())

def is_ok(x): # x人連続した区間をK回以内の操作で作ることができるか
    cnt = 0
    flag = True
    # 初期値の設定
    for i in range(x):
        if flag == True and lst[i] == "0":
            cnt += 1
            flag = False
        if flag == False and lst[i] == "1":
            flag = True

    mn = cnt
    # １マスずつずらしていく
    for i in range(x,n):
        if lst[i-x] == "0" and lst[i-x+1] == "1":
            cnt -= 1
        if lst[i-1] == "1" and lst[i] == "0":
            cnt += 1
        mn = min(cnt, mn)

    return mn <= k

l, r = 0, 1000000

while r-l > 1:
    mid = (r+l) // 2
    if is_ok(mid):
        l = mid
    else:
        r = mid

print(l)
