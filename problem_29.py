'''
I tried to be clever to avoid using big ints
'''
def t_sorted(*args):
    return tuple(sorted(*args))

def factorization(n):
    if n in {1,2,3,5,7,11}:
        return (n,)
    for i in range(2, n):
       if n % i == 0:
            return t_sorted(factorization(i) + factorization(int(n / i)))
    return (n,)

def factorization_times(a, b):
    fac = factorization(a)
    out = ()
    for i in range(b):
        out = t_sorted(out + fac)
    return out

def all_fact_count(rng):
    facs = set()
    for a in rng:
        for b in rng:
            fac_tpl = factorization_times(a, b)
            if fac_tpl not in facs:
                facs.add(fac_tpl)
    return len(facs)

def all_fac_count_until(n):
    return all_fact_count(range(2, n + 1))

def test_all_fac_count_until():
    assert(all_fac_count_until(5) == 15)

if __name__ == '__main__':
    test_all_fac_count_until()
    print(all_fac_count_until(100))






