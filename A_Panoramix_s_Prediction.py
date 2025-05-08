n, m = map(int, input().split())

def is_prime(n):
	for i in range(2,n):
		if (n%i) == 0:
			return False
	return True
flag = False
while True:
	if n == m+1:
		break
	n += 1
	if is_prime(n) and n == m:
		print("YES")
		flag = True
		break
	if is_prime(n):
		break
	
if not flag:
	print("NO")
