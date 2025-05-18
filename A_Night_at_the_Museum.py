s = input()
res = 0
#start from a. go to the char
curr = 'a'
for char in s:
    #find the char in the wheel
    dist = abs(ord(char) - ord(curr))
    res += min(dist, 26 - dist)
    curr = char

print(res)