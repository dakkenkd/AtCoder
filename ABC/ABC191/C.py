h, w = map(int, input().split())
lst = [list(input()) for _ in range(h)]
ans = 0
pre = 0
for i in range(1,h):
    cnt = 0
    flag = 1
    for j in range(w):
        if flag and lst[i-1][j] != lst[i][j]:
            cnt += 1
            flag = 0
        if flag == 0  and lst[i-1][j] == lst[i][j]:
            cnt += 1
            flag = 1

    ans += cnt

print(ans)
