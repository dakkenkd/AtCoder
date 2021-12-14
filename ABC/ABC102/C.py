n = int(input())
lst = [int(x)-(i+1) for i,x in enumerate(input().split())]

lst.sort()
num = lst[len(lst)//2]

print(sum([abs(i - num) for i in lst]))
