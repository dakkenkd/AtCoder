import math
a,b,c = map(int, input().split())
GCD1 = math.gcd(a,b)
GCD = math.gcd(GCD1, c)

print(a//GCD + b//GCD + c//GCD -3)