#Calculater without using if-else statement.
def add (a,b):
    return(a+b)
def subtract (a,b):
    return(a-b)
def multiply (a,b):
    return(a*b)
def divide (a,b):
    return(a/b)
operations={"+":add,"-":subtract,"*":multiply,"/":divide}

a=float(input("Enter First Number-> "))
operators=(input("Enter the Operator(+,-,*,/)-> "))
b=float(input("Enter Second Number-> "))

result=operations.get(operators,lambda a,b:"Invalive Operator")(a,b)
print("The Answer will be-> ",result)
