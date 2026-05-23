#Typecasting: converting a variable from one data type to other, str(), float(), int(), bool()
name="Shreyas"
name1=""
age=20
gpa= 7.6

is_student=True
print(type(name))
print(type(age))

print(type(str(age)))
print(age)


age=float(age) #We are using the type cast function of float
print(age)
print(type(age))


gpa=int(gpa)
print(type(gpa))
print(gpa)

name=bool(name)
print(name)
name1=bool(name1)
print(name1) #This is true because name=Shreyas is not empty, otherwise bool returns False