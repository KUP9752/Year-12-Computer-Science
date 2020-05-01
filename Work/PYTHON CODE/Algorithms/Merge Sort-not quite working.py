list1 = [4,12,18,5,3,1,10,11,2,14]
left =[]
right =[]
def mergesort(list1):
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
mergesort(list1)
print(list1)
