def factor_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def triangles(div_cnt):
    step = 1
    num = 0
    divisors = 1
    count = 0
    while divisors <= div_cnt:
        num += step
        divisors = factor_count(num)
        step += 1
        count += 1
        if not count % 1000:
            print(divisors, num)
    return num

def test_factor_count():
    assert(factor_count(1) == 1)
    assert(factor_count(2) == 2)
    assert(factor_count(3) == 2)
    assert(factor_count(10) == 4)
    assert(factor_count(28) == 6)

def test_triangles():
    assert(triangles(3) == 6)
    assert(triangles(5) == 28)

if __name__ == '__main__':
    test_factor_count()
    test_triangles()
    print(triangles(500))
