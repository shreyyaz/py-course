import random
low = 1
high = 100
guesses= 0
answer=random.randint(1,100)
while True:
    guess= input(f"Enter a number between {low} - {high}: ")
    # guess= int(input(f"Enter a number between {low} - {high}: "))
    #bcoz need a normal input, for the else block.
    if guess.isdigit():
        guess=int(guess)
        # mistake guess=guess.int()
        guesses+=1 #mistake guesses=+1
        if guess<low or guess>high:
            print("Your guess is out of range")
        elif guess < answer:
            print("Your guess is too low.")
        elif guess > answer:
            print("Your guess is too high.")
        else:
            print(f"CORRECT! - You guessed the answer: {answer}") 
            print(f"You took {guesses} guesses.")
            break  # YOU FORGOT BREAK STATEMENT
    else:
        print("Please enter a valid input.")
