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
        
            
     

file = input("enter the name of the file you wish to take to array from")
file = file+".json"
f = open(file,'rt')
list_ = json.load(f)
f.close()

data = int(input("Enter the element in the list you are looking for"))
search_method = False
while not search_method:
    search_choice = input("Enter if you want the element to be found with linear or binary search (IS THE LIST SORTED?). [Linear/Binary]")
    if search_choice in ["Linear", "linear","LINEAR"]:
        linear_search(list_,data)
        search_method = True
    elif search_choice in ["Binary","binary","BINARY"]:
        choice = input("Are you sure the list is sorted.[Yes/No]")
        if choice in ["yes","Yes","YES"]:
            #print("Not implemented yet")
            binary_search(list_,data)
            search_method = True
        #end if
    else:
        print("You have entered an incorrect search method.Try Again!")
    #end if
#endwhile 
        


            
    
