#Recursive function for factorials



def fact(n):
    factorial = 1
    if n==0:
        factorial = 1
        return factorial
    else:
        return n * fact(n-1)
    #end if
#end function


validated = False
while not validated:
    try:
        num = int(input("Enter the number you want to find the factiorial of:  "))
    except ValueError:
        print("That wasn't an integer; Try Again!")
        continue
    #end try
    
    if num>0 and num<1000:
        validated = True
        print("factorial of", num, "is", fact(num))
        yesNo = input("Would you like to try a different number? [Yes/No]")
        
        if yesNo == "yes" or yesNo =="Yes":
            validated = False    
        elif yesNo == "No" or yesNo =="no":
            print("Terminating program")
        #end if
    else:
        print("Value you entered must be in the range [1-1000]")
    #end if
#endwhile
    





