k, n, w = map(int, input().split())
# w = bananas
# He has to pay k dollars for the first banana4
# 2k dollars for the second one and so on
# he has to pay i·k dollars

cost = 0

for i in range(1, w+1):
    cost += i * k
print(max(0,cost - n))