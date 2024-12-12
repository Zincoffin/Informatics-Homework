from math import *
#1

def triangle(x):
    b = list(map(int, [x[0], x[1]]))
    c = list(map(int, [x[0], 0]))
    line1 = round(sqrt(pow(b[0], 2) + pow(b[1], 2)))
    line2 = round(sqrt(pow(c[0], 2) + pow(c[1], 2)))
    print(f'длины векторов {line1} и {line2}')
    angle = ((b[0] * c[0] + b[1] * c[1])/(line1 * line2))
    print(f'угол относительно оси абцисс {angle}')
    return angle


pts = [input().split() for i in range(3)]
rez = {}
for i in pts:
    rez.update({triangle(i): i})
print(f'максимальный угол {max(rez.keys())} у точки с координатами {
      rez.get(max(rez.keys()))}')
# 2


def pldrm(n):
    newn = bin(n)[2:]
    if newn == newn[::-1]:
        return newn
    else:
        return ''


n = int(input())
rez = {}
for i in range(n + 1):
    if pldrm(i) != '':
        rez.update({i: pldrm(i)})
print(f'найдено чисел палиндромов {len(rez)}, сами числа {rez}')