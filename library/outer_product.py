"""
3点のなす角が180度未満かどうかを判定する
P2-P1, P3-P1
反時計回りの順番に点の座標を入力する
"""
def outer_product(p2, p1, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    xa, ya = x3-x1, y3-y1
    xb, yb = x2-x1, y2-y1
    if xa*yb - ya*xb <= 0:
        return False
    else:
        return True
