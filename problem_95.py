'''Could be made faster by caching the chain length'''


class SumHolder:
    def __init__(self, size):
        self._l = [0] * size

    def get(self, n):
        return self._l[n - 1]

    def set(self, n, val):
        self._l[n - 1] = val


if __name__ == '__main__':
    max_val = 10**6
    divisor_sum = SumHolder(max_val)
    for n in range(1, max_val + 1):
        for mul in range(2, (max_val // n) + 1):
            prod = n * mul
            divisor_sum.set(prod, divisor_sum.get(prod) + n)
    msf_val = 0
    msf = 0
    for n in range(1, max_val + 1):
        cur = n
        chain_length = 0
        seen = set()
        while True:
            if cur > max_val or cur < 1:
                chain_length = -1
                break
            seen.add(cur)
            nxt = divisor_sum.get(cur)
            chain_length += 1
            if nxt == n:
                break
            elif nxt in seen:
                # Does not cycle to origin
                chain_length = -1
                break
            cur = nxt
        if chain_length > msf_val:
            msf = n
            msf_val = chain_length
    print(msf)
