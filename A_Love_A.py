s = input() 

countA = s.count('a')
countRest = len(s) - countA

if countA > countRest:
    print(len(s))
elif countA == countRest:
    print(countA + countRest - 1)
else:
    restA = countRest - countA

    countA -= restA + 1

    print(countA + countRest)
    pass
