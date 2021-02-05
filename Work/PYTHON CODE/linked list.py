theOrders = [[184, 1],
             [186, 2],
             [185, 3],
             [187, -1],
             [None, 5],
             [None, -1]]

theOrders2 = [[184, 2],
              [186, 3],
              [185, 1],
              [187, -1],
              [None, 5],
              [None, -1]]

sp = 0
nf = 4


def x():
    finished = False
    count = 0
    while not (finished):
        if theOrders[count][1] == -1:
            finished = True
        else:
            output = theOrders[count][0]
            print(output)
            count = theOrders[count][1]
        # end if
    # end while
    output = theOrders[count][0]
    print(output)


# end procedure

def improved_printout(sp, table):

    index = sp
    while index != -1:
        print(table[index][0])
        index = table[index][1]
    # endwhile
#end function

# end procedure


def find_position(sp, table, item):
    index = sp
    try:
        item = int(item)
    except: ValueError

    while index != -1:
        if table[index][0] == item:
            print('item found in index', index)
            return index
        else:
            index = table[index][1]
        #end if
    #end while
    print('item hasnt been found')
#end function

def find_order(sp, table):
    index_list = []
    index = sp
    index_list.append(index)
    while index != -1:
        index = table[index][1]
        index_list.append(index)
    #endwhile
    return index_list

# end function

def deletion(sp, table, item):

    index_list = find_order(sp, table)
    location = find_position(sp, table, item)
    if location == -1:
        return None
    else:
        for i in range(0, len(index_list)):
            if index_list[i] == location:
                position = (index_list[i-1])
                table[position][1] = table[location][1]
                table[location][1] = -1
                print('deletion of item is completed')
                if location == 0:
                    update_sp(1)
                #end if

            #end if
        #next i
    #end if
#end funtion

def insertion(current_index, sp, table, item, order):

    index_list = find_order(sp, table)
    try:
        order = int(order)
    except:
        ValueError
    try:
        item = int(item)
    except:
        ValueError
    if order>len(table):
        print("cant add an item in a position greater than the length of list")
    else:
        table[current_index][0] = item

        temp = table[index_list[order-1]][1]
        table[index_list[order - 1]][1] = current_index
        table[current_index][1] = temp

        update_nf(table)
    if order == 0:
        update_sp(0)
def update_nf(table):
    global nf
    if table[nf+1][0] == None:
        nf = nf+1
    #end if

def update_sp(value):
    global sp
    sp = value

improved_printout(sp, theOrders)
find_position(sp, theOrders, input("enter the iten you want to find"))
print(find_order(sp, theOrders))
print("the originakl list:", theOrders)
deletion(sp, theOrders, input('enter number to be deleted'))
print("updated list after item is deleted:", theOrders)
print("nextfree:", nf)
print("starting pointer:", sp)

insertion(nf, sp, theOrders, input('Enter the item to be inserted'), input('Enter the index of the item in the linked list '))
print(theOrders)
print("nextfree:", nf)
print("starting pointer:", sp)

