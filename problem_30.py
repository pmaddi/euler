import math


def digit_equal_power_sum(power):
    i = 2
    out = 0
    while True:
        c = 0
        for p in range(int(math.log10(i) + 1)):
            d = (i // (10 ** p)) % 10
            c += d ** power
        if c == i:
            out += c
            # print(c, out)
        if i > (int(math.log10(i)) + 1) * (9 ** power):
            return out
        i += 1


if __name__ == '__main__':
    assert(digit_equal_power_sum(4) == 19316)
    print(digit_equal_power_sum(5))
