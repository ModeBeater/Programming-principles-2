from math import tan, pi
n = int(input())
l = int(input())
s = n * (l * l) / (4 * tan(pi / n))
print('The area of the polygon is:', int(s))