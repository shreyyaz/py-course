# #dictionary= a collection of {key:value} pairs ordered and changeable. No duplicates
capitals={"USA": "Washington DC", "India":"New Delhi", "China": "Beijing"}
# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("Capital exist")   #NONE IS TREATED AS FALSE
else:
    print("That capital doesnt exist")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})
print(capitals)
print(capitals.pop("China"))   #POP returns the value and removes the key-value pair from dictionary.
print(capitals)
print(capitals.popitem())   
#popitem() returns the ENTIRE key-value pair as a tuple, not just the value. And then removes it.
print(capitals)

capitals.clear()
print(capitals)


print(capitals.keys())
print(capitals.values())

for value in capitals.values():
    print(value)

items=capitals.items()
for key,value in capitals.items():
    print(f"{key}:::::: {value}")

