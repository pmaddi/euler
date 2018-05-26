import itertools
max(sum(int(k) for k in str(p))
    for p in (i ** j
                for i, j
                in itertools.product(range(1, 100), range(1, 100))))
