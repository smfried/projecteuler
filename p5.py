import sys

#between 10000 and 998001
def ispalindrome(num):
  #num = str(num)
  if(num < 100000):
    num = str(num)
    if((num[0]==num[4]) and (num[1]==num[3])):
      return True
    else:
      return False
  elif (num > 100000):
    num = str(num)
    if((num[0]==num[5]) and (num[1]==num[4]) and (num[2]==num[3])):
      return True
    else:
      return False

def main():
  solution = 0
  for i in range(100, 999):
    for j in range(100, 999):
      product = i*j
      if(ispalindrome(product)):
        solution = product
  print solution


if __name__ == '__main__':
  main()  
