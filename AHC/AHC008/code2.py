import sys
import random
n = int(input())
pet_list = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
human_list = [tuple(map(int, input().split())) for _ in range(m)]


dic = {
0:"u",
1:"d",
2:"l",
3:"r",
4:".",
5:"U",
6:"D",
7:"L",
8:"R"
}
act = {
"U":(-1,0),
"D":(1,0),
"L":(0,-1),
"R":(0,1),
".":(0,0)
}
# print(human_list)
# sys.stdout = open('out2.txt', 'w')
for k in range(300):
    L = []
    # print(human_list)
    for i in range(m):
        L.append(".")
    print("".join(L))

sys.stdout.flush()

pet_actions = list(input())
# sys.stdout = sys.__stdout__
