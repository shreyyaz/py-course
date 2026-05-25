# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)
for item in reversed(numbers):
    print(item, end=" - ")
    print()
print("=======================")
numbers = (1, 2, 3, 4, 5)
for item in numbers:
    print(item)
    print()
print("=======================")

numbers = {1, 2, 3, 4, 5}
for item in numbers:
    print(item)  # SETS are not REVERSABLE
    print()
print("=======================")
# LIST, TUPLE, SETS. STRINGS are iterable



my_dict={"A":1,"B":2,"C":3}
for x,y in my_dict.items():
    print(f"{x}:{y}")