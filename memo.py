a,b,c,x = map(int, input().split())
if x <= a:
    print(1)
elif a+1 <= x <= b:
    print(1/(b-(a+1)+1))
else:
    print(0)
