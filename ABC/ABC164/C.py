 = int(input())
lst = []
for i in range(a):
    b = input()
    if not(b in lst):
        lst.append(b)
        
print(len(lst))