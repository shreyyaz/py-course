fruits=["apple","orange","banana", "coconut"]
vegetables=["tomato","carrots","potatoes"]
meats=["chicken","turkey","fish"]

groceries=[fruits,vegetables,meats]
print(groceries[0][0])

for collection in groceries:   
    for food in collection:
        print(food, end=" ")
    print()

""" for i in range(len(groceries)):
    for j in range(len(groceries[i])):
        print(groceries[i][j], end=" ")
    print()"""