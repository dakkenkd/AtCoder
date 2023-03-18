def solve():
    n = int(input())
    if n == 0:
        return -1
    lst = [int(input()) for _ in range(n)]
    lst.sort()
    return sum(lst[1:-1])//(n-2)

while True:
    ret = solve()
    if ret == -1: break
    print(ret)
