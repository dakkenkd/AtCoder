cell = 1
death = 0
lst = [0,0]
lst = lst + [i for i in range(1,25)]
print(lst)
for i in range(24):
    cell *= 2
    cell -= lst[i]
    print(cell)
