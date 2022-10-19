from itertools import accumulate
L = []
with open("./D", mode="r", encoding='UTF-8') as f:
    for s_line in f:
        L.append([*map(int, s_line.split())])

def ncr(n, r, mod=998244353):
    ret = 1
    for i in range(1, r+1):
        ret = (ret * (n-i+1) * pow(i, mod-2, mod)) % mod
    return ret

def cut1(ss):
    lst = []
    buf = []
    for i in range(len(ss)):
        if len(buf) == 0:
            buf.append(ss[i])
        else:
            if buf[-1] > ss[i]:
                lst.append(buf)
                buf = [ss[i]]
            else:
                buf.append(ss[i])
    if len(buf) >= 1:
        lst.append(buf)
    return lst

def cut2(ss):
    lst = []
    buf = []
    for i in range(len(ss)):
        if len(buf) == 0:
            buf.append(ss[i])
        else:
            if buf[-1] < ss[i]:
                lst.append(buf)
                buf = [ss[i]]
            else:
                buf.append(ss[i])
    if len(buf) >= 1:
        lst.append(buf)
    return lst

def solve(n, k, s, t):
    dic = {d:i for i, d in enumerate(t)}
    dic2 = {i:d for i, d in enumerate(t)}
    ss = [dic[s[i]] for i in range(n)]
    lst1 = cut1(ss)
    lst2 = []
    for d in lst1:
        dd = []
        for x in d:
            dd.append(dic2[x])
        lst2.append(cut2(dd))
    lst = [len(d) for d in lst2]
    k -= len(lst1)-1
    dp = [[0]*(k+1) for _ in range(len(lst)+1)]

    for i in range(k+1):
        dp[0][i] = ncr(lst[0]-1,i)
    for i in range(len(lst)):
        acc = list(accumulate(dp[i]))
        for j in range(k):
            dp[i+1][j] += acc[k-1-j]
            dp[i+1][j] %= 998244353
    return sum(dp[len(lst)][:k+1]) % 998244353

ans = []
idx = 0

while True:
    n, k = L[idx][0], L[idx][1]
    if n == 0: break
    s = L[idx+1]
    t = L[idx+2]

    print(solve(n, k, s, t))

    idx += 3

with open("./D_out", mode='w') as f:
    f.write('\n'.join(ans))
