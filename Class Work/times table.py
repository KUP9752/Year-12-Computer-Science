#Times Table

run = 1
while run ==1:
    table = input('What Table')
    rows = input("How many rows")
    try:
        table = table +1
        
        if int(table)/1 == int(table) and int(rows)/1 ==int(rows):
            run = 2
            table = int(table)
            rows = int(table)
        else:
            run = 1
            print("Invalid input, Please Enter an Integer")
        #End If
    except TypeError:
        
#EndWhile

for item in range(1, rows + 1):
    print(item, " x ", table, " = ", item*table)
