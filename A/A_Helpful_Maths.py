s = input() 

l = s.split("+")

l.sort()

print(*(l), sep="+")