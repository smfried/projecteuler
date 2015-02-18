large_num = 600851475143

def isprime(num):
	for i in range(2, num-1):
		if(num % i == 0):
			return False
	return True

print isprime(large_num)

# def getfactor():
# 	for i in range(large_num-1, 3, -1):
# 		print i
# 		if large_num % i == 0 and isprime(i):
# 			return i

# print getfactor()