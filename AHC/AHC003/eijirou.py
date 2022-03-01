"""
・考察
    ・同一直線上の辺の長さは近いことが多い。
        ・よって、最短経路は直線的な部分が多いと考えられる。
        ・D が大きいとき、この傾向が薄れる。
        ・M=2 のとき、この傾向は部分的にしか成立しない。
    ・1740本の辺の長さを、それぞれ独立に推定するのは難しい。
        ・変数が1740個あるので、方程式が最低でも1740個必要だが、クエリは全部で1000個しかないため。
        ・同一直線上の辺の長さを全て等しいとみなせば、変数を60個にできる。
            ・M=1 のとき、この方針で97%以上のスコアを出せる。
        ・M=2 のとき、変数を120個程度にしたい。
            ・分割する場所も変数と考えると、変数を180個にしたいという方が適切かもしれない。
    ・評価関数の最大値は、 k が増加するにつれ、指数関数的に増加する。
        ・95%以上のスコアが出るので、序盤もあまり犠牲にしたくない。

・方針
    ・基本的な方針は、辺の長さを推定するというものである。
        ・教師データを用いて、誤差を小さくするように辺の長さを調節する。
            ・使用した辺の本数を n 、誤差を Δb とすると、全ての使用した辺を Δb/n 程度短くする。
        ・序盤は同一直線上の辺の長さを共通にする。
        ・段々と直線を細かく分割し、同じグループの辺の長さを共通にする。
    ・途中で M=1 か M=2 かを推定する。
        ・直線を2分割した後、隣り合うグループの辺の長さが大きく異なるときは M=2 、そうでないときは M=1 と判断した。
        ・M の正答率は9割程度だったと思う。
        ・M=1 のとき、同一直線上の辺の長さを共通にする。
        ・M=2 のとき、さらに直線を細かく分割する。
    ・入出力のログをとって使い回す。
    ・学習率を減衰させる。
        ・あまり意味がないかもしれない。
    ・eを推定する。
        ・あまり意味がないかもしれない。

・おおまかな流れ
    ・初期状態において、全ての辺の長さを3000程度に設定する。
        ・序盤で多くの経路を試すため、短めに設定した。
    ・以下を1000回繰り返す。
        (0.直線の分割数を変更する。）
        1.頂点の入力を受け取る。
        2.最短経路をDijkstra法によって求める。
        3.最短経路を出力する。
        4.経路長の入力を受け取る。
        5.辺の長さを更新する。
        (6.ログを読み込んで辺の長さを更新する。)

・自作ビジュアライザ
    ・太いほど、実際の辺の長さが短い。
    ・左の図
        ・赤が濃いほど、実際の値よりも予測した辺の長さが短い。
        ・青が濃いほど、実際の値よりも予測した辺の長さが長い。
        ・黒に近いほど、予測と実際の長さが一致している。
    ・右の図
        ・緑が濃いほど、使われた回数が多い。
        ・黒が濃いほど、使われた回数が少ない。
"""

try:
    # local environment
    import matplotlib.pyplot as plt
    import cv2
    from PIL import Image, ImageDraw
    from os import makedirs
    from random import randrange, uniform
    tester = True
except:
    # online judge
    tester = False

from heapq import heappush, heappop
from sys import stdin
input = stdin.buffer.readline

size = 30
num_queries = 1000
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
inf = 1 << 30


def main(visualize=False, inputs=False):
    # test ##############################################################
    if tester:
        if inputs:
            real_h = [list(map(int, input().split())) for _ in range(size)]
            real_v = [list(map(int, input().split())) for _ in range(size-1)]
            st = [(0,0,0,0)] * num_queries
            a = [0] * num_queries
            real_e = [0.0] * num_queries
            for i in range(num_queries):
                stae = input().split()
                st[i] = tuple(map(int, stae[:4]))
                a[i] = int(stae[4])
                real_e[i] = float(stae[5])
        else:
            real_h, real_v, st, a, real_e = input_generator()
        scores = [0.0] * num_queries
    if visualize:
        makedirs('images', exist_ok=True)
        h_used = [[1] * (size-1) for _ in range(size)]
        v_used = [[1] * size for _ in range(size-1)]
    ###############################################################

    # hyper parameters
    unit = 30
    units = [3,  5,  6,  10, 15]
    steps = [900,720,540,360,180]
    initial_distance = 3000

    # initializer
    h = [[initial_distance] * (size//unit) for _ in range(size)]
    v = [[initial_distance] * size for _ in range(size//unit)]
    e = [1.0] * num_queries
    h_log = []
    v_log = []
    unit_log = []
    si_log = [0] * num_queries
    sj_log = [0] * num_queries
    ti_log = [0] * num_queries
    tj_log = [0] * num_queries
    output_log = [[] for _ in range(num_queries)]
    b_log = [0] * num_queries

    for k in range(num_queries):
        lr = lr_scheduler(k) # learning rate

        # update unit
        if steps and k == steps[-1]:
            if unit == 15:
                sum_differences = sum([abs(h[i][0]-h[i][1]) for i in range(size)]) + sum([abs(v[0][i]-v[1][i]) for i in range(size)])
                if sum_differences < 30000:
                    M = 1
                    units = [30]
                    steps = [k]
                    #print('M = 1, ', sum_differences)
                else:
                    M = 2
                    #print('M = 2, ', sum_differences)
            h_log.append(h)
            v_log.append(v)
            unit_log.append(unit)
            unit = units.pop()
            steps.pop()
            h = [[0] * (size//unit) for _ in range(size)]
            v = [[0] * size for _ in range(size//unit)]
            for old_idx in range(len(h_log)):
                old_h = h_log[old_idx]
                old_v = v_log[old_idx]
                old_unit = unit_log[old_idx]
                for _ in range(20):
                    for idx in range(k):
                        if 0.0 < update(old_h, old_v, si_log[idx], sj_log[idx], ti_log[idx], tj_log[idx], output_log[idx], round(b_log[idx]/e[idx]), old_unit, lr):
                            e[idx] = min(1.05, max(0.95, e[idx]+0.005))
                        else:
                            e[idx] = min(1.05, max(0.95, e[idx]-0.005))
                for i in range(size):
                    for j in range(size-1):
                        h[i][j//unit] += old_h[i][j//old_unit]
                        v[j//unit][i] += old_v[j//old_unit][i]
            for i in range(size):
                for j in range(size//unit):
                    if j == size//unit - 1:
                        h[i][j] //= (unit - 1) * len(h_log)
                        v[j][i] //= (unit - 1) * len(v_log)
                    else:
                        h[i][j] //= unit * len(h_log)
                        v[j][i] //= unit * len(v_log)

        # input
        # test ##############################################################
        if tester:
            si, sj, ti, tj = st[k]
        ###############################################################
        else:
            si, sj, ti, tj = map(int, input().split())

        # Dijkstra's algorithm
        cost, directions = dijkstra2(h, v, si, sj, ti, tj, unit)
        i = ti
        j = tj
        output = []
        while i != si or j != sj:
            direction = directions[i][j]
            output.append(direction)
            i -= dx[direction]
            j -= dy[direction]
        output.reverse()

        # output
        if not tester:
            print(*['UDLR'[direction] for direction in output], sep='', flush=True)

        # input
        # test ##############################################################
        if tester:
            b = calculate_length(real_h, real_v, si, sj, ti, tj, output)
            scores[k] = pow(0.998, 1000-(k+1))* a[k]/b
            b = round(b*real_e[k])
        ###############################################################
        else:
            b = int(input())

        # update edges
        si_log[k] = si
        sj_log[k] = sj
        ti_log[k] = ti
        tj_log[k] = tj
        output_log[k] = output
        b_log[k] = b
        update(h, v, si, sj, ti, tj, output, b, unit, lr)
        if k % 5 == 0:
            for idx in range(k):
                if 0.0 < update(h, v, si_log[idx], sj_log[idx], ti_log[idx], tj_log[idx], output_log[idx], round(b_log[idx]/e[idx]), unit, lr):
                    e[idx] = min(1.05, max(0.95, e[idx]+0.01))
                else:
                    e[idx] = min(1.05, max(0.95, e[idx]-0.01))

        # test ##############################################################
        if visualize:
            # update h_used, v_used
            i = si
            j = sj
            for direction in output:
                if direction < 2:
                    v_used[i+direction-1][j] += 1
                else:
                    h_used[i][j+direction-3] += 1
                i += dx[direction]
                j += dy[direction]
            # visualize edges
            if k % 10 == 0:
                h_new = [[0] * (size-1) for _ in range(size)]
                v_new = [[0] * size for _ in range(size-1)]
                for i in range(size):
                    for j in range(size-1):
                        h_new[i][j] = h[i][j//unit]
                        v_new[j][i] = v[j//unit][i]
                visualizer(real_h, real_v, h_new, v_new, h_used, v_used, k//10)
        ###############################################################

    # test ##############################################################
    if tester:
        #print([format(i, '.2f') for i in e])
        #print([format(i, '.2f') for i in real_e])
        if visualize:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            video = cv2.VideoWriter('video.mp4',fourcc, 10.0, (6000, 3000))
            for i in range(num_queries//10):
                img = cv2.imread('images/grid{}.jpg'.format(i))
                video.write(img)
            video.release()
            print("'video.mp4' was created.")
        return scores
    ###############################################################


def dijkstra(h, v, si, sj, ti, tj):
    costs = [[inf] * size for _ in range(size)]
    costs[si][sj] = 0
    heap = []
    heappush(heap, si<<5|sj)
    directions = [[-1] * size for _ in range(size)]
    while True:
        cost_i_j = heappop(heap)
        cost = cost_i_j >> 10
        i = (cost_i_j >> 5) % (1 << 5)
        j = cost_i_j % (1 << 5)
        if costs[i][j] < cost:
            continue
        if i == ti and j == tj:
            break
        if i:
            new_cost = cost + v[i-1][j]
            if new_cost < costs[i-1][j]:
                costs[i-1][j] = new_cost
                heappush(heap, new_cost<<10|i-1<<5|j)
                directions[i-1][j] = 0
        if i+1 < size:
            new_cost = cost + v[i][j]
            if new_cost < costs[i+1][j]:
                costs[i+1][j] = new_cost
                heappush(heap, new_cost<<10|i+1<<5|j)
                directions[i+1][j] = 1
        if j:
            new_cost = cost + h[i][j-1]
            if new_cost < costs[i][j-1]:
                costs[i][j-1] = new_cost
                heappush(heap, new_cost<<10|i<<5|j-1)
                directions[i][j-1] = 2
        if j+1 < size:
            new_cost = cost + h[i][j]
            if new_cost < costs[i][j+1]:
                costs[i][j+1] = new_cost
                heappush(heap, new_cost<<10|i<<5|j+1)
                directions[i][j+1] = 3
    return costs[ti][tj], directions


def dijkstra2(h, v, si, sj, ti, tj, unit):
    costs = [[inf] * size for _ in range(size)]
    costs[si][sj] = 0
    heap = []
    heappush(heap, si<<5|sj)
    directions = [[-1] * size for _ in range(size)]
    while True:
        cost_i_j = heappop(heap)
        cost = cost_i_j >> 10
        i = (cost_i_j >> 5) % (1 << 5)
        j = cost_i_j % (1 << 5)
        if costs[i][j] < cost:
            continue
        if i == ti and j == tj:
            break
        if i:
            new_cost = cost + v[(i-1)//unit][j]
            if new_cost < costs[i-1][j]:
                costs[i-1][j] = new_cost
                heappush(heap, new_cost<<10|i-1<<5|j)
                directions[i-1][j] = 0
        if i+1 < size:
            new_cost = cost + v[i//unit][j]
            if new_cost < costs[i+1][j]:
                costs[i+1][j] = new_cost
                heappush(heap, new_cost<<10|i+1<<5|j)
                directions[i+1][j] = 1
        if j:
            new_cost = cost + h[i][(j-1)//unit]
            if new_cost < costs[i][j-1]:
                costs[i][j-1] = new_cost
                heappush(heap, new_cost<<10|i<<5|j-1)
                directions[i][j-1] = 2
        if j+1 < size:
            new_cost = cost + h[i][j//unit]
            if new_cost < costs[i][j+1]:
                costs[i][j+1] = new_cost
                heappush(heap, new_cost<<10|i<<5|j+1)
                directions[i][j+1] = 3
    return costs[ti][tj], directions


def lr_scheduler(k, first_lr=1.0, last_lr=0.25):
    return (last_lr - first_lr) * k / num_queries + first_lr


def update(h, v, si, sj, ti, tj, output, b, unit, lr):
    delta = (b-calculate_length2(h,v,si,sj,ti,tj,output,unit)) // (len(output)*unit)
    delta = round(lr * delta)
    i = si
    j = sj
    for direction in output:
        if direction < 2:
            v[(i+direction-1)//unit][j] = min(9000, max(1000, v[(i+direction-1)//unit][j]+delta))
        else:
            h[i][(j+direction-3)//unit] = min(9000, max(1000, h[i][(j+direction-3)//unit]+delta))
        i += dx[direction]
        j += dy[direction]
    return round(delta / lr)


def calculate_length(h, v, si, sj, ti, tj, output):
    b = 0
    i = si
    j = sj
    for direction in output:
        if direction < 2:
            b += v[i+direction-1][j]
        else:
            b += h[i][j+direction-3]
        i += dx[direction]
        j += dy[direction]
    assert i == ti and j == tj
    return b


def calculate_length2(h, v, si, sj, ti, tj, output, unit):
    b = 0
    i = si
    j = sj
    for direction in output:
        if direction < 2:
            b += v[(i+direction-1)//unit][j]
        else:
            b += h[i][(j+direction-3)//unit]
        i += dx[direction]
        j += dy[direction]
    assert i == ti and j == tj
    return b


def input_generator():
    D = randrange(100, 2001)
    M = randrange(1, 3)
    H = [[randrange(1000+D, 9001-D) for p in range(M)] for i in range(30)]
    if M == 1:
        x = [[0, 29] for i in range(30)]
    else:
        x = [[0, randrange(1, 29), 29] for i in range(30)]
    h = [[0] * 29 for _ in range(30)]
    for i in range(30):
        for p in range(M):
            for j in range(x[i][p], x[i][p+1]):
                h[i][j] = H[i][p] + randrange(-D, D+1)
    V = [[randrange(1000+D, 9001-D) for p in range(M)] for j in range(30)]
    if M == 1:
        y = [[0, 29] for j in range(30)]
    else:
        y = [[0, randrange(1, 29), 29] for j in range(30)]
    v = [[0] * 30 for _ in range(29)]
    for j in range(30):
        for p in range(M):
            for i in range(y[j][p], y[j][p+1]):
                v[i][j] = V[j][p] + randrange(-D, D+1)
    st = [(0,0,0,0)] * 1000
    for k in range(1000):
        si, sj, ti, tj = [randrange(30) for _ in range(4)]
        while abs(si-ti) + abs(sj-tj) < 10:
            si, sj, ti, tj = [randrange(30) for _ in range(4)]
        st[k] = (si, sj, ti, tj)
    a = [0] * 1000
    for k in range(1000):
        si, sj, ti, tj = st[k]
        a[k] = dijkstra(h, v, si, sj, ti, tj)[0]
    e = [uniform(0.9, 1.1) for _ in range(1000)]
    return h, v, st, a, e


def visualizer(real_h, real_v, h, v, h_used, v_used, k):
    img = Image.new('RGB', (6000,3000), (255,255,255))
    draw = ImageDraw.Draw(img)
    x = 50
    y = 50
    for i in range(30):
        for j in range(29):
            draw.line(((100*i+x,100*j+y),(100*i+x,100*j+100+y)), fill=color(real_h[i][j], h[i][j]), width=(9000-real_h[i][j])//125)
    for i in range(29):
        for j in range(30):
            draw.line(((100*i+x,100*j+y),(100*i+100+x,100*j+y)), fill=color(real_v[i][j], v[i][j]), width=(9000-real_v[i][j])//125)
    x = 3050
    y = 50
    for i in range(30):
        for j in range(29):
            draw.line(((100*i+x,100*j+y),(100*i+x,100*j+100+y)), fill=color2(h_used[i][j]-1), width=(9000-real_h[i][j])//125)
    for i in range(29):
        for j in range(30):
            draw.line(((100*i+x,100*j+y),(100*i+100+x,100*j+y)), fill=color2(v_used[i][j]-1), width=(9000-real_v[i][j])//125)
    img.save('images/grid{}.jpg'.format(k))


def color(ans, pred):
    if ans < pred:
        blue = min(255, (pred-ans)*255//2500)
        return (0, 0, blue)
    else:
        red = min(255, (ans-pred)*255//2500)
        return (red, 0, 0)


def color2(used):
    return (0, min(255,16*used), 0)


def test_samples(n=100):
    average_score = [0.0] * num_queries
    for lap in range(n):
        scores = main()
        for k in range(num_queries):
            average_score[k] += scores[k]
        if lap % 10 == 9:
            print(lap+1, 2312311*sum(average_score)/10**7/(lap+1))
    for k in range(num_queries):
        average_score[k] /= n
    plot_scores(average_score)


def plot_scores(scores):
    print('score:', 2312311*sum(scores)/10**7)
    max_score = [pow(0.998, 1000-k-1) for k in range(num_queries)]
    ab = [0.0] * num_queries
    for k in range(num_queries):
        ab[k] = scores[k] / pow(0.998, 1000-k-1)
    plt.plot(range(num_queries), scores, label='score')
    plt.plot(range(num_queries), max_score, label='max score')
    plt.plot(range(num_queries), ab, label='a / b')
    plt.legend()
    plt.show()


if tester:
    scores = main(visualize=True)
    plot_scores(scores)
    test_samples(n=100)
else:
    main()
