s1 = input()
s2 = input()
s3 = input()
ss = set([s1, s2, s3])
s = ["AGC", "ABC", "ARC", "AHC"]

for d in s:
  if d not in ss:
    print(d)
    exit()