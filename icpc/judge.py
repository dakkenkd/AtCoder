lst1 = []
lst2 = []

with open("./A_out", mode="r", encoding='UTF-8') as f:
    for s_line in f:
        lst1.append(s_line)

with open("./A.answer", mode="r", encoding='UTF-8') as f:
    for s_line in f:
        lst2.append(s_line)

if lst1 == lst2:
    print("AC")
else:
    print("WA")
