n = int(input())

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

for i in range(n):
    s = input()
    s2 = rreplace(s, "us", "i", 1)
    print(s2)