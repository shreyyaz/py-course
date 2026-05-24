friends=0
friends+=2  # Augmented Assignment Operator
friends**=3  #exponent
friends/=2
print(friends)

abc=10
print(abc%2)
print(abc//2)

x=3.14
y=-4
z=5
print(round(x)) #Round off to nearest integer
print(abs(y))
print(pow(4,3))
print(max(x,y,z))
x=7.2
import math  #Built in module/library
print(math.pi)
print(math.e) #gives 15 significant digits
print(math.sqrt(x))
print(math.ceil(x))
print(math.floor(x))


import math
a=float(input("Enter side A: "))
b=float(input("Enter side B: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"Side C = {c}")