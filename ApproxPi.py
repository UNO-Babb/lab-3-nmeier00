#ApproxPi.py
#Name: Nick Meier
#Date:February 3, 2025
#Assignment: Lab 3 EC
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3
  decimalPlace = int(input("To how many digits after the decimal point do you want to approximate pi? "))
  while round(approxPi,decimalPlace) != round(realPi,decimalPlace):
    
    print(approxPi)

    approxPi = approxPi + ((sign * 4)/denom)
    sign = sign * -1
    denom = denom + decimalPlace



  end = time.time()

  elapsedTime = end - start
  #print(elapsedTime)
  print(round(approxPi,decimalPlace))

if __name__ == '__main__':
  main()
