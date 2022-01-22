from collections import deque
a, b = map(str, input().split())

lst = deque()
b = list(reversed(b))
for i in range(len(a)):
    if a[i] == "1":
        lst.append(i+1)

ans = 0
for i in range(len(b)):
    if b[i] == "R":
        ans = max(ans, i+lst.pop())
    else:
        ans = max(ans, i+lst.popleft())

print(ans)

# a, b = map(str, input().split())
# from collections import deque
# lst = deque()
# for i in range(len(a)):
#     if a[i] == "1":
#         lst.append(i+1)
# ans = 0
# for i in range(len(b)):
#     if b[i] == "R":
#         ans = max(ans, i+lst.popleft())
#     else:
#         ans = max(ans, i+lst.pop())
# print(ans)
