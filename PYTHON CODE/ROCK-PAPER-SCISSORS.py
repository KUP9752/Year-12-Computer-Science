#Rock, paper, scissors
import random
repeat = 1

while repeat == 1:
    a = int(input("Choose from: 1-ROCK, 2-PAPER, 3-SCISSORS   "))
    if not(a ==1 or a ==2 or a==3):
        print("Invalid input, Please Try Again")
        #a = int(input("Choose from: 1-ROCK, 2-PAPER, 3-SCISSORS   "))
    else:
        if a == 1:
            a = "Rock"
        elif a == 2:
            a = "Paper"
        elif a == 3:
            a = "Scissors"
        
        comp = int(random.randint(1,3))
        #print(comp)
        if comp == 1:
            comp = "Rock"
        elif comp == 2:
            comp = "Paper"
        else:
            comp = "Scissors"

        print("Player Choice:",a)
        print("Computer Choice:", comp)
        if (a == "Rock" and comp =="Scissors") or (a == "Paper" and comp == "Rock") or (a == "Scissors" and comp =="Paper"):
            print("===You Win===")
        elif a == comp:
            print("===You Chose the Same, Draw===")
        else:
            print("===You Lost===")
        b = 0
        repeat = int(input("Would You like to play again? 1.Yes, 2.No    "))
        while b ==0:
            if repeat ==1:
                b = 1
            elif repeat == 2:
                print("Thanks For Playing")
                c = input()
                b = 1
            else:
                print("Invalid Input, Please Try Again")
                b=0
        




    
    
