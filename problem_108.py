"""
1/a + 1/b = 1/n
1 + a/b = a/n
b + a = ab/n
bn + an = ab
(a + b)n = ab

Naiieve: Grid search through a and b, adding to buckets of n if they fall in.

What is the least value of n for which the number of distinct solutions exceeds
one-thousand?
"""

if __name__ == '__main__':
    MAX = 1000
    TRESH = 100
    cnts = {}
    for a in range(1, MAX):
        for b in range(a, MAX):
            prod = a * b
            sm = a + b
            if prod % sm != 0:
                continue
            dv = prod // sm
            cnts[dv] = cnts.get(dv, 0) + 1
    for idx, cnt in sorted(cnts.items(), key=lambda x: x[0]):
        if cnt > TRESH:
            print(idx)
    print(cnts)
