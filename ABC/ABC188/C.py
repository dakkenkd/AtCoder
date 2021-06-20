N=int(input())
A=list(map(int,input().split()))
B=A[0:2**(N-1)]
C=A[2**(N-1):2**N]
num1=max(B)
ans1=A.index(num1)
num2=max(C)
ans2=A.index(num2)
if num1<num2:
  print(ans1+1)
else:
  print(ans2+1)
  
  