from math import sqrt


def is_prime(x):
    if x <= 1:
        return False
    if x % 2 == 0 and x > 2:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in range(10**10, 10**11):
        print(i, is_prime(i))
