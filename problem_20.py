def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
def digitsum(n):
    return sum([int(i) for i in str(n)])
if __name__ == '__main__':
    print(digitsum(fact(100)))
