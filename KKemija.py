message = input()
corrected = ""
letter = 0
vowels = ['a', 'e', 'i', 'o', 'u']
while letter < len(message):
    if message[letter] in vowels:
        letter += 2
    corrected += message[letter]
    letter += 1
print(corrected)