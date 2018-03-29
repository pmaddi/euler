def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_largest_pal_between(rng):
    largest = 0
    for i in rng:
        for j in rng:
            prod = i * j
            if is_palindrome(prod):
                if prod > largest:
                    largest = prod
    return largest

print(find_largest_pal_between(range(0, 100)))
print(find_largest_pal_between(range(100, 1000)))
