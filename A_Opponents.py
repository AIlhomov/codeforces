def allCharactersSame(s) :
    if s.count('1') != len(s):
        return False

    return True

n, d = map(int, input().split())
#the number of opponents and the number of days

streak = 0
AllStreaks = []
for i in range(d):
    opp = input()

    if allCharactersSame(opp): #all are 1
        streak = 0
    else:
        streak += 1
    AllStreaks.append(streak)

print(max(AllStreaks))