from itertools import permutations
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
if __name__ == '__main__':
    msf = 0
    for x in range(2,10):
        for i in permutations(range(1, x)):
            v = (int(''.join((str(j) for j in i))))
            if prime(v):
                if v >= msf:
                    msf = v
    print(msf)
