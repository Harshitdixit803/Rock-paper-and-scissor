import random
#rock paper and scissors game


computer = random.randint(1,3)
user = input("Your Turn : Choose Rock(r) Paper(p) or Scissor(s)? ->  ").lower()
won="Congratulations, You have won!, Hurray!!!"
lose="You lost... Better luck, try next time."
if user == "r":
    print("You chose : Rock")
elif user == "p":
    print("You chose : Paper")
elif user == "s":
    print("You chose : Scissor")
else:
    print("Please choose from given range")

if user != "r" and user != "s" and user != "p":
    None
else:
    if computer == 1:
        computer= "r"
        print("Computer chose : Rock")
    elif computer == 2:
        computer= "p"
        print("Computer chose : Paper")
    else:
        computer="s"
        print("Computer chose : Scissor")
    
    if user == computer:
        print("The match is tied, try next game.")
    if user == "r":
        if computer == "s":
            print(won)
        elif computer == "p":
            print(lose)
    elif user == "s":
        if computer == "r":
            print(lose)
        elif computer == "p":
            print(won)
    elif user == "p":
        if computer == "r":
            print(won)
        elif computer == "s":
            print(lose) 
           

