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
#end procedure
        

file = input("enter the name of the file you wish to take to array from")
file = file+".json"
f = open(file,'rt')
list_ = json.load(f)
f.close()


data = int(input("Enter the element in the list you are looking for"))

linear_search(list_,data)

        


            
    
