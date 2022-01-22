a, b = map(int, input().split())
num = a
for i in range(a+1,b+1):
    num ^= i
    print(num > 1 & 1)
