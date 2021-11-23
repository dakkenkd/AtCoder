q = int(input())
n = 2**20
lst = [ list(map(int, input().split())) for _ in range(q)]
num = 1 << (2**20-1).bit_length()
seg_tree = [-1] * (num * 2)
segfunc = min

def update(k, x):
    k += num
    seg_tree[k] = x
    while k > 1:
        seg_tree[k >> 1] = segfunc(seg_tree[k], seg_tree[k^1])
        k >>= 1

def find(idx, x):
    if seg_tree[idx + num] == -1:
        update(idx, x)
        return
    # -1になるまで登り続ける
    idx += num
    while True:
        if seg_tree[(idx + 1) >> 1] == -1:
            idx = (idx + 1) >> 1
            break
        idx = (idx + 1) >> 1
        if idx == 1:
            break
    
    # -1が来るまで下り続ける
    while idx * 2 < 2097152:
        if seg_tree[idx * 2] == -1:
            idx *= 2
        else:
            idx = idx*2 + 1
    update(idx-num, x)

for d in lst:
    t, x = d[0], d[1]
    if t == 1:
        if seg_tree[1] >= 0:
            continue
        else:
            find(x % n, x)
    else:
        print(seg_tree[x%n + num])