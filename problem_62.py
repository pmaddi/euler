i = 1
dt = {}
dt_v = {}
while True:
    p = i ** 3
    key = ''.join(sorted(list(str(p))))
    n = dt.get(key, 0)
    v = dt_v.get(key, [])
    dt[key] = n + 1
    dt_v[key] = v + [p]
    if dt[key] == 5:
        print(min(dt_v[key]))
        break
    i += 1


