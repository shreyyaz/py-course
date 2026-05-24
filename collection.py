#Collection : Single Variable used to store multiple values
# LIST = [] ordered and changeable. DUPLICATES OK
# Set= {} unordered and immutable, but add/remove ok. no duplicates
# Tuple = () ordered and unchangeable/ Duplicates OK FASTER

fruits=['apple', 'banana', "mango"]
print(fruits[0])  #LIST 

fruits=('apple', 'banana', "mango")
print(fruits[1]) # TUPLE, but then also have to use sq brackets to access items.


fruits={'apple', 'banana', "mango"}
print(fruits[0])

for fruit in fruits:
    print(fruit)

fruits.append("pineapple")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.insert(1,"coconut")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.index("banana")
print(fruits)

fruits.count("banana")
print(fruits)

fruits.clear()
print(fruits)


fruits={'apple', 'banana', "mango"}
print(len(fruits))
print(dir(fruits))
print(help(fruits))