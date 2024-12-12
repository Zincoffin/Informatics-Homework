import re
#1
text = input()
print(f'новая строчка:{text.replace('н', '!')}, кол-во символов:{len(max(re.findall(r'н+', text)))}')

#2

text = input()
print(text[text.find('(') + 1:text.find(')')])

#3
text = input().lower()
print(re.findall(r'\bа\w+я\b', text))