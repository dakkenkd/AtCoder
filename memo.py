n = int(input())
L = int(str(n))

ans = 0

for i in range(L):
    left = int("1"*(L-i) + "0"*i)
    right = int("1"*(L-i) + "9"*i)
    if n > right:
        ans += right - left + 1
    elif n >= left:
        ans += n - left + 1

print(ans)
