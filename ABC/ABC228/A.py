s = input()
s2 = input()
n = len(s)
flag = True
flag2 = False

se = set()
se2 = set()
for i in range(len(s)):
    if s[i] == "#":
        se.add(i)
for i in range(len(s)):
    if s2[i] == "#":
        se2.add(i)
if se == se2:
    print("Yes")
    exit()

for i in range(n-1):
    if s[i] == "#" or s2[i] == "#":
        flag = False
    if flag: continue
    if flag2:
        if s[i] == "#" or s2[i] == "#":
            print("No")
            exit()
    if s[i] != s[i+1] and s2[i] != s2[i+1]:
        print("No")
        exit()
    if s[i] == "." and s2[i] == ".":
        print(i)
        flag2 = True
print("Yes")
