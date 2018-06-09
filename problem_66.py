def issquare(x):
    if not float(x).is_integer():
        return False
    n = int(x ** 0.5)
    return n ** 2 == x

out = []
for d in range(2, 100):
    if issquare(d):
        out.append((d, -1))
        continue
    x = 2
    while True:
        v = (x ** 2 - 1) / d
        print(d, x, v)
        if issquare(v):
            out.append((d, x))
            break
        x += 1

print(out)
