a,b,c,d=map(int,input().split())
 
x = c/b
y = a/d
 
if x > int(x):
    x+=1
    x=int(x)
if y > int(y):
    y+=1
    y=int(y)

if x <= y:
    print("Yes")
else:
    print("No")