import math

#1
radius = int(input())
print(round(2 * math.pi * radius, 2))
print(round(math.pi * math.pow(radius, 2), 2))

#2
x = 10
y = 55
print(x, y)
x, y = y, x
print(x, y)

#3
L = int(input())
g = 9.81
print((2 * math.pi * math.sqrt(float(L) / g), 2))