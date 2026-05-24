import random   #random module 
 #you cannot name the file as random.py bcoz then it will try to import ur made up file, just made this mistake
number=random.randint(1,6)  #both values are mutually exclusive
print(number)

number=random.random() #floating point nos btwn 0 and 1 will not take any args
print(number)

options=('rock',"papers","scissors")
#use the choice function to make choice out of a list/tuple/dict
option=random.choice(options)
print(option)
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# mistake print(random.shuffle(cards))
random.shuffle(cards)
print(cards)

