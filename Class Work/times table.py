#Times Table
print('Times table, please enter a number in the range [1,20] for the table.')
run = 1


while run ==1:
    table = int(input('Input Table [1-20]:'))
    if table>0 and table<21:
        rows = int(input("How many rows[1-20]"))
        if rows>1 and rows<21:
            run = 0
            for item in range(1, rows + 1):
                print(item, " x ", table, " = ", item*table)
            print()
            repeat = input("Would you like to use the Times Table Again? [Yes/No]")
            if repeat =="yes" or repeat =="Yes":
                run = 1
            elif repeat == "No" or repeat =="no":
                print("Thanks for using the Times Table")
                print()
            #End if
        
     
        else:
            run = 1
            print("Invalid Input, try again")
        #End if
        
    else:
        run = 1
        print("Invalid Input, try again")
    #End if
    

        



