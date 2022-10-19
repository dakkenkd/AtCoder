lst = []

with open("./J", mode="r", encoding='UTF-8') as f:
    for s_line in f:
        lst.append([*map(int, s_line.split())])

ans = []
idx = 0

with open("./J_ans", mode='w') as f:
    f.write('\n'.join(ans))
