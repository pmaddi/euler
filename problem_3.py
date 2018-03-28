def factorization(n):
    if n in [1,2,3,5,7,11]:
        return [n]
    for i in range(2, int(n**.5)):
        if n % i == 0:
            return sorted(factorization(i) + factorization(n / i))
    return [n]
if __name__ == '__main__':
    # Exploration
    print(max(factorization(600851475143)))
    assert(set(factorization(13195)) == {5, 7, 13, 29})
    assert(factorization(13) == [13])
    assert(factorization(10) == [2,5])
    assert(factorization(1) == [1])
    print(600851475143 ** .5)
