t = int(input())

# def cost(num):
#     # What is the minimum number of digits you need to remove from 
#     # the number so that its cost becomes the minimum possible?

#     dic = {}   # stores all numbers removed (key) and all costs (value)

#     for i in range(len(list(num))):
#         minRemoval = i
#         for j in range(len(list(num))):

    
        

for i in range(t):

    s = input()
    
    if s.count('0') == 0:
        print(len(s)-1)
    else:
        #zeroCount = s.count('0')
        #print(zeroCount+1)
        removed_trailing_zeros  = s.rstrip('0')
        diff = len(s) - len(removed_trailing_zeros)
        s1 = s.replace('0', '')
        print(len(s1) + diff-1)

