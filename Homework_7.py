#1
def read_last(lines, file):
    f = open(file, 'r', encoding='utf-8')
    strs = f.readlines()
    if len(strs) >= n and n > 0:
        for i in strs[len(strs) - lines:]:
            print(i)

n = int(input())
read_last(n, r'/home/zincoffin/wu.txt')
#2
import os

def print_docs(directory):
    use_files = os.walk(directory)
    for i in use_files:
        print(f'в папке {i[0]} лежит \n в {", ".join([papka for papka in i[1]])} \n файлы {", ".join([file for file in i[2]])} \n')
print_docs('/home/zincoffin/wu.txt')
#3
def longest_words(file):
    f = open(file, 'r', encoding='utf-8')
    strs = f.readlines()
    dl = set()
    for i in strs:
        n = i.split()
        dl.add(max(n, key=len))
    if len(dl) > 0: return max(dl, key=len)

print(longest_words('/home/zincoffin/wu.txt'))
#4
def redact():
    file = open(f'{input('введите название файла: ')}.txt', 'w+', encoding='utf-8')
    text = 'пишите содержимое файла'
    print(text)
    while text != '':
        text = input()
        file.write(f'{text} \n')
    file.close()
redact()