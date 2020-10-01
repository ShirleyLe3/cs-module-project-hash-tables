# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

lookup = dict()
for x in range(2, 14):
    for y in range(3, 6):
        lookup[(x, y)] = slowfun_too_slow(x, y)
        print(lookup[(x, y)], 'x: ', x, 'y: ', y)

def slowfun(x, y):
    if (x, y) not in lookup:
        lookup[(x, y)] = slowfun_too_slow(x, y)
    return lookup[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
