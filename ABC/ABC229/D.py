# 参考コード https://atcoder.jp/contests/abc229/submissions/27563152
# .を１、Xを０に変換する
# a = [1 if s == "." else 0 for s in input()]
# k = int(input())
# n = len(a)
# ans = 0
#
# # 尺取り法
# r = 0
# s = 0
# # [l, r)
# for l in range(n):
#     # while の中でいけるか判断することでバグを発生させにくくする
#     while r < n and s+a[r] <= k:
#         s += a[r] # 進めるなら1を足す
#         r += 1
#     ans = max(ans, r-l)
#     s -= a[l]
# print(ans)

# 二分探索の解法

s = input()
k = int(input())
n = len(s)

R, RR = [], 0
for d in s:
    if d == ".":
        RR += 1
    R.append(RR)

def is_ok(x):
    if x > n: return False
    elif x == n: return R[x-1] <= k
    mn = R[x-1]
    for i in range(x,n):
        mn = min(R[i] - R[i-x], mn)
    return mn <= k

l, r = 0, 10**18

while r-l > 1:
    mid = (r+l) // 2
    if is_ok(mid):
        l = mid
    else:
        r = mid
print(l)
