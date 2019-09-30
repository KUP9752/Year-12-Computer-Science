#Recursive function for factorials

factI=1

def fact(n):
    factorial = 1
    if n==0:
        factorial = 1
        return factorial
    else:
        return n * fact(n-1)
    #end if
#end function
    
print()
print("===Factorial Calculating Program===")
print()

choice = input("Enter the method you want to use: [Iteration/Recursion]")
while not (choice == "Recursion" or choice =="recursion" or choice =="Iteration" or choice == "iteration"):
    choice = input("You didn't enter the correct parameters, try again:")
    

while choice == "Recursion" or choice =="recursion":
    validated = False
    while not validated:
        try:
            num = int(input("Enter the number you want to find the factiorial of:  "))
        except ValueError:
            print("That wasn't an integer; Try Again!")
            continue
        #end try
        
        if num>-1 and num<1000:
            validated = True
            print("factorial of", num, "is", fact(num))
            yesNo = input("Would you like to try a different number? [Yes/No]")
            while not(yesNo == "yes" or yesNo =="Yes" or yesNo == "No" or yesNo =="no"):
                yesNo = input("You didn't enter the correct parameters, try again:")
            #end while
            
            if yesNo == "yes" or yesNo =="Yes":
                validated = False    
            elif yesNo == "No" or yesNo =="no":
                choice = "none"
                print("Terminating program")
                w = input("...")
                
            #end if
        else:
            print("Value you entered must be in the range [1-1000]")
        #end if
    #endwhile
#end while
while choice =="Iteration" or choice == "iteration":
    validated = False
    while not validated:
        try:
            num = int(input("Enter the number you want to find the factiorial of:  "))
        except ValueError:
            print("That wasn't an integer; Try Again!")
            continue
            #end try
        if num>-1 and num<1000:
            validated = True
            for i in range(num,0,-1):
                factI = factI * i
            #next i
            print("factorial of", num, "is", factI)
            factI = 1
            yesNo = input("Would you like to try a different number? [Yes/No]")
            while not(yesNo == "yes" or yesNo =="Yes" or yesNo == "No" or yesNo =="no"):
                yesNo = input("You didn't enter the correct parameters, try again:")
            #end while
            
            if yesNo == "yes" or yesNo =="Yes":
                validated = False    
            elif yesNo == "No" or yesNo =="no":
                choice = "none"
                print("Terminating program")
                w = input("...")
                
            #end if
        else:
            print("Value you entered must be in the range [1-1000]")
        #end if
    #endwhile
#end while

        
        








