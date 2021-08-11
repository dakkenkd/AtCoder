import math
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
  E = int(input())
  
  # 角度を計算（度数方 → 弧度法）
  deg = 360 * E / T
  rad = math.radians(deg)
  
  # 観覧車の座標を計算
  y = - L * math.sin(rad) / 2 
  z = L/2 - L * math.cos(rad)/2
  
  # chokudai像との距離を計算
  a = (X**2 + (y-Y)**2) ** 0.5
  b = z
  
  if b == 0: # zero division error を避ける
    print(0)
  else:
    print(math.degrees(math.atan2(b,a)))
