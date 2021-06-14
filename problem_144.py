last_pt = (0, 10.1)
next_pt = (1.4, -9.6)

d = (next_pt[0] - last_pt[0], next_pt[1] - last_pt[1])

# Where does this slope + point intersect the curve?
# y - y_1 = m(x - x_1)
# 4x^2 + y^2 = 100

# x = (-2 sqrt(-a^2 + 2 a b c - b^2 (c^2 - 25) + 100) - a b + b^2 c)/(b^2 + 4)
# and y = (-2 b sqrt(-a^2 + 2 a b c - b^2 (c^2 - 25) + 100) + 4 a - 4 b c)/(b^2
# + 4) and b^2 + 4!=0

'''
4x^2 + y^2 = 100
y^2 = 100 - 4x^2
y = sqrt(100 - 4x^2)
y = -sqrt(100 - 4x^2)


y - y_1 = m(x - x_1)
y = m(x - x_1) + y_1


m(x - x_1) + y_1 = sqrt(100 - 4x^2)
0 = sqrt(100 - 4x^2) - mx + mx_1 - y_1

'''
print(d)
