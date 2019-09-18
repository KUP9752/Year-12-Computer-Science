#Rock, paper, scissors

#a and b variables just used for loops, so i didn't name them specifically

import random
repeat = 1

while repeat == 1:
    a = str(input("Choose from: Rock, Paper, Scissors   "))
    if not(a =="Rock" or a =="Paper" or a== "Scissors"or a =="rock" or a =="paper" or a== "scissors"):
        print("Invalid input, Please Try Again")
        
    else:
        if a == "rock":
            a = "Rock"
        elif a == "paper":
            a = "Paper"
        elif a == "scissors":
            a = "Scissors"
        
        comp = int(random.randint(1,3))
        #print(comp)
        if comp == 1:
            comp = "Rock"
        elif comp == 2:
            comp = "Paper"
        else:
            comp = "Scissors"
        print()
        print("Player Choice:",a)
        print("Computer Choice:", comp)
        if (a == "Rock" and comp =="Scissors") or (a == "Paper" and comp == "Rock") or (a == "Scissors" and comp =="Paper"):
            print()
            print("===You Win===")
        elif a == comp:
            print()
            print("===You Chose the Same, Draw===")
        else:
            print()
            print("===You Lost===")
        b = 0
        repeat = str(input("Would You like to play again?  Yes/No   "))
        while b ==0:
            if repeat =="Yes" or repeat =="yes":
                b = 1
                repeat = 1
            elif repeat == "NO" or repeat =="no":
                print("Thanks For Playing")
                
                c = input()
                b = 1
            else:
                print("Invalid Input, Please Try Again")
                repeat = str(input("Would You like to play again?  Yes/No   "))
                b=0
        




    
    
