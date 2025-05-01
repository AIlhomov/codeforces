t = int(input())

while t > 0:
    n = int(input())
    test_list = list(map(int, input().split()))
    
    max_so_far = [0] * n
    max_so_far[0] = test_list[0]
    for i in range(1, n):
        max_so_far[i] = max(max_so_far[i - 1], test_list[i])
    
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + test_list[i]
    
    for k in range(n, 0, -1):
        findBiggest = max_so_far[k - 1]
        res = suffix_sum[k]
        ans = findBiggest
        print(res + ans, end=" ")
    t -= 1
    print()