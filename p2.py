import sys

def main():
  prev = 0
  i = 1
  sum = 0
  while (i < 4000000):
    i = i + prev
    prev = i - prev
    if i%2 == 0:
       sum += i
  print sum

if __name__ == '__main__':
  main()
