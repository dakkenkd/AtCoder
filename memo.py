n, m  = map(int, input().split())
A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(m)]
ans = False
if n == m:
    for i in range(n):
        for j in range(n):
            flag = True
            if A[i][j] != B[i][j]:
                flag = False
    if flag:
        ans = True
else:
    for i in range(n-m):
        for j in range(n-m):
            flag = True
            for ii in range(i, i+m):
                for jj in range(j, j+m):
                    if A[ii][jj] != B[ii-i][jj-j]:
                        flag = False
            if flag:
                ans = True
if ans:
    print("Yes")
else:
    print("No")
