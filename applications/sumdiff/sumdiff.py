"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import time
# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

t1 = time.time()

cache_f = {}
cache_plus = {}
cache_minus = {}
outputs_plus = {}
outputs_minus = {}
output = []

for num in q:
    cache_f[num] = f(num)

for a in q:
    for b in q:
        cache_plus[(a, b)] = cache_f[a] + cache_f[b]

for c in q:
    for d in q:
        cache_minus[(c, d)] = cache_f[c] - cache_f[d]

cache_plus = list(cache_plus.items())
cache_minus = list(cache_minus.items())

for item in cache_plus:
    if item[1] not in outputs_plus:
        outputs_plus[item[1]] = []
    outputs_plus[item[1]].append(item[0])

for item in cache_minus:
    if item[1] not in outputs_minus:
        outputs_minus[item[1]] = []
    outputs_minus[item[1]].append(item[0])

outputs_plus_list = list(outputs_plus.items())

for item in outputs_plus_list:
    if item[0] in outputs_minus:
        for tup_plus in item[1]:
            for tup_minus in outputs_minus[item[0]]:
                a = f"f({tup_plus[0]}) +"
                b = f"f({tup_plus[1]}) ="
                c = f"f({tup_minus[0]}) -"
                d = f"f({tup_minus[1]}) ="
                end = f"{item[0]}"
                output.append(f"{a} {b} {c} {d} {end}")

t2 = time.time() - t1

print(f"q = {q}\n\nCombinations: {len(output)}\nTime: {t2}")
# for each in output:
#     print(each)