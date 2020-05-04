#i have 2 different programs I tried, the first one I wrote and when I saw that it didn't work I got some help from realpython.org and tried to seperate the merging and the sorting bits but neither worked.
left= []
right=[]
def mergesort1(list1): #I think there was a mutaility problem of the lists in python for this recursion to work
    
    if len(list1)> 1:
        mid = len(list1) //2
        for i in range(0,mid):
            left.append(list1[i])
            
        for i in range(mid,len(list1)):
            right.append(list1[i])
                       
        mergesort(left)
        mergesort(right)

        lp = 0 #left pointer
        rp = 0 #right pointer
        p = 0 #pointer that sorts the original list

    while lp < len(left) and rp<len(right):
        if left[lp] < right[rp]:
            list1[p] = left[lp]
            lp += 1
        elif right[rp]< left[lp]:
            list1[p] = right[rp]
            rp += 1
        p +=1
    #if integer division is not exact and length of either list is longer we need to check that so
    while lp<len(left):
        list1[p] = left[lp]
        lp += 1
        p +=1
    while rp < len(right):
        list1[p] = right[rp]
        rp+=1
        p+=1
    print("Completed pass: ", list1)

        
list1 = [4,12,18,5,3,1,10,11,2,14]

#I kept the merging and the sorting seperate
def create_slist():
    slist = []
    for i in range(len(list1)):
        slist.append(0)
                      
def merge(left,right):
    if len(left) == 0:
        return left
    if len(right) == 0:
        return right

    lp = 0 #left pointer
    rp = 0 #right pointer
    p = 0 #pointer that sorts the original list

    while lp< len(left) and rp < len(right):
        if left[lp]<=right[rp]:
            slist[p] = left[lp]
        else:
            slist[p] = right[rp]

    while lp<len(left):
        slist[p] = left[lp]
        lp += 1
        p +=1
    while rp < len(right):
        slist[p] = right[rp]
        rp+=1
        p+=1
    return slist

#I got some help to get past the mutability problem I had
def mergesort(list1):
    if len(list1)<1:
        return list1

    mid = len(list1)//2

    return merge(left=mergesort(list1[:mid]),right=mergesort(list1[mid:]))

mergesort1(list1)
#maximum recursion reached no matter the length of my list, I dont know waht else to do


    

    
