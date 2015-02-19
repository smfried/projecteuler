import math

large_num = 600851475143

def isprime(num):
	s = math.sqrt(num)
	c = math.ceil(s)
	sqrt = int(s)
	for i in range(2, sqrt+1):
		if(num % i == 0):
			return False
	return True

sqrt = math.sqrt(large_num)
ceil = math.ceil(sqrt)
int_sqrt = int(sqrt)

for i in range(int_sqrt, 3, -1):
	if large_num % i == 0 and isprime(i):
		print i