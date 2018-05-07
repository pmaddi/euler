def prime(n):
    """Returns True if n is prime."""
    if n < 2:
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

def fn():
    lr = {2, 3, 5, 7}
    rl = {2, 3, 5, 7}
    ct = 0
    count = 0
    while ct != 11:
        n_lr = lr.copy()
        n_rl = rl.copy()
        for i in range(10):
            for v in lr:
                vl = int(''.join(str(i) + str(v)))
                if prime(vl):
                    n_lr.add(vl)
            for v in rl:
                vl = int(''.join(str(v) + str(i)))
                if prime(vl):
                    n_rl.add(vl)
        lr = n_lr
        rl = n_rl

        ct = len((lr & rl) - {2, 3, 5, 7})
        count = sum((lr & rl) - {2, 3, 5, 7})
    return count

if __name__ == '__main__':
    print(fn())
