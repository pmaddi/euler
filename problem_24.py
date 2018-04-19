from math import factorial
def perms(N, rem):
    rem_idx = rem - 1
    remainingdigits = list(range(N))
    digits = []
    for i in range(N):
        idx = N - 1 - i
        f = factorial(idx)
        digit_idx = rem_idx // f
        dg = remainingdigits.pop(digit_idx)
        digits.append(str(dg))
        rem_idx = rem_idx % f
    return ''.join(digits)

if __name__ == '__main__':
    assert(perms(3, 4) == '120')
    print(perms(10, 10**6 - 1))
