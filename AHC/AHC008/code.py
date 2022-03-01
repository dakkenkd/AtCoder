

"""
やりたいこと：ペットをできるだけ入っていないスペースを確保する
----------------------- 基本行動 ---------------------
隣接する通行可能マスの中から一様ランダムに選んだマスへ移動する。
-----------------------------------------------------
牛：基本行動を1回行う

豚：基本行動を2回行う

兎：基本行動を3回行う

犬：
1.目的の人がいる場合
    ・「目的の人」を選んでその人のいるマスに対して最短距離が短くなる方向に１マス進む
    ・その後、基本行動を行う
2.目的の人がいない場合
    ・現在地から到達可能なマス内にいる人の中からランダムに目的の人を選ぶ
3.到達可能なマス内に人がいない場合
    ・基本行動を2回行う

目的の人と同じマスに到達した場合、目的なしの状態にする

猫：
犬の目的の人が目的地になったバージョン

--------------------------------------------------------------------



"""
import sys
import random
n = int(input())
pet_list = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
human_list = [tuple(map(int, input().split())) for _ in range(m)]

pet = {
1:"cow",2:"pig",3:"rabbit",4:"dog",5:"cat"
}
dic = {
0:"u",1:"d",2:"l",3:"r",4:".",5:"U",6:"D",7:"L",8:"R"
}
act = {
"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1),".":(0,0)
}

def main(txt_output=False):
    if txt_output:
        sys.stdout = open('out.txt', 'w')
    solve()
    sys.stdout.flush()
    pet_actions = list(input())
    if txt_output:
        sys.stdout = sys.__stdout__

def check_crd(x,y):
    return x < 0 or y < 0 or x >= 30 or y >= 30

def solve():
    for k in range(300):
        L = []
        # print(human_list)
        for i in range(m):
            xx, yy = human_list[i]
            xx -= 1; yy -= 1;
            while True:
                p = random.randrange(4,9)
                a = dic[p]
                xn, yn = xx+act[a][0], yy+act[a][1]
                if check_crd(xn, yn):
                    continue
                else:
                    L.append(a)
                    human_list[i] = (xn+1,yn+1)
                    break
        print("".join(L))
