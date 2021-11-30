h, w, c = map(int, input().split())
lst = []
for _ in range(h):
    L = [*map(int, input().split())]
    lst.append(L)

mn = float("inf")
# DPらしい
for i in range(h):
    for j in range(w):
        mn = min(lst[])
