# 内積
def dot(a, b):
    x1, y1 = a
    x2, y2 = b
    return x1*x2 + y1*y2

# ノルム
def norm(a):
    x, y = a
    return x**2 + y**2


def add(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1+x2, y1+y2)

# ベクトルAB
def sub(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1-x2, y1-y2)

#
def mul(a, b):
    x1, y1 = a
    if not isinstance(b, tuple):
        return (x1*b, y1*b)
    x2, y2 = b
    return (x1*x2, y1*y2)

# 線分segに対する点pの射影
def project(seg, p):
    p1, p2 = seg
    base = sub(p2, p1)
    r = dot(sub(p, p1), base) / norm(base)
    return add(p1, mul(base, r))
