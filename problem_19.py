'''
Fast enough, but better to increment by days in month rather than per day. Is
there a better constant time way for this?
'''
def leap(y):
    return (y % 4 == 0) and (not (y % 100 == 0 and not (y % 400 == 0)))

def test_leap():
    assert(leap(1900 == False))
    assert(leap(1904 == True))
    assert(leap(2000 == True))
    assert(leap(1901 == False))

def days_in_m(m, y):
    if m in [9, 4, 6, 11]:
        return 30
    elif m == 2:
        if leap(y):
            return 29
        else:
            return 28
    else:
        return 31

def p():
    d = 1
    m = 1
    y = 1900
    dy = 1
    ct = 0
    while not (d == 31 and m == 12 and y == 2000):
        if y >= 1901:
            if d == 1 and dy == 0:
                ct += 1
        dy += 1
        dy = dy % 7
        if d == 31 and m == 12:
            y += 1
            m = 1
            d = 1
        elif d == days_in_m(m, y):
            m += 1
            d = 1
        else:
            d += 1
    return ct
if __name__ == '__main__':
    test_leap()
    print(p())

