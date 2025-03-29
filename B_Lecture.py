n, m = map(int, input().split())

# n the number of words in the end. like "codeforces contest letter contest"
# m the number of words in each of these languages, thus is (t)

wordsOf2 = {}

for i in range(m):
    s1 = list(map(str, input().split()))
    wordsOf2[s1[0]] = s1[1] 

sList = input().split()

for index in range(len(sList)):
    for key, val in wordsOf2.items():
        # if any of "codeforces contest letter contest" is equal to either "codeforces": OR codesecrof
        if sList[index] == key or sList[index] == val: 
            if len(key) < len(val): # print the first one that he has heard.
                print(key, end=" ")
            elif len(key) == len(val): # print the desired
                print(sList[index], end=" ")
            else:
                print(val, end=" ")
            #print(min(len(key), len(val)), end=" ")

