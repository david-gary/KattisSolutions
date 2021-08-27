import sys
vowels = ['a', 'e', 'i', 'o', 'u']
words = []
for i in input().split():
    words.append(i)
for i in words:
    line = ''
    if i[0] in vowels:
        line += (i+'yay')
    
print(line)