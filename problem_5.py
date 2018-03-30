def factorization(n):
    if n in [1,2,3,5,7,11]:
        return [n]
    for i in range(2, n):
       if n % i == 0:
            return sorted(factorization(i) + factorization(int(n / i)))
    return [n]

def aggregate(lst):
    out = {}
    for i in lst:
        out[i] = out.get(i, 0) + 1
    return out

def add_to(outer, inner):
    for i in inner.keys():
        outer[i] = max(outer.get(i, 0), inner[i])

def mult(agged):
    out = 1
    for i, j in agged.items():
        out = out * (i ** j)
    return out

def lcm(vals):
    agg_lcm = {1:1}
    for i in vals:
        add_to(agg_lcm, aggregate(factorization(i)))
    return mult(agg_lcm)

assert(lcm(range(1, 11))==2520)
print(lcm(range(1, 21)))
