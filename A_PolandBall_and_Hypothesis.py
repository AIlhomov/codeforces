n = int(input()) 

def prime(n): return any(n % i == 0 for i in range(2,n))

for m in range(1, 100):
    if prime((n * m) + 1):
        print(m)
        break