#TempConvert.py
#Name:Nick Meier
#Date:February 3 2025
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature

  tempF = float(input("Enter temperature in Farenheit:"))

  #Convert that temperature to celsius, rounding to 1 decimal percision

  tempC = ((tempF-32))*(5/9)
  tempC = round(tempC,1)

  #Output converted temperature.

  print(tempF, "degrees farenheit is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
