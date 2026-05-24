import random
options=('rocks','papers','scissors')
running=True
while running:
    computer=random.choice(options)
    player= input("Enter a choice(rocks,papers,scissors) : ").lower()
    if player not in options:
        print("Enter a valid input")
        continue
    print(f" Player: {player}")
    print(f" Computer: {computer}")
    if player==computer:
        print("It's a tie.")
    elif player=="rocks" and computer=="papers":
        print("You LOSE!")
    elif player=="rocks" and computer=="scissors":
        print("You WIN!")
    elif player=="papers" and computer=="rocks":
        print("You WIN!")
    elif player=="papers" and computer=="scissors":
        print("You LOSE!")
    elif player=="scissors" and computer=="papers":
        print("You WIN!")
    else:
        print("You LOSE!")
        

    play_again= input("PLAY AGAIN (Y/N): ").lower()
    if not play_again=='y':
        running=False

print("THANKS FOR PLAYING")