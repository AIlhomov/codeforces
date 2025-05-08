s = input()
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
consonants = ['B', 'C','D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
               'T', 'V', 'W', 'X', 'Z']
#print(s[::-1])
lowerVowels = [x.lower() for x in vowels]
lowerConsonants = [x.lower() for x in consonants]

for c in s[::-1]:
    if c in vowels or c in lowerVowels:
        print("YES")
        break
    if c in consonants or c in lowerConsonants:
        print("NO")
        break