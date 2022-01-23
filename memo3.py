n, m = map(int, input().split())
lst = [*map(int, input().split())]

dic = []
acc = [lst[0]]
mod_lst = []
mod_dic = {}
for i in range(1,n):
    acc.append(acc[i-1]+lst[i])

for i in range(n):
    mod_lst.append(acc[i]%m)

ans = 0
for i in range(n):
    if (m-lst[i])%m in mod_dic:
        ans += mod_dic[(m-lst[i])%m]
    if mod_lst[i] not in mod_dic:
        mod_dic[mod_lst[i]] = 1
    else:
        mod_dic[mod_lst[i]] += 1
print(ans)
