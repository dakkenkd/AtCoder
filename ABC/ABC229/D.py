# 参考コード https://atcoder.jp/contests/abc229/submissions/27563152
# .を１、Xを０に変換する
a = [1 if s == "." else 0 for s in input()]
k = int(input())
n = len(a)
ans = 0

# 尺取り法
r = 0
s = 0
# [l, r)
for l in range(n):
    # while の中でいけるか判断することでバグを発生させにくくする
    while r < n and s+a[r] <= k:
        s += a[r] # 進めるなら1を足す
        r += 1
    ans = max(ans, r-l)
    s -= a[l]
print(ans)
