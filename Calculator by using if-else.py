a=int(input("Enter the first number-"))
operator=input("""Enter the operator-
                """)
b=int(input("Enter the second number-"))
if operator=="+":
    print("Answer- ",a+b)
elif operator=="-":
    print("Answer- ",a-b)
elif operator=="/":
    print("Answer- ",a/b)
elif operator=="*":
    print("Answer- ",a*b)
else:
    print("error")
