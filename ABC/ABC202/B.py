s = input()
ans = ""
for d in s:
  if d == "6":
    ans = "9" + ans
  elif d == "9":
    ans = "6" + ans
  else:
    ans = d + ans
print(ans)