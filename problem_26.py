def period(num, div):
    assert(div > num)
    idx = 0
    nums = {}
    while num != 0:
        num = num % div
        while num < div and num != 0:
            num = num * 10
            digit = num // div
            if nums.get(num) is not None:
                return idx - nums[num]
            nums[num] = idx
            idx += 1
    return 0

def test_period():
    assert(period(1, 2) == 0)
    assert(period(1, 3) == 1)
    assert(period(1, 7) == 6)
    assert(period(1, 8) == 0)
    assert(period(1, 10) == 0)

def longest_rep(fl):
    dg = int(num) % 10

def max_idx_period_under(n):
    mp = 0
    ix = 0
    for i in range(2, n):
        p = period(1, i)
        if  p > mp:
            mp = p
            ix = i
    return ix

if __name__ == '__main__':
    test_period()
    print(max_idx_period_under(1000))
