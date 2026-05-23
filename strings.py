name=input("Enter your full name: ")
print(len(name))

result=name.find("o")
print(f"First occurence of o in {name} is {result}")

result=name.rfind("o")  #Last Occurence
print(f"First occurence of o in {name} is {result}")

name=name.capitalize()  #capitalize the first letter only
print(name)

name=name.upper()
print(name)  #will turn to UPPERCASE

result=name.isdigit()  #only digits
print(result)

result=name.isalpha()  #only isalpha
print(result)

#Similarly Count, Replace


# print(help(str))

#EXERCISE Validate User Input   
username=input("Enter a username: ")

if len(username)> 12:
    print("Your username cant be more than 12 characters.")
elif not username.find(" ")==-1: # elif " " in username:i 
    print("Your username cant contain spaces")
elif not username.isalpha():  
    print("Your username cant contain numbers.")
# Suppose isalpha is true, then you have to run else not the elif one, so we flip the true to false 
else:
    print(f"Welcome {username}")


#INDEXING: accessing elemts of a sequence using []
credit_no="1234-5678-9012-3456"
last_4_digits=credit_no[-4:]
print(last_4_digits)
#Reversing a string
print(credit_no[::-1])

#Email Slicer Program
email=input("Enter your email: ")
#index=email.index("@")
username=email[:email.index("@")]
domain=email[email.index("@")+1 :]
print(f"Your username is {username} and domain is {domain}")



#FORMAT SPECIFIERS = {value:flags} format a value based on what flags are inserted.
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1=3000.14159
price2=-9870.65
price3=1200.34

print(f"Price 1 is ${price1: .2f}")   #round upto 2decimal places only
print(f"Price 2 is ${price2: .2f}")
print(f"Price 3 is ${price3: .2f}")

print(f"Price 1 is ${price1: 15}")  #each value has 15 places to display the value
print(f"Price 2 is ${price2: 15}")
print(f"Price 3 is ${price3: 15}")

print(f"Price 1 is ${price1: 015}")  # padded with 0 and allocated, slightly similar as before
print(f"Price 2 is ${price2: 015}")
print(f"Price 3 is ${price3: 015}")

print(f"Price 1 is ${price1: >15}")  
print(f"Price 2 is ${price2: >15}")  #RIGHT JUSTIFIED, DEFAULT ONE
print(f"Price 3 is ${price3: >15}")

print(f"Price 1 is ${price1: <15}")  
print(f"Price 2 is ${price2: <15}")
print(f"Price 3 is ${price3: <15}")   #LEFT JUSTIFIED

print(f"Price 1 is ${price1: ^15}")  
print(f"Price 2 is ${price2: ^15}")
print(f"Price 3 is ${price3: ^15}")  #CENTER ALIGN


print(f"Price 1 is ${price1:+}")  
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")   #ADD A PLUS SIGN FOR POSiTIVE NO

print(f"Price 1 is ${price1:,}")  
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")  #COMMA SEPARATOR


print(f"Price 1 is ${price1:+,.2f}")  
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}") #THREE FLAGS INSERTED