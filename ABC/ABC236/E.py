n = int(input())
lst = [*map(int, input().split())]

def is_ok_mean(x):
    use = 0
    nouse = 0
    L = [d-x for d in lst]
    for i in range(n):
        use, nouse = max(use, nouse) + L[i], use
    return max(use, nouse) >= 0

def is_ok_median(x):
    use = 0
    nouse = 0
    L = [[-1,1][d>=x] for d in lst]
    for i in range(n):
        use, nouse = max(use, nouse) + L[i], use
    return max(use, nouse) >= 0

def solve_mean():
    ng, ok = 0, 10**10
    for i in range(100):
        mid = (ng+ok)/2
        if is_ok_mean(mid):
            ng = mid
        else:
            ok = mid
    return ok

def solve_median():
    ng, ok = 0, 10**10
    while True:
        mid = (ng+ok)//2
        if is_ok_median(mid):
            ng = mid
        else:
            ok = mid
    return ok

print(solve_mean(), solve_median())
