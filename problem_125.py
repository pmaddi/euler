def sqsum(n):
    if n < 1:
        return 0
    return (2 * n + 1) * n * (n +  1) // 6

def ans(m):
    max_base = round(m ** .5)
    seen = set()
    for i in range(1, max_base + 1):
        for j in range(i + 1, max_base + 1):
            sm = sqsum(j) - sqsum(i - 1)
            if sm >= m:
                continue
            if sm != int(''.join(list(reversed(list(str(sm)))))):
                continue
            seen.add(sm)
    return sum(seen)

if __name__ == '__main__':
    assert ans(1000) == 4164
    print(ans(10**8))
