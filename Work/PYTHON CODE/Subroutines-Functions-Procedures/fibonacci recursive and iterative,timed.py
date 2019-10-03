#iterative
import time

def fibit(n):
    if n <=1:
        return n
    else:
        return fibit(n-1) + fibit(n-2)
    #end if
#end function

def fibrec(n):
    fibNumbers = [0,1] #list of first two Fibonacci numbers
    for i in range(2,n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    #next i
        return fibNumbers[n]
#end function

n = int(input("Enter the index number"))
startTime = time.time()
print(fibit(n))
##print(fibrec(n))
endTime = time.time()
print(endTime-startTime)
