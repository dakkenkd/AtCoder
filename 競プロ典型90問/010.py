n = int(input())
a_lst = [0] * n
b_lst = [0] * n
ruiseki_a = {i:0 for i in range(1,n+1)}
ruiseki_b = {i:0 for i in range(1,n+1)}
ra = 0
rb = 0
# 入力を受け取る
for i in range(1,n+1):
  c,p = map(int, input().split())
  if c == 1:
    a_lst[i-1] = p
  else:
    b_lst[i-1] = p

# 累積和の計算
for k in ruiseki_a.keys():
  ra += a_lst[k-1]
  ruiseki_a[k] += ra
for k in ruiseki_a.keys():
  rb += b_lst[k-1]
  ruiseki_b[k] += rb

# クエリ処理
q = int(input())

for i in range(q):
  L,R = map(int, input().split())
  # Aクラスの計算
  if R == 1 or L == 1:
    ans_a = ruiseki_a[R]
  else:
    ans_a = ruiseki_a[R] - ruiseki_a[L-1]
  
  # Bクラスの計算
  if R == 1 or L == 1:
    ans_b = ruiseki_b[R]
  else:
    ans_b = ruiseki_b[R] - ruiseki_b[L-1]

  print(ans_a, ans_b)