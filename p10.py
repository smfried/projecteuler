def isprime(n):
	for i in range(2, n-1):
		if (n % i == 0):
			return False
	return True

sum = 2

for i in range(3, 2000000, 2):
	print i
	if isprime(i):
		sum = sum + i

print sum