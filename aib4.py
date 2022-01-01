s = input()
s = s[:-1]
plus = list(s.split("+"))
lst = [ list(map(int, d.split("-"))) for d in plus ]
ans = 0
for d in lst:
    if len(d) == 1:
        ans += d[0]
    else:
        ans += d[0] - sum(d[1:])
print(ans)
