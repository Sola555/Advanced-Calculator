#ask user for number
import os
import time





#function for factorial:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)



def calculate():
  print("1 : multiply")
  print("2 : divide")
  print("3 : add")
  print("4 : subtract")
  print("5 : power")
  print("6 : factorial *")
  print("7 : square roots ")
  print("8 : cube roots")
  print("9 : roots ")
  print("10 : convert fraction into decimal ^")
  print("* indicates that it will only take the first number")
  print("^ indicates that the first number will be the numerator and the second number will be the denominator")
  bedmas = input("Type a number according to the legend above : ")
  value1 = int(input("What is your first number? :"))
  value2 = int(input("What is your second number? :"))

  if bedmas == "1":
      os.system("clear")
      answer = str(value1*value2)
      print("{0} times {1} is {2}.".format(value1,value2,answer))
      print("")
      x = input("press enter to clear the screen and calculate again")
  if bedmas == "2":
      os.system("clear")
      answer = str(value1/value2)
      print("{0} divided by {1} is {2}.".format(value1,value2,answer))
      print("")
      x = input("press enter to clear the screen and calculate again")
  if bedmas == "3":
      os.system("clear")
      answer = value1+value2
      print("{0} plus {1} is {2}.".format(value1,value2,answer)) 
      print("")
      x = input("press enter to clear the screen and calculate again")
  if bedmas == "4":
      os.system("clear")
      answer = value1-value2
      print("{0} minus {1} is {2}.".format(value1,value2,answer)) 
      print("")
      x = input("press enter to clear the screen and calculate again")
  if bedmas == "5":
      os.system("clear")
      answer = value1**value2
      print("{0} to the power of {1} is {2}.".format(value1,value2,answer))
      print("")
      x = input("press enter to clear the screen and calculate again")
  if bedmas == "6":
    os.system("clear")
    answer1 = factorial(value1)
    print("The factorial of {} is {}.".format(value1, answer1))
    print("")
    x = input("press enter to clear the screen and calculate again")
  if bedmas == "7":
    os.system("clear")
    sqrt = value1 ** 0.5
    print(f"The square root of {value1} is {sqrt}")
    print("")
    x = input("press enter to clear the screen and calculate again")
  if bedmas == "8":
    os.system("clear")
    sqrt = value1 ** (1./3)
    print(f"The cube root of {value1} is {sqrt}")
    print("")
    x = input("press enter to clear the screen and calculate again")    
  if bedmas == "9":
    os.system("clear")
    x = 1/value2
    sqrt = value1 ** x
    print(f"The {value2} root of {value1} is {sqrt} ")
    print("")
    x = input("press enter to clear the screen and calculate again")
  if bedmas == "10":
    answer = value1/value2
    os.system("clear")
    print(f"{value1}/{value2} is {answer}")
    print("")
    x = input("press enter to clear the screen and calculate again")
  if not x:
    os.system("clear")
    calculate()

calculate()