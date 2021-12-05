n = int(input())
lst = [*map(int, input().split())]
flower = [0] * n
ans = 0
flag = False
for i in range(max(lst)):
    flag = False
    for j in range(n):
        if lst[j] >= 1:
            flag = True
            lst[j] -= 1
        elif flag==True and lst[j] == 0:
            ans += 1
            flag = False
    if flag == True:
        ans += 1

print(ans)
