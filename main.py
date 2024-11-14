#Simple Calculator
from random import choice

from select import select


def add(x,y):
  return x+y

def substruct(x,y):
        return x-y

def multiply(x,y):
        return x*y

def divide(x,y):
        return x/y

print("Develop a Simple Calculator")
print("Choose an option where add=1, substract=2")

select = int(input("Select operations form 1,2,3,4 :"))

x= int(input("Enter your first number :"))
y= int(input("Enter your second number :"))

if select==1:
        print(x, "+", y, "=",
              add(x, y))
elif select == 2:
        print(x, "-", y, "=", substruct(x,y))

elif select == 3:
        print(x, "*", y, "=", multiply(x,y))

elif select == 4:
        print(x, "/", y, "=", divide(x,y))

else:
        print("Invalid input")





