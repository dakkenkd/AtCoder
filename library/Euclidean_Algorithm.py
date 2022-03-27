# Euclidean Algorithm
def gcd(a,b):
  r = a % b # a >=b としてあまりを求める
  return gcd(b, r) if r else b # rがゼロでないのならば、b と r のgcdを返し、rがゼロであればbが最大公約数になる

# Euclidean Algorithm (non-recursive)
def gcd2(a,b):
  while b:
    a, b = b, a%b
  return a

# Extended Euclidean Algorithm
def extgcd(a,b):
  if b:
    d, y, x = extgcd(b, a%b)
    y -= (a//b)*x
    return d, x, y
  return a, 1, 0

# lcm (least common multiple)
import math
def lcm(a,b):
  return a//math.gcd(a,b)*b
