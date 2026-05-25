#function = A block of reusable code
# place () after the function name to invoke it
def happy_birthday(name, age):   #POSITION OF ARGUMENTS MATTER
    print(f"Happy birthday to you {name}!")
    print(f"You are {age} years old")
    print()

happy_birthday("john",20)
happy_birthday("steve",69)
happy_birthday(20,"shreyas")


def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last

full_name=create_name("shReyas","singh")
print(full_name)
