def primes_lt(n):
    '''too slow'''
    out = []
    for i in range(2, n):
        prime = True
        for d in out:
            if i % d == 0:
                prime = False
                break
        if prime:
            out.append(i)
        if len(out) % 100 == 0:
            print(len(out), max(out))
    return out

if __name__ == '__main__':
    pass


