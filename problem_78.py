
# V1: Works in 20 mins.

N = 10**5

def ways(vals):
    vals = sorted(list(set(vals)))
    lst = [0 for i in range(N)]
    lst[0] = 1
    for v in vals:
        for i in range(v, N):
            lst[i] += lst[i - v]
    return lst

def main():
    w = ways(range(1, N + 1))
    for idx, v in enumerate(w):
        if v % 10**6 == 0:
            print(idx)
if __name__ == '__main__':
    assert(ways([1,2,3,4,5])[5] == 7)
    main()

'''
# V2: Dumb
from sympy import npartitions

if __name__ == '__main__':
    i = 1
    while True:
        if not npartitions(i) % 10**6:
            print(i)
        i += 1
'''
'''
# Stole euler generating function recurrence http://mathworld.wolfram.com/PartitionFunctionP.html
N = 10
cache = [0] * N
cache[0] = 1

for i in range(1, N):
    st = 0
    for k in range(1, i + 1):
        v1 = int(i - .5 * k * (3 * k - 1))
        v2 = int(i - .5 * k * (3 * k + 1))
        if min(v1, v2) < 0:
            break
        if max(v1, v2) > N:
            break
        st += (-1) ** (k+1) * (cache[v1] + cache[v2])
    cache[i] = st
print(cache)
'''
