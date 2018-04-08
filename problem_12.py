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

1. prime factorization of n and n-1
2. prime factorization of s
3. prime fractorization to factor count
    - powerset size thing

s = n(n-1)/2
'''
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
