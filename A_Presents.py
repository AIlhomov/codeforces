input()

def invert_permutation_list_scan(p):
    return [p.index(i + 1) + 1 for i in range(len(p))]

p = list(map(int, input().split()))

res = invert_permutation_list_scan(p)
print(*res)
    

