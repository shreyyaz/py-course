#WHILE LOOP= execute some code WHILE some condition remains true.
age=int(input("Enter your age: "))
while age<0:
    print("Age can't be negative.")
    age=int(input("Enter your age: "))
print(f"You are {age} years old.")



num=int(input("Enter a number between 1 - 10: "))
while num<1 or num>10:
    print(f"{num} is not valid.")
    num=int(input("Enter a number between 1 - 10: "))
print(f"The number is valid and is equal to: {num}")


#FOR LOOP
for x in range(1,21):  #2nd value is not exclusive
    if x==13:
        break
    else:
        print(x, end=" ")

#NESTED LOOP
rows=int(input("Enter the no of rows: "))
columns=int(input("Enter the no of columns: "))
symbol=input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()
