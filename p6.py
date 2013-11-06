import sys

def main():
  solution = 0
  sum_squares = 0
  sum = 0
  for i in range(1, 101):
    sq = i*i
    sum_squares = sum_squares + sq
    sum = sum + i 
  square_sum = sum * sum
  solution = square_sum - sum_squares
  print solution 

if __name__ == '__main__':
  main()
