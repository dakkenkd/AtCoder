n = int(input())
L = int(len(str(n)))

ans = 0

for i in range(1,L):
    ans += i
    cnt = 0
    for j in range(i-1,0,-1):
        ans += j * 9 * 10**cnt
        cnt += 1

for i in range(L):
    left = int("1"*(L-i) + "0"*i)
    right = int("1"*(L-i) + "9"*i)
    print(left, n, right)
    if n > right:
        ans += right - left + 1
    elif n >= left:
        ans += n - left + 1

print(ans)
