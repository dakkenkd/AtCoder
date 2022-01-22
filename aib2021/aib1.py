from functools import reduce
import math

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

print(my_gcd(27522, 639261, 75894))
