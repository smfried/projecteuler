import sys
import math

def isprime(num):
  sqrt = math.sqrt(num)
  for i in range(2, int(sqrt)):
    if(num % i == 0):
      return False
  return True

def main():
  #solution = 0
  #is_found = 1

  #skipping 2, special case
  #know 2 is the first prime
  for i in range(3, 10):
    #print i
    isprime(i)

  """
  while(is_found == 1):
    is_found = 0
    solution = solution + 1
  #print solution

  """

if __name__ == '__main__':
  main()
