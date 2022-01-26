from collections import Counter
n = int(input())
lst = [*map(int, input().split())]
plus_dic = {i: i+1+d for i, d in enumerate(lst)}
minus_dic = {i: i+1-d for i, d in enumerate(lst)}

cnt_dic = Counter(plus_dic.values())
ans = 0
for k in sorted(minus_dic, reverse=True):
    left = minus_dic[k]
    cnt_dic[plus_dic[k]] -= 1
    ans += cnt_dic[left]
print(ans)
