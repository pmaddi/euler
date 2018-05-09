'''
a^2 + b^2 - c^2 = 0
a + b + c       = p

c = p - a - b

a^2 + b^2 - (p - a - b)^2 = 0

a^2 + b^2 - (p^2 -pa - pb -pa +a^2 +ab -pb +ab +b^2) = 0
a^2 + b^2 - p^2 + pa + pb + pa - a^2 - ab + pb - ab - b^2 = 0
a^2 - a^2 + b^2 - b^2 - p^2 + pa + pa + pb + pb - ab - ab = 0
0 + 0 - p^2 + 2pa + 2pb - 2ab = 0
-p^2 + 2pa + (2p - 2a)b = 0

b = (p^2 - 2pa)/(2p - 2a)

'''

if __name__ == '__main__':
    msf = 0
    pmax = 0
    for p in range(1, 1000):
        seen = set()
        for a in range(1, 1000):
            if (2*p - 2*a) == 0:
                continue
            b = (p**2 - 2*p*a)/(2*p - 2*a)
            c = p-a-b
            if int(b) == b and int(c) == c and b > 0 and b < p and c > 0 and c < p  and a+b+c==p and a**2+b**2==c**2:
                sltn = tuple(sorted([a,b,c]))
                seen.add(sltn)
        if len(seen) > msf:
            msf = len(seen)
            pmax = p
    print(pmax)
