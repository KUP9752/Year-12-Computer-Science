import json

##-Linear Search-## (WITH NUMBERS ONLY)

def linear_search(list_, data):
    index_data = -1
    i=0
    found = False
    len_list = len(list_)-1
    while i<=len_list and not found:
        if list_[i] == data :
            index_data = i
            found = True
        #end if
        i +=1
    #endwhile
    if i>len_list and not found:
        print("The element you looked for doesn't exist in this list")
    elif index_data != -1:
        print("The first occurance of the element you looked for is in array index:",index_data, "and position:",index_data+1)
    #end if
#end procedure

def binary_search(list_,data):
    index_data = -1
    len_list = len(list_)-1
    start = 0
    end = len_list
    found = False
    while start<=end and not found:
        mid = (start+end)//2
        if list_[mid] == data:
            found = True
            index_data = mid
        else:
            if list_[mid]<data:
                start = mid+1
            else:
                end = mid -1
            #end if
        #end if
    #endwhile
    if not(start<=end) and not found:
        print("The element you are looking for doesn't exist in this list.")
    elif index_data !=-1:
        print("The first occurance of the element you looked for is in array index", index_data,"and position",index_data+1)
    #end if    
#end procedure

def insertion_sort(list_):
    len_list = len(list_)
    for i in range(1,len_list):
        currentVal = list_[i]
        pos = i
        while pos > 0 and list_[pos-1]>currentVal:
            list_[pos] = list_[pos-1]
            pos = pos-1
        #endwhile
        list_[pos] = currentVal
    #next i
    w = open("InsertionSortedList.json",'wt')
    json.dump(list_,w)
    w.close()
    print("Your list is: ",list_)
    print("(it is also copied into the folder called 'InsertionSortedList.json'")
#end procedure

def bubble_sort(list_):
    len_list = len(list_)
    flag = True     #// to show when a swap is made
    i = 0
    while i < (len_list-1) and flag:
        flag = False
        for j in range(0,len_list-i-1):
            if list_[j]>list_[j+1]:
                temp = list_[j]
                list_[j] = list_[j+1]
                list_[j+1] = temp
                flag = True
            #end if
        #next j
        i+=i
    #endwhile
    w = open("BubbleSortedList.json",'wt')
    json.dump(list_,w)
    w.close()
    print("Your list is: ",list_)
    print("(it is also copied into the folder called 'BubbleSortedList.json'")
#end procedure
            
    
        
            
     


algorithm_choice = False

while not algorithm_choice:

    al_ch = input("Would you like to 'search' or 'sort' algorithm? [Press ENTER to exit]")
    
    
    try:
        file = input("Enter the name of the file you wish to take to array from")
        file = file+".json"
        f = open(file,'rt')
        list_ = json.load(f)
        f.close()
    except FileNotFoundError:
       print("That wasn't a valid file in that folder. Try Again.")
       continue
    
    if al_ch in ["SEARCH","search","Search"]:
        data = int(input("Enter the element in the list you are looking for"))
        search_method = False
        while not search_method:
            search_choice = input("Enter if you want the element to be found with linear or binary search (IS THE LIST SORTED?). [Linear/Binary]")
            if search_choice in ["Linear", "linear","LINEAR"]:
                linear_search(list_,data)
                search_method = True
            elif search_choice in ["Binary","binary","BINARY"]:
                choice = input("Are you sure the list is sorted. [Yes/No]")
                if choice in ["yes","Yes","YES"]:
                    binary_search(list_,data)
                    search_method = True
                #end if
            else:
                print("You have entered an incorrect search method. Try Again!")
            #end if
        #endwhile
    elif al_ch in ["Sort","SORT","sort"]:
        sort_method = False
        while not sort_method:
            sort_ch = input("Enter the type of sort you would like to use. [Insertion/Bubble]")
            if sort_ch in ["Insertion","INSERTION","insertion"]:
                  insertion_sort(list_)
                  sort_method = True
            elif sort_ch in ["Bubble","BUBBLE","bubble"]:
                  bubble_sort(list_)
                  sort_method = True
            else:
                  print("You have not entered an incorrect sort method.Try Again?")
    elif al_ch == "":
            print("You wanted to exit.[ENTER to exit]")
            algorithm_choice = True
            
            
    else:
            print("You have not entered 'search' or 'sort'. Try Again!")
            
            

        


            
    
