vowels =  ["A", "O", "Y", "E", "U", "I", "a", "o", "y", "e", "u", "i"]

s = input()

for c in s:
    if c in vowels:
        continue
    else:
        print(".", c.lower(), end="", sep="")