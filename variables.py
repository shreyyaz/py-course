# This is a Comment
print("leaning py from BroCode")

#Variable
first_name= "Shreyas" #This is a string
print(first_name)

print(f"Hello {first_name}") #This is called f-string #PREFER f-strings over the Concatenation property.
print(f"My name is {first_name}.")

print("Hello " + first_name)

#Integers
age=20
quantity=3.5
num_of_students=60
print(f"I am {age} years old.")
print(f"I am buying {quantity} items")
print(f"My class has {num_of_students} students who are almost {age} years old.")
#print("My class has " + num_of_students + "students who are almost " + age + "years old.")
#Cant concatenate integers

gpa=7.6 #This is a float value. NO DOUBLE EXISTS IN PYTHON.
#We dont have to specifically mention the data type before each variable like C. eg: float gpa =7.6
#This is called Dynamic Typing.

is_student = True
if is_student:
    print("You are a student")
else:
    print("Not a student")    #Since true, if executes


     