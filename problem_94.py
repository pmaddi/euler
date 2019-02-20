# # Too slow
# from math import sqrt
#
# def area(a, b, c):
#     p = (a + b + c) * .5
#     return sqrt(p * (p - a) * (p - b) * (p - c))
#
# def test_area():
#     assert area(5, 5, 6) == 12
#
# def int_ish(f):
#     return f == int(f)
#
# def test_int_ish():
#     assert not int_ish(1.00001)
#     assert not int_ish(.9999)
#     assert int_ish(sqrt(4))
#     assert int_ish(sqrt(1234 ** 2))
#
# if __name__ == '__main__':
#     sm = 0
#     for dbl_side_length in range(2, 10 ** 9):
#         for other in (dbl_side_length - 1, dbl_side_length + 1):
#             p = dbl_side_length * 2 + other
#             if p > 10 ** 9:
#                 print(sm)
#                 exit()
#             a = area(dbl_side_length, dbl_side_length, other)
#             if int_ish(a):
#                 sm += p
#     print(sm)
'''
peremiter = 3s - 1 or 3s + 1

p = (3s - 1) * .5 or (3s + 1) * .5
area = sqrt(((3s - 1) * .5) * (((3s - 1) * .5) - s)**2 * (((3s - 1) * .5) - (s - 1)))

and find where the area value is an int?
is there a diophantine for this?
'''

from math import sqrt

def area(a, b, c):
    p = (a + b + c) * .5
    return sqrt(p * (p - a) * (p - b) * (p - c))

def test_area():
    assert area(5, 5, 6) == 12

def int_ish(f):
    return f == int(f)

def test_int_ish():
    assert not int_ish(1.00001)
    assert not int_ish(.9999)
    assert int_ish(sqrt(4))
    assert int_ish(sqrt(1234 ** 2))

if __name__ == '__main__':
    sm = 0
    for dbl_side_length in range(2, 10 ** 6):
        for other in (dbl_side_length - 1, dbl_side_length + 1):
            p = dbl_side_length * 2 + other
            if p > 10 ** 9:
                print(sm)
                exit()
            a = area(dbl_side_length, dbl_side_length, other)
            if int_ish(a):
                print(dbl_side_length, dbl_side_length, other, a)
                sm += p
    print(sm)
