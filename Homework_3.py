# 1
n = int(input())
print([i**3 for i in range(1, n + 1) if n <= 100])
# 2
for i in range(1, 10):
    str = [i * j for j in range(1, 10)]
    for j in range(len(str)):
        if len(str(str[j])) == 1 and j != 8:
            print(f'{str[j]}  ', end='')
        elif len(str(str[j])) != 1 and j != 8:
            print(f'{str[j]} ', end='')
        else:
            print(f'{str[j]}', end='\n')
