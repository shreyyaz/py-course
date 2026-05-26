#LIST COMPREHENSION = A concise way to create lists
# Use this method: [what to print for value in iterable if condition]
doubles=[num*2 for num in range(1,11)]
print(doubles)

#SAME AS
# doubles=[]
# for x in range(1,11):
#     doubles.append(x*2)
# print(doubles)

squares=[num*num for num in range(1,11)]
print(squares)

numbers=[1,2,3,4,5,6,7,8,9,10,-3,-7,9]
positive_nos=[num for num in numbers if num>=0]
print(positive_nos)
negative_nos=[num for num in numbers if num<0]
print(negative_nos)


fruits=["apple","banana","mango","pineapple"]
initial_letter=[fruit[0] for fruit in fruits]
print(initial_letter)
upper_case=[fruit.upper() for fruit in fruits]  #NOT fruits.upper()
print(upper_case)