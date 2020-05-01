#Merging two SORTED LISTS of any length
list1 = [1,3,6,8,9]
list2 = [5,7,8,10]
slist = []

p1 = 0 #--pointer for list1
p2 = 0 #--pointer for list2

print('First Sorted List = ', list1)
print('Second Sorted List = ',list2)
swap = 0
done = False
while not done:     #--All if statements check if both lists contain enough numbers to be checked with each other(if lists are different lengths this solves that problem)
    slen = len(slist)
    if p1<len(list1) and p2<len(list2) and list1[p1] == list2[p2]: #--if both lists contain the same item it places them together
        slist.append(list1[p1])
        slist.append(list2[p2])
        p1 +=1 #--both pointers for both lists are incremented as they have an item with the same value
        p2 +=1
        
    if list1[p1] < list2[p2] and p1<len(list1) and p2<len(list2): #--if list1 contains a smaller number it places before the item from list2
        slist.append(list1[p1]) #--sorted list is updated
        p1 +=1 #--pointer is incremented
        swap += 1
        
    if  p1<len(list1) and p2<len(list2) and list2[p2] < list1[p1] :#-- if list2 contains a smaller number this if statement places that item in the sorted list
        slist.append(list2[p2])
        p2+=1
        swap += 1
    #-- Next 2 if statements are for checking if the lists are different lengths and if one pointer already finished checking one of the lists
        
    if p2 == len(list2) and p1<len(list1):
        slist.append(list1[p1])
        p1 +=1
    if p1 == len(list1) and p2<len(list2):
        slist.append(list2[p2])
        p2+=1

    #-- Checks if both pointers have finished their respected lists and concludes the merge sort
    if p1 == len(list1) and p2 == len(list2):
        done = True

print('Final Merged Sorted List = ',slist)
print(swap)        
