k2, k3, k5, k6 = map(int,input().split())

findMin256 = min([k2, k5, k6])
k2 -= findMin256
findMin32 = min([k3, k2])

print((findMin256 * 256) + (findMin32 * 32))