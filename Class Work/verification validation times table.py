#times table with integer type check



answer = "n"

while answer =="n": #Verification loop
    table = -1
    while table < 1 or table>20: #Valid Range check
        table = input('What Table[1-20]:')
        if table.isdigit(): #Valid integer check
            table = int(table)
        else:
            table = -1
            print("That wasn't an integer; Try again!")
        #end if
    #end while
    answer = input("Did you mean[Y/N]:" + str(table)).lower() == "y"
#end while

verified = False
while not verified:
    validated = False
    while not validated:
        try:
            rows = int(input("How many rows [1-20]:")
        except ValueError:
            print("That wasn't an integer: Try Again!")
            continue
        #end try
        if rows not in range(1, 21):
            print("Value out of range")
        else:
            validated = True
        #end if
    #end while
    if input("Did you mean[Y/N]: " + str(rows)).lower() == "y":
        verified = True


