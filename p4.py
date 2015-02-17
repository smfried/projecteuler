def ispalindrome(n):
	length = len(n);
	for i in range(0, length/2):
		if n[i] != n[length-i-1]:
			return False
	return True

largest_palindrome = 0

for i in range(100, 999):
	for j in range(i, 999):
		prod = i * j
		if ispalindrome(str(prod)) and prod > largest_palindrome:
			largest_palindrome = prod

print largest_palindrome