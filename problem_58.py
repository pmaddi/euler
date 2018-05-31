MAXVAL = 10**9
def isprime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def lt_ten_pct(pc):
    if not (pc[0] + pc[1]):
        return True
    if (pc[0] / sum(pc)) < .1:
        return False
    return True

def main():
    # p_set = primes_lt(MAXVAL)
    primecounts = [0, 0]
    c = 1
    i = 3
    while True:
        for j in range(4):
            # if c in p_set:
            if isprime(c):
                primecounts[0] += 1
            else:
                primecounts[1] += 1
            if i > 7:
                if sum(primecounts):
                    # print(primecounts, c)
                    if (primecounts[0] / sum(primecounts)) < .1:
                        # print(primecounts[0] / sum(primecounts), primecounts, c, j)
                        if j == 0:
                            return i - 2
                        return i
            c += (i - 1)
            assert(c < MAXVAL)
        i += 2
if __name__ == '__main__':
    print(main())
