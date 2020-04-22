##Merging Lists

list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
mergeList = [ ]
#Lists already sorted

for index in range(0, 10):
    mergeList.append(list1[index])
#next index

len2 = len(list2)
counter = 0

for index in range(0, len2):
    while mergeList[counter]<=list2[index]:
        counter += 1
    #endwhile
    temp = mergeList[counter]
    mergeList[counter] = list2[index]
    mergeList.insert(counter+1, temp)
#next index

print(list1, list2, mergeList)
