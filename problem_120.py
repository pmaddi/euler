"""
(a - 1) ** 2
a^2 - 2a + 1

(a + 1) ** 2
a^2 + 2a + 1




(a - 1) ** 3
(a^2 - 2a + 1) * (a - 1)
a^3 -2a^2 + a - a^2 + 2a - 1
a^3 - 3a^2 + 3a

(a + 1) ** 2
a^2 + 2a + 1


Nice solution I wish I came up with:
print(sum(a * (a - 2 + a % 2) for a in range(3, 1001)))

"""

if __name__ == '__main__':
    sm = 0
    for a in range(3, 1001):
        max_r = 0
        for n in range(1, 2 * a + 2):
            v = (a - 1) ** n + (a + 1) ** n
            r = v % (a ** 2)
            max_r = max(r, max_r)
        print(a, max_r)
        sm += max_r
    print(sm)
