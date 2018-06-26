def farey_function(n, descending=False):
    """
    Wikipedia
    Print the nth Farey sequence, either ascending or descending.
    """
    out = 0
    a, b, c, d = 0, 1, 1, n
    if descending:
        a, c = 1, n-1
    # yield a,b

    while (c <= n and not descending) or (a > 0 and descending):
        rat = a/b
        if 1/3 < rat  and 1/2 > rat:
            out += 1
        if 1/2 < rat:
            return out
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        # yield a,b
if __name__ == '__main__':
    print(farey_function(12000))
