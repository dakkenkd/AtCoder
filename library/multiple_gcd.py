# 複数の数値に対しての最大公約数を求める

from functools import reduce
import math

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

