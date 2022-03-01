n, k = map(int, input().split())
lst = [*map(int, input().split())]

dic = {0:1}
acc = 0
for i in range(n):
    x = lst[i]
    acc += x
    if acc - k  in dic:
        ans += dic[acc-k]
    if acc in dic:
        dic[acc] += 1
    else:
        dic[acc] = 1

print(ans)
