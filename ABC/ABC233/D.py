from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right
n, k = map(int, input().split())
lst = [*map(int, input().split())]
acc = list(accumlate(lst)) # 累積和

for i in range(n):
    num = lst[i]
    if 
