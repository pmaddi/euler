PRIMES = {1}
def is_prime_relative(num, p_set):
    for p in p_set:
        if num % p == 0:
            return False
    return True

def next_prime(p_set):
    max_prime = max(p_set)
    candidate = max_prime + 1
    while not is_prime_relative(candidate, p_set):
        candidate += 1
    return candidate

assert(next_prime({2}) == 3)
assert(next_prime({2, 3}) == 5)

def nth_prime(n):
    p_set = {2}
    while len(p_set) < n:
        p_set.add(next_prime(p_set))
    return max(p_set)

assert(nth_prime(1) == 2)
assert(nth_prime(6) == 13)
print(nth_prime(10001))
