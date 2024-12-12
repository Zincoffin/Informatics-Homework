from random import sample, randint
# 1
m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(m):
    brr = list()
    for j in range(n):
        brr.append(randint(-10, 10))
    arr.append(brr)
print(arr)
summ = {}
for i in arr:
    summ.update({sum(i):i})
print(f'максимальная сумма {max(summ.keys())} у строчки {summ.get(max(summ.keys()))}')
print(f'минимальная сумма {min(summ.keys())} у строчки {summ.get(min(summ.keys()))}')
# 2
m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(n):
    brr = sample(range(-30, 30), m)
    arr.append(brr)
print(arr)
for i in arr:
    if i[i.index(min(i))] % 2 == 0:
        i[i.index(min(i))] = 0
    else:
        i[i.index(min(i))] = 1
print(arr)