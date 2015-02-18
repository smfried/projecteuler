prod = 2

for i in range(2, 1001):
    prod = prod * 2

string_prod = str(prod)
sum = 0

for i in range(0, len(string_prod)):
    sum = sum + int(string_prod[i])

print sum
