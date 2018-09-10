import numpy as np

CEIL = 50 * 10 ** 6

class Primer:
    def __init__(self, maxval):
        self.maxval = maxval
        self.cache = None

    def get(self):
        if self.cache is None:
            self.calculate()
        return self.cache

    def calculate(self):
        n = self.maxval
        nums = np.zeros(n - 1)
        nums[0] = 1
        for i in range(2, int(n ** .5) + 1):
            for j in range(2, (n // i) + 1):
                if i * j < n:
                    nums[i * j - 1] = 1 # is nonprime
        primes = set()
        for i in range(len(nums)):
            if not nums[i]:
                primes.add(i + 1)
        self.cache = sorted(list(primes))

def powers_under(n, power, primer):
    out = []
    primes = primer.get()
    i = 0
    while True:
        val = primes[i] ** power
        if val >= n:
            break
        out.append(val)
        i += 1
    return out

def combine(n, v1, v2):
    st = set()
    for i1 in v1:
        for i2 in v2:
            sm = i1 + i2
            if sm >= n:
                break
            st.add(sm)
    return sorted(list(st))

def nums_below(n, powers):
    if not powers:
        return
    primer = Primer(n)
    vals = powers_under(n, powers[0], primer)
    if len(powers) == 1:
        return vals
    else:
        other_vals = nums_below(n, powers[1:])
        return combine(n, vals, other_vals)

def ways_below(n):
    return len(nums_below(n, [2, 3, 4]))

if __name__ == '__main__':
    print(ways_below(50))
    assert(ways_below(50) == 4)
    print(ways_below(CEIL))

