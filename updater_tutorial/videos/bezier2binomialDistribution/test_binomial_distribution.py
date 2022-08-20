from manimlib import *

n = 1000
p = 0.6

m = int(n * p)

def get_probability(n, p, m):
    return choose(n, m) * (1 - p) ** (n - m) * p ** m

print(get_probability(n, p, m) * n)