L,R = map(int, input().split())

# エラトステネスの篩で同じ素因数を２つ以上持つ数を判定する
cnt = [0]*1048576
for i in range(2,R+1):
    if cnt[i] != 0:
        continue
    k = i
    while k <=R:
        cnt[k] += 1
        k += i
    k = i**2
    while k <= R:
        cnt[k] -= 1000000007
        k += i**2
#print(cnt[:R])
ans = 0
for i in range(2,R+1):
    # x/gが１となるものを除く
    if L <= i <= R:
        ans -= int(R/i) - 1
    # 同じ素因数を２つ以上持っているとスキップ
    if cnt[i] < 0:
        continue
    # 包除原理で足すか引くか判断
    cc = int(R/i) - int((L-1)/i)
    if cnt[i]%2:
        #print(cc)
        #print("ans +=",cc*(cc-1)//2)
        ans += cc*(cc-1)//2
    else:
        #print(cc)
        #print("ans -=",cc*(cc-1)//2)
        ans -= cc*(cc-1)//2
# 最後に２倍して出力
print(ans*2)