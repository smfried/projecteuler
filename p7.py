import math

def isprime(num):
	s = math.sqrt(num)
	c = math.ceil(s)
	sqrt = int(s)
	for i in range(2, sqrt+1):
		if(num % i == 0):
			return False
	return True

count = 1
i = 3

while count < 10001:
	if isprime(i):
		count = count + 1
	i = i + 1

print i - 1