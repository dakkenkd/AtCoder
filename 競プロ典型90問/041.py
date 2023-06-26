def gcd(x, y):
    if x == 0:return y
    return gcd(y % x, x)

def cross(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def cw(p0, p1, p2):
    pa = (p1[0] - p0[0], p1[1] - p0[1])
    pb = (p2[0] - p0[0], p2[1] - p0[1])
    return cross(pa, pb) > 0
    



N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort()

convex_hull = []

for p in points:
    while len(convex_hull) >= 2 and cw(convex_hull[-1], convex_hull[-2], p):
        convex_hull.pop()
    convex_hull.append(p)
upper_size = len(convex_hull)

for p in points[-2::-1]:
    while len(convex_hull) > upper_size and cw(convex_hull[-1], convex_hull[-2], p) <= 0:
        convex_hull.pop()
    convex_hull.append(p)

convex_hull.pop()

n = len(convex_hull)
area2 = 0
inner = 0
outer = 0

for i in range(n):
    now = convex_hull[i]
    nxt = convex_hull[(i+1) % n]
    area2 += cross(now, nxt)
    outer += gcd(abs(now[0] - nxt[0]), abs(now[1] - nxt[1]))

inner = (area2 - outer + 2) // 2

print(inner + outer - N)
