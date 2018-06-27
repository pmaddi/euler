import math
def digits(x):
    return int(math.log10(x)) + 1

if __name__ == '__main__':
    cnt = 0
    power = 1
    while True:
        base = 1
        while True:
            num = base ** power
            d = digits(num)
            if d == power:
                cnt += 1
            if d > power:
                break
            base += 1
        power += 1
        if power > 100:
            break
    print(cnt)
