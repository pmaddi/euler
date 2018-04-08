'''
-  1: 1
2:1, 2
- 3: 1,3
4: 1, 2, 4
5: 1, 5
- 6: 1,2,3,6 : 3*4/2 : 3 * 2
- 10: 1,2,5,10 : 4 * 5 / 2 :
- 15: 1,3,5,15: 5*6
- 21: 1,3,7,21: 6*7
- 28: 1,2,4,7,14,28 : 7*8 / 2 : 7 * 2 * 2 : 1, 2, 4, 14, 28
- 36: 8*9/2 = 2 2 3 3 = 1, 2, 3, 4, 6, 9, 12, 18, 36
    : 1 2 4 8
    : 1 3 9

1. get factors of n, n-1
2. get prods of each of factors across. include if divides s

s = n(n-1)/2
'''
def factors(n):
    out = set()
    for i in range(1, n + 1):
        if n % i == 0:
            out.add(i)
    return out

def test_factors():
    assert(factors(1) == {1})
    assert(factors(2) == {1, 2})
    assert(factors(4) == {1, 2, 4})
    assert(factors(28) == {1, 2, 4, 7, 14, 28})

def triangle_factor_count_from_leg(n):
    s = n * (n - 1) // 2
    n_factors = factors(n)
    n_m_one_factors = factors(n - 1)

    s_factors = set()
    for i in n_factors:
        for j in n_m_one_factors:
            k = i * j
            if k <= s and s % k == 0:
                s_factors.add(k)
    return len(s_factors)


def triangle_divisors_greater_than(divs):
    assert(divs > 0)
    n = 1
    s_div_count = 1
    while s_div_count <= divs:
        n += 1
        s_div_count = triangle_factor_count_from_leg(n)
    return n * (n - 1) // 2

def test_triangle_factor_count_from_leg():
    assert(triangle_factor_count_from_leg(3) == 2)
    assert(triangle_factor_count_from_leg(4) == 4)
    assert(triangle_factor_count_from_leg(8) == 6)

def test_triangle_divisors_greater_than():
    assert(triangle_divisors_greater_than(5) == 28)

if __name__ == '__main__':
    test_factors()
    test_triangle_factor_count_from_leg()
    test_triangle_divisors_greater_than()
    print(triangle_divisors_greater_than(500))

