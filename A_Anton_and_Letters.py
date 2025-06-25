s = input()

sFiltered = s.replace('{', '')
sFiltered = sFiltered.replace('}', '')
if sFiltered == '':
    print(0)
else:
    sFiltered = sFiltered.split(', ')
    print(len(set(sFiltered)))

