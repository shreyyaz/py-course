#Python Calculator
op=input("Enter an operator: ")
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

if (op=='+'):
    result=a+b
    print(result)
elif(op=='-'):
    result=a+b
    print(result)
elif(op=='*'):
    result=a*b
    print(result)
elif(op=='/'):
    result=a/b
    print(result)
else:
    print(f"The {op} is not a valid operator.")

