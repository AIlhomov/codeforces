t = int(input())

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

while t > 0:

    n = int(input())

    a = list(map(int, input().split()))

    counter = 0

    res = ""
    #print(a[0])
    while counter != n:
        counter += 1
        res += str(a[0]) + " "
        a = remove_values_from_list(a, a[0])
        #print(a)
        




        #print(newA)
    print(res)
    t -= 1