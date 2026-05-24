#input() A function that prompts the user to enter data. 
#Returns the entered data as a string

name=input("What is your name?: ")
age=int(input("How old are you? ")) #Converting age from string to directly integer in this step only
print(f"Hello {name}")
print(f"You are {age} years old")



#Exercise 1 Area of Rectangle
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
area=length*width #multiplication is allowed now, as both are float
print(f"The area is: {area} cm².") 
#For SUPERSCRIPT: Make sure Numlock On, ALT +0178  ; Control+Command+Space in Macbook

# #How to COMMENT EVERYTHING: Ctrl + /, for uncomment also same

#Exercise 2 Shopping Cart Program
item=input("what item would you like to buy?: ")
price=float(input("What is the price?: "))
quantity=int(input("How many would you like?: "))
total=price*quantity
print(f"You have brought {quantity} x {item}/s")
print(f"Your total is {total}Rs")