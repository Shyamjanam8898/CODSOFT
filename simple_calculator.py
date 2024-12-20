def add(x,y):
    return x + y

def subtarct(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y==0:
        return "Not Define"
    else:
        return x / y
    
def mod(x,y):
    return x % y

def calculator():
    print("Welcome to Simple Calculator!!")
    num1=float(input("Enter first number: ")) #taking input from the user
    num2=float(input("Enter second number: ")) # showing operation list
    
    print("select operation:")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.modulus")
    
    operation=int(input("Enter the operation number: "))  #taking opration values
    
    if(operation==1):
        print(f"Addition of {num1} and {num2} is {add(num1,num2)}")
    elif (operation==2):
        print(f"Substraction of {num1} and {num2} is {subtarct(num1,num2)}")
    elif (operation==3):
        print(f"Multiplication of {num1} and {num2} is {multiplication(num1,num2)}")
    elif (operation==4):
        print (f"Division of {num1} and {num2} is {division(num1,num2)}")
    elif (operation==5):
        print(f"Modulus of {num1} and {num2} is {mod(num1,num2)}")
    else:
        print("Invalid input operation. Please enter valid operation number")
calculator()                                   #calling function calculator