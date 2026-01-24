import random

l = ["Rock", "Paper", "Scissor"]

while True:
    print("\n0. Rock\n1. Paper\n2. Scissor\n3. EXIT\n")
    com = random.randint(0,2)
    
    try:
        user = int(input("Enter a number between 0 to 3: "))
        
        if user == 3:
            print("GAME OVER")
            break
        
        if user>=0 and user<3:
            if user == com:
                print("DRAWN")
            elif user > com:
                print("User wins, Computer Lose")
            else:
                print("Computer wins, User Lose")
                
            print("\nUser choice:", l[user])
            print("Computer choice:", l[com])
        else:
            print("Please enter a number between 0 and 3")
            
    except ValueError:
        print("Please enter a valid number")