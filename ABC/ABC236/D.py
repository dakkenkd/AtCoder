n = int(input())
lst = []
for i in range(2*n-1):
    L = [*map(int, input().split())]
    lst.append([-1]*(i+1) + L)

done = {}
xor_dic = {}
ans = []
def dfs(num, s, xor):
    if len(s) == 0:
        ans.append(xor)
    for pair in sorted(s):
        s.remove(pair)
        xor ^= lst[num][pair]
        dfs(min(s), s, xor)
        s.add(pair)
        xor ^= lst[num][pair]

dfs(0,{i for i in range(1,2*n)}, 0)

print(max(ans))
