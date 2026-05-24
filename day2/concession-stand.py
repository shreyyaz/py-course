#Concession stand program
menu={"pizza":3.00,
      "nachos":1.5,
       "soda":2.0,
        "pretzel":1.00 }
cart=[]
total=0
print("-------MENU-------")
#for food in menu:  MISTAKE
#   print(f"{menu.keys()}: ${menu.values()}")

for key, value in menu.items():
    print(f"{key}: ${value}")
    
while True:
    food=input("Enter the food item (q to quit) : ").lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)  #in the cart food items are stored not their prices
    else:
        print("that item is not on the menu")
print("------------------")
print("Your cart: ", end=" ")
for food in cart:
    total+=menu.get(food)  
    #here you will take out the values corresponding to the food items present in cart
    print(food,end=" ")
print()
print("------------------")
print(f"Your total is: $ {total}")
