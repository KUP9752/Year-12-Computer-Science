
my_list=[1]

n = int(input("Enter the number to find the nth position in the fibonacci sequence"))
def fib1(n):
    n0 = 0
    n1 =1
    counter = 0
    if n==0:
        return 0
    else:
        while counter<=n:
            if counter<=1:
                counter+=1
            else:
                temp= n0+n1
                n0= n1
                n1 = temp
                counter+=1
                my_list.append(n1)
                
        #end while
    #end if
    return n1
#end function

#other way of using lists and for loop
def fib2(n):
    my_list.append(1)
    for counter in range(2,n):
        my_list.append(my_list[counter-2] + my_list[counter-1])
    #next
    return my_list[n-1]
#end function

#Run fib1 or fib2, they don't work at the same time
print("Number on the nth position is (1st function):", fib1(n))
#print("Number on the nth position is: (2nd function)", fib2(n))
print("All numbers until the nth position are:", my_list)


