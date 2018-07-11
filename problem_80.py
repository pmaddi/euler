'''
Violates the spirit of the problem. Thanks python for being the best
'''
import decimal

if __name__ == '__main__':
    decimal.getcontext().prec = 110
    out = 0
    for i in range(2, 100):
        if int(i ** .5) ** 2 == i:
            continue
        d = decimal.Decimal(i) ** decimal.Decimal(.5)
        val = str(d).replace('.', '')[:100]
        v = sum([int(i) for i in list(val)])
        out += v
    print(out)
