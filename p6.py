sum_squares = 0

for i in range(1, 101):
    n = i * i
    sum_squares = sum_squares + n

square_sum = 0

for i in range(1, 101):
    square_sum = square_sum + i

square_sum = square_sum * square_sum

print square_sum - sum_squares
