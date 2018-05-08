import math

def ndigits(n):
    return int(math.log10(n)) + 1

def concat(i, j):
    return int(str(i) + str(j))

def pandigital(n):
    return sorted(str(n)) == sorted(str(123456789))

def largest_nine_dig(integer):
    d = integer
    e = 1
    last_d = d
    while ndigits(d) < 9:
        e += 1
        last_d = d
        d = concat(d, e * integer)
    if pandigital(d):
        return d
    else:
        return 0

if __name__ == '__main__':
    assert(largest_nine_dig(192) == 192384576)
    assert(largest_nine_dig(9) == 918273645)
    print(max([largest_nine_dig(i) for i in range(1, 1000001)]))
