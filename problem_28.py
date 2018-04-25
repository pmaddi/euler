'''
Theres a straightforward closed form too. Oh well
'''
def f(n):
    '''n is the edge length'''
    if n == 1:
        return 1
    if n < 1:
        return 0
    outside = 4 * (n ** 2)  - 6 * (n - 1)
    return outside  + f(n - 2)

def test_f():
    assert(f(5) == 101)

if __name__ == '__main__':
    test_f()
    print(f(1001))
