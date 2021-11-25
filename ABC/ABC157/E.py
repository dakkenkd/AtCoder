n = int(input())
s = list(input())
q = int(input())

num = 1 << (n-1).bit_length()
seg = [set()]* (num*2)

for i in range(n):
    seg[i+num] = set([s[i]])
for i in range(num-1, 0, -1):
    seg[i] = seg[2*i] | seg[2*i+1]

def update(k, x):
    k += num
    seg[k] = set([d])
    while k > 1:
        seg[k >> 1] = seg[k] | seg[k^1]
        k >>= 1

def query(l, r):
    l += num
    r += num
    ret = {}
    while l < r:
        if l & 1:
            ret |= seg[l]
            l += 1
        if r & 1:
            ret |= seg[r-1]
        l >>= 1
        r >>= 1
    return len(ret)

for _ in range(q):
    s = [*map(str, input().split())]
    if s[0] == "1":
        update(int(s[1])-1, s[2])
    else:
        if s[1] == s[2]:
            print(1)
            continue
        print(query(int(s[1])-1, int(s[2])-1))
