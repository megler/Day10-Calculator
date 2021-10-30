# calculator.py
#
# Python Bootcamp Day 10 - Calculator
# Usage:
#      Python calculator
#
# Marceia Egler October 4, 2021


from art import logo
from replit import clear

def add(n1: float, n2: float) ->float:
  return n1 + n2

def subtract(n1: float, n2: float) ->float:
  return n1 - n2

def multiply(n1: float, n2: float) ->float:
  return n1 * n2

def divide(n1: float, n2: float) ->float:
  return n1 / n2


def calculator():
  print(logo)
  is_calculating = True

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }


  n1 = float(input("What is the first number: "))

  for key in operations:
    print(key)

  while is_calculating:
    
    operation_symbol = input("Pick an operation. ")
    n2 = float(input("What is the next number: "))
    answer = operations[operation_symbol](n1,n2)

    print(f"{n1} {operation_symbol} {n2} = {answer}")

    if input(f"Type Y to keep calculating with {answer} or N to start a new calculation. ").lower() == 'y':  
      n1 = answer
      
    else:
      is_calculating = False
      calculator()

calculator()