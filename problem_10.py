from problem_8 import assertEqual
from problem_7 import next_prime

import logging

def primes_until(n):
    p_set = {2}
    nxt = next_prime(p_set)
    running_sum = sum(p_set)
    while nxt < n:
        if not len(p_set) % 100:
            logging.warning(nxt)
        p_set.add(nxt)
        running_sum += nxt
        nxt = next_prime(p_set)
    return p_set, running_sum

def sum_of_primes_until(n):
    return primes_until(n)[1]

def test_next_prime():
    assertEqual(next_prime({2, 3, 5}), 7)

def test_primes_lst_until():
    assertEqual(primes_until(10), ({2, 3, 5, 7}, 17))

def test_sum_of_primes_until():
    assertEqual(sum_of_primes_until(10), 17)

if __name__ == '__main__':
    test_next_prime()
    test_primes_lst_until()
    test_sum_of_primes_until()

    print(sum_of_primes_until(2000000))
