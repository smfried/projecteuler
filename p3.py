import sys
import math

def isprime(num):
  for i in range(2,num):
    result = num/i
    if (result*i) == num:
      return False
  return True

def main():
  solution = 0
  for i in range(1,600851475143):
    if (600851475143%i == 0) and isprime(i):
      solution = i
  print solution

if __name__ == '__main__':
  main()
